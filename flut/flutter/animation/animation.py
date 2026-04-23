from typing import Callable

from flut._flut.engine import FlutEnumObject
from flut.flutter.foundation.change_notifier import Listenable


class AnimationStatus(FlutEnumObject):
    dismissed: "AnimationStatus"
    forward: "AnimationStatus"
    reverse: "AnimationStatus"
    completed: "AnimationStatus"

    @property
    def isAnimating(self) -> bool:
        return self is AnimationStatus.forward or self is AnimationStatus.reverse

    @property
    def isCompleted(self) -> bool:
        return self is AnimationStatus.completed

    @property
    def isDismissed(self) -> bool:
        return self is AnimationStatus.dismissed

    @property
    def isForwardOrCompleted(self) -> bool:
        return self is AnimationStatus.forward or self is AnimationStatus.completed


class Animation(Listenable):
    _flut_type = "Animation"

    @property
    def value(self):
        raise NotImplementedError

    @property
    def status(self) -> AnimationStatus:
        raise NotImplementedError

    @property
    def isAnimating(self) -> bool:
        return (
            self.status is AnimationStatus.forward
            or self.status is AnimationStatus.reverse
        )

    @property
    def isCompleted(self) -> bool:
        return self.status is AnimationStatus.completed

    @property
    def isDismissed(self) -> bool:
        return self.status is AnimationStatus.dismissed

    @property
    def isForwardOrCompleted(self) -> bool:
        return (
            self.status is AnimationStatus.forward
            or self.status is AnimationStatus.completed
        )

    def addStatusListener(self, listener: Callable[[AnimationStatus], None]):
        self._flut_call_with_callable(
            "addStatusListener", listener, "AnimationStatusListener"
        )

    def removeStatusListener(self, listener: Callable[[AnimationStatus], None]):
        self._flut_remove_callable(
            "removeStatusListener", "addStatusListener", listener
        )
