from typing import Optional, override

from flut._flut.engine import _flut_pack_value, call_dart_static
from flut.flutter.widgets.framework import Widget


class Tooltip(Widget):
    _flut_type = "Tooltip"

    def __init__(
        self,
        *,
        key=None,
        message: Optional[str] = None,
        richMessage=None,
        constraints=None,
        padding=None,
        margin=None,
        verticalOffset: Optional[float] = None,
        preferBelow: Optional[bool] = None,
        excludeFromSemantics: Optional[bool] = None,
        decoration=None,
        textStyle=None,
        textAlign=None,
        waitDuration=None,
        showDuration=None,
        exitDuration=None,
        enableTapToDismiss: bool = True,
        triggerMode=None,
        enableFeedback: Optional[bool] = None,
        onTriggered=None,
        mouseCursor=None,
        ignorePointer: Optional[bool] = None,
        positionDelegate=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.message = message
        self.richMessage = richMessage
        self.constraints = constraints
        self.padding = padding
        self.margin = margin
        self.verticalOffset = verticalOffset
        self.preferBelow = preferBelow
        self.excludeFromSemantics = excludeFromSemantics
        self.decoration = decoration
        self.textStyle = textStyle
        self.textAlign = textAlign
        self.waitDuration = waitDuration
        self.showDuration = showDuration
        self.exitDuration = exitDuration
        self.enableTapToDismiss = enableTapToDismiss
        self.triggerMode = triggerMode
        self.enableFeedback = enableFeedback
        self.onTriggered = onTriggered
        self.mouseCursor = mouseCursor
        self.ignorePointer = ignorePointer
        self.positionDelegate = positionDelegate
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.message is not None:
            result["message"] = _flut_pack_value(self.message)
        if self.richMessage is not None:
            result["richMessage"] = _flut_pack_value(self.richMessage)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.margin is not None:
            result["margin"] = _flut_pack_value(self.margin)
        if self.verticalOffset is not None:
            result["verticalOffset"] = _flut_pack_value(self.verticalOffset)
        if self.preferBelow is not None:
            result["preferBelow"] = _flut_pack_value(self.preferBelow)
        if self.excludeFromSemantics is not None:
            result["excludeFromSemantics"] = _flut_pack_value(self.excludeFromSemantics)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.textStyle is not None:
            result["textStyle"] = _flut_pack_value(self.textStyle)
        if self.textAlign is not None:
            result["textAlign"] = _flut_pack_value(self.textAlign)
        if self.waitDuration is not None:
            result["waitDuration"] = _flut_pack_value(self.waitDuration)
        if self.showDuration is not None:
            result["showDuration"] = _flut_pack_value(self.showDuration)
        if self.exitDuration is not None:
            result["exitDuration"] = _flut_pack_value(self.exitDuration)
        result["enableTapToDismiss"] = _flut_pack_value(self.enableTapToDismiss)
        if self.triggerMode is not None:
            result["triggerMode"] = _flut_pack_value(self.triggerMode)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.onTriggered is not None:
            result["onTriggered"] = self._register_action(
                self.onTriggered, "TooltipTriggeredCallback"
            )._flut_pack()
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.ignorePointer is not None:
            result["ignorePointer"] = _flut_pack_value(self.ignorePointer)
        if self.positionDelegate is not None:
            result["positionDelegate"] = _flut_pack_value(self.positionDelegate)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result

    @staticmethod
    def dismissAllToolTips() -> bool:
        return call_dart_static("Tooltip", "dismissAllToolTips")
