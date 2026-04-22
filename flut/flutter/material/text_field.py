from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip, TextAlign
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.material.input_decorator import InputDecoration
from flut.flutter.widgets.framework import Widget


class TextField(Widget):
    _flut_type = "TextField"

    def __init__(
        self,
        *,
        key=None,
        controller=None,
        focusNode=None,
        decoration: Optional[InputDecoration] = InputDecoration(),
        style=None,
        textAlign: TextAlign = TextAlign.start,
        textDirection=None,
        readOnly: bool = False,
        autofocus: bool = False,
        obscureText: bool = False,
        maxLines: Optional[int] = 1,
        minLines: Optional[int] = None,
        expands: bool = False,
        maxLength: Optional[int] = None,
        onChanged=None,
        onEditingComplete=None,
        onSubmitted=None,
        enabled: Optional[bool] = None,
        cursorWidth: float = 2.0,
        cursorHeight: Optional[float] = None,
        cursorColor=None,
        dragStartBehavior: DragStartBehavior = DragStartBehavior.start,
        onTap=None,
        onTapOutside=None,
        onTapUpOutside=None,
        mouseCursor=None,
        clipBehavior: Clip = Clip.hardEdge,
    ):
        super().__init__(key=key)
        self.controller = controller
        self.focusNode = focusNode
        self.decoration = decoration
        self.style = style
        self.textAlign = textAlign
        self.textDirection = textDirection
        self.readOnly = readOnly
        self.autofocus = autofocus
        self.obscureText = obscureText
        self.maxLines = maxLines
        self.minLines = minLines
        self.expands = expands
        self.maxLength = maxLength
        self.onChanged = onChanged
        self.onEditingComplete = onEditingComplete
        self.onSubmitted = onSubmitted
        self.enabled = enabled
        self.cursorWidth = cursorWidth
        self.cursorHeight = cursorHeight
        self.cursorColor = cursorColor
        self.dragStartBehavior = dragStartBehavior
        self.onTap = onTap
        self.onTapOutside = onTapOutside
        self.onTapUpOutside = onTapUpOutside
        self.mouseCursor = mouseCursor
        self.clipBehavior = clipBehavior

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["textAlign"] = _flut_pack_value(self.textAlign)
        result["readOnly"] = _flut_pack_value(self.readOnly)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        result["obscureText"] = _flut_pack_value(self.obscureText)
        result["expands"] = _flut_pack_value(self.expands)
        result["cursorWidth"] = _flut_pack_value(self.cursorWidth)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        if self.maxLines is not None:
            result["maxLines"] = _flut_pack_value(self.maxLines)
        if self.minLines is not None:
            result["minLines"] = _flut_pack_value(self.minLines)
        if self.maxLength is not None:
            result["maxLength"] = _flut_pack_value(self.maxLength)
        if self.onChanged is not None:
            result["onChanged"] = self._register_action(
                self.onChanged, "ValueChanged<String>"
            )._flut_pack()
        if self.onEditingComplete is not None:
            result["onEditingComplete"] = self._register_action(
                self.onEditingComplete, "VoidCallback"
            )._flut_pack()
        if self.onSubmitted is not None:
            result["onSubmitted"] = self._register_action(
                self.onSubmitted, "ValueChanged<String>"
            )._flut_pack()
        if self.enabled is not None:
            result["enabled"] = _flut_pack_value(self.enabled)
        if self.cursorHeight is not None:
            result["cursorHeight"] = _flut_pack_value(self.cursorHeight)
        if self.cursorColor is not None:
            result["cursorColor"] = _flut_pack_value(self.cursorColor)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "GestureTapCallback"
            )._flut_pack()
        if self.onTapOutside is not None:
            result["onTapOutside"] = self._register_action(
                self.onTapOutside, "TapRegionCallback"
            )._flut_pack()
        if self.onTapUpOutside is not None:
            result["onTapUpOutside"] = self._register_action(
                self.onTapUpOutside, "TapRegionUpCallback"
            )._flut_pack()
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        return result
