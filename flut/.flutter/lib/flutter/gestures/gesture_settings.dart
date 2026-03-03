import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutDeviceGestureSettings extends FlutValueObject {
  final DeviceGestureSettings settings;
  const FlutDeviceGestureSettings(this.settings)
    : super('DeviceGestureSettings');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (settings.touchSlop != null) {
      result['touchSlop'] = settings.touchSlop;
    }
    return result;
  }

  static DeviceGestureSettings? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DeviceGestureSettings(
      touchSlop: runtime.unpackOptionalField<double>(data, 'touchSlop'),
    );
  }
}
