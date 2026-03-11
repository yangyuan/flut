import _overlapped
import asyncio
import collections
import ctypes
from ctypes import wintypes
import json
import logging
import os
import threading

from .native import FlutNative

logger = logging.getLogger(__name__)


WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
WAIT_FAILED = 0xFFFFFFFF
INFINITE = 0xFFFFFFFF
QS_ALLINPUT = 0x04FF
MWMO_ALERTABLE = 0x0002
MWMO_INPUTAVAILABLE = 0x0004
PM_REMOVE = 0x0001
PM_NOREMOVE = 0x0000

WM_DESTROY = 0x0002
WM_SIZE = 0x0005
WM_PAINT = 0x000F
WM_ACTIVATE = 0x0006
WM_SETFOCUS = 0x0007
WM_CLOSE = 0x0010
WM_QUIT = 0x0012
WM_SETICON = 0x0080
WS_OVERLAPPEDWINDOW = 0x00CF0000
WS_VISIBLE = 0x10000000
WS_CHILD = 0x40000000
GWL_STYLE = -16
SW_SHOW = 5
SWP_NOZORDER = 0x0004
SWP_SHOWWINDOW = 0x0040
SWP_FRAMECHANGED = 0x0020
ICON_SMALL = 0
ICON_BIG = 1
IMAGE_ICON = 1
LR_LOADFROMFILE = 0x0010
SM_CXICON = 11
SM_CYICON = 12
SM_CXSMICON = 49
SM_CYSMICON = 50
INTERPOLATION_MODE_HIGH_QUALITY_BICUBIC = 7
PIXEL_FORMAT_32BPP_ARGB = 0x26200A

if ctypes.sizeof(ctypes.c_void_p) == 8:
    LRESULT = ctypes.c_longlong
else:
    LRESULT = ctypes.c_long

WNDPROC = ctypes.WINFUNCTYPE(
    LRESULT, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM
)

HCURSOR = getattr(wintypes, "HCURSOR", wintypes.HANDLE)


class WNDCLASSEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HICON),
        ("hCursor", HCURSOR),
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
        ("hIconSm", wintypes.HICON),
    ]


class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("message", wintypes.UINT),
        ("wParam", wintypes.WPARAM),
        ("lParam", wintypes.LPARAM),
        ("time", wintypes.DWORD),
        ("pt", wintypes.POINT),
        ("lPrivate", wintypes.DWORD),
    ]


class GdiplusStartupInput(ctypes.Structure):
    _fields_ = [
        ("GdiplusVersion", ctypes.c_uint32),
        ("DebugEventCallback", ctypes.c_void_p),
        ("SuppressBackgroundThread", wintypes.BOOL),
        ("SuppressExternalCodecs", wintypes.BOOL),
    ]


class ProactorWakeEvent:
    def __init__(self):
        self._event = None
        self._loop = None
        self._original_write_to_self = None

    def setup(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop

        kernel32 = ctypes.windll.kernel32
        self._event = kernel32.CreateEventW(None, False, False, None)
        if not self._event:
            raise RuntimeError("Failed to create Win32 event")

        self._original_write_to_self = loop._write_to_self
        event = self._event

        def hooked_write_to_self():
            self._original_write_to_self()
            kernel32.SetEvent(event)

        loop._write_to_self = hooked_write_to_self

        return self._event

    def cleanup(self):
        if self._loop and self._original_write_to_self:
            self._loop._write_to_self = self._original_write_to_self

        if self._event:
            ctypes.windll.kernel32.CloseHandle(self._event)
            self._event = None


class IOCPPollerThread:
    def __init__(self):
        self._iocp = None
        self._wake_event = None
        self._thread = None
        self._running = False
        self._relay = collections.deque()

    def start(self, iocp_handle, wake_event):
        self._iocp = iocp_handle
        self._wake_event = wake_event
        self._running = True
        self._thread = threading.Thread(target=self._poll_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        _overlapped.PostQueuedCompletionStatus(self._iocp, 0, 0, 0)
        if self._thread:
            self._thread.join(timeout=2)
            self._thread = None

    def _poll_loop(self):
        kernel32 = ctypes.windll.kernel32

        while True:
            try:
                status = _overlapped.GetQueuedCompletionStatus(self._iocp, INFINITE)
            except OSError:
                break
            if status is not None:
                self._relay.append(status)
                kernel32.SetEvent(self._wake_event)
            if not self._running:
                break


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_FLUT = os.path.join(
    ROOT_DIR,
    ".flutter",
    "build",
    "windows",
    FlutNative._get_arch(),
    "runner",
    "Release",
)
PATH_FLUT_ASSETS = os.path.join(PATH_FLUT, "data", "flutter_assets")
PATH_FLUT_ICU = os.path.join(PATH_FLUT, "data", "icudtl.dat")
PATH_FLUT_AOT = os.path.join(PATH_FLUT, "data", "app.so")
PATH_FLUT_WINDOWS_DLL = os.path.join(PATH_FLUT, "flutter_windows.dll")


class FlutterDesktopEngineProperties(ctypes.Structure):
    _pack_ = 8
    _fields_ = [
        ("assets_path", ctypes.c_wchar_p),
        ("icu_data_path", ctypes.c_wchar_p),
        ("aot_library_path", ctypes.c_wchar_p),
        ("dart_entrypoint", ctypes.c_char_p),
        ("dart_entrypoint_argc", ctypes.c_int),
        ("dart_entrypoint_argv", ctypes.POINTER(ctypes.c_char_p)),
        ("gpu_preference", ctypes.c_int),
        ("ui_thread_policy", ctypes.c_int),
    ]


FlutterDesktopBinaryReply = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t, ctypes.c_void_p
)


class FlutterDesktopMessage(ctypes.Structure):
    _fields_ = [
        ("struct_size", ctypes.c_size_t),
        ("channel", ctypes.c_char_p),
        ("message", ctypes.POINTER(ctypes.c_uint8)),
        ("message_size", ctypes.c_size_t),
        ("response_handle", ctypes.c_void_p),
    ]


FlutterDesktopMessageCallback = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(FlutterDesktopMessage), ctypes.c_void_p
)


class FlutWindowsNative(FlutNative):
    def __init__(self):
        self.engine_dir = PATH_FLUT
        self.dll_path = PATH_FLUT_WINDOWS_DLL
        self.icu_path = PATH_FLUT_ICU

        self.flutter = None
        self.engine = None
        self.view_controller = None
        self._running = False
        self._props = None
        self._wndproc = None
        self._native_callback = None
        self._notify_keepalive = []
        self._notify_acked = 0
        self._last_buffer = None
        self._icon_handles = []
        self._gdiplus = None
        self._gdiplus_token = ctypes.c_size_t()
        self._host_class_name = f"FlutterHostWindow_{id(self)}"

    def initialize(self):
        if not os.path.exists(self.dll_path):
            raise FileNotFoundError(
                f"flutter_windows.dll not found at: {self.dll_path}"
            )

        try:
            ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass

        ctypes.windll.ole32.CoInitialize(None)

        os.add_dll_directory(self.engine_dir)
        self.flutter = ctypes.CDLL(self.dll_path)

        self._setup_api()
        self._setup_win32_api()
        self._setup_gdiplus_api()

    def _get_dpi_scale(self):
        try:
            user32 = ctypes.windll.user32
            dpi = user32.GetDpiForSystem()
            return dpi / 96.0
        except Exception:
            try:
                hdc = ctypes.windll.user32.GetDC(0)
                dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)
                ctypes.windll.user32.ReleaseDC(0, hdc)
                return dpi / 96.0
            except Exception:
                return 1.0

    def _setup_api(self):
        f = self.flutter

        f.FlutterDesktopEngineCreate.argtypes = [
            ctypes.POINTER(FlutterDesktopEngineProperties),
        ]
        f.FlutterDesktopEngineCreate.restype = ctypes.c_void_p

        f.FlutterDesktopEngineDestroy.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopEngineDestroy.restype = ctypes.c_bool

        f.FlutterDesktopEngineRun.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        f.FlutterDesktopEngineRun.restype = ctypes.c_bool

        f.FlutterDesktopViewControllerCreate.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_void_p,
        ]
        f.FlutterDesktopViewControllerCreate.restype = ctypes.c_void_p

        f.FlutterDesktopViewControllerDestroy.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopViewControllerDestroy.restype = None

        f.FlutterDesktopViewControllerGetEngine.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopViewControllerGetEngine.restype = ctypes.c_void_p

        f.FlutterDesktopViewControllerGetView.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopViewControllerGetView.restype = ctypes.c_void_p

        f.FlutterDesktopViewGetHWND.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopViewGetHWND.restype = wintypes.HWND

        f.FlutterDesktopViewControllerHandleTopLevelWindowProc.argtypes = [
            ctypes.c_void_p,
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            wintypes.LPARAM,
            ctypes.POINTER(LRESULT),
        ]
        f.FlutterDesktopViewControllerHandleTopLevelWindowProc.restype = ctypes.c_bool

        f.FlutterDesktopViewControllerForceRedraw.argtypes = [ctypes.c_void_p]
        f.FlutterDesktopViewControllerForceRedraw.restype = None

        f.FlutterDesktopEngineProcessExternalWindowMessage.argtypes = [
            ctypes.c_void_p,
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            wintypes.LPARAM,
            ctypes.POINTER(LRESULT),
        ]
        f.FlutterDesktopEngineProcessExternalWindowMessage.restype = ctypes.c_bool

        try:
            f.FlutterDesktopEngineGetMessenger.argtypes = [ctypes.c_void_p]
            f.FlutterDesktopEngineGetMessenger.restype = ctypes.c_void_p

            f.FlutterDesktopMessengerSetCallback.argtypes = [
                ctypes.c_void_p,
                ctypes.c_char_p,
                FlutterDesktopMessageCallback,
                ctypes.c_void_p,
            ]
            f.FlutterDesktopMessengerSetCallback.restype = None

            f.FlutterDesktopMessengerSendResponse.argtypes = [
                ctypes.c_void_p,
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_uint8),
                ctypes.c_size_t,
            ]
            f.FlutterDesktopMessengerSendResponse.restype = None
        except AttributeError:
            logger.error("Messenger API not found in flutter_windows.dll")

    def setup_call_dart(self, callback_addr):
        DART_CALL_CALLBACK = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)
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
        DART_NOTIFY_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
        dart_fn = DART_NOTIFY_CALLBACK(callback_addr)

        def notify_dart_impl(data_bytes):
            try:
                self._notify_keepalive.append(data_bytes)
                dart_fn(data_bytes)
            except Exception as e:
                logger.error("Error notifying Dart: %s", e)

        return notify_dart_impl

    def _setup_engine(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        async_mode: bool = False,
    ):
        if not os.path.exists(flutter_asset_path):
            raise FileNotFoundError(f"Assets path not found: {flutter_asset_path}")
        if not os.path.exists(self.icu_path):
            raise FileNotFoundError(f"ICU data not found: {self.icu_path}")
        if not os.path.exists(PATH_FLUT_AOT):
            raise FileNotFoundError(f"AOT library not found at: {PATH_FLUT_AOT}")

        dpi_scale = self._get_dpi_scale()
        scaled_width = int(width * dpi_scale)
        scaled_height = int(height * dpi_scale)

        self._props = FlutterDesktopEngineProperties()
        self._props.assets_path = flutter_asset_path
        self._props.icu_data_path = self.icu_path
        self._props.aot_library_path = PATH_FLUT_AOT
        self._props.dart_entrypoint = None
        self._props.dart_entrypoint_argc = 0
        self._props.dart_entrypoint_argv = None
        self._props.gpu_preference = 0
        self._props.ui_thread_policy = 1

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

        NativeCallbackType = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)
        self._native_callback = NativeCallbackType(on_native_callback)

        callback_addr = ctypes.cast(self._native_callback, ctypes.c_void_p).value

        arg1 = f"--native-callback={callback_addr}"
        self._argv_buffers = [arg1.encode("utf-8")]
        self._argv_ptrs = [ctypes.c_char_p(b) for b in self._argv_buffers]
        self._argv_ptrs.append(None)

        ArgvArray = ctypes.c_char_p * len(self._argv_ptrs)
        argv_c = ArgvArray(*self._argv_ptrs)

        self._props.dart_entrypoint_argc = 1
        self._props.dart_entrypoint_argv = ctypes.cast(
            argv_c, ctypes.POINTER(ctypes.c_char_p)
        )

        self.engine = self.flutter.FlutterDesktopEngineCreate(ctypes.byref(self._props))

        if not self.engine:
            logger.error("Failed to create Flutter engine")
            return None, 0, 0

        self.view_controller = self.flutter.FlutterDesktopViewControllerCreate(
            scaled_width, scaled_height, self.engine
        )

        if not self.view_controller:
            logger.error("Failed to create Flutter view controller")
            self.engine = None
            return None, 0, 0

        view = self.flutter.FlutterDesktopViewControllerGetView(self.view_controller)
        hwnd = self.flutter.FlutterDesktopViewGetHWND(view)

        return hwnd, scaled_width, scaled_height, title

    def _setup_win32_api(self):
        user32 = ctypes.windll.user32

        user32.RegisterClassExW.argtypes = [ctypes.c_void_p]
        user32.RegisterClassExW.restype = wintypes.ATOM
        user32.CreateWindowExW.argtypes = [
            wintypes.DWORD,
            wintypes.LPCWSTR,
            wintypes.LPCWSTR,
            wintypes.DWORD,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            wintypes.HWND,
            wintypes.HMENU,
            wintypes.HINSTANCE,
            wintypes.LPVOID,
        ]
        user32.CreateWindowExW.restype = wintypes.HWND
        user32.SetParent.argtypes = [wintypes.HWND, wintypes.HWND]
        user32.SetParent.restype = wintypes.HWND
        user32.SetWindowLongPtrW.argtypes = [
            wintypes.HWND,
            ctypes.c_int,
            ctypes.c_void_p,
        ]
        user32.SetWindowLongPtrW.restype = ctypes.c_void_p
        user32.SetWindowPos.argtypes = [
            wintypes.HWND,
            wintypes.HWND,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            wintypes.UINT,
        ]
        user32.SetWindowPos.restype = wintypes.BOOL
        user32.DefWindowProcW.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            wintypes.LPARAM,
        ]
        user32.DefWindowProcW.restype = LRESULT
        user32.GetClientRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
        user32.GetClientRect.restype = wintypes.BOOL
        user32.MsgWaitForMultipleObjectsEx.argtypes = [
            wintypes.DWORD,
            ctypes.POINTER(wintypes.HANDLE),
            wintypes.DWORD,
            wintypes.DWORD,
            wintypes.DWORD,
        ]
        user32.MsgWaitForMultipleObjectsEx.restype = wintypes.DWORD
        user32.PeekMessageW.argtypes = [
            ctypes.c_void_p,
            wintypes.HWND,
            wintypes.UINT,
            wintypes.UINT,
            wintypes.UINT,
        ]
        user32.PeekMessageW.restype = wintypes.BOOL
        user32.LoadImageW.argtypes = [
            wintypes.HINSTANCE,
            wintypes.LPCWSTR,
            wintypes.UINT,
            ctypes.c_int,
            ctypes.c_int,
            wintypes.UINT,
        ]
        user32.LoadImageW.restype = wintypes.HANDLE
        user32.SendMessageW.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            wintypes.LPARAM,
        ]
        user32.SendMessageW.restype = LRESULT
        user32.DestroyIcon.argtypes = [wintypes.HICON]
        user32.DestroyIcon.restype = wintypes.BOOL
        user32.GetSystemMetrics.argtypes = [ctypes.c_int]
        user32.GetSystemMetrics.restype = ctypes.c_int

    def _setup_gdiplus_api(self):
        self._gdiplus = ctypes.windll.gdiplus
        self._gdiplus.GdiplusStartup.argtypes = [
            ctypes.POINTER(ctypes.c_size_t),
            ctypes.POINTER(GdiplusStartupInput),
            ctypes.c_void_p,
        ]
        self._gdiplus.GdiplusStartup.restype = ctypes.c_uint32
        self._gdiplus.GdiplusShutdown.argtypes = [ctypes.c_size_t]
        self._gdiplus.GdiplusShutdown.restype = None
        self._gdiplus.GdipCreateBitmapFromFile.argtypes = [
            ctypes.c_wchar_p,
            ctypes.POINTER(ctypes.c_void_p),
        ]
        self._gdiplus.GdipCreateBitmapFromFile.restype = ctypes.c_uint32
        self._gdiplus.GdipCreateBitmapFromScan0.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_void_p),
        ]
        self._gdiplus.GdipCreateBitmapFromScan0.restype = ctypes.c_uint32
        self._gdiplus.GdipCreateHICONFromBitmap.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(wintypes.HICON),
        ]
        self._gdiplus.GdipCreateHICONFromBitmap.restype = ctypes.c_uint32
        self._gdiplus.GdipGetImageGraphicsContext.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_void_p),
        ]
        self._gdiplus.GdipGetImageGraphicsContext.restype = ctypes.c_uint32
        self._gdiplus.GdipDrawImageRectI.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
        ]
        self._gdiplus.GdipDrawImageRectI.restype = ctypes.c_uint32
        self._gdiplus.GdipSetInterpolationMode.argtypes = [
            ctypes.c_void_p,
            ctypes.c_int,
        ]
        self._gdiplus.GdipSetInterpolationMode.restype = ctypes.c_uint32
        self._gdiplus.GdipDeleteGraphics.argtypes = [ctypes.c_void_p]
        self._gdiplus.GdipDeleteGraphics.restype = ctypes.c_uint32
        self._gdiplus.GdipDisposeImage.argtypes = [ctypes.c_void_p]
        self._gdiplus.GdipDisposeImage.restype = ctypes.c_uint32

        startup_input = GdiplusStartupInput(1, None, False, False)
        status = self._gdiplus.GdiplusStartup(
            ctypes.byref(self._gdiplus_token),
            ctypes.byref(startup_input),
            None,
        )
        if status != 0:
            raise RuntimeError(f"Failed to initialize GDI+: status {status}")

    def _load_icon_from_png(self, icon_path, width, height):
        source_bitmap = ctypes.c_void_p()
        status = self._gdiplus.GdipCreateBitmapFromFile(
            ctypes.c_wchar_p(icon_path),
            ctypes.byref(source_bitmap),
        )
        if status != 0 or not source_bitmap.value:
            raise RuntimeError(f"Failed to load PNG icon: {icon_path}")

        scaled_bitmap = ctypes.c_void_p()
        graphics = ctypes.c_void_p()
        icon_handle = wintypes.HICON()

        try:
            status = self._gdiplus.GdipCreateBitmapFromScan0(
                width,
                height,
                0,
                PIXEL_FORMAT_32BPP_ARGB,
                None,
                ctypes.byref(scaled_bitmap),
            )
            if status != 0 or not scaled_bitmap.value:
                raise RuntimeError(f"Failed to allocate icon bitmap: {icon_path}")

            status = self._gdiplus.GdipGetImageGraphicsContext(
                scaled_bitmap,
                ctypes.byref(graphics),
            )
            if status != 0 or not graphics.value:
                raise RuntimeError(
                    f"Failed to create icon graphics context: {icon_path}"
                )

            self._gdiplus.GdipSetInterpolationMode(
                graphics,
                INTERPOLATION_MODE_HIGH_QUALITY_BICUBIC,
            )
            status = self._gdiplus.GdipDrawImageRectI(
                graphics,
                source_bitmap,
                0,
                0,
                width,
                height,
            )
            if status != 0:
                raise RuntimeError(f"Failed to scale PNG icon: {icon_path}")

            status = self._gdiplus.GdipCreateHICONFromBitmap(
                scaled_bitmap,
                ctypes.byref(icon_handle),
            )
            if status != 0 or not icon_handle.value:
                raise RuntimeError(f"Failed to create icon from PNG: {icon_path}")
        finally:
            if graphics.value:
                self._gdiplus.GdipDeleteGraphics(graphics)
            if scaled_bitmap.value:
                self._gdiplus.GdipDisposeImage(scaled_bitmap)
            self._gdiplus.GdipDisposeImage(source_bitmap)

        return icon_handle.value

    def _load_icon_handles(self, icon_path):
        with self._use_default_icon_path() as default_icon_path:
            candidates = []
            if icon_path is not None:
                candidates.append(icon_path)
            if default_icon_path is not None and default_icon_path not in candidates:
                candidates.append(default_icon_path)

            user32 = ctypes.windll.user32
            big_width = user32.GetSystemMetrics(SM_CXICON)
            big_height = user32.GetSystemMetrics(SM_CYICON)
            small_width = user32.GetSystemMetrics(SM_CXSMICON)
            small_height = user32.GetSystemMetrics(SM_CYSMICON)
            last_error = None

            for candidate in candidates:
                extension = os.path.splitext(candidate)[1].lower()
                try:
                    if extension == ".ico":
                        big_icon_handle = user32.LoadImageW(
                            None,
                            candidate,
                            IMAGE_ICON,
                            big_width,
                            big_height,
                            LR_LOADFROMFILE,
                        )
                        small_icon_handle = user32.LoadImageW(
                            None,
                            candidate,
                            IMAGE_ICON,
                            small_width,
                            small_height,
                            LR_LOADFROMFILE,
                        )
                        if not big_icon_handle or not small_icon_handle:
                            raise RuntimeError(f"Failed to load icon: {candidate}")
                    elif extension == ".png":
                        big_icon_handle = self._load_icon_from_png(
                            candidate,
                            big_width,
                            big_height,
                        )
                        small_icon_handle = self._load_icon_from_png(
                            candidate,
                            small_width,
                            small_height,
                        )
                    else:
                        raise ValueError("Icon must be a .png or .ico file.")

                    self._icon_handles.extend([big_icon_handle, small_icon_handle])
                    return big_icon_handle, small_icon_handle
                except Exception as exc:
                    last_error = exc
                    if candidate != default_icon_path and default_icon_path is not None:
                        logger.warning(
                            "Failed to load icon %s. Falling back to packaged icon.",
                            candidate,
                        )

            if last_error is not None:
                raise last_error
            return None, None

    def _create_host_window(
        self,
        flutter_hwnd,
        width,
        height,
        title,
        icon_path,
        on_close,
        on_destroy,
    ):
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32

        def _host_wndproc(host_hwnd, msg, wparam, lparam):
            result = LRESULT(0)
            try:
                handled = (
                    self.flutter.FlutterDesktopViewControllerHandleTopLevelWindowProc(
                        self.view_controller,
                        host_hwnd,
                        msg,
                        wparam,
                        lparam,
                        ctypes.byref(result),
                    )
                )
                if handled:
                    return result.value
            except OSError:
                pass

            if msg == WM_SIZE:
                new_w = lparam & 0xFFFF
                new_h = (lparam >> 16) & 0xFFFF
                user32.SetWindowPos(
                    flutter_hwnd,
                    None,
                    0,
                    0,
                    new_w,
                    new_h,
                    SWP_NOZORDER | SWP_SHOWWINDOW,
                )

            if msg == WM_PAINT:
                try:
                    self.flutter.FlutterDesktopViewControllerForceRedraw(
                        self.view_controller
                    )
                except OSError:
                    pass

            if msg == WM_SETFOCUS or msg == WM_ACTIVATE:
                user32.SetFocus(flutter_hwnd)

            if msg == WM_CLOSE:
                if on_close():
                    return 0

            if msg == WM_DESTROY:
                on_destroy()
                return 0

            return user32.DefWindowProcW(host_hwnd, msg, wparam, lparam)

        self._wndproc = WNDPROC(_host_wndproc)

        class_name = self._host_class_name
        h_instance = kernel32.GetModuleHandleW(None)
        big_icon_handle, small_icon_handle = self._load_icon_handles(icon_path)

        wndclass = WNDCLASSEX()
        wndclass.cbSize = ctypes.sizeof(WNDCLASSEX)
        wndclass.style = 0
        wndclass.lpfnWndProc = self._wndproc
        wndclass.cbClsExtra = 0
        wndclass.cbWndExtra = 0
        wndclass.hInstance = h_instance
        wndclass.hIcon = big_icon_handle
        wndclass.hCursor = user32.LoadCursorW(None, 32512)
        wndclass.hbrBackground = None
        wndclass.lpszMenuName = None
        wndclass.lpszClassName = class_name
        wndclass.hIconSm = small_icon_handle

        user32.RegisterClassExW(ctypes.byref(wndclass))

        host_hwnd = user32.CreateWindowExW(
            0,
            class_name,
            title,
            WS_OVERLAPPEDWINDOW | WS_VISIBLE,
            100,
            100,
            width,
            height,
            None,
            None,
            h_instance,
            None,
        )

        if not host_hwnd:
            logger.error("Failed to create host window")
            return None

        if big_icon_handle is not None:
            user32.SendMessageW(host_hwnd, WM_SETICON, ICON_BIG, big_icon_handle)
        if small_icon_handle is not None:
            user32.SendMessageW(host_hwnd, WM_SETICON, ICON_SMALL, small_icon_handle)

        client_rect = wintypes.RECT()
        user32.GetClientRect(host_hwnd, ctypes.byref(client_rect))
        client_w = client_rect.right - client_rect.left
        client_h = client_rect.bottom - client_rect.top

        user32.SetParent(flutter_hwnd, host_hwnd)
        user32.SetWindowLongPtrW(flutter_hwnd, GWL_STYLE, WS_CHILD | WS_VISIBLE)
        user32.SetWindowPos(
            flutter_hwnd,
            None,
            0,
            0,
            client_w,
            client_h,
            SWP_NOZORDER | SWP_SHOWWINDOW | SWP_FRAMECHANGED,
        )
        user32.ShowWindow(flutter_hwnd, SW_SHOW)
        user32.UpdateWindow(flutter_hwnd)

        user32.ShowWindow(host_hwnd, SW_SHOW)
        user32.UpdateWindow(host_hwnd)

        user32.SetFocus(flutter_hwnd)

        self.flutter.FlutterDesktopViewControllerForceRedraw(self.view_controller)

        return host_hwnd

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
        hwnd, scaled_width, scaled_height, title = self._setup_engine(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            async_mode=False,
        )
        if hwnd is None:
            return False

        close_error = [None]
        self._run_message_loop(
            hwnd,
            scaled_width,
            scaled_height,
            title,
            icon_path,
            on_initilized,
            on_close,
            close_error,
        )
        if close_error[0] is not None:
            raise close_error[0]
        return True

    def _run_message_loop(
        self,
        hwnd,
        width,
        height,
        title,
        icon_path,
        on_initilized,
        on_close,
        close_error,
    ):
        user32 = ctypes.windll.user32

        def handle_close():
            if on_close is None:
                return False
            try:
                on_close()
            except Exception as exc:
                if close_error[0] is None:
                    close_error[0] = exc
            return False

        host_hwnd = self._create_host_window(
            hwnd,
            width,
            height,
            title,
            icon_path,
            on_close=handle_close,
            on_destroy=lambda: user32.PostQuitMessage(0),
        )
        if not host_hwnd:
            return False

        if on_initilized is not None:
            on_initilized()

        msg = MSG()
        self._running = True

        while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

            if msg.message == WM_QUIT:
                break

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
        hwnd, scaled_width, scaled_height, title = self._setup_engine(
            method_call_handler,
            flutter_asset_path,
            width,
            height,
            title,
            async_mode=True,
        )
        if hwnd is None:
            return False

        if loop is None:
            loop = asyncio.get_running_loop()

        await self._run_async_message_loop(
            hwnd,
            scaled_width,
            scaled_height,
            title,
            icon_path,
            on_initilized,
            on_close,
            loop,
        )
        return True

    async def _run_async_message_loop(
        self,
        hwnd,
        width,
        height,
        title,
        icon_path,
        on_initilized,
        on_close,
        loop: asyncio.AbstractEventLoop,
    ):
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32

        should_quit = False
        close_requested = False
        close_error = None
        host_hwnd = None

        def handle_close():
            nonlocal close_requested
            close_requested = True
            return True

        def handle_destroy():
            nonlocal should_quit
            should_quit = True
            user32.PostQuitMessage(0)

        host_hwnd = self._create_host_window(
            hwnd,
            width,
            height,
            title,
            icon_path,
            on_close=handle_close,
            on_destroy=handle_destroy,
        )
        if not host_hwnd:
            return False

        if on_initilized is not None:
            await on_initilized()

        wake_bridge = ProactorWakeEvent()
        wake_event = wake_bridge.setup(loop)

        iocp_poller = IOCPPollerThread()
        proactor = getattr(loop, "_proactor", None)
        if proactor is not None:
            iocp_handle = proactor._iocp
            iocp_poller.start(iocp_handle, wake_event)

        def drain_io():
            if proactor is None:
                return False
            had_work = False
            while iocp_poller._relay:
                had_work = True
                err, transferred, key, address = iocp_poller._relay.popleft()
                try:
                    f, ov, obj, callback = proactor._cache.pop(address)
                except KeyError:
                    continue
                if obj in proactor._stopped_serving:
                    f.cancel()
                elif not f.done():
                    try:
                        value = callback(transferred, key, ov)
                    except OSError as e:
                        f.set_exception(e)
                        proactor._results.append(f)
                    else:
                        f.set_result(value)
                        proactor._results.append(f)
            for ov in proactor._unregistered:
                proactor._cache.pop(ov.address, None)
            proactor._unregistered.clear()
            return had_work

        msg = MSG()
        handles_array = (wintypes.HANDLE * 1)(wake_event)

        self._running = True

        try:
            while not should_quit:
                while user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, PM_REMOVE):
                    if msg.message == WM_QUIT:
                        should_quit = True
                        break
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageW(ctypes.byref(msg))

                if should_quit:
                    break

                if close_requested:
                    close_requested = False
                    if on_close is not None:
                        try:
                            await on_close()
                        except Exception as exc:
                            if close_error is None:
                                close_error = exc
                    if host_hwnd is not None:
                        user32.DestroyWindow(host_hwnd)
                    continue

                had_io = drain_io()

                await asyncio.sleep(0)

                while user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, PM_REMOVE):
                    if msg.message == WM_QUIT:
                        should_quit = True
                        break
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageW(ctypes.byref(msg))

                if should_quit:
                    break

                if had_io or loop._ready:
                    continue

                timeout_ms = INFINITE
                scheduled = getattr(loop, "_scheduled", [])
                for handle in scheduled:
                    if not handle._cancelled:
                        delay_sec = handle._when - loop.time()
                        if delay_sec <= 0:
                            timeout_ms = 1
                        else:
                            timeout_ms = max(1, int(delay_sec * 1000))
                        break

                if loop._ready:
                    continue

                result = user32.MsgWaitForMultipleObjectsEx(
                    1,
                    handles_array,
                    timeout_ms,
                    QS_ALLINPUT,
                    MWMO_INPUTAVAILABLE,
                )

                if result == WAIT_FAILED:
                    error = kernel32.GetLastError()
                    logger.error("MsgWaitForMultipleObjectsEx failed: %s", error)
                    break

        finally:
            iocp_poller.stop()
            drain_io()
            wake_bridge.cleanup()

        if close_error is not None:
            raise close_error

        return True

    def shutdown(self):
        user32 = ctypes.windll.user32
        while self._icon_handles:
            user32.DestroyIcon(self._icon_handles.pop())
        if self._gdiplus is not None and self._gdiplus_token.value:
            self._gdiplus.GdiplusShutdown(self._gdiplus_token)
            self._gdiplus_token = ctypes.c_size_t()

        if self.view_controller:
            self.flutter.FlutterDesktopViewControllerDestroy(self.view_controller)
            self.view_controller = None
            self.engine = None
        elif self.engine:
            self.flutter.FlutterDesktopEngineDestroy(self.engine)
            self.engine = None

    @staticmethod
    def get_default_assets_path() -> str:
        return PATH_FLUT_ASSETS
