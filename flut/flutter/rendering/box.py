from typing import Optional, override

from flut._flut.engine import FlutValueObject, FlutRealtimeObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.dart.ui import Offset, Size


class BoxConstraints(FlutValueObject):
    _flut_type = "BoxConstraints"

    def __init__(
        self,
        *,
        minWidth: float = 0.0,
        maxWidth: float = float("inf"),
        minHeight: float = 0.0,
        maxHeight: float = float("inf"),
    ):
        super().__init__()
        self.minWidth = minWidth
        self.maxWidth = maxWidth
        self.minHeight = minHeight
        self.maxHeight = maxHeight

    @staticmethod
    def tight(size: Size) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=size.width,
            maxWidth=size.width,
            minHeight=size.height,
            maxHeight=size.height,
        )

    @staticmethod
    def loose(size: Size) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=0.0,
            maxWidth=size.width,
            minHeight=0.0,
            maxHeight=size.height,
        )

    @staticmethod
    def tightFor(
        *, width: Optional[float] = None, height: Optional[float] = None
    ) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=width if width is not None else 0.0,
            maxWidth=width if width is not None else float("inf"),
            minHeight=height if height is not None else 0.0,
            maxHeight=height if height is not None else float("inf"),
        )

    @staticmethod
    def tightForFinite(
        *, width: float = float("inf"), height: float = float("inf")
    ) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=width if width != float("inf") else 0.0,
            maxWidth=width if width != float("inf") else float("inf"),
            minHeight=height if height != float("inf") else 0.0,
            maxHeight=height if height != float("inf") else float("inf"),
        )

    @staticmethod
    def expand(
        *, width: Optional[float] = None, height: Optional[float] = None
    ) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=width if width is not None else float("inf"),
            maxWidth=width if width is not None else float("inf"),
            minHeight=height if height is not None else float("inf"),
            maxHeight=height if height is not None else float("inf"),
        )

    @property
    def biggest(self) -> Size:
        return Size(self.maxWidth, self.maxHeight)

    @property
    def smallest(self) -> Size:
        return Size(self.minWidth, self.minHeight)

    @property
    def hasBoundedWidth(self) -> bool:
        return self.maxWidth < float("inf")

    @property
    def hasBoundedHeight(self) -> bool:
        return self.maxHeight < float("inf")

    @property
    def hasInfiniteWidth(self) -> bool:
        return self.minWidth >= float("inf")

    @property
    def hasInfiniteHeight(self) -> bool:
        return self.minHeight >= float("inf")

    @property
    def hasTightWidth(self) -> bool:
        return self.minWidth >= self.maxWidth

    @property
    def hasTightHeight(self) -> bool:
        return self.minHeight >= self.maxHeight

    @property
    def isTight(self) -> bool:
        return self.hasTightWidth and self.hasTightHeight

    @property
    def isNormalized(self) -> bool:
        return (
            self.minWidth >= 0.0
            and self.minWidth <= self.maxWidth
            and self.minHeight >= 0.0
            and self.minHeight <= self.maxHeight
        )

    @property
    def flipped(self) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=self.minHeight,
            maxWidth=self.maxHeight,
            minHeight=self.minWidth,
            maxHeight=self.maxWidth,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "BoxConstraints":
        return BoxConstraints(
            minWidth=_flut_unpack_required_field(data, "minWidth"),
            maxWidth=_flut_unpack_required_field(data, "maxWidth"),
            minHeight=_flut_unpack_required_field(data, "minHeight"),
            maxHeight=_flut_unpack_required_field(data, "maxHeight"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["minWidth"] = _flut_pack_value(self.minWidth)
        result["maxWidth"] = _flut_pack_value(self.maxWidth)
        result["minHeight"] = _flut_pack_value(self.minHeight)
        result["maxHeight"] = _flut_pack_value(self.maxHeight)
        return result


class RenderBox(FlutRealtimeObject):
    _flut_type = "RenderBox"

    @property
    def size(self) -> Size:
        return self._flut_get("size")

    @size.setter
    def size(self, value: Size):
        self._flut_set("size", value._flut_pack() if value is not None else None)

    @property
    def hasSize(self) -> bool:
        return self._flut_get("hasSize")

    @property
    def paintBounds(self):
        return self._flut_get("paintBounds")

    @property
    def constraints(self):
        return self._flut_get("constraints")

    def localToGlobal(self, point: Offset, *, ancestor=None) -> Offset:
        kwargs = {}
        if ancestor is not None:
            kwargs["ancestor"] = ancestor._flut_pack()
        return self._flut_call("localToGlobal", point._flut_pack(), **kwargs)

    def globalToLocal(self, point: Offset, *, ancestor=None) -> Offset:
        kwargs = {}
        if ancestor is not None:
            kwargs["ancestor"] = ancestor._flut_pack()
        return self._flut_call("globalToLocal", point._flut_pack(), **kwargs)
