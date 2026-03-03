from typing import Callable, Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.material.slider_theme import ShowValueIndicator
from flut.flutter.services.mouse_cursor import MouseCursor
from flut.flutter.widgets.framework import Widget


class SliderInteraction(FlutEnumObject):
    tapAndSlide: "SliderInteraction"
    tapOnly: "SliderInteraction"
    slideOnly: "SliderInteraction"
    slideThumb: "SliderInteraction"


class Slider(Widget):
    _flut_type = "Slider"

    def __init__(
        self,
        *,
        key=None,
        value: float,
        secondaryTrackValue: Optional[float] = None,
        onChanged: Optional[Callable[[float], None]] = None,
        onChangeStart: Optional[Callable[[float], None]] = None,
        onChangeEnd: Optional[Callable[[float], None]] = None,
        min: float = 0.0,
        max: float = 1.0,
        divisions: Optional[int] = None,
        label: Optional[str] = None,
        activeColor: Optional[Color] = None,
        inactiveColor: Optional[Color] = None,
        secondaryActiveColor: Optional[Color] = None,
        thumbColor: Optional[Color] = None,
        overlayColor=None,
        mouseCursor: Optional[MouseCursor] = None,
        semanticFormatterCallback=None,
        focusNode=None,
        autofocus: bool = False,
        allowedInteraction: Optional["SliderInteraction"] = None,
        padding=None,
        showValueIndicator: Optional["ShowValueIndicator"] = None,
    ):
        super().__init__(key=key)
        self.value = value
        self.secondaryTrackValue = secondaryTrackValue
        self.onChanged = onChanged
        self.onChangeStart = onChangeStart
        self.onChangeEnd = onChangeEnd
        self.min = min
        self.max = max
        self.divisions = divisions
        self.label = label
        self.activeColor = activeColor
        self.inactiveColor = inactiveColor
        self.secondaryActiveColor = secondaryActiveColor
        self.thumbColor = thumbColor
        self.overlayColor = overlayColor
        self.mouseCursor = mouseCursor
        self.semanticFormatterCallback = semanticFormatterCallback
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.allowedInteraction = allowedInteraction
        self.padding = padding
        self.showValueIndicator = showValueIndicator

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        result["onChanged"] = (
            self._register_action(self.onChanged, "ValueChanged<double>")._flut_pack()
            if self.onChanged is not None
            else None
        )
        result["min"] = _flut_pack_value(self.min)
        result["max"] = _flut_pack_value(self.max)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.secondaryTrackValue is not None:
            result["secondaryTrackValue"] = _flut_pack_value(self.secondaryTrackValue)
        if self.onChangeStart is not None:
            result["onChangeStart"] = self._register_action(
                self.onChangeStart, "ValueChanged<double>"
            )._flut_pack()
        if self.onChangeEnd is not None:
            result["onChangeEnd"] = self._register_action(
                self.onChangeEnd, "ValueChanged<double>"
            )._flut_pack()
        if self.divisions is not None:
            result["divisions"] = _flut_pack_value(self.divisions)
        if self.label is not None:
            result["label"] = _flut_pack_value(self.label)
        if self.activeColor is not None:
            result["activeColor"] = _flut_pack_value(self.activeColor)
        if self.inactiveColor is not None:
            result["inactiveColor"] = _flut_pack_value(self.inactiveColor)
        if self.secondaryActiveColor is not None:
            result["secondaryActiveColor"] = _flut_pack_value(self.secondaryActiveColor)
        if self.thumbColor is not None:
            result["thumbColor"] = _flut_pack_value(self.thumbColor)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.semanticFormatterCallback is not None:
            result["semanticFormatterCallback"] = self._register_action(
                self.semanticFormatterCallback, "SemanticFormatterCallback"
            )._flut_pack()
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.allowedInteraction is not None:
            result["allowedInteraction"] = _flut_pack_value(self.allowedInteraction)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.showValueIndicator is not None:
            result["showValueIndicator"] = _flut_pack_value(self.showValueIndicator)
        return result
