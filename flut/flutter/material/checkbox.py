from typing import Optional, override

from flut._flut.engine import named_constructor, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class Checkbox(Widget):
    _flut_type = "Checkbox"

    width: float = 18.0

    def __init__(
        self,
        *,
        key=None,
        value: Optional[bool] = None,
        tristate: bool = False,
        onChanged=None,
        mouseCursor=None,
        activeColor=None,
        fillColor=None,
        checkColor=None,
        focusColor=None,
        hoverColor=None,
        overlayColor=None,
        splashRadius: Optional[float] = None,
        materialTapTargetSize=None,
        visualDensity=None,
        focusNode=None,
        autofocus: bool = False,
        shape=None,
        side=None,
        isError: bool = False,
        semanticLabel: Optional[str] = None,
    ):
        super().__init__(key=key)
        self.value = value
        self.tristate = tristate
        self.onChanged = onChanged
        self.mouseCursor = mouseCursor
        self.activeColor = activeColor
        self.fillColor = fillColor
        self.checkColor = checkColor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.overlayColor = overlayColor
        self.splashRadius = splashRadius
        self.materialTapTargetSize = materialTapTargetSize
        self.visualDensity = visualDensity
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.shape = shape
        self.side = side
        self.isError = isError
        self.semanticLabel = semanticLabel

    @named_constructor
    def adaptive(
        cls,
        *,
        key=None,
        value: Optional[bool] = None,
        tristate: bool = False,
        onChanged=None,
        mouseCursor=None,
        activeColor=None,
        fillColor=None,
        checkColor=None,
        focusColor=None,
        hoverColor=None,
        overlayColor=None,
        splashRadius: Optional[float] = None,
        materialTapTargetSize=None,
        visualDensity=None,
        focusNode=None,
        autofocus: bool = False,
        shape=None,
        side=None,
        isError: bool = False,
        semanticLabel: Optional[str] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.value = value
        instance.tristate = tristate
        instance.onChanged = onChanged
        instance.mouseCursor = mouseCursor
        instance.activeColor = activeColor
        instance.fillColor = fillColor
        instance.checkColor = checkColor
        instance.focusColor = focusColor
        instance.hoverColor = hoverColor
        instance.overlayColor = overlayColor
        instance.splashRadius = splashRadius
        instance.materialTapTargetSize = materialTapTargetSize
        instance.visualDensity = visualDensity
        instance.focusNode = focusNode
        instance.autofocus = autofocus
        instance.shape = shape
        instance.side = side
        instance.isError = isError
        instance.semanticLabel = semanticLabel
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        result["tristate"] = _flut_pack_value(self.tristate)
        result["onChanged"] = (
            self._register_action(self.onChanged, "ValueChanged<bool?>")._flut_pack()
            if self.onChanged is not None
            else None
        )
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.activeColor is not None:
            result["activeColor"] = _flut_pack_value(self.activeColor)
        if self.fillColor is not None:
            result["fillColor"] = _flut_pack_value(self.fillColor)
        if self.checkColor is not None:
            result["checkColor"] = _flut_pack_value(self.checkColor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.overlayColor is not None:
            result["overlayColor"] = _flut_pack_value(self.overlayColor)
        if self.splashRadius is not None:
            result["splashRadius"] = _flut_pack_value(self.splashRadius)
        if self.materialTapTargetSize is not None:
            result["materialTapTargetSize"] = _flut_pack_value(
                self.materialTapTargetSize
            )
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.side is not None:
            result["side"] = _flut_pack_value(self.side)
        result["isError"] = _flut_pack_value(self.isError)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        return result
