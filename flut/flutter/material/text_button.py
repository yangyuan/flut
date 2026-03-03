from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class TextButton(Widget):
    _flut_type = "TextButton"

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
        isSemanticButton: Optional[bool] = None,
        child: Widget,
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
        self.isSemanticButton = isSemanticButton
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["onPressed"] = (
            self._register_action(self.onPressed, "VoidCallback")._flut_pack()
            if self.onPressed is not None
            else None
        )
        result["autofocus"] = _flut_pack_value(self.autofocus)
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
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.statesController is not None:
            result["statesController"] = _flut_pack_value(self.statesController)
        if self.isSemanticButton is not None:
            result["isSemanticButton"] = _flut_pack_value(self.isSemanticButton)
        result["child"] = _flut_pack_value(self.child)
        return result
