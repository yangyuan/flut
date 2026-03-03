from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value


class MenuStyle(FlutValueObject):
    _flut_type = "MenuStyle"

    def __init__(
        self,
        *,
        backgroundColor=None,
        shadowColor=None,
        surfaceTintColor=None,
        elevation=None,
        padding=None,
        minimumSize=None,
        fixedSize=None,
        maximumSize=None,
        side=None,
        shape=None,
        mouseCursor=None,
        visualDensity=None,
        alignment=None,
    ):
        super().__init__()
        self.backgroundColor = backgroundColor
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.elevation = elevation
        self.padding = padding
        self.minimumSize = minimumSize
        self.fixedSize = fixedSize
        self.maximumSize = maximumSize
        self.side = side
        self.shape = shape
        self.mouseCursor = mouseCursor
        self.visualDensity = visualDensity
        self.alignment = alignment

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.minimumSize is not None:
            result["minimumSize"] = _flut_pack_value(self.minimumSize)
        if self.fixedSize is not None:
            result["fixedSize"] = _flut_pack_value(self.fixedSize)
        if self.maximumSize is not None:
            result["maximumSize"] = _flut_pack_value(self.maximumSize)
        if self.side is not None:
            result["side"] = _flut_pack_value(self.side)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        return result
