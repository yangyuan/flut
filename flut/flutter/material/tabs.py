from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip, Color
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.widgets.framework import Widget
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.painting.edge_insets import EdgeInsets


class TabBar(Widget):
    _flut_type = "TabBar"

    def __init__(
        self,
        *,
        key=None,
        tabs: list[Widget],
        controller=None,
        isScrollable: bool = False,
        indicatorColor: Optional[Color] = None,
        dividerColor: Optional[Color] = None,
        labelColor: Optional[Color] = None,
        labelStyle: Optional[TextStyle] = None,
        unselectedLabelColor: Optional[Color] = None,
        unselectedLabelStyle: Optional[TextStyle] = None,
        labelPadding: Optional[EdgeInsets] = None,
        onTap: Optional[Callable[[int], None]] = None,
    ):
        super().__init__(key=key)
        self.tabs = tabs
        self.controller = controller
        self.isScrollable = isScrollable
        self.indicatorColor = indicatorColor
        self.dividerColor = dividerColor
        self.labelColor = labelColor
        self.labelStyle = labelStyle
        self.unselectedLabelColor = unselectedLabelColor
        self.unselectedLabelStyle = unselectedLabelStyle
        self.labelPadding = labelPadding
        self.onTap = onTap

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["tabs"] = _flut_pack_value(self.tabs)
        result["isScrollable"] = _flut_pack_value(self.isScrollable)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.indicatorColor is not None:
            result["indicatorColor"] = _flut_pack_value(self.indicatorColor)
        if self.dividerColor is not None:
            result["dividerColor"] = _flut_pack_value(self.dividerColor)
        if self.labelColor is not None:
            result["labelColor"] = _flut_pack_value(self.labelColor)
        if self.labelStyle is not None:
            result["labelStyle"] = _flut_pack_value(self.labelStyle)
        if self.unselectedLabelColor is not None:
            result["unselectedLabelColor"] = _flut_pack_value(self.unselectedLabelColor)
        if self.unselectedLabelStyle is not None:
            result["unselectedLabelStyle"] = _flut_pack_value(self.unselectedLabelStyle)
        if self.labelPadding is not None:
            result["labelPadding"] = _flut_pack_value(self.labelPadding)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "ValueChanged<int>"
            )._flut_pack()
        return result


class TabBarView(Widget):
    _flut_type = "TabBarView"

    def __init__(
        self,
        *,
        key=None,
        children: list[Widget],
        controller=None,
        physics=None,
        dragStartBehavior=DragStartBehavior.start,
        viewportFraction: float = 1.0,
        clipBehavior=Clip.hardEdge,
    ):
        super().__init__(key=key)
        self.children = children
        self.controller = controller
        self.physics = physics
        self.dragStartBehavior = dragStartBehavior
        self.viewportFraction = viewportFraction
        self.clipBehavior = clipBehavior

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["children"] = _flut_pack_value(self.children)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.physics is not None:
            result["physics"] = _flut_pack_value(self.physics)
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        result["viewportFraction"] = _flut_pack_value(self.viewportFraction)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        return result


class Tab(Widget):
    _flut_type = "Tab"

    def __init__(
        self,
        *,
        key=None,
        text: Optional[str] = None,
        icon: Optional[Widget] = None,
        iconMargin=None,
        height: Optional[float] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.text = text
        self.icon = icon
        self.iconMargin = iconMargin
        self.height = height
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.text is not None:
            result["text"] = _flut_pack_value(self.text)
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.iconMargin is not None:
            result["iconMargin"] = _flut_pack_value(self.iconMargin)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
