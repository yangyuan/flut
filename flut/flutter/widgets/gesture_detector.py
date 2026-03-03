from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.gestures.recognizer import DragStartBehavior

from flut.flutter.widgets.framework import Widget


class GestureDetector(Widget):
    _flut_type = "GestureDetector"

    def __init__(
        self,
        *,
        key=None,
        onTapDown: Optional[Callable] = None,
        onTapUp: Optional[Callable] = None,
        onTap=None,
        onDoubleTap=None,
        onTapCancel=None,
        onSecondaryTapDown: Optional[Callable] = None,
        onSecondaryTapUp: Optional[Callable] = None,
        onSecondaryTapCancel: Optional[Callable] = None,
        onTertiaryTapDown: Optional[Callable] = None,
        onTertiaryTapUp: Optional[Callable] = None,
        onTertiaryTapCancel: Optional[Callable] = None,
        onDoubleTapDown: Optional[Callable] = None,
        onDoubleTapCancel: Optional[Callable] = None,
        onLongPress=None,
        onLongPressStart: Optional[Callable] = None,
        onLongPressMoveUpdate: Optional[Callable] = None,
        onLongPressUp=None,
        onLongPressEnd: Optional[Callable] = None,
        onSecondaryLongPress: Optional[Callable] = None,
        onSecondaryLongPressUp: Optional[Callable] = None,
        onTertiaryLongPress: Optional[Callable] = None,
        onTertiaryLongPressUp: Optional[Callable] = None,
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
        self.onDoubleTap = onDoubleTap
        self.onTapCancel = onTapCancel
        self.onSecondaryTapDown = onSecondaryTapDown
        self.onSecondaryTapUp = onSecondaryTapUp
        self.onSecondaryTapCancel = onSecondaryTapCancel
        self.onTertiaryTapDown = onTertiaryTapDown
        self.onTertiaryTapUp = onTertiaryTapUp
        self.onTertiaryTapCancel = onTertiaryTapCancel
        self.onDoubleTapDown = onDoubleTapDown
        self.onDoubleTapCancel = onDoubleTapCancel
        self.onLongPress = onLongPress
        self.onLongPressStart = onLongPressStart
        self.onLongPressMoveUpdate = onLongPressMoveUpdate
        self.onLongPressUp = onLongPressUp
        self.onLongPressEnd = onLongPressEnd
        self.onSecondaryLongPress = onSecondaryLongPress
        self.onSecondaryLongPressUp = onSecondaryLongPressUp
        self.onTertiaryLongPress = onTertiaryLongPress
        self.onTertiaryLongPressUp = onTertiaryLongPressUp
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
        if self.onDoubleTap is not None:
            result["onDoubleTap"] = self._register_action(
                self.onDoubleTap, "GestureTapCallback"
            )._flut_pack()
        if self.onTapCancel is not None:
            result["onTapCancel"] = self._register_action(
                self.onTapCancel, "GestureTapCancelCallback"
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
        if self.onSecondaryLongPress is not None:
            result["onSecondaryLongPress"] = self._register_action(
                self.onSecondaryLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onSecondaryLongPressUp is not None:
            result["onSecondaryLongPressUp"] = self._register_action(
                self.onSecondaryLongPressUp, "GestureLongPressUpCallback"
            )._flut_pack()
        if self.onTertiaryLongPress is not None:
            result["onTertiaryLongPress"] = self._register_action(
                self.onTertiaryLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.onTertiaryLongPressUp is not None:
            result["onTertiaryLongPressUp"] = self._register_action(
                self.onTertiaryLongPressUp, "GestureLongPressUpCallback"
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
