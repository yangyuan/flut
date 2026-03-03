import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutTabController with FlutRealtimeObject<TabController> {
  FlutTabController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required TabController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutTabController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required TabController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'TabController',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final controller = TabController(
      initialIndex: runtime.unpackRequiredField<int>(data, 'initialIndex'),
      animationDuration: runtime.unpackOptionalField<Duration>(
        data,
        'animationDuration',
      ),
      length: runtime.unpackRequiredField<int>(data, 'length'),
      vsync: runtime.resolveArg(data['vsync']) as TickerProvider,
    );
    return FlutTabController.createFromData(
      runtime: runtime,
      data: data,
      target: controller,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'index':
        return flutTarget.index;
      case 'length':
        return flutTarget.length;
      case 'previousIndex':
        return flutTarget.previousIndex;
      case 'indexIsChanging':
        return flutTarget.indexIsChanging;
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('TabController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'index':
        flutTarget.index = value as int;
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
      case 'animateTo':
        flutTarget.animateTo(
          args[0] as int,
          duration: kwargs['duration'] as Duration?,
          curve: kwargs['curve'] as Curve,
        );
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}

class FlutDefaultTabController {
  FlutDefaultTabController._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return DefaultTabController(
      key: runtime.decodeKey(data),
      length: runtime.unpackRequiredField<int>(data, 'length'),
      initialIndex: runtime.unpackRequiredField<int>(data, 'initialIndex'),
      animationDuration: runtime.unpackOptionalField<Duration>(
        data,
        'animationDuration',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
