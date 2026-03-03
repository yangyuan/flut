import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';

class FlutStadiumBorder extends FlutValueObject {
  final StadiumBorder value;
  const FlutStadiumBorder(this.value) : super('StadiumBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    return result;
  }

  static StadiumBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return StadiumBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
    );
  }
}
