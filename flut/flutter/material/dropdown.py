from typing import Callable, Generic, Optional, TypeVar, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.painting.alignment import Alignment, AlignmentDirectional
from flut.flutter.painting.border_radius import BorderRadius
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.widgets.focus_manager import FocusNode
from flut.flutter.widgets.framework import Widget

T = TypeVar("T")


class DropdownMenuItem(Widget, Generic[T]):
    _flut_type = "DropdownMenuItem"

    def __init__(
        self,
        *,
        key=None,
        onTap: Optional[Callable[[], None]] = None,
        value: Optional[T] = None,
        enabled: bool = True,
        alignment=AlignmentDirectional.centerStart,
        child: Widget,
    ):
        super().__init__(key=key)
        self.onTap = onTap
        self.value = value
        self.enabled = enabled
        self.alignment = alignment
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["enabled"] = _flut_pack_value(self.enabled)
        result["child"] = _flut_pack_value(self.child)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "VoidCallback"
            )._flut_pack()
        if self.value is not None:
            result["value"] = _flut_pack_value(self.value)
        result["alignment"] = _flut_pack_value(self.alignment)
        return result


class DropdownButton(Widget, Generic[T]):
    _flut_type = "DropdownButton"

    def __init__(
        self,
        *,
        key=None,
        items: Optional[list[DropdownMenuItem[T]]] = None,
        value: Optional[T] = None,
        hint: Optional[Widget] = None,
        disabledHint: Optional[Widget] = None,
        onChanged: Optional[Callable[[Optional[T]], None]] = None,
        onTap: Optional[Callable[[], None]] = None,
        selectedItemBuilder: Optional[Callable] = None,
        elevation: int = 8,
        style: Optional[TextStyle] = None,
        underline: Optional[Widget] = None,
        icon: Optional[Widget] = None,
        iconDisabledColor: Optional[Color] = None,
        iconEnabledColor: Optional[Color] = None,
        iconSize: float = 24.0,
        isDense: bool = False,
        isExpanded: bool = False,
        itemHeight: Optional[float] = None,
        menuWidth: Optional[float] = None,
        focusColor: Optional[Color] = None,
        focusNode: Optional[FocusNode] = None,
        autofocus: bool = False,
        dropdownColor: Optional[Color] = None,
        menuMaxHeight: Optional[float] = None,
        enableFeedback: Optional[bool] = None,
        alignment=AlignmentDirectional.centerStart,
        borderRadius: Optional[BorderRadius] = None,
        padding: Optional[EdgeInsets] = None,
        barrierDismissible: bool = True,
        mouseCursor=None,
        dropdownMenuItemMouseCursor=None,
    ):
        super().__init__(key=key)
        self.items = items
        self.value = value
        self.hint = hint
        self.disabledHint = disabledHint
        self.onChanged = onChanged
        self.onTap = onTap
        self.selectedItemBuilder = selectedItemBuilder
        self.elevation = elevation
        self.style = style
        self.underline = underline
        self.icon = icon
        self.iconDisabledColor = iconDisabledColor
        self.iconEnabledColor = iconEnabledColor
        self.iconSize = iconSize
        self.isDense = isDense
        self.isExpanded = isExpanded
        self.itemHeight = itemHeight
        self.menuWidth = menuWidth
        self.focusColor = focusColor
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.dropdownColor = dropdownColor
        self.menuMaxHeight = menuMaxHeight
        self.enableFeedback = enableFeedback
        self.alignment = alignment
        self.borderRadius = borderRadius
        self.padding = padding
        self.barrierDismissible = barrierDismissible
        self.mouseCursor = mouseCursor
        self.dropdownMenuItemMouseCursor = dropdownMenuItemMouseCursor

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["items"] = _flut_pack_value(self.items)
        result["onChanged"] = (
            self._register_action(self.onChanged, "ValueChanged<dynamic?>")._flut_pack()
            if self.onChanged is not None
            else None
        )
        result["elevation"] = _flut_pack_value(self.elevation)
        result["iconSize"] = _flut_pack_value(self.iconSize)
        result["isDense"] = _flut_pack_value(self.isDense)
        result["isExpanded"] = _flut_pack_value(self.isExpanded)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        result["barrierDismissible"] = _flut_pack_value(self.barrierDismissible)
        if self.value is not None:
            result["value"] = _flut_pack_value(self.value)
        if self.hint is not None:
            result["hint"] = _flut_pack_value(self.hint)
        if self.disabledHint is not None:
            result["disabledHint"] = _flut_pack_value(self.disabledHint)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "VoidCallback"
            )._flut_pack()
        if self.selectedItemBuilder is not None:
            result["selectedItemBuilder"] = self._register_action(
                self.selectedItemBuilder, "DropdownButtonBuilder"
            )._flut_pack()
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.underline is not None:
            result["underline"] = _flut_pack_value(self.underline)
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.iconDisabledColor is not None:
            result["iconDisabledColor"] = _flut_pack_value(self.iconDisabledColor)
        if self.iconEnabledColor is not None:
            result["iconEnabledColor"] = _flut_pack_value(self.iconEnabledColor)
        if self.menuWidth is not None:
            result["menuWidth"] = _flut_pack_value(self.menuWidth)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.dropdownColor is not None:
            result["dropdownColor"] = _flut_pack_value(self.dropdownColor)
        if self.menuMaxHeight is not None:
            result["menuMaxHeight"] = _flut_pack_value(self.menuMaxHeight)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        result["alignment"] = _flut_pack_value(self.alignment)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.itemHeight is not None:
            result["itemHeight"] = _flut_pack_value(self.itemHeight)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.dropdownMenuItemMouseCursor is not None:
            result["dropdownMenuItemMouseCursor"] = _flut_pack_value(
                self.dropdownMenuItemMouseCursor
            )
        return result
