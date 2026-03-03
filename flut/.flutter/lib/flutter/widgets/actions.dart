import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

/// Concrete Intent subclass for Python-side intents.
/// Intent is abstract in Dart, so this provides the concrete implementation.
class _FlutIntent extends Intent {
  final String name;
  final Map<String, dynamic>? data;
  const _FlutIntent(this.name, {this.data});
}

/// InheritedWidget that carries action handlers for Python Actions widgets.
/// Replaces Flutter's type-based Actions dispatch with name-based lookup
/// via visitAncestorElements, avoiding the Dart Type collision.
class FlutActionScope extends InheritedWidget {
  final FlutRuntime runtime;
  final Map<String, int> handlers; // intentName → cid

  const FlutActionScope({
    super.key,
    required this.runtime,
    required this.handlers,
    required super.child,
  });

  @override
  bool updateShouldNotify(FlutActionScope oldWidget) {
    return handlers != oldWidget.handlers;
  }

  /// Walk ancestors to find the first FlutActionScope that handles intentName.
  static int? findHandler(BuildContext context, String intentName) {
    int? result;
    context.visitAncestorElements((element) {
      if (element.widget is FlutActionScope) {
        final scope = element.widget as FlutActionScope;
        final cid = scope.handlers[intentName];
        if (cid != null) {
          result = cid;
          return false; // stop walking
        }
      }
      return true; // continue walking
    });
    return result;
  }

  /// Invoke the handler for intentName, passing intent data.
  static void invokeHandler(
    BuildContext context,
    FlutRuntime runtime,
    String intentName, [
    Map<String, dynamic>? intentData,
  ]) {
    final cid = findHandler(context, intentName);
    if (cid != null) {
      runtime.callAction(cid, args: [intentData ?? const {}]);
    }
  }
}

/// Dart-side decoder for Intent [value, abstract].
class FlutIntent {
  FlutIntent._();

  static Intent flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return _FlutIntent(
      data['intentName'] as String,
      data: data['data'] as Map<String, dynamic>?,
    );
  }
}

class FlutActions {
  FlutActions._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final actionsData = data['actions'] as Map<String, dynamic>;
    final Map<String, int> handlers = {};
    for (final entry in actionsData.entries) {
      final callableData = entry.value as Map<String, dynamic>;
      final cid = callableData['_flut_cid'] as int?;
      if (cid != null) {
        handlers[entry.key] = cid;
      }
    }

    return FlutActionScope(
      key: runtime.decodeKey(data),
      runtime: runtime,
      handlers: handlers,
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Actions.invoke', _invoke);
    runtime.registerStatic('Actions.maybeInvoke', _maybeInvoke);
  }

  static dynamic _invoke(
    FlutRuntime runtime,
    dynamic contextArg,
    dynamic intentArg,
  ) {
    final context = contextArg as BuildContext;
    final intent = intentArg as _FlutIntent;
    FlutActionScope.invokeHandler(context, runtime, intent.name, intent.data);
    return null;
  }

  static dynamic _maybeInvoke(
    FlutRuntime runtime,
    dynamic contextArg,
    dynamic intentArg,
  ) {
    final context = contextArg as BuildContext;
    final intent = intentArg as _FlutIntent;
    FlutActionScope.invokeHandler(context, runtime, intent.name, intent.data);
    return null;
  }
}

class FlutActionDispatcher with FlutRealtimeObject<ActionDispatcher> {
  FlutActionDispatcher.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ActionDispatcher target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  static FlutActionDispatcher flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutActionDispatcher.createFromData(
      runtime: runtime,
      data: data,
      target: const ActionDispatcher(),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('ActionDispatcher', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ActionDispatcher', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'invokeAction':
        // invokeAction is handled Python-side; this is a no-op fallback.
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
