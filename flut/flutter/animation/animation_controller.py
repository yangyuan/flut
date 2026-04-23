from typing import Optional

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.flutter.foundation.change_notifier import Listenable
from flut.flutter.animation.animation import Animation, AnimationStatus
from flut.flutter.animation.curves import Curve, Curves
from flut.dart.core import Duration


class AnimationBehavior(FlutEnumObject):
    normal: "AnimationBehavior"
    preserve: "AnimationBehavior"


class AnimationController(Animation):
    _flut_type = "AnimationController"

    def __init__(
        self,
        *,
        value: Optional[float] = None,
        duration: Optional[Duration] = None,
        reverseDuration: Optional[Duration] = None,
        debugLabel: Optional[str] = None,
        lowerBound: float = 0.0,
        upperBound: float = 1.0,
        animationBehavior: AnimationBehavior = AnimationBehavior.normal,
        vsync,
    ):
        props = {
            "lowerBound": lowerBound,
            "upperBound": upperBound,
            "vsync": vsync._flut_pack(),
            "animationBehavior": _flut_pack_value(animationBehavior),
        }
        if value is not None:
            props["value"] = value
        if duration is not None:
            props["duration"] = duration._flut_pack()
        if reverseDuration is not None:
            props["reverseDuration"] = reverseDuration._flut_pack()
        if debugLabel is not None:
            props["debugLabel"] = debugLabel
        self._flut_init_props = props
        Listenable.__init__(self)

    @property
    def value(self) -> float:
        return self._flut_get("value")

    @value.setter
    def value(self, new_value: float):
        self._flut_set("value", new_value)

    @property
    def status(self) -> AnimationStatus:
        return self._flut_get("status")

    @property
    def isAnimating(self) -> bool:
        return bool(self._flut_get("isAnimating"))

    @property
    def duration(self) -> Optional[Duration]:
        return self._flut_get("duration")

    @duration.setter
    def duration(self, value: Optional[Duration]):
        self._flut_set("duration", value._flut_pack() if value is not None else None)

    @property
    def reverseDuration(self) -> Optional[Duration]:
        return self._flut_get("reverseDuration")

    @reverseDuration.setter
    def reverseDuration(self, value: Optional[Duration]):
        self._flut_set(
            "reverseDuration", value._flut_pack() if value is not None else None
        )

    def forward(self, *, from_: Optional[float] = None):
        if from_ is not None:
            self._flut_call("forward", from_=from_)
        else:
            self._flut_call("forward")

    def reverse(self, *, from_: Optional[float] = None):
        if from_ is not None:
            self._flut_call("reverse", from_=from_)
        else:
            self._flut_call("reverse")

    def repeat(
        self,
        *,
        min: Optional[float] = None,
        max: Optional[float] = None,
        reverse: bool = False,
        period: Optional[Duration] = None,
    ):
        kwargs = {"reverse": reverse}
        if min is not None:
            kwargs["min"] = min
        if max is not None:
            kwargs["max"] = max
        if period is not None:
            kwargs["period"] = period._flut_pack()
        self._flut_call("repeat", **kwargs)

    def stop(self):
        self._flut_call("stop")

    def reset(self):
        self._flut_call("reset")

    def animateTo(
        self,
        target: float,
        *,
        duration: Optional[Duration] = None,
        curve: Curve = Curves.linear,
    ):
        kwargs = {"curve": curve._flut_pack()}
        if duration is not None:
            kwargs["duration"] = duration._flut_pack()
        self._flut_call("animateTo", target, **kwargs)
