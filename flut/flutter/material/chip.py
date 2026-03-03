from typing import Callable, Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field
from flut.dart.ui import Clip, Color
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.widgets.framework import Widget


class Chip(Widget):
    _flut_type = "Chip"

    def __init__(
        self,
        *,
        key=None,
        avatar: Optional[Widget] = None,
        label: Widget,
        labelStyle: Optional[TextStyle] = None,
        labelPadding: Optional[EdgeInsets] = None,
        deleteIcon: Optional[Widget] = None,
        onDeleted: Optional[Callable[[], None]] = None,
        deleteIconColor: Optional[Color] = None,
        deleteButtonTooltipMessage: Optional[str] = None,
        side=None,
        shape=None,
        clipBehavior: Clip = Clip.none,
        focusNode=None,
        autofocus: bool = False,
        color=None,
        backgroundColor: Optional[Color] = None,
        padding: Optional[EdgeInsets] = None,
        visualDensity=None,
        materialTapTargetSize=None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        iconTheme=None,
        avatarBoxConstraints=None,
        deleteIconBoxConstraints=None,
        chipAnimationStyle=None,
        mouseCursor=None,
    ):
        super().__init__(key=key)
        self.avatar = avatar
        self.label = label
        self.labelStyle = labelStyle
        self.labelPadding = labelPadding
        self.deleteIcon = deleteIcon
        self.onDeleted = onDeleted
        self.deleteIconColor = deleteIconColor
        self.deleteButtonTooltipMessage = deleteButtonTooltipMessage
        self.side = side
        self.shape = shape
        self.clipBehavior = clipBehavior
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.color = color
        self.backgroundColor = backgroundColor
        self.padding = padding
        self.visualDensity = visualDensity
        self.materialTapTargetSize = materialTapTargetSize
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.iconTheme = iconTheme
        self.avatarBoxConstraints = avatarBoxConstraints
        self.deleteIconBoxConstraints = deleteIconBoxConstraints
        self.chipAnimationStyle = chipAnimationStyle
        self.mouseCursor = mouseCursor

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["label"] = _flut_pack_value(self.label)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.avatar is not None:
            result["avatar"] = _flut_pack_value(self.avatar)
        if self.labelStyle is not None:
            result["labelStyle"] = _flut_pack_value(self.labelStyle)
        if self.labelPadding is not None:
            result["labelPadding"] = _flut_pack_value(self.labelPadding)
        if self.deleteIcon is not None:
            result["deleteIcon"] = _flut_pack_value(self.deleteIcon)
        if self.onDeleted is not None:
            result["onDeleted"] = self._register_action(
                self.onDeleted, "VoidCallback"
            )._flut_pack()
        if self.deleteIconColor is not None:
            result["deleteIconColor"] = _flut_pack_value(self.deleteIconColor)
        if self.deleteButtonTooltipMessage is not None:
            result["deleteButtonTooltipMessage"] = _flut_pack_value(
                self.deleteButtonTooltipMessage
            )
        if self.side is not None:
            result["side"] = _flut_pack_value(self.side)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        if self.materialTapTargetSize is not None:
            result["materialTapTargetSize"] = _flut_pack_value(
                self.materialTapTargetSize
            )
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.iconTheme is not None:
            result["iconTheme"] = _flut_pack_value(self.iconTheme)
        if self.avatarBoxConstraints is not None:
            result["avatarBoxConstraints"] = _flut_pack_value(self.avatarBoxConstraints)
        if self.deleteIconBoxConstraints is not None:
            result["deleteIconBoxConstraints"] = _flut_pack_value(
                self.deleteIconBoxConstraints
            )
        if self.chipAnimationStyle is not None:
            result["chipAnimationStyle"] = _flut_pack_value(self.chipAnimationStyle)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        return result


class ChipAnimationStyle(FlutValueObject):
    _flut_type = "ChipAnimationStyle"

    def __init__(
        self,
        *,
        enableAnimation=None,
        selectAnimation=None,
        avatarDrawerAnimation=None,
        deleteDrawerAnimation=None,
    ):
        super().__init__()
        self.enableAnimation = enableAnimation
        self.selectAnimation = selectAnimation
        self.avatarDrawerAnimation = avatarDrawerAnimation
        self.deleteDrawerAnimation = deleteDrawerAnimation

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.enableAnimation is not None:
            result["enableAnimation"] = _flut_pack_value(self.enableAnimation)
        if self.selectAnimation is not None:
            result["selectAnimation"] = _flut_pack_value(self.selectAnimation)
        if self.avatarDrawerAnimation is not None:
            result["avatarDrawerAnimation"] = _flut_pack_value(
                self.avatarDrawerAnimation
            )
        if self.deleteDrawerAnimation is not None:
            result["deleteDrawerAnimation"] = _flut_pack_value(
                self.deleteDrawerAnimation
            )
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ChipAnimationStyle":
        return ChipAnimationStyle(
            enableAnimation=_flut_unpack_optional_field(data, "enableAnimation"),
            selectAnimation=_flut_unpack_optional_field(data, "selectAnimation"),
            avatarDrawerAnimation=_flut_unpack_optional_field(
                data, "avatarDrawerAnimation"
            ),
            deleteDrawerAnimation=_flut_unpack_optional_field(
                data, "deleteDrawerAnimation"
            ),
        )
