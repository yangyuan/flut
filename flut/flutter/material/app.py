from typing import Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class ThemeMode(FlutEnumObject):
    system: "ThemeMode"
    light: "ThemeMode"
    dark: "ThemeMode"


class MaterialApp(Widget):
    _flut_type = "MaterialApp"

    def __init__(
        self,
        *,
        key=None,
        home: Optional[Widget] = None,
        title: str = "",
        theme=None,
        darkTheme=None,
        highContrastTheme=None,
        highContrastDarkTheme=None,
        themeMode: Optional["ThemeMode"] = None,
        color=None,
        debugShowCheckedModeBanner: bool = True,
    ):
        super().__init__(key=key)
        self.home = home
        self.title = title
        self.theme = theme
        self.darkTheme = darkTheme
        self.highContrastTheme = highContrastTheme
        self.highContrastDarkTheme = highContrastDarkTheme
        self.themeMode = themeMode
        self.color = color
        self.debugShowCheckedModeBanner = debugShowCheckedModeBanner

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["title"] = _flut_pack_value(self.title)
        result["debugShowCheckedModeBanner"] = _flut_pack_value(
            self.debugShowCheckedModeBanner
        )
        if self.theme is not None:
            result["theme"] = _flut_pack_value(self.theme)
        if self.darkTheme is not None:
            result["darkTheme"] = _flut_pack_value(self.darkTheme)
        if self.highContrastTheme is not None:
            result["highContrastTheme"] = _flut_pack_value(self.highContrastTheme)
        if self.highContrastDarkTheme is not None:
            result["highContrastDarkTheme"] = _flut_pack_value(
                self.highContrastDarkTheme
            )
        if self.themeMode is not None:
            result["themeMode"] = _flut_pack_value(self.themeMode)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.home is not None:
            result["home"] = _flut_pack_value(self.home)
        return result
