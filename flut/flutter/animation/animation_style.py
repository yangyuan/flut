from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field
from flut.dart.core import Duration
from .curves import Curve


class _AnimationStyle(FlutValueObject):
    _flut_type = "AnimationStyle"

    def __init__(
        self,
        *,
        curve: Optional[Curve] = None,
        duration: Optional[Duration] = None,
        reverseCurve: Optional[Curve] = None,
        reverseDuration: Optional[Duration] = None,
    ):
        super().__init__()
        self.curve = curve
        self.duration = duration
        self.reverseCurve = reverseCurve
        self.reverseDuration = reverseDuration

    @staticmethod
    def _flut_unpack(data: dict) -> "_AnimationStyle":
        return _AnimationStyle(
            curve=_flut_unpack_optional_field(data, "curve"),
            duration=_flut_unpack_optional_field(data, "duration"),
            reverseCurve=_flut_unpack_optional_field(data, "reverseCurve"),
            reverseDuration=_flut_unpack_optional_field(data, "reverseDuration"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.curve is not None:
            result["curve"] = _flut_pack_value(self.curve)
        if self.duration is not None:
            result["duration"] = _flut_pack_value(self.duration)
        if self.reverseCurve is not None:
            result["reverseCurve"] = _flut_pack_value(self.reverseCurve)
        if self.reverseDuration is not None:
            result["reverseDuration"] = _flut_pack_value(self.reverseDuration)
        return result


class AnimationStyle(_AnimationStyle):
    noAnimation = _AnimationStyle(
        duration=Duration.zero,
        reverseDuration=Duration.zero,
    )
