import 'dart:ui' show Offset, Rect;

import 'package:flutter/widgets.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flut/error.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutMagnifierController with FlutRealtimeObject<MagnifierController> {
  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic(
      'MagnifierController.shiftWithinBounds',
      _shiftWithinBounds,
    );
  }

  static Rect _shiftWithinBounds(FlutRuntime runtime, Rect rect, Rect bounds) {
    return MagnifierController.shiftWithinBounds(rect: rect, bounds: bounds);
  }

  FlutMagnifierController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required MagnifierController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutMagnifierController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required MagnifierController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'MagnifierController',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutMagnifierController.createFromData(
      runtime: runtime,
      data: data,
      target: MagnifierController(
        animationController: runtime.unpackOptionalField<AnimationController>(
          data,
          'animationController',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'animationController':
        return flutTarget.animationController;
      case 'overlayEntry':
        return flutTarget.overlayEntry;
      case 'shown':
        return flutTarget.shown;
    }
    throw FlutUnknownPropertyException(flutType, property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'animationController':
        flutTarget.animationController = value as AnimationController?;
        return true;
    }
    throw FlutUnknownPropertyException(flutType, property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'show':
        flutTarget.show(
          context: kwargs['context'] as BuildContext,
          builder: kwargs['builder'] as WidgetBuilder,
          debugRequiredFor: kwargs['debugRequiredFor'] as Widget?,
          below: kwargs['below'] as OverlayEntry?,
        );
        return null;
      case 'hide':
        flutTarget.hide(
          removeFromOverlay: kwargs['removeFromOverlay'] as bool? ?? true,
        );
        return null;
      case 'removeFromOverlay':
        // ignore: invalid_use_of_visible_for_testing_member
        flutTarget.removeFromOverlay();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}

class FlutMagnifierInfo extends FlutValueObject {
  final MagnifierInfo info;

  const FlutMagnifierInfo(this.info) : super('MagnifierInfo');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalGesturePosition'] = FlutOffset(
      info.globalGesturePosition,
    ).flutEncode();
    result['caretRect'] = FlutRect(info.caretRect).flutEncode();
    result['fieldBounds'] = FlutRect(info.fieldBounds).flutEncode();
    result['currentLineBoundaries'] = FlutRect(
      info.currentLineBoundaries,
    ).flutEncode();
    return result;
  }

  static MagnifierInfo? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return MagnifierInfo(
      globalGesturePosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalGesturePosition',
      ),
      caretRect: runtime.unpackRequiredField<Rect>(data, 'caretRect'),
      fieldBounds: runtime.unpackRequiredField<Rect>(data, 'fieldBounds'),
      currentLineBoundaries: runtime.unpackRequiredField<Rect>(
        data,
        'currentLineBoundaries',
      ),
    );
  }
}

class FlutTextMagnifierConfiguration extends FlutValueObject {
  final TextMagnifierConfiguration configuration;

  const FlutTextMagnifierConfiguration(this.configuration)
    : super('TextMagnifierConfiguration');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['shouldDisplayHandlesInMagnifier'] =
        configuration.shouldDisplayHandlesInMagnifier;
    return result;
  }

  static TextMagnifierConfiguration? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextMagnifierConfiguration(
      magnifierBuilder: runtime.unpackOptionalCallback(
        data,
        'magnifierBuilder',
      ),
      shouldDisplayHandlesInMagnifier: runtime.unpackRequiredField<bool>(
        data,
        'shouldDisplayHandlesInMagnifier',
      ),
    );
  }
}
