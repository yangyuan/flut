import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutGestureDetector {
  FlutGestureDetector._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return GestureDetector(
      key: runtime.decodeKey(data),
      onTapDown: runtime.unpackOptionalCallback(data, 'onTapDown'),
      onTapUp: runtime.unpackOptionalCallback(data, 'onTapUp'),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onTapMove: runtime.unpackOptionalCallback(data, 'onTapMove'),
      onDoubleTap: runtime.unpackOptionalCallback(data, 'onDoubleTap'),
      onTapCancel: runtime.unpackOptionalCallback(data, 'onTapCancel'),
      onSecondaryTap: runtime.unpackOptionalCallback(data, 'onSecondaryTap'),
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
      onLongPressDown: runtime.unpackOptionalCallback(data, 'onLongPressDown'),
      onLongPressCancel: runtime.unpackOptionalCallback(
        data,
        'onLongPressCancel',
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
      onSecondaryLongPressDown: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressDown',
      ),
      onSecondaryLongPressCancel: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressCancel',
      ),
      onSecondaryLongPress: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPress',
      ),
      onSecondaryLongPressStart: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressStart',
      ),
      onSecondaryLongPressMoveUpdate: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressMoveUpdate',
      ),
      onSecondaryLongPressUp: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressUp',
      ),
      onSecondaryLongPressEnd: runtime.unpackOptionalCallback(
        data,
        'onSecondaryLongPressEnd',
      ),
      onTertiaryLongPressDown: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressDown',
      ),
      onTertiaryLongPressCancel: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressCancel',
      ),
      onTertiaryLongPress: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPress',
      ),
      onTertiaryLongPressStart: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressStart',
      ),
      onTertiaryLongPressMoveUpdate: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressMoveUpdate',
      ),
      onTertiaryLongPressUp: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressUp',
      ),
      onTertiaryLongPressEnd: runtime.unpackOptionalCallback(
        data,
        'onTertiaryLongPressEnd',
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

class FlutGestureRecognizerFactory
    extends GestureRecognizerFactory<GestureRecognizer>
    with FlutAbstractObject {
  @override
  final FlutRuntime runtime;

  FlutGestureRecognizerFactory._(this.runtime);

  @override
  GestureRecognizer constructor() => throw UnimplementedError(
    'GestureRecognizerFactory has no concrete wire form. Pass a concrete subtype.',
  );

  @override
  void initializer(GestureRecognizer instance) => throw UnimplementedError(
    'GestureRecognizerFactory has no concrete wire form. Pass a concrete subtype.',
  );

  static GestureRecognizerFactory? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'GestureRecognizerFactory has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutGestureRecognizerFactoryWithHandlers {
  FlutGestureRecognizerFactoryWithHandlers._();

  static GestureRecognizerFactory? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return GestureRecognizerFactoryWithHandlers<GestureRecognizer>(
      runtime.unpackRequiredCallback(data, 'constructor'),
      runtime.unpackRequiredCallback(data, 'initializer'),
    );
  }
}

class FlutRawGestureDetector {
  FlutRawGestureDetector._();

  static RawGestureDetector? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return RawGestureDetector(
      key: runtime.decodeKey(data),
      gestures: runtime
          .unpackRequiredField<Map<Type, GestureRecognizerFactory>>(
            data,
            'gestures',
          ),
      behavior: runtime.unpackOptionalField<HitTestBehavior>(data, 'behavior'),
      excludeFromSemantics: runtime.unpackRequiredField<bool>(
        data,
        'excludeFromSemantics',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
