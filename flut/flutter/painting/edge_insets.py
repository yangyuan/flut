import math
from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Offset, RRect, Radius, Rect, Size, TextDirection, ViewPadding
from flut.flutter.painting.basic_types import Axis


def _canonicalize_edge_insets(
    left: float,
    right: float,
    start: float,
    end: float,
    top: float,
    bottom: float,
):
    if start == 0.0 and end == 0.0:
        return EdgeInsets.fromLTRB(left, top, right, bottom)
    if left == 0.0 and right == 0.0:
        return EdgeInsetsDirectional.fromSTEB(start, top, end, bottom)
    return _MixedEdgeInsets(left, right, start, end, top, bottom)


class _EdgeInsetsGeometry(FlutValueObject):
    _flut_type = "EdgeInsetsGeometry"

    def __init__(self):
        super().__init__()

    @staticmethod
    def _flut_unpack(data: dict):
        return _MixedEdgeInsets(
            _flut_unpack_required_field(data, "left"),
            _flut_unpack_required_field(data, "right"),
            _flut_unpack_required_field(data, "start"),
            _flut_unpack_required_field(data, "end"),
            _flut_unpack_required_field(data, "top"),
            _flut_unpack_required_field(data, "bottom"),
        )

    @staticmethod
    def all(value: float):
        return EdgeInsets.all(value)

    @staticmethod
    def only(
        *, left: float = 0.0, right: float = 0.0, top: float = 0.0, bottom: float = 0.0
    ):
        return EdgeInsets.only(left=left, right=right, top=top, bottom=bottom)

    @staticmethod
    def directional(
        *,
        start: float = 0.0,
        end: float = 0.0,
        top: float = 0.0,
        bottom: float = 0.0,
    ):
        return EdgeInsetsDirectional.only(
            start=start,
            end=end,
            top=top,
            bottom=bottom,
        )

    @staticmethod
    def symmetric(*, vertical: float = 0.0, horizontal: float = 0.0):
        return EdgeInsets.symmetric(vertical=vertical, horizontal=horizontal)

    @staticmethod
    def fromLTRB(left: float, top: float, right: float, bottom: float):
        return EdgeInsets.fromLTRB(left, top, right, bottom)

    @staticmethod
    def fromViewPadding(padding: ViewPadding, devicePixelRatio: float):
        return EdgeInsets.fromViewPadding(padding, devicePixelRatio)

    @staticmethod
    def fromSTEB(start: float, top: float, end: float, bottom: float):
        return EdgeInsetsDirectional.fromSTEB(start, top, end, bottom)

    @property
    def _left(self) -> float:
        raise NotImplementedError()

    @property
    def _right(self) -> float:
        raise NotImplementedError()

    @property
    def _start(self) -> float:
        raise NotImplementedError()

    @property
    def _end(self) -> float:
        raise NotImplementedError()

    @property
    def _top(self) -> float:
        raise NotImplementedError()

    @property
    def _bottom(self) -> float:
        raise NotImplementedError()

    @property
    def isNonNegative(self) -> bool:
        return (
            self._left >= 0.0
            and self._right >= 0.0
            and self._start >= 0.0
            and self._end >= 0.0
            and self._top >= 0.0
            and self._bottom >= 0.0
        )

    @property
    def horizontal(self) -> float:
        return self._left + self._right + self._start + self._end

    @property
    def vertical(self) -> float:
        return self._top + self._bottom

    @property
    def collapsedSize(self) -> Size:
        return Size(self.horizontal, self.vertical)

    @property
    def flipped(self):
        return _canonicalize_edge_insets(
            self._right,
            self._left,
            self._end,
            self._start,
            self._bottom,
            self._top,
        )

    def along(self, axis: Axis) -> float:
        if axis == Axis.horizontal:
            return self.horizontal
        return self.vertical

    def inflateSize(self, size: Size) -> Size:
        return Size(size.width + self.horizontal, size.height + self.vertical)

    def deflateSize(self, size: Size) -> Size:
        return Size(size.width - self.horizontal, size.height - self.vertical)

    def add(self, other: "_EdgeInsetsGeometry"):
        return _canonicalize_edge_insets(
            self._left + other._left,
            self._right + other._right,
            self._start + other._start,
            self._end + other._end,
            self._top + other._top,
            self._bottom + other._bottom,
        )

    def subtract(self, other: "_EdgeInsetsGeometry"):
        return _canonicalize_edge_insets(
            self._left - other._left,
            self._right - other._right,
            self._start - other._start,
            self._end - other._end,
            self._top - other._top,
            self._bottom - other._bottom,
        )

    def clamp(self, min: "_EdgeInsetsGeometry", max: "_EdgeInsetsGeometry"):
        return _canonicalize_edge_insets(
            (
                min._left
                if self._left < min._left
                else max._left if self._left > max._left else self._left
            ),
            (
                min._right
                if self._right < min._right
                else max._right if self._right > max._right else self._right
            ),
            (
                min._start
                if self._start < min._start
                else max._start if self._start > max._start else self._start
            ),
            (
                min._end
                if self._end < min._end
                else max._end if self._end > max._end else self._end
            ),
            (
                min._top
                if self._top < min._top
                else max._top if self._top > max._top else self._top
            ),
            (
                min._bottom
                if self._bottom < min._bottom
                else max._bottom if self._bottom > max._bottom else self._bottom
            ),
        )

    @staticmethod
    def lerp(
        a: "_EdgeInsetsGeometry | None", b: "_EdgeInsetsGeometry | None", t: float
    ):
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        return _canonicalize_edge_insets(
            a._left + (b._left - a._left) * t,
            a._right + (b._right - a._right) * t,
            a._start + (b._start - a._start) * t,
            a._end + (b._end - a._end) * t,
            a._top + (b._top - a._top) * t,
            a._bottom + (b._bottom - a._bottom) * t,
        )

    def resolve(self, direction: TextDirection | None):
        raise NotImplementedError()

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["left"] = _flut_pack_value(self._left)
        result["right"] = _flut_pack_value(self._right)
        result["start"] = _flut_pack_value(self._start)
        result["end"] = _flut_pack_value(self._end)
        result["top"] = _flut_pack_value(self._top)
        result["bottom"] = _flut_pack_value(self._bottom)
        return result

    def __neg__(self):
        return _canonicalize_edge_insets(
            -self._left,
            -self._right,
            -self._start,
            -self._end,
            -self._top,
            -self._bottom,
        )

    def __mul__(self, other: float):
        return _canonicalize_edge_insets(
            self._left * other,
            self._right * other,
            self._start * other,
            self._end * other,
            self._top * other,
            self._bottom * other,
        )

    def __truediv__(self, other: float):
        return _canonicalize_edge_insets(
            self._left / other,
            self._right / other,
            self._start / other,
            self._end / other,
            self._top / other,
            self._bottom / other,
        )

    def __floordiv__(self, other: float):
        return _canonicalize_edge_insets(
            float(math.trunc(self._left / other)),
            float(math.trunc(self._right / other)),
            float(math.trunc(self._start / other)),
            float(math.trunc(self._end / other)),
            float(math.trunc(self._top / other)),
            float(math.trunc(self._bottom / other)),
        )

    def __mod__(self, other: float):
        return _canonicalize_edge_insets(
            self._left % other,
            self._right % other,
            self._start % other,
            self._end % other,
            self._top % other,
            self._bottom % other,
        )

    def __eq__(self, other):
        if isinstance(other, _EdgeInsetsGeometry):
            return (
                self._left == other._left
                and self._right == other._right
                and self._start == other._start
                and self._end == other._end
                and self._top == other._top
                and self._bottom == other._bottom
            )
        return False

    def __hash__(self):
        return hash(
            (self._left, self._right, self._start, self._end, self._top, self._bottom)
        )

    def __repr__(self):
        return (
            f"EdgeInsetsGeometry(left={self._left}, right={self._right}, start={self._start}, "
            f"end={self._end}, top={self._top}, bottom={self._bottom})"
        )


class _MixedEdgeInsets(_EdgeInsetsGeometry):
    def __init__(
        self,
        left: float,
        right: float,
        start: float,
        end: float,
        top: float,
        bottom: float,
    ):
        super().__init__()
        self.left = left
        self.right = right
        self.start = start
        self.end = end
        self.top = top
        self.bottom = bottom

    @property
    def _left(self) -> float:
        return self.left

    @property
    def _right(self) -> float:
        return self.right

    @property
    def _start(self) -> float:
        return self.start

    @property
    def _end(self) -> float:
        return self.end

    @property
    def _top(self) -> float:
        return self.top

    @property
    def _bottom(self) -> float:
        return self.bottom

    def resolve(self, direction: TextDirection | None):
        if direction is None:
            raise ValueError(
                "TextDirection is required to resolve mixed EdgeInsetsGeometry"
            )
        if direction == TextDirection.rtl:
            return EdgeInsets.fromLTRB(
                self.end + self.left, self.top, self.start + self.right, self.bottom
            )
        return EdgeInsets.fromLTRB(
            self.start + self.left, self.top, self.end + self.right, self.bottom
        )


class _EdgeInsets(_EdgeInsetsGeometry):
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
    def fromLTRB(left: float, top: float, right: float, bottom: float) -> "_EdgeInsets":
        return _EdgeInsets(left, top, right, bottom)

    @staticmethod
    def all(value: float):
        return _EdgeInsets.fromLTRB(value, value, value, value)

    @staticmethod
    def symmetric(*, vertical: float = 0.0, horizontal: float = 0.0):
        return _EdgeInsets.fromLTRB(horizontal, vertical, horizontal, vertical)

    @staticmethod
    def only(
        *,
        left: float = 0.0,
        top: float = 0.0,
        right: float = 0.0,
        bottom: float = 0.0,
    ):
        return _EdgeInsets.fromLTRB(left, top, right, bottom)

    @staticmethod
    def fromViewPadding(padding: ViewPadding, devicePixelRatio: float):
        return _EdgeInsets.fromLTRB(
            padding.left / devicePixelRatio,
            padding.top / devicePixelRatio,
            padding.right / devicePixelRatio,
            padding.bottom / devicePixelRatio,
        )

    @property
    def _left(self) -> float:
        return self.left

    @property
    def _right(self) -> float:
        return self.right

    @property
    def _start(self) -> float:
        return 0.0

    @property
    def _end(self) -> float:
        return 0.0

    @property
    def _top(self) -> float:
        return self.top

    @property
    def _bottom(self) -> float:
        return self.bottom

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

    @property
    def flipped(self) -> "_EdgeInsets":
        return _EdgeInsets.fromLTRB(self.right, self.bottom, self.left, self.top)

    def copyWith(
        self,
        *,
        left: float | None = None,
        top: float | None = None,
        right: float | None = None,
        bottom: float | None = None,
    ) -> "_EdgeInsets":
        return _EdgeInsets.only(
            left=self.left if left is None else left,
            top=self.top if top is None else top,
            right=self.right if right is None else right,
            bottom=self.bottom if bottom is None else bottom,
        )

    def deflateRect(self, rect: Rect) -> Rect:
        return Rect.fromLTRB(
            rect.left + self.left,
            rect.top + self.top,
            rect.right - self.right,
            rect.bottom - self.bottom,
        )

    def inflateRect(self, rect: Rect) -> Rect:
        return Rect.fromLTRB(
            rect.left - self.left,
            rect.top - self.top,
            rect.right + self.right,
            rect.bottom + self.bottom,
        )

    def inflateRRect(self, rect: RRect) -> RRect:
        return RRect.fromLTRBAndCorners(
            rect.left - self.left,
            rect.top - self.top,
            rect.right + self.right,
            rect.bottom + self.bottom,
            topLeft=(rect.tlRadius + Radius.elliptical(self.left, self.top)).clamp(
                minimum=Radius.zero
            ),
            topRight=(rect.trRadius + Radius.elliptical(self.right, self.top)).clamp(
                minimum=Radius.zero
            ),
            bottomRight=(
                rect.brRadius + Radius.elliptical(self.right, self.bottom)
            ).clamp(minimum=Radius.zero),
            bottomLeft=(
                rect.blRadius + Radius.elliptical(self.left, self.bottom)
            ).clamp(minimum=Radius.zero),
        )

    def deflateRRect(self, rect: RRect) -> RRect:
        return RRect.fromLTRBAndCorners(
            rect.left + self.left,
            rect.top + self.top,
            rect.right - self.right,
            rect.bottom - self.bottom,
            topLeft=(rect.tlRadius - Radius.elliptical(self.left, self.top)).clamp(
                minimum=Radius.zero
            ),
            topRight=(rect.trRadius - Radius.elliptical(self.right, self.top)).clamp(
                minimum=Radius.zero
            ),
            bottomRight=(
                rect.brRadius - Radius.elliptical(self.right, self.bottom)
            ).clamp(minimum=Radius.zero),
            bottomLeft=(
                rect.blRadius - Radius.elliptical(self.left, self.bottom)
            ).clamp(minimum=Radius.zero),
        )

    def add(self, other: "_EdgeInsetsGeometry"):
        if isinstance(other, _EdgeInsets):
            return self + other
        return super().add(other)

    def subtract(self, other: "_EdgeInsetsGeometry"):
        if isinstance(other, _EdgeInsets):
            return self - other
        return super().subtract(other)

    def clamp(self, min: "_EdgeInsetsGeometry", max: "_EdgeInsetsGeometry"):
        return EdgeInsets.fromLTRB(
            (
                min._left
                if self.left < min._left
                else max._left if self.left > max._left else self.left
            ),
            (
                min._top
                if self.top < min._top
                else max._top if self.top > max._top else self.top
            ),
            (
                min._right
                if self.right < min._right
                else max._right if self.right > max._right else self.right
            ),
            (
                min._bottom
                if self.bottom < min._bottom
                else max._bottom if self.bottom > max._bottom else self.bottom
            ),
        )

    @staticmethod
    def lerp(a: "_EdgeInsets | None", b: "_EdgeInsets | None", t: float):
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        return _EdgeInsets.fromLTRB(
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

    def resolve(self, direction: TextDirection | None) -> "_EdgeInsets":
        return self

    def __add__(self, other):
        if isinstance(other, _EdgeInsets):
            return _EdgeInsets.fromLTRB(
                self.left + other.left,
                self.top + other.top,
                self.right + other.right,
                self.bottom + other.bottom,
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, _EdgeInsets):
            return _EdgeInsets.fromLTRB(
                self.left - other.left,
                self.top - other.top,
                self.right - other.right,
                self.bottom - other.bottom,
            )
        return NotImplemented

    def __neg__(self):
        return _EdgeInsets.fromLTRB(-self.left, -self.top, -self.right, -self.bottom)

    def __mul__(self, other):
        return _EdgeInsets.fromLTRB(
            self.left * other,
            self.top * other,
            self.right * other,
            self.bottom * other,
        )

    def __truediv__(self, other):
        return _EdgeInsets.fromLTRB(
            self.left / other,
            self.top / other,
            self.right / other,
            self.bottom / other,
        )

    def __floordiv__(self, other):
        return _EdgeInsets.fromLTRB(
            float(math.trunc(self.left / other)),
            float(math.trunc(self.top / other)),
            float(math.trunc(self.right / other)),
            float(math.trunc(self.bottom / other)),
        )

    def __mod__(self, other):
        return _EdgeInsets.fromLTRB(
            self.left % other,
            self.top % other,
            self.right % other,
            self.bottom % other,
        )


class _EdgeInsetsDirectional(_EdgeInsetsGeometry):
    _flut_type = "EdgeInsetsDirectional"

    def __init__(
        self,
        start: float = 0.0,
        top: float = 0.0,
        end: float = 0.0,
        bottom: float = 0.0,
    ):
        super().__init__()
        self.start = start
        self.top = top
        self.end = end
        self.bottom = bottom

    @staticmethod
    def _flut_unpack(data: dict) -> "_EdgeInsetsDirectional":
        return _EdgeInsetsDirectional(
            start=_flut_unpack_required_field(data, "start"),
            top=_flut_unpack_required_field(data, "top"),
            end=_flut_unpack_required_field(data, "end"),
            bottom=_flut_unpack_required_field(data, "bottom"),
        )

    @staticmethod
    def fromSTEB(start: float, top: float, end: float, bottom: float):
        return _EdgeInsetsDirectional(start, top, end, bottom)

    @staticmethod
    def only(
        *,
        start: float = 0.0,
        top: float = 0.0,
        end: float = 0.0,
        bottom: float = 0.0,
    ):
        return _EdgeInsetsDirectional.fromSTEB(start, top, end, bottom)

    @staticmethod
    def symmetric(*, horizontal: float = 0.0, vertical: float = 0.0):
        return _EdgeInsetsDirectional.fromSTEB(
            horizontal, vertical, horizontal, vertical
        )

    @staticmethod
    def all(value: float):
        return _EdgeInsetsDirectional.fromSTEB(value, value, value, value)

    @property
    def _left(self) -> float:
        return 0.0

    @property
    def _right(self) -> float:
        return 0.0

    @property
    def _start(self) -> float:
        return self.start

    @property
    def _end(self) -> float:
        return self.end

    @property
    def _top(self) -> float:
        return self.top

    @property
    def _bottom(self) -> float:
        return self.bottom

    @property
    def flipped(self) -> "_EdgeInsetsDirectional":
        return _EdgeInsetsDirectional.fromSTEB(
            self.end, self.bottom, self.start, self.top
        )

    def add(self, other: "_EdgeInsetsGeometry"):
        if isinstance(other, _EdgeInsetsDirectional):
            return self + other
        return super().add(other)

    def subtract(self, other: "_EdgeInsetsGeometry"):
        if isinstance(other, _EdgeInsetsDirectional):
            return self - other
        return super().subtract(other)

    @staticmethod
    def lerp(
        a: "_EdgeInsetsDirectional | None", b: "_EdgeInsetsDirectional | None", t: float
    ):
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        return _EdgeInsetsDirectional.fromSTEB(
            a.start + (b.start - a.start) * t,
            a.top + (b.top - a.top) * t,
            a.end + (b.end - a.end) * t,
            a.bottom + (b.bottom - a.bottom) * t,
        )

    def copyWith(
        self,
        *,
        start: float | None = None,
        top: float | None = None,
        end: float | None = None,
        bottom: float | None = None,
    ):
        return _EdgeInsetsDirectional.only(
            start=self.start if start is None else start,
            top=self.top if top is None else top,
            end=self.end if end is None else end,
            bottom=self.bottom if bottom is None else bottom,
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["start"] = _flut_pack_value(self.start)
        result["top"] = _flut_pack_value(self.top)
        result["end"] = _flut_pack_value(self.end)
        result["bottom"] = _flut_pack_value(self.bottom)
        return result

    def resolve(self, direction: TextDirection | None):
        if direction is None:
            raise ValueError(
                "TextDirection is required to resolve EdgeInsetsDirectional"
            )
        if direction == TextDirection.rtl:
            return EdgeInsets.fromLTRB(self.end, self.top, self.start, self.bottom)
        return EdgeInsets.fromLTRB(self.start, self.top, self.end, self.bottom)

    def __add__(self, other):
        if isinstance(other, _EdgeInsetsDirectional):
            return _EdgeInsetsDirectional.fromSTEB(
                self.start + other.start,
                self.top + other.top,
                self.end + other.end,
                self.bottom + other.bottom,
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, _EdgeInsetsDirectional):
            return _EdgeInsetsDirectional.fromSTEB(
                self.start - other.start,
                self.top - other.top,
                self.end - other.end,
                self.bottom - other.bottom,
            )
        return NotImplemented

    def __neg__(self):
        return _EdgeInsetsDirectional.fromSTEB(
            -self.start, -self.top, -self.end, -self.bottom
        )

    def __mul__(self, other):
        return _EdgeInsetsDirectional.fromSTEB(
            self.start * other,
            self.top * other,
            self.end * other,
            self.bottom * other,
        )

    def __truediv__(self, other):
        return _EdgeInsetsDirectional.fromSTEB(
            self.start / other,
            self.top / other,
            self.end / other,
            self.bottom / other,
        )

    def __floordiv__(self, other):
        return _EdgeInsetsDirectional.fromSTEB(
            float(math.trunc(self.start / other)),
            float(math.trunc(self.top / other)),
            float(math.trunc(self.end / other)),
            float(math.trunc(self.bottom / other)),
        )

    def __mod__(self, other):
        return _EdgeInsetsDirectional.fromSTEB(
            self.start % other,
            self.top % other,
            self.end % other,
            self.bottom % other,
        )


class EdgeInsetsGeometry(_EdgeInsetsGeometry):
    zero = _EdgeInsets(0.0, 0.0, 0.0, 0.0)
    infinity = _MixedEdgeInsets(
        float("inf"),
        float("inf"),
        float("inf"),
        float("inf"),
        float("inf"),
        float("inf"),
    )


class EdgeInsets(_EdgeInsets, EdgeInsetsGeometry):
    zero = _EdgeInsets(0.0, 0.0, 0.0, 0.0)


class EdgeInsetsDirectional(_EdgeInsetsDirectional, EdgeInsetsGeometry):
    zero = _EdgeInsetsDirectional(0.0, 0.0, 0.0, 0.0)
