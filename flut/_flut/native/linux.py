import ctypes
import ctypes.util
import logging
import os
import json
import collections
import asyncio
import heapq
from ctypes import (
    c_void_p,
    c_char_p,
    c_int,
    CFUNCTYPE,
    c_size_t,
    CDLL,
    POINTER,
    c_uint,
    c_uint64,
    c_long,
)

from .native import FlutNative

logger = logging.getLogger(__name__)

c_ssize_t = c_long

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PATH_FLUT_BUNDLE = os.path.join(
    ROOT_DIR,
    ".flutter",
    "build",
    "linux",
    FlutNative._get_arch(),
    "release",
    "bundle",
)

PATH_LIB = os.path.join(PATH_FLUT_BUNDLE, "lib")
PATH_DATA = os.path.join(PATH_FLUT_BUNDLE, "data")
PATH_FLUTTER_LIB = os.path.join(PATH_LIB, "libflutter_linux_gtk.so")
PATH_FLUT_ASSETS = os.path.join(PATH_DATA, "flutter_assets")
PATH_FLUT_ICU = os.path.join(PATH_DATA, "icudtl.dat")
PATH_FLUT_AOT = os.path.join(PATH_LIB, "libapp.so")

_gtk_lib = ctypes.util.find_library("gtk-3")
if not _gtk_lib:
    try:
        gtk = CDLL("libgtk-3.so.0")
    except OSError:
        gtk = None
else:
    gtk = CDLL(_gtk_lib)

_gobject_lib = ctypes.util.find_library("gobject-2.0")
if not _gobject_lib:
    try:
        gobject = CDLL("libgobject-2.0.so.0")
    except OSError:
        gobject = None
else:
    gobject = CDLL(_gobject_lib)

_glib_lib = ctypes.util.find_library("glib-2.0")
if not _glib_lib:
    try:
        glib = CDLL("libglib-2.0.so.0")
    except OSError:
        glib = None
else:
    glib = CDLL(_glib_lib)

try:
    libc = CDLL("libc.so.6")
except OSError:
    libc = None


if not gtk or not gobject:
    logger.error("GTK 3 or GObject 2.0 libraries not found. Linux support may fail.")

GType = c_size_t

GTK_WINDOW_TOPLEVEL = 0

G_IO_IN = 1
G_IO_OUT = 4
G_IO_PRI = 2
G_IO_ERR = 8
G_IO_HUP = 16

EFD_NONBLOCK = 0x800
EFD_CLOEXEC = 0x80000

GCallback = CFUNCTYPE(None, c_void_p, c_void_p)
GDeleteEventCallback = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)

GUnixFDSourceFunc = CFUNCTYPE(c_int, c_int, c_uint, c_void_p)


GSourceFunc = CFUNCTYPE(c_int, c_void_p)


class GLibAsyncBridge:
    def __init__(self):
        self._loop = None
        self._eventfd = -1
        self._fd_source_id = 0
        self._io_source_id = 0
        self._timer_source_id = 0
        self._next_deadline = float("inf")
        self._fd_callback = None
        self._io_callback_ref = None
        self._timer_callback = None
        self._original_write_to_self = None
        self._selector = None
        self._selector_fd = -1

    def setup(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop

        if not libc:
            raise RuntimeError("libc not available")
        if not glib:
            raise RuntimeError("glib not available")

        libc.eventfd.argtypes = [c_uint, c_int]
        libc.eventfd.restype = c_int
        self._eventfd = libc.eventfd(0, EFD_NONBLOCK | EFD_CLOEXEC)
        if self._eventfd < 0:
            raise RuntimeError("Failed to create eventfd")

        libc.write.argtypes = [c_int, c_void_p, c_size_t]
        libc.write.restype = c_ssize_t
        libc.read.argtypes = [c_int, c_void_p, c_size_t]
        libc.read.restype = c_ssize_t

        eventfd = self._eventfd
        bridge = self

        self._original_write_to_self = loop._write_to_self
        original_write = self._original_write_to_self

        def hooked_write_to_self():
            original_write()
            buf = ctypes.c_uint64(1)
            libc.write(eventfd, ctypes.byref(buf), 8)

        loop._write_to_self = hooked_write_to_self

        def fd_callback(fd, condition, user_data):
            buf = ctypes.c_uint64(0)
            libc.read(fd, ctypes.byref(buf), 8)
            return 1

        self._fd_callback = GUnixFDSourceFunc(fd_callback)
        glib.g_unix_fd_add.argtypes = [c_int, c_uint, GUnixFDSourceFunc, c_void_p]
        glib.g_unix_fd_add.restype = c_uint
        self._fd_source_id = glib.g_unix_fd_add(
            self._eventfd, G_IO_IN, self._fd_callback, None
        )

        self._selector = getattr(loop, "_selector", None)
        if self._selector is not None:
            self._selector_fd = self._selector.fileno()
            selector = self._selector
            bridge = self

            def io_callback(fd, condition, user_data):
                events = selector.select(0)
                loop._process_events(events)
                bridge._io_source_id = 0
                return 0

            self._io_callback_ref = GUnixFDSourceFunc(io_callback)
            self._register_io_source()

        def timer_callback(user_data):
            buf = ctypes.c_uint64(1)
            libc.write(eventfd, ctypes.byref(buf), 8)
            bridge._timer_source_id = 0
            bridge._next_deadline = float("inf")
            return 0

        self._timer_callback = GSourceFunc(timer_callback)
        return self._eventfd

    def _register_io_source(self):
        if self._selector is None or self._io_source_id > 0:
            return
        glib.g_unix_fd_add.argtypes = [c_int, c_uint, GUnixFDSourceFunc, c_void_p]
        glib.g_unix_fd_add.restype = c_uint
        self._io_source_id = glib.g_unix_fd_add(
            self._selector_fd, G_IO_IN, self._io_callback_ref, None
        )

    def re_register_io_source(self):
        self._register_io_source()

    def schedule_next_timer(self):
        self._next_deadline = float("inf")

        if self._timer_source_id > 0:
            glib.g_source_remove.argtypes = [c_uint]
            glib.g_source_remove.restype = c_int
            glib.g_source_remove(self._timer_source_id)
            self._timer_source_id = 0

        if not self._loop._scheduled:
            return

        for handle in self._loop._scheduled:
            if not handle._cancelled:
                when = handle._when
                break
        else:
            return

        delay_ms = max(1, int((when - self._loop.time()) * 1000))
        glib.g_timeout_add.argtypes = [c_uint, GSourceFunc, c_void_p]
        glib.g_timeout_add.restype = c_uint
        self._timer_source_id = glib.g_timeout_add(delay_ms, self._timer_callback, None)
        self._next_deadline = when

    def cleanup(self):
        if self._loop and self._original_write_to_self:
            self._loop._write_to_self = self._original_write_to_self

        glib.g_source_remove.argtypes = [c_uint]
        glib.g_source_remove.restype = c_int
        if self._timer_source_id > 0:
            glib.g_source_remove(self._timer_source_id)
            self._timer_source_id = 0
        if self._io_source_id > 0:
            glib.g_source_remove(self._io_source_id)
            self._io_source_id = 0
        if self._fd_source_id > 0:
            glib.g_source_remove(self._fd_source_id)
            self._fd_source_id = 0

        if self._eventfd >= 0:
            libc.close.argtypes = [c_int]
            libc.close.restype = c_int
            libc.close(self._eventfd)
            self._eventfd = -1


class FlutLinuxNative(FlutNative):
    def __init__(self):
        self._running = False
        self.libflutter = None
        self._native_callback = None
        self._last_buffer = None
        self._window = None
        self._close_error = None
        self._close_requested = False
        self._notify_keepalive = []
        self._notify_acked = 0

    def initialize(self):
        if not os.path.exists(PATH_FLUTTER_LIB):
            raise FileNotFoundError(
                f"libflutter_linux_gtk.so not found at: {PATH_FLUTTER_LIB}\n"
                "Please run: cd flut/.flutter && flutter build linux"
            )

        self.libflutter = CDLL(PATH_FLUTTER_LIB)

        if gtk:
            gtk.gtk_init(None, None)

    def setup_call_dart(self, callback_addr):
        DART_CALL_CALLBACK = CFUNCTYPE(c_void_p, c_char_p)
        dart_fn = DART_CALL_CALLBACK(callback_addr)

        def call_dart_impl(call_type, data):
            try:
                req = json.dumps({"type": call_type, "data": data})
                req_bytes = req.encode("utf-8")
                result_ptr = dart_fn(req_bytes)
                if result_ptr == 0 or result_ptr is None:
                    return None
                result_str = ctypes.string_at(result_ptr).decode("utf-8")
                return json.loads(result_str)
            except Exception as e:
                logger.error("Error calling Dart: %s", e)
                return None

        return call_dart_impl

    def setup_notify_dart(self, callback_addr):
        DART_NOTIFY_CALLBACK = CFUNCTYPE(None, c_char_p)
        dart_fn = DART_NOTIFY_CALLBACK(callback_addr)

        def notify_dart_impl(data_bytes):
            try:
                self._notify_keepalive.append(data_bytes)
                dart_fn(data_bytes)
            except Exception as e:
                logger.error("Error notifying Dart: %s", e)

        return notify_dart_impl

    def _setup_flutter(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        async_mode: bool = False,
        show_window: bool = True,
    ):
        if not self.libflutter:
            self.initialize()

        if not os.path.exists(flutter_asset_path):
            raise FileNotFoundError(f"Assets path not found: {flutter_asset_path}")

        mode_str = " (async mode)" if async_mode else ""

        def on_native_callback(request_ptr):
            try:
                if not request_ptr:
                    return 0
                req_str = ctypes.string_at(request_ptr).decode("utf-8")
                req_json = json.loads(req_str)
                result_bytes = method_call_handler(req_json)
                if result_bytes:
                    self._last_buffer = ctypes.create_string_buffer(result_bytes)
                    return ctypes.addressof(self._last_buffer)
                return 0
            except Exception as e:
                logger.error("Error in on_native_callback: %s", e)
                return 0

        NativeCallbackType = CFUNCTYPE(c_void_p, c_char_p)
        self._native_callback = NativeCallbackType(on_native_callback)
        callback_addr = ctypes.cast(self._native_callback, c_void_p).value

        self.libflutter.fl_dart_project_new.restype = c_void_p
        project = self.libflutter.fl_dart_project_new()

        self.libflutter.fl_dart_project_set_assets_path.argtypes = [c_void_p, c_char_p]
        self.libflutter.fl_dart_project_set_assets_path(
            project, flutter_asset_path.encode("utf-8")
        )

        icu_path = PATH_FLUT_ICU
        if os.path.exists(icu_path):
            self.libflutter.fl_dart_project_set_icu_data_path.argtypes = [
                c_void_p,
                c_char_p,
            ]
            self.libflutter.fl_dart_project_set_icu_data_path(
                project, icu_path.encode("utf-8")
            )

        aot_path = PATH_FLUT_AOT
        if os.path.exists(aot_path):
            try:
                self.libflutter.fl_dart_project_set_aot_library_path.argtypes = [
                    c_void_p,
                    c_char_p,
                ]
                self.libflutter.fl_dart_project_set_aot_library_path(
                    project, aot_path.encode("utf-8")
                )
            except AttributeError:
                pass

        arg1 = f"--native-callback={callback_addr}"
        argv = [arg1.encode("utf-8")]

        argv_c = (c_char_p * (len(argv) + 1))()
        argv_c[0] = argv[0]
        argv_c[1] = None

        self.libflutter.fl_dart_project_set_dart_entrypoint_arguments.argtypes = [
            c_void_p,
            POINTER(c_char_p),
        ]
        self.libflutter.fl_dart_project_set_dart_entrypoint_arguments(project, argv_c)

        self.libflutter.fl_view_new.argtypes = [c_void_p]
        self.libflutter.fl_view_new.restype = c_void_p
        fl_view = self.libflutter.fl_view_new(project)

        gtk.gtk_window_new.argtypes = [c_int]
        gtk.gtk_window_new.restype = c_void_p
        window = gtk.gtk_window_new(GTK_WINDOW_TOPLEVEL)
        self._window = window

        gtk.gtk_window_set_default_size.argtypes = [c_void_p, c_int, c_int]
        gtk.gtk_window_set_default_size(window, width, height)

        gtk.gtk_window_set_title.argtypes = [c_void_p, c_char_p]
        gtk.gtk_window_set_title(window, title.encode("utf-8"))

        gtk.gtk_window_set_default_icon_from_file.argtypes = [
            c_char_p,
            POINTER(c_void_p),
        ]
        gtk.gtk_window_set_default_icon_from_file.restype = c_int

        gtk.gtk_window_set_icon_from_file.argtypes = [
            c_void_p,
            c_char_p,
            POINTER(c_void_p),
        ]
        gtk.gtk_window_set_icon_from_file.restype = c_int

        def try_set_icon(candidate):
            error = c_void_p()
            ok = gtk.gtk_window_set_default_icon_from_file(
                candidate.encode("utf-8"),
                ctypes.byref(error),
            )
            if not ok:
                if error.value and glib is not None:
                    glib.g_error_free.argtypes = [c_void_p]
                    glib.g_error_free.restype = None
                    glib.g_error_free(error)
                return False

            error = c_void_p()
            ok = gtk.gtk_window_set_icon_from_file(
                window,
                candidate.encode("utf-8"),
                ctypes.byref(error),
            )
            if ok:
                return True
            if error.value and glib is not None:
                glib.g_error_free.argtypes = [c_void_p]
                glib.g_error_free.restype = None
                glib.g_error_free(error)
            return False

        with self._use_default_icon_path() as default_icon_path:
            candidates = []
            if icon_path is not None:
                candidates.append(icon_path)
            if default_icon_path is not None and default_icon_path not in candidates:
                candidates.append(default_icon_path)

            for candidate in candidates:
                if try_set_icon(candidate):
                    break
                if candidate != default_icon_path and default_icon_path is not None:
                    logger.warning(
                        "Failed to load icon %s. Falling back to packaged icon.",
                        candidate,
                    )
            else:
                if icon_path is not None:
                    raise RuntimeError(f"Failed to load icon: {icon_path}")

        gtk.gtk_container_add.argtypes = [c_void_p, c_void_p]
        gtk.gtk_container_add(window, fl_view)

        if show_window:
            gtk.gtk_widget_show_all.argtypes = [c_void_p]
            gtk.gtk_widget_show_all(window)

        return window

    def run(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        on_initilized=None,
        on_close=None,
    ):
        self._close_error = None

        window = self._setup_flutter(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            async_mode=False,
            show_window=False,
        )
        if window is None:
            return False

        def on_delete_event(widget, event, data):
            if on_close is not None:
                try:
                    on_close()
                except Exception as exc:
                    if self._close_error is None:
                        self._close_error = exc
            return 0

        def on_destroy(widget, data):
            gtk.gtk_main_quit()

        self._delete_event_cb = GDeleteEventCallback(on_delete_event)
        self._destroy_cb = GCallback(on_destroy)

        gobject.g_signal_connect_data.argtypes = [
            c_void_p,
            c_char_p,
            c_void_p,
            c_void_p,
            c_void_p,
            c_int,
        ]
        gobject.g_signal_connect_data(
            window,
            b"delete-event",
            ctypes.cast(self._delete_event_cb, c_void_p),
            None,
            None,
            0,
        )
        gobject.g_signal_connect_data(
            window,
            b"destroy",
            ctypes.cast(self._destroy_cb, c_void_p),
            None,
            None,
            0,
        )

        gtk.gtk_widget_show_all.argtypes = [c_void_p]
        gtk.gtk_widget_show_all(window)

        self._running = True

        if on_initilized is not None:
            on_initilized()

        gtk.gtk_main()
        if self._close_error is not None:
            raise self._close_error
        return True

    async def run_async(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        on_initilized=None,
        on_close=None,
        loop: asyncio.AbstractEventLoop = None,
    ):
        if loop is None:
            loop = asyncio.get_running_loop()

        self._close_requested = False

        window = self._setup_flutter(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            async_mode=True,
            show_window=False,
        )
        if window is None:
            return False

        def on_delete_event(widget, event, data):
            self._close_requested = True
            return 1

        self._delete_event_cb = GDeleteEventCallback(on_delete_event)
        gobject.g_signal_connect_data.argtypes = [
            c_void_p,
            c_char_p,
            c_void_p,
            c_void_p,
            c_void_p,
            c_int,
        ]
        gobject.g_signal_connect_data(
            window,
            b"delete-event",
            ctypes.cast(self._delete_event_cb, c_void_p),
            None,
            None,
            0,
        )

        gtk.gtk_widget_show_all.argtypes = [c_void_p]
        gtk.gtk_widget_show_all(window)

        if on_initilized is not None:
            await on_initilized()

        await self._run_async_gtk_loop(window, loop, on_close=on_close)
        return True

    async def _run_async_gtk_loop(
        self, window, loop: asyncio.AbstractEventLoop, on_close=None
    ):
        should_quit = False

        def on_destroy(widget, data):
            nonlocal should_quit
            should_quit = True

        self._destroy_cb = GCallback(on_destroy)
        gobject.g_signal_connect_data.argtypes = [
            c_void_p,
            c_char_p,
            c_void_p,
            c_void_p,
            c_void_p,
            c_int,
        ]
        gobject.g_signal_connect_data(
            window,
            b"destroy",
            ctypes.cast(self._destroy_cb, c_void_p),
            None,
            None,
            0,
        )

        bridge = GLibAsyncBridge()
        bridge.setup(loop)

        self._running = True
        gtk.gtk_events_pending.argtypes = []
        gtk.gtk_events_pending.restype = c_int
        gtk.gtk_main_iteration_do.argtypes = [c_int]
        gtk.gtk_main_iteration_do.restype = c_int

        def process_asyncio_timers():
            now = loop.time()
            while loop._scheduled:
                handle = loop._scheduled[0]
                if handle._cancelled:
                    heapq.heappop(loop._scheduled)
                    handle._scheduled = False
                elif handle._when <= now:
                    heapq.heappop(loop._scheduled)
                    handle._scheduled = False
                    loop._ready.append(handle)
                else:
                    break
            return bool(loop._ready)

        def drain_gtk():
            nonlocal should_quit
            while gtk.gtk_events_pending():
                gtk.gtk_main_iteration_do(False)
                if should_quit:
                    return False
            return True

        try:
            while not should_quit:
                if not drain_gtk():
                    break

                if self._close_requested:
                    self._close_requested = False
                    if on_close is not None:
                        await on_close()
                    gtk.gtk_widget_hide.argtypes = [c_void_p]
                    gtk.gtk_widget_hide(window)
                    should_quit = True
                    continue

                while process_asyncio_timers():
                    await asyncio.sleep(0)
                    if not drain_gtk():
                        break

                if should_quit:
                    break

                bridge.schedule_next_timer()

                bridge.re_register_io_source()

                if loop._ready:
                    continue

                gtk.gtk_main_iteration_do(True)
        finally:
            bridge.cleanup()

        return True

    def shutdown(self):
        if self._running:
            if gtk:
                gtk.gtk_main_level.argtypes = []
                gtk.gtk_main_level.restype = c_uint
                if gtk.gtk_main_level() > 0:
                    gtk.gtk_main_quit()
            self._running = False
        self._window = None

    @staticmethod
    def get_default_assets_path() -> str:
        return PATH_FLUT_ASSETS
