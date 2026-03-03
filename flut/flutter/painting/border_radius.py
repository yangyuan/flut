from typing import Optional, override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class _BorderRadius(FlutValueObject):
    _flut_type = "BorderRadius"

    def __init__(
        self,
        *,
        topLeft: float = 0.0,
        topRight: float = 0.0,
        bottomLeft: float = 0.0,
        bottomRight: float = 0.0,
    ):
        super().__init__()
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    @staticmethod
    def circular(radius):
        return _BorderRadius(
            topLeft=radius, topRight=radius, bottomLeft=radius, bottomRight=radius
        )

    @staticmethod
    def all(radius):
        return _BorderRadius.circular(radius)

    @staticmethod
    def horizontal(*, left: float = 0.0, right: float = 0.0):
        return _BorderRadius(
            topLeft=left, topRight=right, bottomLeft=left, bottomRight=right
        )

    @staticmethod
    def vertical(*, top: float = 0.0, bottom: float = 0.0):
        return _BorderRadius(
            topLeft=top, topRight=top, bottomLeft=bottom, bottomRight=bottom
        )

    def copyWith(
        self,
        *,
        topLeft: float = None,
        topRight: float = None,
        bottomLeft: float = None,
        bottomRight: float = None,
    ) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=topLeft if topLeft is not None else self.topLeft,
            topRight=topRight if topRight is not None else self.topRight,
            bottomLeft=bottomLeft if bottomLeft is not None else self.bottomLeft,
            bottomRight=bottomRight if bottomRight is not None else self.bottomRight,
        )

    @staticmethod
    def lerp(a, b, t: float):
        if a is None and b is None:
            return None
        if a is None:
            return _BorderRadius(
                topLeft=b.topLeft * t,
                topRight=b.topRight * t,
                bottomLeft=b.bottomLeft * t,
                bottomRight=b.bottomRight * t,
            )
        if b is None:
            s = 1.0 - t
            return _BorderRadius(
                topLeft=a.topLeft * s,
                topRight=a.topRight * s,
                bottomLeft=a.bottomLeft * s,
                bottomRight=a.bottomRight * s,
            )
        return _BorderRadius(
            topLeft=a.topLeft + (b.topLeft - a.topLeft) * t,
            topRight=a.topRight + (b.topRight - a.topRight) * t,
            bottomLeft=a.bottomLeft + (b.bottomLeft - a.bottomLeft) * t,
            bottomRight=a.bottomRight + (b.bottomRight - a.bottomRight) * t,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=_flut_unpack_required_field(data, "topLeft"),
            topRight=_flut_unpack_required_field(data, "topRight"),
            bottomLeft=_flut_unpack_required_field(data, "bottomLeft"),
            bottomRight=_flut_unpack_required_field(data, "bottomRight"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["topLeft"] = _flut_pack_value(self.topLeft)
        result["topRight"] = _flut_pack_value(self.topRight)
        result["bottomLeft"] = _flut_pack_value(self.bottomLeft)
        result["bottomRight"] = _flut_pack_value(self.bottomRight)
        return result

    def __eq__(self, other):
        if isinstance(other, _BorderRadius):
            return (
                self.topLeft == other.topLeft
                and self.topRight == other.topRight
                and self.bottomLeft == other.bottomLeft
                and self.bottomRight == other.bottomRight
            )
        return False

    def __hash__(self):
        return hash((self.topLeft, self.topRight, self.bottomLeft, self.bottomRight))

    def __repr__(self):
        return f"BorderRadius(topLeft={self.topLeft}, topRight={self.topRight}, bottomLeft={self.bottomLeft}, bottomRight={self.bottomRight})"


class BorderRadius(_BorderRadius):
    zero = _BorderRadius()
