from typing import Optional, override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Color, FontWeight, TextBaseline


class TextStyle(FlutValueObject):
    _flut_type = "TextStyle"

    def __init__(
        self,
        *,
        inherit: bool = True,
        color: Optional[Color] = None,
        backgroundColor: Optional[Color] = None,
        fontSize: Optional[float] = None,
        fontWeight: Optional[FontWeight] = None,
        fontStyle=None,
        letterSpacing: Optional[float] = None,
        wordSpacing: Optional[float] = None,
        textBaseline: Optional[TextBaseline] = None,
        height: Optional[float] = None,
        leadingDistribution=None,
        locale=None,
        foreground=None,
        background=None,
        shadows: Optional[list] = None,
        fontFeatures: Optional[list] = None,
        fontVariations: Optional[list] = None,
        decoration=None,
        decorationColor: Optional[Color] = None,
        decorationStyle=None,
        decorationThickness: Optional[float] = None,
        debugLabel: Optional[str] = None,
        fontFamily: Optional[str] = None,
        fontFamilyFallback: Optional[list[str]] = None,
        package: Optional[str] = None,
        overflow=None,
    ):
        super().__init__()
        self.inherit = inherit
        self.color = color
        self.backgroundColor = backgroundColor
        self.fontSize = fontSize
        self.fontWeight = fontWeight
        self.fontStyle = fontStyle
        self.letterSpacing = letterSpacing
        self.wordSpacing = wordSpacing
        self.textBaseline = textBaseline
        self.height = height
        self.leadingDistribution = leadingDistribution
        self.locale = locale
        self.foreground = foreground
        self.background = background
        self.shadows = shadows
        self.fontFeatures = fontFeatures
        self.fontVariations = fontVariations
        self.decoration = decoration
        self.decorationColor = decorationColor
        self.decorationStyle = decorationStyle
        self.decorationThickness = decorationThickness
        self.debugLabel = debugLabel
        self.fontFamily = fontFamily
        self.fontFamilyFallback = fontFamilyFallback
        self.package = package
        self.overflow = overflow

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["inherit"] = _flut_pack_value(self.inherit)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.fontSize is not None:
            result["fontSize"] = _flut_pack_value(self.fontSize)
        if self.fontWeight is not None:
            result["fontWeight"] = _flut_pack_value(self.fontWeight)
        if self.fontStyle is not None:
            result["fontStyle"] = _flut_pack_value(self.fontStyle)
        if self.letterSpacing is not None:
            result["letterSpacing"] = _flut_pack_value(self.letterSpacing)
        if self.wordSpacing is not None:
            result["wordSpacing"] = _flut_pack_value(self.wordSpacing)
        if self.textBaseline is not None:
            result["textBaseline"] = _flut_pack_value(self.textBaseline)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.leadingDistribution is not None:
            result["leadingDistribution"] = _flut_pack_value(self.leadingDistribution)
        if self.locale is not None:
            result["locale"] = _flut_pack_value(self.locale)
        if self.foreground is not None:
            result["foreground"] = _flut_pack_value(self.foreground)
        if self.background is not None:
            result["background"] = _flut_pack_value(self.background)
        if self.shadows is not None:
            result["shadows"] = _flut_pack_value(self.shadows)
        if self.fontFeatures is not None:
            result["fontFeatures"] = _flut_pack_value(self.fontFeatures)
        if self.fontVariations is not None:
            result["fontVariations"] = _flut_pack_value(self.fontVariations)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.decorationColor is not None:
            result["decorationColor"] = _flut_pack_value(self.decorationColor)
        if self.decorationStyle is not None:
            result["decorationStyle"] = _flut_pack_value(self.decorationStyle)
        if self.decorationThickness is not None:
            result["decorationThickness"] = _flut_pack_value(self.decorationThickness)
        if self.fontFamily is not None:
            result["fontFamily"] = _flut_pack_value(self.fontFamily)
        if self.fontFamilyFallback is not None:
            result["fontFamilyFallback"] = _flut_pack_value(self.fontFamilyFallback)
        if self.package is not None:
            result["package"] = _flut_pack_value(self.package)
        if self.overflow is not None:
            result["overflow"] = _flut_pack_value(self.overflow)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "TextStyle":
        return TextStyle(
            inherit=_flut_unpack_required_field(data, "inherit"),
            color=_flut_unpack_optional_field(data, "color"),
            backgroundColor=_flut_unpack_optional_field(data, "backgroundColor"),
            fontSize=_flut_unpack_optional_field(data, "fontSize"),
            fontWeight=_flut_unpack_optional_field(data, "fontWeight"),
            fontStyle=_flut_unpack_optional_field(data, "fontStyle"),
            letterSpacing=_flut_unpack_optional_field(data, "letterSpacing"),
            wordSpacing=_flut_unpack_optional_field(data, "wordSpacing"),
            textBaseline=_flut_unpack_optional_field(data, "textBaseline"),
            height=_flut_unpack_optional_field(data, "height"),
            leadingDistribution=_flut_unpack_optional_field(
                data, "leadingDistribution"
            ),
            locale=_flut_unpack_optional_field(data, "locale"),
            foreground=_flut_unpack_optional_field(data, "foreground"),
            background=_flut_unpack_optional_field(data, "background"),
            shadows=_flut_unpack_optional_field(data, "shadows"),
            fontFeatures=_flut_unpack_optional_field(data, "fontFeatures"),
            fontVariations=_flut_unpack_optional_field(data, "fontVariations"),
            decoration=_flut_unpack_optional_field(data, "decoration"),
            decorationColor=_flut_unpack_optional_field(data, "decorationColor"),
            decorationStyle=_flut_unpack_optional_field(data, "decorationStyle"),
            decorationThickness=_flut_unpack_optional_field(
                data, "decorationThickness"
            ),
            fontFamily=_flut_unpack_optional_field(data, "fontFamily"),
            fontFamilyFallback=_flut_unpack_optional_field(data, "fontFamilyFallback"),
            overflow=_flut_unpack_optional_field(data, "overflow"),
        )
