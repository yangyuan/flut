from flut._flut.engine import FlutAbstractObject
from flut.flutter.widgets.routes import ModalRoute


class PageRoute(ModalRoute, FlutAbstractObject):
    _flut_type = "PageRoute"

    def __init__(self, *, settings=None, fullscreenDialog: bool = False):
        super().__init__(settings=settings)

    @property
    def fullscreenDialog(self):
        return self._flut_get("fullscreenDialog")

    @property
    def maintainState(self):
        return self._flut_get("maintainState")
