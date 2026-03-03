from flut._flut.engine import FlutRealtimeObject
from flut.dart import Duration
from flut.flutter.animation.curves import Curve


class ScrollPosition(FlutRealtimeObject):
    _flut_type = "ScrollPosition"

    @property
    def pixels(self) -> float:
        return self._flut_get("pixels")

    @property
    def minScrollExtent(self) -> float:
        return self._flut_get("minScrollExtent")

    @property
    def maxScrollExtent(self) -> float:
        return self._flut_get("maxScrollExtent")

    @property
    def viewportDimension(self) -> float:
        return self._flut_get("viewportDimension")

    @property
    def hasContentDimensions(self) -> bool:
        return self._flut_get("hasContentDimensions")

    @property
    def hasPixels(self) -> bool:
        return self._flut_get("hasPixels")

    @property
    def atEdge(self) -> bool:
        return self._flut_get("atEdge")

    def jumpTo(self, value: float):
        self._flut_call("jumpTo", value)

    def animateTo(self, to: float, *, duration: Duration, curve: Curve):
        self._flut_call(
            "animateTo",
            to,
            duration=duration._flut_pack(),
            curve=curve._flut_pack(),
        )
