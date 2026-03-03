from typing import override

from flut._flut.engine import (
    FlutAbstractObject,
    FlutRealtimeObject,
    call_dart_static,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field
from flut.flutter.widgets.navigator import RouteSettings


class ModalRoute(FlutRealtimeObject, FlutAbstractObject):
    _flut_type = "ModalRoute"

    def __init__(self, *, settings=None):
        super().__init__()

    @staticmethod
    def of(context):
        return call_dart_static("ModalRoute", "of", context._flut_pack())

    @property
    def isCurrent(self):
        return self._flut_get("isCurrent")

    @property
    def isActive(self):
        return self._flut_get("isActive")

    @property
    def settings(self):
        return self._flut_get("settings")

    @property
    def canPop(self):
        return self._flut_get("canPop")

    @property
    def transitionDuration(self):
        return self._flut_get("transitionDuration")

    @property
    def barrierColor(self):
        return self._flut_get("barrierColor")

    @property
    def barrierLabel(self):
        return self._flut_get("barrierLabel")
