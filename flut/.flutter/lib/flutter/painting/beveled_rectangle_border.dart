import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';
import 'package:flut/flutter/painting/border_radius.dart';

class FlutBeveledRectangleBorder extends FlutValueObject {
  final BeveledRectangleBorder value;
  const FlutBeveledRectangleBorder(this.value)
    : super('BeveledRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadiusGeometry(
      value.borderRadius,
    ).flutEncode();
    return result;
  }

  static BeveledRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BeveledRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
    );
  }
}
