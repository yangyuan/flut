from typing import Optional, override

from flut._flut.engine import _flut_pack_value, call_dart_static
from flut.flutter.widgets.framework import Widget


class IconButton(Widget):
    _flut_type = "IconButton"

    def __init__(
        self,
        *,
        key=None,
        iconSize: Optional[float] = None,
        padding=None,
        alignment=None,
        splashRadius: Optional[float] = None,
        color=None,
        focusColor=None,
        hoverColor=None,
        highlightColor=None,
        splashColor=None,
        disabledColor=None,
        onPressed=None,
        onLongPress=None,
        mouseCursor=None,
        focusNode=None,
        autofocus: bool = False,
        tooltip: Optional[str] = None,
        enableFeedback: Optional[bool] = None,
        constraints=None,
        style=None,
        isSelected: Optional[bool] = None,
        selectedIcon: Optional[Widget] = None,
        icon: Widget,
    ):
        super().__init__(key=key)
        self.iconSize = iconSize
        self.padding = padding
        self.alignment = alignment
        self.splashRadius = splashRadius
        self.color = color
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.highlightColor = highlightColor
        self.splashColor = splashColor
        self.disabledColor = disabledColor
        self.onPressed = onPressed
        self.onLongPress = onLongPress
        self.mouseCursor = mouseCursor
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.tooltip = tooltip
        self.enableFeedback = enableFeedback
        self.constraints = constraints
        self.style = style
        self.isSelected = isSelected
        self.selectedIcon = selectedIcon
        self.icon = icon

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["onPressed"] = (
            self._register_action(self.onPressed, "VoidCallback")._flut_pack()
            if self.onPressed is not None
            else None
        )
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.iconSize is not None:
            result["iconSize"] = _flut_pack_value(self.iconSize)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.splashRadius is not None:
            result["splashRadius"] = _flut_pack_value(self.splashRadius)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.highlightColor is not None:
            result["highlightColor"] = _flut_pack_value(self.highlightColor)
        if self.splashColor is not None:
            result["splashColor"] = _flut_pack_value(self.splashColor)
        if self.disabledColor is not None:
            result["disabledColor"] = _flut_pack_value(self.disabledColor)
        if self.onLongPress is not None:
            result["onLongPress"] = self._register_action(
                self.onLongPress, "VoidCallback"
            )._flut_pack()
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.tooltip is not None:
            result["tooltip"] = _flut_pack_value(self.tooltip)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.isSelected is not None:
            result["isSelected"] = _flut_pack_value(self.isSelected)
        if self.selectedIcon is not None:
            result["selectedIcon"] = _flut_pack_value(self.selectedIcon)
        result["icon"] = _flut_pack_value(self.icon)
        return result

    @staticmethod
    def styleFrom(
        *,
        foregroundColor=None,
        backgroundColor=None,
        disabledForegroundColor=None,
        disabledBackgroundColor=None,
        focusColor=None,
        hoverColor=None,
        highlightColor=None,
        shadowColor=None,
        surfaceTintColor=None,
        overlayColor=None,
        elevation=None,
        minimumSize=None,
        fixedSize=None,
        maximumSize=None,
        iconSize=None,
        side=None,
        shape=None,
        padding=None,
        enabledMouseCursor=None,
        disabledMouseCursor=None,
        visualDensity=None,
        tapTargetSize=None,
        animationDuration=None,
        enableFeedback=None,
        alignment=None,
        splashFactory=None,
    ):
        kwargs = {}
        if foregroundColor is not None:
            kwargs["foregroundColor"] = _flut_pack_value(foregroundColor)
        if backgroundColor is not None:
            kwargs["backgroundColor"] = _flut_pack_value(backgroundColor)
        if disabledForegroundColor is not None:
            kwargs["disabledForegroundColor"] = _flut_pack_value(
                disabledForegroundColor
            )
        if disabledBackgroundColor is not None:
            kwargs["disabledBackgroundColor"] = _flut_pack_value(
                disabledBackgroundColor
            )
        if focusColor is not None:
            kwargs["focusColor"] = _flut_pack_value(focusColor)
        if hoverColor is not None:
            kwargs["hoverColor"] = _flut_pack_value(hoverColor)
        if highlightColor is not None:
            kwargs["highlightColor"] = _flut_pack_value(highlightColor)
        if shadowColor is not None:
            kwargs["shadowColor"] = _flut_pack_value(shadowColor)
        if surfaceTintColor is not None:
            kwargs["surfaceTintColor"] = _flut_pack_value(surfaceTintColor)
        if overlayColor is not None:
            kwargs["overlayColor"] = _flut_pack_value(overlayColor)
        if elevation is not None:
            kwargs["elevation"] = _flut_pack_value(elevation)
        if minimumSize is not None:
            kwargs["minimumSize"] = _flut_pack_value(minimumSize)
        if fixedSize is not None:
            kwargs["fixedSize"] = _flut_pack_value(fixedSize)
        if maximumSize is not None:
            kwargs["maximumSize"] = _flut_pack_value(maximumSize)
        if iconSize is not None:
            kwargs["iconSize"] = _flut_pack_value(iconSize)
        if side is not None:
            kwargs["side"] = _flut_pack_value(side)
        if shape is not None:
            kwargs["shape"] = _flut_pack_value(shape)
        if padding is not None:
            kwargs["padding"] = _flut_pack_value(padding)
        if enabledMouseCursor is not None:
            kwargs["enabledMouseCursor"] = _flut_pack_value(enabledMouseCursor)
        if disabledMouseCursor is not None:
            kwargs["disabledMouseCursor"] = _flut_pack_value(disabledMouseCursor)
        if visualDensity is not None:
            kwargs["visualDensity"] = _flut_pack_value(visualDensity)
        if tapTargetSize is not None:
            kwargs["tapTargetSize"] = _flut_pack_value(tapTargetSize)
        if animationDuration is not None:
            kwargs["animationDuration"] = _flut_pack_value(animationDuration)
        if enableFeedback is not None:
            kwargs["enableFeedback"] = _flut_pack_value(enableFeedback)
        if alignment is not None:
            kwargs["alignment"] = _flut_pack_value(alignment)
        if splashFactory is not None:
            kwargs["splashFactory"] = _flut_pack_value(splashFactory)
        return call_dart_static("IconButton", "styleFrom", **kwargs)
