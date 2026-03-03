from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class CircleAvatar(Widget):
    _flut_type = "CircleAvatar"

    def __init__(
        self,
        *,
        key=None,
        child: Optional[Widget] = None,
        backgroundColor=None,
        backgroundImage=None,
        foregroundImage=None,
        onBackgroundImageError=None,
        onForegroundImageError=None,
        foregroundColor=None,
        radius: Optional[float] = None,
        minRadius: Optional[float] = None,
        maxRadius: Optional[float] = None,
    ):
        super().__init__(key=key)
        self.child = child
        self.backgroundColor = backgroundColor
        self.backgroundImage = backgroundImage
        self.foregroundImage = foregroundImage
        self.onBackgroundImageError = onBackgroundImageError
        self.onForegroundImageError = onForegroundImageError
        self.foregroundColor = foregroundColor
        self.radius = radius
        self.minRadius = minRadius
        self.maxRadius = maxRadius

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.backgroundImage is not None:
            result["backgroundImage"] = _flut_pack_value(self.backgroundImage)
        if self.foregroundImage is not None:
            result["foregroundImage"] = _flut_pack_value(self.foregroundImage)
        if self.onBackgroundImageError is not None:
            result["onBackgroundImageError"] = self._register_action(
                self.onBackgroundImageError, "ImageErrorListener"
            )._flut_pack()
        if self.onForegroundImageError is not None:
            result["onForegroundImageError"] = self._register_action(
                self.onForegroundImageError, "ImageErrorListener"
            )._flut_pack()
        if self.foregroundColor is not None:
            result["foregroundColor"] = _flut_pack_value(self.foregroundColor)
        if self.radius is not None:
            result["radius"] = _flut_pack_value(self.radius)
        if self.minRadius is not None:
            result["minRadius"] = _flut_pack_value(self.minRadius)
        if self.maxRadius is not None:
            result["maxRadius"] = _flut_pack_value(self.maxRadius)
        return result
