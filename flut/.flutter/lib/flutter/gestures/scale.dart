import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';

class FlutScaleStartDetails extends FlutValueObject {
  final ScaleStartDetails details;

  const FlutScaleStartDetails(this.details) : super('ScaleStartDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['focalPoint'] = FlutOffset(details.focalPoint).flutEncode();
    result['localFocalPoint'] = FlutOffset(
      details.localFocalPoint,
    ).flutEncode();
    result['pointerCount'] = details.pointerCount;
    return result;
  }
}

class FlutScaleUpdateDetails extends FlutValueObject {
  final ScaleUpdateDetails details;

  const FlutScaleUpdateDetails(this.details) : super('ScaleUpdateDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['focalPoint'] = FlutOffset(details.focalPoint).flutEncode();
    result['localFocalPoint'] = FlutOffset(
      details.localFocalPoint,
    ).flutEncode();
    result['scale'] = details.scale;
    result['horizontalScale'] = details.horizontalScale;
    result['verticalScale'] = details.verticalScale;
    result['rotation'] = details.rotation;
    result['pointerCount'] = details.pointerCount;
    result['focalPointDelta'] = FlutOffset(
      details.focalPointDelta,
    ).flutEncode();
    return result;
  }
}

class FlutScaleEndDetails extends FlutValueObject {
  final ScaleEndDetails details;

  const FlutScaleEndDetails(this.details) : super('ScaleEndDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['velocity'] = FlutVelocity(details.velocity).flutEncode();
    result['pointerCount'] = details.pointerCount;
    result['scaleVelocity'] = FlutDouble.encode(details.scaleVelocity);
    return result;
  }
}
