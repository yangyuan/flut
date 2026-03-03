from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value, call_dart_static
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import PlaceholderAlignment, TextBaseline
from flut.flutter.widgets.framework import Widget
from flut.flutter.painting.text_style import TextStyle


class WidgetSpan(FlutValueObject):
    _flut_type = "WidgetSpan"

    def __init__(
        self,
        *,
        child: Widget,
        alignment: PlaceholderAlignment = PlaceholderAlignment.bottom,
        baseline: Optional[TextBaseline] = None,
        style: Optional[TextStyle] = None,
    ):
        super().__init__()
        self.child = child
        self.alignment = alignment
        self.baseline = baseline
        self.style = style

    @staticmethod
    def _flut_unpack(data: dict) -> "WidgetSpan":
        return WidgetSpan(
            child=_flut_unpack_required_field(data, "child"),
            alignment=_flut_unpack_required_field(data, "alignment"),
            baseline=_flut_unpack_optional_field(data, "baseline"),
            style=_flut_unpack_optional_field(data, "style"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["child"] = _flut_pack_value(self.child)
        result["alignment"] = _flut_pack_value(self.alignment)
        if self.baseline is not None:
            result["baseline"] = _flut_pack_value(self.baseline)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        return result

    @staticmethod
    def extractFromInlineSpan(span, textScaler):
        return call_dart_static(
            "WidgetSpan",
            "extractFromInlineSpan",
            span._flut_pack(),
            textScaler._flut_pack(),
        )
