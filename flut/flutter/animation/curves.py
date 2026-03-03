from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class Curve(FlutValueObject):
    _flut_type = "Curve"

    def __init__(self, kind: str):
        super().__init__()
        self.kind = kind

    @staticmethod
    def _flut_unpack(data: dict) -> "Curve":
        return Curve(kind=_flut_unpack_required_field(data, "kind"))

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["kind"] = _flut_pack_value(self.kind)
        return result


class Curves:
    linear = Curve("linear")
    decelerate = Curve("decelerate")
    ease = Curve("ease")
    easeIn = Curve("easeIn")
    easeInSine = Curve("easeInSine")
    easeInQuad = Curve("easeInQuad")
    easeInCubic = Curve("easeInCubic")
    easeInQuart = Curve("easeInQuart")
    easeInQuint = Curve("easeInQuint")
    easeInExpo = Curve("easeInExpo")
    easeInCirc = Curve("easeInCirc")
    easeInBack = Curve("easeInBack")
    easeOut = Curve("easeOut")
    easeOutSine = Curve("easeOutSine")
    easeOutQuad = Curve("easeOutQuad")
    easeOutCubic = Curve("easeOutCubic")
    easeOutQuart = Curve("easeOutQuart")
    easeOutQuint = Curve("easeOutQuint")
    easeOutExpo = Curve("easeOutExpo")
    easeOutCirc = Curve("easeOutCirc")
    easeOutBack = Curve("easeOutBack")
    easeInOut = Curve("easeInOut")
    easeInOutSine = Curve("easeInOutSine")
    easeInOutQuad = Curve("easeInOutQuad")
    easeInOutCubic = Curve("easeInOutCubic")
    easeInOutCubicEmphasized = Curve("easeInOutCubicEmphasized")
    easeInOutQuart = Curve("easeInOutQuart")
    easeInOutQuint = Curve("easeInOutQuint")
    easeInOutExpo = Curve("easeInOutExpo")
    easeInOutCirc = Curve("easeInOutCirc")
    easeInOutBack = Curve("easeInOutBack")
    fastOutSlowIn = Curve("fastOutSlowIn")
    slowMiddle = Curve("slowMiddle")
    bounceIn = Curve("bounceIn")
    bounceOut = Curve("bounceOut")
    bounceInOut = Curve("bounceInOut")
    elasticIn = Curve("elasticIn")
    elasticOut = Curve("elasticOut")
    elasticInOut = Curve("elasticInOut")
    easeInToLinear = Curve("easeInToLinear")
    linearToEaseOut = Curve("linearToEaseOut")
    fastLinearToSlowEaseIn = Curve("fastLinearToSlowEaseIn")
    fastEaseInToSlowEaseOut = Curve("fastEaseInToSlowEaseOut")
