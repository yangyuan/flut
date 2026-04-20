import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

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
    extends FlutChangeNotifier<TransformationController> {
  FlutTransformationController.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutTransformationController.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'TransformationController');

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
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'value':
        flutTarget.value = value as Matrix4;
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
      case 'toScene':
        return flutTarget.toScene(args[0] as Offset);
    }
    return super.callMethod(method, args, kwargs);
  }
}
