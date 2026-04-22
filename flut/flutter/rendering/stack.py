from typing import override

from flut._flut.engine import (
    FlutEnumObject,
    FlutValueObject,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_required_field


class StackFit(FlutEnumObject):
    loose: "StackFit"
    expand: "StackFit"
    passthrough: "StackFit"


class _RelativeRect(FlutValueObject):
    _flut_type = "RelativeRect"

    def __init__(self, left: float, top: float, right: float, bottom: float):
        super().__init__()
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @staticmethod
    def fromLTRB(
        left: float, top: float, right: float, bottom: float
    ) -> "RelativeRect":
        return _RelativeRect(left, top, right, bottom)

    @staticmethod
    def fromRect(rect, container) -> "RelativeRect":
        return _RelativeRect(
            rect.left - container.left,
            rect.top - container.top,
            container.right - rect.right,
            container.bottom - rect.bottom,
        )

    @staticmethod
    def fromSize(rect, container) -> "RelativeRect":
        return _RelativeRect(
            rect.left,
            rect.top,
            container.width - rect.right,
            container.height - rect.bottom,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "_RelativeRect":
        return _RelativeRect(
            left=_flut_unpack_required_field(data, "left"),
            top=_flut_unpack_required_field(data, "top"),
            right=_flut_unpack_required_field(data, "right"),
            bottom=_flut_unpack_required_field(data, "bottom"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["left"] = _flut_pack_value(self.left)
        result["top"] = _flut_pack_value(self.top)
        result["right"] = _flut_pack_value(self.right)
        result["bottom"] = _flut_pack_value(self.bottom)
        return result

    def __eq__(self, other):
        if isinstance(other, _RelativeRect):
            return (
                self.left == other.left
                and self.top == other.top
                and self.right == other.right
                and self.bottom == other.bottom
            )
        return False

    def __hash__(self):
        return hash((self.left, self.top, self.right, self.bottom))


class RelativeRect(_RelativeRect):
    fill = _RelativeRect(0.0, 0.0, 0.0, 0.0)
