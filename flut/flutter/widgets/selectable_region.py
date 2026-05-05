from typing import Callable, Optional, override

from flut.flutter.rendering.selection import SelectedContent

from flut._flut.engine import FlutEnumObject, FlutRealtimeObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget
from flut.flutter.widgets.magnifier import TextMagnifierConfiguration


class SelectableRegionSelectionStatus(FlutEnumObject):
    changing: "SelectableRegionSelectionStatus"
    finalized: "SelectableRegionSelectionStatus"


class SelectableRegionState(FlutRealtimeObject):
    _flut_type = "SelectableRegionState"


class SelectableRegion(Widget):
    _flut_type = "SelectableRegion"

    def __init__(
        self,
        *,
        selectionControls: "TextSelectionControls",
        child: Widget,
        key: Optional["Key"] = None,
        contextMenuBuilder: Optional[
            Callable[["BuildContext", SelectableRegionState], Widget]
        ] = None,
        focusNode: Optional["FocusNode"] = None,
        magnifierConfiguration: TextMagnifierConfiguration = TextMagnifierConfiguration.disabled,
        onSelectionChanged: Optional[
            Callable[[Optional[SelectedContent]], None]
        ] = None,
    ) -> None:
        super().__init__(key=key)
        self.selectionControls = selectionControls
        self.child = child
        self.contextMenuBuilder = contextMenuBuilder
        self.focusNode = focusNode
        self.magnifierConfiguration = magnifierConfiguration
        self.onSelectionChanged = onSelectionChanged

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["selectionControls"] = _flut_pack_value(self.selectionControls)
        result["child"] = _flut_pack_value(self.child)
        if self.contextMenuBuilder is not None:
            result["contextMenuBuilder"] = self._register_action(
                self.contextMenuBuilder, "SelectableRegionContextMenuBuilder"
            )._flut_pack()
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        result["magnifierConfiguration"] = _flut_pack_value(self.magnifierConfiguration)
        if self.onSelectionChanged is not None:
            result["onSelectionChanged"] = self._register_action(
                self.onSelectionChanged, "ValueChanged<SelectedContent?>"
            )._flut_pack()
        return result
