import 'package:flutter/rendering.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutStackFit extends FlutEnumObject<StackFit> {
  const FlutStackFit()
    : super('StackFit', const {
        'loose': StackFit.loose,
        'expand': StackFit.expand,
        'passthrough': StackFit.passthrough,
      });
}

class FlutRelativeRect extends FlutValueObject {
  final RelativeRect rect;

  const FlutRelativeRect(this.rect) : super('RelativeRect');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = rect.left;
    result['top'] = rect.top;
    result['right'] = rect.right;
    result['bottom'] = rect.bottom;
    return result;
  }

  static RelativeRect? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return RelativeRect.fromLTRB(
      runtime.unpackRequiredField<double>(data, 'left'),
      runtime.unpackRequiredField<double>(data, 'top'),
      runtime.unpackRequiredField<double>(data, 'right'),
      runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}
