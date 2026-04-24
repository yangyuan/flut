import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';
import 'package:flut/flutter/painting/border_radius.dart';

class FlutRoundedRectangleBorder extends FlutValueObject {
  final RoundedRectangleBorder value;
  const FlutRoundedRectangleBorder(this.value)
    : super('RoundedRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadiusGeometry(
      value.borderRadius,
    ).flutEncode();
    return result;
  }

  static RoundedRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return RoundedRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
    );
  }
}
