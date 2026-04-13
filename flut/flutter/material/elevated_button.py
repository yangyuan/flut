from typing import Optional, override

from flut._flut.engine import (
    FlutRealtimeObject,
    named_constructor,
    _flut_pack_value,
    call_dart_static,
)
from flut.dart.ui import Clip
from flut.flutter.material.ink_well import InteractiveInkFeatureFactory
from flut.flutter.widgets.framework import Widget


class ElevatedButton(Widget):
    _flut_type = "ElevatedButton"

    def __init__(
        self,
        *,
        key=None,
        onPressed=None,
        onLongPress=None,
        onHover=None,
        onFocusChange=None,
        style=None,
        focusNode=None,
        autofocus: bool = False,
        clipBehavior=None,
        statesController=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onPressed = onPressed
        self.onLongPress = onLongPress
        self.onHover = onHover
        self.onFocusChange = onFocusChange
        self.style = style
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.clipBehavior = clipBehavior
        self.statesController = statesController
        self.child = child

    @named_constructor
    def icon(
        cls,
        *,
        key=None,
        onPressed=None,
        onLongPress=None,
        onHover=None,
        onFocusChange=None,
        style=None,
        focusNode=None,
        autofocus: bool = False,
        clipBehavior=Clip.none,
        statesController=None,
        icon: Optional[Widget] = None,
        label: Widget,
        iconAlignment=None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.onPressed = onPressed
        instance.onLongPress = onLongPress
        instance.onHover = onHover
        instance.onFocusChange = onFocusChange
        instance.style = style
        instance.focusNode = focusNode
        instance.autofocus = autofocus
        instance.clipBehavior = clipBehavior
        instance.statesController = statesController
        instance.child = None
        instance.icon = icon
        instance.label = label
        instance.iconAlignment = iconAlignment
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["onPressed"] = (
            self._register_action(self.onPressed, "VoidCallback")._flut_pack()
            if self.onPressed is not None
            else None
        )
        if self.onLongPress is not None:
            result["onLongPress"] = self._register_action(
                self.onLongPress, "VoidCallback"
            )._flut_pack()
        if self.onHover is not None:
            result["onHover"] = self._register_action(
                self.onHover, "ValueChanged<bool>"
            )._flut_pack()
        if self.onFocusChange is not None:
            result["onFocusChange"] = self._register_action(
                self.onFocusChange, "ValueChanged<bool>"
            )._flut_pack()
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.statesController is not None:
            result["statesController"] = _flut_pack_value(self.statesController)
        if self._flut_init is None:
            if self.clipBehavior is not None:
                result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
            result["child"] = (
                _flut_pack_value(self.child) if self.child is not None else None
            )
        if self._flut_init == "icon":
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
            if self.icon is not None:
                result["icon"] = _flut_pack_value(self.icon)
            result["label"] = _flut_pack_value(self.label)
            if self.iconAlignment is not None:
                result["iconAlignment"] = _flut_pack_value(self.iconAlignment)
        return result

    @staticmethod
    def styleFrom(
        *,
        foregroundColor=None,
        backgroundColor=None,
        disabledForegroundColor=None,
        disabledBackgroundColor=None,
        shadowColor=None,
        surfaceTintColor=None,
        iconColor=None,
        iconSize=None,
        disabledIconColor=None,
        overlayColor=None,
        elevation=None,
        textStyle=None,
        padding=None,
        minimumSize=None,
        fixedSize=None,
        maximumSize=None,
        side=None,
        shape=None,
        enabledMouseCursor=None,
        disabledMouseCursor=None,
        visualDensity=None,
        tapTargetSize=None,
        animationDuration=None,
        enableFeedback=None,
        alignment=None,
        splashFactory: Optional[InteractiveInkFeatureFactory] = None,
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
        if shadowColor is not None:
            kwargs["shadowColor"] = _flut_pack_value(shadowColor)
        if surfaceTintColor is not None:
            kwargs["surfaceTintColor"] = _flut_pack_value(surfaceTintColor)
        if iconColor is not None:
            kwargs["iconColor"] = _flut_pack_value(iconColor)
        if iconSize is not None:
            kwargs["iconSize"] = _flut_pack_value(iconSize)
        if disabledIconColor is not None:
            kwargs["disabledIconColor"] = _flut_pack_value(disabledIconColor)
        if overlayColor is not None:
            kwargs["overlayColor"] = _flut_pack_value(overlayColor)
        if elevation is not None:
            kwargs["elevation"] = _flut_pack_value(elevation)
        if textStyle is not None:
            kwargs["textStyle"] = _flut_pack_value(textStyle)
        if padding is not None:
            kwargs["padding"] = _flut_pack_value(padding)
        if minimumSize is not None:
            kwargs["minimumSize"] = _flut_pack_value(minimumSize)
        if fixedSize is not None:
            kwargs["fixedSize"] = _flut_pack_value(fixedSize)
        if maximumSize is not None:
            kwargs["maximumSize"] = _flut_pack_value(maximumSize)
        if side is not None:
            kwargs["side"] = _flut_pack_value(side)
        if shape is not None:
            kwargs["shape"] = _flut_pack_value(shape)
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
        result = call_dart_static("ElevatedButton", "styleFrom", **kwargs)
        return result
