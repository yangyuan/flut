from typing import Optional, override

from flut._flut.engine import (
    FlutValueObject,
    call_dart_static,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field
from flut.dart.ui import Color
from flut.flutter.widgets.framework import Widget


class TextSelectionThemeData(FlutValueObject):
    _flut_type = "TextSelectionThemeData"

    def __init__(
        self,
        *,
        cursorColor: Optional[Color] = None,
        selectionColor: Optional[Color] = None,
        selectionHandleColor: Optional[Color] = None,
    ) -> None:
        super().__init__()
        self.cursorColor = cursorColor
        self.selectionColor = selectionColor
        self.selectionHandleColor = selectionHandleColor

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSelectionThemeData":
        return TextSelectionThemeData(
            cursorColor=_flut_unpack_optional_field(data, "cursorColor"),
            selectionColor=_flut_unpack_optional_field(data, "selectionColor"),
            selectionHandleColor=_flut_unpack_optional_field(
                data, "selectionHandleColor"
            ),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self.cursorColor is not None:
            result["cursorColor"] = _flut_pack_value(self.cursorColor)
        if self.selectionColor is not None:
            result["selectionColor"] = _flut_pack_value(self.selectionColor)
        if self.selectionHandleColor is not None:
            result["selectionHandleColor"] = _flut_pack_value(self.selectionHandleColor)
        return result


class TextSelectionTheme(Widget):
    _flut_type = "TextSelectionTheme"

    def __init__(
        self,
        *,
        data: TextSelectionThemeData,
        child: Widget,
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.data = data
        self.child = child

    @staticmethod
    def of(context: "BuildContext") -> TextSelectionThemeData:
        return call_dart_static("TextSelectionTheme", "of", context._flut_pack())

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["data"] = _flut_pack_value(self.data)
        result["child"] = _flut_pack_value(self.child)
        return result
