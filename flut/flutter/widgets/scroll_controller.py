from flut.flutter.foundation.change_notifier import ChangeNotifier
from flut.dart import Duration
from flut.flutter.animation.curves import Curve, Curves

from .scroll_position import ScrollPosition


class ScrollController(ChangeNotifier):
    _flut_type = "ScrollController"

    def __init__(self, initialScrollOffset: float = 0.0):
        super().__init__()
        self._flut_create(props={"initialScrollOffset": initialScrollOffset})

    @property
    def offset(self) -> float:
        return self._flut_get("offset")

    @property
    def hasClients(self) -> bool:
        return self._flut_get("hasClients")

    @property
    def position(self) -> ScrollPosition | None:
        return self._flut_get("position")

    def jumpTo(self, value: float):
        self._flut_call("jumpTo", value)

    def dispose(self):
        self._flut_call("dispose")

    def animateTo(self, offset: float, *, duration: Duration, curve: Curve):
        self._flut_call(
            "animateTo",
            offset,
            duration=duration._flut_pack(),
            curve=curve._flut_pack(),
        )
