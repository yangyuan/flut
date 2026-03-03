from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Offset

from typing import Optional, override


class TapDownDetails(FlutValueObject):
    _flut_type = "TapDownDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=None,
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "TapDownDetails":
        return TapDownDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            kind=_flut_unpack_optional_field(data, "kind"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        if self.kind is not None:
            result["kind"] = _flut_pack_value(self.kind)
        return result


class TapUpDetails(FlutValueObject):
    _flut_type = "TapUpDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=Offset(),
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "TapUpDetails":
        return TapUpDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
            kind=_flut_unpack_required_field(data, "kind"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        result["kind"] = _flut_pack_value(self.kind)
        return result
