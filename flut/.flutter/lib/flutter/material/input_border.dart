import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutInputBorder extends FlutValueObject {
  final InputBorder inputBorder;

  const FlutInputBorder(this.inputBorder) : super('InputBorder');

  @override
  Map<String, dynamic> flutEncode() {
    if (inputBorder == InputBorder.none) {
      final result = flutBaseProps();
      result['value'] = 'none';
      return result;
    }
    throw ArgumentError('Unsupported InputBorder for encoding: $inputBorder');
  }

  static InputBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final value = runtime.unpackRequiredField<String>(data, 'value');
    if (value == 'none') return InputBorder.none;
    throw ArgumentError('Unknown InputBorder value: $value');
  }
}
