from typing import Optional, override

from flut._flut.engine import named_constructor, _flut_pack_value

from flut.flutter.widgets.framework import Widget
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.painting.text_painter import TextOverflow


class Text(Widget):
    _flut_type = "Text"

    def __init__(
        self,
        data: str,
        *,
        key=None,
        style: Optional[TextStyle] = None,
        strutStyle=None,
        textAlign=None,
        textDirection=None,
        locale=None,
        softWrap: Optional[bool] = None,
        overflow: Optional[TextOverflow] = None,
        textScaler=None,
        maxLines: Optional[int] = None,
        semanticsLabel: Optional[str] = None,
        semanticsIdentifier: Optional[str] = None,
        textWidthBasis=None,
        textHeightBehavior=None,
        selectionColor=None,
    ):
        super().__init__(key=key)
        self.data = data
        self.style = style
        self.strutStyle = strutStyle
        self.textAlign = textAlign
        self.textDirection = textDirection
        self.locale = locale
        self.softWrap = softWrap
        self.overflow = overflow
        self.textScaler = textScaler
        self.maxLines = maxLines
        self.semanticsLabel = semanticsLabel
        self.semanticsIdentifier = semanticsIdentifier
        self.textWidthBasis = textWidthBasis
        self.textHeightBehavior = textHeightBehavior
        self.selectionColor = selectionColor

    @named_constructor
    def rich(
        cls,
        textSpan,
        *,
        key=None,
        style: Optional[TextStyle] = None,
        strutStyle=None,
        textAlign=None,
        textDirection=None,
        locale=None,
        softWrap: Optional[bool] = None,
        overflow: Optional[TextOverflow] = None,
        textScaler=None,
        maxLines: Optional[int] = None,
        semanticsLabel: Optional[str] = None,
        semanticsIdentifier: Optional[str] = None,
        textWidthBasis=None,
        textHeightBehavior=None,
        selectionColor=None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.data = None
        instance.style = style
        instance.strutStyle = strutStyle
        instance.textAlign = textAlign
        instance.textDirection = textDirection
        instance.locale = locale
        instance.softWrap = softWrap
        instance.overflow = overflow
        instance.textScaler = textScaler
        instance.maxLines = maxLines
        instance.semanticsLabel = semanticsLabel
        instance.semanticsIdentifier = semanticsIdentifier
        instance.textWidthBasis = textWidthBasis
        instance.textHeightBehavior = textHeightBehavior
        instance.selectionColor = selectionColor
        instance.textSpan = textSpan
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.strutStyle is not None:
            result["strutStyle"] = _flut_pack_value(self.strutStyle)
        if self.textAlign is not None:
            result["textAlign"] = _flut_pack_value(self.textAlign)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        if self.locale is not None:
            result["locale"] = _flut_pack_value(self.locale)
        if self.softWrap is not None:
            result["softWrap"] = _flut_pack_value(self.softWrap)
        if self.overflow is not None:
            result["overflow"] = _flut_pack_value(self.overflow)
        if self.textScaler is not None:
            result["textScaler"] = _flut_pack_value(self.textScaler)
        if self.maxLines is not None:
            result["maxLines"] = _flut_pack_value(self.maxLines)
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.semanticsIdentifier is not None:
            result["semanticsIdentifier"] = _flut_pack_value(self.semanticsIdentifier)
        if self.textWidthBasis is not None:
            result["textWidthBasis"] = _flut_pack_value(self.textWidthBasis)
        if self.textHeightBehavior is not None:
            result["textHeightBehavior"] = _flut_pack_value(self.textHeightBehavior)
        if self.selectionColor is not None:
            result["selectionColor"] = _flut_pack_value(self.selectionColor)
        if self._flut_init is None:
            result["data"] = _flut_pack_value(self.data)
        if self._flut_init == "rich":
            result["textSpan"] = _flut_pack_value(self.textSpan)
        return result
