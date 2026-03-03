from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import TextAlign
from flut.flutter.widgets.framework import Widget
from flut.flutter.widgets.form import AutovalidateMode


class TextFormField(Widget):
    _flut_type = "TextFormField"

    def __init__(
        self,
        *,
        key=None,
        controller=None,
        initialValue: Optional[str] = None,
        focusNode=None,
        decoration=None,
        style=None,
        textAlign: TextAlign = TextAlign.start,
        autofocus: bool = False,
        readOnly: bool = False,
        obscureText: bool = False,
        maxLines: Optional[int] = 1,
        minLines: Optional[int] = None,
        maxLength: Optional[int] = None,
        onChanged: Optional[Callable[[str], None]] = None,
        onFieldSubmitted: Optional[Callable[[str], None]] = None,
        onSaved: Optional[Callable[[Optional[str]], None]] = None,
        validator: Optional[Callable[[Optional[str]], Optional[str]]] = None,
        enabled: Optional[bool] = None,
        autovalidateMode: Optional[AutovalidateMode] = None,
    ):
        super().__init__(key=key)
        self.controller = controller
        self.initialValue = initialValue
        self.focusNode = focusNode
        self.decoration = decoration
        self.style = style
        self.textAlign = textAlign
        self.autofocus = autofocus
        self.readOnly = readOnly
        self.obscureText = obscureText
        self.maxLines = maxLines
        self.minLines = minLines
        self.maxLength = maxLength
        self.onChanged = onChanged
        self.onFieldSubmitted = onFieldSubmitted
        self.onSaved = onSaved
        self.validator = validator
        self.enabled = enabled
        self.autovalidateMode = autovalidateMode

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["autofocus"] = _flut_pack_value(self.autofocus)
        result["readOnly"] = _flut_pack_value(self.readOnly)
        result["obscureText"] = _flut_pack_value(self.obscureText)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.initialValue is not None:
            result["initialValue"] = _flut_pack_value(self.initialValue)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        result["textAlign"] = _flut_pack_value(self.textAlign)
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
        if self.onFieldSubmitted is not None:
            result["onFieldSubmitted"] = self._register_action(
                self.onFieldSubmitted, "ValueChanged<String>"
            )._flut_pack()
        if self.onSaved is not None:
            result["onSaved"] = self._register_action(
                self.onSaved, "FormFieldSetter"
            )._flut_pack()
        if self.validator is not None:
            result["validator"] = self._register_action(
                self.validator, "FormFieldValidator"
            )._flut_pack()
        if self.enabled is not None:
            result["enabled"] = _flut_pack_value(self.enabled)
        if self.autovalidateMode is not None:
            result["autovalidateMode"] = _flut_pack_value(self.autovalidateMode)
        return result
