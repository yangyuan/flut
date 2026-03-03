import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutBoxShadow extends FlutValueObject {
  final BoxShadow shadow;
  const FlutBoxShadow(this.shadow) : super('BoxShadow');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['color'] = FlutColor(shadow.color).flutEncode();
    result['offset'] = FlutOffset(shadow.offset).flutEncode();
    result['blurRadius'] = FlutDouble.encode(shadow.blurRadius);
    result['spreadRadius'] = FlutDouble.encode(shadow.spreadRadius);
    result['blurStyle'] = const FlutBlurStyle().flutEncode(shadow.blurStyle);
    return result;
  }

  static BoxShadow? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return BoxShadow(
      color: runtime.unpackRequiredField<Color>(data, 'color'),
      offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
      blurRadius: runtime.unpackRequiredField<double>(data, 'blurRadius'),
      spreadRadius: runtime.unpackRequiredField<double>(data, 'spreadRadius'),
      blurStyle: runtime.unpackRequiredField<BlurStyle>(data, 'blurStyle'),
    );
  }
}
