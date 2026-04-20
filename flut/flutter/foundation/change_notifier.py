from typing import Callable, Optional, override

from flut._flut.engine import (
    FlutRealtimeObject,
    FlutAbstractObject,
    _flut_pack_value,
    named_constructor,
)


class Listenable(FlutAbstractObject):
    _flut_type = "Listenable"

    def __init__(self):
        super().__init__()
        self._listenables = None

    @named_constructor
    def merge(cls, listenables):
        inst = cls.__new__(cls)
        Listenable.__init__(inst)
        inst._listenables = list(listenables)
        return inst

    def addListener(self, callback: Callable[[], None]):
        raise NotImplementedError

    def removeListener(self, callback: Callable[[], None]):
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self._flut_init == "merge":
            result["listenables"] = _flut_pack_value(self._listenables)
        return result


class ValueListenable(Listenable):
    _flut_type = "ValueListenable"

    def __init__(self):
        super().__init__()

    @property
    def value(self):
        raise NotImplementedError


class ChangeNotifier(FlutRealtimeObject, Listenable):
    _flut_type = "ChangeNotifier"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        original_init = cls.__init__

        def __init__(self, *args, **kw):
            original_init(self, *args, **kw)
            if self._flut_oid is None:
                self._flut_create()

        cls.__init__ = __init__

    def __init__(self):
        FlutRealtimeObject.__init__(self)

    @property
    def hasListeners(self) -> bool:
        return bool(self._flut_get("hasListeners"))

    def addListener(self, callback: Callable[[], None]):
        self._flut_call_with_callable("addListener", callback, "VoidCallback")

    def removeListener(self, callback: Callable[[], None]):
        self._flut_remove_callable("removeListener", "addListener", callback)

    def dispose(self):
        self._flut_call("dispose")
        FlutRealtimeObject._alive_objects.pop(self._flut_oid, None)

    def notifyListeners(self):
        self._flut_call("notifyListeners")


class ValueNotifier(ChangeNotifier):
    _flut_type = "ValueNotifier"

    def __init__(self, value=None):
        super().__init__()
        self._flut_create(props={"value": _flut_pack_value(value)})

    @property
    def value(self):
        return self._flut_get("value")

    @value.setter
    def value(self, new_value):
        self._flut_set("value", new_value)
