import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

class _FlutFocusNode extends FocusNode {
  _FlutFocusNode({required FlutRuntime runtime, super.onKeyEvent});
}

class FlutFocusNode extends FlutChangeNotifier<FocusNode> {
  FlutFocusNode.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutFocusNode.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'FocusNode');

  static FlutFocusNode flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutFocusNode.createFromData(
      runtime: runtime,
      data: data,
      target: _FlutFocusNode(
        runtime: runtime,
        onKeyEvent:
            runtime.unpackOptionalCallback(data, 'onKeyEvent')
                as FocusOnKeyEventCallback?,
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'hasFocus':
        return flutTarget.hasFocus;
      case 'hasPrimaryFocus':
        return flutTarget.hasPrimaryFocus;
      case 'onKeyEvent':
        return flutTarget.onKeyEvent;
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onKeyEvent':
        flutTarget.onKeyEvent = value as FocusOnKeyEventCallback?;
        return true;
    }
    return super.setProperty(property, value);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'requestFocus':
        flutTarget.requestFocus();
        return null;
      case 'unfocus':
        flutTarget.unfocus();
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}

class FlutFocusScopeNode extends FlutChangeNotifier<FocusScopeNode> {
  FlutFocusScopeNode.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutFocusScopeNode.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'FocusScopeNode');

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final node = FocusScopeNode(
      debugLabel: runtime.unpackOptionalField<String>(data, 'debugLabel'),
      onKeyEvent:
          runtime.unpackOptionalCallback(data, 'onKeyEvent')
              as FocusOnKeyEventCallback?,
      skipTraversal: runtime.unpackRequiredField<bool>(data, 'skipTraversal'),
      canRequestFocus: runtime.unpackRequiredField<bool>(
        data,
        'canRequestFocus',
      ),
      traversalEdgeBehavior: runtime.unpackRequiredField<TraversalEdgeBehavior>(
        data,
        'traversalEdgeBehavior',
      ),
      directionalTraversalEdgeBehavior: runtime
          .unpackRequiredField<TraversalEdgeBehavior>(
            data,
            'directionalTraversalEdgeBehavior',
          ),
    );
    return FlutFocusScopeNode.createFromData(
      runtime: runtime,
      data: data,
      target: node,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'hasFocus':
        return flutTarget.hasFocus;
      case 'hasPrimaryFocus':
        return flutTarget.hasPrimaryFocus;
      case 'onKeyEvent':
        return flutTarget.onKeyEvent;
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onKeyEvent':
        flutTarget.onKeyEvent = value as FocusOnKeyEventCallback?;
        return true;
    }
    return super.setProperty(property, value);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'requestFocus':
        flutTarget.requestFocus();
        return null;
      case 'unfocus':
        flutTarget.unfocus();
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}

class FlutKeyEventResult extends FlutEnumObject<KeyEventResult> {
  const FlutKeyEventResult()
    : super('KeyEventResult', const {
        'handled': KeyEventResult.handled,
        'ignored': KeyEventResult.ignored,
        'skipRemainingHandlers': KeyEventResult.skipRemainingHandlers,
      });
}
