from typing import Callable, Optional, override

from flut._flut.engine import (
    FlutAbstractObject,
    FlutRealtimeObject,
    _flut_pack_value,
    call_dart_static,
)
from flut.flutter.widgets.framework import Widget


class InteractiveInkFeatureFactory(FlutRealtimeObject, FlutAbstractObject):
    _flut_type = "InteractiveInkFeatureFactory"

    def __init__(self) -> None:
        FlutRealtimeObject.__init__(self)

    def create(
        self,
        *,
        controller: "MaterialInkController",
        referenceBox: "RenderBox",
        position: "Offset",
        color: "Color",
        textDirection: "TextDirection",
        containedInkWell: bool = False,
        rectCallback: "RectCallback | None" = None,
        borderRadius: "BorderRadius | None" = None,
        customBorder: "ShapeBorder | None" = None,
        radius: Optional[float] = None,
        onRemoved: "Callable[[], None] | None" = None,
    ) -> "InteractiveInkFeature":
        raise NotImplementedError


class InkSplash:
    @staticmethod
    def splashFactory() -> InteractiveInkFeatureFactory:
        return call_dart_static("InkSplash", "splashFactory")


class InkRipple:
    @staticmethod
    def splashFactory() -> InteractiveInkFeatureFactory:
        return call_dart_static("InkRipple", "splashFactory")


class NoSplash:
    @staticmethod
    def splashFactory() -> InteractiveInkFeatureFactory:
        return call_dart_static("NoSplash", "splashFactory")


class InkWell(Widget):
    _flut_type = "InkWell"

    def __init__(
        self,
        *,
        key=None,
        onTap=None,
        onDoubleTap=None,
        onLongPress=None,
        onLongPressUp=None,
        onTapDown: Optional[Callable] = None,
        onTapUp: Optional[Callable] = None,
        onTapCancel=None,
        onSecondaryTap=None,
        onSecondaryTapUp: Optional[Callable] = None,
        onSecondaryTapDown: Optional[Callable] = None,
        onSecondaryTapCancel=None,
        onHighlightChanged=None,
        onHover=None,
        mouseCursor=None,
        focusColor=None,
        hoverColor=None,
        highlightColor=None,
        overlayColor=None,
        splashColor=None,
        splashFactory: Optional[InteractiveInkFeatureFactory] = None,
        radius: Optional[float] = None,
        borderRadius=None,
        customBorder=None,
        enableFeedback: bool = True,
        excludeFromSemantics: bool = False,
        focusNode=None,
        canRequestFocus: bool = True,
        onFocusChange=None,
        autofocus: bool = False,
        statesController=None,
        hoverDuration=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onTap = onTap
        self.onDoubleTap = onDoubleTap
        self.onLongPress = onLongPress
        self.onLongPressUp = onLongPressUp
        self.onTapDown = onTapDown
        self.onTapUp = onTapUp
        self.onTapCancel = onTapCancel
        self.onSecondaryTap = onSecondaryTap
        self.onSecondaryTapUp = onSecondaryTapUp
        self.onSecondaryTapDown = onSecondaryTapDown
        self.onSecondaryTapCancel = onSecondaryTapCancel
        self.onHighlightChanged = onHighlightChanged
        self.onHover = onHover
        self.mouseCursor = mouseCursor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.highlightColor = highlightColor
        self.overlayColor = overlayColor
        self.splashColor = splashColor
        self.splashFactory = splashFactory
        self.radius = radius
        self.borderRadius = borderRadius
        self.customBorder = customBorder
        self.enableFeedback = enableFeedback
        self.excludeFromSemantics = excludeFromSemantics
        self.focusNode = focusNode
        self.canRequestFocus = canRequestFocus
        self.onFocusChange = onFocusChange
        self.autofocus = autofocus
        self.statesController = statesController
        self.hoverDuration = hoverDuration
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        result["excludeFromSemantics"] = _flut_pack_value(self.excludeFromSemantics)
        result["canRequestFocus"] = _flut_pack_value(self.canRequestFocus)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "GestureTapCallback"
            )._flut_pack()
        if self.onDoubleTap is not None:
            result["onDoubleTap"] = self._register_action(
                self.onDoubleTap, "GestureTapCallback"
            )._flut_pack()
        if self.onLongPress is not None:
            result["onLongPress"] = self._register_action(
                self.onLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onLongPressUp is not None:
            result["onLongPressUp"] = self._register_action(
                self.onLongPressUp, "GestureLongPressUpCallback"
            )._flut_pack()
        if self.onTapDown is not None:
            result["onTapDown"] = self._register_action(
                self.onTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onTapUp is not None:
            result["onTapUp"] = self._register_action(
                self.onTapUp, "GestureTapUpCallback"
            )._flut_pack()
        if self.onTapCancel is not None:
            result["onTapCancel"] = self._register_action(
                self.onTapCancel, "GestureTapCallback"
            )._flut_pack()
        if self.onSecondaryTap is not None:
            result["onSecondaryTap"] = self._register_action(
                self.onSecondaryTap, "GestureTapCallback"
            )._flut_pack()
        if self.onSecondaryTapUp is not None:
            result["onSecondaryTapUp"] = self._register_action(
                self.onSecondaryTapUp, "GestureTapUpCallback"
            )._flut_pack()
        if self.onSecondaryTapDown is not None:
            result["onSecondaryTapDown"] = self._register_action(
                self.onSecondaryTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onSecondaryTapCancel is not None:
            result["onSecondaryTapCancel"] = self._register_action(
                self.onSecondaryTapCancel, "GestureTapCallback"
            )._flut_pack()
        if self.onHighlightChanged is not None:
            result["onHighlightChanged"] = self._register_action(
                self.onHighlightChanged, "ValueChanged<bool>"
            )._flut_pack()
        if self.onHover is not None:
            result["onHover"] = self._register_action(
                self.onHover, "ValueChanged<bool>"
            )._flut_pack()
        if self.onFocusChange is not None:
            result["onFocusChange"] = self._register_action(
                self.onFocusChange, "ValueChanged<bool>"
            )._flut_pack()
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.highlightColor is not None:
            result["highlightColor"] = _flut_pack_value(self.highlightColor)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.splashColor is not None:
            result["splashColor"] = _flut_pack_value(self.splashColor)
        if self.splashFactory is not None:
            result["splashFactory"] = _flut_pack_value(self.splashFactory)
        if self.radius is not None:
            result["radius"] = _flut_pack_value(self.radius)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.customBorder is not None:
            result["customBorder"] = _flut_pack_value(self.customBorder)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.statesController is not None:
            result["statesController"] = _flut_pack_value(self.statesController)
        if self.hoverDuration is not None:
            result["hoverDuration"] = _flut_pack_value(self.hoverDuration)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
