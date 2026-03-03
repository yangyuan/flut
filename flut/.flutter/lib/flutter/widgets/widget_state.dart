import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutWidgetState extends FlutEnumObject<WidgetState> {
  const FlutWidgetState()
    : super('WidgetState', const {
        'hovered': WidgetState.hovered,
        'focused': WidgetState.focused,
        'pressed': WidgetState.pressed,
        'dragged': WidgetState.dragged,
        'selected': WidgetState.selected,
        'scrolledUnder': WidgetState.scrolledUnder,
        'disabled': WidgetState.disabled,
        'error': WidgetState.error,
      });
}

class FlutWidgetStatesConstraint
    with FlutAbstractObject
    implements WidgetStatesConstraint {
  @override
  final FlutRuntime runtime;
  final int isSatisfiedById;

  FlutWidgetStatesConstraint._(this.runtime, this.isSatisfiedById);

  @override
  bool isSatisfiedBy(Set<WidgetState> states) {
    return runtime.callAction<bool>(isSatisfiedById, args: [states]) ?? false;
  }

  static WidgetStatesConstraint? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutWidgetStatesConstraint._(
      runtime,
      runtime.unpackRequiredField<int>(data, 'isSatisfiedBy'),
    );
  }
}

class FlutWidgetStateColor
    with FlutRealtimeObject<WidgetStateColor>
    implements WidgetStateColor {
  final int? resolveId;

  FlutWidgetStateColor.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required int this.resolveId,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: this);
  }

  FlutWidgetStateColor.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required WidgetStateColor target,
  }) : resolveId = null {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'WidgetStateColor',
      target: target,
    );
  }

  @override
  Color resolve(Set<WidgetState> states) {
    if (resolveId != null) {
      return runtime.callAction<Color>(resolveId!, args: [states]) as Color;
    }
    return flutTarget.resolve(states);
  }

  @override
  Never noSuchMethod(Invocation invocation) {
    throw FlutterError.fromParts(<DiagnosticsNode>[
      ErrorSummary(
        'WidgetStateColor does not support direct Color member access.',
      ),
      ErrorDescription(
        'Use resolve() to get the Color for a given set of states.',
      ),
    ]);
  }

  static FlutWidgetStateColor flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutWidgetStateColor.createFromData(
      runtime: runtime,
      data: data,
      resolveId: runtime.unpackRequiredField<int>(data, 'resolve'),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('WidgetStateColor', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('WidgetStateColor', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'resolve':
        return resolve(args[0] as Set<WidgetState>);
    }
    throw FlutUnknownMethodException(method);
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('WidgetStateColor.transparent', _transparent);
    runtime.registerStatic('WidgetStateColor.resolveWith', _resolveWith);
  }

  static FlutWidgetStateColor _transparent(FlutRuntime runtime) {
    return runtime.wrapObject<FlutWidgetStateColor>(
      WidgetStateColor.transparent,
      (oid) => FlutWidgetStateColor.createFromObject(
        runtime: runtime,
        oid: oid,
        target: WidgetStateColor.transparent,
      ),
    );
  }

  static dynamic _resolveWith(FlutRuntime runtime, int actionId) {
    final color = WidgetStateColor.resolveWith((Set<WidgetState> states) {
      return runtime.callAction<Color>(actionId, args: [states]) as Color;
    });
    return runtime.wrapObject<FlutWidgetStateColor>(
      color,
      (oid) => FlutWidgetStateColor.createFromObject(
        runtime: runtime,
        oid: oid,
        target: color,
      ),
    );
  }
}

class FlutWidgetStatePropertyAll extends WidgetStatePropertyAll<dynamic>
    with FlutRealtimeObject<WidgetStatePropertyAll<dynamic>> {
  FlutWidgetStatePropertyAll.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required dynamic value,
  }) : super(value) {
    initRealtimeFromData(runtime: runtime, data: data, target: this);
  }

  @override
  dynamic adaptGeneric<V>() {
    return WidgetStatePropertyAll<V>(resolve({}));
  }

  static FlutWidgetStatePropertyAll flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final value = runtime.unpackDynamicOptionalField(data, 'value');
    return FlutWidgetStatePropertyAll.createFromData(
      runtime: runtime,
      data: data,
      value: value,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('WidgetStatePropertyAll', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('WidgetStatePropertyAll', property);
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

class FlutWidgetStateProperty extends WidgetStateProperty<dynamic>
    with FlutRealtimeObject<WidgetStateProperty<dynamic>> {
  final int resolveId;

  FlutWidgetStateProperty.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required this.resolveId,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: this);
  }

  @override
  dynamic resolve(Set<WidgetState> states) {
    return runtime.callAction(resolveId, args: [states]);
  }

  @override
  dynamic adaptGeneric<V>() {
    return WidgetStateProperty.resolveWith<V>((states) => resolve(states) as V);
  }

  static FlutWidgetStateProperty flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutWidgetStateProperty.createFromData(
      runtime: runtime,
      data: data,
      resolveId: runtime.unpackRequiredField<int>(data, 'resolve'),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('WidgetStateProperty', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('WidgetStateProperty', property);
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

class FlutWidgetStatesController
    with FlutRealtimeObject<WidgetStatesController> {
  FlutWidgetStatesController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required WidgetStatesController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutWidgetStatesController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required WidgetStatesController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'WidgetStatesController',
      target: target,
    );
  }

  static FlutWidgetStatesController flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final controller = WidgetStatesController(
      runtime.unpackOptionalField<Set<WidgetState>>(data, 'value'),
    );
    return FlutWidgetStatesController.createFromData(
      runtime: runtime,
      data: data,
      target: controller,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
    }
    throw FlutUnknownPropertyException('WidgetStatesController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = value as Set<WidgetState>;
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
      case 'update':
        flutTarget.update(args[0] as WidgetState, args[1] as bool);
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
