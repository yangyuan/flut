from typing import override

from flut._flut.engine import _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.flutter.painting.borders import BorderSide, OutlinedBorder


class StadiumBorder(OutlinedBorder):
    _flut_type = "StadiumBorder"

    def __init__(
        self,
        *,
        side: BorderSide = BorderSide.none,
    ):
        super().__init__()
        self.side = side

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["side"] = _flut_pack_value(self.side)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "StadiumBorder":
        return StadiumBorder(
            side=_flut_unpack_required_field(data, "side"),
        )
