from typing import override

from flut._flut.engine import FlutValueObject
from flut._flut.runtime import _flut_unpack_required_field


class _InputBorder(FlutValueObject):
    _flut_type = "InputBorder"

    def __init__(self):
        super().__init__()


class _InputBorderNone(_InputBorder):
    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = "none"
        return result


class InputBorder(_InputBorder):
    none = _InputBorderNone()

    @staticmethod
    def _flut_unpack(data: dict) -> "InputBorder":
        value = _flut_unpack_required_field(data, "value")
        if value == "none":
            return InputBorder.none
        raise ValueError(f"Unknown InputBorder value: {value}")
