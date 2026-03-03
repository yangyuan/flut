import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';

class FlutBoxShape extends FlutEnumObject<BoxShape> {
  const FlutBoxShape()
    : super('BoxShape', const {
        'rectangle': BoxShape.rectangle,
        'circle': BoxShape.circle,
      });
}

class FlutBorder extends FlutValueObject {
  final Border border;

  const FlutBorder(this.border) : super('Border');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['top'] = FlutBorderSide(border.top).flutEncode();
    result['right'] = FlutBorderSide(border.right).flutEncode();
    result['bottom'] = FlutBorderSide(border.bottom).flutEncode();
    result['left'] = FlutBorderSide(border.left).flutEncode();
    return result;
  }

  static Border? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Border(
      top: runtime.unpackRequiredField<BorderSide>(data, 'top'),
      right: runtime.unpackRequiredField<BorderSide>(data, 'right'),
      bottom: runtime.unpackRequiredField<BorderSide>(data, 'bottom'),
      left: runtime.unpackRequiredField<BorderSide>(data, 'left'),
    );
  }
}
