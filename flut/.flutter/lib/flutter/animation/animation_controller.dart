import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutAnimationBehavior extends FlutEnumObject<AnimationBehavior> {
  const FlutAnimationBehavior()
    : super('AnimationBehavior', const {
        'normal': AnimationBehavior.normal,
        'preserve': AnimationBehavior.preserve,
      });
}

class FlutAnimationController with FlutRealtimeObject<AnimationController> {
  FlutAnimationController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required AnimationController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutAnimationController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required AnimationController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'AnimationController',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final vsync = runtime.resolveArg(data['vsync']);
    if (vsync is! TickerProvider) {
      throw FlutRuntimeException('vsync object is not a TickerProvider');
    }
    final controller = AnimationController(
      value: runtime.unpackOptionalField<double>(data, 'value'),
      duration: runtime.unpackOptionalField<Duration>(data, 'duration'),
      reverseDuration: runtime.unpackOptionalField<Duration>(
        data,
        'reverseDuration',
      ),
      debugLabel: runtime.unpackOptionalField<String>(data, 'debugLabel'),
      lowerBound: runtime.unpackRequiredField<double>(data, 'lowerBound'),
      upperBound: runtime.unpackRequiredField<double>(data, 'upperBound'),
      animationBehavior: runtime.unpackRequiredField<AnimationBehavior>(
        data,
        'animationBehavior',
      ),
      vsync: vsync,
    );
    return FlutAnimationController.createFromData(
      runtime: runtime,
      data: data,
      target: controller,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
      case 'status':
        return flutTarget.status;
      case 'isAnimating':
        return flutTarget.isAnimating;
      case 'duration':
        return flutTarget.duration;
      case 'reverseDuration':
        return flutTarget.reverseDuration;
    }
    throw FlutUnknownPropertyException('AnimationController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = (value as num).toDouble();
        return true;
      case 'duration':
        flutTarget.duration = value as Duration?;
        return true;
      case 'reverseDuration':
        flutTarget.reverseDuration = value as Duration?;
        return true;
    }
    return false;
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'forward':
        final from = kwargs['from_'] as double?;
        flutTarget.forward(from: from);
        return null;
      case 'reverse':
        final from = kwargs['from_'] as double?;
        flutTarget.reverse(from: from);
        return null;
      case 'repeat':
        flutTarget.repeat(
          min: kwargs['min'] as double?,
          max: kwargs['max'] as double?,
          reverse: kwargs['reverse'] as bool? ?? false,
          period: kwargs['period'] as Duration?,
        );
        return null;
      case 'stop':
        flutTarget.stop();
        return null;
      case 'reset':
        flutTarget.reset();
        return null;
      case 'animateTo':
        flutTarget.animateTo(
          (args[0] as num).toDouble(),
          duration: kwargs['duration'] as Duration?,
          curve: kwargs['curve'] as Curve? ?? Curves.linear,
        );
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
