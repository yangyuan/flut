import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutTextScaler extends FlutValueObject {
  final TextScaler textScaler;
  const FlutTextScaler(this.textScaler) : super('TextScaler');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['textScaleFactor'] = textScaler.scale(1.0);
    return result;
  }

  static TextScaler? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextScaler.linear(
      runtime.unpackRequiredField<double>(data, 'textScaleFactor'),
    );
  }
}
