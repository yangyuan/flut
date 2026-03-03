import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class _FlutMaterialPageRoute extends MaterialPageRoute {
  VoidCallback? onDispose;

  _FlutMaterialPageRoute({
    required super.builder,
    super.maintainState,
    super.fullscreenDialog,
    super.settings,
  });

  @override
  void dispose() {
    onDispose?.call();
    super.dispose();
  }
}

class FlutMaterialPageRoute with FlutRealtimeObject<MaterialPageRoute> {
  FlutMaterialPageRoute.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required MaterialPageRoute target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutMaterialPageRoute.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required MaterialPageRoute target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'MaterialPageRoute',
      target: target,
    );
  }

  static FlutMaterialPageRoute flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final builderId = runtime.unpackRequiredField<int>(data, 'builder');
    final inner = _FlutMaterialPageRoute(
      builder: (context) {
        return runtime.callAction<Widget>(builderId, args: [context]) ??
            const SizedBox.shrink();
      },
      maintainState: runtime.unpackRequiredField<bool>(data, 'maintainState'),
      fullscreenDialog: runtime.unpackRequiredField<bool>(
        data,
        'fullscreenDialog',
      ),
      settings: runtime.unpackOptionalField<RouteSettings>(data, 'settings'),
    );
    final wrapper = FlutMaterialPageRoute.createFromData(
      runtime: runtime,
      data: data,
      target: inner,
    );
    inner.onDispose = wrapper.flutDispose;
    return wrapper;
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
      case 'fullscreenDialog':
        return flutTarget.fullscreenDialog;
      case 'maintainState':
        return flutTarget.maintainState;
      case 'transitionDuration':
        return flutTarget.transitionDuration;
      case 'barrierColor':
        return flutTarget.barrierColor;
      case 'barrierLabel':
        return flutTarget.barrierLabel;
    }
    throw FlutUnknownPropertyException('MaterialPageRoute', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('MaterialPageRoute', property);
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
