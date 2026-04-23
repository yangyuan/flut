from flut._flut.engine import FlutAbstractObject
from flut.flutter.widgets.routes import ModalRoute


class PageRoute(ModalRoute, FlutAbstractObject):
    _flut_type = "PageRoute"

    @property
    def fullscreenDialog(self):
        return self._flut_get("fullscreenDialog")

    @property
    def maintainState(self):
        return self._flut_get("maintainState")
