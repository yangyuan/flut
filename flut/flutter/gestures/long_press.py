from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Offset
from flut.flutter.gestures.velocity_tracker import Velocity

from typing import override


class LongPressStartDetails(FlutValueObject):
    _flut_type = "LongPressStartDetails"

    def __init__(
        self,
        *,
        globalPosition: Offset = Offset.zero,
        localPosition: Offset = Offset.zero,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition

    @staticmethod
    def _flut_unpack(data: dict) -> "LongPressStartDetails":
        return LongPressStartDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        return result


class LongPressMoveUpdateDetails(FlutValueObject):
    _flut_type = "LongPressMoveUpdateDetails"

    def __init__(
        self,
        *,
        globalPosition: Offset = Offset.zero,
        localPosition: Offset = Offset.zero,
        offsetFromOrigin: Offset = Offset.zero,
        localOffsetFromOrigin: Offset = Offset.zero,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.offsetFromOrigin = offsetFromOrigin
        self.localOffsetFromOrigin = localOffsetFromOrigin

    @staticmethod
    def _flut_unpack(data: dict) -> "LongPressMoveUpdateDetails":
        return LongPressMoveUpdateDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
            offsetFromOrigin=_flut_unpack_required_field(data, "offsetFromOrigin"),
            localOffsetFromOrigin=_flut_unpack_required_field(
                data, "localOffsetFromOrigin"
            ),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        result["offsetFromOrigin"] = _flut_pack_value(self.offsetFromOrigin)
        result["localOffsetFromOrigin"] = _flut_pack_value(self.localOffsetFromOrigin)
        return result


class LongPressEndDetails(FlutValueObject):
    _flut_type = "LongPressEndDetails"

    def __init__(
        self,
        *,
        globalPosition: Offset = Offset.zero,
        localPosition: Offset = Offset.zero,
        velocity: Velocity = Velocity.zero,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.velocity = velocity

    @staticmethod
    def _flut_unpack(data: dict) -> "LongPressEndDetails":
        return LongPressEndDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
            velocity=_flut_unpack_required_field(data, "velocity"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        result["velocity"] = _flut_pack_value(self.velocity)
        return result
