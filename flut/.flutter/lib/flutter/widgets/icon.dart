import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutIcon {
  FlutIcon._();

  static Icon? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Icon(
      runtime.unpackOptionalField<IconData>(data, 'icon'),
      key: runtime.decodeKey(data),
      size: runtime.unpackOptionalField<double>(data, 'size'),
      fill: runtime.unpackOptionalField<double>(data, 'fill'),
      weight: runtime.unpackOptionalField<double>(data, 'weight'),
      grade: runtime.unpackOptionalField<double>(data, 'grade'),
      opticalSize: runtime.unpackOptionalField<double>(data, 'opticalSize'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      shadows: runtime.unpackOptionalField<List<Shadow>>(data, 'shadows'),
      semanticLabel: runtime.unpackOptionalField<String>(data, 'semanticLabel'),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      applyTextScaling: runtime.unpackOptionalField<bool>(
        data,
        'applyTextScaling',
      ),
      blendMode: runtime.unpackOptionalField<BlendMode>(data, 'blendMode'),
      fontWeight: runtime.unpackOptionalField<FontWeight>(data, 'fontWeight'),
    );
  }
}
