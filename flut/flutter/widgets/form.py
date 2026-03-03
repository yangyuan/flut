from typing import Callable, Optional, override

from flut._flut.engine import (
    FlutEnumObject,
    FlutRealtimeObject,
    call_dart_static,
    _flut_pack_value,
)
from flut.flutter.widgets.framework import Widget


class AutovalidateMode(FlutEnumObject):
    disabled: "AutovalidateMode"
    always: "AutovalidateMode"
    onUserInteraction: "AutovalidateMode"
    onUnfocus: "AutovalidateMode"
    onUserInteractionIfError: "AutovalidateMode"


class FormState(FlutRealtimeObject):
    _flut_type = "FormState"

    def validate(self) -> bool:
        return bool(self._flut_call("validate"))

    def validateGranularly(self):
        return self._flut_call("validateGranularly")

    def save(self):
        self._flut_call("save")

    def reset(self):
        self._flut_call("reset")


class Form(Widget):
    _flut_type = "Form"

    def __init__(
        self,
        *,
        key=None,
        onChanged: Optional[Callable[[], None]] = None,
        autovalidateMode: Optional[AutovalidateMode] = None,
        child: Widget,
    ):
        super().__init__(key=key)
        self.onChanged = onChanged
        self.autovalidateMode = autovalidateMode
        self.child = child

    @staticmethod
    def of(context) -> FormState:
        return call_dart_static("Form", "of", context._flut_pack())

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["child"] = _flut_pack_value(self.child)
        if self.onChanged is not None:
            result["onChanged"] = self._register_action(
                self.onChanged, "VoidCallback"
            )._flut_pack()
        if self.autovalidateMode is not None:
            result["autovalidateMode"] = _flut_pack_value(self.autovalidateMode)
        return result


class FormFieldState(FlutRealtimeObject):
    _flut_type = "FormFieldState"

    @property
    def value(self):
        return self._flut_get("value")

    @property
    def hasError(self) -> bool:
        return bool(self._flut_get("hasError"))

    @property
    def errorText(self):
        return self._flut_get("errorText")

    @property
    def isValid(self) -> bool:
        return bool(self._flut_get("isValid"))

    @property
    def hasInteractedByUser(self) -> bool:
        return bool(self._flut_get("hasInteractedByUser"))

    def validate(self) -> bool:
        return bool(self._flut_call("validate"))

    def save(self):
        self._flut_call("save")

    def reset(self):
        self._flut_call("reset")

    def didChange(self, value):
        self._flut_call("didChange", _flut_pack_value(value))

    def setValue(self, value):
        self._flut_call("setValue", _flut_pack_value(value))
