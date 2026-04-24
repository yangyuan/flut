from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Radius, TextDirection


class _BorderRadiusGeometry(FlutValueObject):
    _flut_type = "BorderRadiusGeometry"

    def __init__(self):
        super().__init__()

    @override
    def _flut_pack(self) -> dict:
        raise NotImplementedError(
            "BorderRadiusGeometry has no concrete wire form. Pass a concrete subtype."
        )

    @staticmethod
    def _flut_unpack(data: dict):
        raise NotImplementedError(
            "BorderRadiusGeometry has no concrete wire form. Pass a concrete subtype."
        )

    @staticmethod
    def all(radius: Radius) -> "_BorderRadius":
        return BorderRadius.all(radius)

    @staticmethod
    def circular(radius: float) -> "_BorderRadius":
        return BorderRadius.circular(radius)

    @staticmethod
    def only(
        *,
        topLeft: Radius = Radius.zero,
        topRight: Radius = Radius.zero,
        bottomLeft: Radius = Radius.zero,
        bottomRight: Radius = Radius.zero,
    ) -> "_BorderRadius":
        return BorderRadius.only(
            topLeft=topLeft,
            topRight=topRight,
            bottomLeft=bottomLeft,
            bottomRight=bottomRight,
        )

    @staticmethod
    def directional(
        *,
        topStart: Radius = Radius.zero,
        topEnd: Radius = Radius.zero,
        bottomStart: Radius = Radius.zero,
        bottomEnd: Radius = Radius.zero,
    ) -> "_BorderRadiusDirectional":
        return BorderRadiusDirectional.only(
            topStart=topStart,
            topEnd=topEnd,
            bottomStart=bottomStart,
            bottomEnd=bottomEnd,
        )

    @staticmethod
    def horizontal(
        *,
        left: Radius | None = None,
        right: Radius | None = None,
        start: Radius | None = None,
        end: Radius | None = None,
    ) -> "_BorderRadiusGeometry":
        assert (left is None and right is None) or (
            start is None and end is None
        ), "The left and right values cannot be used in conjunction with start and end."
        if start is not None or end is not None:
            return BorderRadiusDirectional.horizontal(
                start=start if start is not None else Radius.zero,
                end=end if end is not None else Radius.zero,
            )
        return BorderRadius.horizontal(
            left=left if left is not None else Radius.zero,
            right=right if right is not None else Radius.zero,
        )

    @staticmethod
    def vertical(
        *, top: Radius = Radius.zero, bottom: Radius = Radius.zero
    ) -> "_BorderRadius":
        return BorderRadius.vertical(top=top, bottom=bottom)

    def add(self, other: "_BorderRadiusGeometry") -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    def subtract(self, other: "_BorderRadiusGeometry") -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    @staticmethod
    def lerp(
        a: "_BorderRadiusGeometry | None",
        b: "_BorderRadiusGeometry | None",
        t: float,
    ) -> "_BorderRadiusGeometry | None":
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        if isinstance(a, _BorderRadius) and isinstance(b, _BorderRadius):
            return _BorderRadius.lerp(a, b, t)
        if isinstance(a, _BorderRadiusDirectional) and isinstance(
            b, _BorderRadiusDirectional
        ):
            return _BorderRadiusDirectional.lerp(a, b, t)
        raise TypeError(
            "BorderRadiusGeometry.lerp can only interpolate between two BorderRadius "
            "values or two BorderRadiusDirectional values."
        )

    def resolve(self, direction: TextDirection | None) -> "_BorderRadius":
        raise NotImplementedError()

    def __neg__(self) -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    def __mul__(self, other: float) -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    def __truediv__(self, other: float) -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    def __floordiv__(self, other: float) -> "_BorderRadiusGeometry":
        raise NotImplementedError()

    def __mod__(self, other: float) -> "_BorderRadiusGeometry":
        raise NotImplementedError()


class _BorderRadius(_BorderRadiusGeometry):
    _flut_type = "BorderRadius"

    def __init__(
        self,
        *,
        topLeft: Radius = Radius.zero,
        topRight: Radius = Radius.zero,
        bottomLeft: Radius = Radius.zero,
        bottomRight: Radius = Radius.zero,
    ):
        super().__init__()
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    @staticmethod
    def _flut_unpack(data: dict) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=_flut_unpack_required_field(data, "topLeft"),
            topRight=_flut_unpack_required_field(data, "topRight"),
            bottomLeft=_flut_unpack_required_field(data, "bottomLeft"),
            bottomRight=_flut_unpack_required_field(data, "bottomRight"),
        )

    @staticmethod
    def only(
        *,
        topLeft: Radius = Radius.zero,
        topRight: Radius = Radius.zero,
        bottomLeft: Radius = Radius.zero,
        bottomRight: Radius = Radius.zero,
    ) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=topLeft,
            topRight=topRight,
            bottomLeft=bottomLeft,
            bottomRight=bottomRight,
        )

    @staticmethod
    def all(radius: Radius) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=radius,
            topRight=radius,
            bottomLeft=radius,
            bottomRight=radius,
        )

    @staticmethod
    def circular(radius: float) -> "_BorderRadius":
        return _BorderRadius.all(Radius.circular(radius))

    @staticmethod
    def horizontal(
        *, left: Radius = Radius.zero, right: Radius = Radius.zero
    ) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=left,
            topRight=right,
            bottomLeft=left,
            bottomRight=right,
        )

    @staticmethod
    def vertical(
        *, top: Radius = Radius.zero, bottom: Radius = Radius.zero
    ) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=top,
            topRight=top,
            bottomLeft=bottom,
            bottomRight=bottom,
        )

    def copyWith(
        self,
        *,
        topLeft: Radius | None = None,
        topRight: Radius | None = None,
        bottomLeft: Radius | None = None,
        bottomRight: Radius | None = None,
    ) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=topLeft if topLeft is not None else self.topLeft,
            topRight=topRight if topRight is not None else self.topRight,
            bottomLeft=bottomLeft if bottomLeft is not None else self.bottomLeft,
            bottomRight=bottomRight if bottomRight is not None else self.bottomRight,
        )

    @override
    def add(self, other: "_BorderRadiusGeometry") -> "_BorderRadius":
        if isinstance(other, _BorderRadius):
            return self + other
        raise TypeError(
            "BorderRadius.add only accepts BorderRadius. Resolve the other operand "
            "with resolve(direction) before combining."
        )

    @override
    def subtract(self, other: "_BorderRadiusGeometry") -> "_BorderRadius":
        if isinstance(other, _BorderRadius):
            return self - other
        raise TypeError(
            "BorderRadius.subtract only accepts BorderRadius. Resolve the other "
            "operand with resolve(direction) before combining."
        )

    @staticmethod
    def lerp(
        a: "_BorderRadius | None", b: "_BorderRadius | None", t: float
    ) -> "_BorderRadius | None":
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        return _BorderRadius(
            topLeft=Radius.lerp(a.topLeft, b.topLeft, t),
            topRight=Radius.lerp(a.topRight, b.topRight, t),
            bottomLeft=Radius.lerp(a.bottomLeft, b.bottomLeft, t),
            bottomRight=Radius.lerp(a.bottomRight, b.bottomRight, t),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["topLeft"] = _flut_pack_value(self.topLeft)
        result["topRight"] = _flut_pack_value(self.topRight)
        result["bottomLeft"] = _flut_pack_value(self.bottomLeft)
        result["bottomRight"] = _flut_pack_value(self.bottomRight)
        return result

    @override
    def resolve(self, direction: TextDirection | None) -> "_BorderRadius":
        return self

    def __add__(self, other: "_BorderRadius") -> "_BorderRadius":
        if isinstance(other, _BorderRadius):
            return _BorderRadius(
                topLeft=self.topLeft + other.topLeft,
                topRight=self.topRight + other.topRight,
                bottomLeft=self.bottomLeft + other.bottomLeft,
                bottomRight=self.bottomRight + other.bottomRight,
            )
        return NotImplemented

    def __sub__(self, other: "_BorderRadius") -> "_BorderRadius":
        if isinstance(other, _BorderRadius):
            return _BorderRadius(
                topLeft=self.topLeft - other.topLeft,
                topRight=self.topRight - other.topRight,
                bottomLeft=self.bottomLeft - other.bottomLeft,
                bottomRight=self.bottomRight - other.bottomRight,
            )
        return NotImplemented

    @override
    def __neg__(self) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=-self.topLeft,
            topRight=-self.topRight,
            bottomLeft=-self.bottomLeft,
            bottomRight=-self.bottomRight,
        )

    @override
    def __mul__(self, other: float) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=self.topLeft * other,
            topRight=self.topRight * other,
            bottomLeft=self.bottomLeft * other,
            bottomRight=self.bottomRight * other,
        )

    @override
    def __truediv__(self, other: float) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=self.topLeft / other,
            topRight=self.topRight / other,
            bottomLeft=self.bottomLeft / other,
            bottomRight=self.bottomRight / other,
        )

    @override
    def __floordiv__(self, other: float) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=self.topLeft // other,
            topRight=self.topRight // other,
            bottomLeft=self.bottomLeft // other,
            bottomRight=self.bottomRight // other,
        )

    @override
    def __mod__(self, other: float) -> "_BorderRadius":
        return _BorderRadius(
            topLeft=self.topLeft % other,
            topRight=self.topRight % other,
            bottomLeft=self.bottomLeft % other,
            bottomRight=self.bottomRight % other,
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, _BorderRadius):
            return (
                self.topLeft == other.topLeft
                and self.topRight == other.topRight
                and self.bottomLeft == other.bottomLeft
                and self.bottomRight == other.bottomRight
            )
        return False

    def __hash__(self) -> int:
        return hash((self.topLeft, self.topRight, self.bottomLeft, self.bottomRight))

    def __repr__(self) -> str:
        return (
            f"BorderRadius(topLeft={self.topLeft}, topRight={self.topRight}, "
            f"bottomLeft={self.bottomLeft}, bottomRight={self.bottomRight})"
        )


class _BorderRadiusDirectional(_BorderRadiusGeometry):
    _flut_type = "BorderRadiusDirectional"

    def __init__(
        self,
        *,
        topStart: Radius = Radius.zero,
        topEnd: Radius = Radius.zero,
        bottomStart: Radius = Radius.zero,
        bottomEnd: Radius = Radius.zero,
    ):
        super().__init__()
        self.topStart = topStart
        self.topEnd = topEnd
        self.bottomStart = bottomStart
        self.bottomEnd = bottomEnd

    @staticmethod
    def _flut_unpack(data: dict) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=_flut_unpack_required_field(data, "topStart"),
            topEnd=_flut_unpack_required_field(data, "topEnd"),
            bottomStart=_flut_unpack_required_field(data, "bottomStart"),
            bottomEnd=_flut_unpack_required_field(data, "bottomEnd"),
        )

    @staticmethod
    def only(
        *,
        topStart: Radius = Radius.zero,
        topEnd: Radius = Radius.zero,
        bottomStart: Radius = Radius.zero,
        bottomEnd: Radius = Radius.zero,
    ) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=topStart,
            topEnd=topEnd,
            bottomStart=bottomStart,
            bottomEnd=bottomEnd,
        )

    @staticmethod
    def all(radius: Radius) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=radius,
            topEnd=radius,
            bottomStart=radius,
            bottomEnd=radius,
        )

    @staticmethod
    def circular(radius: float) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional.all(Radius.circular(radius))

    @staticmethod
    def horizontal(
        *, start: Radius = Radius.zero, end: Radius = Radius.zero
    ) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=start,
            topEnd=end,
            bottomStart=start,
            bottomEnd=end,
        )

    @staticmethod
    def vertical(
        *, top: Radius = Radius.zero, bottom: Radius = Radius.zero
    ) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=top,
            topEnd=top,
            bottomStart=bottom,
            bottomEnd=bottom,
        )

    @override
    def add(self, other: "_BorderRadiusGeometry") -> "_BorderRadiusDirectional":
        if isinstance(other, _BorderRadiusDirectional):
            return self + other
        raise TypeError(
            "BorderRadiusDirectional.add only accepts BorderRadiusDirectional. "
            "Resolve the other operand with resolve(direction) before combining."
        )

    @override
    def subtract(self, other: "_BorderRadiusGeometry") -> "_BorderRadiusDirectional":
        if isinstance(other, _BorderRadiusDirectional):
            return self - other
        raise TypeError(
            "BorderRadiusDirectional.subtract only accepts BorderRadiusDirectional. "
            "Resolve the other operand with resolve(direction) before combining."
        )

    @staticmethod
    def lerp(
        a: "_BorderRadiusDirectional | None",
        b: "_BorderRadiusDirectional | None",
        t: float,
    ) -> "_BorderRadiusDirectional | None":
        if a is b:
            return a
        if a is None:
            return b * t
        if b is None:
            return a * (1.0 - t)
        return _BorderRadiusDirectional(
            topStart=Radius.lerp(a.topStart, b.topStart, t),
            topEnd=Radius.lerp(a.topEnd, b.topEnd, t),
            bottomStart=Radius.lerp(a.bottomStart, b.bottomStart, t),
            bottomEnd=Radius.lerp(a.bottomEnd, b.bottomEnd, t),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["topStart"] = _flut_pack_value(self.topStart)
        result["topEnd"] = _flut_pack_value(self.topEnd)
        result["bottomStart"] = _flut_pack_value(self.bottomStart)
        result["bottomEnd"] = _flut_pack_value(self.bottomEnd)
        return result

    @override
    def resolve(self, direction: TextDirection | None) -> "_BorderRadius":
        assert (
            direction is not None
        ), "TextDirection is required to resolve BorderRadiusDirectional."
        if direction == TextDirection.rtl:
            return _BorderRadius(
                topLeft=self.topEnd,
                topRight=self.topStart,
                bottomLeft=self.bottomEnd,
                bottomRight=self.bottomStart,
            )
        return _BorderRadius(
            topLeft=self.topStart,
            topRight=self.topEnd,
            bottomLeft=self.bottomStart,
            bottomRight=self.bottomEnd,
        )

    def __add__(self, other: "_BorderRadiusDirectional") -> "_BorderRadiusDirectional":
        if isinstance(other, _BorderRadiusDirectional):
            return _BorderRadiusDirectional(
                topStart=self.topStart + other.topStart,
                topEnd=self.topEnd + other.topEnd,
                bottomStart=self.bottomStart + other.bottomStart,
                bottomEnd=self.bottomEnd + other.bottomEnd,
            )
        return NotImplemented

    def __sub__(self, other: "_BorderRadiusDirectional") -> "_BorderRadiusDirectional":
        if isinstance(other, _BorderRadiusDirectional):
            return _BorderRadiusDirectional(
                topStart=self.topStart - other.topStart,
                topEnd=self.topEnd - other.topEnd,
                bottomStart=self.bottomStart - other.bottomStart,
                bottomEnd=self.bottomEnd - other.bottomEnd,
            )
        return NotImplemented

    @override
    def __neg__(self) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=-self.topStart,
            topEnd=-self.topEnd,
            bottomStart=-self.bottomStart,
            bottomEnd=-self.bottomEnd,
        )

    @override
    def __mul__(self, other: float) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=self.topStart * other,
            topEnd=self.topEnd * other,
            bottomStart=self.bottomStart * other,
            bottomEnd=self.bottomEnd * other,
        )

    @override
    def __truediv__(self, other: float) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=self.topStart / other,
            topEnd=self.topEnd / other,
            bottomStart=self.bottomStart / other,
            bottomEnd=self.bottomEnd / other,
        )

    @override
    def __floordiv__(self, other: float) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=self.topStart // other,
            topEnd=self.topEnd // other,
            bottomStart=self.bottomStart // other,
            bottomEnd=self.bottomEnd // other,
        )

    @override
    def __mod__(self, other: float) -> "_BorderRadiusDirectional":
        return _BorderRadiusDirectional(
            topStart=self.topStart % other,
            topEnd=self.topEnd % other,
            bottomStart=self.bottomStart % other,
            bottomEnd=self.bottomEnd % other,
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, _BorderRadiusDirectional):
            return (
                self.topStart == other.topStart
                and self.topEnd == other.topEnd
                and self.bottomStart == other.bottomStart
                and self.bottomEnd == other.bottomEnd
            )
        return False

    def __hash__(self) -> int:
        return hash((self.topStart, self.topEnd, self.bottomStart, self.bottomEnd))

    def __repr__(self) -> str:
        return (
            f"BorderRadiusDirectional(topStart={self.topStart}, topEnd={self.topEnd}, "
            f"bottomStart={self.bottomStart}, bottomEnd={self.bottomEnd})"
        )


class BorderRadiusGeometry(_BorderRadiusGeometry):
    zero = _BorderRadius()


class BorderRadius(_BorderRadius, BorderRadiusGeometry):
    zero = _BorderRadius()


class BorderRadiusDirectional(_BorderRadiusDirectional, BorderRadiusGeometry):
    zero = _BorderRadiusDirectional()
