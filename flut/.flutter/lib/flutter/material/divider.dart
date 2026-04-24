import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutDivider {
  FlutDivider._();

  static Divider? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Divider(
      key: runtime.decodeKey(data),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      thickness: runtime.unpackOptionalField<double>(data, 'thickness'),
      indent: runtime.unpackOptionalField<double>(data, 'indent'),
      endIndent: runtime.unpackOptionalField<double>(data, 'endIndent'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      radius: runtime.unpackOptionalField<BorderRadiusGeometry>(data, 'radius'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Divider.createBorderSide', createBorderSide);
  }

  static dynamic createBorderSide(
    FlutRuntime runtime,
    BuildContext? context, {
    Color? color,
    double? width,
  }) {
    return Divider.createBorderSide(context, color: color, width: width);
  }
}
