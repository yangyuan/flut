import 'package:flutter/foundation.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

/// Shared base for any Flutter `Listenable` wrapped as a realtime object.
abstract class FlutListenable<T extends Listenable> with FlutRealtimeObject<T> {
  final Map<int, VoidCallback> listenersByCid = {};

  FlutListenable.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required T target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutListenable.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required String type,
    required T target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: type,
      target: target,
    );
  }

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

  void clearTrackedListeners() {
    for (final cb in listenersByCid.values) {
      flutTarget.removeListener(cb);
    }
    listenersByCid.clear();
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException(flutType, property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException(flutType, property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'addListener':
        final cb = args[0] as VoidCallback;
        flutTarget.addListener(cb);
        final cid = runtime.cidForCallable(cb);
        if (cid != null) listenersByCid[cid] = cb;
        return null;
      case 'removeListener':
        final cidArg = args[0];
        if (cidArg is int) {
          final cb = listenersByCid.remove(cidArg);
          if (cb != null) flutTarget.removeListener(cb);
        }
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}

/// Shared base for any Flutter `ChangeNotifier` wrapped as a realtime object.
class FlutChangeNotifier<T extends ChangeNotifier> extends FlutListenable<T> {
  FlutChangeNotifier.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutChangeNotifier.createFromObject({
    required super.runtime,
    required super.oid,
    required super.type,
    required super.target,
  }) : super.createFromObject();

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutChangeNotifier<ChangeNotifier>.createFromData(
      runtime: runtime,
      data: data,
      target: ChangeNotifier(),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    return super.getRawProperty(property);
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
      case 'dispose':
        clearTrackedListeners();
        flutTarget.dispose();
        flutDispose();
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}

class FlutValueNotifier extends FlutChangeNotifier<ValueNotifier<dynamic>> {
  FlutValueNotifier.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutValueNotifier.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'ValueNotifier');

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final value = runtime.unpackDynamicOptionalField(data, 'value');
    return FlutValueNotifier.createFromData(
      runtime: runtime,
      data: data,
      target: ValueNotifier<dynamic>(value),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = value;
        return true;
    }
    return super.setProperty(property, value);
  }
}
