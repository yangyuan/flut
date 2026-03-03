import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutGestureDetector {
  FlutGestureDetector._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return GestureDetector(
      key: runtime.decodeKey(data),
      onTapDown: runtime.unpackOptionalCallback(data, 'onTapDown'),
      onTapUp: runtime.unpackOptionalCallback(data, 'onTapUp'),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onDoubleTap: runtime.unpackOptionalCallback(data, 'onDoubleTap'),
      onTapCancel: runtime.unpackOptionalCallback(data, 'onTapCancel'),
      onSecondaryTapDown: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapDown',
      ),
      onSecondaryTapUp: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapUp',
      ),
      onSecondaryTapCancel: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapCancel',
      ),
      onTertiaryTapDown: runtime.unpackOptionalCallback(
        data,
        'onTertiaryTapDown',
      ),
      onTertiaryTapUp: runtime.unpackOptionalCallback(data, 'onTertiaryTapUp'),
      onTertiaryTapCancel: runtime.unpackOptionalCallback(
        data,
        'onTertiaryTapCancel',
      ),
      onDoubleTapDown: runtime.unpackOptionalCallback(data, 'onDoubleTapDown'),
      onDoubleTapCancel: runtime.unpackOptionalCallback(
        data,
        'onDoubleTapCancel',
      ),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      onLongPressStart: runtime.unpackOptionalCallback(
        data,
        'onLongPressStart',
      ),
      onLongPressMoveUpdate: runtime.unpackOptionalCallback(
        data,
        'onLongPressMoveUpdate',
      ),
      onLongPressUp: runtime.unpackOptionalCallback(data, 'onLongPressUp'),
      onLongPressEnd: runtime.unpackOptionalCallback(data, 'onLongPressEnd'),
      onSecondaryLongPress: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPress',
      ),
      onSecondaryLongPressUp: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressUp',
      ),
      onTertiaryLongPress: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPress',
      ),
      onTertiaryLongPressUp: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressUp',
      ),
      onVerticalDragStart: runtime.unpackOptionalCallback(
        data,
        'onVerticalDragStart',
      ),
      onVerticalDragUpdate: runtime.unpackOptionalCallback(
        data,
        'onVerticalDragUpdate',
      ),
      onVerticalDragEnd: runtime.unpackOptionalCallback(
        data,
        'onVerticalDragEnd',
      ),
      onHorizontalDragStart: runtime.unpackOptionalCallback(
        data,
        'onHorizontalDragStart',
      ),
      onHorizontalDragUpdate: runtime.unpackOptionalCallback(
        data,
        'onHorizontalDragUpdate',
      ),
      onHorizontalDragEnd: runtime.unpackOptionalCallback(
        data,
        'onHorizontalDragEnd',
      ),
      onPanDown: runtime.unpackOptionalCallback(data, 'onPanDown'),
      onPanStart: runtime.unpackOptionalCallback(data, 'onPanStart'),
      onPanUpdate: runtime.unpackOptionalCallback(data, 'onPanUpdate'),
      onPanEnd: runtime.unpackOptionalCallback(data, 'onPanEnd'),
      onPanCancel: runtime.unpackOptionalCallback(data, 'onPanCancel'),
      onScaleStart: runtime.unpackOptionalCallback(data, 'onScaleStart'),
      onScaleUpdate: runtime.unpackOptionalCallback(data, 'onScaleUpdate'),
      onScaleEnd: runtime.unpackOptionalCallback(data, 'onScaleEnd'),
      excludeFromSemantics: runtime.unpackRequiredField<bool>(
        data,
        'excludeFromSemantics',
      ),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      behavior: runtime.unpackOptionalField<HitTestBehavior>(data, 'behavior'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
