import 'package:flutter/foundation.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutListenable {
  FlutListenable._();

  static Listenable? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'merge':
        return Listenable.merge(
          runtime.unpackRequiredField<List<Listenable?>>(data, 'listenables'),
        );
      default:
        return null;
    }
  }
}

class FlutValueNotifier with FlutRealtimeObject<ValueNotifier<dynamic>> {
  FlutValueNotifier.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ValueNotifier<dynamic> target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutValueNotifier.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ValueNotifier<dynamic> target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ValueNotifier',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final value = runtime.unpackDynamicOptionalField(data, 'value');
    final notifier = ValueNotifier<dynamic>(value);
    return FlutValueNotifier.createFromData(
      runtime: runtime,
      data: data,
      target: notifier,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('ValueNotifier', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = value;
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
      case 'notifyListeners':
        // ignore: invalid_use_of_visible_for_testing_member, invalid_use_of_protected_member
        flutTarget.notifyListeners();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
