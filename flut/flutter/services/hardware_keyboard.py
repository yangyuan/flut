from typing import Optional, Set, override

from flut._flut.engine import (
    FlutValueObject,
    FlutRealtimeObject,
    FlutSingletonInstance,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.core import Duration

from .keyboard_key import (
    LogicalKeyboardKey,
    PhysicalKeyboardKey,
)


class KeyEvent(FlutValueObject):
    _flut_type = "KeyEvent"

    def __init__(
        self,
        physicalKey: PhysicalKeyboardKey,
        logicalKey: LogicalKeyboardKey,
        timeStamp: Duration,
        character: Optional[str] = None,
        synthesized: bool = False,
    ):
        super().__init__()
        self.physicalKey = physicalKey
        self.logicalKey = logicalKey
        self.timeStamp = timeStamp
        self.character = character
        self.synthesized = synthesized

    @staticmethod
    def _flut_unpack(data: dict) -> "KeyEvent":
        return KeyEvent(
            physicalKey=_flut_unpack_required_field(data, "physicalKey"),
            logicalKey=_flut_unpack_required_field(data, "logicalKey"),
            timeStamp=_flut_unpack_required_field(data, "timeStamp"),
            character=_flut_unpack_optional_field(data, "character"),
            synthesized=_flut_unpack_required_field(data, "synthesized"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["physicalKey"] = _flut_pack_value(self.physicalKey)
        result["logicalKey"] = _flut_pack_value(self.logicalKey)
        result["timeStamp"] = _flut_pack_value(self.timeStamp)
        if self.character is not None:
            result["character"] = _flut_pack_value(self.character)
        result["synthesized"] = _flut_pack_value(self.synthesized)
        return result


class KeyDownEvent(KeyEvent):
    _flut_type = "KeyDownEvent"

    def __init__(
        self,
        physicalKey: PhysicalKeyboardKey,
        logicalKey: LogicalKeyboardKey,
        timeStamp: Duration,
        character: Optional[str] = None,
        synthesized: bool = False,
    ):
        super().__init__(
            physicalKey=physicalKey,
            logicalKey=logicalKey,
            timeStamp=timeStamp,
            character=character,
            synthesized=synthesized,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "KeyDownEvent":
        return KeyDownEvent(
            physicalKey=_flut_unpack_required_field(data, "physicalKey"),
            logicalKey=_flut_unpack_required_field(data, "logicalKey"),
            timeStamp=_flut_unpack_required_field(data, "timeStamp"),
            character=_flut_unpack_optional_field(data, "character"),
            synthesized=_flut_unpack_required_field(data, "synthesized"),
        )


class KeyUpEvent(KeyEvent):
    _flut_type = "KeyUpEvent"

    def __init__(
        self,
        physicalKey: PhysicalKeyboardKey,
        logicalKey: LogicalKeyboardKey,
        timeStamp: Duration,
        synthesized: bool = False,
    ):
        super().__init__(
            physicalKey=physicalKey,
            logicalKey=logicalKey,
            timeStamp=timeStamp,
            synthesized=synthesized,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "KeyUpEvent":
        return KeyUpEvent(
            physicalKey=_flut_unpack_required_field(data, "physicalKey"),
            logicalKey=_flut_unpack_required_field(data, "logicalKey"),
            timeStamp=_flut_unpack_required_field(data, "timeStamp"),
            synthesized=_flut_unpack_required_field(data, "synthesized"),
        )


class KeyRepeatEvent(KeyEvent):
    _flut_type = "KeyRepeatEvent"

    def __init__(
        self,
        physicalKey: PhysicalKeyboardKey,
        logicalKey: LogicalKeyboardKey,
        timeStamp: Duration,
        character: Optional[str] = None,
    ):
        super().__init__(
            physicalKey=physicalKey,
            logicalKey=logicalKey,
            timeStamp=timeStamp,
            character=character,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "KeyRepeatEvent":
        return KeyRepeatEvent(
            physicalKey=_flut_unpack_required_field(data, "physicalKey"),
            logicalKey=_flut_unpack_required_field(data, "logicalKey"),
            timeStamp=_flut_unpack_required_field(data, "timeStamp"),
            character=_flut_unpack_optional_field(data, "character"),
        )


class HardwareKeyboard(FlutRealtimeObject):
    _flut_type = "HardwareKeyboard"

    instance: "HardwareKeyboard" = FlutSingletonInstance()

    @property
    def physicalKeysPressed(self) -> Set[PhysicalKeyboardKey]:
        result = self._flut_get("physicalKeysPressed")
        if result is None:
            return set()
        return {PhysicalKeyboardKey(usage) for usage in result}

    @property
    def logicalKeysPressed(self) -> Set[LogicalKeyboardKey]:
        result = self._flut_get("logicalKeysPressed")
        if result is None:
            return set()
        return {LogicalKeyboardKey(kid) for kid in result}

    def isPhysicalKeyPressed(self, key: PhysicalKeyboardKey) -> bool:
        return bool(self._flut_call("isPhysicalKeyPressed", key._flut_pack()))

    def isLogicalKeyPressed(self, key: LogicalKeyboardKey) -> bool:
        return bool(self._flut_call("isLogicalKeyPressed", key._flut_pack()))

    @property
    def isShiftPressed(self) -> bool:
        return self._flut_get("isShiftPressed")

    @property
    def isControlPressed(self) -> bool:
        return self._flut_get("isControlPressed")

    @property
    def isAltPressed(self) -> bool:
        return self._flut_get("isAltPressed")

    @property
    def isMetaPressed(self) -> bool:
        return self._flut_get("isMetaPressed")
