import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutContainer {
  FlutContainer._();

  static Container? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Container(
      key: runtime.decodeKey(data),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
      width: runtime.unpackOptionalField<double>(data, 'width'),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      isAntiAlias: runtime.unpackRequiredField<bool>(data, 'isAntiAlias'),
      decoration: runtime.unpackOptionalField<BoxDecoration>(
        data,
        'decoration',
      ),
      foregroundDecoration: runtime.unpackOptionalField<BoxDecoration>(
        data,
        'foregroundDecoration',
      ),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
      transform: runtime.unpackOptionalField<Matrix4>(data, 'transform'),
      transformAlignment: runtime.unpackOptionalField<Alignment>(
        data,
        'transformAlignment',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
