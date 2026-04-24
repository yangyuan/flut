import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutBorderRadiusGeometry extends FlutValueObject {
  final BorderRadiusGeometry borderRadiusGeometry;

  const FlutBorderRadiusGeometry(this.borderRadiusGeometry)
    : super('BorderRadiusGeometry');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'BorderRadiusGeometry has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static BorderRadiusGeometry? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'BorderRadiusGeometry has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutBorderRadius extends FlutValueObject {
  final BorderRadius borderRadius;

  const FlutBorderRadius(this.borderRadius) : super('BorderRadius');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['topLeft'] = FlutRadius(borderRadius.topLeft).flutEncode();
    result['topRight'] = FlutRadius(borderRadius.topRight).flutEncode();
    result['bottomLeft'] = FlutRadius(borderRadius.bottomLeft).flutEncode();
    result['bottomRight'] = FlutRadius(borderRadius.bottomRight).flutEncode();
    return result;
  }

  static BorderRadius? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BorderRadius.only(
      topLeft: runtime.unpackRequiredField<Radius>(data, 'topLeft'),
      topRight: runtime.unpackRequiredField<Radius>(data, 'topRight'),
      bottomLeft: runtime.unpackRequiredField<Radius>(data, 'bottomLeft'),
      bottomRight: runtime.unpackRequiredField<Radius>(data, 'bottomRight'),
    );
  }
}

class FlutBorderRadiusDirectional extends FlutValueObject {
  final BorderRadiusDirectional borderRadiusDirectional;

  const FlutBorderRadiusDirectional(this.borderRadiusDirectional)
    : super('BorderRadiusDirectional');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['topStart'] = FlutRadius(
      borderRadiusDirectional.topStart,
    ).flutEncode();
    result['topEnd'] = FlutRadius(borderRadiusDirectional.topEnd).flutEncode();
    result['bottomStart'] = FlutRadius(
      borderRadiusDirectional.bottomStart,
    ).flutEncode();
    result['bottomEnd'] = FlutRadius(
      borderRadiusDirectional.bottomEnd,
    ).flutEncode();
    return result;
  }

  static BorderRadiusDirectional? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BorderRadiusDirectional.only(
      topStart: runtime.unpackRequiredField<Radius>(data, 'topStart'),
      topEnd: runtime.unpackRequiredField<Radius>(data, 'topEnd'),
      bottomStart: runtime.unpackRequiredField<Radius>(data, 'bottomStart'),
      bottomEnd: runtime.unpackRequiredField<Radius>(data, 'bottomEnd'),
    );
  }
}
