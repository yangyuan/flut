import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutExpansibleController with FlutRealtimeObject<ExpansibleController> {
  FlutExpansibleController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ExpansibleController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutExpansibleController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ExpansibleController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ExpansibleController',
      target: target,
    );
  }

  static FlutExpansibleController flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutExpansibleController.createFromData(
      runtime: runtime,
      data: data,
      target: ExpansibleController(),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('ExpansibleController.of', of);
    runtime.registerStatic('ExpansibleController.maybeOf', maybeOf);
  }

  static dynamic of(FlutRuntime runtime, BuildContext context) {
    return ExpansibleController.of(context);
  }

  static dynamic maybeOf(FlutRuntime runtime, BuildContext context) {
    return ExpansibleController.maybeOf(context);
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'isExpanded':
        return flutTarget.isExpanded;
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('ExpansibleController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ExpansibleController', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'expand':
        flutTarget.expand();
        return null;
      case 'collapse':
        flutTarget.collapse();
        return null;
      case 'notifyListeners':
        // ignore: invalid_use_of_visible_for_testing_member, invalid_use_of_protected_member
        flutTarget.notifyListeners();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
