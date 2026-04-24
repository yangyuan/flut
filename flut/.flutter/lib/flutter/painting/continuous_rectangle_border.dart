import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';
import 'package:flut/flutter/painting/border_radius.dart';

class FlutContinuousRectangleBorder extends FlutValueObject {
  final ContinuousRectangleBorder value;
  const FlutContinuousRectangleBorder(this.value)
    : super('ContinuousRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadiusGeometry(
      value.borderRadius,
    ).flutEncode();
    return result;
  }

  static ContinuousRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ContinuousRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
    );
  }
}
