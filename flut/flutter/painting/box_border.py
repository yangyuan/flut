from typing import override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Color
from flut.flutter.painting.borders import BorderSide, BorderStyle


class BoxShape(FlutEnumObject):
    rectangle: "BoxShape"
    circle: "BoxShape"


class Border(FlutValueObject):
    _flut_type = "Border"

    def __init__(
        self,
        *,
        top: BorderSide = BorderSide.none,
        right: BorderSide = BorderSide.none,
        bottom: BorderSide = BorderSide.none,
        left: BorderSide = BorderSide.none,
    ):
        super().__init__()
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    @staticmethod
    def all(
        *,
        width: float = 1.0,
        color: Color = Color(0xFF000000),
        style: BorderStyle = BorderStyle.solid,
        strokeAlign: float = -1.0,
    ):
        side = BorderSide(
            color=color, width=width, style=style, strokeAlign=strokeAlign
        )
        return Border(top=side, right=side, bottom=side, left=side)

    @staticmethod
    def fromBorderSide(side):
        return Border(top=side, right=side, bottom=side, left=side)

    @staticmethod
    def symmetric(
        *,
        vertical=BorderSide.none,
        horizontal=BorderSide.none,
    ):
        return Border(top=vertical, right=horizontal, bottom=vertical, left=horizontal)

    @staticmethod
    def _flut_unpack(data: dict) -> "Border":
        return Border(
            top=_flut_unpack_required_field(data, "top"),
            right=_flut_unpack_required_field(data, "right"),
            bottom=_flut_unpack_required_field(data, "bottom"),
            left=_flut_unpack_required_field(data, "left"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["top"] = _flut_pack_value(self.top)
        result["right"] = _flut_pack_value(self.right)
        result["bottom"] = _flut_pack_value(self.bottom)
        result["left"] = _flut_pack_value(self.left)
        return result
