from typing import List, Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field
from flut.dart.ui import Color


class IconThemeData(FlutValueObject):
    _flut_type = "IconThemeData"

    def __init__(
        self,
        *,
        size: Optional[float] = None,
        fill: Optional[float] = None,
        weight: Optional[float] = None,
        grade: Optional[float] = None,
        opticalSize: Optional[float] = None,
        color: Optional[Color] = None,
        opacity: Optional[float] = None,
        shadows: Optional[List] = None,
        applyTextScaling: Optional[bool] = None,
    ):
        super().__init__()
        self.size = size
        self.fill = fill
        self.weight = weight
        self.grade = grade
        self.opticalSize = opticalSize
        self.color = color
        self.opacity = opacity
        self.shadows = shadows
        self.applyTextScaling = applyTextScaling

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
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
        if self.opacity is not None:
            result["opacity"] = _flut_pack_value(self.opacity)
        if self.shadows is not None:
            result["shadows"] = _flut_pack_value(self.shadows)
        if self.applyTextScaling is not None:
            result["applyTextScaling"] = _flut_pack_value(self.applyTextScaling)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "IconThemeData":
        return IconThemeData(
            size=_flut_unpack_optional_field(data, "size"),
            fill=_flut_unpack_optional_field(data, "fill"),
            weight=_flut_unpack_optional_field(data, "weight"),
            grade=_flut_unpack_optional_field(data, "grade"),
            opticalSize=_flut_unpack_optional_field(data, "opticalSize"),
            color=_flut_unpack_optional_field(data, "color"),
            opacity=_flut_unpack_optional_field(data, "opacity"),
            shadows=_flut_unpack_optional_field(data, "shadows"),
            applyTextScaling=_flut_unpack_optional_field(data, "applyTextScaling"),
        )
