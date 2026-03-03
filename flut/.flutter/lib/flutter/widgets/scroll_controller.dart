import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutScrollController with FlutRealtimeObject<ScrollController> {
  FlutScrollController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ScrollController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutScrollController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ScrollController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ScrollController',
      target: target,
    );
  }

  static FlutScrollController flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutScrollController.createFromData(
      runtime: runtime,
      data: data,
      target: ScrollController(
        initialScrollOffset: runtime.unpackRequiredField<double>(
          data,
          'initialScrollOffset',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'offset':
        return flutTarget.offset;
      case 'hasClients':
        return flutTarget.hasClients;
      case 'position':
        return flutTarget.position;
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('ScrollController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ScrollController', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'jumpTo':
        flutTarget.jumpTo((args[0] as num).toDouble());
        return null;
      case 'animateTo':
        flutTarget.animateTo(
          (args[0] as num).toDouble(),
          duration: runtime.decodeObject<Duration>(kwargs['duration'])!,
          curve: runtime.decodeObject<Curve>(kwargs['curve'])!,
        );
        return null;
      case 'notifyListeners':
        // ignore: invalid_use_of_visible_for_testing_member, invalid_use_of_protected_member
        flutTarget.notifyListeners();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
