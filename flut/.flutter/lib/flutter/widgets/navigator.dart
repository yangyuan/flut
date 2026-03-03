import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutRouteSettings extends FlutValueObject {
  final RouteSettings settings;
  const FlutRouteSettings(this.settings) : super('RouteSettings');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (settings.name != null) result['name'] = settings.name;
    if (settings.arguments != null) result['arguments'] = settings.arguments;
    return result;
  }

  static RouteSettings? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return RouteSettings(
      name: runtime.unpackOptionalField<String>(data, 'name'),
      arguments: runtime.unpackOptionalField<Object>(data, 'arguments'),
    );
  }
}

class FlutNavigator {
  FlutNavigator._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Navigator.push', _push);
    runtime.registerStatic('Navigator.pop', _pop);
    runtime.registerStatic('Navigator.canPop', _canPop);
    runtime.registerStatic('Navigator.pushReplacement', _pushReplacement);
  }

  static dynamic _push(FlutRuntime runtime, BuildContext context, Route route) {
    return Navigator.push(context, route);
  }

  static dynamic _pop(
    FlutRuntime runtime,
    BuildContext context, [
    dynamic result,
  ]) {
    Navigator.pop(context, result);
    return null;
  }

  static dynamic _canPop(FlutRuntime runtime, BuildContext context) {
    return Navigator.canPop(context);
  }

  static dynamic _pushReplacement(
    FlutRuntime runtime,
    BuildContext context,
    Route newRoute, {
    dynamic result,
  }) {
    return Navigator.pushReplacement(context, newRoute, result: result);
  }
}
