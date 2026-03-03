import 'package:flutter/scheduler.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutSchedulerBinding with FlutRealtimeObject<SchedulerBinding> {
  FlutSchedulerBinding.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required SchedulerBinding target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'SchedulerBinding',
      target: target,
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('SchedulerBinding.instance', instance);
  }

  static FlutSchedulerBinding instance(FlutRuntime runtime) {
    final binding = SchedulerBinding.instance;
    return runtime.wrapObject<FlutSchedulerBinding>(
      binding,
      (oid) => FlutSchedulerBinding.createFromObject(
        runtime: runtime,
        oid: oid,
        target: binding,
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('SchedulerBinding', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('SchedulerBinding', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'addPostFrameCallback':
        final callbackId = kwargs['callbackId'] as int;
        final debugLabel = kwargs['debugLabel'] as String? ?? 'callback';
        flutTarget.addPostFrameCallback((_) {
          runtime.callAction(callbackId);
        }, debugLabel: debugLabel);
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
