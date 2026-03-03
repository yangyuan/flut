from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field


class ScrollMetrics(FlutValueObject):
    _flut_type = "ScrollMetrics"

    def __init__(
        self,
        *,
        pixels: float,
        minScrollExtent: float,
        maxScrollExtent: float,
        viewportDimension: float,
        axisDirection,
    ):
        super().__init__()
        self.pixels = pixels
        self.minScrollExtent = minScrollExtent
        self.maxScrollExtent = maxScrollExtent
        self.viewportDimension = viewportDimension
        self.axisDirection = axisDirection

    @property
    def atEdge(self) -> bool:
        return (
            self.pixels == self.minScrollExtent or self.pixels == self.maxScrollExtent
        )

    @property
    def outOfRange(self) -> bool:
        return self.pixels < self.minScrollExtent or self.pixels > self.maxScrollExtent

    @property
    def extentBefore(self) -> float:
        return max(self.pixels - self.minScrollExtent, 0.0)

    @property
    def extentAfter(self) -> float:
        return max(self.maxScrollExtent - self.pixels, 0.0)

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollMetrics":
        return ScrollMetrics(
            pixels=_flut_unpack_required_field(data, "pixels"),
            minScrollExtent=_flut_unpack_required_field(data, "minScrollExtent"),
            maxScrollExtent=_flut_unpack_required_field(data, "maxScrollExtent"),
            viewportDimension=_flut_unpack_required_field(data, "viewportDimension"),
            axisDirection=_flut_unpack_required_field(data, "axisDirection"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["pixels"] = _flut_pack_value(self.pixels)
        result["minScrollExtent"] = _flut_pack_value(self.minScrollExtent)
        result["maxScrollExtent"] = _flut_pack_value(self.maxScrollExtent)
        result["viewportDimension"] = _flut_pack_value(self.viewportDimension)
        result["axisDirection"] = _flut_pack_value(self.axisDirection)
        return result
