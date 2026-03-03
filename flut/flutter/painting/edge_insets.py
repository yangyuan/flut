from typing import override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Size, Offset, Rect
from flut.flutter.painting.basic_types import Axis


class _EdgeInsets(FlutValueObject):
    _flut_type = "EdgeInsets"

    def __init__(
        self,
        left: float = 0.0,
        top: float = 0.0,
        right: float = 0.0,
        bottom: float = 0.0,
    ):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @staticmethod
    def _flut_unpack(data: dict) -> "_EdgeInsets":
        return _EdgeInsets(
            left=_flut_unpack_required_field(data, "left"),
            top=_flut_unpack_required_field(data, "top"),
            right=_flut_unpack_required_field(data, "right"),
            bottom=_flut_unpack_required_field(data, "bottom"),
        )

    @staticmethod
    def all(value):
        return _EdgeInsets(value, value, value, value)

    @staticmethod
    def symmetric(*, vertical: float = 0, horizontal: float = 0):
        return _EdgeInsets(horizontal, vertical, horizontal, vertical)

    @staticmethod
    def only(
        *,
        left: float = 0,
        top: float = 0,
        right: float = 0,
        bottom: float = 0,
    ):
        return _EdgeInsets(left, top, right, bottom)

    @staticmethod
    def fromViewPadding(padding, devicePixelRatio: float):
        return _EdgeInsets(
            padding.left / devicePixelRatio,
            padding.top / devicePixelRatio,
            padding.right / devicePixelRatio,
            padding.bottom / devicePixelRatio,
        )

    @property
    def horizontal(self) -> float:
        return self.left + self.right

    @property
    def vertical(self) -> float:
        return self.top + self.bottom

    @property
    def isNonNegative(self) -> bool:
        return self.left >= 0 and self.top >= 0 and self.right >= 0 and self.bottom >= 0

    @property
    def flipped(self) -> "_EdgeInsets":
        return _EdgeInsets(self.right, self.bottom, self.left, self.top)

    @property
    def collapsedSize(self):
        return Size(self.horizontal, self.vertical)

    @property
    def topLeft(self):
        return Offset(self.left, self.top)

    @property
    def topRight(self):
        return Offset(-self.right, self.top)

    @property
    def bottomLeft(self):
        return Offset(self.left, -self.bottom)

    @property
    def bottomRight(self):
        return Offset(-self.right, -self.bottom)

    def copyWith(
        self,
        *,
        left: float = None,
        top: float = None,
        right: float = None,
        bottom: float = None,
    ) -> "_EdgeInsets":
        return _EdgeInsets(
            left if left is not None else self.left,
            top if top is not None else self.top,
            right if right is not None else self.right,
            bottom if bottom is not None else self.bottom,
        )

    def deflateRect(self, rect) -> "object":
        return Rect(
            rect.left + self.left,
            rect.top + self.top,
            rect.right - self.right,
            rect.bottom - self.bottom,
        )

    def inflateRect(self, rect) -> "object":
        return Rect(
            rect.left - self.left,
            rect.top - self.top,
            rect.right + self.right,
            rect.bottom + self.bottom,
        )

    def along(self, axis) -> float:
        if axis == Axis.horizontal:
            return self.horizontal
        return self.vertical

    def resolve(self, direction) -> "_EdgeInsets":
        return self

    @staticmethod
    def lerp(a, b, t: float):
        if a is None and b is None:
            return None
        if a is None:
            return _EdgeInsets(b.left * t, b.top * t, b.right * t, b.bottom * t)
        if b is None:
            s = 1.0 - t
            return _EdgeInsets(a.left * s, a.top * s, a.right * s, a.bottom * s)
        return _EdgeInsets(
            a.left + (b.left - a.left) * t,
            a.top + (b.top - a.top) * t,
            a.right + (b.right - a.right) * t,
            a.bottom + (b.bottom - a.bottom) * t,
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["left"] = _flut_pack_value(self.left)
        result["top"] = _flut_pack_value(self.top)
        result["right"] = _flut_pack_value(self.right)
        result["bottom"] = _flut_pack_value(self.bottom)
        return result

    def __eq__(self, other):
        if isinstance(other, _EdgeInsets):
            return (
                self.left == other.left
                and self.top == other.top
                and self.right == other.right
                and self.bottom == other.bottom
            )
        return False

    def __hash__(self):
        return hash((self.left, self.top, self.right, self.bottom))

    def __repr__(self):
        return f"EdgeInsets({self.left}, {self.top}, {self.right}, {self.bottom})"

    def __add__(self, other):
        if isinstance(other, _EdgeInsets):
            return _EdgeInsets(
                self.left + other.left,
                self.top + other.top,
                self.right + other.right,
                self.bottom + other.bottom,
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, _EdgeInsets):
            return _EdgeInsets(
                self.left - other.left,
                self.top - other.top,
                self.right - other.right,
                self.bottom - other.bottom,
            )
        return NotImplemented

    def __neg__(self):
        return _EdgeInsets(-self.left, -self.top, -self.right, -self.bottom)

    def __mul__(self, other):
        return _EdgeInsets(
            self.left * other, self.top * other, self.right * other, self.bottom * other
        )

    def __mod__(self, other):
        return _EdgeInsets(
            self.left % other, self.top % other, self.right % other, self.bottom % other
        )


class EdgeInsets(_EdgeInsets):
    zero = _EdgeInsets(0, 0, 0, 0)
