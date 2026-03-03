import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutPanAxis extends FlutEnumObject<PanAxis> {
  const FlutPanAxis()
    : super('PanAxis', const {
        'horizontal': PanAxis.horizontal,
        'vertical': PanAxis.vertical,
        'aligned': PanAxis.aligned,
        'free': PanAxis.free,
      });
}

class FlutInteractiveViewer {
  FlutInteractiveViewer._();

  static InteractiveViewer? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return InteractiveViewer(
      key: runtime.decodeKey(data),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      panAxis: runtime.unpackRequiredField<PanAxis>(data, 'panAxis'),
      boundaryMargin: runtime.unpackRequiredField<EdgeInsets>(
        data,
        'boundaryMargin',
      ),
      constrained: runtime.unpackRequiredField<bool>(data, 'constrained'),
      maxScale: runtime.unpackRequiredField<double>(data, 'maxScale'),
      minScale: runtime.unpackRequiredField<double>(data, 'minScale'),
      interactionEndFrictionCoefficient: runtime.unpackRequiredField<double>(
        data,
        'interactionEndFrictionCoefficient',
      ),
      onInteractionEnd: runtime.unpackOptionalCallback(
        data,
        'onInteractionEnd',
      ),
      onInteractionStart: runtime.unpackOptionalCallback(
        data,
        'onInteractionStart',
      ),
      onInteractionUpdate: runtime.unpackOptionalCallback(
        data,
        'onInteractionUpdate',
      ),
      panEnabled: runtime.unpackRequiredField<bool>(data, 'panEnabled'),
      scaleEnabled: runtime.unpackRequiredField<bool>(data, 'scaleEnabled'),
      scaleFactor: runtime.unpackRequiredField<double>(data, 'scaleFactor'),
      transformationController: runtime
          .unpackOptionalField<TransformationController>(
            data,
            'transformationController',
          ),
      trackpadScrollCausesScale: runtime.unpackRequiredField<bool>(
        data,
        'trackpadScrollCausesScale',
      ),
      alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutTransformationController
    with FlutRealtimeObject<TransformationController> {
  FlutTransformationController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required TransformationController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutTransformationController.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required TransformationController target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'TransformationController',
      target: target,
    );
  }

  static FlutRealtimeObject flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final value = runtime.unpackOptionalField<Matrix4>(data, 'value');
    return FlutTransformationController.createFromData(
      runtime: runtime,
      data: data,
      target: TransformationController(value ?? Matrix4.identity()),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('TransformationController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = value as Matrix4;
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
      case 'toScene':
        return flutTarget.toScene(args[0] as Offset);
      case 'notifyListeners':
        // ignore: invalid_use_of_visible_for_testing_member, invalid_use_of_protected_member
        flutTarget.notifyListeners();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
