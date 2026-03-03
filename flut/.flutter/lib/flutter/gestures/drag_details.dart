import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/dart/core.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';

class FlutDragStartDetails extends FlutValueObject {
  final DragStartDetails details;

  const FlutDragStartDetails(this.details) : super('DragStartDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    if (details.sourceTimeStamp != null) {
      result['sourceTimeStamp'] = FlutDuration(
        details.sourceTimeStamp!,
      ).flutEncode();
    }
    if (details.kind != null) {
      result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind!);
    }
    return result;
  }

  static DragStartDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DragStartDetails(
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      localPosition: runtime.unpackOptionalField<Offset>(data, 'localPosition'),
      sourceTimeStamp: runtime.unpackOptionalField<Duration>(
        data,
        'sourceTimeStamp',
      ),
      kind: runtime.unpackOptionalField<PointerDeviceKind>(data, 'kind'),
    );
  }
}

class FlutDragUpdateDetails extends FlutValueObject {
  final DragUpdateDetails details;

  const FlutDragUpdateDetails(this.details) : super('DragUpdateDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['delta'] = FlutOffset(details.delta).flutEncode();
    if (details.sourceTimeStamp != null) {
      result['sourceTimeStamp'] = FlutDuration(
        details.sourceTimeStamp!,
      ).flutEncode();
    }
    if (details.primaryDelta != null) {
      result['primaryDelta'] = details.primaryDelta;
    }
    if (details.kind != null) {
      result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind!);
    }
    return result;
  }

  static DragUpdateDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DragUpdateDetails(
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      localPosition: runtime.unpackOptionalField<Offset>(data, 'localPosition'),
      sourceTimeStamp: runtime.unpackOptionalField<Duration>(
        data,
        'sourceTimeStamp',
      ),
      delta: runtime.unpackRequiredField<Offset>(data, 'delta'),
      primaryDelta: runtime.unpackOptionalField<double>(data, 'primaryDelta'),
      kind: runtime.unpackOptionalField<PointerDeviceKind>(data, 'kind'),
    );
  }
}

class FlutDragDownDetails extends FlutValueObject {
  final DragDownDetails details;

  const FlutDragDownDetails(this.details) : super('DragDownDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    return result;
  }
}

class FlutDragEndDetails extends FlutValueObject {
  final DragEndDetails details;

  const FlutDragEndDetails(this.details) : super('DragEndDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['velocity'] = FlutVelocity(details.velocity).flutEncode();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    if (details.primaryVelocity != null) {
      result['primaryVelocity'] = details.primaryVelocity;
    }
    return result;
  }

  static DragEndDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DragEndDetails(
      velocity: runtime.unpackRequiredField<Velocity>(data, 'velocity'),
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      localPosition: runtime.unpackOptionalField<Offset>(data, 'localPosition'),
      primaryVelocity: runtime.unpackOptionalField<double>(
        data,
        'primaryVelocity',
      ),
    );
  }
}
