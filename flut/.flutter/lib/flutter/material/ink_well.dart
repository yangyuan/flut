import 'package:flutter/material.dart';
import 'package:flut/flut/error.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class _FlutInteractiveInkFeatureFactory extends InteractiveInkFeatureFactory {
  @override
  InteractiveInkFeature create({
    required MaterialInkController controller,
    required RenderBox referenceBox,
    required Offset position,
    required Color color,
    required TextDirection textDirection,
    bool containedInkWell = false,
    RectCallback? rectCallback,
    BorderRadius? borderRadius,
    ShapeBorder? customBorder,
    double? radius,
    VoidCallback? onRemoved,
  }) {
    throw UnimplementedError(
      'InteractiveInkFeatureFactory.create is not implementable because InteractiveInkFeature is not tracked in flut_map.yml.',
    );
  }
}

class FlutInteractiveInkFeatureFactory
    with FlutRealtimeObject<InteractiveInkFeatureFactory> {
  FlutInteractiveInkFeatureFactory.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required InteractiveInkFeatureFactory target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutInteractiveInkFeatureFactory.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required InteractiveInkFeatureFactory target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'InteractiveInkFeatureFactory',
      target: target,
    );
  }

  static FlutInteractiveInkFeatureFactory flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutInteractiveInkFeatureFactory.createFromData(
      runtime: runtime,
      data: data,
      target: _FlutInteractiveInkFeatureFactory(),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException(
      'InteractiveInkFeatureFactory',
      property,
    );
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException(
      'InteractiveInkFeatureFactory',
      property,
    );
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    if (method == 'create') {
      throw UnimplementedError(
        'InteractiveInkFeatureFactory.create is not implementable because InteractiveInkFeature is not tracked in flut_map.yml.',
      );
    }
    throw FlutUnknownMethodException(method);
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('InkSplash.splashFactory', _inkSplashFactory);
    runtime.registerStatic('InkRipple.splashFactory', _inkRippleFactory);
    runtime.registerStatic('NoSplash.splashFactory', _noSplashFactory);
  }

  static FlutInteractiveInkFeatureFactory _inkSplashFactory(
    FlutRuntime runtime,
  ) {
    return runtime.wrapObject<FlutInteractiveInkFeatureFactory>(
      InkSplash.splashFactory,
      (oid) => FlutInteractiveInkFeatureFactory.createFromObject(
        runtime: runtime,
        oid: oid,
        target: InkSplash.splashFactory,
      ),
    );
  }

  static FlutInteractiveInkFeatureFactory _inkRippleFactory(
    FlutRuntime runtime,
  ) {
    return runtime.wrapObject<FlutInteractiveInkFeatureFactory>(
      InkRipple.splashFactory,
      (oid) => FlutInteractiveInkFeatureFactory.createFromObject(
        runtime: runtime,
        oid: oid,
        target: InkRipple.splashFactory,
      ),
    );
  }

  static FlutInteractiveInkFeatureFactory _noSplashFactory(
    FlutRuntime runtime,
  ) {
    return runtime.wrapObject<FlutInteractiveInkFeatureFactory>(
      NoSplash.splashFactory,
      (oid) => FlutInteractiveInkFeatureFactory.createFromObject(
        runtime: runtime,
        oid: oid,
        target: NoSplash.splashFactory,
      ),
    );
  }
}

class FlutInkWell {
  FlutInkWell._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return InkWell(
      key: runtime.decodeKey(data),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onDoubleTap: runtime.unpackOptionalCallback(data, 'onDoubleTap'),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      onLongPressUp: runtime.unpackOptionalCallback(data, 'onLongPressUp'),
      onTapDown: runtime.unpackOptionalCallback(data, 'onTapDown'),
      onTapUp: runtime.unpackOptionalCallback(data, 'onTapUp'),
      onTapCancel: runtime.unpackOptionalCallback(data, 'onTapCancel'),
      onSecondaryTap: runtime.unpackOptionalCallback(data, 'onSecondaryTap'),
      onSecondaryTapUp: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapUp',
      ),
      onSecondaryTapDown: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapDown',
      ),
      onSecondaryTapCancel: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapCancel',
      ),
      onHighlightChanged: runtime.unpackOptionalCallback(
        data,
        'onHighlightChanged',
      ),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      highlightColor: runtime.unpackOptionalField<Color>(
        data,
        'highlightColor',
      ),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      splashFactory: runtime.unpackOptionalField<InteractiveInkFeatureFactory>(
        data,
        'splashFactory',
      ),
      radius: runtime.unpackOptionalField<double>(data, 'radius'),
      borderRadius: runtime.unpackOptionalField<BorderRadius>(
        data,
        'borderRadius',
      ),
      customBorder: runtime.unpackOptionalField<ShapeBorder>(
        data,
        'customBorder',
      ),
      enableFeedback: runtime.unpackRequiredField<bool>(data, 'enableFeedback'),
      excludeFromSemantics: runtime.unpackRequiredField<bool>(
        data,
        'excludeFromSemantics',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      canRequestFocus: runtime.unpackRequiredField<bool>(
        data,
        'canRequestFocus',
      ),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      statesController: runtime.unpackOptionalField<WidgetStatesController>(
        data,
        'statesController',
      ),
      hoverDuration: runtime.unpackOptionalField<Duration>(
        data,
        'hoverDuration',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
