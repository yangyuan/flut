from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import TextAffinity


class TextSelection(FlutValueObject):
    _flut_type = "TextSelection"

    def __init__(
        self,
        *,
        baseOffset: int,
        extentOffset: int,
        affinity: TextAffinity = TextAffinity.downstream,
        isDirectional: bool = False,
    ) -> None:
        super().__init__()
        self.baseOffset = baseOffset
        self.extentOffset = extentOffset
        self.affinity = affinity
        self.isDirectional = isDirectional

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSelection":
        return TextSelection(
            baseOffset=_flut_unpack_required_field(data, "baseOffset"),
            extentOffset=_flut_unpack_required_field(data, "extentOffset"),
            affinity=_flut_unpack_required_field(data, "affinity"),
            isDirectional=_flut_unpack_required_field(data, "isDirectional"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["baseOffset"] = _flut_pack_value(self.baseOffset)
        result["extentOffset"] = _flut_pack_value(self.extentOffset)
        result["affinity"] = _flut_pack_value(self.affinity)
        result["isDirectional"] = _flut_pack_value(self.isDirectional)
        return result
