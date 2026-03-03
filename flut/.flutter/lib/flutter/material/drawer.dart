import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutDrawer {
  FlutDrawer._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Drawer(
      key: runtime.decodeKey(data),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      width: runtime.unpackOptionalField<double>(data, 'width'),
      semanticLabel: runtime.unpackOptionalField<String>(data, 'semanticLabel'),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
