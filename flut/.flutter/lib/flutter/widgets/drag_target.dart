import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';

class FlutDraggableDetails extends FlutValueObject {
  final DraggableDetails details;

  const FlutDraggableDetails(this.details) : super('DraggableDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['wasAccepted'] = details.wasAccepted;
    result['velocity'] = FlutVelocity(details.velocity).flutEncode();
    result['offset'] = FlutOffset(details.offset).flutEncode();
    return result;
  }

  static DraggableDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DraggableDetails(
      wasAccepted: runtime.unpackRequiredField<bool>(data, 'wasAccepted'),
      velocity: runtime.unpackRequiredField<Velocity>(data, 'velocity'),
      offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
    );
  }
}

class FlutDragTargetDetails extends FlutValueObject {
  final DragTargetDetails details;
  final FlutRuntime? _runtime;

  const FlutDragTargetDetails(this.details, [this._runtime])
    : super('DragTargetDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (_runtime != null) {
      result['data'] = _runtime.encodeValue(details.data);
    }
    result['offset'] = FlutOffset(details.offset).flutEncode();
    return result;
  }

  static DragTargetDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DragTargetDetails(
      data: runtime.unpackDynamicRequiredField(data, 'data'),
      offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
    );
  }
}

class FlutDraggable {
  FlutDraggable._();

  static Draggable<Object>? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return Draggable<Object>(
      key: runtime.decodeKey(data),
      data: runtime.unpackDynamicOptionalField(data, 'data'),
      axis: runtime.unpackOptionalField<Axis>(data, 'axis'),
      childWhenDragging: runtime.unpackOptionalField<Widget>(
        data,
        'childWhenDragging',
      ),
      feedbackOffset: runtime.unpackRequiredField<Offset>(
        data,
        'feedbackOffset',
      ),
      affinity: runtime.unpackOptionalField<Axis>(data, 'affinity'),
      maxSimultaneousDrags: runtime.unpackOptionalField<int>(
        data,
        'maxSimultaneousDrags',
      ),
      onDragStarted: runtime.unpackOptionalCallback(data, 'onDragStarted'),
      onDragUpdate: runtime.unpackOptionalCallback(data, 'onDragUpdate'),
      onDraggableCanceled: runtime.unpackOptionalCallback(
        data,
        'onDraggableCanceled',
      ),
      onDragEnd: runtime.unpackOptionalCallback(data, 'onDragEnd'),
      onDragCompleted: runtime.unpackOptionalCallback(data, 'onDragCompleted'),
      ignoringFeedbackSemantics: runtime.unpackRequiredField<bool>(
        data,
        'ignoringFeedbackSemantics',
      ),
      ignoringFeedbackPointer: runtime.unpackRequiredField<bool>(
        data,
        'ignoringFeedbackPointer',
      ),
      rootOverlay: runtime.unpackRequiredField<bool>(data, 'rootOverlay'),
      hitTestBehavior: runtime.unpackRequiredField<HitTestBehavior>(
        data,
        'hitTestBehavior',
      ),
      feedback: runtime.unpackRequiredField<Widget>(data, 'feedback'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutDragTarget {
  FlutDragTarget._();

  static DragTarget<Object>? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DragTarget<Object>(
      key: runtime.decodeKey(data),
      builder: runtime.unpackRequiredCallback(data, 'builder'),
      onWillAcceptWithDetails: runtime.unpackOptionalCallback(
        data,
        'onWillAcceptWithDetails',
      ),
      onAcceptWithDetails: runtime.unpackOptionalCallback(
        data,
        'onAcceptWithDetails',
      ),
      onLeave: runtime.unpackOptionalCallback(data, 'onLeave'),
      onMove: runtime.unpackOptionalCallback(data, 'onMove'),
      hitTestBehavior: runtime.unpackRequiredField<HitTestBehavior>(
        data,
        'hitTestBehavior',
      ),
    );
  }
}
