from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Clip
from flut.flutter.widgets.framework import Widget


class Container(Widget):
    _flut_type = "Container"

    def __init__(
        self,
        *,
        key=None,
        padding=None,
        margin=None,
        color=None,
        isAntiAlias: bool = True,
        width: Optional[float] = None,
        height: Optional[float] = None,
        decoration=None,
        foregroundDecoration=None,
        constraints=None,
        alignment=None,
        transform=None,
        transformAlignment=None,
        child: Optional[Widget] = None,
        clipBehavior: Clip = Clip.none,
    ):
        super().__init__(key=key)
        self.padding = padding
        self.margin = margin
        self.color = color
        self.isAntiAlias = isAntiAlias
        self.width = width
        self.height = height
        self.decoration = decoration
        self.foregroundDecoration = foregroundDecoration
        self.constraints = constraints
        self.alignment = alignment
        self.transform = transform
        self.transformAlignment = transformAlignment
        self.child = child
        self.clipBehavior = clipBehavior

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.margin is not None:
            result["margin"] = _flut_pack_value(self.margin)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        result["isAntiAlias"] = _flut_pack_value(self.isAntiAlias)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.decoration is not None:
            result["decoration"] = _flut_pack_value(self.decoration)
        if self.foregroundDecoration is not None:
            result["foregroundDecoration"] = _flut_pack_value(self.foregroundDecoration)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.transform is not None:
            result["transform"] = _flut_pack_value(self.transform)
        if self.transformAlignment is not None:
            result["transformAlignment"] = _flut_pack_value(self.transformAlignment)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        return result
