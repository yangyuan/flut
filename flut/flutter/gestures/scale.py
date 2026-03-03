from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Offset
from flut.flutter.gestures.velocity_tracker import Velocity

from typing import Optional, override


class ScaleStartDetails(FlutValueObject):
    _flut_type = "ScaleStartDetails"

    def __init__(
        self,
        *,
        focalPoint=Offset(),
        localFocalPoint=Offset(),
        pointerCount=0,
        sourceTimestamp=None,
    ):
        super().__init__()
        self.focalPoint = focalPoint
        self.localFocalPoint = localFocalPoint
        self.pointerCount = pointerCount
        self.sourceTimestamp = sourceTimestamp

    @staticmethod
    def _flut_unpack(data: dict) -> "ScaleStartDetails":
        return ScaleStartDetails(
            focalPoint=_flut_unpack_required_field(data, "focalPoint"),
            localFocalPoint=_flut_unpack_required_field(data, "localFocalPoint"),
            pointerCount=_flut_unpack_required_field(data, "pointerCount"),
            sourceTimestamp=_flut_unpack_optional_field(data, "sourceTimestamp"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["focalPoint"] = _flut_pack_value(self.focalPoint)
        result["localFocalPoint"] = _flut_pack_value(self.localFocalPoint)
        result["pointerCount"] = self.pointerCount
        if self.sourceTimestamp is not None:
            result["sourceTimestamp"] = _flut_pack_value(self.sourceTimestamp)
        return result


class ScaleUpdateDetails(FlutValueObject):
    _flut_type = "ScaleUpdateDetails"

    def __init__(
        self,
        *,
        focalPoint=Offset(),
        localFocalPoint=Offset(),
        scale=1.0,
        horizontalScale=1.0,
        verticalScale=1.0,
        rotation=0.0,
        pointerCount=0,
        focalPointDelta=Offset(),
        sourceTimestamp=None,
    ):
        super().__init__()
        self.focalPoint = focalPoint
        self.localFocalPoint = localFocalPoint
        self.scale = scale
        self.horizontalScale = horizontalScale
        self.verticalScale = verticalScale
        self.rotation = rotation
        self.pointerCount = pointerCount
        self.focalPointDelta = focalPointDelta
        self.sourceTimestamp = sourceTimestamp

    @staticmethod
    def _flut_unpack(data: dict) -> "ScaleUpdateDetails":
        return ScaleUpdateDetails(
            focalPoint=_flut_unpack_required_field(data, "focalPoint"),
            localFocalPoint=_flut_unpack_required_field(data, "localFocalPoint"),
            scale=_flut_unpack_required_field(data, "scale"),
            horizontalScale=_flut_unpack_required_field(data, "horizontalScale"),
            verticalScale=_flut_unpack_required_field(data, "verticalScale"),
            rotation=_flut_unpack_required_field(data, "rotation"),
            pointerCount=_flut_unpack_required_field(data, "pointerCount"),
            focalPointDelta=_flut_unpack_required_field(data, "focalPointDelta"),
            sourceTimestamp=_flut_unpack_optional_field(data, "sourceTimestamp"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["focalPoint"] = _flut_pack_value(self.focalPoint)
        result["localFocalPoint"] = _flut_pack_value(self.localFocalPoint)
        result["scale"] = self.scale
        result["horizontalScale"] = self.horizontalScale
        result["verticalScale"] = self.verticalScale
        result["rotation"] = self.rotation
        result["pointerCount"] = self.pointerCount
        result["focalPointDelta"] = _flut_pack_value(self.focalPointDelta)
        if self.sourceTimestamp is not None:
            result["sourceTimestamp"] = _flut_pack_value(self.sourceTimestamp)
        return result


class ScaleEndDetails(FlutValueObject):
    _flut_type = "ScaleEndDetails"

    def __init__(
        self,
        *,
        velocity=Velocity.zero,
        pointerCount=0,
        scaleVelocity=0.0,
    ):
        super().__init__()
        self.velocity = velocity
        self.pointerCount = pointerCount
        self.scaleVelocity = scaleVelocity

    @staticmethod
    def _flut_unpack(data: dict) -> "ScaleEndDetails":
        return ScaleEndDetails(
            velocity=_flut_unpack_required_field(data, "velocity"),
            pointerCount=_flut_unpack_required_field(data, "pointerCount"),
            scaleVelocity=_flut_unpack_required_field(data, "scaleVelocity"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["velocity"] = _flut_pack_value(self.velocity)
        result["pointerCount"] = self.pointerCount
        result["scaleVelocity"] = self.scaleVelocity
        return result
