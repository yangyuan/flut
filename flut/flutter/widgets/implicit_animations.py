from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.core import Duration
from flut.dart.ui import Clip
from flut.flutter.animation.curves import Curves

from flut.flutter.widgets.framework import Widget


class AnimatedContainer(Widget):
    _flut_type = "AnimatedContainer"

    def __init__(
        self,
        *,
        key=None,
        alignment=None,
        padding=None,
        color=None,
        decoration=None,
        foregroundDecoration=None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        constraints=None,
        margin=None,
        transform=None,
        transformAlignment=None,
        clipBehavior: Clip = Clip.none,
        curve=Curves.linear,
        duration: Duration,
        onEnd=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.alignment = alignment
        self.padding = padding
        self.color = color
        self.decoration = decoration
        self.foregroundDecoration = foregroundDecoration
        self.width = width
        self.height = height
        self.constraints = constraints
        self.margin = margin
        self.transform = transform
        self.transformAlignment = transformAlignment
        self.clipBehavior = clipBehavior
        self.curve = curve
        self.duration = duration
        self.onEnd = onEnd
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["duration"] = _flut_pack_value(self.duration)
        result["curve"] = _flut_pack_value(self.curve)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.foregroundDecoration is not None:
            result["foregroundDecoration"] = _flut_pack_value(self.foregroundDecoration)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.margin is not None:
            result["margin"] = _flut_pack_value(self.margin)
        if self.transform is not None:
            result["transform"] = _flut_pack_value(self.transform)
        if self.transformAlignment is not None:
            result["transformAlignment"] = _flut_pack_value(self.transformAlignment)
        if self.onEnd is not None:
            result["onEnd"] = self._register_action(
                self.onEnd, "VoidCallback"
            )._flut_pack()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class AnimatedOpacity(Widget):
    _flut_type = "AnimatedOpacity"

    def __init__(
        self,
        *,
        key=None,
        opacity: float,
        curve=Curves.linear,
        duration: Duration,
        onEnd=None,
        alwaysIncludeSemantics: bool = False,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.opacity = opacity
        self.curve = curve
        self.duration = duration
        self.onEnd = onEnd
        self.alwaysIncludeSemantics = alwaysIncludeSemantics
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["opacity"] = _flut_pack_value(self.opacity)
        result["curve"] = _flut_pack_value(self.curve)
        result["duration"] = _flut_pack_value(self.duration)
        result["alwaysIncludeSemantics"] = _flut_pack_value(self.alwaysIncludeSemantics)
        if self.onEnd is not None:
            result["onEnd"] = self._register_action(
                self.onEnd, "VoidCallback"
            )._flut_pack()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
