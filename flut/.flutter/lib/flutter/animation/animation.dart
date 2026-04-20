import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

class FlutAnimationStatus extends FlutEnumObject<AnimationStatus> {
  const FlutAnimationStatus()
    : super('AnimationStatus', const {
        'dismissed': AnimationStatus.dismissed,
        'forward': AnimationStatus.forward,
        'reverse': AnimationStatus.reverse,
        'completed': AnimationStatus.completed,
      });
}

class FlutAnimation<T extends Animation<dynamic>> extends FlutListenable<T> {
  final Map<int, AnimationStatusListener> statusListenersByCid = {};

  FlutAnimation.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutAnimation.createFromObject({
    required super.runtime,
    required super.oid,
    required super.type,
    required super.target,
  }) : super.createFromObject();

  void clearTrackedStatusListeners() {
    for (final cb in statusListenersByCid.values) {
      flutTarget.removeStatusListener(cb);
    }
    statusListenersByCid.clear();
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
      case 'status':
        return flutTarget.status;
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
      case 'addStatusListener':
        final cb = args[0] as AnimationStatusListener;
        flutTarget.addStatusListener(cb);
        final cid = runtime.cidForCallable(cb);
        if (cid != null) statusListenersByCid[cid] = cb;
        return null;
      case 'removeStatusListener':
        final cidArg = args[0];
        if (cidArg is int) {
          final cb = statusListenersByCid.remove(cidArg);
          if (cb != null) flutTarget.removeStatusListener(cb);
        }
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}
