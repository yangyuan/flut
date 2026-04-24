from typing import Callable, Generic, Optional, TypeVar, override

from flut._flut.engine import (
    FlutRealtimeObject,
    _flut_pack_value,
    call_dart_static,
    transient_build_scope,
    wrap_popup_menu_item_builder,
)
from flut.dart.ui import Clip, Color, Offset
from flut.flutter.animation.animation_style import AnimationStyle
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.rendering.box import BoxConstraints
from flut.flutter.rendering.stack import RelativeRect
from flut.flutter.widgets.framework import Widget

T = TypeVar("T")


class PopupMenuItem(Widget, Generic[T]):
    _flut_type = "PopupMenuItem"

    def __init__(
        self,
        *,
        key=None,
        value: Optional[T] = None,
        onTap: Optional[Callable[[], None]] = None,
        enabled: bool = True,
        height: float = 48.0,
        padding: Optional[EdgeInsets] = None,
        textStyle: Optional[TextStyle] = None,
        labelTextStyle=None,
        mouseCursor=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.value = value
        self.onTap = onTap
        self.enabled = enabled
        self.height = height
        self.padding = padding
        self.textStyle = textStyle
        self.labelTextStyle = labelTextStyle
        self.mouseCursor = mouseCursor
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["enabled"] = _flut_pack_value(self.enabled)
        result["height"] = _flut_pack_value(self.height)
        if self.value is not None:
            result["value"] = _flut_pack_value(self.value)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "VoidCallback"
            )._flut_pack()
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.textStyle is not None:
            result["textStyle"] = _flut_pack_value(self.textStyle)
        if self.labelTextStyle is not None:
            result["labelTextStyle"] = _flut_pack_value(self.labelTextStyle)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class PopupMenuButton(Widget, Generic[T]):
    _flut_type = "PopupMenuButton"

    def __init__(
        self,
        *,
        key=None,
        itemBuilder: Callable,
        initialValue: Optional[T] = None,
        onOpened: Optional[Callable[[], None]] = None,
        onSelected: Optional[Callable[[T], None]] = None,
        onCanceled: Optional[Callable[[], None]] = None,
        tooltip: Optional[str] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        padding: EdgeInsets = EdgeInsets.all(8.0),
        menuPadding: Optional[EdgeInsets] = None,
        borderRadius=None,
        splashRadius: Optional[float] = None,
        icon: Optional[Widget] = None,
        iconSize: Optional[float] = None,
        offset: Offset = Offset(),
        enabled: bool = True,
        shape=None,
        color: Optional[Color] = None,
        iconColor: Optional[Color] = None,
        enableFeedback: Optional[bool] = None,
        constraints: Optional[BoxConstraints] = None,
        position=None,
        clipBehavior: Clip = Clip.none,
        useRootNavigator: bool = False,
        popUpAnimationStyle=None,
        routeSettings=None,
        style=None,
        requestFocus: Optional[bool] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.itemBuilder = itemBuilder
        self.initialValue = initialValue
        self.onOpened = onOpened
        self.onSelected = onSelected
        self.onCanceled = onCanceled
        self.tooltip = tooltip
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.padding = padding
        self.menuPadding = menuPadding
        self.borderRadius = borderRadius
        self.splashRadius = splashRadius
        self.icon = icon
        self.iconSize = iconSize
        self.offset = offset
        self.enabled = enabled
        self.shape = shape
        self.color = color
        self.iconColor = iconColor
        self.enableFeedback = enableFeedback
        self.constraints = constraints
        self.position = position
        self.clipBehavior = clipBehavior
        self.useRootNavigator = useRootNavigator
        self.popUpAnimationStyle = popUpAnimationStyle
        self.routeSettings = routeSettings
        self.style = style
        self.requestFocus = requestFocus
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["itemBuilder"] = self._register_build_action(
            wrap_popup_menu_item_builder(self.itemBuilder),
            "PopupMenuItemBuilder",
        )._flut_pack()
        result["padding"] = _flut_pack_value(self.padding)
        result["offset"] = _flut_pack_value(self.offset)
        result["enabled"] = _flut_pack_value(self.enabled)
        result["useRootNavigator"] = _flut_pack_value(self.useRootNavigator)
        if self.initialValue is not None:
            result["initialValue"] = _flut_pack_value(self.initialValue)
        if self.onOpened is not None:
            result["onOpened"] = self._register_action(
                self.onOpened, "VoidCallback"
            )._flut_pack()
        if self.onSelected is not None:
            result["onSelected"] = self._register_action(
                self.onSelected, "ValueChanged<dynamic?>"
            )._flut_pack()
        if self.onCanceled is not None:
            result["onCanceled"] = self._register_action(
                self.onCanceled, "VoidCallback"
            )._flut_pack()
        if self.tooltip is not None:
            result["tooltip"] = _flut_pack_value(self.tooltip)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.menuPadding is not None:
            result["menuPadding"] = _flut_pack_value(self.menuPadding)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.splashRadius is not None:
            result["splashRadius"] = _flut_pack_value(self.splashRadius)
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.iconSize is not None:
            result["iconSize"] = _flut_pack_value(self.iconSize)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.iconColor is not None:
            result["iconColor"] = _flut_pack_value(self.iconColor)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.position is not None:
            result["position"] = _flut_pack_value(self.position)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.popUpAnimationStyle is not None:
            result["popUpAnimationStyle"] = _flut_pack_value(self.popUpAnimationStyle)
        if self.routeSettings is not None:
            result["routeSettings"] = _flut_pack_value(self.routeSettings)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.requestFocus is not None:
            result["requestFocus"] = _flut_pack_value(self.requestFocus)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class PopupMenuDivider(Widget):
    _flut_type = "PopupMenuDivider"

    def __init__(
        self,
        *,
        key=None,
        height: float = 16.0,
        thickness: Optional[float] = None,
        indent: Optional[float] = None,
        endIndent: Optional[float] = None,
        radius=None,
        color: Optional[Color] = None,
    ):
        super().__init__(key=key)
        self.height = height
        self.thickness = thickness
        self.indent = indent
        self.endIndent = endIndent
        self.radius = radius
        self.color = color

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["height"] = _flut_pack_value(self.height)
        if self.thickness is not None:
            result["thickness"] = _flut_pack_value(self.thickness)
        if self.indent is not None:
            result["indent"] = _flut_pack_value(self.indent)
        if self.endIndent is not None:
            result["endIndent"] = _flut_pack_value(self.endIndent)
        if self.radius is not None:
            result["radius"] = _flut_pack_value(self.radius)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        return result


def showMenu(
    *,
    context,
    position: Optional[RelativeRect] = None,
    items,
    initialValue=None,
    elevation: Optional[float] = None,
    shadowColor: Optional[Color] = None,
    surfaceTintColor: Optional[Color] = None,
    semanticLabel: Optional[str] = None,
    shape=None,
    menuPadding=None,
    color: Optional[Color] = None,
    useRootNavigator: bool = False,
    constraints: Optional[BoxConstraints] = None,
    clipBehavior: Clip = Clip.none,
    routeSettings=None,
    popUpAnimationStyle: Optional[AnimationStyle] = None,
    requestFocus: Optional[bool] = None,
):
    with transient_build_scope():
        packed_items = [item._flut_pack() for item in items]

    kwargs = {
        "items": packed_items,
        "useRootNavigator": useRootNavigator,
        "clipBehavior": clipBehavior._flut_pack(),
    }
    if position is not None:
        kwargs["position"] = position._flut_pack()
    if initialValue is not None:
        kwargs["initialValue"] = _flut_pack_value(initialValue)
    if elevation is not None:
        kwargs["elevation"] = elevation
    if shadowColor is not None:
        kwargs["shadowColor"] = shadowColor._flut_pack()
    if surfaceTintColor is not None:
        kwargs["surfaceTintColor"] = surfaceTintColor._flut_pack()
    if semanticLabel is not None:
        kwargs["semanticLabel"] = semanticLabel
    if shape is not None:
        kwargs["shape"] = shape._flut_pack()
    if menuPadding is not None:
        kwargs["menuPadding"] = menuPadding._flut_pack()
    if color is not None:
        kwargs["color"] = color._flut_pack()
    if constraints is not None:
        kwargs["constraints"] = constraints._flut_pack()
    if routeSettings is not None:
        kwargs["routeSettings"] = routeSettings._flut_pack()
    if popUpAnimationStyle is not None:
        kwargs["popUpAnimationStyle"] = popUpAnimationStyle._flut_pack()
    if requestFocus is not None:
        kwargs["requestFocus"] = requestFocus
    return call_dart_static("showMenu", "showMenu", context._flut_pack(), **kwargs)
