from typing import Optional

from flut._flut.engine import (
    FlutAbstractObject,
    FlutRealtimeObject,
    call_dart_static,
)


class ModalRoute(FlutRealtimeObject, FlutAbstractObject):
    _flut_type = "ModalRoute"
    _flut_init_props: dict = {}
    _flut_init_bindings: Optional[list] = None

    def __init__(self):
        FlutRealtimeObject.__init__(self)
        self._flut_create(
            props=self._flut_init_props or None,
            bindings=self._flut_init_bindings,
        )

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
