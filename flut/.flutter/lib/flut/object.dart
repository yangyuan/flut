import 'package:flutter/foundation.dart';
import 'package:flut/flut/error.dart';
import 'package:flut/flut/runtime.dart';

/// Base class for pass by value objects passed between Dart and Python.
/// These are simple data carriers - no bidirectional sync needed.
///
/// Subclasses must implement:
/// - flutEncode(): Convert to JSON for Python
/// - static flutDecode(dynamic data, FlutRuntime runtime): Decode from JSON
abstract class FlutValueObject {
  final String flutType;

  const FlutValueObject(this.flutType);

  Map<String, dynamic> flutBaseProps() => {'_flut_type': flutType};

  Map<String, dynamic> flutEncode();
}

mixin FlutAbstractObject {
  FlutRuntime get runtime;
}

/// Base class for enum-like types that map string values to Dart enum values.
///
/// Subclasses provide [flutType] and [flutValueMap], and get generic
/// decode/encode for free.
///
/// Standard JSON format: {"_flut_type": "SomeEnum", "_flut_value": "someValue"}
abstract class FlutEnumObject<T> {
  final String flutType;
  final Map<String, T> flutValueMap;

  const FlutEnumObject(this.flutType, this.flutValueMap);

  T? flutDecode(Map<String, dynamic> data) {
    return flutValueMap[data['_flut_value'] as String?];
  }

  Map<String, dynamic>? flutEncode(T value) {
    for (final entry in flutValueMap.entries) {
      if (entry.value == value) {
        return {'_flut_type': flutType, '_flut_value': entry.key};
      }
    }
    return null;
  }
}

mixin FlutRealtimeObject<T extends Object> {
  late final FlutRuntime runtime;
  late final int flutOid;
  late final String flutType;
  late final T flutTarget;
  final Map<int, VoidCallback> listenersByCid = {};

  void initRealtimeFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required T target,
  }) {
    this.runtime = runtime;
    flutOid = data['_flut_oid'] as int;
    flutType = data['_flut_type'] as String;
    flutTarget = target;
  }

  void initRealtimeFromObject({
    required FlutRuntime runtime,
    required int oid,
    required String type,
    required T target,
  }) {
    this.runtime = runtime;
    flutOid = oid;
    flutType = type;
    flutTarget = target;
  }

  Map<String, dynamic> flutBaseProps() {
    return {'_flut_type': flutType, '_flut_oid': flutOid};
  }

  Map<String, dynamic> flutEncode() => flutBaseProps();

  void flutDispose() {
    runtime.signalObjectDisposed(flutOid);
  }

  dynamic getRawProperty(String property);

  dynamic getProperty(String property) {
    return runtime.encodeValue(getRawProperty(property));
  }

  bool setProperty(String property, dynamic value);
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  );

  dynamic adaptGeneric<V>() => null;
}

class FlutFuture with FlutRealtimeObject<Future<dynamic>> {
  FlutFuture._({
    required FlutRuntime runtime,
    required int oid,
    required Future<dynamic> target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'Future',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) =>
      throw FlutUnknownPropertyException('Future', property);

  @override
  bool setProperty(String property, dynamic value) =>
      throw FlutUnknownPropertyException('Future', property);

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) => throw FlutUnknownMethodException(method);

  static FlutFuture wrap(FlutRuntime runtime, Future<dynamic> future) {
    final oid = runtime.generateOid();
    final wrapper = FlutFuture._(runtime: runtime, oid: oid, target: future);
    runtime.objectRegistry[oid] = wrapper;
    future
        .then((value) {
          runtime.flutNative.invokeNativeAsync('future_complete', {
            'oid': oid,
            'value': runtime.encodeValue(value),
          });
        })
        .catchError((error) {
          runtime.flutNative.invokeNativeAsync('future_complete', {
            'oid': oid,
            'error': error.toString(),
          });
        });
    return wrapper;
  }
}

class FlutDouble {
  static dynamic encode(double value) {
    if (value == double.infinity) {
      return {'_flut_type': 'Double', 'value': 'inf'};
    }
    if (value == double.negativeInfinity) {
      return {'_flut_type': 'Double', 'value': '-inf'};
    }
    if (value.isNaN) {
      return {'_flut_type': 'Double', 'value': 'nan'};
    }
    return value;
  }

  static double decode(dynamic value) {
    if (value is Map<String, dynamic> && value['_flut_type'] == 'Double') {
      final v = value['value'];
      if (v == 'inf') return double.infinity;
      if (v == '-inf') return double.negativeInfinity;
      if (v == 'nan') return double.nan;
      return double.parse(v.toString());
    }
    return (value as num).toDouble();
  }
}
