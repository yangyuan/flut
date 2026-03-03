from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class AppBar(Widget):
    _flut_type = "AppBar"

    def __init__(
        self,
        *,
        key=None,
        leading: Optional[Widget] = None,
        automaticallyImplyLeading: bool = True,
        title: Optional[Widget] = None,
        actions=None,
        elevation: Optional[float] = None,
        scrolledUnderElevation: Optional[float] = None,
        shadowColor=None,
        surfaceTintColor=None,
        backgroundColor=None,
        foregroundColor=None,
        primary: bool = True,
        centerTitle: Optional[bool] = None,
        titleSpacing: Optional[float] = None,
        toolbarOpacity: float = 1.0,
        bottomOpacity: float = 1.0,
        toolbarHeight: Optional[float] = None,
        leadingWidth: Optional[float] = None,
        toolbarTextStyle=None,
        titleTextStyle=None,
        forceMaterialTransparency: bool = False,
        clipBehavior=None,
        bottom=None,
    ):
        super().__init__(key=key)
        self.leading = leading
        self.automaticallyImplyLeading = automaticallyImplyLeading
        self.title = title
        self.actions = actions
        self.elevation = elevation
        self.scrolledUnderElevation = scrolledUnderElevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.backgroundColor = backgroundColor
        self.foregroundColor = foregroundColor
        self.primary = primary
        self.centerTitle = centerTitle
        self.titleSpacing = titleSpacing
        self.toolbarOpacity = toolbarOpacity
        self.bottomOpacity = bottomOpacity
        self.toolbarHeight = toolbarHeight
        self.leadingWidth = leadingWidth
        self.toolbarTextStyle = toolbarTextStyle
        self.titleTextStyle = titleTextStyle
        self.forceMaterialTransparency = forceMaterialTransparency
        self.clipBehavior = clipBehavior
        self.bottom = bottom

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["automaticallyImplyLeading"] = _flut_pack_value(
            self.automaticallyImplyLeading
        )
        result["primary"] = _flut_pack_value(self.primary)
        result["toolbarOpacity"] = _flut_pack_value(self.toolbarOpacity)
        result["bottomOpacity"] = _flut_pack_value(self.bottomOpacity)
        result["forceMaterialTransparency"] = _flut_pack_value(
            self.forceMaterialTransparency
        )
        if self.leading is not None:
            result["leading"] = _flut_pack_value(self.leading)
        if self.title is not None:
            result["title"] = _flut_pack_value(self.title)
        if self.actions is not None:
            result["actions"] = _flut_pack_value(self.actions)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.scrolledUnderElevation is not None:
            result["scrolledUnderElevation"] = _flut_pack_value(
                self.scrolledUnderElevation
            )
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.foregroundColor is not None:
            result["foregroundColor"] = _flut_pack_value(self.foregroundColor)
        if self.centerTitle is not None:
            result["centerTitle"] = _flut_pack_value(self.centerTitle)
        if self.titleSpacing is not None:
            result["titleSpacing"] = _flut_pack_value(self.titleSpacing)
        if self.toolbarHeight is not None:
            result["toolbarHeight"] = _flut_pack_value(self.toolbarHeight)
        if self.leadingWidth is not None:
            result["leadingWidth"] = _flut_pack_value(self.leadingWidth)
        if self.toolbarTextStyle is not None:
            result["toolbarTextStyle"] = _flut_pack_value(self.toolbarTextStyle)
        if self.titleTextStyle is not None:
            result["titleTextStyle"] = _flut_pack_value(self.titleTextStyle)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.bottom is not None:
            result["bottom"] = _flut_pack_value(self.bottom)
        return result
