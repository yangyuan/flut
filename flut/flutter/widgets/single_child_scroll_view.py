from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.painting import Axis
from flut.flutter.rendering.proxy_box import HitTestBehavior
from flut.flutter.widgets.scroll_view import ScrollViewKeyboardDismissBehavior

from flut.flutter.widgets.framework import Widget


class SingleChildScrollView(Widget):
    _flut_type = "SingleChildScrollView"

    def __init__(
        self,
        *,
        key=None,
        scrollDirection: Axis = Axis.vertical,
        reverse: bool = False,
        padding=None,
        primary: Optional[bool] = None,
        physics=None,
        controller=None,
        dragStartBehavior: DragStartBehavior = DragStartBehavior.start,
        clipBehavior: Clip = Clip.hardEdge,
        hitTestBehavior: HitTestBehavior = HitTestBehavior.opaque,
        restorationId: Optional[str] = None,
        keyboardDismissBehavior: Optional[ScrollViewKeyboardDismissBehavior] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.scrollDirection = scrollDirection
        self.reverse = reverse
        self.padding = padding
        self.primary = primary
        self.physics = physics
        self.controller = controller
        self.dragStartBehavior = dragStartBehavior
        self.clipBehavior = clipBehavior
        self.hitTestBehavior = hitTestBehavior
        self.restorationId = restorationId
        self.keyboardDismissBehavior = keyboardDismissBehavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["scrollDirection"] = _flut_pack_value(self.scrollDirection)
        result["reverse"] = _flut_pack_value(self.reverse)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["hitTestBehavior"] = _flut_pack_value(self.hitTestBehavior)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.primary is not None:
            result["primary"] = _flut_pack_value(self.primary)
        if self.physics is not None:
            result["physics"] = _flut_pack_value(self.physics)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.restorationId is not None:
            result["restorationId"] = _flut_pack_value(self.restorationId)
        if self.keyboardDismissBehavior is not None:
            result["keyboardDismissBehavior"] = _flut_pack_value(
                self.keyboardDismissBehavior
            )
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
