from typing import override

from flut._flut.engine import _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.flutter.painting.borders import BorderSide, OutlinedBorder


class CircleBorder(OutlinedBorder):
    _flut_type = "CircleBorder"

    def __init__(
        self,
        *,
        side: BorderSide = BorderSide.none,
        eccentricity: float = 0.0,
    ):
        super().__init__()
        self.side = side
        self.eccentricity = eccentricity

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["side"] = _flut_pack_value(self.side)
        result["eccentricity"] = _flut_pack_value(self.eccentricity)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "CircleBorder":
        return CircleBorder(
            side=_flut_unpack_required_field(data, "side"),
            eccentricity=_flut_unpack_required_field(data, "eccentricity"),
        )
