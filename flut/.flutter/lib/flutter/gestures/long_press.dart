import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';

class FlutLongPressStartDetails extends FlutValueObject {
  final LongPressStartDetails details;

  const FlutLongPressStartDetails(this.details)
    : super('LongPressStartDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    return result;
  }
}

class FlutLongPressMoveUpdateDetails extends FlutValueObject {
  final LongPressMoveUpdateDetails details;

  const FlutLongPressMoveUpdateDetails(this.details)
    : super('LongPressMoveUpdateDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['offsetFromOrigin'] = FlutOffset(
      details.offsetFromOrigin,
    ).flutEncode();
    result['localOffsetFromOrigin'] = FlutOffset(
      details.localOffsetFromOrigin,
    ).flutEncode();
    return result;
  }
}

class FlutLongPressEndDetails extends FlutValueObject {
  final LongPressEndDetails details;

  const FlutLongPressEndDetails(this.details) : super('LongPressEndDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['velocity'] = FlutVelocity(details.velocity).flutEncode();
    return result;
  }
}
