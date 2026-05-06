from typing import Callable, Optional, override

from flut._flut.engine import (
    _flut_pack_value,
    call_dart_static,
    named_constructor,
)
from flut.flutter.rendering.selection import SelectionGeometry
from flut.flutter.widgets.context_menu_button_item import ContextMenuButtonItem
from flut.flutter.widgets.editable_text import EditableTextState
from flut.flutter.widgets.framework import BuildContext, Widget
from flut.flutter.widgets.selectable_region import SelectableRegionState
from flut.flutter.widgets.text_selection import ClipboardStatus
from flut.flutter.widgets.text_selection_toolbar_anchors import (
    TextSelectionToolbarAnchors,
)


class AdaptiveTextSelectionToolbar(Widget):
    _flut_type = "AdaptiveTextSelectionToolbar"

    def __init__(
        self,
        *,
        children: list[Widget],
        anchors: TextSelectionToolbarAnchors,
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.children: Optional[list[Widget]] = children
        self.anchors: Optional[TextSelectionToolbarAnchors] = anchors
        self.buttonItems: Optional[list[ContextMenuButtonItem]] = None
        self.clipboardStatus: Optional[ClipboardStatus] = None
        self.onCopy: Optional[Callable[[], None]] = None
        self.onCut: Optional[Callable[[], None]] = None
        self.onPaste: Optional[Callable[[], None]] = None
        self.onSelectAll: Optional[Callable[[], None]] = None
        self.onLookUp: Optional[Callable[[], None]] = None
        self.onSearchWeb: Optional[Callable[[], None]] = None
        self.onShare: Optional[Callable[[], None]] = None
        self.onLiveTextInput: Optional[Callable[[], None]] = None
        self.editableTextState: Optional[EditableTextState] = None
        self.selectionGeometry: Optional[SelectionGeometry] = None
        self.selectableRegionState: Optional[SelectableRegionState] = None

    @named_constructor
    def buttonItems(
        cls,
        *,
        buttonItems: Optional[list[ContextMenuButtonItem]],
        anchors: TextSelectionToolbarAnchors,
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = anchors
        instance.buttonItems = buttonItems
        instance.clipboardStatus = None
        instance.onCopy = None
        instance.onCut = None
        instance.onPaste = None
        instance.onSelectAll = None
        instance.onLookUp = None
        instance.onSearchWeb = None
        instance.onShare = None
        instance.onLiveTextInput = None
        instance.editableTextState = None
        instance.selectionGeometry = None
        instance.selectableRegionState = None
        return instance

    @named_constructor
    def editable(
        cls,
        *,
        clipboardStatus: ClipboardStatus,
        onCopy: Optional[Callable[[], None]],
        onCut: Optional[Callable[[], None]],
        onPaste: Optional[Callable[[], None]],
        onSelectAll: Optional[Callable[[], None]],
        onLookUp: Optional[Callable[[], None]],
        onSearchWeb: Optional[Callable[[], None]],
        onShare: Optional[Callable[[], None]],
        onLiveTextInput: Optional[Callable[[], None]],
        anchors: TextSelectionToolbarAnchors,
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = anchors
        instance.buttonItems = None
        instance.clipboardStatus = clipboardStatus
        instance.onCopy = onCopy
        instance.onCut = onCut
        instance.onPaste = onPaste
        instance.onSelectAll = onSelectAll
        instance.onLookUp = onLookUp
        instance.onSearchWeb = onSearchWeb
        instance.onShare = onShare
        instance.onLiveTextInput = onLiveTextInput
        instance.editableTextState = None
        instance.selectionGeometry = None
        instance.selectableRegionState = None
        return instance

    @named_constructor
    def editableText(
        cls,
        *,
        editableTextState: EditableTextState,
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = None
        instance.buttonItems = None
        instance.clipboardStatus = None
        instance.onCopy = None
        instance.onCut = None
        instance.onPaste = None
        instance.onSelectAll = None
        instance.onLookUp = None
        instance.onSearchWeb = None
        instance.onShare = None
        instance.onLiveTextInput = None
        instance.editableTextState = editableTextState
        instance.selectionGeometry = None
        instance.selectableRegionState = None
        return instance

    @named_constructor
    def selectable(
        cls,
        *,
        onCopy: Callable[[], None],
        onSelectAll: Callable[[], None],
        onShare: Optional[Callable[[], None]],
        selectionGeometry: SelectionGeometry,
        anchors: TextSelectionToolbarAnchors,
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = anchors
        instance.buttonItems = None
        instance.clipboardStatus = None
        instance.onCopy = onCopy
        instance.onCut = None
        instance.onPaste = None
        instance.onSelectAll = onSelectAll
        instance.onLookUp = None
        instance.onSearchWeb = None
        instance.onShare = onShare
        instance.onLiveTextInput = None
        instance.editableTextState = None
        instance.selectionGeometry = selectionGeometry
        instance.selectableRegionState = None
        return instance

    @named_constructor
    def selectableRegion(
        cls,
        *,
        selectableRegionState: SelectableRegionState,
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = None
        instance.buttonItems = None
        instance.clipboardStatus = None
        instance.onCopy = None
        instance.onCut = None
        instance.onPaste = None
        instance.onSelectAll = None
        instance.onLookUp = None
        instance.onSearchWeb = None
        instance.onShare = None
        instance.onLiveTextInput = None
        instance.editableTextState = None
        instance.selectionGeometry = None
        instance.selectableRegionState = selectableRegionState
        return instance

    @staticmethod
    def getButtonLabel(context: BuildContext, buttonItem: ContextMenuButtonItem) -> str:
        return call_dart_static(
            "AdaptiveTextSelectionToolbar",
            "getButtonLabel",
            context._flut_pack(),
            buttonItem._flut_pack(),
        )

    @staticmethod
    def getAdaptiveButtons(
        context: BuildContext, buttonItems: list[ContextMenuButtonItem]
    ) -> list[Widget]:
        return call_dart_static(
            "AdaptiveTextSelectionToolbar",
            "getAdaptiveButtons",
            context._flut_pack(),
            [item._flut_pack() for item in buttonItems],
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self._flut_init is None:
            result["children"] = _flut_pack_value(self.children)
            result["anchors"] = _flut_pack_value(self.anchors)
        elif self._flut_init == "buttonItems":
            result["buttonItems"] = (
                _flut_pack_value(self.buttonItems)
                if self.buttonItems is not None
                else None
            )
            result["anchors"] = _flut_pack_value(self.anchors)
        elif self._flut_init == "editable":
            result["clipboardStatus"] = _flut_pack_value(self.clipboardStatus)
            result["onCopy"] = (
                self._register_action(self.onCopy, "VoidCallback")._flut_pack()
                if self.onCopy is not None
                else None
            )
            result["onCut"] = (
                self._register_action(self.onCut, "VoidCallback")._flut_pack()
                if self.onCut is not None
                else None
            )
            result["onPaste"] = (
                self._register_action(self.onPaste, "VoidCallback")._flut_pack()
                if self.onPaste is not None
                else None
            )
            result["onSelectAll"] = (
                self._register_action(self.onSelectAll, "VoidCallback")._flut_pack()
                if self.onSelectAll is not None
                else None
            )
            result["onLookUp"] = (
                self._register_action(self.onLookUp, "VoidCallback")._flut_pack()
                if self.onLookUp is not None
                else None
            )
            result["onSearchWeb"] = (
                self._register_action(self.onSearchWeb, "VoidCallback")._flut_pack()
                if self.onSearchWeb is not None
                else None
            )
            result["onShare"] = (
                self._register_action(self.onShare, "VoidCallback")._flut_pack()
                if self.onShare is not None
                else None
            )
            result["onLiveTextInput"] = (
                self._register_action(self.onLiveTextInput, "VoidCallback")._flut_pack()
                if self.onLiveTextInput is not None
                else None
            )
            result["anchors"] = _flut_pack_value(self.anchors)
        elif self._flut_init == "editableText":
            result["editableTextState"] = _flut_pack_value(self.editableTextState)
        elif self._flut_init == "selectable":
            result["onCopy"] = self._register_action(
                self.onCopy, "VoidCallback"
            )._flut_pack()
            result["onSelectAll"] = self._register_action(
                self.onSelectAll, "VoidCallback"
            )._flut_pack()
            result["onShare"] = (
                self._register_action(self.onShare, "VoidCallback")._flut_pack()
                if self.onShare is not None
                else None
            )
            result["selectionGeometry"] = _flut_pack_value(self.selectionGeometry)
            result["anchors"] = _flut_pack_value(self.anchors)
        elif self._flut_init == "selectableRegion":
            result["selectableRegionState"] = _flut_pack_value(
                self.selectableRegionState
            )
        return result
