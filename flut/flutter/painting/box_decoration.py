from typing import Optional, override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from .box_border import BoxShape


class BoxDecoration(FlutValueObject):
    _flut_type = "BoxDecoration"

    def __init__(
        self,
        *,
        color=None,
        image=None,
        border=None,
        borderRadius=None,
        boxShadow: Optional[list] = None,
        gradient=None,
        backgroundBlendMode=None,
        shape: BoxShape = BoxShape.rectangle,
    ):
        super().__init__()
        self.color = color
        self.image = image
        self.border = border
        self.borderRadius = borderRadius
        self.boxShadow = boxShadow
        self.gradient = gradient
        self.backgroundBlendMode = backgroundBlendMode
        self.shape = shape

    @staticmethod
    def _flut_unpack(data: dict) -> "BoxDecoration":
        return BoxDecoration(
            color=_flut_unpack_optional_field(data, "color"),
            image=_flut_unpack_optional_field(data, "image"),
            border=_flut_unpack_optional_field(data, "border"),
            borderRadius=_flut_unpack_optional_field(data, "borderRadius"),
            boxShadow=_flut_unpack_optional_field(data, "boxShadow"),
            gradient=_flut_unpack_optional_field(data, "gradient"),
            backgroundBlendMode=_flut_unpack_optional_field(
                data, "backgroundBlendMode"
            ),
            shape=_flut_unpack_required_field(data, "shape"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.image is not None:
            result["image"] = _flut_pack_value(self.image)
        if self.border is not None:
            result["border"] = _flut_pack_value(self.border)
        if self.borderRadius is not None:
            result["borderRadius"] = _flut_pack_value(self.borderRadius)
        if self.boxShadow is not None:
            result["boxShadow"] = _flut_pack_value(self.boxShadow)
        if self.gradient is not None:
            result["gradient"] = _flut_pack_value(self.gradient)
        if self.backgroundBlendMode is not None:
            result["backgroundBlendMode"] = _flut_pack_value(self.backgroundBlendMode)
        result["shape"] = _flut_pack_value(self.shape)
        return result
