from typing import override
from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Color, Paint, PaintingStyle, _lerpDouble


class ShapeBorder(FlutValueObject):
    _flut_type = "ShapeBorder"

    def __init__(self):
        super().__init__()


class BorderStyle(FlutEnumObject):
    solid: "BorderStyle"
    none: "BorderStyle"


class _BorderSide(FlutValueObject):
    _flut_type = "BorderSide"

    strokeAlignInside = -1.0
    strokeAlignCenter = 0.0
    strokeAlignOutside = 1.0

    def __init__(
        self,
        *,
        color: Color = Color(0xFF000000),
        width: float = 1.0,
        style: BorderStyle = BorderStyle.solid,
        strokeAlign: float = -1.0,
    ):
        super().__init__()
        self.color = color
        self.width = width
        self.style = style
        self.strokeAlign = strokeAlign

    @property
    def strokeInset(self) -> float:
        return self.width * (1 - (1 + self.strokeAlign) / 2)

    @property
    def strokeOutset(self) -> float:
        return self.width * (1 + self.strokeAlign) / 2

    @property
    def strokeOffset(self) -> float:
        return self.width * self.strokeAlign

    def copyWith(
        self,
        *,
        color: Color | None = None,
        width: float | None = None,
        style: BorderStyle | None = None,
        strokeAlign: float | None = None,
    ) -> "_BorderSide":
        return _BorderSide(
            color=color if color is not None else self.color,
            width=width if width is not None else self.width,
            style=style if style is not None else self.style,
            strokeAlign=strokeAlign if strokeAlign is not None else self.strokeAlign,
        )

    def scale(self, t: float) -> "_BorderSide":
        return _BorderSide(
            color=self.color,
            width=max(0.0, self.width * t),
            style=BorderStyle.none if t <= 0.0 else self.style,
        )

    def toPaint(self) -> Paint:
        paint = Paint()
        if self.style == BorderStyle.solid:
            paint.color = self.color
            paint.strokeWidth = self.width
            paint.style = PaintingStyle.stroke
        else:
            paint.color = Color(0x00000000)
            paint.strokeWidth = 0.0
            paint.style = PaintingStyle.stroke
        return paint

    @staticmethod
    def canMerge(a: "_BorderSide", b: "_BorderSide") -> bool:
        if (a.style == BorderStyle.none and a.width == 0.0) or (
            b.style == BorderStyle.none and b.width == 0.0
        ):
            return True
        return a.style == b.style and a.color == b.color

    @staticmethod
    def lerp(a: "_BorderSide", b: "_BorderSide", t: float) -> "_BorderSide":
        if a is b:
            return a
        if t == 0.0:
            return a
        if t == 1.0:
            return b
        width = _lerpDouble(a.width, b.width, t)
        if width < 0.0:
            return BorderSide.none
        if a.style == b.style and a.strokeAlign == b.strokeAlign:
            return _BorderSide(
                color=Color.lerp(a.color, b.color, t),
                width=width,
                style=a.style,
                strokeAlign=a.strokeAlign,
            )
        colorA = a.color if a.style == BorderStyle.solid else a.color.withAlpha(0x00)
        colorB = b.color if b.style == BorderStyle.solid else b.color.withAlpha(0x00)
        if a.strokeAlign != b.strokeAlign:
            return _BorderSide(
                color=Color.lerp(colorA, colorB, t),
                width=width,
                strokeAlign=_lerpDouble(a.strokeAlign, b.strokeAlign, t),
            )
        return _BorderSide(
            color=Color.lerp(colorA, colorB, t),
            width=width,
            strokeAlign=a.strokeAlign,
        )

    @staticmethod
    def merge(a: "_BorderSide", b: "_BorderSide") -> "_BorderSide":
        a_is_none = a.style == BorderStyle.none and a.width == 0.0
        b_is_none = b.style == BorderStyle.none and b.width == 0.0
        if a_is_none and b_is_none:
            return BorderSide.none
        if a_is_none:
            return b
        if b_is_none:
            return a
        return _BorderSide(
            color=a.color,
            width=a.width + b.width,
            strokeAlign=max(a.strokeAlign, b.strokeAlign),
            style=a.style,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "_BorderSide":
        return _BorderSide(
            color=_flut_unpack_required_field(data, "color"),
            width=_flut_unpack_required_field(data, "width"),
            style=_flut_unpack_required_field(data, "style"),
            strokeAlign=_flut_unpack_required_field(data, "strokeAlign"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["color"] = _flut_pack_value(self.color)
        result["width"] = _flut_pack_value(self.width)
        result["style"] = _flut_pack_value(self.style)
        result["strokeAlign"] = _flut_pack_value(self.strokeAlign)
        return result


class BorderSide(_BorderSide):
    none = _BorderSide(color=Color(0xFF000000), width=0.0, style=BorderStyle.none)


class OutlinedBorder(ShapeBorder):
    _flut_type = "OutlinedBorder"

    def __init__(self, *, side: "BorderSide" = BorderSide.none):
        super().__init__()
        self.side = side
