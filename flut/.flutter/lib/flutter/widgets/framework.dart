import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutBuildContext with FlutRealtimeObject<BuildContext> {
  FlutBuildContext.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required BuildContext target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'BuildContext',
      target: target,
    );
  }

  BuildContext get context => flutTarget;

  @override
  dynamic getRawProperty(String property) {
    return null;
  }

  @override
  bool setProperty(String property, dynamic value) {
    return false;
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'findRenderObject':
        final ro = flutTarget.findRenderObject();
        if (ro is RenderBox) return ro;
        return null;
    }
    return null;
  }
}

class FlutGlobalKey with FlutRealtimeObject<GlobalKey> {
  FlutGlobalKey.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required GlobalKey target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  static FlutGlobalKey flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final debugLabel = runtime.unpackOptionalField<String>(data, 'debugLabel');
    return FlutGlobalKey.createFromData(
      runtime: runtime,
      data: data,
      target: GlobalKey(debugLabel: debugLabel),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'currentContext':
        return flutTarget.currentContext;
      case 'currentState':
        final state = flutTarget.currentState;
        if (state == null) return null;
        if (state is FlutRealtimeObject) {
          return (state as FlutRealtimeObject).flutOid;
        }
        return state;
    }
    throw FlutUnknownPropertyException('GlobalKey', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('GlobalKey', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    throw FlutUnknownMethodException(method);
  }
}
