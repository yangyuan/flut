import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutBorderRadius extends FlutValueObject {
  final BorderRadius borderRadius;

  const FlutBorderRadius(this.borderRadius) : super('BorderRadius');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['topLeft'] = borderRadius.topLeft.x;
    result['topRight'] = borderRadius.topRight.x;
    result['bottomLeft'] = borderRadius.bottomLeft.x;
    result['bottomRight'] = borderRadius.bottomRight.x;
    return result;
  }

  static BorderRadius? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final circular = runtime.unpackOptionalField<double>(data, 'circular');
    if (circular != null) {
      return BorderRadius.circular(circular);
    }
    return BorderRadius.only(
      topLeft: Radius.circular(
        runtime.unpackRequiredField<double>(data, 'topLeft'),
      ),
      topRight: Radius.circular(
        runtime.unpackRequiredField<double>(data, 'topRight'),
      ),
      bottomLeft: Radius.circular(
        runtime.unpackRequiredField<double>(data, 'bottomLeft'),
      ),
      bottomRight: Radius.circular(
        runtime.unpackRequiredField<double>(data, 'bottomRight'),
      ),
    );
  }
}
