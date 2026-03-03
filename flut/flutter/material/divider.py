from typing import Optional, override

from flut._flut.engine import _flut_pack_value, call_dart_static
from flut.flutter.widgets.framework import Widget


class Divider(Widget):
    _flut_type = "Divider"

    def __init__(
        self,
        *,
        key=None,
        height: Optional[float] = None,
        thickness: Optional[float] = None,
        indent: Optional[float] = None,
        endIndent: Optional[float] = None,
        color=None,
        radius=None,
    ):
        super().__init__(key=key)
        self.height = height
        self.thickness = thickness
        self.indent = indent
        self.endIndent = endIndent
        self.color = color
        self.radius = radius

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.thickness is not None:
            result["thickness"] = _flut_pack_value(self.thickness)
        if self.indent is not None:
            result["indent"] = _flut_pack_value(self.indent)
        if self.endIndent is not None:
            result["endIndent"] = _flut_pack_value(self.endIndent)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.radius is not None:
            result["radius"] = _flut_pack_value(self.radius)
        return result

    @staticmethod
    def createBorderSide(context, *, color=None, width=None):
        return call_dart_static(
            "Divider",
            "createBorderSide",
            context._flut_pack() if context is not None else None,
            color=color._flut_pack() if color is not None else None,
            width=width,
        )
