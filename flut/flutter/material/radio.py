from typing import Callable, Generic, Optional, TypeVar, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.services.mouse_cursor import MouseCursor
from flut.flutter.widgets.framework import Widget

T = TypeVar("T")


class Radio(Widget, Generic[T]):
    _flut_type = "Radio"

    def __init__(
        self,
        *,
        key=None,
        value: T,
        groupValue: Optional[T] = None,
        onChanged: Optional[Callable[[Optional[T]], None]] = None,
        mouseCursor: Optional[MouseCursor] = None,
        toggleable: bool = False,
        activeColor: Optional[Color] = None,
        fillColor=None,
        focusColor: Optional[Color] = None,
        hoverColor: Optional[Color] = None,
        overlayColor=None,
        splashRadius: Optional[float] = None,
        materialTapTargetSize=None,
        visualDensity=None,
        focusNode=None,
        autofocus: bool = False,
        enabled: Optional[bool] = None,
        groupRegistry=None,
        backgroundColor=None,
        side=None,
        innerRadius=None,
    ):
        super().__init__(key=key)
        self.value = value
        self.groupValue = groupValue
        self.onChanged = onChanged
        self.mouseCursor = mouseCursor
        self.toggleable = toggleable
        self.activeColor = activeColor
        self.fillColor = fillColor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.overlayColor = overlayColor
        self.splashRadius = splashRadius
        self.materialTapTargetSize = materialTapTargetSize
        self.visualDensity = visualDensity
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.enabled = enabled
        self.groupRegistry = groupRegistry
        self.backgroundColor = backgroundColor
        self.side = side
        self.innerRadius = innerRadius

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        result["onChanged"] = (
            self._register_action(self.onChanged, "ValueChanged<dynamic?>")._flut_pack()
            if self.onChanged is not None
            else None
        )
        result["toggleable"] = _flut_pack_value(self.toggleable)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.groupValue is not None:
            result["groupValue"] = _flut_pack_value(self.groupValue)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.activeColor is not None:
            result["activeColor"] = _flut_pack_value(self.activeColor)
        if self.fillColor is not None:
            result["fillColor"] = _flut_pack_value(self.fillColor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.splashRadius is not None:
            result["splashRadius"] = _flut_pack_value(self.splashRadius)
        if self.materialTapTargetSize is not None:
            result["materialTapTargetSize"] = _flut_pack_value(
                self.materialTapTargetSize
            )
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.enabled is not None:
            result["enabled"] = _flut_pack_value(self.enabled)
        if self.groupRegistry is not None:
            result["groupRegistry"] = _flut_pack_value(self.groupRegistry)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.side is not None:
            result["side"] = _flut_pack_value(self.side)
        if self.innerRadius is not None:
            result["innerRadius"] = _flut_pack_value(self.innerRadius)
        return result
