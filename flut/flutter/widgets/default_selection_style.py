from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.services.mouse_cursor import MouseCursor
from flut.flutter.widgets.framework import Widget


class DefaultSelectionStyle(Widget):
    _flut_type = "DefaultSelectionStyle"

    defaultColor: Color = Color(0x80808080)

    def __init__(
        self,
        *,
        cursorColor: Optional[Color] = None,
        selectionColor: Optional[Color] = None,
        mouseCursor: Optional[MouseCursor] = None,
        child: Widget,
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.cursorColor = cursorColor
        self.selectionColor = selectionColor
        self.mouseCursor = mouseCursor
        self.child = child

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self.cursorColor is not None:
            result["cursorColor"] = _flut_pack_value(self.cursorColor)
        if self.selectionColor is not None:
            result["selectionColor"] = _flut_pack_value(self.selectionColor)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        result["child"] = _flut_pack_value(self.child)
        return result
