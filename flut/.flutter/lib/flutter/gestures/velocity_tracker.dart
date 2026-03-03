import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/dart/ui.dart';

class FlutVelocity extends FlutValueObject {
  final Velocity velocity;

  const FlutVelocity(this.velocity) : super('Velocity');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['pixelsPerSecond'] = FlutOffset(
      velocity.pixelsPerSecond,
    ).flutEncode();
    return result;
  }

  static Velocity? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Velocity(
      pixelsPerSecond: runtime.unpackRequiredField<Offset>(
        data,
        'pixelsPerSecond',
      ),
    );
  }
}
