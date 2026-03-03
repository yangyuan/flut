import math
from typing import override
from flut._flut.engine import (
    FlutEnumObject,
    FlutValueObject,
    FlutRealtimeObject,
    named_constructor,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class ColorSpace(FlutEnumObject):
    sRGB: "ColorSpace"
    extendedSRGB: "ColorSpace"
    displayP3: "ColorSpace"


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def _lerpDouble(a, b, t):
    return a * (1.0 - t) + b * t


class Color(FlutValueObject):
    _flut_type = "Color"

    def __init__(self, value: int = 0x00000000):
        super().__init__()
        self._value = value & 0xFFFFFFFF

    @staticmethod
    def _flut_unpack(data: dict) -> "Color":
        return Color(value=_flut_unpack_required_field(data, "value"))

    @staticmethod
    def fromARGB(a: int, r: int, g: int, b: int) -> "Color":
        return Color(
            ((a & 0xFF) << 24) | ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)
        )

    @staticmethod
    def fromRGBO(r: int, g: int, b: int, opacity: float) -> "Color":
        return Color(
            ((int(opacity * 255) & 0xFF) << 24)
            | ((r & 0xFF) << 16)
            | ((g & 0xFF) << 8)
            | (b & 0xFF)
        )

    @staticmethod
    def from_(
        *,
        alpha: float,
        red: float,
        green: float,
        blue: float,
        colorSpace: "ColorSpace | None" = None,
    ) -> "Color":
        return Color.fromARGB(
            _clamp(int(alpha * 255), 0, 255),
            _clamp(int(red * 255), 0, 255),
            _clamp(int(green * 255), 0, 255),
            _clamp(int(blue * 255), 0, 255),
        )

    @property
    def a(self) -> float:
        return ((self._value >> 24) & 0xFF) / 255.0

    @property
    def r(self) -> float:
        return ((self._value >> 16) & 0xFF) / 255.0

    @property
    def g(self) -> float:
        return ((self._value >> 8) & 0xFF) / 255.0

    @property
    def b(self) -> float:
        return (self._value & 0xFF) / 255.0

    @property
    def colorSpace(self) -> "ColorSpace":
        return ColorSpace.sRGB

    @property
    def value(self) -> int:
        return self._value

    @property
    def alpha(self) -> int:
        return (self._value >> 24) & 0xFF

    @property
    def red(self) -> int:
        return (self._value >> 16) & 0xFF

    @property
    def green(self) -> int:
        return (self._value >> 8) & 0xFF

    @property
    def blue(self) -> int:
        return self._value & 0xFF

    @property
    def opacity(self) -> float:
        return self.alpha / 255.0

    def toARGB32(self) -> int:
        return self._value

    def computeLuminance(self) -> float:
        def _linearize(c: float) -> float:
            return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

        return (
            0.2126 * _linearize(self.r)
            + 0.7152 * _linearize(self.g)
            + 0.0722 * _linearize(self.b)
        )

    def withAlpha(self, a: int) -> "Color":
        return Color.fromARGB(a, self.red, self.green, self.blue)

    def withRed(self, r: int) -> "Color":
        return Color.fromARGB(self.alpha, r, self.green, self.blue)

    def withGreen(self, g: int) -> "Color":
        return Color.fromARGB(self.alpha, self.red, g, self.blue)

    def withBlue(self, b: int) -> "Color":
        return Color.fromARGB(self.alpha, self.red, self.green, b)

    def withOpacity(self, opacity: float) -> "Color":
        return Color.fromARGB(int(opacity * 255), self.red, self.green, self.blue)

    def withValues(
        self,
        *,
        alpha: float | None = None,
        red: float | None = None,
        green: float | None = None,
        blue: float | None = None,
        colorSpace: "ColorSpace | None" = None,
    ) -> "Color":
        return Color.fromARGB(
            _clamp(int((alpha if alpha is not None else self.a) * 255), 0, 255),
            _clamp(int((red if red is not None else self.r) * 255), 0, 255),
            _clamp(int((green if green is not None else self.g) * 255), 0, 255),
            _clamp(int((blue if blue is not None else self.b) * 255), 0, 255),
        )

    @staticmethod
    def alphaBlend(foreground: "Color", background: "Color") -> "Color":
        a = foreground.a
        inv = 1.0 - a
        br = background.a
        out_a = a + br * inv
        if out_a == 0.0:
            return Color(0x00000000)
        return Color.from_(
            alpha=out_a,
            red=(foreground.r * a + background.r * br * inv) / out_a,
            green=(foreground.g * a + background.g * br * inv) / out_a,
            blue=(foreground.b * a + background.b * br * inv) / out_a,
        )

    @staticmethod
    def getAlphaFromOpacity(opacity: float) -> int:
        return _clamp(int(opacity * 255), 0, 255)

    @staticmethod
    def lerp(x: "Color | None", y: "Color | None", t: float) -> "Color | None":
        if x is None and y is None:
            return None
        if x is None:
            return Color.from_(
                alpha=_lerpDouble(0, y.a, t),
                red=y.r,
                green=y.g,
                blue=y.b,
            )
        if y is None:
            return Color.from_(
                alpha=_lerpDouble(x.a, 0, t),
                red=x.r,
                green=x.g,
                blue=x.b,
            )
        return Color.from_(
            alpha=_lerpDouble(x.a, y.a, t),
            red=_lerpDouble(x.r, y.r, t),
            green=_lerpDouble(x.g, y.g, t),
            blue=_lerpDouble(x.b, y.b, t),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self._value)
        return result

    def __repr__(self):
        return f"Color(0x{self._value:08X})"

    def __eq__(self, other):
        if isinstance(other, Color):
            return self._value == other._value
        return False

    def __hash__(self):
        return hash(self._value)


class PaintingStyle(FlutEnumObject):
    fill: "PaintingStyle"
    stroke: "PaintingStyle"


class StrokeCap(FlutEnumObject):
    butt: "StrokeCap"
    round: "StrokeCap"
    square: "StrokeCap"


class StrokeJoin(FlutEnumObject):
    miter: "StrokeJoin"
    round: "StrokeJoin"
    bevel: "StrokeJoin"


class BlurStyle(FlutEnumObject):
    normal: "BlurStyle"
    solid: "BlurStyle"
    outer: "BlurStyle"
    inner: "BlurStyle"


class TileMode(FlutEnumObject):
    clamp: "TileMode"
    repeated: "TileMode"
    mirror: "TileMode"
    decal: "TileMode"


class FilterQuality(FlutEnumObject):
    none: "FilterQuality"
    low: "FilterQuality"
    medium: "FilterQuality"
    high: "FilterQuality"


class MaskFilter(FlutValueObject):
    _flut_type = "MaskFilter"

    def __init__(self, *args, **kwargs):
        raise TypeError("MaskFilter has no default constructor. Use MaskFilter.blur().")

    @named_constructor
    def blur(cls, style: "BlurStyle", sigma: float):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.style = style
        instance.sigma = sigma
        return instance

    @staticmethod
    def _flut_unpack(data: dict) -> "MaskFilter":
        return MaskFilter.blur(
            style=_flut_unpack_required_field(data, "style"),
            sigma=_flut_unpack_required_field(data, "sigma"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self._flut_init == "blur":
            result["style"] = _flut_pack_value(self.style)
            result["sigma"] = _flut_pack_value(self.sigma)
        return result

    def __eq__(self, other):
        if isinstance(other, MaskFilter):
            return self.style == other.style and self.sigma == other.sigma
        return False

    def __hash__(self):
        return hash((self.style, self.sigma))

    def __repr__(self):
        return f"MaskFilter.blur({self.style!r}, {self.sigma})"


class ImageFilter(FlutValueObject):
    _flut_type = "ImageFilter"

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "ImageFilter has no default constructor. "
            "Use ImageFilter.blur(), .dilate(), .erode(), .matrix(), or .compose()."
        )

    @named_constructor
    def blur(
        cls,
        *,
        sigmaX: float = 0.0,
        sigmaY: float = 0.0,
        tileMode: "TileMode" = TileMode.clamp,
    ):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.sigmaX = sigmaX
        instance.sigmaY = sigmaY
        instance.tileMode = tileMode
        instance.radiusX = None
        instance.radiusY = None
        instance.matrix4 = None
        instance.filterQuality = None
        instance.outer = None
        instance.inner = None
        return instance

    @named_constructor
    def dilate(cls, *, radiusX: float = 0.0, radiusY: float = 0.0):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.sigmaX = None
        instance.sigmaY = None
        instance.tileMode = None
        instance.radiusX = radiusX
        instance.radiusY = radiusY
        instance.matrix4 = None
        instance.filterQuality = None
        instance.outer = None
        instance.inner = None
        return instance

    @named_constructor
    def erode(cls, *, radiusX: float = 0.0, radiusY: float = 0.0):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.sigmaX = None
        instance.sigmaY = None
        instance.tileMode = None
        instance.radiusX = radiusX
        instance.radiusY = radiusY
        instance.matrix4 = None
        instance.filterQuality = None
        instance.outer = None
        instance.inner = None
        return instance

    @named_constructor
    def matrix(
        cls, matrix4: list, *, filterQuality: "FilterQuality" = FilterQuality.medium
    ):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.sigmaX = None
        instance.sigmaY = None
        instance.tileMode = None
        instance.radiusX = None
        instance.radiusY = None
        instance.matrix4 = matrix4
        instance.filterQuality = filterQuality
        instance.outer = None
        instance.inner = None
        return instance

    @named_constructor
    def compose(cls, *, outer: "ImageFilter", inner: "ImageFilter"):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.sigmaX = None
        instance.sigmaY = None
        instance.tileMode = None
        instance.radiusX = None
        instance.radiusY = None
        instance.matrix4 = None
        instance.filterQuality = None
        instance.outer = outer
        instance.inner = inner
        return instance

    @staticmethod
    def _flut_unpack(data: dict) -> "ImageFilter":
        constructor = data.get("_flut_init", "blur")
        if constructor == "blur":
            return ImageFilter.blur(
                sigmaX=_flut_unpack_optional_field(data, "sigmaX") or 0.0,
                sigmaY=_flut_unpack_optional_field(data, "sigmaY") or 0.0,
                tileMode=_flut_unpack_optional_field(data, "tileMode"),
            )
        elif constructor == "dilate":
            return ImageFilter.dilate(
                radiusX=_flut_unpack_optional_field(data, "radiusX") or 0.0,
                radiusY=_flut_unpack_optional_field(data, "radiusY") or 0.0,
            )
        elif constructor == "erode":
            return ImageFilter.erode(
                radiusX=_flut_unpack_optional_field(data, "radiusX") or 0.0,
                radiusY=_flut_unpack_optional_field(data, "radiusY") or 0.0,
            )
        elif constructor == "matrix":
            return ImageFilter.matrix(
                matrix4=_flut_unpack_required_field(data, "matrix4"),
                filterQuality=_flut_unpack_optional_field(data, "filterQuality"),
            )
        elif constructor == "compose":
            return ImageFilter.compose(
                outer=_flut_unpack_required_field(data, "outer"),
                inner=_flut_unpack_required_field(data, "inner"),
            )
        raise ValueError(f"Unknown ImageFilter constructor: {constructor}")

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self._flut_init == "blur":
            result["sigmaX"] = _flut_pack_value(self.sigmaX)
            result["sigmaY"] = _flut_pack_value(self.sigmaY)
            result["tileMode"] = _flut_pack_value(self.tileMode)
        if self._flut_init == "dilate":
            result["radiusX"] = _flut_pack_value(self.radiusX)
            result["radiusY"] = _flut_pack_value(self.radiusY)
        if self._flut_init == "erode":
            result["radiusX"] = _flut_pack_value(self.radiusX)
            result["radiusY"] = _flut_pack_value(self.radiusY)
        if self._flut_init == "matrix":
            result["matrix4"] = _flut_pack_value(self.matrix4)
            result["filterQuality"] = _flut_pack_value(self.filterQuality)
        if self._flut_init == "compose":
            result["outer"] = _flut_pack_value(self.outer)
            result["inner"] = _flut_pack_value(self.inner)
        return result

    def __repr__(self):
        return f"ImageFilter.{self._flut_init}(...)"


class ColorFilter(ImageFilter):
    _flut_type = "ColorFilter"

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "ColorFilter has no default constructor. "
            "Use ColorFilter.mode(), .matrix(), .linearToSrgbGamma(), "
            ".srgbToLinearGamma(), or .saturation()."
        )

    @named_constructor
    def mode(cls, color: "Color", blendMode: "BlendMode"):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.color = color
        instance.blendMode = blendMode
        instance.matrix = None
        instance.saturation = None
        return instance

    @named_constructor
    def matrix(cls, matrix: list):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.color = None
        instance.blendMode = None
        instance.matrix = matrix
        instance.saturation = None
        return instance

    @named_constructor
    def linearToSrgbGamma(cls):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.color = None
        instance.blendMode = None
        instance.matrix = None
        instance.saturation = None
        return instance

    @named_constructor
    def srgbToLinearGamma(cls):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.color = None
        instance.blendMode = None
        instance.matrix = None
        instance.saturation = None
        return instance

    @named_constructor
    def saturation(cls, saturation: float):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.color = None
        instance.blendMode = None
        instance.matrix = None
        instance.saturation = saturation
        return instance

    @staticmethod
    def _flut_unpack(data: dict) -> "ColorFilter":
        constructor = data.get("_flut_init", "mode")
        if constructor == "mode":
            return ColorFilter.mode(
                color=_flut_unpack_required_field(data, "color"),
                blendMode=_flut_unpack_required_field(data, "blendMode"),
            )
        elif constructor == "matrix":
            return ColorFilter.matrix(
                matrix=_flut_unpack_required_field(data, "matrix")
            )
        elif constructor == "linearToSrgbGamma":
            return ColorFilter.linearToSrgbGamma()
        elif constructor == "srgbToLinearGamma":
            return ColorFilter.srgbToLinearGamma()
        elif constructor == "saturation":
            return ColorFilter.saturation(
                saturation=_flut_unpack_required_field(data, "saturation")
            )
        raise ValueError(f"Unknown ColorFilter constructor: {constructor}")

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self._flut_init == "mode":
            result["color"] = _flut_pack_value(self.color)
            result["blendMode"] = _flut_pack_value(self.blendMode)
        if self._flut_init == "matrix":
            result["matrix"] = _flut_pack_value(self.matrix)
        if self._flut_init == "saturation":
            result["saturation"] = _flut_pack_value(self.saturation)
        return result

    def __repr__(self):
        return f"ColorFilter.{self._flut_init}(...)"


class Shader(FlutValueObject):
    _flut_type = "Shader"


class Gradient(Shader):
    _flut_type = "Gradient"

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "Gradient has no default constructor. "
            "Use Gradient.linear(), .radial(), or .sweep()."
        )

    @named_constructor
    def linear(
        cls,
        from_: "Offset",
        to: "Offset",
        colors: list,
        colorStops: "list | None" = None,
        tileMode: "TileMode" = TileMode.clamp,
        matrix4: "list | None" = None,
    ):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.from_ = from_
        instance.to = to
        instance.colors = colors
        instance.colorStops = colorStops
        instance.tileMode = tileMode
        instance.matrix4 = matrix4
        instance.center = None
        instance.radius = None
        instance.focal = None
        instance.focalRadius = None
        instance.startAngle = None
        instance.endAngle = None
        return instance

    @named_constructor
    def radial(
        cls,
        center: "Offset",
        radius: float,
        colors: list,
        colorStops: "list | None" = None,
        tileMode: "TileMode" = TileMode.clamp,
        matrix4: "list | None" = None,
        focal: "Offset | None" = None,
        focalRadius: float = 0.0,
    ):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.from_ = None
        instance.to = None
        instance.colors = colors
        instance.colorStops = colorStops
        instance.tileMode = tileMode
        instance.matrix4 = matrix4
        instance.center = center
        instance.radius = radius
        instance.focal = focal
        instance.focalRadius = focalRadius
        instance.startAngle = None
        instance.endAngle = None
        return instance

    @named_constructor
    def sweep(
        cls,
        center: "Offset",
        colors: list,
        colorStops: "list | None" = None,
        tileMode: "TileMode" = TileMode.clamp,
        startAngle: float = 0.0,
        endAngle: float = math.pi * 2,
        matrix4: "list | None" = None,
    ):
        instance = cls.__new__(cls)
        FlutValueObject.__init__(instance)
        instance.from_ = None
        instance.to = None
        instance.colors = colors
        instance.colorStops = colorStops
        instance.tileMode = tileMode
        instance.matrix4 = matrix4
        instance.center = center
        instance.radius = None
        instance.focal = None
        instance.focalRadius = None
        instance.startAngle = startAngle
        instance.endAngle = endAngle
        return instance

    @staticmethod
    def _flut_unpack(data: dict) -> "Gradient":
        constructor = data.get("_flut_init", "linear")
        if constructor == "linear":
            return Gradient.linear(
                from_=_flut_unpack_required_field(data, "from"),
                to=_flut_unpack_required_field(data, "to"),
                colors=_flut_unpack_required_field(data, "colors"),
                colorStops=_flut_unpack_optional_field(data, "colorStops"),
                tileMode=_flut_unpack_optional_field(data, "tileMode"),
                matrix4=_flut_unpack_optional_field(data, "matrix4"),
            )
        elif constructor == "radial":
            return Gradient.radial(
                center=_flut_unpack_required_field(data, "center"),
                radius=_flut_unpack_required_field(data, "radius"),
                colors=_flut_unpack_required_field(data, "colors"),
                colorStops=_flut_unpack_optional_field(data, "colorStops"),
                tileMode=_flut_unpack_optional_field(data, "tileMode"),
                matrix4=_flut_unpack_optional_field(data, "matrix4"),
                focal=_flut_unpack_optional_field(data, "focal"),
                focalRadius=_flut_unpack_optional_field(data, "focalRadius") or 0.0,
            )
        elif constructor == "sweep":
            return Gradient.sweep(
                center=_flut_unpack_required_field(data, "center"),
                colors=_flut_unpack_required_field(data, "colors"),
                colorStops=_flut_unpack_optional_field(data, "colorStops"),
                tileMode=_flut_unpack_optional_field(data, "tileMode"),
                startAngle=_flut_unpack_optional_field(data, "startAngle") or 0.0,
                endAngle=_flut_unpack_optional_field(data, "endAngle") or math.pi * 2,
                matrix4=_flut_unpack_optional_field(data, "matrix4"),
            )
        raise ValueError(f"Unknown Gradient constructor: {constructor}")

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["colors"] = [_flut_pack_value(c) for c in self.colors]
        if self.colorStops is not None:
            result["colorStops"] = _flut_pack_value(self.colorStops)
        result["tileMode"] = _flut_pack_value(self.tileMode)
        if self.matrix4 is not None:
            result["matrix4"] = _flut_pack_value(self.matrix4)
        if self._flut_init == "linear":
            result["from"] = _flut_pack_value(self.from_)
            result["to"] = _flut_pack_value(self.to)
        if self._flut_init == "radial":
            result["center"] = _flut_pack_value(self.center)
            result["radius"] = _flut_pack_value(self.radius)
            if self.focal is not None:
                result["focal"] = _flut_pack_value(self.focal)
            result["focalRadius"] = _flut_pack_value(self.focalRadius)
        if self._flut_init == "sweep":
            result["center"] = _flut_pack_value(self.center)
            result["startAngle"] = _flut_pack_value(self.startAngle)
            result["endAngle"] = _flut_pack_value(self.endAngle)
        return result

    def __repr__(self):
        return f"Gradient.{self._flut_init}(...)"


class _FontWeight(FlutValueObject):
    _flut_type = "FontWeight"

    def __init__(self, index: int, value: int):
        super().__init__()
        self.index = index
        self.value = value

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["index"] = _flut_pack_value(self.index)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "_FontWeight":
        return FontWeight._by_index[_flut_unpack_required_field(data, "index")]


class FontWeight(_FontWeight):
    def __init__(self, value: int):
        super().__init__(index=max(0, min(8, (value // 100) - 1)), value=value)

    w100 = _FontWeight(0, 100)
    w200 = _FontWeight(1, 200)
    w300 = _FontWeight(2, 300)
    w400 = _FontWeight(3, 400)
    w500 = _FontWeight(4, 500)
    w600 = _FontWeight(5, 600)
    w700 = _FontWeight(6, 700)
    w800 = _FontWeight(7, 800)
    w900 = _FontWeight(8, 900)
    normal = w400
    bold = w700
    values = [w100, w200, w300, w400, w500, w600, w700, w800, w900]
    _by_index = values

    @staticmethod
    def lerp(
        a: "_FontWeight | None", b: "_FontWeight | None", t: float
    ) -> "_FontWeight | None":
        if a is b:
            return a
        a_index = a.index if a is not None else 3
        b_index = b.index if b is not None else 3
        index = max(0, min(8, round(a_index + (b_index - a_index) * t)))
        return FontWeight.values[index]


class _Size(FlutValueObject):
    _flut_type = "Size"

    def __init__(self, width: float = 0, height: float = 0):
        super().__init__()
        self.width = width
        self.height = height

    @staticmethod
    def copy(source: "Size") -> "Size":
        return _Size(source.width, source.height)

    @staticmethod
    def fromHeight(height: float) -> "Size":
        return _Size(float("inf"), height)

    @staticmethod
    def fromWidth(width: float) -> "Size":
        return _Size(width, float("inf"))

    @staticmethod
    def fromRadius(radius: float) -> "Size":
        return _Size(radius * 2, radius * 2)

    @staticmethod
    def square(dimension: float) -> "Size":
        return _Size(dimension, dimension)

    @staticmethod
    def _flut_unpack(data: dict) -> "_Size":
        return _Size(
            width=_flut_unpack_required_field(data, "width"),
            height=_flut_unpack_required_field(data, "height"),
        )

    @property
    def aspectRatio(self) -> float:
        if self.height != 0.0:
            return self.width / self.height
        if self.width > 0.0:
            return float("inf")
        if self.width < 0.0:
            return float("-inf")
        return 0.0

    @property
    def flipped(self) -> "Size":
        return _Size(self.height, self.width)

    @property
    def isEmpty(self) -> bool:
        return self.width <= 0.0 or self.height <= 0.0

    @property
    def longestSide(self) -> float:
        return max(abs(self.width), abs(self.height))

    @property
    def shortestSide(self) -> float:
        return min(abs(self.width), abs(self.height))

    def bottomCenter(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width / 2.0, origin.dy + self.height)

    def bottomLeft(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx, origin.dy + self.height)

    def bottomRight(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width, origin.dy + self.height)

    def center(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width / 2.0, origin.dy + self.height / 2.0)

    def centerLeft(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx, origin.dy + self.height / 2.0)

    def centerRight(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width, origin.dy + self.height / 2.0)

    def contains(self, offset: "Offset") -> bool:
        return 0.0 <= offset.dx <= self.width and 0.0 <= offset.dy <= self.height

    def topCenter(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width / 2.0, origin.dy)

    def topLeft(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx, origin.dy)

    def topRight(self, origin: "Offset") -> "Offset":
        return _Offset(origin.dx + self.width, origin.dy)

    def __add__(self, other: "Offset") -> "Size":
        return _Size(self.width + other.dx, self.height + other.dy)

    def __sub__(self, other) -> "Offset | Size":
        if isinstance(other, _Size):
            return _Offset(self.width - other.width, self.height - other.height)
        if isinstance(other, _Offset):
            return _Size(self.width - other.dx, self.height - other.dy)
        return NotImplemented

    def __mul__(self, operand: float) -> "Size":
        return _Size(self.width * operand, self.height * operand)

    def __truediv__(self, operand: float) -> "Size":
        return _Size(self.width / operand, self.height / operand)

    def __floordiv__(self, operand: float) -> "Size":
        return _Size(self.width // operand, self.height // operand)

    def __mod__(self, operand: float) -> "Size":
        return _Size(self.width % operand, self.height % operand)

    @staticmethod
    def lerp(a: "Size | None", b: "Size | None", t: float) -> "Size | None":
        if a is None and b is None:
            return None
        if a is None:
            return _Size(b.width * t, b.height * t)
        if b is None:
            return _Size(a.width * (1.0 - t), a.height * (1.0 - t))
        return _Size(
            _lerpDouble(a.width, b.width, t),
            _lerpDouble(a.height, b.height, t),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["width"] = _flut_pack_value(self.width)
        result["height"] = _flut_pack_value(self.height)
        return result

    def __eq__(self, other):
        if isinstance(other, _Size):
            return self.width == other.width and self.height == other.height
        return False

    def __hash__(self):
        return hash((self.width, self.height))

    def __repr__(self):
        return f"Size({self.width}, {self.height})"


class Size(_Size):
    zero = _Size(0, 0)
    infinite = _Size(float("inf"), float("inf"))


class _Offset(FlutValueObject):
    _flut_type = "Offset"

    def __init__(self, dx: float = 0, dy: float = 0):
        super().__init__()
        self.dx = dx
        self.dy = dy

    @staticmethod
    def fromDirection(direction: float, distance: float = 1.0) -> "Offset":
        return _Offset(math.cos(direction) * distance, math.sin(direction) * distance)

    @staticmethod
    def _flut_unpack(data: dict) -> "_Offset":
        return _Offset(
            dx=_flut_unpack_required_field(data, "dx"),
            dy=_flut_unpack_required_field(data, "dy"),
        )

    @property
    def direction(self) -> float:
        return math.atan2(self.dy, self.dx)

    @property
    def distance(self) -> float:
        return math.sqrt(self.dx * self.dx + self.dy * self.dy)

    @property
    def distanceSquared(self) -> float:
        return self.dx * self.dx + self.dy * self.dy

    def scale(self, scaleX: float, scaleY: float) -> "Offset":
        return _Offset(self.dx * scaleX, self.dy * scaleY)

    def translate(self, translateX: float, translateY: float) -> "Offset":
        return _Offset(self.dx + translateX, self.dy + translateY)

    def __and__(self, other: "Size") -> "Rect":
        return Rect(self.dx, self.dy, self.dx + other.width, self.dy + other.height)

    def __add__(self, other: "Offset") -> "Offset":
        return _Offset(self.dx + other.dx, self.dy + other.dy)

    def __sub__(self, other: "Offset") -> "Offset":
        return _Offset(self.dx - other.dx, self.dy - other.dy)

    def __neg__(self) -> "Offset":
        return _Offset(-self.dx, -self.dy)

    def __mul__(self, operand: float) -> "Offset":
        return _Offset(self.dx * operand, self.dy * operand)

    def __truediv__(self, operand: float) -> "Offset":
        return _Offset(self.dx / operand, self.dy / operand)

    def __floordiv__(self, operand: float) -> "Offset":
        return _Offset(self.dx // operand, self.dy // operand)

    def __mod__(self, operand: float) -> "Offset":
        return _Offset(self.dx % operand, self.dy % operand)

    @staticmethod
    def lerp(a: "Offset | None", b: "Offset | None", t: float) -> "Offset | None":
        if a is None and b is None:
            return None
        if a is None:
            return _Offset(b.dx * t, b.dy * t)
        if b is None:
            return _Offset(a.dx * (1.0 - t), a.dy * (1.0 - t))
        return _Offset(
            _lerpDouble(a.dx, b.dx, t),
            _lerpDouble(a.dy, b.dy, t),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["dx"] = _flut_pack_value(self.dx)
        result["dy"] = _flut_pack_value(self.dy)
        return result

    def __eq__(self, other):
        if isinstance(other, _Offset):
            return self.dx == other.dx and self.dy == other.dy
        return False

    def __hash__(self):
        return hash((self.dx, self.dy))

    def __repr__(self):
        return f"Offset({self.dx}, {self.dy})"


class Offset(_Offset):
    zero = _Offset(0, 0)
    infinite = _Offset(float("inf"), float("inf"))


class Rect(FlutValueObject):
    _flut_type = "Rect"

    def __init__(self, left: float, top: float, right: float, bottom: float):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    zero = None  # set after class
    largest = None  # set after class

    @staticmethod
    def _flut_unpack(data: dict) -> "Rect":
        return Rect(
            left=_flut_unpack_required_field(data, "left"),
            top=_flut_unpack_required_field(data, "top"),
            right=_flut_unpack_required_field(data, "right"),
            bottom=_flut_unpack_required_field(data, "bottom"),
        )

    @staticmethod
    def fromLTWH(left: float, top: float, width: float, height: float) -> "Rect":
        return Rect(left, top, left + width, top + height)

    @staticmethod
    def fromLTRB(left: float, top: float, right: float, bottom: float) -> "Rect":
        return Rect(left, top, right, bottom)

    @staticmethod
    def fromCircle(*, center, radius: float) -> "Rect":
        return Rect(
            center.dx - radius,
            center.dy - radius,
            center.dx + radius,
            center.dy + radius,
        )

    @staticmethod
    def fromCenter(*, center, width: float, height: float) -> "Rect":
        return Rect(
            center.dx - width / 2,
            center.dy - height / 2,
            center.dx + width / 2,
            center.dy + height / 2,
        )

    @staticmethod
    def fromPoints(a, b) -> "Rect":
        return Rect(
            min(a.dx, b.dx),
            min(a.dy, b.dy),
            max(a.dx, b.dx),
            max(a.dy, b.dy),
        )

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top

    @property
    def size(self):
        return Size(self.width, self.height)

    @property
    def center(self):
        return Offset((self.left + self.right) / 2, (self.top + self.bottom) / 2)

    @property
    def topLeft(self):
        return Offset(self.left, self.top)

    @property
    def topCenter(self):
        return Offset((self.left + self.right) / 2, self.top)

    @property
    def topRight(self):
        return Offset(self.right, self.top)

    @property
    def centerLeft(self):
        return Offset(self.left, (self.top + self.bottom) / 2)

    @property
    def centerRight(self):
        return Offset(self.right, (self.top + self.bottom) / 2)

    @property
    def bottomLeft(self):
        return Offset(self.left, self.bottom)

    @property
    def bottomCenter(self):
        return Offset((self.left + self.right) / 2, self.bottom)

    @property
    def bottomRight(self):
        return Offset(self.right, self.bottom)

    @property
    def hasNaN(self) -> bool:
        return (
            math.isnan(self.left)
            or math.isnan(self.top)
            or math.isnan(self.right)
            or math.isnan(self.bottom)
        )

    @property
    def isEmpty(self) -> bool:
        return self.left >= self.right or self.top >= self.bottom

    @property
    def isFinite(self) -> bool:
        return (
            math.isfinite(self.left)
            and math.isfinite(self.top)
            and math.isfinite(self.right)
            and math.isfinite(self.bottom)
        )

    @property
    def isInfinite(self) -> bool:
        return (
            self.left >= float("inf")
            or self.top >= float("inf")
            or self.right >= float("inf")
            or self.bottom >= float("inf")
        )

    @property
    def longestSide(self) -> float:
        return max(abs(self.width), abs(self.height))

    @property
    def shortestSide(self) -> float:
        return min(abs(self.width), abs(self.height))

    def contains(self, offset) -> bool:
        return (
            offset.dx >= self.left
            and offset.dx < self.right
            and offset.dy >= self.top
            and offset.dy < self.bottom
        )

    def deflate(self, delta: float) -> "Rect":
        return self.inflate(-delta)

    def expandToInclude(self, other: "Rect") -> "Rect":
        return Rect(
            min(self.left, other.left),
            min(self.top, other.top),
            max(self.right, other.right),
            max(self.bottom, other.bottom),
        )

    def inflate(self, delta: float) -> "Rect":
        return Rect(
            self.left - delta, self.top - delta, self.right + delta, self.bottom + delta
        )

    def intersect(self, other: "Rect") -> "Rect":
        return Rect(
            max(self.left, other.left),
            max(self.top, other.top),
            min(self.right, other.right),
            min(self.bottom, other.bottom),
        )

    def overlaps(self, other: "Rect") -> bool:
        if self.right <= other.left or other.right <= self.left:
            return False
        if self.bottom <= other.top or other.bottom <= self.top:
            return False
        return True

    def shift(self, offset) -> "Rect":
        return Rect(
            self.left + offset.dx,
            self.top + offset.dy,
            self.right + offset.dx,
            self.bottom + offset.dy,
        )

    def translate(self, translateX: float, translateY: float) -> "Rect":
        return Rect(
            self.left + translateX,
            self.top + translateY,
            self.right + translateX,
            self.bottom + translateY,
        )

    @staticmethod
    def lerp(a, b, t: float):
        if a is None and b is None:
            return None
        if a is None:
            return Rect(b.left * t, b.top * t, b.right * t, b.bottom * t)
        if b is None:
            s = 1.0 - t
            return Rect(a.left * s, a.top * s, a.right * s, a.bottom * s)
        return Rect(
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
        if isinstance(other, Rect):
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
        return f"Rect.fromLTRB({self.left}, {self.top}, {self.right}, {self.bottom})"


Rect.zero = Rect(0, 0, 0, 0)
Rect.largest = Rect(-1e9, -1e9, 1e9, 1e9)


class Paint(FlutValueObject):
    _flut_type = "Paint"

    def __init__(self):
        super().__init__()
        self.blendMode = None
        self.color = None
        self.colorFilter = None
        self.filterQuality = None
        self.imageFilter = None
        self.invertColors = None
        self.isAntiAlias = None
        self.maskFilter = None
        self.shader = None
        self.strokeCap = None
        self.strokeJoin = None
        self.strokeMiterLimit = None
        self.strokeWidth = None
        self.style = None

    @staticmethod
    def from_(source: "Paint") -> "Paint":
        paint = Paint()
        paint.blendMode = source.blendMode
        paint.color = source.color
        paint.colorFilter = source.colorFilter
        paint.filterQuality = source.filterQuality
        paint.imageFilter = source.imageFilter
        paint.invertColors = source.invertColors
        paint.isAntiAlias = source.isAntiAlias
        paint.maskFilter = source.maskFilter
        paint.shader = source.shader
        paint.strokeCap = source.strokeCap
        paint.strokeJoin = source.strokeJoin
        paint.strokeMiterLimit = source.strokeMiterLimit
        paint.strokeWidth = source.strokeWidth
        paint.style = source.style
        return paint

    @staticmethod
    def _flut_unpack(data: dict) -> "Paint":
        paint = Paint()
        paint.blendMode = _flut_unpack_optional_field(data, "blendMode")
        paint.color = _flut_unpack_optional_field(data, "color")
        paint.colorFilter = _flut_unpack_optional_field(data, "colorFilter")
        paint.filterQuality = _flut_unpack_optional_field(data, "filterQuality")
        paint.imageFilter = _flut_unpack_optional_field(data, "imageFilter")
        paint.invertColors = _flut_unpack_optional_field(data, "invertColors")
        paint.isAntiAlias = _flut_unpack_optional_field(data, "isAntiAlias")
        paint.maskFilter = _flut_unpack_optional_field(data, "maskFilter")
        paint.shader = _flut_unpack_optional_field(data, "shader")
        paint.strokeCap = _flut_unpack_optional_field(data, "strokeCap")
        paint.strokeJoin = _flut_unpack_optional_field(data, "strokeJoin")
        paint.strokeMiterLimit = _flut_unpack_optional_field(data, "strokeMiterLimit")
        paint.strokeWidth = _flut_unpack_optional_field(data, "strokeWidth")
        paint.style = _flut_unpack_optional_field(data, "style")
        return paint

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.blendMode is not None:
            result["blendMode"] = _flut_pack_value(self.blendMode)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.colorFilter is not None:
            result["colorFilter"] = _flut_pack_value(self.colorFilter)
        if self.filterQuality is not None:
            result["filterQuality"] = _flut_pack_value(self.filterQuality)
        if self.imageFilter is not None:
            result["imageFilter"] = _flut_pack_value(self.imageFilter)
        if self.invertColors is not None:
            result["invertColors"] = _flut_pack_value(self.invertColors)
        if self.isAntiAlias is not None:
            result["isAntiAlias"] = _flut_pack_value(self.isAntiAlias)
        if self.maskFilter is not None:
            result["maskFilter"] = _flut_pack_value(self.maskFilter)
        if self.shader is not None:
            result["shader"] = _flut_pack_value(self.shader)
        if self.strokeCap is not None:
            result["strokeCap"] = _flut_pack_value(self.strokeCap)
        if self.strokeJoin is not None:
            result["strokeJoin"] = _flut_pack_value(self.strokeJoin)
        if self.strokeMiterLimit is not None:
            result["strokeMiterLimit"] = _flut_pack_value(self.strokeMiterLimit)
        if self.strokeWidth is not None:
            result["strokeWidth"] = _flut_pack_value(self.strokeWidth)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        return result


class Shadow(FlutValueObject):
    _flut_type = "Shadow"

    def __init__(
        self,
        *,
        color: "Color" = Color(0xFF000000),
        offset: "Offset" = Offset.zero,
        blurRadius: float = 0.0,
    ):
        super().__init__()
        self.color = color
        self.offset = offset
        self.blurRadius = blurRadius

    @property
    def blurSigma(self) -> float:
        r = self.blurRadius
        return r * 0.57735 + 0.5 if r > 0 else 0

    @staticmethod
    def _flut_unpack(data: dict) -> "Shadow":
        return Shadow(
            color=_flut_unpack_optional_field(data, "color"),
            offset=_flut_unpack_optional_field(data, "offset"),
            blurRadius=_flut_unpack_optional_field(data, "blurRadius") or 0.0,
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["color"] = _flut_pack_value(self.color)
        result["offset"] = _flut_pack_value(self.offset)
        result["blurRadius"] = _flut_pack_value(self.blurRadius)
        return result


class Canvas(FlutRealtimeObject):
    _flut_type = "Canvas"

    def drawLine(self, p1: Offset, p2: Offset, paint: Paint):
        self._flut_call(
            "drawLine",
            p1._flut_pack(),
            p2._flut_pack(),
            paint._flut_pack(),
        )

    def drawRect(self, rect: Rect, paint: Paint):
        self._flut_call("drawRect", rect._flut_pack(), paint._flut_pack())

    def drawCircle(self, c: Offset, radius: float, paint: Paint):
        self._flut_call(
            "drawCircle",
            c._flut_pack(),
            radius,
            paint._flut_pack(),
        )

    def drawOval(self, rect: Rect, paint: Paint):
        self._flut_call("drawOval", rect._flut_pack(), paint._flut_pack())

    def drawArc(
        self,
        rect: Rect,
        startAngle: float,
        sweepAngle: float,
        useCenter: bool,
        paint: Paint,
    ):
        self._flut_call(
            "drawArc",
            rect._flut_pack(),
            startAngle,
            sweepAngle,
            useCenter,
            paint._flut_pack(),
        )

    def clipRect(self, rect: Rect):
        self._flut_call("clipRect", rect._flut_pack())

    def save(self):
        self._flut_call("save")

    def restore(self):
        self._flut_call("restore")

    def translate(self, dx: float, dy: float):
        self._flut_call("translate", dx, dy)

    def scale(self, sx: float, sy: float = None):
        if sy is not None:
            self._flut_call("scale", sx, sy)
        else:
            self._flut_call("scale", sx)

    def rotate(self, radians: float):
        self._flut_call("rotate", radians)


class PlaceholderAlignment(FlutEnumObject):
    baseline: "PlaceholderAlignment"
    aboveBaseline: "PlaceholderAlignment"
    belowBaseline: "PlaceholderAlignment"
    top: "PlaceholderAlignment"
    bottom: "PlaceholderAlignment"
    middle: "PlaceholderAlignment"


class TextBaseline(FlutEnumObject):
    alphabetic: "TextBaseline"
    ideographic: "TextBaseline"


class TextAlign(FlutEnumObject):
    left: "TextAlign"
    right: "TextAlign"
    center: "TextAlign"
    justify: "TextAlign"
    start: "TextAlign"
    end: "TextAlign"


class Brightness(FlutEnumObject):
    dark: "Brightness"
    light: "Brightness"


class TextDirection(FlutEnumObject):
    rtl: "TextDirection"
    ltr: "TextDirection"


class BlendMode(FlutEnumObject):
    clear: "BlendMode"
    src: "BlendMode"
    dst: "BlendMode"
    srcOver: "BlendMode"
    dstOver: "BlendMode"
    srcIn: "BlendMode"
    dstIn: "BlendMode"
    srcOut: "BlendMode"
    dstOut: "BlendMode"
    srcATop: "BlendMode"
    dstATop: "BlendMode"
    xor: "BlendMode"
    plus: "BlendMode"
    modulate: "BlendMode"
    screen: "BlendMode"
    overlay: "BlendMode"
    darken: "BlendMode"
    lighten: "BlendMode"
    colorDodge: "BlendMode"
    colorBurn: "BlendMode"
    hardLight: "BlendMode"
    softLight: "BlendMode"
    difference: "BlendMode"
    exclusion: "BlendMode"
    multiply: "BlendMode"
    hue: "BlendMode"
    saturation: "BlendMode"
    color: "BlendMode"
    luminosity: "BlendMode"


class Clip(FlutEnumObject):
    none: "Clip"
    hardEdge: "Clip"
    antiAlias: "Clip"
    antiAliasWithSaveLayer: "Clip"


class PointerDeviceKind(FlutEnumObject):
    touch: "PointerDeviceKind"
    mouse: "PointerDeviceKind"
    stylus: "PointerDeviceKind"
    invertedStylus: "PointerDeviceKind"
    trackpad: "PointerDeviceKind"
    unknown: "PointerDeviceKind"


class FontStyle(FlutEnumObject):
    normal: "FontStyle"
    italic: "FontStyle"


class TextDecorationStyle(FlutEnumObject):
    solid: "TextDecorationStyle"
    double: "TextDecorationStyle"
    dotted: "TextDecorationStyle"
    dashed: "TextDecorationStyle"
    wavy: "TextDecorationStyle"


class TextLeadingDistribution(FlutEnumObject):
    proportional: "TextLeadingDistribution"
    even: "TextLeadingDistribution"
