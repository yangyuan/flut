from typing import List, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget
from flut.flutter.widgets.icon_data import IconData


class Icon(Widget):
    _flut_type = "Icon"

    def __init__(
        self,
        icon: Optional[IconData] = None,
        *,
        key=None,
        size: Optional[float] = None,
        fill: Optional[float] = None,
        weight: Optional[float] = None,
        grade: Optional[float] = None,
        opticalSize: Optional[float] = None,
        color=None,
        shadows: Optional[List] = None,
        semanticLabel: Optional[str] = None,
        textDirection=None,
        applyTextScaling: Optional[bool] = None,
        blendMode=None,
        fontWeight=None,
    ):
        super().__init__(key=key)
        self.icon = icon
        self.size = size
        self.fill = fill
        self.weight = weight
        self.grade = grade
        self.opticalSize = opticalSize
        self.color = color
        self.shadows = shadows
        self.semanticLabel = semanticLabel
        self.textDirection = textDirection
        self.applyTextScaling = applyTextScaling
        self.blendMode = blendMode
        self.fontWeight = fontWeight

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.size is not None:
            result["size"] = _flut_pack_value(self.size)
        if self.fill is not None:
            result["fill"] = _flut_pack_value(self.fill)
        if self.weight is not None:
            result["weight"] = _flut_pack_value(self.weight)
        if self.grade is not None:
            result["grade"] = _flut_pack_value(self.grade)
        if self.opticalSize is not None:
            result["opticalSize"] = _flut_pack_value(self.opticalSize)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.shadows is not None:
            result["shadows"] = _flut_pack_value(self.shadows)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        if self.applyTextScaling is not None:
            result["applyTextScaling"] = _flut_pack_value(self.applyTextScaling)
        if self.blendMode is not None:
            result["blendMode"] = _flut_pack_value(self.blendMode)
        if self.fontWeight is not None:
            result["fontWeight"] = _flut_pack_value(self.fontWeight)
        return result
