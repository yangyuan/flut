import 'package:flutter/services.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutLogicalKeyboardKey extends FlutValueObject {
  final LogicalKeyboardKey key;

  const FlutLogicalKeyboardKey(this.key) : super('LogicalKeyboardKey');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['keyId'] = key.keyId;
    return result;
  }

  static LogicalKeyboardKey? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return LogicalKeyboardKey(runtime.unpackRequiredField<int>(data, 'keyId'));
  }
}

class FlutPhysicalKeyboardKey extends FlutValueObject {
  final PhysicalKeyboardKey key;

  const FlutPhysicalKeyboardKey(this.key) : super('PhysicalKeyboardKey');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['usbHidUsage'] = key.usbHidUsage;
    return result;
  }

  static PhysicalKeyboardKey? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PhysicalKeyboardKey(
      runtime.unpackRequiredField<int>(data, 'usbHidUsage'),
    );
  }
}
