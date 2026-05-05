from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class TextSelectionToolbar(Widget):
    _flut_type = "TextSelectionToolbar"

    def __init__(
        self,
        *,
        anchorAbove: "Offset",
        anchorBelow: "Offset",
        children: list[Widget],
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.anchorAbove = anchorAbove
        self.anchorBelow = anchorBelow
        self.children = children

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["anchorAbove"] = _flut_pack_value(self.anchorAbove)
        result["anchorBelow"] = _flut_pack_value(self.anchorBelow)
        result["children"] = _flut_pack_value(self.children)
        return result
