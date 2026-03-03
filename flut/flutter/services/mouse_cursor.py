from typing import override

from flut._flut.engine import FlutAbstractObject, _flut_pack_value


class _MouseCursor(FlutAbstractObject):
    _flut_type = "MouseCursor"

    def __init__(self, debugDescription: str = ""):
        super().__init__()
        self._debugDescription = debugDescription

    @property
    def debugDescription(self) -> str:
        return self._debugDescription

    def createSession(self, device: int):
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["debugDescription"] = _flut_pack_value(self.debugDescription)
        return result


class MouseCursor(_MouseCursor):
    defer = _MouseCursor("defer")
    uncontrolled = _MouseCursor("uncontrolled")


class SystemMouseCursor(MouseCursor):
    _flut_type = "SystemMouseCursor"

    def __init__(self, kind: str):
        super().__init__(f"SystemMouseCursor({kind})")
        self.kind = kind

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["kind"] = _flut_pack_value(self.kind)
        return result


class SystemMouseCursors:
    none = SystemMouseCursor("none")
    basic = SystemMouseCursor("basic")
    click = SystemMouseCursor("click")
    forbidden = SystemMouseCursor("forbidden")
    wait = SystemMouseCursor("wait")
    progress = SystemMouseCursor("progress")
    contextMenu = SystemMouseCursor("contextMenu")
    help = SystemMouseCursor("help")
    text = SystemMouseCursor("text")
    verticalText = SystemMouseCursor("verticalText")
    cell = SystemMouseCursor("cell")
    precise = SystemMouseCursor("precise")
    move = SystemMouseCursor("move")
    grab = SystemMouseCursor("grab")
    grabbing = SystemMouseCursor("grabbing")
    noDrop = SystemMouseCursor("noDrop")
    alias = SystemMouseCursor("alias")
    copy = SystemMouseCursor("copy")
    disappearing = SystemMouseCursor("disappearing")
    allScroll = SystemMouseCursor("allScroll")
    resizeLeftRight = SystemMouseCursor("resizeLeftRight")
    resizeUpDown = SystemMouseCursor("resizeUpDown")
    resizeUpLeftDownRight = SystemMouseCursor("resizeUpLeftDownRight")
    resizeUpRightDownLeft = SystemMouseCursor("resizeUpRightDownLeft")
    resizeUp = SystemMouseCursor("resizeUp")
    resizeDown = SystemMouseCursor("resizeDown")
    resizeLeft = SystemMouseCursor("resizeLeft")
    resizeRight = SystemMouseCursor("resizeRight")
    resizeUpLeft = SystemMouseCursor("resizeUpLeft")
    resizeUpRight = SystemMouseCursor("resizeUpRight")
    resizeDownLeft = SystemMouseCursor("resizeDownLeft")
    resizeDownRight = SystemMouseCursor("resizeDownRight")
    resizeColumn = SystemMouseCursor("resizeColumn")
    resizeRow = SystemMouseCursor("resizeRow")
    zoomIn = SystemMouseCursor("zoomIn")
    zoomOut = SystemMouseCursor("zoomOut")
