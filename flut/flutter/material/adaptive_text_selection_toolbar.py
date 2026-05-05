from typing import Optional, override

from flut._flut.engine import _flut_pack_value, named_constructor
from flut.flutter.widgets.framework import Widget


class AdaptiveTextSelectionToolbar(Widget):
    _flut_type = "AdaptiveTextSelectionToolbar"

    def __init__(
        self,
        *,
        children: list[Widget],
        anchors: "TextSelectionToolbarAnchors",
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.children = children
        self.anchors = anchors
        self.selectableRegionState = None

    @named_constructor
    def selectableRegion(
        cls,
        *,
        selectableRegionState: "SelectableRegionState",
        key: Optional["Key"] = None,
    ) -> "AdaptiveTextSelectionToolbar":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.children = None
        instance.anchors = None
        instance.selectableRegionState = selectableRegionState
        return instance

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self._flut_init == "selectableRegion":
            result["selectableRegionState"] = _flut_pack_value(
                self.selectableRegionState
            )
        else:
            result["children"] = _flut_pack_value(self.children)
            result["anchors"] = _flut_pack_value(self.anchors)
        return result
