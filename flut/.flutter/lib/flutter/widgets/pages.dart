import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class _FlutPageRoute extends PageRoute<dynamic> {
  final FlutRuntime _runtime;
  final int? builderId;
  final bool _maintainState;
  VoidCallback? onDispose;

  _FlutPageRoute({
    required FlutRuntime runtime,
    this.builderId,
    bool maintainState = true,
    super.fullscreenDialog,
    super.settings,
  }) : _runtime = runtime,
       _maintainState = maintainState;

  @override
  bool get maintainState => _maintainState;

  @override
  Duration get transitionDuration => const Duration(milliseconds: 300);

  @override
  Color? get barrierColor => null;

  @override
  String? get barrierLabel => null;

  @override
  Widget buildPage(
    BuildContext context,
    Animation<double> animation,
    Animation<double> secondaryAnimation,
  ) {
    if (builderId == null) return const SizedBox.shrink();
    return _runtime.callAction<Widget>(builderId!, args: [context]) ??
        const SizedBox.shrink();
  }

  @override
  void dispose() {
    onDispose?.call();
    super.dispose();
  }
}

class FlutPageRoute with FlutRealtimeObject<PageRoute<dynamic>> {
  FlutPageRoute.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required PageRoute<dynamic> target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutPageRoute.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required PageRoute<dynamic> target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'PageRoute',
      target: target,
    );
  }

  static FlutPageRoute flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final inner = _FlutPageRoute(
      runtime: runtime,
      builderId: runtime.unpackOptionalField<int>(data, 'builder'),
      maintainState: runtime.unpackRequiredField<bool>(data, 'maintainState'),
      fullscreenDialog: runtime.unpackRequiredField<bool>(
        data,
        'fullscreenDialog',
      ),
      settings: runtime.unpackOptionalField<RouteSettings>(data, 'settings'),
    );
    final wrapper = FlutPageRoute.createFromData(
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
    throw FlutUnknownPropertyException('PageRoute', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('PageRoute', property);
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
