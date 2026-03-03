from typing import Optional, override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field


class ScrollDecelerationRate(FlutEnumObject):
    normal: "ScrollDecelerationRate"
    fast: "ScrollDecelerationRate"


class ScrollPhysics(FlutValueObject):
    _flut_type = "ScrollPhysics"

    def __init__(
        self,
        *,
        parent: Optional["ScrollPhysics"] = None,
    ):
        super().__init__()
        self.parent = parent

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.parent is not None:
            result["parent"] = _flut_pack_value(self.parent)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollPhysics":
        return ScrollPhysics(
            parent=_flut_unpack_optional_field(data, "parent"),
        )


class BouncingScrollPhysics(ScrollPhysics):
    _flut_type = "BouncingScrollPhysics"

    def __init__(
        self,
        *,
        decelerationRate: ScrollDecelerationRate = ScrollDecelerationRate.normal,
        parent: Optional[ScrollPhysics] = None,
    ):
        super().__init__(parent=parent)
        self.decelerationRate = decelerationRate

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["decelerationRate"] = _flut_pack_value(self.decelerationRate)
        if self.parent is not None:
            result["parent"] = _flut_pack_value(self.parent)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "BouncingScrollPhysics":
        return BouncingScrollPhysics(
            decelerationRate=_flut_unpack_optional_field(data, "decelerationRate")
            or ScrollDecelerationRate.normal,
            parent=_flut_unpack_optional_field(data, "parent"),
        )


class ClampingScrollPhysics(ScrollPhysics):
    _flut_type = "ClampingScrollPhysics"

    def __init__(
        self,
        *,
        parent: Optional[ScrollPhysics] = None,
    ):
        super().__init__(parent=parent)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.parent is not None:
            result["parent"] = _flut_pack_value(self.parent)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ClampingScrollPhysics":
        return ClampingScrollPhysics(
            parent=_flut_unpack_optional_field(data, "parent"),
        )


class NeverScrollableScrollPhysics(ScrollPhysics):
    _flut_type = "NeverScrollableScrollPhysics"

    def __init__(
        self,
        *,
        parent: Optional[ScrollPhysics] = None,
    ):
        super().__init__(parent=parent)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.parent is not None:
            result["parent"] = _flut_pack_value(self.parent)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "NeverScrollableScrollPhysics":
        return NeverScrollableScrollPhysics(
            parent=_flut_unpack_optional_field(data, "parent"),
        )


class AlwaysScrollableScrollPhysics(ScrollPhysics):
    _flut_type = "AlwaysScrollableScrollPhysics"

    def __init__(
        self,
        *,
        parent: Optional[ScrollPhysics] = None,
    ):
        super().__init__(parent=parent)

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.parent is not None:
            result["parent"] = _flut_pack_value(self.parent)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "AlwaysScrollableScrollPhysics":
        return AlwaysScrollableScrollPhysics(
            parent=_flut_unpack_optional_field(data, "parent"),
        )
