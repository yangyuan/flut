from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Offset


class _Velocity(FlutValueObject):
    _flut_type = "Velocity"

    def __init__(
        self,
        *,
        pixelsPerSecond: Offset,
    ):
        super().__init__()
        self.pixelsPerSecond = pixelsPerSecond

    def clampMagnitude(self, minValue: float, maxValue: float) -> "Velocity":
        valueSquared = self.pixelsPerSecond.distanceSquared
        if valueSquared > maxValue * maxValue:
            return Velocity(
                pixelsPerSecond=(self.pixelsPerSecond / self.pixelsPerSecond.distance)
                * maxValue
            )
        if valueSquared < minValue * minValue:
            if valueSquared == 0.0:
                return self
            return Velocity(
                pixelsPerSecond=(self.pixelsPerSecond / self.pixelsPerSecond.distance)
                * minValue
            )
        return self

    def __add__(self, other: "Velocity") -> "Velocity":
        return Velocity(pixelsPerSecond=self.pixelsPerSecond + other.pixelsPerSecond)

    def __sub__(self, other: "Velocity") -> "Velocity":
        return Velocity(pixelsPerSecond=self.pixelsPerSecond - other.pixelsPerSecond)

    def __neg__(self) -> "Velocity":
        return Velocity(pixelsPerSecond=-self.pixelsPerSecond)

    def __eq__(self, other):
        if isinstance(other, _Velocity):
            return self.pixelsPerSecond == other.pixelsPerSecond
        return False

    def __hash__(self):
        return hash(self.pixelsPerSecond)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["pixelsPerSecond"] = _flut_pack_value(self.pixelsPerSecond)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "Velocity":
        return Velocity(
            pixelsPerSecond=_flut_unpack_required_field(data, "pixelsPerSecond"),
        )


class Velocity(_Velocity):
    zero = _Velocity(pixelsPerSecond=Offset(0, 0))
