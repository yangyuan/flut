from typing import Callable, Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import (
    _flut_unpack_required_field,
    _flut_unpack_optional_field,
)
from flut.dart.ui import Offset
from flut.flutter.gestures.velocity_tracker import Velocity
from flut.flutter.painting.basic_types import Axis
from flut.flutter.rendering.proxy_box import HitTestBehavior
from flut.flutter.widgets.framework import Widget, BuildContext


class DraggableDetails(FlutValueObject):
    _flut_type = "DraggableDetails"

    def __init__(
        self,
        *,
        wasAccepted: bool = False,
        velocity: Velocity,
        offset: Offset,
    ):
        super().__init__()
        self.wasAccepted = wasAccepted
        self.velocity = velocity
        self.offset = offset

    @staticmethod
    def _flut_unpack(data: dict) -> "DraggableDetails":
        return DraggableDetails(
            wasAccepted=_flut_unpack_required_field(data, "wasAccepted"),
            velocity=_flut_unpack_required_field(data, "velocity"),
            offset=_flut_unpack_required_field(data, "offset"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["wasAccepted"] = _flut_pack_value(self.wasAccepted)
        result["velocity"] = _flut_pack_value(self.velocity)
        result["offset"] = _flut_pack_value(self.offset)
        return result


class DragTargetDetails(FlutValueObject):
    _flut_type = "DragTargetDetails"

    def __init__(
        self,
        *,
        data,
        offset: Offset,
    ):
        super().__init__()
        self.data = data
        self.offset = offset

    @staticmethod
    def _flut_unpack(data: dict) -> "DragTargetDetails":
        return DragTargetDetails(
            data=_flut_unpack_required_field(data, "data"),
            offset=_flut_unpack_required_field(data, "offset"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["data"] = _flut_pack_value(self.data)
        result["offset"] = _flut_pack_value(self.offset)
        return result


def wrap_drag_target_builder(builder):
    def _wrapper(context, candidate_data, rejected_data):
        built = builder(context, candidate_data, rejected_data)
        if built is not None:
            return built._flut_pack()
        return None

    return _wrapper


class Draggable(Widget):
    _flut_type = "Draggable"

    def __init__(
        self,
        *,
        key=None,
        data=None,
        axis: Optional[Axis] = None,
        childWhenDragging: Optional[Widget] = None,
        feedbackOffset: Offset = Offset(),
        affinity: Optional[Axis] = None,
        maxSimultaneousDrags: Optional[int] = None,
        onDragStarted: Optional[Callable[[], None]] = None,
        onDragUpdate=None,
        onDraggableCanceled=None,
        onDragEnd=None,
        onDragCompleted: Optional[Callable[[], None]] = None,
        ignoringFeedbackSemantics: bool = True,
        ignoringFeedbackPointer: bool = True,
        rootOverlay: bool = False,
        hitTestBehavior: HitTestBehavior = HitTestBehavior.deferToChild,
        child: Widget,
        feedback: Widget,
    ):
        super().__init__(key=key)
        self.data = data
        self.axis = axis
        self.childWhenDragging = childWhenDragging
        self.feedbackOffset = feedbackOffset
        self.affinity = affinity
        self.maxSimultaneousDrags = maxSimultaneousDrags
        self.onDragStarted = onDragStarted
        self.onDragUpdate = onDragUpdate
        self.onDraggableCanceled = onDraggableCanceled
        self.onDragEnd = onDragEnd
        self.onDragCompleted = onDragCompleted
        self.ignoringFeedbackSemantics = ignoringFeedbackSemantics
        self.ignoringFeedbackPointer = ignoringFeedbackPointer
        self.rootOverlay = rootOverlay
        self.hitTestBehavior = hitTestBehavior
        self.child = child
        self.feedback = feedback

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["feedbackOffset"] = _flut_pack_value(self.feedbackOffset)
        result["ignoringFeedbackSemantics"] = _flut_pack_value(
            self.ignoringFeedbackSemantics
        )
        result["ignoringFeedbackPointer"] = _flut_pack_value(
            self.ignoringFeedbackPointer
        )
        result["rootOverlay"] = _flut_pack_value(self.rootOverlay)
        result["hitTestBehavior"] = _flut_pack_value(self.hitTestBehavior)
        result["child"] = _flut_pack_value(self.child)
        result["feedback"] = _flut_pack_value(self.feedback)
        if self.data is not None:
            result["data"] = _flut_pack_value(self.data)
        if self.axis is not None:
            result["axis"] = _flut_pack_value(self.axis)
        if self.childWhenDragging is not None:
            result["childWhenDragging"] = _flut_pack_value(self.childWhenDragging)
        if self.affinity is not None:
            result["affinity"] = _flut_pack_value(self.affinity)
        if self.maxSimultaneousDrags is not None:
            result["maxSimultaneousDrags"] = _flut_pack_value(self.maxSimultaneousDrags)
        if self.onDragStarted is not None:
            result["onDragStarted"] = self._register_action(
                self.onDragStarted, "VoidCallback"
            )._flut_pack()
        if self.onDragUpdate is not None:
            result["onDragUpdate"] = self._register_action(
                self.onDragUpdate, "GestureDragUpdateCallback"
            )._flut_pack()
        if self.onDraggableCanceled is not None:
            result["onDraggableCanceled"] = self._register_action(
                self.onDraggableCanceled, "DraggableCanceledCallback"
            )._flut_pack()
        if self.onDragEnd is not None:
            result["onDragEnd"] = self._register_action(
                self.onDragEnd, "DragEndCallback"
            )._flut_pack()
        if self.onDragCompleted is not None:
            result["onDragCompleted"] = self._register_action(
                self.onDragCompleted, "VoidCallback"
            )._flut_pack()
        return result


class DragTarget(Widget):
    _flut_type = "DragTarget"

    def __init__(
        self,
        *,
        key=None,
        builder: Callable[[BuildContext, list, list], Widget],
        onWillAcceptWithDetails=None,
        onAcceptWithDetails=None,
        onLeave=None,
        onMove=None,
        hitTestBehavior: HitTestBehavior = HitTestBehavior.translucent,
    ):
        super().__init__(key=key)
        self.builder = builder
        self.onWillAcceptWithDetails = onWillAcceptWithDetails
        self.onAcceptWithDetails = onAcceptWithDetails
        self.onLeave = onLeave
        self.onMove = onMove
        self.hitTestBehavior = hitTestBehavior

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["builder"] = self._register_build_action(
            wrap_drag_target_builder(self.builder), "DragTargetBuilder"
        )._flut_pack()
        result["hitTestBehavior"] = _flut_pack_value(self.hitTestBehavior)
        if self.onWillAcceptWithDetails is not None:
            result["onWillAcceptWithDetails"] = self._register_action(
                self.onWillAcceptWithDetails, "DragTargetWillAcceptWithDetails"
            )._flut_pack()
        if self.onAcceptWithDetails is not None:
            result["onAcceptWithDetails"] = self._register_action(
                self.onAcceptWithDetails, "DragTargetAcceptWithDetails"
            )._flut_pack()
        if self.onLeave is not None:
            result["onLeave"] = self._register_action(
                self.onLeave, "DragTargetLeave"
            )._flut_pack()
        if self.onMove is not None:
            result["onMove"] = self._register_action(
                self.onMove, "DragTargetMove"
            )._flut_pack()
        return result
