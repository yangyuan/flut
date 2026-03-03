import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutCard {
  FlutCard._();

  static Card? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'filled':
        return Card.filled(
          key: runtime.decodeKey(data),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
          surfaceTintColor: runtime.unpackOptionalField<Color>(
            data,
            'surfaceTintColor',
          ),
          elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
          shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
          borderOnForeground: runtime.unpackRequiredField<bool>(
            data,
            'borderOnForeground',
          ),
          margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
          clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
          semanticContainer: runtime.unpackRequiredField<bool>(
            data,
            'semanticContainer',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'outlined':
        return Card.outlined(
          key: runtime.decodeKey(data),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
          surfaceTintColor: runtime.unpackOptionalField<Color>(
            data,
            'surfaceTintColor',
          ),
          elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
          shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
          borderOnForeground: runtime.unpackRequiredField<bool>(
            data,
            'borderOnForeground',
          ),
          margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
          clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
          semanticContainer: runtime.unpackRequiredField<bool>(
            data,
            'semanticContainer',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      default:
        return Card(
          key: runtime.decodeKey(data),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
          surfaceTintColor: runtime.unpackOptionalField<Color>(
            data,
            'surfaceTintColor',
          ),
          elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
          shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
          borderOnForeground: runtime.unpackRequiredField<bool>(
            data,
            'borderOnForeground',
          ),
          margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
          clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
          semanticContainer: runtime.unpackRequiredField<bool>(
            data,
            'semanticContainer',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
    }
  }
}
