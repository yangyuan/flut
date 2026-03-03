from typing import Callable, Generic, Optional, TypeVar, override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.dart.ui import TextAlign
from flut.flutter.material.button_style import ButtonStyle
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.widgets.editable_text import TextEditingController
from flut.flutter.widgets.focus_manager import FocusNode
from flut.flutter.widgets.framework import Widget

T = TypeVar("T")


class DropdownMenuEntry(FlutValueObject, Generic[T]):
    _flut_type = "DropdownMenuEntry"

    def __init__(
        self,
        *,
        value: T,
        label: str,
        labelWidget: Optional[Widget] = None,
        leadingIcon: Optional[Widget] = None,
        trailingIcon: Optional[Widget] = None,
        enabled: bool = True,
        style: Optional[ButtonStyle] = None,
    ):
        super().__init__()
        self.value = value
        self.label = label
        self.labelWidget = labelWidget
        self.leadingIcon = leadingIcon
        self.trailingIcon = trailingIcon
        self.enabled = enabled
        self.style = style

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        result["label"] = _flut_pack_value(self.label)
        result["enabled"] = _flut_pack_value(self.enabled)
        if self.labelWidget is not None:
            result["labelWidget"] = _flut_pack_value(self.labelWidget)
        if self.leadingIcon is not None:
            result["leadingIcon"] = _flut_pack_value(self.leadingIcon)
        if self.trailingIcon is not None:
            result["trailingIcon"] = _flut_pack_value(self.trailingIcon)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "DropdownMenuEntry":
        return DropdownMenuEntry(
            value=_flut_unpack_required_field(data, "value"),
            label=_flut_unpack_required_field(data, "label"),
            labelWidget=_flut_unpack_optional_field(data, "labelWidget"),
            leadingIcon=_flut_unpack_optional_field(data, "leadingIcon"),
            trailingIcon=_flut_unpack_optional_field(data, "trailingIcon"),
            enabled=_flut_unpack_required_field(data, "enabled"),
            style=_flut_unpack_optional_field(data, "style"),
        )


class DropdownMenuCloseBehavior(FlutEnumObject):
    all: "DropdownMenuCloseBehavior"
    self: "DropdownMenuCloseBehavior"
    none: "DropdownMenuCloseBehavior"


class DropdownMenu(Widget, Generic[T]):
    _flut_type = "DropdownMenu"

    def __init__(
        self,
        *,
        key=None,
        enabled: bool = True,
        width: Optional[float] = None,
        menuHeight: Optional[float] = None,
        leadingIcon: Optional[Widget] = None,
        trailingIcon: Optional[Widget] = None,
        showTrailingIcon: bool = True,
        trailingIconFocusNode: Optional[FocusNode] = None,
        label: Optional[Widget] = None,
        hintText: Optional[str] = None,
        helperText: Optional[str] = None,
        errorText: Optional[str] = None,
        selectedTrailingIcon: Optional[Widget] = None,
        enableFilter: bool = False,
        enableSearch: bool = True,
        keyboardType=None,
        textStyle: Optional[TextStyle] = None,
        textAlign: TextAlign = TextAlign.start,
        inputDecorationTheme=None,
        menuStyle=None,
        controller: Optional[TextEditingController] = None,
        initialSelection: Optional[T] = None,
        onSelected: Optional[Callable[[Optional[T]], None]] = None,
        focusNode: Optional[FocusNode] = None,
        requestFocusOnTap: Optional[bool] = None,
        selectOnly: bool = False,
        expandedInsets: Optional[EdgeInsets] = None,
        alignmentOffset=None,
        dropdownMenuEntries: list[DropdownMenuEntry[T]],
        inputFormatters=None,
        closeBehavior=DropdownMenuCloseBehavior.all,
        maxLines: Optional[int] = 1,
        textInputAction=None,
        cursorHeight: Optional[float] = None,
        restorationId: Optional[str] = None,
        decorationBuilder=None,
        filterCallback=None,
        searchCallback=None,
        menuController=None,
    ):
        super().__init__(key=key)
        self.enabled = enabled
        self.width = width
        self.menuHeight = menuHeight
        self.leadingIcon = leadingIcon
        self.trailingIcon = trailingIcon
        self.showTrailingIcon = showTrailingIcon
        self.trailingIconFocusNode = trailingIconFocusNode
        self.label = label
        self.hintText = hintText
        self.helperText = helperText
        self.errorText = errorText
        self.selectedTrailingIcon = selectedTrailingIcon
        self.enableFilter = enableFilter
        self.enableSearch = enableSearch
        self.keyboardType = keyboardType
        self.textStyle = textStyle
        self.textAlign = textAlign
        self.inputDecorationTheme = inputDecorationTheme
        self.menuStyle = menuStyle
        self.controller = controller
        self.initialSelection = initialSelection
        self.onSelected = onSelected
        self.focusNode = focusNode
        self.requestFocusOnTap = requestFocusOnTap
        self.selectOnly = selectOnly
        self.expandedInsets = expandedInsets
        self.alignmentOffset = alignmentOffset
        self.dropdownMenuEntries = dropdownMenuEntries
        self.inputFormatters = inputFormatters
        self.closeBehavior = closeBehavior
        self.maxLines = maxLines
        self.textInputAction = textInputAction
        self.cursorHeight = cursorHeight
        self.restorationId = restorationId
        self.menuController = menuController
        self.decorationBuilder = decorationBuilder
        self.filterCallback = filterCallback
        self.searchCallback = searchCallback

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["enabled"] = _flut_pack_value(self.enabled)
        result["showTrailingIcon"] = _flut_pack_value(self.showTrailingIcon)
        result["enableFilter"] = _flut_pack_value(self.enableFilter)
        result["enableSearch"] = _flut_pack_value(self.enableSearch)
        result["textAlign"] = _flut_pack_value(self.textAlign)
        result["selectOnly"] = _flut_pack_value(self.selectOnly)
        result["closeBehavior"] = _flut_pack_value(self.closeBehavior)
        result["dropdownMenuEntries"] = _flut_pack_value(self.dropdownMenuEntries)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.menuHeight is not None:
            result["menuHeight"] = _flut_pack_value(self.menuHeight)
        if self.leadingIcon is not None:
            result["leadingIcon"] = _flut_pack_value(self.leadingIcon)
        if self.trailingIcon is not None:
            result["trailingIcon"] = _flut_pack_value(self.trailingIcon)
        if self.trailingIconFocusNode is not None:
            result["trailingIconFocusNode"] = _flut_pack_value(
                self.trailingIconFocusNode
            )
        if self.label is not None:
            result["label"] = _flut_pack_value(self.label)
        if self.hintText is not None:
            result["hintText"] = _flut_pack_value(self.hintText)
        if self.helperText is not None:
            result["helperText"] = _flut_pack_value(self.helperText)
        if self.errorText is not None:
            result["errorText"] = _flut_pack_value(self.errorText)
        if self.selectedTrailingIcon is not None:
            result["selectedTrailingIcon"] = _flut_pack_value(self.selectedTrailingIcon)
        if self.keyboardType is not None:
            result["keyboardType"] = _flut_pack_value(self.keyboardType)
        if self.textStyle is not None:
            result["textStyle"] = _flut_pack_value(self.textStyle)
        if self.inputDecorationTheme is not None:
            result["inputDecorationTheme"] = _flut_pack_value(self.inputDecorationTheme)
        if self.menuStyle is not None:
            result["menuStyle"] = _flut_pack_value(self.menuStyle)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.initialSelection is not None:
            result["initialSelection"] = _flut_pack_value(self.initialSelection)
        if self.onSelected is not None:
            result["onSelected"] = self._register_action(
                self.onSelected, "ValueChanged<dynamic?>"
            )._flut_pack()
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.requestFocusOnTap is not None:
            result["requestFocusOnTap"] = _flut_pack_value(self.requestFocusOnTap)
        if self.expandedInsets is not None:
            result["expandedInsets"] = _flut_pack_value(self.expandedInsets)
        if self.alignmentOffset is not None:
            result["alignmentOffset"] = _flut_pack_value(self.alignmentOffset)
        if self.inputFormatters is not None:
            result["inputFormatters"] = _flut_pack_value(self.inputFormatters)
        if self.maxLines is not None:
            result["maxLines"] = _flut_pack_value(self.maxLines)
        if self.textInputAction is not None:
            result["textInputAction"] = _flut_pack_value(self.textInputAction)
        if self.cursorHeight is not None:
            result["cursorHeight"] = _flut_pack_value(self.cursorHeight)
        if self.restorationId is not None:
            result["restorationId"] = _flut_pack_value(self.restorationId)
        if self.menuController is not None:
            result["menuController"] = _flut_pack_value(self.menuController)
        if self.decorationBuilder is not None:
            result["decorationBuilder"] = self._register_action(
                self.decorationBuilder, "DropdownMenuDecorationBuilder"
            )._flut_pack()
        if self.filterCallback is not None:
            result["filterCallback"] = self._register_action(
                self.filterCallback, "FilterCallback"
            )._flut_pack()
        if self.searchCallback is not None:
            result["searchCallback"] = self._register_action(
                self.searchCallback, "SearchCallback"
            )._flut_pack()
        return result
