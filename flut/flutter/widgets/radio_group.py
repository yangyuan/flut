from typing import Callable, Generic, Optional, TypeVar, override

from flut._flut.engine import FlutRealtimeObject, FlutAbstractObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget

T = TypeVar("T")


class RadioGroupRegistry(FlutRealtimeObject, FlutAbstractObject):
    _flut_type = "RadioGroupRegistry"

    def __init__(self):
        FlutRealtimeObject.__init__(self)

    @property
    def groupValue(self):
        return self._flut_get("groupValue")

    @property
    def onChanged(self):
        return self._flut_get("onChanged")


class RadioGroup(Widget, Generic[T]):
    _flut_type = "RadioGroup"

    def __init__(
        self,
        *,
        key=None,
        groupValue: Optional[T] = None,
        onChanged: Callable[[Optional[T]], None],
        child: Widget,
    ):
        super().__init__(key=key)
        self.groupValue = groupValue
        self.onChanged = onChanged
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["groupValue"] = (
            _flut_pack_value(self.groupValue) if self.groupValue is not None else None
        )
        result["onChanged"] = self._register_action(
            self.onChanged, "ValueChanged<dynamic?>"
        )._flut_pack()
        result["child"] = _flut_pack_value(self.child)
        return result
