from typing import Callable, Optional, override

from flut._flut.engine import (
    FlutEnumObject,
    named_constructor,
    wrap_indexed_widget_builder,
    _flut_pack_value,
)
from flut.dart.ui import Clip
from flut.flutter.widgets.framework import Widget, BuildContext
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.painting.basic_types import Axis
from flut.flutter.rendering.proxy_box import HitTestBehavior


class ScrollViewKeyboardDismissBehavior(FlutEnumObject):
    manual: "ScrollViewKeyboardDismissBehavior"
    onDrag: "ScrollViewKeyboardDismissBehavior"


class ListView(Widget):
    _flut_type = "ListView"

    def __init__(
        self,
        *,
        key=None,
        scrollDirection: Axis = Axis.vertical,
        reverse: bool = False,
        controller=None,
        primary=None,
        physics=None,
        shrinkWrap: bool = False,
        padding=None,
        itemExtent: Optional[float] = None,
        cacheExtent: Optional[float] = None,
        dragStartBehavior=DragStartBehavior.start,
        clipBehavior=Clip.hardEdge,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.scrollDirection = scrollDirection
        self.reverse = reverse
        self.controller = controller
        self.primary = primary
        self.physics = physics
        self.shrinkWrap = shrinkWrap
        self.padding = padding
        self.itemExtent = itemExtent
        self.cacheExtent = cacheExtent
        self.dragStartBehavior = dragStartBehavior
        self.clipBehavior = clipBehavior
        self.children = children
        self.itemBuilder = None
        self.itemCount = None

    @named_constructor
    def builder(
        cls,
        *,
        key=None,
        scrollDirection: Axis = Axis.vertical,
        reverse: bool = False,
        controller=None,
        primary=None,
        shrinkWrap: bool = False,
        padding=None,
        itemExtent: Optional[float] = None,
        cacheExtent: Optional[float] = None,
        itemBuilder: Callable[[BuildContext, int], Optional[Widget]],
        itemCount: Optional[int] = None,
        dragStartBehavior=DragStartBehavior.start,
        clipBehavior=Clip.hardEdge,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.scrollDirection = scrollDirection
        instance.reverse = reverse
        instance.controller = controller
        instance.primary = primary
        instance.physics = None
        instance.shrinkWrap = shrinkWrap
        instance.padding = padding
        instance.itemExtent = itemExtent
        instance.cacheExtent = cacheExtent
        instance.children = []
        instance.itemBuilder = itemBuilder
        instance.itemCount = itemCount
        instance.dragStartBehavior = dragStartBehavior
        instance.clipBehavior = clipBehavior
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["scrollDirection"] = _flut_pack_value(self.scrollDirection)
        result["reverse"] = _flut_pack_value(self.reverse)
        result["shrinkWrap"] = _flut_pack_value(self.shrinkWrap)
        result["children"] = _flut_pack_value(self.children)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.primary is not None:
            result["primary"] = _flut_pack_value(self.primary)
        if self.physics is not None:
            result["physics"] = _flut_pack_value(self.physics)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.itemExtent is not None:
            result["itemExtent"] = _flut_pack_value(self.itemExtent)
        if self.cacheExtent is not None:
            result["cacheExtent"] = _flut_pack_value(self.cacheExtent)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self._flut_init == "builder":
            result["itemBuilder"] = self._register_build_action(
                wrap_indexed_widget_builder(self.itemBuilder),
                "NullableIndexedWidgetBuilder",
            )._flut_pack()
            if self.itemCount is not None:
                result["itemCount"] = _flut_pack_value(self.itemCount)
        return result


class CustomScrollView(Widget):
    _flut_type = "CustomScrollView"

    def __init__(
        self,
        *,
        key=None,
        scrollDirection: Axis = Axis.vertical,
        reverse: bool = False,
        controller=None,
        primary=None,
        physics=None,
        scrollBehavior=None,
        shrinkWrap: bool = False,
        center=None,
        anchor: float = 0.0,
        cacheExtent: Optional[float] = None,
        paintOrder=None,
        slivers: list[Widget] = [],
        semanticChildCount: Optional[int] = None,
        dragStartBehavior=DragStartBehavior.start,
        keyboardDismissBehavior: Optional[ScrollViewKeyboardDismissBehavior] = None,
        restorationId: Optional[str] = None,
        clipBehavior=Clip.hardEdge,
        hitTestBehavior: HitTestBehavior = HitTestBehavior.opaque,
    ):
        super().__init__(key=key)
        self.scrollDirection = scrollDirection
        self.reverse = reverse
        self.controller = controller
        self.primary = primary
        self.physics = physics
        self.scrollBehavior = scrollBehavior
        self.shrinkWrap = shrinkWrap
        self.center = center
        self.anchor = anchor
        self.cacheExtent = cacheExtent
        self.paintOrder = paintOrder
        self.slivers = slivers
        self.semanticChildCount = semanticChildCount
        self.dragStartBehavior = dragStartBehavior
        self.keyboardDismissBehavior = keyboardDismissBehavior
        self.restorationId = restorationId
        self.clipBehavior = clipBehavior
        self.hitTestBehavior = hitTestBehavior

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["scrollDirection"] = _flut_pack_value(self.scrollDirection)
        result["reverse"] = _flut_pack_value(self.reverse)
        result["shrinkWrap"] = _flut_pack_value(self.shrinkWrap)
        result["anchor"] = _flut_pack_value(self.anchor)
        result["hitTestBehavior"] = _flut_pack_value(self.hitTestBehavior)
        result["slivers"] = _flut_pack_value(self.slivers)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.primary is not None:
            result["primary"] = _flut_pack_value(self.primary)
        if self.physics is not None:
            result["physics"] = _flut_pack_value(self.physics)
        if self.cacheExtent is not None:
            result["cacheExtent"] = _flut_pack_value(self.cacheExtent)
        if self.semanticChildCount is not None:
            result["semanticChildCount"] = _flut_pack_value(self.semanticChildCount)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        if self.keyboardDismissBehavior is not None:
            result["keyboardDismissBehavior"] = _flut_pack_value(
                self.keyboardDismissBehavior
            )
        if self.restorationId is not None:
            result["restorationId"] = _flut_pack_value(self.restorationId)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.scrollBehavior is not None:
            result["scrollBehavior"] = _flut_pack_value(self.scrollBehavior)
        if self.center is not None:
            result["center"] = _flut_pack_value(self.center)
        if self.paintOrder is not None:
            result["paintOrder"] = _flut_pack_value(self.paintOrder)
        return result
