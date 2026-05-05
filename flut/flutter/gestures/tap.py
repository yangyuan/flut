from flut._flut.engine import FlutRealtimeObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Offset
from flut.flutter.gestures.recognizer import GestureRecognizer

from typing import Callable, Optional, override


class TapDownDetails(FlutValueObject):
    _flut_type = "TapDownDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=None,
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "TapDownDetails":
        return TapDownDetails(
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


class TapUpDetails(FlutValueObject):
    _flut_type = "TapUpDetails"

    def __init__(
        self,
        *,
        globalPosition=Offset(),
        localPosition=Offset(),
        kind=None,
    ):
        super().__init__()
        self.globalPosition = globalPosition
        self.localPosition = localPosition
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "TapUpDetails":
        return TapUpDetails(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            localPosition=_flut_unpack_required_field(data, "localPosition"),
            kind=_flut_unpack_required_field(data, "kind"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["localPosition"] = _flut_pack_value(self.localPosition)
        result["kind"] = _flut_pack_value(self.kind)
        return result


class TapMoveDetails(FlutValueObject):
    _flut_type = "TapMoveDetails"

    def __init__(
        self,
        *,
        kind,
        globalPosition=Offset(),
        delta=Offset(),
        localPosition=None,
    ):
        super().__init__()
        self.kind = kind
        self.globalPosition = globalPosition
        self.delta = delta
        self.localPosition = localPosition

    @staticmethod
    def _flut_unpack(data: dict) -> "TapMoveDetails":
        return TapMoveDetails(
            kind=_flut_unpack_required_field(data, "kind"),
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            delta=_flut_unpack_required_field(data, "delta"),
            localPosition=_flut_unpack_optional_field(data, "localPosition"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["kind"] = _flut_pack_value(self.kind)
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["delta"] = _flut_pack_value(self.delta)
        if self.localPosition is not None:
            result["localPosition"] = _flut_pack_value(self.localPosition)
        return result


def _default_button_accept_behavior(buttons: int) -> bool:
    return True


class TapGestureRecognizer(GestureRecognizer, FlutRealtimeObject):
    _flut_type = "TapGestureRecognizer"

    def __init__(
        self,
        *,
        debugOwner: Optional[object] = None,
        supportedDevices: Optional[set] = None,
        allowedButtonsFilter: Callable[[int], bool] = _default_button_accept_behavior,
        preAcceptSlopTolerance: Optional[float] = -1.0,
        postAcceptSlopTolerance: Optional[float] = -1.0,
    ) -> None:
        FlutRealtimeObject.__init__(self)
        props: dict = {}
        if debugOwner is not None:
            props["debugOwner"] = _flut_pack_value(debugOwner)
        if supportedDevices is not None:
            props["supportedDevices"] = _flut_pack_value(list(supportedDevices))
        if preAcceptSlopTolerance is not None:
            props["preAcceptSlopTolerance"] = _flut_pack_value(preAcceptSlopTolerance)
        if postAcceptSlopTolerance is not None:
            props["postAcceptSlopTolerance"] = _flut_pack_value(postAcceptSlopTolerance)
        bindings: list = [
            ("allowedButtonsFilter", allowedButtonsFilter, "AllowedButtonsFilter"),
        ]
        self._flut_create(props=props or None, bindings=bindings)

    @property
    def onTapDown(self) -> Optional[Callable[["TapDownDetails"], None]]:
        return self._flut_get("onTapDown")

    @onTapDown.setter
    def onTapDown(self, value: Optional[Callable[["TapDownDetails"], None]]) -> None:
        self._flut_set("onTapDown", value, "GestureTapDownCallback")

    @property
    def onTapUp(self) -> Optional[Callable[["TapUpDetails"], None]]:
        return self._flut_get("onTapUp")

    @onTapUp.setter
    def onTapUp(self, value: Optional[Callable[["TapUpDetails"], None]]) -> None:
        self._flut_set("onTapUp", value, "GestureTapUpCallback")

    @property
    def onTap(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTap")

    @onTap.setter
    def onTap(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onTap", value, "GestureTapCallback")

    @property
    def onTapMove(self) -> Optional[Callable[["TapMoveDetails"], None]]:
        return self._flut_get("onTapMove")

    @onTapMove.setter
    def onTapMove(self, value: Optional[Callable[["TapMoveDetails"], None]]) -> None:
        self._flut_set("onTapMove", value, "GestureTapMoveCallback")

    @property
    def onTapCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTapCancel")

    @onTapCancel.setter
    def onTapCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onTapCancel", value, "GestureTapCancelCallback")

    @property
    def onSecondaryTap(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onSecondaryTap")

    @onSecondaryTap.setter
    def onSecondaryTap(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onSecondaryTap", value, "GestureTapCallback")

    @property
    def onSecondaryTapDown(self) -> Optional[Callable[["TapDownDetails"], None]]:
        return self._flut_get("onSecondaryTapDown")

    @onSecondaryTapDown.setter
    def onSecondaryTapDown(
        self, value: Optional[Callable[["TapDownDetails"], None]]
    ) -> None:
        self._flut_set("onSecondaryTapDown", value, "GestureTapDownCallback")

    @property
    def onSecondaryTapUp(self) -> Optional[Callable[["TapUpDetails"], None]]:
        return self._flut_get("onSecondaryTapUp")

    @onSecondaryTapUp.setter
    def onSecondaryTapUp(
        self, value: Optional[Callable[["TapUpDetails"], None]]
    ) -> None:
        self._flut_set("onSecondaryTapUp", value, "GestureTapUpCallback")

    @property
    def onSecondaryTapCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onSecondaryTapCancel")

    @onSecondaryTapCancel.setter
    def onSecondaryTapCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onSecondaryTapCancel", value, "GestureTapCancelCallback")

    @property
    def onTertiaryTapDown(self) -> Optional[Callable[["TapDownDetails"], None]]:
        return self._flut_get("onTertiaryTapDown")

    @onTertiaryTapDown.setter
    def onTertiaryTapDown(
        self, value: Optional[Callable[["TapDownDetails"], None]]
    ) -> None:
        self._flut_set("onTertiaryTapDown", value, "GestureTapDownCallback")

    @property
    def onTertiaryTapUp(self) -> Optional[Callable[["TapUpDetails"], None]]:
        return self._flut_get("onTertiaryTapUp")

    @onTertiaryTapUp.setter
    def onTertiaryTapUp(
        self, value: Optional[Callable[["TapUpDetails"], None]]
    ) -> None:
        self._flut_set("onTertiaryTapUp", value, "GestureTapUpCallback")

    @property
    def onTertiaryTapCancel(self) -> Optional[Callable[[], None]]:
        return self._flut_get("onTertiaryTapCancel")

    @onTertiaryTapCancel.setter
    def onTertiaryTapCancel(self, value: Optional[Callable[[], None]]) -> None:
        self._flut_set("onTertiaryTapCancel", value, "GestureTapCancelCallback")
