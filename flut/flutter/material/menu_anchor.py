from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip, Offset
from flut.flutter.painting.basic_types import Axis
from flut.flutter.widgets.framework import Widget


class MenuBar(Widget):
    _flut_type = "MenuBar"

    def __init__(
        self,
        *,
        key=None,
        style=None,
        clipBehavior: Clip = Clip.none,
        controller=None,
        children: list,
    ):
        super().__init__(key=key)
        self.style = style
        self.clipBehavior = clipBehavior
        self.controller = controller
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["children"] = _flut_pack_value(self.children)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        return result


class MenuAnchor(Widget):
    _flut_type = "MenuAnchor"

    def __init__(
        self,
        *,
        key=None,
        controller=None,
        childFocusNode=None,
        style=None,
        alignmentOffset: Offset = Offset(),
        clipBehavior: Clip = Clip.hardEdge,
        consumeOutsideTap: bool = False,
        onOpen: Optional[Callable] = None,
        onClose: Optional[Callable] = None,
        crossAxisUnconstrained: bool = True,
        useRootOverlay: bool = False,
        menuChildren: list,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.controller = controller
        self.childFocusNode = childFocusNode
        self.style = style
        self.alignmentOffset = alignmentOffset
        self.clipBehavior = clipBehavior
        self.consumeOutsideTap = consumeOutsideTap
        self.onOpen = onOpen
        self.onClose = onClose
        self.crossAxisUnconstrained = crossAxisUnconstrained
        self.useRootOverlay = useRootOverlay
        self.menuChildren = menuChildren
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["alignmentOffset"] = _flut_pack_value(self.alignmentOffset)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["consumeOutsideTap"] = _flut_pack_value(self.consumeOutsideTap)
        result["crossAxisUnconstrained"] = _flut_pack_value(self.crossAxisUnconstrained)
        result["useRootOverlay"] = _flut_pack_value(self.useRootOverlay)
        result["menuChildren"] = _flut_pack_value(self.menuChildren)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.childFocusNode is not None:
            result["childFocusNode"] = _flut_pack_value(self.childFocusNode)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.onOpen is not None:
            result["onOpen"] = self._register_action(
                self.onOpen, "VoidCallback"
            )._flut_pack()
        if self.onClose is not None:
            result["onClose"] = self._register_action(
                self.onClose, "VoidCallback"
            )._flut_pack()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class MenuItemButton(Widget):
    _flut_type = "MenuItemButton"

    def __init__(
        self,
        *,
        key=None,
        onPressed: Optional[Callable] = None,
        onHover: Optional[Callable] = None,
        requestFocusOnHover: bool = True,
        onFocusChange: Optional[Callable] = None,
        focusNode=None,
        autofocus: bool = False,
        shortcut=None,
        semanticsLabel: Optional[str] = None,
        style=None,
        statesController=None,
        clipBehavior: Clip = Clip.none,
        leadingIcon: Optional[Widget] = None,
        trailingIcon: Optional[Widget] = None,
        closeOnActivate: bool = True,
        overflowAxis: Axis = Axis.horizontal,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onPressed = onPressed
        self.onHover = onHover
        self.requestFocusOnHover = requestFocusOnHover
        self.onFocusChange = onFocusChange
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.shortcut = shortcut
        self.semanticsLabel = semanticsLabel
        self.style = style
        self.statesController = statesController
        self.clipBehavior = clipBehavior
        self.leadingIcon = leadingIcon
        self.trailingIcon = trailingIcon
        self.closeOnActivate = closeOnActivate
        self.overflowAxis = overflowAxis
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["requestFocusOnHover"] = _flut_pack_value(self.requestFocusOnHover)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["closeOnActivate"] = _flut_pack_value(self.closeOnActivate)
        result["overflowAxis"] = _flut_pack_value(self.overflowAxis)
        if self.onPressed is not None:
            result["onPressed"] = self._register_action(
                self.onPressed, "VoidCallback"
            )._flut_pack()
        if self.onHover is not None:
            result["onHover"] = self._register_action(
                self.onHover, "ValueChanged<bool>"
            )._flut_pack()
        if self.onFocusChange is not None:
            result["onFocusChange"] = self._register_action(
                self.onFocusChange, "ValueChanged<bool>"
            )._flut_pack()
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.shortcut is not None:
            result["shortcut"] = _flut_pack_value(self.shortcut)
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.statesController is not None:
            result["statesController"] = _flut_pack_value(self.statesController)
        if self.leadingIcon is not None:
            result["leadingIcon"] = _flut_pack_value(self.leadingIcon)
        if self.trailingIcon is not None:
            result["trailingIcon"] = _flut_pack_value(self.trailingIcon)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class SubmenuButton(Widget):
    _flut_type = "SubmenuButton"

    def __init__(
        self,
        *,
        key=None,
        onHover: Optional[Callable] = None,
        onFocusChange: Optional[Callable] = None,
        onOpen: Optional[Callable] = None,
        onClose: Optional[Callable] = None,
        controller=None,
        style=None,
        menuStyle=None,
        alignmentOffset: Optional[Offset] = None,
        clipBehavior: Clip = Clip.hardEdge,
        focusNode=None,
        statesController=None,
        leadingIcon: Optional[Widget] = None,
        trailingIcon: Optional[Widget] = None,
        useRootOverlay: bool = False,
        menuChildren: list,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onHover = onHover
        self.onFocusChange = onFocusChange
        self.onOpen = onOpen
        self.onClose = onClose
        self.controller = controller
        self.style = style
        self.menuStyle = menuStyle
        self.alignmentOffset = alignmentOffset
        self.clipBehavior = clipBehavior
        self.focusNode = focusNode
        self.statesController = statesController
        self.leadingIcon = leadingIcon
        self.trailingIcon = trailingIcon
        self.useRootOverlay = useRootOverlay
        self.menuChildren = menuChildren
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["useRootOverlay"] = _flut_pack_value(self.useRootOverlay)
        result["menuChildren"] = _flut_pack_value(self.menuChildren)
        result["child"] = (
            _flut_pack_value(self.child) if self.child is not None else None
        )
        if self.onHover is not None:
            result["onHover"] = self._register_action(
                self.onHover, "ValueChanged<bool>"
            )._flut_pack()
        if self.onFocusChange is not None:
            result["onFocusChange"] = self._register_action(
                self.onFocusChange, "ValueChanged<bool>"
            )._flut_pack()
        if self.onOpen is not None:
            result["onOpen"] = self._register_action(
                self.onOpen, "VoidCallback"
            )._flut_pack()
        if self.onClose is not None:
            result["onClose"] = self._register_action(
                self.onClose, "VoidCallback"
            )._flut_pack()
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.menuStyle is not None:
            result["menuStyle"] = _flut_pack_value(self.menuStyle)
        if self.alignmentOffset is not None:
            result["alignmentOffset"] = _flut_pack_value(self.alignmentOffset)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.statesController is not None:
            result["statesController"] = _flut_pack_value(self.statesController)
        if self.leadingIcon is not None:
            result["leadingIcon"] = _flut_pack_value(self.leadingIcon)
        if self.trailingIcon is not None:
            result["trailingIcon"] = _flut_pack_value(self.trailingIcon)
        return result


class MenuAcceleratorLabel(Widget):
    _flut_type = "MenuAcceleratorLabel"

    def __init__(
        self,
        label: str,
        *,
        key=None,
    ):
        super().__init__(key=key)
        self.label = label

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["label"] = _flut_pack_value(self.label)
        return result
