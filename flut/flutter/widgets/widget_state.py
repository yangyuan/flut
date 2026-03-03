from typing import Generic, TypeVar, override

from flut._flut.engine import (
    FlutAbstractObject,
    FlutEnumObject,
    FlutRealtimeObject,
    _flut_pack_value,
    call_dart_static,
)
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Color
from flut.flutter.foundation.change_notifier import ChangeNotifier

T = TypeVar("T")


class WidgetStateOperators:
    def __and__(self, other: "WidgetStatesConstraint") -> "WidgetStatesConstraint":
        return WidgetStatesConstraint._flut_create_abstract(
            isSatisfiedBy=lambda states: self.isSatisfiedBy(states)
            and other.isSatisfiedBy(states)
        )

    def __or__(self, other: "WidgetStatesConstraint") -> "WidgetStatesConstraint":
        return WidgetStatesConstraint._flut_create_abstract(
            isSatisfiedBy=lambda states: self.isSatisfiedBy(states)
            or other.isSatisfiedBy(states)
        )

    def __invert__(self) -> "WidgetStatesConstraint":
        return WidgetStatesConstraint._flut_create_abstract(
            isSatisfiedBy=lambda states: not self.isSatisfiedBy(states)
        )


class WidgetStatesConstraint(FlutAbstractObject, WidgetStateOperators):
    _flut_type = "WidgetStatesConstraint"

    def __init__(self):
        super().__init__()

    def isSatisfiedBy(self, states: "set[WidgetState]") -> bool:
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        is_satisfied_callable = self._register_action(
            self.isSatisfiedBy,
            base_class=WidgetStatesConstraint,
            method_name="isSatisfiedBy",
        )
        if is_satisfied_callable is not None:
            result["isSatisfiedBy"] = is_satisfied_callable._flut_pack()
        return result


WidgetStateMap = dict[WidgetStatesConstraint, T]


class _WidgetState(FlutEnumObject, WidgetStatesConstraint):
    _flut_type = "WidgetState"

    hovered: "_WidgetState"
    focused: "_WidgetState"
    pressed: "_WidgetState"
    dragged: "_WidgetState"
    selected: "_WidgetState"
    scrolledUnder: "_WidgetState"
    disabled: "_WidgetState"
    error: "_WidgetState"

    any: WidgetStatesConstraint = WidgetStatesConstraint._flut_create_abstract(
        isSatisfiedBy=lambda states: True
    )

    def __init__(self, value: str):
        FlutEnumObject.__init__(self, value)
        WidgetStatesConstraint.__init__(self)

    @override
    def isSatisfiedBy(self, states) -> bool:
        return self in states

    @staticmethod
    def _flut_unpack(data: dict) -> "_WidgetState":
        return _WidgetState(_flut_unpack_required_field(data, "_flut_value"))


class WidgetState:
    hovered = _WidgetState.hovered
    focused = _WidgetState.focused
    pressed = _WidgetState.pressed
    dragged = _WidgetState.dragged
    selected = _WidgetState.selected
    scrolledUnder = _WidgetState.scrolledUnder
    disabled = _WidgetState.disabled
    error = _WidgetState.error
    any = _WidgetState.any
    values = [
        hovered,
        focused,
        pressed,
        dragged,
        selected,
        scrolledUnder,
        disabled,
        error,
    ]


class WidgetStateProperty(FlutRealtimeObject, FlutAbstractObject, Generic[T]):
    _flut_type = "WidgetStateProperty"

    def __init__(self):
        super().__init__()
        self._flut_create(
            bindings=[
                ("resolve", self.resolve),
            ],
        )

    def resolve(self, states):
        raise NotImplementedError

    @staticmethod
    def fromMap(map: WidgetStateMap[T]) -> "WidgetStateProperty[T]":
        return WidgetStatePropertyWith(WidgetStatePropertyWith._map_resolver(map))

    @staticmethod
    def all(value) -> "WidgetStateProperty":
        return WidgetStatePropertyAll(value)

    @staticmethod
    def resolveWith(callback) -> "WidgetStateProperty":
        return WidgetStatePropertyWith(callback)

    @staticmethod
    def resolveAs(value, states):
        if isinstance(value, WidgetStateProperty):
            return value.resolve(states)
        return value

    @staticmethod
    def lerp(a, b, t, lerpFunction):
        if a is None and b is None:
            return None
        return WidgetStatePropertyWith(
            lambda states: lerpFunction(
                a.resolve(states) if a is not None else None,
                b.resolve(states) if b is not None else None,
                t,
            )
        )


class WidgetStatePropertyWith(WidgetStateProperty[T]):

    def __init__(self, resolver):
        self._resolver = resolver
        super().__init__()

    @override
    def resolve(self, states):
        return self._resolver(states)

    @staticmethod
    def _map_resolver(map: WidgetStateMap[T]):
        def resolver(states):
            for constraint, value in map.items():
                if constraint.isSatisfiedBy(states):
                    return value
            return None

        return resolver


class WidgetStatePropertyAll(FlutRealtimeObject, Generic[T]):
    _flut_type = "WidgetStatePropertyAll"

    def __init__(self, value):
        self._value = value
        super().__init__()
        self._flut_create(props={"value": _flut_pack_value(value)})

    def resolve(self, states):
        return self._value


class WidgetStateColor(WidgetStatePropertyWith[Color]):
    _flut_type = "WidgetStateColor"

    @staticmethod
    def transparent():
        return call_dart_static("WidgetStateColor", "transparent")

    @staticmethod
    def fromMap(map: WidgetStateMap[Color]) -> "WidgetStateColor":
        return WidgetStateColor.resolveWith(WidgetStatePropertyWith._map_resolver(map))

    @staticmethod
    def resolveWith(callback) -> "WidgetStateColor":
        action_id = FlutRealtimeObject._register_static_action(callback)
        result = call_dart_static("WidgetStateColor", "resolveWith", action_id)
        result._scope_action(action_id)
        return result


class WidgetStatesController(ChangeNotifier):
    _flut_type = "WidgetStatesController"

    def __init__(self, value=None):
        super().__init__()
        props = {}
        if value is not None:
            props["value"] = _flut_pack_value(value)
        self._flut_create(props=props)

    @property
    def value(self):
        return self._flut_get("value")

    @value.setter
    def value(self, new_value):
        self._flut_set("value", new_value)

    def update(self, state, add):
        self._flut_call("update", state._flut_pack(), add)
