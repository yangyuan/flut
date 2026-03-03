from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.dart.ui import BlurStyle, Color, Offset, Shadow


class BoxShadow(Shadow):
    _flut_type = "BoxShadow"

    def __init__(
        self,
        *,
        color: Color = Color(0xFF000000),
        offset: Offset = Offset(0, 0),
        blurRadius: float = 0.0,
        spreadRadius: float = 0.0,
        blurStyle: BlurStyle = BlurStyle.normal,
    ):
        super().__init__()
        self.color = color
        self.offset = offset
        self.blurRadius = blurRadius
        self.spreadRadius = spreadRadius
        self.blurStyle = blurStyle

    @staticmethod
    def _flut_unpack(data: dict) -> "BoxShadow":
        return BoxShadow(
            color=_flut_unpack_required_field(data, "color"),
            offset=_flut_unpack_required_field(data, "offset"),
            blurRadius=_flut_unpack_required_field(data, "blurRadius"),
            spreadRadius=_flut_unpack_required_field(data, "spreadRadius"),
            blurStyle=_flut_unpack_required_field(data, "blurStyle"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["color"] = _flut_pack_value(self.color)
        result["offset"] = _flut_pack_value(self.offset)
        result["blurRadius"] = _flut_pack_value(self.blurRadius)
        result["spreadRadius"] = _flut_pack_value(self.spreadRadius)
        result["blurStyle"] = _flut_pack_value(self.blurStyle)
        return result
