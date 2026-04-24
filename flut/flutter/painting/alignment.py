from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Offset, Rect, Size, TextDirection


class _AlignmentGeometry(FlutValueObject):
    _flut_type = "AlignmentGeometry"

    def __init__(self):
        super().__init__()

    @override
    def _flut_pack(self) -> dict:
        raise NotImplementedError(
            "AlignmentGeometry has no concrete wire form. Pass a concrete subtype."
        )

    @staticmethod
    def _flut_unpack(data: dict):
        raise NotImplementedError(
            "AlignmentGeometry has no concrete wire form. Pass a concrete subtype."
        )

    @staticmethod
    def directional(start: float, y: float):
        return AlignmentDirectional(start, y)

    @staticmethod
    def lerp(a: "_AlignmentGeometry | None", b: "_AlignmentGeometry | None", t: float):
        if a is b:
            return a
        if a is None:
            x = b._x * t
            start = b._start * t
            y = b._y * t
            if start == 0.0:
                return Alignment(x, y)
            if x == 0.0:
                return AlignmentDirectional(start, y)
            raise NotImplementedError(
                "Mixed AlignmentGeometry values are not supported yet. "
                "Only Alignment and AlignmentDirectional are supported."
            )
        if b is None:
            x = a._x * (1.0 - t)
            start = a._start * (1.0 - t)
            y = a._y * (1.0 - t)
            if start == 0.0:
                return Alignment(x, y)
            if x == 0.0:
                return AlignmentDirectional(start, y)
            raise NotImplementedError(
                "Mixed AlignmentGeometry values are not supported yet. "
                "Only Alignment and AlignmentDirectional are supported."
            )
        x = a._x + (b._x - a._x) * t
        start = a._start + (b._start - a._start) * t
        y = a._y + (b._y - a._y) * t
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    @staticmethod
    def xy(x: float, y: float):
        return Alignment(x, y)

    @property
    def _x(self) -> float:
        raise NotImplementedError

    @property
    def _start(self) -> float:
        raise NotImplementedError

    @property
    def _y(self) -> float:
        raise NotImplementedError

    def add(self, other: "_AlignmentGeometry"):
        x = self._x + other._x
        start = self._start + other._start
        y = self._y + other._y
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def resolve(self, direction: TextDirection | None) -> "Alignment":
        if direction == TextDirection.rtl:
            return Alignment(self._x - self._start, self._y)
        return Alignment(self._x + self._start, self._y)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["x"] = _flut_pack_value(self._x)
        result["start"] = _flut_pack_value(self._start)
        result["y"] = _flut_pack_value(self._y)
        return result

    def __add__(self, other: "_AlignmentGeometry"):
        return self.add(other)

    def __neg__(self):
        x = -self._x
        start = -self._start
        y = -self._y
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def __mul__(self, other: float):
        x = self._x * other
        start = self._start * other
        y = self._y * other
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def __truediv__(self, other: float):
        x = self._x / other
        start = self._start / other
        y = self._y / other
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def __floordiv__(self, other: float):
        x = float(int(self._x // other))
        start = float(int(self._start // other))
        y = float(int(self._y // other))
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def __mod__(self, other: float):
        x = self._x % other
        start = self._start % other
        y = self._y % other
        if start == 0.0:
            return Alignment(x, y)
        if x == 0.0:
            return AlignmentDirectional(start, y)
        raise NotImplementedError(
            "Mixed AlignmentGeometry values are not supported yet. "
            "Only Alignment and AlignmentDirectional are supported."
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _AlignmentGeometry):
            return NotImplemented
        return (
            self._x == other._x and self._start == other._start and self._y == other._y
        )

    def __hash__(self) -> int:
        return hash((self._x, self._start, self._y))


class _Alignment(_AlignmentGeometry):
    _flut_type = "Alignment"

    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    @staticmethod
    def _flut_unpack(data: dict) -> "_Alignment":
        return _Alignment(
            x=_flut_unpack_required_field(data, "x"),
            y=_flut_unpack_required_field(data, "y"),
        )

    @property
    def _x(self) -> float:
        return self.x

    @property
    def _start(self) -> float:
        return 0.0

    @property
    def _y(self) -> float:
        return self.y

    def add(self, other: "_AlignmentGeometry"):
        return super().add(other)

    def alongOffset(self, other: Offset) -> Offset:
        center_x = other.dx / 2.0
        center_y = other.dy / 2.0
        return Offset(center_x + self.x * center_x, center_y + self.y * center_y)

    def alongSize(self, other: Size) -> Offset:
        center_x = other.width / 2.0
        center_y = other.height / 2.0
        return Offset(center_x + self.x * center_x, center_y + self.y * center_y)

    def inscribe(self, size: Size, rect: Rect) -> Rect:
        half_width_delta = (rect.width - size.width) / 2.0
        half_height_delta = (rect.height - size.height) / 2.0
        return Rect.fromLTWH(
            rect.left + half_width_delta + self.x * half_width_delta,
            rect.top + half_height_delta + self.y * half_height_delta,
            size.width,
            size.height,
        )

    def resolve(self, direction=None) -> "_Alignment":
        return self

    def withinRect(self, rect: Rect) -> Offset:
        half_width = rect.width / 2.0
        half_height = rect.height / 2.0
        return Offset(
            rect.left + half_width + self.x * half_width,
            rect.top + half_height + self.y * half_height,
        )

    @staticmethod
    def _lerp_double(a: float, b: float, t: float) -> float:
        return a + (b - a) * t

    @staticmethod
    def lerp(
        a: "_Alignment | None", b: "_Alignment | None", t: float
    ) -> "_Alignment | None":
        if a is b:
            return a
        if a is None:
            return _Alignment(
                _Alignment._lerp_double(0.0, b.x, t),
                _Alignment._lerp_double(0.0, b.y, t),
            )
        if b is None:
            return _Alignment(
                _Alignment._lerp_double(a.x, 0.0, t),
                _Alignment._lerp_double(a.y, 0.0, t),
            )
        return _Alignment(
            _Alignment._lerp_double(a.x, b.x, t), _Alignment._lerp_double(a.y, b.y, t)
        )

    def __add__(self, other: "_AlignmentGeometry"):
        return self.add(other)

    def __sub__(self, other: "_Alignment") -> "_Alignment":
        return _Alignment(self.x - other.x, self.y - other.y)

    def __neg__(self) -> "_Alignment":
        return _Alignment(-self.x, -self.y)

    def __mul__(self, other: float) -> "_Alignment":
        return _Alignment(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> "_Alignment":
        return _Alignment(self.x / other, self.y / other)

    def __floordiv__(self, other: float) -> "_Alignment":
        return _Alignment(float(int(self.x // other)), float(int(self.y // other)))

    def __mod__(self, other: float) -> "_Alignment":
        return _Alignment(self.x % other, self.y % other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _AlignmentGeometry):
            return NotImplemented
        return (
            self._x == other._x and self._start == other._start and self._y == other._y
        )

    def __hash__(self) -> int:
        return super().__hash__()

    def __repr__(self) -> str:
        known = {
            (-1.0, -1.0): "Alignment.topLeft",
            (0.0, -1.0): "Alignment.topCenter",
            (1.0, -1.0): "Alignment.topRight",
            (-1.0, 0.0): "Alignment.centerLeft",
            (0.0, 0.0): "Alignment.center",
            (1.0, 0.0): "Alignment.centerRight",
            (-1.0, 1.0): "Alignment.bottomLeft",
            (0.0, 1.0): "Alignment.bottomCenter",
            (1.0, 1.0): "Alignment.bottomRight",
        }
        key = (self.x, self.y)
        if key in known:
            return known[key]
        return f"Alignment({self.x:.1f}, {self.y:.1f})"


class _AlignmentDirectional(_AlignmentGeometry):
    _flut_type = "AlignmentDirectional"

    def __init__(self, start: float, y: float):
        super().__init__()
        self.start = start
        self.y = y

    @staticmethod
    def _flut_unpack(data: dict) -> "_AlignmentDirectional":
        return _AlignmentDirectional(
            start=_flut_unpack_required_field(data, "start"),
            y=_flut_unpack_required_field(data, "y"),
        )

    @property
    def _x(self) -> float:
        return 0.0

    @property
    def _start(self) -> float:
        return self.start

    @property
    def _y(self) -> float:
        return self.y


class AlignmentGeometry(_AlignmentGeometry):
    topLeft = _Alignment(-1.0, -1.0)
    topCenter = _Alignment(0.0, -1.0)
    topRight = _Alignment(1.0, -1.0)
    centerLeft = _Alignment(-1.0, 0.0)
    center = _Alignment(0.0, 0.0)
    centerRight = _Alignment(1.0, 0.0)
    bottomLeft = _Alignment(-1.0, 1.0)
    bottomCenter = _Alignment(0.0, 1.0)
    bottomRight = _Alignment(1.0, 1.0)
    topStart = _AlignmentDirectional(-1.0, -1.0)
    centerStart = _AlignmentDirectional(-1.0, 0.0)
    bottomStart = _AlignmentDirectional(-1.0, 1.0)
    topEnd = _AlignmentDirectional(1.0, -1.0)
    centerEnd = _AlignmentDirectional(1.0, 0.0)
    bottomEnd = _AlignmentDirectional(1.0, 1.0)


class AlignmentDirectional(_AlignmentDirectional, AlignmentGeometry):
    topStart = _AlignmentDirectional(-1.0, -1.0)
    topCenter = _AlignmentDirectional(0.0, -1.0)
    topEnd = _AlignmentDirectional(1.0, -1.0)
    centerStart = _AlignmentDirectional(-1.0, 0.0)
    center = _AlignmentDirectional(0.0, 0.0)
    centerEnd = _AlignmentDirectional(1.0, 0.0)
    bottomStart = _AlignmentDirectional(-1.0, 1.0)
    bottomCenter = _AlignmentDirectional(0.0, 1.0)
    bottomEnd = _AlignmentDirectional(1.0, 1.0)


class Alignment(_Alignment, AlignmentGeometry):
    topLeft = _Alignment(-1.0, -1.0)
    topCenter = _Alignment(0.0, -1.0)
    topRight = _Alignment(1.0, -1.0)
    centerLeft = _Alignment(-1.0, 0.0)
    center = _Alignment(0.0, 0.0)
    centerRight = _Alignment(1.0, 0.0)
    bottomLeft = _Alignment(-1.0, 1.0)
    bottomCenter = _Alignment(0.0, 1.0)
    bottomRight = _Alignment(1.0, 1.0)
