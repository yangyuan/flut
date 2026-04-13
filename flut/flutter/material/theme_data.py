from typing import Optional, override
from flut._flut.engine import (
    FlutEnumObject,
    FlutRealtimeObject,
    FlutValueObject,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field
from flut.dart.ui import Brightness, Color, _Offset
from flut.flutter.material.color_scheme import ColorScheme
from flut.flutter.material.ink_well import InteractiveInkFeatureFactory
from flut.flutter.material.text_theme import TextTheme


class MaterialTapTargetSize(FlutEnumObject):
    padded: "MaterialTapTargetSize"
    shrinkWrap: "MaterialTapTargetSize"


class _VisualDensity(FlutValueObject):
    _flut_type = "VisualDensity"

    def __init__(self, *, horizontal: float = 0.0, vertical: float = 0.0):
        super().__init__()
        self.horizontal = horizontal
        self.vertical = vertical

    @property
    def baseSizeAdjustment(self):
        return _Offset(self.horizontal * 4.0, self.vertical * 4.0)

    @staticmethod
    def _flut_unpack(data: dict) -> "_VisualDensity":
        return _VisualDensity(
            horizontal=_flut_unpack_optional_field(data, "horizontal") or 0.0,
            vertical=_flut_unpack_optional_field(data, "vertical") or 0.0,
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["horizontal"] = _flut_pack_value(self.horizontal)
        result["vertical"] = _flut_pack_value(self.vertical)
        return result


class VisualDensity(_VisualDensity):
    minimumDensity = -4.0
    maximumDensity = 4.0
    comfortable = _VisualDensity(horizontal=-1.0, vertical=-1.0)
    standard = _VisualDensity(horizontal=0.0, vertical=0.0)
    compact = _VisualDensity(horizontal=-2.0, vertical=-2.0)


class ThemeData(FlutRealtimeObject):
    _flut_type = "ThemeData"

    def __init__(
        self,
        *,
        colorScheme=None,
        brightness: Optional[Brightness] = None,
        colorSchemeSeed: Optional[Color] = None,
        useMaterial3: Optional[bool] = None,
        textTheme=None,
        fontFamily: Optional[str] = None,
        fontFamilyFallback: Optional[list[str]] = None,
        package: Optional[str] = None,
        primaryColor: Optional[Color] = None,
        primaryColorDark: Optional[Color] = None,
        primaryColorLight: Optional[Color] = None,
        canvasColor: Optional[Color] = None,
        cardColor: Optional[Color] = None,
        scaffoldBackgroundColor: Optional[Color] = None,
        dividerColor: Optional[Color] = None,
        focusColor: Optional[Color] = None,
        highlightColor: Optional[Color] = None,
        hintColor: Optional[Color] = None,
        hoverColor: Optional[Color] = None,
        shadowColor: Optional[Color] = None,
        splashColor: Optional[Color] = None,
        disabledColor: Optional[Color] = None,
        unselectedWidgetColor: Optional[Color] = None,
        secondaryHeaderColor: Optional[Color] = None,
        iconTheme=None,
        primaryIconTheme=None,
        primaryTextTheme=None,
        typography=None,
        applyElevationOverlayColor: Optional[bool] = None,
        materialTapTargetSize=None,
        pageTransitionsTheme=None,
        platform=None,
        splashFactory: Optional[InteractiveInkFeatureFactory] = None,
        useSystemColors: Optional[bool] = None,
        visualDensity=None,
        inputDecorationTheme=None,
    ):
        super().__init__()
        props = {}
        if colorScheme is not None:
            props["colorScheme"] = colorScheme._flut_pack()
        if brightness is not None:
            props["brightness"] = brightness._flut_pack()
        if colorSchemeSeed is not None:
            props["colorSchemeSeed"] = colorSchemeSeed._flut_pack()
        if useMaterial3 is not None:
            props["useMaterial3"] = useMaterial3
        if textTheme is not None:
            props["textTheme"] = textTheme._flut_pack()
        if fontFamily is not None:
            props["fontFamily"] = fontFamily
        if fontFamilyFallback is not None:
            props["fontFamilyFallback"] = fontFamilyFallback
        if package is not None:
            props["package"] = package
        if primaryColor is not None:
            props["primaryColor"] = primaryColor._flut_pack()
        if primaryColorDark is not None:
            props["primaryColorDark"] = primaryColorDark._flut_pack()
        if primaryColorLight is not None:
            props["primaryColorLight"] = primaryColorLight._flut_pack()
        if canvasColor is not None:
            props["canvasColor"] = canvasColor._flut_pack()
        if cardColor is not None:
            props["cardColor"] = cardColor._flut_pack()
        if scaffoldBackgroundColor is not None:
            props["scaffoldBackgroundColor"] = scaffoldBackgroundColor._flut_pack()
        if dividerColor is not None:
            props["dividerColor"] = dividerColor._flut_pack()
        if focusColor is not None:
            props["focusColor"] = focusColor._flut_pack()
        if highlightColor is not None:
            props["highlightColor"] = highlightColor._flut_pack()
        if hintColor is not None:
            props["hintColor"] = hintColor._flut_pack()
        if hoverColor is not None:
            props["hoverColor"] = hoverColor._flut_pack()
        if shadowColor is not None:
            props["shadowColor"] = shadowColor._flut_pack()
        if splashColor is not None:
            props["splashColor"] = splashColor._flut_pack()
        if disabledColor is not None:
            props["disabledColor"] = disabledColor._flut_pack()
        if unselectedWidgetColor is not None:
            props["unselectedWidgetColor"] = unselectedWidgetColor._flut_pack()
        if secondaryHeaderColor is not None:
            props["secondaryHeaderColor"] = secondaryHeaderColor._flut_pack()
        if iconTheme is not None:
            props["iconTheme"] = _flut_pack_value(iconTheme)
        if primaryIconTheme is not None:
            props["primaryIconTheme"] = _flut_pack_value(primaryIconTheme)
        if primaryTextTheme is not None:
            props["primaryTextTheme"] = primaryTextTheme._flut_pack()
        if typography is not None:
            props["typography"] = _flut_pack_value(typography)
        if applyElevationOverlayColor is not None:
            props["applyElevationOverlayColor"] = applyElevationOverlayColor
        if materialTapTargetSize is not None:
            props["materialTapTargetSize"] = _flut_pack_value(materialTapTargetSize)
        if pageTransitionsTheme is not None:
            props["pageTransitionsTheme"] = _flut_pack_value(pageTransitionsTheme)
        if platform is not None:
            props["platform"] = _flut_pack_value(platform)
        if splashFactory is not None:
            props["splashFactory"] = _flut_pack_value(splashFactory)
        if useSystemColors is not None:
            props["useSystemColors"] = useSystemColors
        if visualDensity is not None:
            props["visualDensity"] = _flut_pack_value(visualDensity)
        if inputDecorationTheme is not None:
            props["inputDecorationTheme"] = _flut_pack_value(inputDecorationTheme)
        self._flut_create(props=props)

    @property
    def brightness(self) -> Brightness:
        return self._flut_get("brightness")

    @property
    def colorScheme(self) -> ColorScheme:
        return self._flut_get("colorScheme")

    @property
    def useMaterial3(self) -> bool:
        return self._flut_get("useMaterial3")

    @property
    def textTheme(self) -> TextTheme:
        return self._flut_get("textTheme")

    @property
    def primaryColor(self) -> Color:
        return self._flut_get("primaryColor")

    @property
    def primaryColorDark(self) -> Color:
        return self._flut_get("primaryColorDark")

    @property
    def primaryColorLight(self) -> Color:
        return self._flut_get("primaryColorLight")

    @property
    def canvasColor(self) -> Color:
        return self._flut_get("canvasColor")

    @property
    def cardColor(self) -> Color:
        return self._flut_get("cardColor")

    @property
    def scaffoldBackgroundColor(self) -> Color:
        return self._flut_get("scaffoldBackgroundColor")

    @property
    def dividerColor(self) -> Color:
        return self._flut_get("dividerColor")

    @property
    def focusColor(self) -> Color:
        return self._flut_get("focusColor")

    @property
    def highlightColor(self) -> Color:
        return self._flut_get("highlightColor")

    @property
    def hintColor(self) -> Color:
        return self._flut_get("hintColor")

    @property
    def hoverColor(self) -> Color:
        return self._flut_get("hoverColor")

    @property
    def shadowColor(self) -> Color:
        return self._flut_get("shadowColor")

    @property
    def splashColor(self) -> Color:
        return self._flut_get("splashColor")

    @property
    def disabledColor(self) -> Color:
        return self._flut_get("disabledColor")

    @property
    def unselectedWidgetColor(self) -> Color:
        return self._flut_get("unselectedWidgetColor")

    @property
    def secondaryHeaderColor(self) -> Color:
        return self._flut_get("secondaryHeaderColor")

    @property
    def primaryTextTheme(self) -> TextTheme:
        return self._flut_get("primaryTextTheme")
