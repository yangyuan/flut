from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field


class DeviceGestureSettings(FlutValueObject):
    _flut_type = "DeviceGestureSettings"

    def __init__(self, *, touchSlop: Optional[float] = None):
        super().__init__()
        self.touchSlop = touchSlop

    @property
    def panSlop(self) -> Optional[float]:
        return self.touchSlop * 2.0 if self.touchSlop is not None else None

    @staticmethod
    def _flut_unpack(data: dict) -> "DeviceGestureSettings":
        return DeviceGestureSettings(
            touchSlop=_flut_unpack_optional_field(data, "touchSlop"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.touchSlop is not None:
            result["touchSlop"] = _flut_pack_value(self.touchSlop)
        return result
