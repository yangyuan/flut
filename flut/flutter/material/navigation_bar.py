from typing import Callable, Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.widgets.framework import Widget


class NavigationDestinationLabelBehavior(FlutEnumObject):
    alwaysShow: "NavigationDestinationLabelBehavior"
    alwaysHide: "NavigationDestinationLabelBehavior"
    onlyShowSelected: "NavigationDestinationLabelBehavior"


class NavigationDestination(Widget):
    _flut_type = "NavigationDestination"

    def __init__(
        self,
        *,
        key=None,
        icon: Widget,
        selectedIcon: Optional[Widget] = None,
        label: str,
        tooltip: Optional[str] = None,
        enabled: bool = True,
    ):
        super().__init__(key=key)
        self.icon = icon
        self.selectedIcon = selectedIcon
        self.label = label
        self.tooltip = tooltip
        self.enabled = enabled

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["icon"] = _flut_pack_value(self.icon)
        result["label"] = _flut_pack_value(self.label)
        result["enabled"] = _flut_pack_value(self.enabled)
        if self.selectedIcon is not None:
            result["selectedIcon"] = _flut_pack_value(self.selectedIcon)
        if self.tooltip is not None:
            result["tooltip"] = _flut_pack_value(self.tooltip)
        return result


class NavigationBar(Widget):
    _flut_type = "NavigationBar"

    def __init__(
        self,
        *,
        key=None,
        animationDuration=None,
        selectedIndex: int = 0,
        destinations: list[Widget],
        onDestinationSelected: Optional[Callable[[int], None]] = None,
        backgroundColor: Optional[Color] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        indicatorColor: Optional[Color] = None,
        indicatorShape=None,
        height: Optional[float] = None,
        labelBehavior: Optional["NavigationDestinationLabelBehavior"] = None,
        overlayColor=None,
        labelTextStyle=None,
        labelPadding=None,
        maintainBottomViewPadding: bool = False,
    ):
        super().__init__(key=key)
        self.animationDuration = animationDuration
        self.selectedIndex = selectedIndex
        self.destinations = destinations
        self.onDestinationSelected = onDestinationSelected
        self.backgroundColor = backgroundColor
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.indicatorColor = indicatorColor
        self.indicatorShape = indicatorShape
        self.height = height
        self.labelBehavior = labelBehavior
        self.overlayColor = overlayColor
        self.labelTextStyle = labelTextStyle
        self.labelPadding = labelPadding
        self.maintainBottomViewPadding = maintainBottomViewPadding

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["destinations"] = _flut_pack_value(self.destinations)
        result["selectedIndex"] = _flut_pack_value(self.selectedIndex)
        result["maintainBottomViewPadding"] = _flut_pack_value(
            self.maintainBottomViewPadding
        )
        if self.animationDuration is not None:
            result["animationDuration"] = _flut_pack_value(self.animationDuration)
        if self.onDestinationSelected is not None:
            result["onDestinationSelected"] = self._register_action(
                self.onDestinationSelected, "ValueChanged<int>"
            )._flut_pack()
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.indicatorColor is not None:
            result["indicatorColor"] = _flut_pack_value(self.indicatorColor)
        if self.indicatorShape is not None:
            result["indicatorShape"] = _flut_pack_value(self.indicatorShape)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.labelBehavior is not None:
            result["labelBehavior"] = _flut_pack_value(self.labelBehavior)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.labelTextStyle is not None:
            result["labelTextStyle"] = _flut_pack_value(self.labelTextStyle)
        if self.labelPadding is not None:
            result["labelPadding"] = _flut_pack_value(self.labelPadding)
        return result
