import logging
import os
import sys
import json
import asyncio
import weakref
from typing import override

from flut._flut.native.native import FlutNative
from flut._flut.runtime import flut_unpack

logger = logging.getLogger(__name__)


class _FlutNullType:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return "FlutNull"

    def __bool__(self):
        return False

    def _flut_pack(self):
        return None


FlutNull = _FlutNullType()


def _decode_value(value):
    if isinstance(value, dict) and "_flut_type" in value:
        flut_type = value.get("_flut_type")
        if flut_type == "Double":
            v = value.get("value")
            if v == "inf":
                return float("inf")
            if v == "-inf":
                return float("-inf")
            if v == "nan":
                return float("nan")
            return float(v)
        if flut_type == "Callable":
            cid = value.get("_flut_cid")
            engine = _engine
            if engine is not None and cid is not None:
                entry = engine.binding_registry.get(cid)
                if entry is not None:
                    return entry.callable if isinstance(entry, FlutCallable) else entry
            raise RuntimeError("Unknown callback.")
        oid = value.get("_flut_oid")
        if oid is not None:
            existing = FlutRealtimeObject._lookup_oid(oid)
            if existing is not None:
                return existing
        return flut_unpack(value)
    if isinstance(value, list):
        return [_decode_value(item) for item in value]
    return value


_engine = None


def get_engine():
    return _engine


class BuildScope:
    def __init__(self):
        self._flut_registered_actions = []
        self._flut_deferred_cleanup = []
        self._kept_alive = []

    def _clear_actions(self, engine):
        for cid in self._flut_deferred_cleanup:
            engine.binding_registry.pop(cid, None)
        self._flut_deferred_cleanup = self._flut_registered_actions
        self._flut_registered_actions = []
        self._kept_alive = []

    def _dispose_actions(self, engine):
        for cid in self._flut_deferred_cleanup:
            engine.binding_registry.pop(cid, None)
        self._flut_deferred_cleanup = []
        for cid in self._flut_registered_actions:
            engine.binding_registry.pop(cid, None)
        self._flut_registered_actions = []
        self._kept_alive = []


class FlutterEngine:
    def __init__(self, native, root_widget):
        global _engine

        self._native = native
        self._root_widget = root_widget
        self._dart_call_fn = None
        self._notify_set_state_fn = None
        self._shutting_down = False
        self._action_context = None
        self._event_loop = None
        self._dart_enter_isolate = None
        self._dart_exit_isolate = None
        self._dart_current_isolate = None
        self._dart_isolate_handle = None

        self.binding_registry = {}

        self._current_build_scope = None

        _engine = self

    def call_dart(self, call_type, data):
        if self._dart_call_fn is None:
            raise RuntimeError("Dart call is not registered.")

        entered = False
        if self._dart_current_isolate is not None:
            if not self._dart_current_isolate():
                self._dart_enter_isolate(self._dart_isolate_handle)
                entered = True
        try:
            return self._dart_call_fn(call_type, data)
        finally:
            if entered:
                self._dart_exit_isolate()

    def _setup_dart_call_callback(self, callback_addr):
        self._dart_call_fn = self._native.setup_call_dart(callback_addr)

    def _setup_set_state_notification(self, callback_addr):
        self._notify_set_state_fn = self._native.setup_notify_dart(callback_addr)

    def call_dart_async(self, call_type, data):
        if self._notify_set_state_fn is None:
            if self._shutting_down:
                return
            raise RuntimeError("Set state call is not registered.")
        try:
            msg = {"_type": call_type}
            msg.update(data)
            msg_json = json.dumps(msg)
            self._notify_set_state_fn(msg_json.encode("utf-8"))
        except Exception as e:
            logger.error("Error notifying Dart: %s", e)

    def register_action(self, callback, callable_type=None) -> "FlutCallable":
        if self._current_build_scope is None:
            raise RuntimeError("Action registered outside of build scope.")

        flut_callable = FlutCallable(callback, callable_type=callable_type)
        self._current_build_scope._flut_registered_actions.append(flut_callable._cid)
        return flut_callable

    def register_build_action(self, callback, callable_type=None) -> "FlutCallable":
        if self._current_build_scope is None:
            raise RuntimeError("Action registered outside of build scope.")

        build_scope = self._current_build_scope

        def scoped_callback(*args, **kwargs):
            previous_scope = self._current_build_scope
            self._current_build_scope = build_scope
            try:
                return callback(*args, **kwargs)
            finally:
                self._current_build_scope = previous_scope

        flut_callable = FlutCallable(scoped_callback, callable_type=callable_type)
        self._current_build_scope._flut_registered_actions.append(flut_callable._cid)
        return flut_callable

    def initialize(self):
        logger.info("Flut engine start")
        try:
            self._native.initialize()
        except Exception as e:
            logger.error("Flut engine failed to initialize: %s", e)
            raise
        logger.info("Flut engine ready")

    def run(
        self,
        flutter_asset_path,
        width,
        height,
        title,
        icon_path=None,
        on_initialized=None,
        on_close=None,
    ):
        self._native.run(
            self._handle_method_call,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_initialized=on_initialized,
            on_close=on_close,
        )

    async def run_async(
        self,
        flutter_asset_path,
        width,
        height,
        title,
        icon_path=None,
        on_initialized=None,
        on_close=None,
        loop=None,
    ):
        self._event_loop = loop or asyncio.get_running_loop()
        await self._native.run_async(
            self._handle_method_call,
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_initialized=on_initialized,
            on_close=on_close,
            loop=self._event_loop,
        )

    def shutdown(self):
        global _engine
        self._shutting_down = True
        self._notify_set_state_fn = None
        self._dart_call_fn = None
        self._dart_enter_isolate = None
        self._dart_exit_isolate = None
        self._dart_current_isolate = None
        self._dart_isolate_handle = None
        try:
            self._native.shutdown()
        except Exception as e:
            logger.error("Flut engine failed to shutdown: %s", e)
            raise
        self.binding_registry.clear()
        FlutRealtimeObject._alive_objects.clear()
        FlutRealtimeObject._oid_registry.clear()
        _engine = None
        logger.info("Flut engine shutdown")

    def _process_single_action(self, action_data):
        action_id = action_data.get("id")
        self._action_context = action_data.get("context") or None
        result = None
        try:
            cb = self.binding_registry.get(action_id)
            if callable(cb):

                if action_data.get("args") is not None:
                    args = tuple(_decode_value(a) for a in action_data["args"])
                else:
                    args = ()

                kwargs = {}
                if action_data.get("kwargs") is not None:
                    for k, v in action_data["kwargs"].items():
                        kwargs[k] = _decode_value(v)

                raw_fn = getattr(cb, "_func", cb)
                if asyncio.iscoroutinefunction(raw_fn):
                    if self._event_loop is not None:
                        self._event_loop.create_task(cb(*args, **kwargs))
                    else:
                        logger.error(
                            "Async callback for %s ignored (no event loop - use run_app_async)",
                            action_id,
                        )
                else:
                    result = cb(*args, **kwargs)
            return result
        finally:
            self._action_context = None

    def _handle_method_call(self, request_json):
        try:
            req_type = request_json.get("type")
            data = request_json.get("data") or {}

            ack = request_json.get("_ack")
            if ack is not None:
                try:
                    self._native.trim_notify_keepalive(ack)
                except Exception as e:
                    logger.error("Error trimming notify keepalive: %s", e)

            if req_type == "get_root":
                if self._root_widget is not None:
                    resp = self._root_widget._flut_pack()
                    return json.dumps(resp).encode("utf-8")
                return json.dumps(None).encode("utf-8")

            elif req_type == "register_dart_callback":
                callback_addr = data.get("callback_addr")
                if callback_addr:
                    self._setup_dart_call_callback(callback_addr)
                    return json.dumps({"success": True}).encode("utf-8")
                return json.dumps({"_flut_error": "No callback_addr"}).encode("utf-8")

            elif req_type == "register_set_state_callback":
                callback_addr = data.get("callback_addr")
                if callback_addr:
                    self._setup_set_state_notification(callback_addr)
                    return json.dumps({"success": True}).encode("utf-8")
                return json.dumps({"_flut_error": "No callback_addr"}).encode("utf-8")

            elif req_type == "register_isolate_functions":
                import ctypes

                enter_addr = data.get("enter")
                exit_addr = data.get("exit")
                current_addr = data.get("current")
                isolate_addr = data.get("isolate")
                if (
                    enter_addr is None
                    or exit_addr is None
                    or current_addr is None
                    or isolate_addr is None
                ):
                    return json.dumps(
                        {"_flut_error": "Missing isolate function pointers"}
                    ).encode("utf-8")
                ENTER_FN = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
                EXIT_FN = ctypes.CFUNCTYPE(None)
                CURRENT_FN = ctypes.CFUNCTYPE(ctypes.c_void_p)
                self._dart_enter_isolate = ENTER_FN(enter_addr)
                self._dart_exit_isolate = EXIT_FN(exit_addr)
                self._dart_current_isolate = CURRENT_FN(current_addr)
                self._dart_isolate_handle = ctypes.c_void_p(isolate_addr)
                return json.dumps({"success": True}).encode("utf-8")

            elif req_type == "action":
                result = self._process_single_action(data)

                if result is not None:
                    if hasattr(result, "_flut_pack"):
                        result_value = result._flut_pack()
                    elif isinstance(result, list):
                        result_value = [
                            item._flut_pack() if hasattr(item, "_flut_pack") else item
                            for item in result
                        ]
                    else:
                        result_value = result
                    return json.dumps({"_flut_result": result_value}).encode("utf-8")

                return json.dumps({"status": "ok"}).encode("utf-8")

            elif req_type == "realtime_dispose":
                oid = data.get("oid")
                if oid is not None:
                    obj = FlutRealtimeObject._alive_objects.get(oid)
                    if obj is None:
                        ref = FlutRealtimeObject._oid_registry.get(oid)
                        if ref is not None:
                            obj = ref()
                    if obj is not None:
                        obj._flut_dispose()
                return json.dumps({"status": "ok"}).encode("utf-8")

            elif req_type == "future_complete":
                Future._handle_complete(data)
                return json.dumps({"status": "ok"}).encode("utf-8")

            elif req_type == "release_packing":
                pid = data.get("pid")
                if pid is not None:
                    self.binding_registry.pop(pid, None)
                return json.dumps({"status": "ok"}).encode("utf-8")

            return json.dumps(
                {"_flut_error": "Unknown request type", "type": req_type}
            ).encode("utf-8")

        except Exception as e:
            logger.error("Error handling method call: %s", e, exc_info=True)
            return json.dumps({"_flut_error": str(e)}).encode("utf-8")


def _get_native_and_assets(flutter_asset_path):
    native = FlutNative._create()

    if flutter_asset_path is None:
        flutter_asset_path = native.get_default_assets_path()
        if len(sys.argv) > 1:
            flutter_asset_path = sys.argv[1]

    if not os.path.exists(flutter_asset_path):
        logger.error(
            "Assets not found at: %s. Build the Flutter app first.",
            flutter_asset_path,
        )
        return None, None

    return native, flutter_asset_path


def _resolve_icon_path(icon):
    if icon is None:
        return None

    icon_path = os.path.abspath(os.path.expanduser(os.fspath(icon)))
    extension = os.path.splitext(icon_path)[1].lower()
    if extension not in {".png", ".ico"}:
        raise ValueError("Icon must be a .png or .ico file.")
    if not os.path.exists(icon_path):
        logger.warning(
            "Icon not found at: %s. Falling back to packaged icon.",
            icon_path,
        )
        return None
    return icon_path


def run_app(
    widget,
    flutter_asset_path=None,
    width=800,
    height=600,
    title="Flut",
    icon=None,
    on_initialized=None,
    on_close=None,
):
    native, flutter_asset_path = _get_native_and_assets(flutter_asset_path)
    if native is None:
        return None
    icon_path = _resolve_icon_path(icon)

    engine = FlutterEngine(native, widget)
    engine.initialize()

    try:
        engine.run(
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_initialized=on_initialized,
            on_close=on_close,
        )
    finally:
        engine.shutdown()

    return engine


async def run_app_async(
    widget,
    flutter_asset_path=None,
    width=800,
    height=600,
    title="Flut",
    icon=None,
    on_initialized=None,
    on_close=None,
):
    native, flutter_asset_path = _get_native_and_assets(flutter_asset_path)
    if native is None:
        return None
    icon_path = _resolve_icon_path(icon)

    engine = FlutterEngine(native, widget)
    engine.initialize()

    try:
        await engine.run_async(
            flutter_asset_path,
            width,
            height,
            title,
            icon_path=icon_path,
            on_initialized=on_initialized,
            on_close=on_close,
        )
    finally:
        engine.shutdown()

    return engine


_next_py_oid = 0


def generate_flut_id() -> int:
    global _next_py_oid
    _next_py_oid -= 1
    return _next_py_oid


def named_constructor(fn):
    name = fn.__name__

    def wrapper(cls, *args, **kwargs):
        inst = fn(cls, *args, **kwargs)
        inst._flut_init = name
        return inst

    return classmethod(wrapper)


class FlutObject:
    _flut_type: str

    def __init__(self):
        self._flut_init = None

    def _flut_base_props(self) -> dict:
        result = {"_flut_type": self._flut_type}
        if self._flut_init is not None:
            result["_flut_init"] = self._flut_init
        return result

    def _flut_pack(self) -> dict:
        raise NotImplementedError(f"{type(self).__name__} must implement _flut_pack()")

    def _register_action(
        self,
        callback,
        callable_type: str | None = None,
        base_class: type | None = None,
        method_name: str | None = None,
        args: tuple = (),
    ) -> "FlutCallable | None":
        if method_name is not None and base_class is not None:
            if getattr(type(self), method_name) is getattr(base_class, method_name):
                return None
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        if args:

            def wrapper():
                result = callback(*args)
                if result is not None:
                    return result._flut_pack()
                return None

            return engine.register_action(wrapper, callable_type)
        return engine.register_action(callback, callable_type)

    def _register_build_action(
        self, callback, callable_type: str | None = None
    ) -> "FlutCallable":
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        return engine.register_build_action(callback, callable_type)


def wrap_widget_builder(builder):
    def _wrapper(context):
        built = builder(context)
        if built is not None:
            return built._flut_pack()
        return None

    return _wrapper


def wrap_indexed_widget_builder(builder):
    def _wrapper(context, index):
        built = builder(context, index)
        if built is not None:
            return built._flut_pack()
        return None

    return _wrapper


def wrap_layout_widget_builder(builder):
    def _wrapper(context, constraints):
        built = builder(context, constraints)
        if built is not None:
            return built._flut_pack()
        return None

    return _wrapper


def wrap_value_widget_builder(builder):
    def _wrapper(context, value):
        built = builder(context, value)
        if built is not None:
            return built._flut_pack()
        return None

    return _wrapper


def wrap_popup_menu_item_builder(builder):
    def _wrapper(context):
        items = builder(context)
        if items is not None:
            return [item._flut_pack() for item in items]
        return []

    return _wrapper


def _flut_pack_value(value):
    if isinstance(value, FlutObject):
        return value._flut_pack()
    if isinstance(value, float):
        if value == float("inf"):
            return {"_flut_type": "Double", "value": "inf"}
        if value == float("-inf"):
            return {"_flut_type": "Double", "value": "-inf"}
        if value != value:
            return {"_flut_type": "Double", "value": "nan"}
    if isinstance(value, list):
        return [_flut_pack_value(item) for item in value]
    return value


class FlutValueObject(FlutObject):
    pass


class FlutAbstractObject(FlutObject):
    @classmethod
    def _flut_create_abstract(cls, **overrides):
        inst = cls.__new__(cls)
        cls.__init__(inst)
        for name, fn in overrides.items():
            setattr(inst, name, fn)
        return inst


class FlutSingletonInstance:
    def __get__(self, obj, objtype=None):
        cls = objtype if objtype is not None else type(obj)
        cached = getattr(cls, "_flut_instance", None)
        if cached is not None and cached._flut_oid is not None:
            return cached
        proxy = call_dart_static(cls._flut_type, "instance")
        cls._flut_instance = proxy
        return proxy


def call_dart_static(class_name: str, method_name: str, *args, **kwargs):
    engine = get_engine()
    if engine is None:
        raise RuntimeError("Engine is not initialized.")
    data = {
        "name": f"{class_name}.{method_name}",
        "args": list(args),
    }
    if kwargs:
        data["kwargs"] = kwargs
    result = engine.call_dart("static", data)
    if result and "_flut_error" in result:
        raise RuntimeError(
            f"Dart static call {class_name}.{method_name} failed: {result['_flut_error']}"
        )
    if result and "_flut_value" in result:
        ret = result["_flut_value"]
        if isinstance(ret, dict):
            decoded = flut_unpack(ret)
            return decoded if decoded is not None else ret
        return ret
    return None


class FlutEnumObject(FlutObject):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "_flut_type") or "_flut_type" not in cls.__dict__:
            cls._flut_type = cls.__name__
        for name, annotation in cls.__annotations__.items():
            if annotation == cls.__name__:
                setattr(cls, name, cls(name))

    def __init__(self, value: str):
        super().__init__()
        self._flut_value = value

    def __eq__(self, other):
        return isinstance(other, type(self)) and self._flut_value == other._flut_value

    def __hash__(self):
        return hash(self._flut_value)

    @classmethod
    def _flut_unpack(cls, data: dict):
        return getattr(cls, data["_flut_value"])

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["_flut_value"] = self._flut_value
        return result


def _weakref_bound_method(callback):
    try:
        ref = weakref.ref(callback.__self__)
    except TypeError:
        return callback
    func = callback.__func__

    def wrapper(*args, **kwargs):
        obj = ref()
        if obj is None:
            raise RuntimeError("Callable target has been garbage collected.")
        return func(obj, *args, **kwargs)

    return wrapper


class FlutCallable:
    def __init__(self, callback, callable_type=None):
        self._cid = generate_flut_id()
        self._callable_type = callable_type
        self._disposed = False
        if (
            callable_type is not None
            and hasattr(callback, "__self__")
            and hasattr(callback, "__func__")
        ):
            try:
                self._self_ref = weakref.ref(callback.__self__)
            except TypeError:
                self._self_ref = None
                self._func = callback
                self._register()
                return
            self._func = callback.__func__
        else:
            self._self_ref = None
            self._func = callback
        self._register()

    def _register(self):
        engine = _engine
        if engine is not None:
            engine.binding_registry[self._cid] = self

    @property
    def callable(self):
        if self._func is None:
            return None
        if self._self_ref is None:
            return self._func
        obj = self._self_ref()
        if obj is None:
            raise RuntimeError("Callable target has been garbage collected.")
        return self._func.__get__(obj, type(obj))

    def __call__(self, *args, **kwargs):
        fn = self.callable
        if fn is None:
            raise RuntimeError("Callable has been disposed.")
        return fn(*args, **kwargs)

    def _flut_pack(self):
        result = {"_flut_type": "Callable", "_flut_cid": self._cid}
        if self._callable_type is not None:
            result["_flut_callable_type"] = self._callable_type
        return result

    def dispose(self):
        if self._disposed:
            return
        self._disposed = True
        engine = _engine
        if engine is not None:
            engine.binding_registry.pop(self._cid, None)
        self._func = None
        self._self_ref = None


class FlutRealtimeObject(FlutObject):
    _oid_registry: dict[int, weakref.ref] = {}
    _alive_objects: dict[int, "FlutRealtimeObject"] = {}

    def __init__(self):
        super().__init__()
        self._flut_oid = None
        self._flut_owned_callables = set()
        self._flut_owned_callable_keys = {}

    @classmethod
    def _flut_unpack(cls, data: dict):
        from flut._flut.runtime import _flut_unpack_required_field

        return cls._flut_wrap(_flut_unpack_required_field(data, "_flut_oid"))

    @classmethod
    def _flut_wrap(cls, oid: int):
        inst = cls.__new__(cls)
        FlutRealtimeObject.__init__(inst)
        inst._flut_create(oid=oid)
        return inst

    def _flut_create(self, *, oid=None, props=None, bindings=None):
        if oid is not None:
            self._flut_oid = oid
            FlutRealtimeObject._oid_registry[oid] = weakref.ref(self)
            return
        init_data = dict(props) if props else {}
        if bindings:
            for binding in bindings:
                key = binding[0]
                callback = binding[1]
                if len(binding) > 2 and binding[2] == "build_scope":
                    cb = self._register_init_build_action(callback)
                    if cb is not None:
                        init_data[key] = cb._cid
                elif len(binding) > 2 and isinstance(binding[2], str):
                    callable_type = binding[2]
                    if callback is not None:
                        flut_callable = FlutCallable(
                            callback, callable_type=callable_type
                        )
                        self._own_callable(key, flut_callable)
                        init_data[key] = flut_callable._flut_pack()
                else:
                    base_class = binding[2] if len(binding) > 2 else None
                    method_name = binding[3] if len(binding) > 3 else None
                    cb = self._register_init_action(callback, base_class, method_name)
                    if cb is not None:
                        init_data[key] = cb._flut_pack()
        self._flut_create_dart(**init_data)

    def _flut_create_dart(self, **props):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        data = {"_flut_type": self._flut_type}
        data.update(props)
        result = engine.call_dart("createObject", data)
        if result and "_flut_error" in result:
            raise RuntimeError(
                f"Dart createObject {self._flut_type} failed: {result['_flut_error']}"
            )
        if result and "_flut_oid" in result:
            self._flut_oid = result["_flut_oid"]
            FlutRealtimeObject._oid_registry[self._flut_oid] = weakref.ref(self)
            if hasattr(self, "_flut_build_scope"):
                FlutRealtimeObject._alive_objects[self._flut_oid] = self
            elif engine._current_build_scope is not None:
                engine._current_build_scope._kept_alive.append(self)
        else:
            raise RuntimeError("Failed to create object.")

    def _own_callable(self, key, flut_callable):
        self._flut_owned_callables.add(flut_callable._cid)
        if key is not None:
            self._flut_owned_callable_keys[key] = flut_callable._cid

    def _dispose_owned_callable_for_key(self, key):
        old_cid = self._flut_owned_callable_keys.pop(key, None)
        if old_cid is not None:
            self._flut_owned_callables.discard(old_cid)
            engine = _engine
            if engine is not None:
                entry = engine.binding_registry.get(old_cid)
                if isinstance(entry, FlutCallable):
                    entry.dispose()

    def _flut_call_with_callable(self, method, callback, callable_type):
        fc = FlutCallable(callback, callable_type=callable_type)
        key = ("_callable_arg", method, callback)
        self._own_callable(key, fc)
        self._flut_call(method, fc._flut_pack())

    def _flut_remove_callable(self, remove_method, add_method, callback):
        key = ("_callable_arg", add_method, callback)
        cid = self._flut_owned_callable_keys.get(key)
        if cid is not None:
            self._flut_call(remove_method, cid)
            self._dispose_owned_callable_for_key(key)

    def _register_init_build_action(self, callback):
        if callback is None:
            return None
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        build_scope = BuildScope()
        self._flut_build_scope = build_scope

        def scoped_callback(*args, **kwargs):
            build_scope._clear_actions(engine)
            previous_scope = engine._current_build_scope
            engine._current_build_scope = build_scope
            try:
                return callback(*args, **kwargs)
            finally:
                engine._current_build_scope = previous_scope

        return self._register_init_action(scoped_callback)

    @classmethod
    def _register_static_action(cls, callback):
        if callback is None:
            return None
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        action_id = generate_flut_id()
        engine.binding_registry[action_id] = callback
        return action_id

    def _scope_action(self, action_id):
        if action_id is None:
            return
        engine = _engine
        if engine is not None and engine._current_build_scope is not None:
            engine._current_build_scope._flut_registered_actions.append(action_id)
        elif engine is not None:
            existing_entry = engine.binding_registry.get(action_id)
            if existing_entry is not None:
                if hasattr(existing_entry, "__self__") and hasattr(
                    existing_entry, "__func__"
                ):
                    existing_entry = _weakref_bound_method(existing_entry)
                flut_callable = FlutCallable(existing_entry)
                auto_cid = flut_callable._cid
                flut_callable._cid = action_id
                engine.binding_registry.pop(auto_cid, None)
                engine.binding_registry[action_id] = flut_callable
                self._own_callable(None, flut_callable)

    def _register_init_action(self, callback, base_class=None, method_name=None):
        if callback is None:
            return None
        if method_name is not None and base_class is not None:
            if getattr(type(self), method_name) is getattr(base_class, method_name):
                return None
        if (
            hasattr(callback, "__self__")
            and hasattr(callback, "__func__")
            and callback.__self__ is self
        ):
            callback = _weakref_bound_method(callback)
        flut_callable = FlutCallable(callback)
        self._own_callable(None, flut_callable)
        return flut_callable

    def _unregister_init_action(self, cid):
        engine = _engine
        if engine is not None:
            entry = engine.binding_registry.get(cid)
            if isinstance(entry, FlutCallable):
                entry.dispose()

    def _register_oneshot_action(self, callback):
        flut_callable = FlutCallable(callback)

        def wrapper(*args, **kwargs):
            flut_callable.dispose()
            callback(*args, **kwargs)

        flut_callable._func = wrapper
        return flut_callable._cid

    def _flut_dispose(self):
        oid = self._flut_oid
        if oid is None:
            return
        FlutRealtimeObject._alive_objects.pop(oid, None)
        FlutRealtimeObject._oid_registry.pop(oid, None)
        build_scope = getattr(self, "_flut_build_scope", None)
        if build_scope is not None:
            engine = _engine
            if engine is not None:
                build_scope._dispose_actions(engine)
        engine = _engine
        if engine is not None:
            for cid in self._flut_owned_callables:
                entry = engine.binding_registry.get(cid)
                if isinstance(entry, FlutCallable):
                    entry.dispose()
        self._flut_owned_callables.clear()
        self._flut_owned_callable_keys.clear()
        self._flut_oid = None

    @override
    def _flut_base_props(self) -> dict:
        result = super()._flut_base_props()
        result["_flut_oid"] = self._flut_oid
        return result

    @override
    def _flut_pack(self) -> dict:
        return self._flut_base_props()

    def _flut_get(self, property: str):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        result = engine.call_dart(
            "get", {"_flut_oid": self._flut_oid, "_flut_property": property}
        )
        if result and "_flut_error" in result:
            raise RuntimeError(
                f"Dart get {self._flut_type}.{property} failed: {result['_flut_error']}"
            )
        if result and "_flut_value" in result:
            return _decode_value(result["_flut_value"])
        return None

    def _flut_set(self, property: str, value, callable_type=None):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        self._dispose_owned_callable_for_key(property)
        if callable(value) and not isinstance(value, FlutCallable):
            flut_callable = FlutCallable(value, callable_type=callable_type)
            self._own_callable(property, flut_callable)
            value = flut_callable._flut_pack()
        elif isinstance(value, FlutCallable):
            self._own_callable(property, value)
            value = value._flut_pack()
        else:
            value = _flut_pack_value(value)
        result = engine.call_dart(
            "set",
            {
                "_flut_oid": self._flut_oid,
                "_flut_property": property,
                "_flut_value": value,
            },
        )
        if result and "_flut_error" in result:
            raise RuntimeError(
                f"Dart set {self._flut_type}.{property} failed: {result['_flut_error']}"
            )

    def _flut_call(self, method: str, *args, **kwargs):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        data = {"_flut_oid": self._flut_oid, "_flut_method": method}
        if args:
            data["args"] = [_flut_pack_value(a) for a in args]
        if kwargs:
            data["kwargs"] = {k: _flut_pack_value(v) for k, v in kwargs.items()}
        result = engine.call_dart("call", data)
        if result and "_flut_error" in result:
            raise RuntimeError(
                f"Dart call {self._flut_type}.{method} failed: {result['_flut_error']}"
            )
        if result and "_flut_value" in result:
            return _decode_value(result["_flut_value"])
        return None

    def _flut_call_void_async(self, method: str, *args, **kwargs):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        data = {"_flut_oid": self._flut_oid, "_flut_method": method}
        if args:
            data["args"] = [_flut_pack_value(a) for a in args]
        if kwargs:
            data["kwargs"] = {k: _flut_pack_value(v) for k, v in kwargs.items()}
        engine.call_dart_async("call", data)

    @staticmethod
    def _lookup_oid(oid: int):
        ref = FlutRealtimeObject._oid_registry.get(oid)
        if ref is not None:
            obj = ref()
            if obj is not None:
                return obj
        return None

    def __del__(self):
        try:
            owned = getattr(self, "_flut_owned_callables", ())
            for cid in owned:
                engine = _engine
                if engine is not None:
                    engine.binding_registry.pop(cid, None)
            oid = self._flut_oid
            if oid is None:
                return
            should_release = False
            if FlutRealtimeObject._oid_registry.get(oid) is not None:
                ref = FlutRealtimeObject._oid_registry[oid]
                if ref() is None or ref() is self:
                    FlutRealtimeObject._oid_registry.pop(oid, None)
                    should_release = True
            if should_release:
                engine = _engine
                if engine is not None:
                    engine.call_dart_async("release", {"oids": [oid]})
        except (TypeError, AttributeError):
            pass


class Future(FlutRealtimeObject):
    _flut_type = "Future"
    _registry = {}

    def __init__(self):
        raise TypeError(
            "Future cannot be constructed directly. "
            "It is returned by APIs like Navigator.push()."
        )

    @classmethod
    def _flut_wrap(cls, oid):
        inst = cls.__new__(cls)
        FlutRealtimeObject.__init__(inst)
        inst._flut_create(oid=oid)
        inst._then_callbacks = []
        inst._completed = False
        inst._result = None
        inst._error = None
        return inst

    @property
    def isCompleted(self):
        return self._completed

    @property
    def result(self):
        return self._result

    @property
    def hasError(self):
        return self._error is not None

    @property
    def error(self):
        return self._error

    def then(self, callback):
        if self._completed:
            callback(self._result)
        else:
            Future._registry[self._flut_oid] = self
            self._then_callbacks.append(callback)
        return self

    def _resolve(self, value, error=None):
        self._completed = True
        self._result = value
        self._error = error
        Future._registry.pop(self._flut_oid, None)
        for cb in self._then_callbacks:
            cb(value)
        self._then_callbacks.clear()

    @staticmethod
    def _handle_complete(data):
        oid = data.get("oid")
        if oid is None:
            return
        raw_value = data.get("value")
        error = data.get("error")
        value = None
        if raw_value is not None:
            value = _decode_value(raw_value)
        ref = FlutRealtimeObject._oid_registry.get(oid)
        if ref is not None:
            obj = ref()
            if isinstance(obj, Future):
                obj._resolve(value, error)
                return
        inst = Future._flut_wrap(oid)
        inst._resolve(value, error)
