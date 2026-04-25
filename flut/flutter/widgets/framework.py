import weakref
from typing import Generic, Optional, TypeVar, override
from flut._flut.engine import (
    BuildScope,
    FlutObject,
    FlutRealtimeObject,
    call_dart_static,
    generate_flut_id,
    get_engine,
)
from flut.flutter.foundation.key import ValueKey
from flut.flutter.widgets.ticker_provider import (
    SingleTickerProviderStateMixin,
    TickerProviderStateMixin,
)
from flut.flutter.widgets.automatic_keep_alive import AutomaticKeepAliveClientMixin


class GlobalKey(FlutRealtimeObject):
    _flut_type = "GlobalKey"

    def __init__(self, *, debugLabel: Optional[str] = None):
        super().__init__()
        self._current_widget = None
        props = {}
        if debugLabel is not None:
            props["debugLabel"] = debugLabel
        self._flut_create(props=props)

    @property
    def currentContext(self):
        return self._flut_get("currentContext")

    @property
    def currentState(self):
        result = self._flut_get("currentState")
        if result is None:
            return None
        if isinstance(result, int):
            return FlutRealtimeObject._lookup_oid(result)
        return result

    @property
    def currentWidget(self):
        if self.currentContext is None:
            self._current_widget = None
            return None
        return self._current_widget

    @override
    def _flut_pack(self) -> dict:
        return self._flut_base_props()

    def __repr__(self):
        return f"GlobalKey({self._flut_oid})"


class BuildContext(FlutRealtimeObject):
    _flut_type = "BuildContext"

    def findRenderObject(self):
        return self._flut_call("findRenderObject")

    @override
    def _flut_pack(self) -> dict:
        return self._flut_base_props()


class Widget(FlutObject):

    def __init__(self, key=None):
        super().__init__()
        if isinstance(key, str):
            key = ValueKey(key)
        self._key = key

    @override
    def _flut_base_props(self) -> dict:
        result = super()._flut_base_props()
        if self._key is not None:
            result["key"] = self._key._flut_pack()
            if isinstance(self._key, GlobalKey):
                self._key._current_widget = self
        return result


class StatelessWidget(Widget):
    _flut_type = "StatelessWidget"

    def __init__(self, key=None):
        super().__init__(key=key)

    def build(self, context):
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        pid = generate_flut_id()
        widget_ref = [self]

        def _init_callback(oid, context):
            scope_holder = BuildContext()
            scope_holder._flut_oid = oid
            scope_holder._flut_build_scope = BuildScope()
            FlutRealtimeObject._oid_registry[oid] = weakref.ref(scope_holder)
            FlutRealtimeObject._alive_objects[oid] = scope_holder

            scope = scope_holder._flut_build_scope

            def _build(context, new_pid=None):
                if new_pid is not None:
                    entry = engine.binding_registry.get(new_pid, None)
                    if entry is not None:
                        widget_ref[0] = getattr(entry, "_flut_widget", entry)
                scope._clear_actions(engine)
                previous_scope = engine._current_build_scope
                engine._current_build_scope = scope
                try:
                    built = widget_ref[0].build(context)
                    return built._flut_pack() if built else None
                finally:
                    engine._current_build_scope = previous_scope

            build_cb = scope_holder._register_init_action(_build)

            previous_scope = engine._current_build_scope
            engine._current_build_scope = scope
            try:
                built = widget_ref[0].build(context)
                subtree = built._flut_pack() if built else None
            finally:
                engine._current_build_scope = previous_scope

            return {
                "build_action": build_cb._cid,
                "subtree": subtree,
            }

        _init_callback._flut_widget = self
        engine.binding_registry[pid] = _init_callback
        result = self._flut_base_props()
        result["_flut_pid"] = pid
        result["className"] = f"{type(self).__module__}.{type(self).__qualname__}"
        return result


TWidget = TypeVar("TWidget", bound="StatefulWidget")


class State(FlutRealtimeObject, Generic[TWidget]):
    _flut_type = "State"

    def __init__(self):
        super().__init__()
        self._flut_widget: Optional[TWidget] = None
        self._flut_last_build_context: Optional[BuildContext] = None
        self._flut_build_scope = BuildScope()

    @property
    def widget(self) -> TWidget:
        return self._flut_widget

    @property
    def context(self) -> Optional[BuildContext]:
        return self._flut_last_build_context

    def initState(self):
        pass

    def didUpdateWidget(self, oldWidget: TWidget):
        pass

    def dispose(self):
        pass

    def build(self, context: BuildContext):
        raise NotImplementedError

    def setState(self, fn):
        if fn:
            fn()
        self._flut_call_void_async("setState")

    def _execute_build(self, context, new_pid=None):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")

        if new_pid is not None:
            entry = engine.binding_registry.get(new_pid, None)
            if entry is not None:
                new_widget = getattr(entry, "_flut_widget", entry)
                old_widget = self._flut_widget
                self._flut_widget = new_widget
                self.didUpdateWidget(old_widget)

        self._flut_last_build_context = context
        scope = self._flut_build_scope
        scope._clear_actions(engine)
        previous_scope = engine._current_build_scope
        engine._current_build_scope = scope
        try:
            built = self.build(context)
            return built._flut_pack() if built else None
        finally:
            engine._current_build_scope = previous_scope

    @override
    def _flut_dispose(self):
        try:
            self.dispose()
        finally:
            widget = self._flut_widget
            if widget is not None and widget._key is not None:
                if isinstance(widget._key, GlobalKey):
                    widget._key._current_widget = None
            self._flut_widget = None
            self._flut_last_build_context = None
            super()._flut_dispose()


class StatefulWidget(Widget):
    _flut_type = "StatefulWidget"

    def __init__(self, key=None):
        super().__init__(key=key)

    def createState(self):
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        pid = generate_flut_id()
        widget_ref = self

        def _init_callback(oid, context):
            state = widget_ref.createState()
            state._flut_widget = widget_ref
            state._flut_oid = oid
            FlutRealtimeObject._oid_registry[oid] = weakref.ref(state)
            FlutRealtimeObject._alive_objects[oid] = state

            state.initState()

            def _build(context, new_pid=None):
                return state._execute_build(context, new_pid)

            build_cb = state._register_init_action(_build)

            state._flut_last_build_context = context
            scope = state._flut_build_scope
            previous_scope = engine._current_build_scope
            engine._current_build_scope = scope
            try:
                built = state.build(context)
                subtree = built._flut_pack() if built else None
            finally:
                engine._current_build_scope = previous_scope

            result = {
                "build_action": build_cb._cid,
                "subtree": subtree,
            }

            mixins = []
            if isinstance(
                state, (SingleTickerProviderStateMixin, TickerProviderStateMixin)
            ):
                mixins.append("TickerProviderStateMixin")
            if isinstance(state, AutomaticKeepAliveClientMixin):
                mixins.append("AutomaticKeepAliveClientMixin")
            if mixins:
                result["_flut_mixins"] = mixins

            return result

        _init_callback._flut_widget = self
        engine.binding_registry[pid] = _init_callback
        result = self._flut_base_props()
        result["_flut_pid"] = pid
        result["className"] = f"{type(self).__module__}.{type(self).__qualname__}"
        return result


class _InheritedScopeState(FlutRealtimeObject):
    _flut_type = "InheritedScopeState"

    def __init__(self):
        super().__init__()
        self._flut_widget: Optional["InheritedWidget"] = None
        self._flut_last_build_context: Optional[BuildContext] = None
        self._flut_build_scope = BuildScope()

    @property
    def widget(self):
        return self._flut_widget

    @property
    def context(self) -> Optional[BuildContext]:
        return self._flut_last_build_context

    def build(self, context):
        return self._flut_widget._child

    def _execute_build(self, context, new_pid=None):
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")

        old_widget = self._flut_widget
        should_notify = False

        if new_pid is not None:
            entry = engine.binding_registry.get(new_pid, None)
            if entry is not None:
                new_widget = getattr(entry, "_flut_widget", entry)
                self._flut_widget = new_widget
                should_notify = new_widget.updateShouldNotify(old_widget)

        self._flut_last_build_context = context
        scope = self._flut_build_scope
        scope._clear_actions(engine)
        previous_scope = engine._current_build_scope
        engine._current_build_scope = scope
        try:
            built = self.build(context)
            result = {"subtree": built._flut_pack() if built else None}
            if should_notify:
                result["_flut_should_notify"] = True
            return result
        finally:
            engine._current_build_scope = previous_scope

    @override
    def _flut_dispose(self):
        self._flut_widget = None
        self._flut_last_build_context = None
        super()._flut_dispose()


class InheritedWidget(Widget):
    _flut_type = "InheritedWidget"

    def __init__(self, *, child, key=None):
        super().__init__(key=key)
        self._child = child

    def updateShouldNotify(self, old_widget):
        return True

    @staticmethod
    def _of(context, scope_name):
        oid = call_dart_static(
            "FlutInheritedScope", "of", context._flut_pack(), scope_name
        )
        if oid is None:
            return None
        state = FlutRealtimeObject._lookup_oid(oid)
        if state is None:
            return None
        return state._flut_widget

    @override
    def _flut_pack(self) -> dict:
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Engine is not initialized.")
        pid = generate_flut_id()
        widget_ref = self

        def _init_callback(oid, context):
            state = _InheritedScopeState()
            state._flut_widget = widget_ref
            state._flut_oid = oid
            FlutRealtimeObject._oid_registry[oid] = weakref.ref(state)
            FlutRealtimeObject._alive_objects[oid] = state

            def _build(context, new_pid=None):
                return state._execute_build(context, new_pid)

            build_cb = state._register_init_action(_build)

            state._flut_last_build_context = context
            scope = state._flut_build_scope
            previous_scope = engine._current_build_scope
            engine._current_build_scope = scope
            try:
                built = state.build(context)
                subtree = built._flut_pack() if built else None
            finally:
                engine._current_build_scope = previous_scope

            return {
                "build_action": build_cb._cid,
                "subtree": subtree,
            }

        _init_callback._flut_widget = self
        engine.binding_registry[pid] = _init_callback
        result = self._flut_base_props()
        result["_flut_pid"] = pid
        result["scopeName"] = self.__class__.__name__
        result["className"] = f"{type(self).__module__}.{type(self).__qualname__}"
        return result
