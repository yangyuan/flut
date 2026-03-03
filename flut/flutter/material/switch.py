from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.widgets.framework import Widget


class Switch(Widget):
    _flut_type = "Switch"

    def __init__(
        self,
        *,
        key=None,
        value: bool,
        onChanged=None,
        activeThumbColor=None,
        activeTrackColor=None,
        inactiveThumbColor=None,
        inactiveTrackColor=None,
        activeThumbImage=None,
        onActiveThumbImageError=None,
        inactiveThumbImage=None,
        onInactiveThumbImageError=None,
        thumbColor=None,
        trackColor=None,
        trackOutlineColor=None,
        trackOutlineWidth=None,
        thumbIcon=None,
        materialTapTargetSize=None,
        dragStartBehavior: DragStartBehavior = DragStartBehavior.start,
        mouseCursor=None,
        focusColor=None,
        hoverColor=None,
        overlayColor=None,
        splashRadius: Optional[float] = None,
        focusNode=None,
        onFocusChange=None,
        autofocus: bool = False,
        padding=None,
    ):
        super().__init__(key=key)
        self.value = value
        self.onChanged = onChanged
        self.activeThumbColor = activeThumbColor
        self.activeTrackColor = activeTrackColor
        self.inactiveThumbColor = inactiveThumbColor
        self.inactiveTrackColor = inactiveTrackColor
        self.activeThumbImage = activeThumbImage
        self.onActiveThumbImageError = onActiveThumbImageError
        self.inactiveThumbImage = inactiveThumbImage
        self.onInactiveThumbImageError = onInactiveThumbImageError
        self.thumbColor = thumbColor
        self.trackColor = trackColor
        self.trackOutlineColor = trackOutlineColor
        self.trackOutlineWidth = trackOutlineWidth
        self.thumbIcon = thumbIcon
        self.materialTapTargetSize = materialTapTargetSize
        self.dragStartBehavior = dragStartBehavior
        self.mouseCursor = mouseCursor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.overlayColor = overlayColor
        self.splashRadius = splashRadius
        self.focusNode = focusNode
        self.onFocusChange = onFocusChange
        self.autofocus = autofocus
        self.padding = padding

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        result["onChanged"] = (
            self._register_action(self.onChanged, "ValueChanged<bool>")._flut_pack()
            if self.onChanged is not None
            else None
        )
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.activeThumbColor is not None:
            result["activeThumbColor"] = _flut_pack_value(self.activeThumbColor)
        if self.activeTrackColor is not None:
            result["activeTrackColor"] = _flut_pack_value(self.activeTrackColor)
        if self.inactiveThumbColor is not None:
            result["inactiveThumbColor"] = _flut_pack_value(self.inactiveThumbColor)
        if self.inactiveTrackColor is not None:
            result["inactiveTrackColor"] = _flut_pack_value(self.inactiveTrackColor)
        if self.activeThumbImage is not None:
            result["activeThumbImage"] = _flut_pack_value(self.activeThumbImage)
        if self.onActiveThumbImageError is not None:
            result["onActiveThumbImageError"] = self._register_action(
                self.onActiveThumbImageError, "ImageErrorListener"
            )._flut_pack()
        if self.inactiveThumbImage is not None:
            result["inactiveThumbImage"] = _flut_pack_value(self.inactiveThumbImage)
        if self.onInactiveThumbImageError is not None:
            result["onInactiveThumbImageError"] = self._register_action(
                self.onInactiveThumbImageError, "ImageErrorListener"
            )._flut_pack()
        if self.thumbColor is not None:
            result["thumbColor"] = _flut_pack_value(self.thumbColor)
        if self.trackColor is not None:
            result["trackColor"] = _flut_pack_value(self.trackColor)
        if self.trackOutlineColor is not None:
            result["trackOutlineColor"] = _flut_pack_value(self.trackOutlineColor)
        if self.trackOutlineWidth is not None:
            result["trackOutlineWidth"] = _flut_pack_value(self.trackOutlineWidth)
        if self.thumbIcon is not None:
            result["thumbIcon"] = _flut_pack_value(self.thumbIcon)
        if self.materialTapTargetSize is not None:
            result["materialTapTargetSize"] = _flut_pack_value(
                self.materialTapTargetSize
            )
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.splashRadius is not None:
            result["splashRadius"] = _flut_pack_value(self.splashRadius)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.onFocusChange is not None:
            result["onFocusChange"] = self._register_action(
                self.onFocusChange, "ValueChanged<bool>"
            )._flut_pack()
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        return result
