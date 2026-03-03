from typing import Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.dart.core import Duration
from flut.dart.ui import Clip, Color
from flut.flutter.painting.border_radius import BorderRadius
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.widgets.framework import Widget


class MaterialType(FlutEnumObject):
    canvas: "MaterialType"
    card: "MaterialType"
    circle: "MaterialType"
    button: "MaterialType"
    transparency: "MaterialType"


class Material(Widget):
    _flut_type = "Material"

    def __init__(
        self,
        *,
        key=None,
        type: MaterialType = MaterialType.canvas,
        elevation: float = 0.0,
        color: Optional[Color] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        textStyle: Optional[TextStyle] = None,
        borderRadius: Optional[BorderRadius] = None,
        shape=None,
        borderOnForeground: bool = True,
        clipBehavior: Clip = Clip.none,
        animationDuration: Duration = Duration(milliseconds=200),
        animateColor: bool = True,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.type = type
        self.elevation = elevation
        self.color = color
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.textStyle = textStyle
        self.borderRadius = borderRadius
        self.shape = shape
        self.borderOnForeground = borderOnForeground
        self.clipBehavior = clipBehavior
        self.animationDuration = animationDuration
        self.animateColor = animateColor
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["type"] = _flut_pack_value(self.type)
        result["elevation"] = _flut_pack_value(self.elevation)
        result["borderOnForeground"] = _flut_pack_value(self.borderOnForeground)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["animationDuration"] = _flut_pack_value(self.animationDuration)
        result["animateColor"] = _flut_pack_value(self.animateColor)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.textStyle is not None:
            result["textStyle"] = _flut_pack_value(self.textStyle)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
