from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.material.adaptive_text_selection_toolbar import (
    AdaptiveTextSelectionToolbar,
)
from flut.flutter.rendering.selection import SelectedContent
from flut.flutter.widgets.selectable_region import SelectableRegionState
from flut.flutter.widgets.framework import Widget


def _default_context_menu_builder(
    context: "BuildContext",
    selectableRegionState: SelectableRegionState,
) -> Widget:
    return AdaptiveTextSelectionToolbar.selectableRegion(
        selectableRegionState=selectableRegionState,
    )


class SelectionArea(Widget):
    _flut_type = "SelectionArea"

    def __init__(
        self,
        *,
        child: Widget,
        key: Optional["Key"] = None,
        focusNode: Optional["FocusNode"] = None,
        selectionControls: Optional["TextSelectionControls"] = None,
        contextMenuBuilder: Optional[
            Callable[["BuildContext", SelectableRegionState], Widget]
        ] = _default_context_menu_builder,
        magnifierConfiguration: Optional["TextMagnifierConfiguration"] = None,
        onSelectionChanged: Optional[
            Callable[[Optional[SelectedContent]], None]
        ] = None,
    ) -> None:
        super().__init__(key=key)
        self.child = child
        self.focusNode = focusNode
        self.selectionControls = selectionControls
        self.contextMenuBuilder = contextMenuBuilder
        self.magnifierConfiguration = magnifierConfiguration
        self.onSelectionChanged = onSelectionChanged

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["child"] = _flut_pack_value(self.child)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.selectionControls is not None:
            result["selectionControls"] = _flut_pack_value(self.selectionControls)
        if self.contextMenuBuilder is not None:
            result["contextMenuBuilder"] = self._register_action(
                self.contextMenuBuilder, "SelectableRegionContextMenuBuilder"
            )._flut_pack()
        if self.magnifierConfiguration is not None:
            result["magnifierConfiguration"] = _flut_pack_value(
                self.magnifierConfiguration
            )
        if self.onSelectionChanged is not None:
            result["onSelectionChanged"] = self._register_action(
                self.onSelectionChanged, "ValueChanged<SelectedContent?>"
            )._flut_pack()
        return result
