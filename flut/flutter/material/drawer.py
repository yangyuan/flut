from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.widgets.framework import Widget


class Drawer(Widget):
    _flut_type = "Drawer"

    def __init__(
        self,
        *,
        key=None,
        backgroundColor: Optional[Color] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        shape=None,
        width: Optional[float] = None,
        semanticLabel: Optional[str] = None,
        clipBehavior=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.backgroundColor = backgroundColor
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.shape = shape
        self.width = width
        self.semanticLabel = semanticLabel
        self.clipBehavior = clipBehavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
