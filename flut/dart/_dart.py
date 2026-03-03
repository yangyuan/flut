import math
from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class Matrix4(FlutValueObject):
    _flut_type = "Matrix4"

    def __init__(
        self,
        arg0: float,
        arg1: float,
        arg2: float,
        arg3: float,
        arg4: float,
        arg5: float,
        arg6: float,
        arg7: float,
        arg8: float,
        arg9: float,
        arg10: float,
        arg11: float,
        arg12: float,
        arg13: float,
        arg14: float,
        arg15: float,
    ):
        super().__init__()
        self._storage = [
            arg0,
            arg1,
            arg2,
            arg3,
            arg4,
            arg5,
            arg6,
            arg7,
            arg8,
            arg9,
            arg10,
            arg11,
            arg12,
            arg13,
            arg14,
            arg15,
        ]

    @property
    def storage(self) -> list[float]:
        return list(self._storage)

    @staticmethod
    def identity() -> "Matrix4":
        return Matrix4(
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def rotationX(radians: float) -> "Matrix4":
        c = math.cos(radians)
        s = math.sin(radians)
        return Matrix4(
            1,
            0,
            0,
            0,
            0,
            c,
            s,
            0,
            0,
            -s,
            c,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def rotationY(radians: float) -> "Matrix4":
        c = math.cos(radians)
        s = math.sin(radians)
        return Matrix4(
            c,
            0,
            -s,
            0,
            0,
            1,
            0,
            0,
            s,
            0,
            c,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def rotationZ(radians: float) -> "Matrix4":
        c = math.cos(radians)
        s = math.sin(radians)
        return Matrix4(
            c,
            s,
            0,
            0,
            -s,
            c,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def translationValues(x: float, y: float, z: float) -> "Matrix4":
        return Matrix4(
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            x,
            y,
            z,
            1,
        )

    @staticmethod
    def diagonal3Values(x: float, y: float, z: float) -> "Matrix4":
        return Matrix4(
            x,
            0,
            0,
            0,
            0,
            y,
            0,
            0,
            0,
            0,
            z,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def skewX(alpha: float) -> "Matrix4":
        return Matrix4(
            1,
            0,
            0,
            0,
            math.tan(alpha),
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def skewY(beta: float) -> "Matrix4":
        return Matrix4(
            1,
            math.tan(beta),
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def skew(alpha: float, beta: float) -> "Matrix4":
        return Matrix4(
            1,
            math.tan(beta),
            0,
            0,
            math.tan(alpha),
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "Matrix4":
        storage = _flut_unpack_required_field(data, "storage")
        return Matrix4(*storage)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["storage"] = _flut_pack_value(self._storage)
        return result
