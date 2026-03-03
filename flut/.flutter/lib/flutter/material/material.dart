import 'package:flutter/material.dart' hide Material;
import 'package:flutter/material.dart' as m show Material;
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutMaterialType extends FlutEnumObject<MaterialType> {
  const FlutMaterialType()
    : super('MaterialType', const {
        'canvas': MaterialType.canvas,
        'card': MaterialType.card,
        'circle': MaterialType.circle,
        'button': MaterialType.button,
        'transparency': MaterialType.transparency,
      });
}

class FlutMaterial {
  FlutMaterial._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return m.Material(
      key: runtime.decodeKey(data),
      type: runtime.unpackRequiredField<MaterialType>(data, 'type'),
      elevation: runtime.unpackRequiredField<double>(data, 'elevation'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      textStyle: runtime.unpackOptionalField<TextStyle>(data, 'textStyle'),
      borderRadius: runtime.unpackOptionalField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      borderOnForeground: runtime.unpackRequiredField<bool>(
        data,
        'borderOnForeground',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      animationDuration: runtime.unpackRequiredField<Duration>(
        data,
        'animationDuration',
      ),
      animateColor: runtime.unpackRequiredField<bool>(data, 'animateColor'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
