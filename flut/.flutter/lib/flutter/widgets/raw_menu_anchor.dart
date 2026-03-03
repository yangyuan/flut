import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutMenuController with FlutRealtimeObject<MenuController> {
  FlutMenuController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required MenuController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutMenuController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required MenuController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'MenuController',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutMenuController.createFromData(
      runtime: runtime,
      data: data,
      target: MenuController(),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'isOpen':
        return flutTarget.isOpen;
    }
    throw FlutUnknownPropertyException('MenuController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('MenuController', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'open':
        final position = kwargs['position'] as Offset?;
        flutTarget.open(position: position);
        return null;
      case 'close':
        flutTarget.close();
        return null;
      case 'closeChildren':
        flutTarget.closeChildren();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
