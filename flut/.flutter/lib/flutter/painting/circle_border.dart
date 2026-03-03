import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';

class FlutCircleBorder extends FlutValueObject {
  final CircleBorder value;
  const FlutCircleBorder(this.value) : super('CircleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['eccentricity'] = value.eccentricity;
    return result;
  }

  static CircleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CircleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      eccentricity: runtime.unpackRequiredField<double>(data, 'eccentricity'),
    );
  }
}
