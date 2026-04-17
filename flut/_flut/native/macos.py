import ctypes
import ctypes.util
import logging
import os
import json
import collections
import asyncio
import threading
import select
from ctypes import (
    c_void_p,
    c_char_p,
    c_int,
    c_int32,
    c_int64,
    c_size_t,
    CFUNCTYPE,
    c_double,
    c_bool,
    c_uint64,
    c_uint32,
    c_long,
)

from .native import FlutNative

logger = logging.getLogger(__name__)

c_ssize_t = c_long

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_FLUT = os.path.join(
    ROOT_DIR,
    ".flutter",
    "build",
    "macos",
    "Build",
    "Products",
    "Release",
    "flut.app",
)
PATH_FLUT_FRAMEWORKS = os.path.join(PATH_FLUT, "Contents", "Frameworks")
PATH_FLUT_ASSETS = os.path.join(
    PATH_FLUT_FRAMEWORKS, "App.framework", "Resources", "flutter_assets"
)
PATH_FLUTTER_FRAMEWORK = os.path.join(PATH_FLUT_FRAMEWORKS, "FlutterMacOS.framework")
PATH_FLUTTER_DYLIB = os.path.join(PATH_FLUTTER_FRAMEWORK, "FlutterMacOS")
PATH_APP_FRAMEWORK = os.path.join(PATH_FLUT_FRAMEWORKS, "App.framework")

_objc_lib = ctypes.util.find_library("objc")
if not _objc_lib:
    raise ImportError("Could not find Objective-C runtime library")
libobjc = ctypes.CDLL(_objc_lib)

libobjc.objc_getClass.argtypes = [c_char_p]
libobjc.objc_getClass.restype = c_void_p

libobjc.sel_registerName.argtypes = [c_char_p]
libobjc.sel_registerName.restype = c_void_p

objc_msgSend = libobjc.objc_msgSend

libobjc.class_addMethod.argtypes = [c_void_p, c_void_p, c_void_p, c_char_p]
libobjc.class_addMethod.restype = c_bool

libobjc.object_getClass.argtypes = [c_void_p]
libobjc.object_getClass.restype = c_void_p

libobjc.class_addIvar.argtypes = [c_void_p, c_char_p, c_size_t, c_int, c_char_p]
libobjc.class_addIvar.restype = c_bool

libobjc.class_copyMethodList.argtypes = [c_void_p, ctypes.POINTER(c_uint32)]
libobjc.class_copyMethodList.restype = c_void_p

libobjc.method_getName.argtypes = [c_void_p]
libobjc.method_getName.restype = c_void_p

libobjc.method_getImplementation.argtypes = [c_void_p]
libobjc.method_getImplementation.restype = c_void_p

libobjc.method_getTypeEncoding.argtypes = [c_void_p]
libobjc.method_getTypeEncoding.restype = c_char_p

libobjc.class_getInstanceSize.argtypes = [c_void_p]
libobjc.class_getInstanceSize.restype = c_size_t

libobjc.class_getInstanceMethod.argtypes = [c_void_p, c_void_p]
libobjc.class_getInstanceMethod.restype = c_void_p

libobjc.sel_getName.argtypes = [c_void_p]
libobjc.sel_getName.restype = c_char_p

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.free.argtypes = [c_void_p]
libc.free.restype = None

libobjc.objc_allocateClassPair.argtypes = [c_void_p, c_char_p, c_size_t]
libobjc.objc_allocateClassPair.restype = c_void_p

libobjc.objc_registerClassPair.argtypes = [c_void_p]
libobjc.objc_registerClassPair.restype = None


def objc_class(name):
    return libobjc.objc_getClass(name.encode("utf-8"))


def sel(name):
    return libobjc.sel_registerName(name.encode("utf-8"))


def msg(obj, selector, *args, restype=c_void_p, argtypes=None):
    if argtypes is None:
        argtypes = [c_void_p, c_void_p] + [c_void_p] * len(args)

    send = ctypes.cast(objc_msgSend, ctypes.CFUNCTYPE(restype, *argtypes))
    return send(obj, sel(selector), *args)


IMP_VOID = ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)

_FLUTAPP_PADDING = 8192
_flutapp_class = None
_flutapp_resolve_imp = None
_flutapp_compat_sources = set()

libobjc.objc_copyClassList.argtypes = [ctypes.POINTER(c_uint32)]
libobjc.objc_copyClassList.restype = c_void_p

libobjc.class_getSuperclass.argtypes = [c_void_p]
libobjc.class_getSuperclass.restype = c_void_p

libobjc.class_getName.argtypes = [c_void_p]
libobjc.class_getName.restype = c_char_p


def _find_nsapp_subclasses():
    NSApplication = objc_class("NSApplication")
    if not NSApplication:
        return []

    count = c_uint32(0)
    class_list = libobjc.objc_copyClassList(ctypes.byref(count))
    if not class_list:
        return []

    result = []
    arr = ctypes.cast(class_list, ctypes.POINTER(c_void_p))
    for i in range(count.value):
        cls = arr[i]
        if not cls or cls == _flutapp_class:
            continue
        sup = libobjc.class_getSuperclass(cls)
        if sup == NSApplication:
            result.append(cls)

    libc.free(class_list)
    return result


def _copy_methods_from_class(source_class, target_class):
    NSApplication = objc_class("NSApplication")

    count = c_uint32(0)
    methods = libobjc.class_copyMethodList(source_class, ctypes.byref(count))
    if not methods:
        return

    method_array = ctypes.cast(methods, ctypes.POINTER(c_void_p))
    for i in range(count.value):
        m = method_array[i]
        sel_ptr = libobjc.method_getName(m)
        if libobjc.class_getInstanceMethod(NSApplication, sel_ptr):
            continue
        imp = libobjc.method_getImplementation(m)
        types = libobjc.method_getTypeEncoding(m)
        libobjc.class_addMethod(target_class, sel_ptr, imp, types)

    libc.free(methods)


def _copy_compat_methods(target_class):
    subclasses = _find_nsapp_subclasses()
    for cls in subclasses:
        cls_id = ctypes.cast(cls, c_void_p).value
        if cls_id not in _flutapp_compat_sources:
            _flutapp_compat_sources.add(cls_id)
            _copy_methods_from_class(cls, target_class)


def _create_flutapp_class():
    global _flutapp_class, _flutapp_resolve_imp

    if _flutapp_class is not None:
        return _flutapp_class

    NSApplication = objc_class("NSApplication")
    cls = libobjc.objc_allocateClassPair(NSApplication, b"FlutApp", 0)
    if not cls:
        return NSApplication
    _flutapp_class = cls

    libobjc.class_addIvar(_flutapp_class, b"_compat_pad", _FLUTAPP_PADDING, 3, b"?")

    RESOLVE_IMP = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)

    def resolve_instance_method(cls_ptr, cmd_ptr, sel_ptr):
        _copy_compat_methods(_flutapp_class)

        sel_name = libobjc.sel_getName(sel_ptr)
        check_sel = libobjc.sel_registerName(sel_name)
        count = c_uint32(0)
        methods = libobjc.class_copyMethodList(_flutapp_class, ctypes.byref(count))
        if methods:
            method_array = ctypes.cast(methods, ctypes.POINTER(c_void_p))
            found = False
            for i in range(count.value):
                m_sel = libobjc.method_getName(method_array[i])
                if m_sel == check_sel:
                    found = True
                    break
            libc.free(methods)
            if found:
                return True

        return False

    _flutapp_resolve_imp = RESOLVE_IMP(resolve_instance_method)

    metaclass = libobjc.object_getClass(_flutapp_class)
    libobjc.class_addMethod(
        metaclass,
        sel("resolveInstanceMethod:"),
        ctypes.cast(_flutapp_resolve_imp, c_void_p),
        b"B@::",
    )

    libobjc.objc_registerClassPair(_flutapp_class)

    return _flutapp_class


_window_delegate_callback = None
_window_delegate_should_close_callback = None
_window_delegate_class = None
_window_close_handlers = {}


def create_window_delegate_class():
    global _window_delegate_class, _window_delegate_callback
    global _window_delegate_should_close_callback

    if _window_delegate_class is not None:
        return _window_delegate_class

    NSObject = objc_class("NSObject")
    _window_delegate_class = libobjc.objc_allocateClassPair(
        NSObject, b"FlutWindowDelegate", 0
    )

    if not _window_delegate_class:
        logger.error("Failed to create delegate class")
        return None

    def window_should_close(self_ptr, cmd_ptr, sender_ptr):
        handler = _window_close_handlers.get(self_ptr)
        if handler is not None:
            return bool(handler())
        return True

    def window_will_close(self_ptr, cmd_ptr, notification_ptr):
        _window_close_handlers.pop(self_ptr, None)

        NSApplication = libobjc.objc_getClass(b"NSApplication")
        shared_app_sel = libobjc.sel_registerName(b"sharedApplication")
        terminate_sel = libobjc.sel_registerName(b"terminate:")

        get_app = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(c_void_p, c_void_p, c_void_p)
        )
        app = get_app(NSApplication, shared_app_sel)

        terminate = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)
        )
        terminate(app, terminate_sel, None)

    _window_delegate_should_close_callback = CFUNCTYPE(
        c_bool, c_void_p, c_void_p, c_void_p
    )(window_should_close)
    _window_delegate_callback = IMP_VOID(window_will_close)

    libobjc.class_addMethod(
        _window_delegate_class,
        sel("windowShouldClose:"),
        ctypes.cast(_window_delegate_should_close_callback, c_void_p),
        b"B@:@",
    )

    libobjc.class_addMethod(
        _window_delegate_class,
        sel("windowWillClose:"),
        _window_delegate_callback,
        b"v@:@",
    )

    libobjc.objc_registerClassPair(_window_delegate_class)

    return _window_delegate_class


class CGPoint(ctypes.Structure):
    _fields_ = [("x", c_double), ("y", c_double)]


class CGSize(ctypes.Structure):
    _fields_ = [("width", c_double), ("height", c_double)]


class CGRect(ctypes.Structure):
    _fields_ = [("origin", CGPoint), ("size", CGSize)]


def NSMakeRect(x, y, w, h):
    return CGRect(CGPoint(x, y), CGSize(w, h))


_cf_lib = ctypes.util.find_library("CoreFoundation")
if _cf_lib:
    CoreFoundation = ctypes.CDLL(_cf_lib)
else:
    CoreFoundation = None

kCFRunLoopCommonModes = (
    c_void_p.in_dll(CoreFoundation, "kCFRunLoopCommonModes") if CoreFoundation else None
)

CFRunLoopTimerCallBack = CFUNCTYPE(None, c_void_p, c_void_p)


class CFRunLoopSourceContext(ctypes.Structure):
    _fields_ = [
        ("version", c_long),
        ("info", c_void_p),
        ("retain", c_void_p),
        ("release", c_void_p),
        ("copyDescription", c_void_p),
        ("equal", c_void_p),
        ("hash", c_void_p),
        ("schedule", c_void_p),
        ("cancel", c_void_p),
        ("perform", c_void_p),
    ]


CFRunLoopSourcePerform = CFUNCTYPE(None, c_void_p)


class CocoaAsyncBridge:
    def __init__(self):
        self._loop = None
        self._app = None
        self._runloop = None
        self._timer = None
        self._next_deadline = float("inf")
        self._timer_callback = None
        self._original_write_to_self = None
        self._source = None
        self._perform_cb = None
        self._watcher_thread = None
        self._stop_pipe_r = -1
        self._stop_pipe_w = -1

    def _signal_source(self):
        if self._source and self._runloop:
            CoreFoundation.CFRunLoopSourceSignal(self._source)
            CoreFoundation.CFRunLoopWakeUp(self._runloop)

    def setup(self, loop: asyncio.AbstractEventLoop, app, runloop=None):
        self._loop = loop
        self._app = app

        if not CoreFoundation:
            raise RuntimeError("CoreFoundation not available")

        bridge = self

        self._nsevent_class = objc_class("NSEvent")
        self._create_event_sel = sel(
            "otherEventWithType:location:modifierFlags:timestamp:"
            "windowNumber:context:subtype:data1:data2:"
        )
        self._create_event_fn = ctypes.cast(
            objc_msgSend,
            ctypes.CFUNCTYPE(
                c_void_p,
                c_void_p,
                c_void_p,
                c_uint64,
                c_double,
                c_double,
                c_uint64,
                c_double,
                c_int64,
                c_void_p,
                c_int64,
                c_int64,
                c_int64,
            ),
        )
        self._post_event_fn = ctypes.cast(
            objc_msgSend,
            ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_bool),
        )
        self._post_event_sel = sel("postEvent:atStart:")

        def wake_perform(info):
            event = bridge._create_event_fn(
                bridge._nsevent_class,
                bridge._create_event_sel,
                15,
                0.0,
                0.0,
                0,
                0.0,
                0,
                None,
                0,
                0,
                0,
            )
            if event:
                bridge._post_event_fn(
                    bridge._app,
                    bridge._post_event_sel,
                    event,
                    False,
                )

        self._perform_cb = CFRunLoopSourcePerform(wake_perform)

        ctx = CFRunLoopSourceContext(
            0,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            ctypes.cast(self._perform_cb, c_void_p),
        )

        CoreFoundation.CFRunLoopSourceCreate.argtypes = [
            c_void_p,
            c_long,
            ctypes.POINTER(CFRunLoopSourceContext),
        ]
        CoreFoundation.CFRunLoopSourceCreate.restype = c_void_p
        CoreFoundation.CFRunLoopSourceSignal.argtypes = [c_void_p]
        CoreFoundation.CFRunLoopSourceSignal.restype = None
        CoreFoundation.CFRunLoopSourceInvalidate.argtypes = [c_void_p]
        CoreFoundation.CFRunLoopSourceInvalidate.restype = None
        CoreFoundation.CFRunLoopWakeUp.argtypes = [c_void_p]
        CoreFoundation.CFRunLoopWakeUp.restype = None
        CoreFoundation.CFRunLoopAddSource.argtypes = [c_void_p, c_void_p, c_void_p]
        CoreFoundation.CFRunLoopRemoveSource.argtypes = [c_void_p, c_void_p, c_void_p]
        CoreFoundation.CFRelease.argtypes = [c_void_p]

        self._source = CoreFoundation.CFRunLoopSourceCreate(
            None,
            0,
            ctypes.byref(ctx),
        )
        if not self._source:
            raise RuntimeError("Failed to create CFRunLoopSource")

        if runloop:
            self._runloop = runloop
        else:
            CoreFoundation.CFRunLoopGetCurrent.argtypes = []
            CoreFoundation.CFRunLoopGetCurrent.restype = c_void_p
            self._runloop = CoreFoundation.CFRunLoopGetCurrent()

        CoreFoundation.CFRunLoopAddSource(
            self._runloop,
            self._source,
            kCFRunLoopCommonModes,
        )

        self._original_write_to_self = loop._write_to_self
        original_write = self._original_write_to_self

        def hooked_write_to_self():
            original_write()
            bridge._signal_source()

        loop._write_to_self = hooked_write_to_self

        CoreFoundation.CFRunLoopTimerCreate.argtypes = [
            c_void_p,
            c_double,
            c_double,
            c_uint32,
            c_int32,
            CFRunLoopTimerCallBack,
            c_void_p,
        ]
        CoreFoundation.CFRunLoopTimerCreate.restype = c_void_p
        CoreFoundation.CFRunLoopAddTimer.argtypes = [c_void_p, c_void_p, c_void_p]
        CoreFoundation.CFRunLoopRemoveTimer.argtypes = [c_void_p, c_void_p, c_void_p]
        CoreFoundation.CFAbsoluteTimeGetCurrent.argtypes = []
        CoreFoundation.CFAbsoluteTimeGetCurrent.restype = c_double

        def timer_callback(timer, info):
            bridge._signal_source()
            if bridge._timer:
                CoreFoundation.CFRunLoopRemoveTimer(
                    bridge._runloop,
                    bridge._timer,
                    kCFRunLoopCommonModes,
                )
                CoreFoundation.CFRelease(bridge._timer)
                bridge._timer = None
            bridge._next_deadline = float("inf")

        self._timer_callback = CFRunLoopTimerCallBack(timer_callback)

        self._selector = getattr(loop, "_selector", None)
        if self._selector is not None:
            self._stop_pipe_r, self._stop_pipe_w = os.pipe()
            self._watcher_thread = threading.Thread(
                target=self._watch_loop,
                args=(self._selector.fileno(), self._runloop, self._source),
                daemon=True,
                name="FlutMacIO",
            )
            self._watcher_thread.start()

    def _watch_loop(self, fd, runloop, source):
        stop_fd = self._stop_pipe_r
        while True:
            try:
                r, _, _ = select.select([fd, stop_fd], [], [])
                if stop_fd in r:
                    break
                if fd in r:
                    CoreFoundation.CFRunLoopSourceSignal(source)
                    CoreFoundation.CFRunLoopWakeUp(runloop)
            except (OSError, ValueError):
                break
            except Exception as e:
                logger.error("Watcher thread error: %s", e)
                break

    def schedule_next_timer(self):
        self._next_deadline = float("inf")
        if self._timer:
            CoreFoundation.CFRunLoopRemoveTimer(
                self._runloop,
                self._timer,
                kCFRunLoopCommonModes,
            )
            CoreFoundation.CFRelease(self._timer)
            self._timer = None

        scheduled = getattr(self._loop, "_scheduled", [])
        if not scheduled:
            return

        for handle in scheduled:
            if not handle._cancelled:
                when = handle._when
                break
        else:
            return

        delay_sec = max(0.001, when - self._loop.time())
        fire_time = CoreFoundation.CFAbsoluteTimeGetCurrent() + delay_sec

        self._timer = CoreFoundation.CFRunLoopTimerCreate(
            None,
            fire_time,
            0,
            0,
            0,
            self._timer_callback,
            None,
        )

        if self._timer:
            CoreFoundation.CFRunLoopAddTimer(
                self._runloop,
                self._timer,
                kCFRunLoopCommonModes,
            )
            self._next_deadline = when

    def cleanup(self):
        if self._watcher_thread:
            if self._stop_pipe_w >= 0:
                os.write(self._stop_pipe_w, b"\x00")
                os.close(self._stop_pipe_w)
                self._stop_pipe_w = -1
            self._watcher_thread.join(timeout=2)
            if self._stop_pipe_r >= 0:
                os.close(self._stop_pipe_r)
                self._stop_pipe_r = -1

        if self._loop and self._original_write_to_self:
            self._loop._write_to_self = self._original_write_to_self

        if self._timer and CoreFoundation:
            CoreFoundation.CFRunLoopRemoveTimer(
                self._runloop,
                self._timer,
                kCFRunLoopCommonModes,
            )
            CoreFoundation.CFRelease(self._timer)
            self._timer = None

        if self._source and CoreFoundation:
            CoreFoundation.CFRunLoopSourceInvalidate(self._source)
            CoreFoundation.CFRelease(self._source)
            self._source = None


class FlutMacOSNative(FlutNative):
    def __init__(self):
        self.flutter_engine = None
        self.flutter_view_controller = None
        self._running = False
        self._native_callback = None
        self._last_buffer = None
        self._window = None
        self._window_delegate = None
        self._icon_image = None
        self._close_error = None
        self._close_requested = False
        self._close_allowed = False
        self._notify_keepalive = []
        self._notify_acked = 0

    def initialize(self):
        if not os.path.exists(PATH_FLUT):
            raise FileNotFoundError(
                f"Flutter app bundle not found at {PATH_FLUT}. Build with: cd flut/.flutter && flutter build macos --no-tree-shake-icons"
            )

        if not os.path.exists(PATH_FLUTTER_DYLIB):
            raise FileNotFoundError(
                f"FlutterMacOS.framework not found at: {PATH_FLUTTER_DYLIB}"
            )

        NSBundle = objc_class("NSBundle")
        flutter_path_ns = self._create_nsstring(PATH_FLUTTER_FRAMEWORK)
        flutter_bundle = msg(NSBundle, "bundleWithPath:", flutter_path_ns)
        if flutter_bundle:
            msg(flutter_bundle, "load")

        app_path_ns = self._create_nsstring(PATH_APP_FRAMEWORK)
        app_bundle = msg(NSBundle, "bundleWithPath:", app_path_ns)
        if app_bundle:
            msg(app_bundle, "load")

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

    def _create_nsstring(self, s):
        NSString = objc_class("NSString")
        return msg(NSString, "stringWithUTF8String:", s.encode("utf-8"))

    def _create_nsarray(self, items):
        NSMutableArray = objc_class("NSMutableArray")
        arr = msg(NSMutableArray, "array")
        for item in items:
            ns_item = self._create_nsstring(item)
            msg(arr, "addObject:", ns_item)
        return arr

    def _apply_icon(self, app, icon_path):
        NSImage = objc_class("NSImage")
        with self._use_default_icon_path() as default_icon_path:
            candidates = []
            if icon_path is not None:
                candidates.append(icon_path)
            if default_icon_path is not None and default_icon_path not in candidates:
                candidates.append(default_icon_path)

            for candidate in candidates:
                image = msg(
                    msg(NSImage, "alloc"),
                    "initWithContentsOfFile:",
                    self._create_nsstring(candidate),
                )
                if image:
                    self._icon_image = image
                    msg(app, "setApplicationIconImage:", image)
                    if self._window is not None:
                        msg(self._window, "setMiniwindowImage:", image)
                    return

                if candidate != default_icon_path and default_icon_path is not None:
                    logger.warning(
                        "Failed to load icon %s. Falling back to packaged icon.",
                        candidate,
                    )

        if icon_path is not None:
            raise RuntimeError(f"Failed to load icon: {icon_path}")

    def _setup_flutter(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        on_close=None,
        async_mode: bool = False,
    ):
        if not os.path.exists(flutter_asset_path):
            raise FileNotFoundError(f"Assets path not found: {flutter_asset_path}")

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

        FlutApp = _create_flutapp_class()
        NSWindow = objc_class("NSWindow")
        FlutterDartProject = objc_class("FlutterDartProject")
        FlutterViewController = objc_class("FlutterViewController")

        app = msg(FlutApp, "sharedApplication")
        set_policy = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(c_bool, c_void_p, c_void_p, c_int)
        )
        set_policy(app, sel("setActivationPolicy:"), 0)
        msg(app, "finishLaunching")

        dart_project = msg(msg(FlutterDartProject, "alloc"), "init")
        dart_args = self._create_nsarray([f"--native-callback={callback_addr}"])
        msg(dart_project, "setDartEntrypointArguments:", dart_args)

        self.flutter_view_controller = msg(
            msg(FlutterViewController, "alloc"),
            "initWithProject:",
            dart_project,
        )

        if not self.flutter_view_controller:
            raise RuntimeError("Failed to create Flutter view controller")

        self.flutter_engine = msg(self.flutter_view_controller, "engine")
        style_mask = (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3)
        init_window = ctypes.cast(
            objc_msgSend,
            ctypes.CFUNCTYPE(
                c_void_p,
                c_void_p,
                c_void_p,
                CGRect,
                c_uint64,
                c_uint64,
                c_bool,
            ),
        )

        rect = NSMakeRect(100, 100, width, height)
        self._window = init_window(
            msg(NSWindow, "alloc"),
            sel("initWithContentRect:styleMask:backing:defer:"),
            rect,
            style_mask,
            2,
            False,
        )

        if not self._window:
            raise RuntimeError("Failed to create window")

        delegate_class = create_window_delegate_class()
        if delegate_class:
            self._window_delegate = msg(msg(delegate_class, "alloc"), "init")
            _window_close_handlers[self._window_delegate] = on_close
            msg(self._window, "setDelegate:", self._window_delegate)

        set_released = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_bool)
        )
        set_released(self._window, sel("setReleasedWhenClosed:"), False)

        title_str = self._create_nsstring(title)
        msg(self._window, "setTitle:", title_str)
        self._apply_icon(app, icon_path)

        flutter_view = msg(self.flutter_view_controller, "view")
        msg(self._window, "setContentView:", flutter_view)

        set_frame = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(None, c_void_p, c_void_p, CGRect)
        )
        content_rect = NSMakeRect(0, 0, width, height)
        set_frame(flutter_view, sel("setFrame:"), content_rect)

        set_hidden = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_bool)
        )
        set_hidden(flutter_view, sel("setHidden:"), False)
        msg(flutter_view, "setNeedsDisplay:", c_void_p(1))
        msg(flutter_view, "display")
        msg(self._window, "center")
        msg(self._window, "makeKeyAndOrderFront:", c_void_p(0))

        activate = ctypes.cast(
            objc_msgSend, ctypes.CFUNCTYPE(None, c_void_p, c_void_p, c_bool)
        )
        activate(app, sel("activateIgnoringOtherApps:"), True)

        self._running = True
        return app

    def run(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        on_initialized=None,
        on_close=None,
    ):
        self._close_error = None

        def handle_close():
            self._running = False
            if on_close is None:
                return True
            try:
                on_close()
            except Exception as exc:
                if self._close_error is None:
                    self._close_error = exc
            return True

        app = self._setup_flutter(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_close=handle_close,
            async_mode=False,
        )
        if app is None:
            return False
        if on_initialized is not None:
            on_initialized()
        msg(app, "run")
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
        on_initialized=None,
        on_close=None,
        loop=None,
    ):
        if loop is None:
            loop = asyncio.get_running_loop()

        self._close_requested = False
        self._close_allowed = False
        self._close_error = None

        def handle_close():
            if self._close_allowed or on_close is None:
                self._running = False
                return True
            self._close_requested = True
            return False

        app = self._setup_flutter(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_close=handle_close,
            async_mode=True,
        )
        if app is None:
            return False

        if on_initialized is not None:
            await on_initialized()
        await self._run_async_runloop(app, loop, on_close=on_close)

        if self._close_error is not None:
            raise self._close_error

        return True

    async def _run_async_runloop(self, app, loop, on_close=None):
        NSDate = objc_class("NSDate")
        cf = ctypes.CDLL(
            "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation"
        )
        kCFRunLoopDefaultMode = c_void_p.in_dll(cf, "kCFRunLoopDefaultMode")

        CFRunLoopGetMain = cf.CFRunLoopGetMain
        CFRunLoopGetMain.argtypes = []
        CFRunLoopGetMain.restype = c_void_p

        main_runloop = CFRunLoopGetMain()
        bridge = CocoaAsyncBridge()
        bridge.setup(loop, app, main_runloop)

        NSEventMaskAny = 0xFFFFFFFFFFFFFFFF
        next_event_fn = ctypes.cast(
            objc_msgSend,
            ctypes.CFUNCTYPE(
                c_void_p,
                c_void_p,
                c_void_p,
                c_uint64,
                c_void_p,
                c_void_p,
                c_bool,
            ),
        )
        next_event_sel = sel("nextEventMatchingMask:untilDate:inMode:dequeue:")
        distant_future = msg(NSDate, "distantFuture")

        def drain_nsevents():
            now_date = msg(NSDate, "date")
            while True:
                event = next_event_fn(
                    app,
                    next_event_sel,
                    NSEventMaskAny,
                    now_date,
                    kCFRunLoopDefaultMode,
                    True,
                )
                if not event:
                    break
                msg(app, "sendEvent:", event)
            msg(app, "updateWindows")

        try:
            while self._running:
                drain_nsevents()

                if self._close_requested:
                    self._close_requested = False
                    if on_close is not None:
                        try:
                            await on_close()
                        except Exception as exc:
                            if self._close_error is None:
                                self._close_error = exc
                    self._close_allowed = True
                    msg(self._window, "performClose:", c_void_p(0))
                    continue

                await asyncio.sleep(0)

                drain_nsevents()

                if self._close_requested:
                    self._close_requested = False
                    if on_close is not None:
                        try:
                            await on_close()
                        except Exception as exc:
                            if self._close_error is None:
                                self._close_error = exc
                    self._close_allowed = True
                    msg(self._window, "performClose:", c_void_p(0))
                    continue

                if not self._running:
                    break

                bridge.schedule_next_timer()

                if loop._ready:
                    continue

                event = next_event_fn(
                    app,
                    next_event_sel,
                    NSEventMaskAny,
                    distant_future,
                    kCFRunLoopDefaultMode,
                    True,
                )

                if event:
                    msg(app, "sendEvent:", event)

        finally:
            bridge.cleanup()

    def shutdown(self):
        self._running = False
        if self._window_delegate is not None:
            _window_close_handlers.pop(self._window_delegate, None)
        if self.flutter_engine:
            msg(self.flutter_engine, "shutDownEngine")
            self.flutter_engine = None

    @staticmethod
    def get_default_assets_path() -> str:
        return PATH_FLUT_ASSETS
