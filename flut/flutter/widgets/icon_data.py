from typing import Optional, override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class IconData(FlutValueObject):
    _flut_type = "IconData"

    def __init__(
        self,
        codePoint: int,
        *,
        fontFamily: Optional[str] = None,
        fontPackage: Optional[str] = None,
        matchTextDirection: bool = False,
        fontFamilyFallback: Optional[list[str]] = None,
    ):
        super().__init__()
        self.codePoint = codePoint
        self.fontFamily = fontFamily
        self.fontPackage = fontPackage
        self.matchTextDirection = matchTextDirection
        self.fontFamilyFallback = fontFamilyFallback

    @staticmethod
    def _flut_unpack(data: dict) -> "IconData":
        return IconData(
            codePoint=_flut_unpack_required_field(data, "codePoint"),
            fontFamily=_flut_unpack_optional_field(data, "fontFamily"),
            fontPackage=_flut_unpack_optional_field(data, "fontPackage"),
            matchTextDirection=_flut_unpack_required_field(data, "matchTextDirection"),
            fontFamilyFallback=_flut_unpack_optional_field(data, "fontFamilyFallback"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["codePoint"] = _flut_pack_value(self.codePoint)
        result["matchTextDirection"] = _flut_pack_value(self.matchTextDirection)
        if self.fontFamily is not None:
            result["fontFamily"] = _flut_pack_value(self.fontFamily)
        if self.fontPackage is not None:
            result["fontPackage"] = _flut_pack_value(self.fontPackage)
        if self.fontFamilyFallback is not None:
            result["fontFamilyFallback"] = _flut_pack_value(self.fontFamilyFallback)
        return result
