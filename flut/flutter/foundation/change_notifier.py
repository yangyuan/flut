from typing import Callable, Optional

from flut._flut.engine import (
    FlutRealtimeObject,
    FlutAbstractObject,
    _flut_pack_value,
    named_constructor,
)


class Listenable(FlutRealtimeObject, FlutAbstractObject):
    _flut_type = "Listenable"
    _flut_init_props: dict = {}
    _flut_init_bindings: Optional[list] = None

    def __init__(self):
        FlutRealtimeObject.__init__(self)
        self._flut_create(
            props=self._flut_init_props or None,
            bindings=self._flut_init_bindings,
        )

    @named_constructor
    def merge(cls, listenables):
        inst = cls.__new__(cls)
        inst._flut_init_props = {
            "listenables": _flut_pack_value(list(listenables)),
        }
        Listenable.__init__(inst)
        return inst

    def addListener(self, callback: Callable[[], None]):
        self._flut_call_with_callable("addListener", callback, "VoidCallback")

    def removeListener(self, callback: Callable[[], None]):
        self._flut_remove_callable("removeListener", "addListener", callback)


class ValueListenable(Listenable):
    _flut_type = "ValueListenable"

    @property
    def value(self):
        raise NotImplementedError


class ChangeNotifier(Listenable):
    _flut_type = "ChangeNotifier"

    @property
    def hasListeners(self) -> bool:
        return bool(self._flut_get("hasListeners"))

    def dispose(self):
        self._flut_call("dispose")
        FlutRealtimeObject._alive_objects.pop(self._flut_oid, None)

    def notifyListeners(self):
        self._flut_call("notifyListeners")


class ValueNotifier(ChangeNotifier):
    _flut_type = "ValueNotifier"

    def __init__(self, value=None):
        self._flut_init_props = {"value": _flut_pack_value(value)}
        Listenable.__init__(self)

    @property
    def value(self):
        return self._flut_get("value")

    @value.setter
    def value(self, new_value):
        self._flut_set("value", new_value)
