from typing import Optional, override

from flut._flut.engine import named_constructor, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class Card(Widget):
    _flut_type = "Card"

    def __init__(
        self,
        *,
        key=None,
        color=None,
        shadowColor=None,
        surfaceTintColor=None,
        elevation: Optional[float] = None,
        shape=None,
        borderOnForeground: bool = True,
        margin=None,
        clipBehavior=None,
        child: Optional[Widget] = None,
        semanticContainer: bool = True,
    ):
        super().__init__(key=key)
        self.color = color
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.elevation = elevation
        self.shape = shape
        self.borderOnForeground = borderOnForeground
        self.margin = margin
        self.clipBehavior = clipBehavior
        self.child = child
        self.semanticContainer = semanticContainer

    @named_constructor
    def filled(
        cls,
        *,
        key=None,
        color=None,
        shadowColor=None,
        surfaceTintColor=None,
        elevation: Optional[float] = None,
        shape=None,
        borderOnForeground: bool = True,
        margin=None,
        clipBehavior=None,
        child: Optional[Widget] = None,
        semanticContainer: bool = True,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.color = color
        instance.shadowColor = shadowColor
        instance.surfaceTintColor = surfaceTintColor
        instance.elevation = elevation
        instance.shape = shape
        instance.borderOnForeground = borderOnForeground
        instance.margin = margin
        instance.clipBehavior = clipBehavior
        instance.child = child
        instance.semanticContainer = semanticContainer
        return instance

    @named_constructor
    def outlined(
        cls,
        *,
        key=None,
        color=None,
        shadowColor=None,
        surfaceTintColor=None,
        elevation: Optional[float] = None,
        shape=None,
        borderOnForeground: bool = True,
        margin=None,
        clipBehavior=None,
        child: Optional[Widget] = None,
        semanticContainer: bool = True,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.color = color
        instance.shadowColor = shadowColor
        instance.surfaceTintColor = surfaceTintColor
        instance.elevation = elevation
        instance.shape = shape
        instance.borderOnForeground = borderOnForeground
        instance.margin = margin
        instance.clipBehavior = clipBehavior
        instance.child = child
        instance.semanticContainer = semanticContainer
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        result["borderOnForeground"] = _flut_pack_value(self.borderOnForeground)
        if self.margin is not None:
            result["margin"] = _flut_pack_value(self.margin)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        result["semanticContainer"] = _flut_pack_value(self.semanticContainer)
        return result
