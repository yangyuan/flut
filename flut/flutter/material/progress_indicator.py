from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class CircularProgressIndicator(Widget):
    _flut_type = "CircularProgressIndicator"

    def __init__(
        self,
        *,
        key=None,
        value: Optional[float] = None,
        backgroundColor=None,
        color=None,
        valueColor=None,
        strokeWidth: float = 4.0,
        strokeAlign: Optional[float] = None,
        semanticsLabel: Optional[str] = None,
        semanticsValue: Optional[str] = None,
        strokeCap=None,
        constraints=None,
        trackGap: Optional[float] = None,
        padding=None,
        controller=None,
    ):
        super().__init__(key=key)
        self.value = value
        self.backgroundColor = backgroundColor
        self.color = color
        self.valueColor = valueColor
        self.strokeWidth = strokeWidth
        self.strokeAlign = strokeAlign
        self.semanticsLabel = semanticsLabel
        self.semanticsValue = semanticsValue
        self.strokeCap = strokeCap
        self.constraints = constraints
        self.trackGap = trackGap
        self.padding = padding
        self.controller = controller

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.value is not None:
            result["value"] = _flut_pack_value(self.value)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.valueColor is not None:
            result["valueColor"] = _flut_pack_value(self.valueColor)
        result["strokeWidth"] = _flut_pack_value(self.strokeWidth)
        if self.strokeAlign is not None:
            result["strokeAlign"] = _flut_pack_value(self.strokeAlign)
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.semanticsValue is not None:
            result["semanticsValue"] = _flut_pack_value(self.semanticsValue)
        if self.strokeCap is not None:
            result["strokeCap"] = _flut_pack_value(self.strokeCap)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.trackGap is not None:
            result["trackGap"] = _flut_pack_value(self.trackGap)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        return result


class LinearProgressIndicator(Widget):
    _flut_type = "LinearProgressIndicator"

    def __init__(
        self,
        *,
        key=None,
        value: Optional[float] = None,
        backgroundColor=None,
        color=None,
        valueColor=None,
        minHeight: Optional[float] = None,
        semanticsLabel: Optional[str] = None,
        semanticsValue: Optional[str] = None,
        borderRadius=None,
        stopIndicatorColor=None,
        stopIndicatorRadius: Optional[float] = None,
        trackGap: Optional[float] = None,
        controller=None,
    ):
        super().__init__(key=key)
        self.value = value
        self.backgroundColor = backgroundColor
        self.color = color
        self.valueColor = valueColor
        self.minHeight = minHeight
        self.semanticsLabel = semanticsLabel
        self.semanticsValue = semanticsValue
        self.borderRadius = borderRadius
        self.stopIndicatorColor = stopIndicatorColor
        self.stopIndicatorRadius = stopIndicatorRadius
        self.trackGap = trackGap
        self.controller = controller

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.value is not None:
            result["value"] = _flut_pack_value(self.value)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.valueColor is not None:
            result["valueColor"] = _flut_pack_value(self.valueColor)
        if self.minHeight is not None:
            result["minHeight"] = _flut_pack_value(self.minHeight)
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.semanticsValue is not None:
            result["semanticsValue"] = _flut_pack_value(self.semanticsValue)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.stopIndicatorColor is not None:
            result["stopIndicatorColor"] = _flut_pack_value(self.stopIndicatorColor)
        if self.stopIndicatorRadius is not None:
            result["stopIndicatorRadius"] = _flut_pack_value(self.stopIndicatorRadius)
        if self.trackGap is not None:
            result["trackGap"] = _flut_pack_value(self.trackGap)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        return result
