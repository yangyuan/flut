import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

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
    runtime.registerStatic('Navigator.of', _of);
    runtime.registerStatic('Navigator.maybeOf', _maybeOf);
    runtime.registerStatic('Navigator.push', _push);
    runtime.registerStatic('Navigator.pushReplacement', _pushReplacement);
    runtime.registerStatic('Navigator.pushAndRemoveUntil', _pushAndRemoveUntil);
    runtime.registerStatic('Navigator.pushNamed', _pushNamed);
    runtime.registerStatic(
      'Navigator.pushReplacementNamed',
      _pushReplacementNamed,
    );
    runtime.registerStatic(
      'Navigator.pushNamedAndRemoveUntil',
      _pushNamedAndRemoveUntil,
    );
    runtime.registerStatic('Navigator.popAndPushNamed', _popAndPushNamed);
    runtime.registerStatic('Navigator.pop', _pop);
    runtime.registerStatic('Navigator.maybePop', _maybePop);
    runtime.registerStatic('Navigator.popUntil', _popUntil);
    runtime.registerStatic('Navigator.canPop', _canPop);
    runtime.registerStatic('Navigator.replace', _replace);
    runtime.registerStatic('Navigator.replaceRouteBelow', _replaceRouteBelow);
    runtime.registerStatic('Navigator.removeRoute', _removeRoute);
    runtime.registerStatic('Navigator.removeRouteBelow', _removeRouteBelow);
  }

  static dynamic _of(
    FlutRuntime runtime,
    BuildContext context, {
    bool rootNavigator = false,
  }) {
    return Navigator.of(context, rootNavigator: rootNavigator);
  }

  static dynamic _maybeOf(
    FlutRuntime runtime,
    BuildContext context, {
    bool rootNavigator = false,
  }) {
    return Navigator.maybeOf(context, rootNavigator: rootNavigator);
  }

  static dynamic _push(FlutRuntime runtime, BuildContext context, Route route) {
    return Navigator.push(context, route);
  }

  static dynamic _pushReplacement(
    FlutRuntime runtime,
    BuildContext context,
    Route newRoute, {
    dynamic result,
  }) {
    return Navigator.pushReplacement(context, newRoute, result: result);
  }

  static dynamic _pushAndRemoveUntil(
    FlutRuntime runtime,
    BuildContext context,
    Route newRoute,
    FlutCallableRef predicate,
  ) {
    return Navigator.pushAndRemoveUntil(
      context,
      newRoute,
      runtime.adaptCallableByType(predicate) as RoutePredicate,
    );
  }

  static dynamic _pushNamed(
    FlutRuntime runtime,
    BuildContext context,
    String routeName, {
    Object? arguments,
  }) {
    return Navigator.pushNamed(context, routeName, arguments: arguments);
  }

  static dynamic _pushReplacementNamed(
    FlutRuntime runtime,
    BuildContext context,
    String routeName, {
    dynamic result,
    Object? arguments,
  }) {
    return Navigator.pushReplacementNamed(
      context,
      routeName,
      result: result,
      arguments: arguments,
    );
  }

  static dynamic _pushNamedAndRemoveUntil(
    FlutRuntime runtime,
    BuildContext context,
    String newRouteName,
    FlutCallableRef predicate, {
    Object? arguments,
  }) {
    return Navigator.pushNamedAndRemoveUntil(
      context,
      newRouteName,
      runtime.adaptCallableByType(predicate) as RoutePredicate,
      arguments: arguments,
    );
  }

  static dynamic _popAndPushNamed(
    FlutRuntime runtime,
    BuildContext context,
    String routeName, {
    dynamic result,
    Object? arguments,
  }) {
    return Navigator.popAndPushNamed(
      context,
      routeName,
      result: result,
      arguments: arguments,
    );
  }

  static dynamic _pop(
    FlutRuntime runtime,
    BuildContext context, [
    dynamic result,
  ]) {
    Navigator.pop(context, result);
    return null;
  }

  static dynamic _maybePop(
    FlutRuntime runtime,
    BuildContext context, [
    dynamic result,
  ]) {
    return Navigator.maybePop(context, result);
  }

  static dynamic _popUntil(
    FlutRuntime runtime,
    BuildContext context,
    FlutCallableRef predicate,
  ) {
    Navigator.popUntil(
      context,
      runtime.adaptCallableByType(predicate) as RoutePredicate,
    );
    return null;
  }

  static dynamic _canPop(FlutRuntime runtime, BuildContext context) {
    return Navigator.canPop(context);
  }

  static dynamic _replace(
    FlutRuntime runtime,
    BuildContext context, {
    required Route oldRoute,
    required Route newRoute,
  }) {
    Navigator.replace(context, oldRoute: oldRoute, newRoute: newRoute);
    return null;
  }

  static dynamic _replaceRouteBelow(
    FlutRuntime runtime,
    BuildContext context, {
    required Route anchorRoute,
    required Route newRoute,
  }) {
    Navigator.replaceRouteBelow(
      context,
      anchorRoute: anchorRoute,
      newRoute: newRoute,
    );
    return null;
  }

  static dynamic _removeRoute(
    FlutRuntime runtime,
    BuildContext context,
    Route route,
  ) {
    Navigator.removeRoute(context, route);
    return null;
  }

  static dynamic _removeRouteBelow(
    FlutRuntime runtime,
    BuildContext context,
    Route anchorRoute,
  ) {
    Navigator.removeRouteBelow(context, anchorRoute);
    return null;
  }
}

class FlutNavigatorState with FlutRealtimeObject<NavigatorState> {
  FlutNavigatorState.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required NavigatorState target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'NavigatorState',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('NavigatorState', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('NavigatorState', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'push':
        return flutTarget.push(args[0] as Route);
      case 'pushReplacement':
        return flutTarget.pushReplacement(
          args[0] as Route,
          result: kwargs['result'],
        );
      case 'pushAndRemoveUntil':
        return flutTarget.pushAndRemoveUntil(
          args[0] as Route,
          runtime.adaptCallableByType(args[1] as FlutCallableRef)
              as RoutePredicate,
        );
      case 'pushNamed':
        return flutTarget.pushNamed(
          args[0] as String,
          arguments: kwargs['arguments'],
        );
      case 'pushReplacementNamed':
        return flutTarget.pushReplacementNamed(
          args[0] as String,
          result: kwargs['result'],
          arguments: kwargs['arguments'],
        );
      case 'pushNamedAndRemoveUntil':
        return flutTarget.pushNamedAndRemoveUntil(
          args[0] as String,
          runtime.adaptCallableByType(args[1] as FlutCallableRef)
              as RoutePredicate,
          arguments: kwargs['arguments'],
        );
      case 'popAndPushNamed':
        return flutTarget.popAndPushNamed(
          args[0] as String,
          result: kwargs['result'],
          arguments: kwargs['arguments'],
        );
      case 'pop':
        if (args.isEmpty) {
          flutTarget.pop();
        } else {
          flutTarget.pop(args[0]);
        }
        return null;
      case 'maybePop':
        if (args.isEmpty) {
          return flutTarget.maybePop();
        }
        return flutTarget.maybePop(args[0]);
      case 'popUntil':
        flutTarget.popUntil(
          runtime.adaptCallableByType(args[0] as FlutCallableRef)
              as RoutePredicate,
        );
        return null;
      case 'canPop':
        return flutTarget.canPop();
      case 'replace':
        flutTarget.replace(
          oldRoute: kwargs['oldRoute'] as Route,
          newRoute: kwargs['newRoute'] as Route,
        );
        return null;
      case 'replaceRouteBelow':
        flutTarget.replaceRouteBelow(
          anchorRoute: kwargs['anchorRoute'] as Route,
          newRoute: kwargs['newRoute'] as Route,
        );
        return null;
      case 'removeRoute':
        flutTarget.removeRoute(args[0] as Route);
        return null;
      case 'removeRouteBelow':
        flutTarget.removeRouteBelow(args[0] as Route);
        return null;
      case 'finalizeRoute':
        flutTarget.finalizeRoute(args[0] as Route);
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
