import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutBorderStyle extends FlutEnumObject<BorderStyle> {
  const FlutBorderStyle()
    : super('BorderStyle', const {
        'solid': BorderStyle.solid,
        'none': BorderStyle.none,
      });
}

class FlutBorderSide extends FlutValueObject {
  final BorderSide borderSide;

  const FlutBorderSide(this.borderSide) : super('BorderSide');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['color'] = FlutColor(borderSide.color).flutEncode();
    result['width'] = borderSide.width;
    result['style'] = const FlutBorderStyle().flutEncode(borderSide.style);
    result['strokeAlign'] = borderSide.strokeAlign;
    return result;
  }

  static BorderSide? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BorderSide(
      color: runtime.unpackRequiredField<Color>(data, 'color'),
      width: runtime.unpackRequiredField<double>(data, 'width'),
      style: runtime.unpackRequiredField<BorderStyle>(data, 'style'),
      strokeAlign: runtime.unpackRequiredField<double>(data, 'strokeAlign'),
    );
  }
}
