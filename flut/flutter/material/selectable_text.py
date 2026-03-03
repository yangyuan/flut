from typing import Optional, override

from flut._flut.engine import named_constructor, _flut_pack_value
from flut.flutter.gestures.recognizer import DragStartBehavior
from ..widgets.framework import Widget
from ..painting.text_style import TextStyle


class SelectableText(Widget):
    _flut_type = "SelectableText"

    def __init__(
        self,
        data: str,
        *,
        key=None,
        focusNode=None,
        style: Optional[TextStyle] = None,
        strutStyle=None,
        textAlign=None,
        textDirection=None,
        textScaler=None,
        showCursor: bool = False,
        autofocus: bool = False,
        minLines: Optional[int] = None,
        maxLines: Optional[int] = None,
        cursorWidth: float = 2.0,
        cursorHeight: Optional[float] = None,
        cursorRadius=None,
        cursorColor=None,
        selectionColor=None,
        selectionHeightStyle=None,
        selectionWidthStyle=None,
        dragStartBehavior=DragStartBehavior.start,
        enableInteractiveSelection: bool = True,
        selectionControls=None,
        onTap=None,
        scrollPhysics=None,
        semanticsLabel: Optional[str] = None,
        textHeightBehavior=None,
        textWidthBasis=None,
        onSelectionChanged=None,
        contextMenuBuilder=None,
        magnifierConfiguration=None,
        scrollBehavior=None,
    ):
        super().__init__(key=key)
        self.data = data
        self.focusNode = focusNode
        self.style = style
        self.strutStyle = strutStyle
        self.textAlign = textAlign
        self.textDirection = textDirection
        self.textScaler = textScaler
        self.showCursor = showCursor
        self.autofocus = autofocus
        self.minLines = minLines
        self.maxLines = maxLines
        self.cursorWidth = cursorWidth
        self.cursorHeight = cursorHeight
        self.cursorRadius = cursorRadius
        self.cursorColor = cursorColor
        self.selectionColor = selectionColor
        self.selectionHeightStyle = selectionHeightStyle
        self.selectionWidthStyle = selectionWidthStyle
        self.dragStartBehavior = dragStartBehavior
        self.enableInteractiveSelection = enableInteractiveSelection
        self.selectionControls = selectionControls
        self.onTap = onTap
        self.scrollPhysics = scrollPhysics
        self.semanticsLabel = semanticsLabel
        self.textHeightBehavior = textHeightBehavior
        self.textWidthBasis = textWidthBasis
        self.onSelectionChanged = onSelectionChanged
        self.contextMenuBuilder = contextMenuBuilder
        self.magnifierConfiguration = magnifierConfiguration
        self.scrollBehavior = scrollBehavior

    @named_constructor
    def rich(
        cls,
        textSpan,
        *,
        key=None,
        focusNode=None,
        style: Optional[TextStyle] = None,
        strutStyle=None,
        textAlign=None,
        textDirection=None,
        textScaler=None,
        showCursor: bool = False,
        autofocus: bool = False,
        minLines: Optional[int] = None,
        maxLines: Optional[int] = None,
        cursorWidth: float = 2.0,
        cursorHeight: Optional[float] = None,
        cursorRadius=None,
        cursorColor=None,
        selectionColor=None,
        selectionHeightStyle=None,
        selectionWidthStyle=None,
        dragStartBehavior=DragStartBehavior.start,
        enableInteractiveSelection: bool = True,
        selectionControls=None,
        onTap=None,
        scrollPhysics=None,
        semanticsLabel: Optional[str] = None,
        textHeightBehavior=None,
        textWidthBasis=None,
        onSelectionChanged=None,
        contextMenuBuilder=None,
        magnifierConfiguration=None,
        scrollBehavior=None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.data = None
        instance.focusNode = focusNode
        instance.style = style
        instance.strutStyle = strutStyle
        instance.textAlign = textAlign
        instance.textDirection = textDirection
        instance.textScaler = textScaler
        instance.showCursor = showCursor
        instance.autofocus = autofocus
        instance.minLines = minLines
        instance.maxLines = maxLines
        instance.cursorWidth = cursorWidth
        instance.cursorHeight = cursorHeight
        instance.cursorRadius = cursorRadius
        instance.cursorColor = cursorColor
        instance.selectionColor = selectionColor
        instance.selectionHeightStyle = selectionHeightStyle
        instance.selectionWidthStyle = selectionWidthStyle
        instance.dragStartBehavior = dragStartBehavior
        instance.enableInteractiveSelection = enableInteractiveSelection
        instance.selectionControls = selectionControls
        instance.onTap = onTap
        instance.scrollPhysics = scrollPhysics
        instance.semanticsLabel = semanticsLabel
        instance.textHeightBehavior = textHeightBehavior
        instance.textWidthBasis = textWidthBasis
        instance.onSelectionChanged = onSelectionChanged
        instance.contextMenuBuilder = contextMenuBuilder
        instance.magnifierConfiguration = magnifierConfiguration
        instance.scrollBehavior = scrollBehavior
        instance.textSpan = textSpan
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.strutStyle is not None:
            result["strutStyle"] = _flut_pack_value(self.strutStyle)
        if self.textAlign is not None:
            result["textAlign"] = _flut_pack_value(self.textAlign)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        if self.textScaler is not None:
            result["textScaler"] = _flut_pack_value(self.textScaler)
        result["showCursor"] = _flut_pack_value(self.showCursor)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.minLines is not None:
            result["minLines"] = _flut_pack_value(self.minLines)
        if self.maxLines is not None:
            result["maxLines"] = _flut_pack_value(self.maxLines)
        result["cursorWidth"] = _flut_pack_value(self.cursorWidth)
        if self.cursorHeight is not None:
            result["cursorHeight"] = _flut_pack_value(self.cursorHeight)
        if self.cursorRadius is not None:
            result["cursorRadius"] = _flut_pack_value(self.cursorRadius)
        if self.cursorColor is not None:
            result["cursorColor"] = _flut_pack_value(self.cursorColor)
        if self.selectionColor is not None:
            result["selectionColor"] = _flut_pack_value(self.selectionColor)
        if self.selectionHeightStyle is not None:
            result["selectionHeightStyle"] = _flut_pack_value(self.selectionHeightStyle)
        if self.selectionWidthStyle is not None:
            result["selectionWidthStyle"] = _flut_pack_value(self.selectionWidthStyle)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        result["enableInteractiveSelection"] = _flut_pack_value(
            self.enableInteractiveSelection
        )
        if self.selectionControls is not None:
            result["selectionControls"] = _flut_pack_value(self.selectionControls)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "GestureTapCallback"
            )._flut_pack()
        if self.scrollPhysics is not None:
            result["scrollPhysics"] = _flut_pack_value(self.scrollPhysics)
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.textHeightBehavior is not None:
            result["textHeightBehavior"] = _flut_pack_value(self.textHeightBehavior)
        if self.textWidthBasis is not None:
            result["textWidthBasis"] = _flut_pack_value(self.textWidthBasis)
        if self.onSelectionChanged is not None:
            result["onSelectionChanged"] = self._register_action(
                self.onSelectionChanged, "SelectionChangedCallback"
            )._flut_pack()
        if self.contextMenuBuilder is not None:
            result["contextMenuBuilder"] = self._register_action(
                self.contextMenuBuilder, "EditableTextContextMenuBuilder"
            )._flut_pack()
        if self.magnifierConfiguration is not None:
            result["magnifierConfiguration"] = _flut_pack_value(
                self.magnifierConfiguration
            )
        if self.scrollBehavior is not None:
            result["scrollBehavior"] = _flut_pack_value(self.scrollBehavior)
        if self._flut_init is None:
            result["data"] = _flut_pack_value(self.data)
        if self._flut_init == "rich":
            result["textSpan"] = _flut_pack_value(self.textSpan)
        return result
