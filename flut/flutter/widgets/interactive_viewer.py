from typing import Callable, Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.dart.ui import Clip
from flut.flutter.foundation.change_notifier import Listenable, ValueNotifier
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.widgets.framework import Widget


class PanAxis(FlutEnumObject):
    horizontal: "PanAxis"
    vertical: "PanAxis"
    aligned: "PanAxis"
    free: "PanAxis"


class InteractiveViewer(Widget):
    _flut_type = "InteractiveViewer"

    def __init__(
        self,
        *,
        key=None,
        clipBehavior=Clip.hardEdge,
        panAxis: PanAxis = PanAxis.free,
        boundaryMargin=EdgeInsets.zero,
        constrained: bool = True,
        maxScale: float = 2.5,
        minScale: float = 0.8,
        interactionEndFrictionCoefficient: float = 0.0000135,
        onInteractionEnd: Optional[Callable] = None,
        onInteractionStart: Optional[Callable] = None,
        onInteractionUpdate: Optional[Callable] = None,
        panEnabled: bool = True,
        scaleEnabled: bool = True,
        scaleFactor: float = 200.0,
        transformationController: Optional["TransformationController"] = None,
        trackpadScrollCausesScale: bool = False,
        alignment=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.clipBehavior = clipBehavior
        self.panAxis = panAxis
        self.boundaryMargin = boundaryMargin
        self.constrained = constrained
        self.maxScale = maxScale
        self.minScale = minScale
        self.interactionEndFrictionCoefficient = interactionEndFrictionCoefficient
        self.onInteractionEnd = onInteractionEnd
        self.onInteractionStart = onInteractionStart
        self.onInteractionUpdate = onInteractionUpdate
        self.panEnabled = panEnabled
        self.scaleEnabled = scaleEnabled
        self.scaleFactor = scaleFactor
        self.transformationController = transformationController
        self.trackpadScrollCausesScale = trackpadScrollCausesScale
        self.alignment = alignment
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["panAxis"] = _flut_pack_value(self.panAxis)
        result["constrained"] = _flut_pack_value(self.constrained)
        result["maxScale"] = _flut_pack_value(self.maxScale)
        result["minScale"] = _flut_pack_value(self.minScale)
        result["interactionEndFrictionCoefficient"] = _flut_pack_value(
            self.interactionEndFrictionCoefficient
        )
        result["panEnabled"] = _flut_pack_value(self.panEnabled)
        result["scaleEnabled"] = _flut_pack_value(self.scaleEnabled)
        result["scaleFactor"] = _flut_pack_value(self.scaleFactor)
        result["trackpadScrollCausesScale"] = _flut_pack_value(
            self.trackpadScrollCausesScale
        )
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["boundaryMargin"] = _flut_pack_value(self.boundaryMargin)
        if self.onInteractionEnd is not None:
            result["onInteractionEnd"] = self._register_action(
                self.onInteractionEnd, "GestureScaleEndCallback"
            )._flut_pack()
        if self.onInteractionStart is not None:
            result["onInteractionStart"] = self._register_action(
                self.onInteractionStart, "GestureScaleStartCallback"
            )._flut_pack()
        if self.onInteractionUpdate is not None:
            result["onInteractionUpdate"] = self._register_action(
                self.onInteractionUpdate, "GestureScaleUpdateCallback"
            )._flut_pack()
        if self.transformationController is not None:
            result["transformationController"] = _flut_pack_value(
                self.transformationController
            )
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class TransformationController(ValueNotifier):
    _flut_type = "TransformationController"

    def __init__(self, value=None):
        props = {}
        if value is not None:
            props["value"] = _flut_pack_value(value)
        self._flut_init_props = props
        Listenable.__init__(self)

    def toScene(self, viewportPoint):
        return self._flut_call("toScene", viewportPoint._flut_pack())
