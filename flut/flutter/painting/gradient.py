from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.dart.ui import Color, TileMode
from .alignment import Alignment


class GradientTransform(FlutValueObject):
    _flut_type = "GradientTransform"

    def __init__(self):
        super().__init__()

    def transform(self, bounds, *, textDirection=None):
        raise NotImplementedError


class LinearGradient(FlutValueObject):
    _flut_type = "LinearGradient"

    def __init__(
        self,
        *,
        begin=Alignment.centerLeft,
        end=Alignment.centerRight,
        colors: list[Color],
        stops: Optional[list[float]] = None,
        tileMode: TileMode = TileMode.clamp,
        transform: Optional[GradientTransform] = None,
    ):
        super().__init__()
        self.begin = begin
        self.end = end
        self.colors = colors
        self.stops = stops
        self.tileMode = tileMode
        self.transform = transform

    @staticmethod
    def _flut_unpack(data: dict) -> "LinearGradient":
        return LinearGradient(
            begin=_flut_unpack_required_field(data, "begin"),
            end=_flut_unpack_required_field(data, "end"),
            colors=_flut_unpack_required_field(data, "colors"),
            stops=_flut_unpack_optional_field(data, "stops"),
            tileMode=_flut_unpack_required_field(data, "tileMode"),
            transform=_flut_unpack_optional_field(data, "transform"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["begin"] = _flut_pack_value(self.begin)
        result["end"] = _flut_pack_value(self.end)
        result["colors"] = _flut_pack_value(self.colors)
        if self.stops is not None:
            result["stops"] = _flut_pack_value(self.stops)
        result["tileMode"] = _flut_pack_value(self.tileMode)
        if self.transform is not None:
            result["transform"] = _flut_pack_value(self.transform)
        return result


class RadialGradient(FlutValueObject):
    _flut_type = "RadialGradient"

    def __init__(
        self,
        *,
        center=Alignment.center,
        radius: float = 0.5,
        colors: list[Color],
        stops: Optional[list[float]] = None,
        tileMode: TileMode = TileMode.clamp,
        focal=None,
        focalRadius: float = 0.0,
        transform: Optional[GradientTransform] = None,
    ):
        super().__init__()
        self.center = center
        self.radius = radius
        self.colors = colors
        self.stops = stops
        self.tileMode = tileMode
        self.focal = focal
        self.focalRadius = focalRadius
        self.transform = transform

    @staticmethod
    def _flut_unpack(data: dict) -> "RadialGradient":
        return RadialGradient(
            center=_flut_unpack_required_field(data, "center"),
            radius=_flut_unpack_required_field(data, "radius"),
            colors=_flut_unpack_required_field(data, "colors"),
            stops=_flut_unpack_optional_field(data, "stops"),
            tileMode=_flut_unpack_required_field(data, "tileMode"),
            focal=_flut_unpack_optional_field(data, "focal"),
            focalRadius=_flut_unpack_required_field(data, "focalRadius"),
            transform=_flut_unpack_optional_field(data, "transform"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["center"] = _flut_pack_value(self.center)
        result["radius"] = _flut_pack_value(self.radius)
        result["colors"] = _flut_pack_value(self.colors)
        if self.stops is not None:
            result["stops"] = _flut_pack_value(self.stops)
        result["tileMode"] = _flut_pack_value(self.tileMode)
        if self.focal is not None:
            result["focal"] = _flut_pack_value(self.focal)
        result["focalRadius"] = _flut_pack_value(self.focalRadius)
        if self.transform is not None:
            result["transform"] = _flut_pack_value(self.transform)
        return result


class GradientRotation(GradientTransform):
    _flut_type = "GradientRotation"

    def __init__(self, radians: float):
        super().__init__()
        self.radians = radians

    @staticmethod
    def _flut_unpack(data: dict) -> "GradientRotation":
        return GradientRotation(
            radians=_flut_unpack_required_field(data, "radians"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["radians"] = _flut_pack_value(self.radians)
        return result


class SweepGradient(FlutValueObject):
    _flut_type = "SweepGradient"

    def __init__(
        self,
        *,
        center=Alignment.center,
        startAngle: float = 0.0,
        endAngle: float = 6.283185307179586,
        colors: list[Color],
        stops: Optional[list[float]] = None,
        tileMode: TileMode = TileMode.clamp,
        transform: Optional[GradientTransform] = None,
    ):
        super().__init__()
        self.center = center
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.colors = colors
        self.stops = stops
        self.tileMode = tileMode
        self.transform = transform

    @staticmethod
    def _flut_unpack(data: dict) -> "SweepGradient":
        return SweepGradient(
            center=_flut_unpack_required_field(data, "center"),
            startAngle=_flut_unpack_required_field(data, "startAngle"),
            endAngle=_flut_unpack_required_field(data, "endAngle"),
            colors=_flut_unpack_required_field(data, "colors"),
            stops=_flut_unpack_optional_field(data, "stops"),
            tileMode=_flut_unpack_required_field(data, "tileMode"),
            transform=_flut_unpack_optional_field(data, "transform"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["center"] = _flut_pack_value(self.center)
        result["startAngle"] = _flut_pack_value(self.startAngle)
        result["endAngle"] = _flut_pack_value(self.endAngle)
        result["colors"] = _flut_pack_value(self.colors)
        if self.stops is not None:
            result["stops"] = _flut_pack_value(self.stops)
        result["tileMode"] = _flut_pack_value(self.tileMode)
        if self.transform is not None:
            result["transform"] = _flut_pack_value(self.transform)
        return result
