from typing import Optional, override

from flut._flut.engine import _flut_pack_value

from flut.dart.ui import Radius
from flut.flutter.widgets.framework import Widget
from flut.flutter.widgets.scroll_controller import ScrollController
from flut.flutter.widgets.scrollbar import ScrollbarOrientation


class Scrollbar(Widget):
    _flut_type = "Scrollbar"

    def __init__(
        self,
        *,
        key=None,
        child: Widget,
        controller: Optional[ScrollController] = None,
        thumbVisibility: Optional[bool] = None,
        trackVisibility: Optional[bool] = None,
        thickness: Optional[float] = None,
        radius: Optional[Radius] = None,
        interactive: Optional[bool] = None,
        scrollbarOrientation: Optional[ScrollbarOrientation] = None,
    ):
        super().__init__(key=key)
        self.child = child
        self.controller = controller
        self.thumbVisibility = thumbVisibility
        self.trackVisibility = trackVisibility
        self.thickness = thickness
        self.radius = radius
        self.interactive = interactive
        self.scrollbarOrientation = scrollbarOrientation

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["child"] = _flut_pack_value(self.child)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.thumbVisibility is not None:
            result["thumbVisibility"] = _flut_pack_value(self.thumbVisibility)
        if self.trackVisibility is not None:
            result["trackVisibility"] = _flut_pack_value(self.trackVisibility)
        if self.thickness is not None:
            result["thickness"] = _flut_pack_value(self.thickness)
        if self.radius is not None:
            result["radius"] = _flut_pack_value(self.radius)
        if self.interactive is not None:
            result["interactive"] = _flut_pack_value(self.interactive)
        if self.scrollbarOrientation is not None:
            result["scrollbarOrientation"] = _flut_pack_value(self.scrollbarOrientation)
        return result
