from flut._flut.engine import FlutRealtimeObject, _flut_pack_value


class MenuController(FlutRealtimeObject):
    _flut_type = "MenuController"

    def __init__(self):
        super().__init__()
        self._flut_create(props={})

    @property
    def isOpen(self) -> bool:
        return bool(self._flut_get("isOpen"))

    def open(self, *, position=None):
        self._flut_call("open", position=_flut_pack_value(position))

    def close(self):
        self._flut_call("close")

    def closeChildren(self):
        self._flut_call("closeChildren")
