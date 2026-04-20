import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

class FlutTabController extends FlutChangeNotifier<TabController> {
  FlutTabController.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutTabController.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'TabController');

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
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'index':
        flutTarget.index = value as int;
        return true;
    }
    return super.setProperty(property, value);
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
    return super.callMethod(method, args, kwargs);
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
