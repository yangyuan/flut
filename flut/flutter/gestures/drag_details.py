from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Offset, PointerDeviceKind
from flut.flutter.gestures.velocity_tracker import Velocity

from typing import override


class DragStartDetails(FlutValueObject):
    _flut_type = "DragStartDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=None,
        sourceTimeStamp=None,
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.sourceTimeStamp = sourceTimeStamp
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "DragStartDetails":
        return DragStartDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            sourceTimeStamp=_flut_unpack_optional_field(data, "sourceTimeStamp"),
            kind=_flut_unpack_optional_field(data, "kind"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        if self.sourceTimeStamp is not None:
            result["sourceTimeStamp"] = _flut_pack_value(self.sourceTimeStamp)
        if self.kind is not None:
            result["kind"] = _flut_pack_value(self.kind)
        return result


class DragUpdateDetails(FlutValueObject):
    _flut_type = "DragUpdateDetails"

    def __init__(
        self,
        *,
        globalPosition,
        localPosition=None,
        sourceTimeStamp=None,
        delta=Offset(),
        primaryDelta=None,
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.sourceTimeStamp = sourceTimeStamp
        self.delta = delta
        self.primaryDelta = primaryDelta
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "DragUpdateDetails":
        return DragUpdateDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            sourceTimeStamp=_flut_unpack_optional_field(data, "sourceTimeStamp"),
            delta=_flut_unpack_required_field(data, "delta"),
            primaryDelta=_flut_unpack_optional_field(data, "primaryDelta"),
            kind=_flut_unpack_optional_field(data, "kind"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        if self.sourceTimeStamp is not None:
            result["sourceTimeStamp"] = _flut_pack_value(self.sourceTimeStamp)
        result["delta"] = _flut_pack_value(self.delta)
        if self.primaryDelta is not None:
            result["primaryDelta"] = _flut_pack_value(self.primaryDelta)
        if self.kind is not None:
            result["kind"] = _flut_pack_value(self.kind)
        return result


class DragDownDetails(FlutValueObject):
    _flut_type = "DragDownDetails"

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
    def _flut_unpack(data: dict) -> "DragDownDetails":
        return DragDownDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        return result


class DragEndDetails(FlutValueObject):
    _flut_type = "DragEndDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=None,
        velocity=Velocity.zero,
        primaryVelocity=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.velocity = velocity
        self.primaryVelocity = primaryVelocity

    @staticmethod
    def _flut_unpack(data: dict) -> "DragEndDetails":
        return DragEndDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            velocity=_flut_unpack_required_field(data, "velocity"),
            primaryVelocity=_flut_unpack_optional_field(data, "primaryVelocity"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        result["velocity"] = _flut_pack_value(self.velocity)
        if self.primaryVelocity is not None:
            result["primaryVelocity"] = _flut_pack_value(self.primaryVelocity)
        return result
