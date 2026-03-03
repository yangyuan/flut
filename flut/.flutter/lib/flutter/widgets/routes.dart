import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutModalRoute with FlutRealtimeObject<ModalRoute> {
  FlutModalRoute.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ModalRoute target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ModalRoute',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'isCurrent':
        return flutTarget.isCurrent;
      case 'isActive':
        return flutTarget.isActive;
      case 'settings':
        return flutTarget.settings;
      case 'canPop':
        return flutTarget.canPop;
      case 'transitionDuration':
        return flutTarget.transitionDuration;
      case 'barrierColor':
        return flutTarget.barrierColor;
      case 'barrierLabel':
        return flutTarget.barrierLabel;
    }
    throw FlutUnknownPropertyException('ModalRoute', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ModalRoute', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    throw FlutUnknownMethodException(method);
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('ModalRoute.of', _of);
  }

  static dynamic _of(FlutRuntime runtime, BuildContext context) {
    return ModalRoute.of(context);
  }
}
