from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.dart.ui import Offset


class PointerEvent(FlutValueObject):
    _flut_type = "PointerEvent"

    def __init__(
        self,
        *,
        position=Offset(0, 0),
        localPosition=None,
        delta=Offset(0, 0),
        localDelta=None,
        buttons: int = 0,
        down: bool = False,
        pointer: int = 0,
        device: int = 0,
    ):
        super().__init__()
        self.position = position
        self.localPosition = localPosition
        self.delta = delta
        self.localDelta = localDelta
        self.buttons = buttons
        self.down = down
        self.pointer = pointer
        self.device = device

    @staticmethod
    def _flut_unpack(data: dict) -> "PointerEvent":
        return PointerEvent(
            position=_flut_unpack_required_field(data, "position"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            delta=_flut_unpack_required_field(data, "delta"),
            localDelta=_flut_unpack_optional_field(data, "localDelta"),
            buttons=_flut_unpack_required_field(data, "buttons"),
            down=_flut_unpack_required_field(data, "down"),
            pointer=_flut_unpack_required_field(data, "pointer"),
            device=_flut_unpack_required_field(data, "device"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["position"] = _flut_pack_value(self.position)
        result["delta"] = _flut_pack_value(self.delta)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        if self.localDelta is not None:
            result["localDelta"] = _flut_pack_value(self.localDelta)
        result["buttons"] = _flut_pack_value(self.buttons)
        result["down"] = _flut_pack_value(self.down)
        result["pointer"] = _flut_pack_value(self.pointer)
        result["device"] = _flut_pack_value(self.device)
        return result


class PointerEnterEvent(PointerEvent):
    _flut_type = "PointerEnterEvent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def _flut_unpack(data: dict) -> "PointerEnterEvent":
        return PointerEnterEvent(
            position=_flut_unpack_required_field(data, "position"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            delta=_flut_unpack_required_field(data, "delta"),
            localDelta=_flut_unpack_optional_field(data, "localDelta"),
            buttons=_flut_unpack_required_field(data, "buttons"),
            down=_flut_unpack_required_field(data, "down"),
            pointer=_flut_unpack_required_field(data, "pointer"),
            device=_flut_unpack_required_field(data, "device"),
        )


class PointerExitEvent(PointerEvent):
    _flut_type = "PointerExitEvent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def _flut_unpack(data: dict) -> "PointerExitEvent":
        return PointerExitEvent(
            position=_flut_unpack_required_field(data, "position"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
            delta=_flut_unpack_required_field(data, "delta"),
            localDelta=_flut_unpack_optional_field(data, "localDelta"),
            buttons=_flut_unpack_required_field(data, "buttons"),
            down=_flut_unpack_required_field(data, "down"),
            pointer=_flut_unpack_required_field(data, "pointer"),
            device=_flut_unpack_required_field(data, "device"),
        )
