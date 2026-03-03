from flut._flut.engine import FlutRealtimeObject


class RenderObject(FlutRealtimeObject):
    _flut_type = "RenderObject"

    @property
    def attached(self) -> bool:
        return bool(self._flut_get("attached"))

    @property
    def parent(self):
        return self._flut_get("parent")

    @property
    def paintBounds(self):
        return self._flut_get("paintBounds")
