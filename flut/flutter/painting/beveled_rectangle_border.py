from typing import override

from flut._flut.engine import _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.flutter.painting.borders import BorderSide, OutlinedBorder
from flut.flutter.painting.border_radius import BorderRadius


class BeveledRectangleBorder(OutlinedBorder):
    _flut_type = "BeveledRectangleBorder"

    def __init__(
        self,
        *,
        side: BorderSide = BorderSide.none,
        borderRadius: BorderRadius = BorderRadius.zero,
    ):
        super().__init__()
        self.side = side
        self.borderRadius = borderRadius

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["side"] = _flut_pack_value(self.side)
        result["borderRadius"] = _flut_pack_value(self.borderRadius)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "BeveledRectangleBorder":
        return BeveledRectangleBorder(
            side=_flut_unpack_required_field(data, "side"),
            borderRadius=_flut_unpack_required_field(data, "borderRadius"),
        )
