from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.flutter.widgets.scroll_metrics import ScrollMetrics
from flut.flutter.gestures.drag_details import (
    DragStartDetails,
    DragUpdateDetails,
    DragEndDetails,
)


class ScrollNotification(FlutValueObject):
    _flut_type = "ScrollNotification"

    def __init__(self, *, metrics: ScrollMetrics, depth: int = 0):
        super().__init__()
        self.metrics = metrics
        self.depth = depth

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollNotification":
        return ScrollNotification(
            metrics=_flut_unpack_required_field(data, "metrics"),
            depth=_flut_unpack_required_field(data, "depth"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["metrics"] = _flut_pack_value(self.metrics)
        result["depth"] = _flut_pack_value(self.depth)
        return result


class ScrollStartNotification(ScrollNotification):
    _flut_type = "ScrollStartNotification"

    def __init__(
        self,
        *,
        metrics: ScrollMetrics,
        depth: int = 0,
        dragDetails: Optional[DragStartDetails] = None,
    ):
        super().__init__(metrics=metrics, depth=depth)
        self.dragDetails = dragDetails

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollStartNotification":
        return ScrollStartNotification(
            metrics=_flut_unpack_required_field(data, "metrics"),
            depth=_flut_unpack_required_field(data, "depth"),
            dragDetails=_flut_unpack_optional_field(data, "dragDetails"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = super()._flut_pack()
        if self.dragDetails is not None:
            result["dragDetails"] = _flut_pack_value(self.dragDetails)
        return result


class ScrollUpdateNotification(ScrollNotification):
    _flut_type = "ScrollUpdateNotification"

    def __init__(
        self,
        *,
        metrics: ScrollMetrics,
        depth: int = 0,
        scrollDelta: Optional[float] = None,
        dragDetails: Optional[DragUpdateDetails] = None,
    ):
        super().__init__(metrics=metrics, depth=depth)
        self.scrollDelta = scrollDelta
        self.dragDetails = dragDetails

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollUpdateNotification":
        return ScrollUpdateNotification(
            metrics=_flut_unpack_required_field(data, "metrics"),
            depth=_flut_unpack_required_field(data, "depth"),
            scrollDelta=_flut_unpack_optional_field(data, "scrollDelta"),
            dragDetails=_flut_unpack_optional_field(data, "dragDetails"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = super()._flut_pack()
        if self.scrollDelta is not None:
            result["scrollDelta"] = _flut_pack_value(self.scrollDelta)
        if self.dragDetails is not None:
            result["dragDetails"] = _flut_pack_value(self.dragDetails)
        return result


class ScrollEndNotification(ScrollNotification):
    _flut_type = "ScrollEndNotification"

    def __init__(
        self,
        *,
        metrics: ScrollMetrics,
        depth: int = 0,
        dragDetails: Optional[DragEndDetails] = None,
    ):
        super().__init__(metrics=metrics, depth=depth)
        self.dragDetails = dragDetails

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollEndNotification":
        return ScrollEndNotification(
            metrics=_flut_unpack_required_field(data, "metrics"),
            depth=_flut_unpack_required_field(data, "depth"),
            dragDetails=_flut_unpack_optional_field(data, "dragDetails"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = super()._flut_pack()
        if self.dragDetails is not None:
            result["dragDetails"] = _flut_pack_value(self.dragDetails)
        return result


class OverscrollNotification(ScrollNotification):
    _flut_type = "OverscrollNotification"

    def __init__(
        self,
        *,
        metrics: ScrollMetrics,
        depth: int = 0,
        overscroll: float,
        velocity: float = 0.0,
        dragDetails: Optional[DragUpdateDetails] = None,
    ):
        super().__init__(metrics=metrics, depth=depth)
        self.overscroll = overscroll
        self.velocity = velocity
        self.dragDetails = dragDetails

    @staticmethod
    def _flut_unpack(data: dict) -> "OverscrollNotification":
        return OverscrollNotification(
            metrics=_flut_unpack_required_field(data, "metrics"),
            depth=_flut_unpack_required_field(data, "depth"),
            overscroll=_flut_unpack_required_field(data, "overscroll"),
            velocity=_flut_unpack_required_field(data, "velocity"),
            dragDetails=_flut_unpack_optional_field(data, "dragDetails"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = super()._flut_pack()
        result["overscroll"] = _flut_pack_value(self.overscroll)
        result["velocity"] = _flut_pack_value(self.velocity)
        if self.dragDetails is not None:
            result["dragDetails"] = _flut_pack_value(self.dragDetails)
        return result
