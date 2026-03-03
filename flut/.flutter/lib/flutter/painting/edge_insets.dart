import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutEdgeInsets extends FlutValueObject {
  final EdgeInsets edgeInsets;

  const FlutEdgeInsets(this.edgeInsets) : super('EdgeInsets');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = edgeInsets.left;
    result['top'] = edgeInsets.top;
    result['right'] = edgeInsets.right;
    result['bottom'] = edgeInsets.bottom;
    return result;
  }

  static EdgeInsets? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return EdgeInsets.only(
      left: runtime.unpackRequiredField<double>(data, 'left'),
      top: runtime.unpackRequiredField<double>(data, 'top'),
      right: runtime.unpackRequiredField<double>(data, 'right'),
      bottom: runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}
