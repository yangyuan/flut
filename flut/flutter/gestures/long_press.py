from flut._flut.engine import FlutRealtimeObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.core import Duration
from flut.dart.ui import Offset
from flut.flutter.gestures.recognizer import GestureRecognizer
from flut.flutter.gestures.velocity_tracker import Velocity

from typing import Callable, Optional, override


class LongPressDownDetails(FlutValueObject):
    _flut_type = "LongPressDownDetails"

    def __init__(
        self,
        *,
        globalPosition: Offset = Offset.zero,
        localPosition: Offset | None = None,
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "LongPressDownDetails":
        return LongPressDownDetails(
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


class LongPressGestureRecognizer(GestureRecognizer, FlutRealtimeObject):
    _flut_type = "LongPressGestureRecognizer"

    def __init__(
        self,
        *,
        duration: Optional[Duration] = None,
        debugOwner: Optional[object] = None,
        supportedDevices: Optional[set] = None,
        allowedButtonsFilter: Optional[Callable[[int], bool]] = None,
        postAcceptSlopTolerance: Optional[float] = None,
    ) -> None:
        FlutRealtimeObject.__init__(self)
        props: dict = {}
        if duration is not None:
            props["duration"] = _flut_pack_value(duration)
        if debugOwner is not None:
            props["debugOwner"] = _flut_pack_value(debugOwner)
        if supportedDevices is not None:
            props["supportedDevices"] = _flut_pack_value(list(supportedDevices))
        if postAcceptSlopTolerance is not None:
            props["postAcceptSlopTolerance"] = _flut_pack_value(postAcceptSlopTolerance)
        bindings: list = []
        if allowedButtonsFilter is not None:
            bindings.append(
                ("allowedButtonsFilter", allowedButtonsFilter, "AllowedButtonsFilter")
            )
        self._flut_create(props=props or None, bindings=bindings or None)

    @property
    def onLongPressDown(self) -> Optional[Callable[["LongPressDownDetails"], None]]:
        return self._flut_get("onLongPressDown")

    @onLongPressDown.setter
    def onLongPressDown(
        self, value: Optional[Callable[["LongPressDownDetails"], None]]
    ) -> None:
        self._flut_set("onLongPressDown", value, "GestureLongPressDownCallback")

    @property
    def onLongPressCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onLongPressCancel")

    @onLongPressCancel.setter
    def onLongPressCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onLongPressCancel", value, "GestureLongPressCancelCallback")

    @property
    def onLongPress(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onLongPress")

    @onLongPress.setter
    def onLongPress(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onLongPress", value, "GestureLongPressCallback")

    @property
    def onLongPressStart(self) -> Optional[Callable[["LongPressStartDetails"], None]]:
        return self._flut_get("onLongPressStart")

    @onLongPressStart.setter
    def onLongPressStart(
        self, value: Optional[Callable[["LongPressStartDetails"], None]]
    ) -> None:
        self._flut_set("onLongPressStart", value, "GestureLongPressStartCallback")

    @property
    def onLongPressMoveUpdate(
        self,
    ) -> Optional[Callable[["LongPressMoveUpdateDetails"], None]]:
        return self._flut_get("onLongPressMoveUpdate")

    @onLongPressMoveUpdate.setter
    def onLongPressMoveUpdate(
        self, value: Optional[Callable[["LongPressMoveUpdateDetails"], None]]
    ) -> None:
        self._flut_set(
            "onLongPressMoveUpdate", value, "GestureLongPressMoveUpdateCallback"
        )

    @property
    def onLongPressUp(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onLongPressUp")

    @onLongPressUp.setter
    def onLongPressUp(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onLongPressUp", value, "GestureLongPressUpCallback")

    @property
    def onLongPressEnd(self) -> Optional[Callable[["LongPressEndDetails"], None]]:
        return self._flut_get("onLongPressEnd")

    @onLongPressEnd.setter
    def onLongPressEnd(
        self, value: Optional[Callable[["LongPressEndDetails"], None]]
    ) -> None:
        self._flut_set("onLongPressEnd", value, "GestureLongPressEndCallback")

    @property
    def onSecondaryLongPressDown(
        self,
    ) -> Optional[Callable[["LongPressDownDetails"], None]]:
        return self._flut_get("onSecondaryLongPressDown")

    @onSecondaryLongPressDown.setter
    def onSecondaryLongPressDown(
        self, value: Optional[Callable[["LongPressDownDetails"], None]]
    ) -> None:
        self._flut_set(
            "onSecondaryLongPressDown", value, "GestureLongPressDownCallback"
        )

    @property
    def onSecondaryLongPressCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onSecondaryLongPressCancel")

    @onSecondaryLongPressCancel.setter
    def onSecondaryLongPressCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set(
            "onSecondaryLongPressCancel", value, "GestureLongPressCancelCallback"
        )

    @property
    def onSecondaryLongPress(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onSecondaryLongPress")

    @onSecondaryLongPress.setter
    def onSecondaryLongPress(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onSecondaryLongPress", value, "GestureLongPressCallback")

    @property
    def onSecondaryLongPressStart(
        self,
    ) -> Optional[Callable[["LongPressStartDetails"], None]]:
        return self._flut_get("onSecondaryLongPressStart")

    @onSecondaryLongPressStart.setter
    def onSecondaryLongPressStart(
        self, value: Optional[Callable[["LongPressStartDetails"], None]]
    ) -> None:
        self._flut_set(
            "onSecondaryLongPressStart", value, "GestureLongPressStartCallback"
        )

    @property
    def onSecondaryLongPressMoveUpdate(
        self,
    ) -> Optional[Callable[["LongPressMoveUpdateDetails"], None]]:
        return self._flut_get("onSecondaryLongPressMoveUpdate")

    @onSecondaryLongPressMoveUpdate.setter
    def onSecondaryLongPressMoveUpdate(
        self, value: Optional[Callable[["LongPressMoveUpdateDetails"], None]]
    ) -> None:
        self._flut_set(
            "onSecondaryLongPressMoveUpdate",
            value,
            "GestureLongPressMoveUpdateCallback",
        )

    @property
    def onSecondaryLongPressUp(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onSecondaryLongPressUp")

    @onSecondaryLongPressUp.setter
    def onSecondaryLongPressUp(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onSecondaryLongPressUp", value, "GestureLongPressUpCallback")

    @property
    def onSecondaryLongPressEnd(
        self,
    ) -> Optional[Callable[["LongPressEndDetails"], None]]:
        return self._flut_get("onSecondaryLongPressEnd")

    @onSecondaryLongPressEnd.setter
    def onSecondaryLongPressEnd(
        self, value: Optional[Callable[["LongPressEndDetails"], None]]
    ) -> None:
        self._flut_set("onSecondaryLongPressEnd", value, "GestureLongPressEndCallback")

    @property
    def onTertiaryLongPressDown(
        self,
    ) -> Optional[Callable[["LongPressDownDetails"], None]]:
        return self._flut_get("onTertiaryLongPressDown")

    @onTertiaryLongPressDown.setter
    def onTertiaryLongPressDown(
        self, value: Optional[Callable[["LongPressDownDetails"], None]]
    ) -> None:
        self._flut_set("onTertiaryLongPressDown", value, "GestureLongPressDownCallback")

    @property
    def onTertiaryLongPressCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTertiaryLongPressCancel")

    @onTertiaryLongPressCancel.setter
    def onTertiaryLongPressCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set(
            "onTertiaryLongPressCancel", value, "GestureLongPressCancelCallback"
        )

    @property
    def onTertiaryLongPress(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTertiaryLongPress")

    @onTertiaryLongPress.setter
    def onTertiaryLongPress(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onTertiaryLongPress", value, "GestureLongPressCallback")

    @property
    def onTertiaryLongPressStart(
        self,
    ) -> Optional[Callable[["LongPressStartDetails"], None]]:
        return self._flut_get("onTertiaryLongPressStart")

    @onTertiaryLongPressStart.setter
    def onTertiaryLongPressStart(
        self, value: Optional[Callable[["LongPressStartDetails"], None]]
    ) -> None:
        self._flut_set(
            "onTertiaryLongPressStart", value, "GestureLongPressStartCallback"
        )

    @property
    def onTertiaryLongPressMoveUpdate(
        self,
    ) -> Optional[Callable[["LongPressMoveUpdateDetails"], None]]:
        return self._flut_get("onTertiaryLongPressMoveUpdate")

    @onTertiaryLongPressMoveUpdate.setter
    def onTertiaryLongPressMoveUpdate(
        self, value: Optional[Callable[["LongPressMoveUpdateDetails"], None]]
    ) -> None:
        self._flut_set(
            "onTertiaryLongPressMoveUpdate",
            value,
            "GestureLongPressMoveUpdateCallback",
        )

    @property
    def onTertiaryLongPressUp(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTertiaryLongPressUp")

    @onTertiaryLongPressUp.setter
    def onTertiaryLongPressUp(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onTertiaryLongPressUp", value, "GestureLongPressUpCallback")

    @property
    def onTertiaryLongPressEnd(
        self,
    ) -> Optional[Callable[["LongPressEndDetails"], None]]:
        return self._flut_get("onTertiaryLongPressEnd")

    @onTertiaryLongPressEnd.setter
    def onTertiaryLongPressEnd(
        self, value: Optional[Callable[["LongPressEndDetails"], None]]
    ) -> None:
        self._flut_set("onTertiaryLongPressEnd", value, "GestureLongPressEndCallback")
