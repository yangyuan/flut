from typing import Callable, Optional, override

from flut._flut.engine import FlutAbstractObject, _flut_pack_value
from flut.flutter.foundation.key import Key
from flut.flutter.gestures.recognizer import DragStartBehavior, GestureRecognizer
from flut.flutter.rendering.proxy_box import HitTestBehavior
from flut.flutter.widgets.framework import Widget


class GestureRecognizerFactory(FlutAbstractObject):
    _flut_type = "GestureRecognizerFactory"

    def constructor(self) -> GestureRecognizer:
        raise NotImplementedError

    def initializer(self, instance: GestureRecognizer) -> None:
        raise NotImplementedError

    @staticmethod
    def _flut_unpack(data: dict) -> "GestureRecognizerFactory":
        raise NotImplementedError(
            "GestureRecognizerFactory has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "GestureRecognizerFactory has no concrete wire form. Pass a concrete subtype."
        )


class GestureRecognizerFactoryWithHandlers(GestureRecognizerFactory):
    _flut_type = "GestureRecognizerFactoryWithHandlers"

    def __init__(
        self,
        constructor: Callable[[], GestureRecognizer],
        initializer: Callable[[GestureRecognizer], None],
    ) -> None:
        super().__init__()
        self._constructor = constructor
        self._initializer = initializer

    def constructor(self) -> GestureRecognizer:
        return self._constructor()

    def initializer(self, instance: GestureRecognizer) -> None:
        self._initializer(instance)

    @staticmethod
    def _flut_unpack(data: dict) -> "GestureRecognizerFactoryWithHandlers":
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["constructor"] = self._register_action(
            self._constructor, "GestureRecognizerFactoryConstructor"
        )._flut_pack()
        result["initializer"] = self._register_action(
            self._initializer, "GestureRecognizerFactoryInitializer"
        )._flut_pack()
        return result


class GestureDetector(Widget):
    _flut_type = "GestureDetector"

    def __init__(
        self,
        *,
        key=None,
        onTapDown: Optional[Callable] = None,
        onTapUp: Optional[Callable] = None,
        onTap=None,
        onTapMove: Optional[Callable] = None,
        onDoubleTap=None,
        onTapCancel=None,
        onSecondaryTap=None,
        onSecondaryTapDown: Optional[Callable] = None,
        onSecondaryTapUp: Optional[Callable] = None,
        onSecondaryTapCancel: Optional[Callable] = None,
        onTertiaryTapDown: Optional[Callable] = None,
        onTertiaryTapUp: Optional[Callable] = None,
        onTertiaryTapCancel: Optional[Callable] = None,
        onDoubleTapDown: Optional[Callable] = None,
        onDoubleTapCancel: Optional[Callable] = None,
        onLongPressDown: Optional[Callable] = None,
        onLongPressCancel: Optional[Callable] = None,
        onLongPress=None,
        onLongPressStart: Optional[Callable] = None,
        onLongPressMoveUpdate: Optional[Callable] = None,
        onLongPressUp=None,
        onLongPressEnd: Optional[Callable] = None,
        onSecondaryLongPressDown: Optional[Callable] = None,
        onSecondaryLongPressCancel: Optional[Callable] = None,
        onSecondaryLongPress: Optional[Callable] = None,
        onSecondaryLongPressStart: Optional[Callable] = None,
        onSecondaryLongPressMoveUpdate: Optional[Callable] = None,
        onSecondaryLongPressUp: Optional[Callable] = None,
        onSecondaryLongPressEnd: Optional[Callable] = None,
        onTertiaryLongPressDown: Optional[Callable] = None,
        onTertiaryLongPressCancel: Optional[Callable] = None,
        onTertiaryLongPress: Optional[Callable] = None,
        onTertiaryLongPressStart: Optional[Callable] = None,
        onTertiaryLongPressMoveUpdate: Optional[Callable] = None,
        onTertiaryLongPressUp: Optional[Callable] = None,
        onTertiaryLongPressEnd: Optional[Callable] = None,
        onVerticalDragStart=None,
        onVerticalDragUpdate=None,
        onVerticalDragEnd=None,
        onHorizontalDragStart=None,
        onHorizontalDragUpdate=None,
        onHorizontalDragEnd=None,
        onPanDown: Optional[Callable] = None,
        onPanStart=None,
        onPanUpdate=None,
        onPanEnd=None,
        onPanCancel: Optional[Callable] = None,
        onScaleStart: Optional[Callable] = None,
        onScaleUpdate: Optional[Callable] = None,
        onScaleEnd: Optional[Callable] = None,
        excludeFromSemantics: bool = False,
        dragStartBehavior: DragStartBehavior = DragStartBehavior.start,
        behavior=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onTapDown = onTapDown
        self.onTapUp = onTapUp
        self.onTap = onTap
        self.onTapMove = onTapMove
        self.onDoubleTap = onDoubleTap
        self.onTapCancel = onTapCancel
        self.onSecondaryTap = onSecondaryTap
        self.onSecondaryTapDown = onSecondaryTapDown
        self.onSecondaryTapUp = onSecondaryTapUp
        self.onSecondaryTapCancel = onSecondaryTapCancel
        self.onTertiaryTapDown = onTertiaryTapDown
        self.onTertiaryTapUp = onTertiaryTapUp
        self.onTertiaryTapCancel = onTertiaryTapCancel
        self.onDoubleTapDown = onDoubleTapDown
        self.onDoubleTapCancel = onDoubleTapCancel
        self.onLongPressDown = onLongPressDown
        self.onLongPressCancel = onLongPressCancel
        self.onLongPress = onLongPress
        self.onLongPressStart = onLongPressStart
        self.onLongPressMoveUpdate = onLongPressMoveUpdate
        self.onLongPressUp = onLongPressUp
        self.onLongPressEnd = onLongPressEnd
        self.onSecondaryLongPressDown = onSecondaryLongPressDown
        self.onSecondaryLongPressCancel = onSecondaryLongPressCancel
        self.onSecondaryLongPress = onSecondaryLongPress
        self.onSecondaryLongPressStart = onSecondaryLongPressStart
        self.onSecondaryLongPressMoveUpdate = onSecondaryLongPressMoveUpdate
        self.onSecondaryLongPressUp = onSecondaryLongPressUp
        self.onSecondaryLongPressEnd = onSecondaryLongPressEnd
        self.onTertiaryLongPressDown = onTertiaryLongPressDown
        self.onTertiaryLongPressCancel = onTertiaryLongPressCancel
        self.onTertiaryLongPress = onTertiaryLongPress
        self.onTertiaryLongPressStart = onTertiaryLongPressStart
        self.onTertiaryLongPressMoveUpdate = onTertiaryLongPressMoveUpdate
        self.onTertiaryLongPressUp = onTertiaryLongPressUp
        self.onTertiaryLongPressEnd = onTertiaryLongPressEnd
        self.onVerticalDragStart = onVerticalDragStart
        self.onVerticalDragUpdate = onVerticalDragUpdate
        self.onVerticalDragEnd = onVerticalDragEnd
        self.onHorizontalDragStart = onHorizontalDragStart
        self.onHorizontalDragUpdate = onHorizontalDragUpdate
        self.onHorizontalDragEnd = onHorizontalDragEnd
        self.onPanDown = onPanDown
        self.onPanStart = onPanStart
        self.onPanUpdate = onPanUpdate
        self.onPanEnd = onPanEnd
        self.onPanCancel = onPanCancel
        self.onScaleStart = onScaleStart
        self.onScaleUpdate = onScaleUpdate
        self.onScaleEnd = onScaleEnd
        self.excludeFromSemantics = excludeFromSemantics
        self.dragStartBehavior = dragStartBehavior
        self.behavior = behavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["excludeFromSemantics"] = _flut_pack_value(self.excludeFromSemantics)
        if self.onTapDown is not None:
            result["onTapDown"] = self._register_action(
                self.onTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onTapUp is not None:
            result["onTapUp"] = self._register_action(
                self.onTapUp, "GestureTapUpCallback"
            )._flut_pack()
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "GestureTapCallback"
            )._flut_pack()
        if self.onTapMove is not None:
            result["onTapMove"] = self._register_action(
                self.onTapMove, "GestureTapMoveCallback"
            )._flut_pack()
        if self.onDoubleTap is not None:
            result["onDoubleTap"] = self._register_action(
                self.onDoubleTap, "GestureTapCallback"
            )._flut_pack()
        if self.onTapCancel is not None:
            result["onTapCancel"] = self._register_action(
                self.onTapCancel, "GestureTapCancelCallback"
            )._flut_pack()
        if self.onSecondaryTap is not None:
            result["onSecondaryTap"] = self._register_action(
                self.onSecondaryTap, "GestureTapCallback"
            )._flut_pack()
        if self.onSecondaryTapDown is not None:
            result["onSecondaryTapDown"] = self._register_action(
                self.onSecondaryTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onSecondaryTapUp is not None:
            result["onSecondaryTapUp"] = self._register_action(
                self.onSecondaryTapUp, "GestureTapUpCallback"
            )._flut_pack()
        if self.onSecondaryTapCancel is not None:
            result["onSecondaryTapCancel"] = self._register_action(
                self.onSecondaryTapCancel, "GestureTapCancelCallback"
            )._flut_pack()
        if self.onTertiaryTapDown is not None:
            result["onTertiaryTapDown"] = self._register_action(
                self.onTertiaryTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onTertiaryTapUp is not None:
            result["onTertiaryTapUp"] = self._register_action(
                self.onTertiaryTapUp, "GestureTapUpCallback"
            )._flut_pack()
        if self.onTertiaryTapCancel is not None:
            result["onTertiaryTapCancel"] = self._register_action(
                self.onTertiaryTapCancel, "GestureTapCancelCallback"
            )._flut_pack()
        if self.onDoubleTapDown is not None:
            result["onDoubleTapDown"] = self._register_action(
                self.onDoubleTapDown, "GestureTapDownCallback"
            )._flut_pack()
        if self.onDoubleTapCancel is not None:
            result["onDoubleTapCancel"] = self._register_action(
                self.onDoubleTapCancel, "GestureTapCancelCallback"
            )._flut_pack()
        if self.onLongPressDown is not None:
            result["onLongPressDown"] = self._register_action(
                self.onLongPressDown, "GestureLongPressDownCallback"
            )._flut_pack()
        if self.onLongPressCancel is not None:
            result["onLongPressCancel"] = self._register_action(
                self.onLongPressCancel, "GestureLongPressCancelCallback"
            )._flut_pack()
        if self.onLongPress is not None:
            result["onLongPress"] = self._register_action(
                self.onLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onLongPressStart is not None:
            result["onLongPressStart"] = self._register_action(
                self.onLongPressStart, "GestureLongPressStartCallback"
            )._flut_pack()
        if self.onLongPressMoveUpdate is not None:
            result["onLongPressMoveUpdate"] = self._register_action(
                self.onLongPressMoveUpdate, "GestureLongPressMoveUpdateCallback"
            )._flut_pack()
        if self.onLongPressUp is not None:
            result["onLongPressUp"] = self._register_action(
                self.onLongPressUp, "GestureLongPressUpCallback"
            )._flut_pack()
        if self.onLongPressEnd is not None:
            result["onLongPressEnd"] = self._register_action(
                self.onLongPressEnd, "GestureLongPressEndCallback"
            )._flut_pack()
        if self.onSecondaryLongPressDown is not None:
            result["onSecondaryLongPressDown"] = self._register_action(
                self.onSecondaryLongPressDown, "GestureLongPressDownCallback"
            )._flut_pack()
        if self.onSecondaryLongPressCancel is not None:
            result["onSecondaryLongPressCancel"] = self._register_action(
                self.onSecondaryLongPressCancel, "GestureLongPressCancelCallback"
            )._flut_pack()
        if self.onSecondaryLongPress is not None:
            result["onSecondaryLongPress"] = self._register_action(
                self.onSecondaryLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onSecondaryLongPressStart is not None:
            result["onSecondaryLongPressStart"] = self._register_action(
                self.onSecondaryLongPressStart, "GestureLongPressStartCallback"
            )._flut_pack()
        if self.onSecondaryLongPressMoveUpdate is not None:
            result["onSecondaryLongPressMoveUpdate"] = self._register_action(
                self.onSecondaryLongPressMoveUpdate,
                "GestureLongPressMoveUpdateCallback",
            )._flut_pack()
        if self.onSecondaryLongPressUp is not None:
            result["onSecondaryLongPressUp"] = self._register_action(
                self.onSecondaryLongPressUp, "GestureLongPressUpCallback"
            )._flut_pack()
        if self.onSecondaryLongPressEnd is not None:
            result["onSecondaryLongPressEnd"] = self._register_action(
                self.onSecondaryLongPressEnd, "GestureLongPressEndCallback"
            )._flut_pack()
        if self.onTertiaryLongPressDown is not None:
            result["onTertiaryLongPressDown"] = self._register_action(
                self.onTertiaryLongPressDown, "GestureLongPressDownCallback"
            )._flut_pack()
        if self.onTertiaryLongPressCancel is not None:
            result["onTertiaryLongPressCancel"] = self._register_action(
                self.onTertiaryLongPressCancel, "GestureLongPressCancelCallback"
            )._flut_pack()
        if self.onTertiaryLongPress is not None:
            result["onTertiaryLongPress"] = self._register_action(
                self.onTertiaryLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onTertiaryLongPressStart is not None:
            result["onTertiaryLongPressStart"] = self._register_action(
                self.onTertiaryLongPressStart, "GestureLongPressStartCallback"
            )._flut_pack()
        if self.onTertiaryLongPressMoveUpdate is not None:
            result["onTertiaryLongPressMoveUpdate"] = self._register_action(
                self.onTertiaryLongPressMoveUpdate,
                "GestureLongPressMoveUpdateCallback",
            )._flut_pack()
        if self.onTertiaryLongPressUp is not None:
            result["onTertiaryLongPressUp"] = self._register_action(
                self.onTertiaryLongPressUp, "GestureLongPressUpCallback"
            )._flut_pack()
        if self.onTertiaryLongPressEnd is not None:
            result["onTertiaryLongPressEnd"] = self._register_action(
                self.onTertiaryLongPressEnd, "GestureLongPressEndCallback"
            )._flut_pack()
        if self.onVerticalDragStart is not None:
            result["onVerticalDragStart"] = self._register_action(
                self.onVerticalDragStart, "GestureDragStartCallback"
            )._flut_pack()
        if self.onVerticalDragUpdate is not None:
            result["onVerticalDragUpdate"] = self._register_action(
                self.onVerticalDragUpdate, "GestureDragUpdateCallback"
            )._flut_pack()
        if self.onVerticalDragEnd is not None:
            result["onVerticalDragEnd"] = self._register_action(
                self.onVerticalDragEnd, "GestureDragEndCallback"
            )._flut_pack()
        if self.onHorizontalDragStart is not None:
            result["onHorizontalDragStart"] = self._register_action(
                self.onHorizontalDragStart, "GestureDragStartCallback"
            )._flut_pack()
        if self.onHorizontalDragUpdate is not None:
            result["onHorizontalDragUpdate"] = self._register_action(
                self.onHorizontalDragUpdate, "GestureDragUpdateCallback"
            )._flut_pack()
        if self.onHorizontalDragEnd is not None:
            result["onHorizontalDragEnd"] = self._register_action(
                self.onHorizontalDragEnd, "GestureDragEndCallback"
            )._flut_pack()
        if self.onPanDown is not None:
            result["onPanDown"] = self._register_action(
                self.onPanDown, "GestureDragDownCallback"
            )._flut_pack()
        if self.onPanStart is not None:
            result["onPanStart"] = self._register_action(
                self.onPanStart, "GestureDragStartCallback"
            )._flut_pack()
        if self.onPanUpdate is not None:
            result["onPanUpdate"] = self._register_action(
                self.onPanUpdate, "GestureDragUpdateCallback"
            )._flut_pack()
        if self.onPanEnd is not None:
            result["onPanEnd"] = self._register_action(
                self.onPanEnd, "GestureDragEndCallback"
            )._flut_pack()
        if self.onPanCancel is not None:
            result["onPanCancel"] = self._register_action(
                self.onPanCancel, "GestureDragCancelCallback"
            )._flut_pack()
        if self.onScaleStart is not None:
            result["onScaleStart"] = self._register_action(
                self.onScaleStart, "GestureScaleStartCallback"
            )._flut_pack()
        if self.onScaleUpdate is not None:
            result["onScaleUpdate"] = self._register_action(
                self.onScaleUpdate, "GestureScaleUpdateCallback"
            )._flut_pack()
        if self.onScaleEnd is not None:
            result["onScaleEnd"] = self._register_action(
                self.onScaleEnd, "GestureScaleEndCallback"
            )._flut_pack()
        result["dragStartBehavior"] = _flut_pack_value(self.dragStartBehavior)
        if self.behavior is not None:
            result["behavior"] = _flut_pack_value(self.behavior)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class RawGestureDetector(Widget):
    _flut_type = "RawGestureDetector"

    def __init__(
        self,
        *,
        key: Optional[Key] = None,
        child: Optional[Widget] = None,
        gestures: Optional[dict[type, "GestureRecognizerFactory"]] = None,
        behavior: Optional[HitTestBehavior] = None,
        excludeFromSemantics: bool = False,
    ) -> None:
        super().__init__(key=key)
        self.child = child
        self.gestures = gestures or {}
        self.behavior = behavior
        self.excludeFromSemantics = excludeFromSemantics

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        result["gestures"] = _flut_pack_value(list(self.gestures.values()))
        if self.behavior is not None:
            result["behavior"] = _flut_pack_value(self.behavior)
        result["excludeFromSemantics"] = _flut_pack_value(self.excludeFromSemantics)
        return result
