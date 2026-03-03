import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutValueKey extends FlutValueObject {
  final ValueKey valueKey;
  const FlutValueKey(this.valueKey) : super('ValueKey');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['value'] = valueKey.value;
    return result;
  }

  static ValueKey? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ValueKey(runtime.unpackDynamicRequiredField(data, 'value'));
  }
}

class FlutUniqueKey with FlutRealtimeObject<UniqueKey> {
  FlutUniqueKey.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required UniqueKey target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  static FlutUniqueKey flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutUniqueKey.createFromData(
      runtime: runtime,
      data: data,
      target: UniqueKey(),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('UniqueKey', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('UniqueKey', property);
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
