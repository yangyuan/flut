import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class _FlutFocusNode extends FocusNode {
  _FlutFocusNode({required FlutRuntime runtime, super.onKeyEvent});
}

class FlutFocusNode with FlutRealtimeObject<FocusNode> {
  FlutFocusNode.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required FocusNode target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutFocusNode.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required FocusNode target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'FocusNode',
      target: target,
    );
  }

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
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('FocusNode', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onKeyEvent':
        flutTarget.onKeyEvent = value as FocusOnKeyEventCallback?;
        return true;
    }
    throw FlutUnknownPropertyException('FocusNode', property);
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
    throw FlutUnknownMethodException(method);
  }
}

class FlutFocusScopeNode with FlutRealtimeObject<FocusScopeNode> {
  FlutFocusScopeNode.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required FocusScopeNode target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutFocusScopeNode.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required FocusScopeNode target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'FocusScopeNode',
      target: target,
    );
  }

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
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('FocusScopeNode', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onKeyEvent':
        flutTarget.onKeyEvent = value as FocusOnKeyEventCallback?;
        return true;
    }
    throw FlutUnknownPropertyException('FocusScopeNode', property);
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
    throw FlutUnknownMethodException(method);
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
