from flut._flut.engine import FlutEnumObject


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
