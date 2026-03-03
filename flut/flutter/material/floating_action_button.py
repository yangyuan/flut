from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip
from flut.flutter.widgets.framework import Widget


class FloatingActionButton(Widget):
    _flut_type = "FloatingActionButton"

    def __init__(
        self,
        *,
        key=None,
        tooltip: Optional[str] = None,
        foregroundColor=None,
        backgroundColor=None,
        focusColor=None,
        hoverColor=None,
        splashColor=None,
        elevation: Optional[float] = None,
        focusElevation: Optional[float] = None,
        hoverElevation: Optional[float] = None,
        highlightElevation: Optional[float] = None,
        disabledElevation: Optional[float] = None,
        onPressed=None,
        mouseCursor=None,
        mini: bool = False,
        clipBehavior: Clip = Clip.none,
        focusNode=None,
        autofocus: bool = False,
        materialTapTargetSize=None,
        isExtended: bool = False,
        enableFeedback: Optional[bool] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.tooltip = tooltip
        self.foregroundColor = foregroundColor
        self.backgroundColor = backgroundColor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.splashColor = splashColor
        self.elevation = elevation
        self.focusElevation = focusElevation
        self.hoverElevation = hoverElevation
        self.highlightElevation = highlightElevation
        self.disabledElevation = disabledElevation
        self.onPressed = onPressed
        self.mouseCursor = mouseCursor
        self.mini = mini
        self.clipBehavior = clipBehavior
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.materialTapTargetSize = materialTapTargetSize
        self.isExtended = isExtended
        self.enableFeedback = enableFeedback
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["onPressed"] = (
            self._register_action(self.onPressed, "VoidCallback")._flut_pack()
            if self.onPressed is not None
            else None
        )
        result["mini"] = _flut_pack_value(self.mini)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        result["isExtended"] = _flut_pack_value(self.isExtended)
        if self.tooltip is not None:
            result["tooltip"] = _flut_pack_value(self.tooltip)
        if self.foregroundColor is not None:
            result["foregroundColor"] = _flut_pack_value(self.foregroundColor)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.splashColor is not None:
            result["splashColor"] = _flut_pack_value(self.splashColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.focusElevation is not None:
            result["focusElevation"] = _flut_pack_value(self.focusElevation)
        if self.hoverElevation is not None:
            result["hoverElevation"] = _flut_pack_value(self.hoverElevation)
        if self.highlightElevation is not None:
            result["highlightElevation"] = _flut_pack_value(self.highlightElevation)
        if self.disabledElevation is not None:
            result["disabledElevation"] = _flut_pack_value(self.disabledElevation)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.materialTapTargetSize is not None:
            result["materialTapTargetSize"] = _flut_pack_value(
                self.materialTapTargetSize
            )
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
