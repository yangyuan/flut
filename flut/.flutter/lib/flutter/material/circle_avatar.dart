import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutCircleAvatar {
  FlutCircleAvatar._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return CircleAvatar(
      key: runtime.decodeKey(data),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      backgroundImage: runtime.unpackOptionalField<ImageProvider>(
        data,
        'backgroundImage',
      ),
      foregroundImage: runtime.unpackOptionalField<ImageProvider>(
        data,
        'foregroundImage',
      ),
      onBackgroundImageError: runtime.unpackOptionalCallback(
        data,
        'onBackgroundImageError',
      ),
      onForegroundImageError: runtime.unpackOptionalCallback(
        data,
        'onForegroundImageError',
      ),
      foregroundColor: runtime.unpackOptionalField<Color>(
        data,
        'foregroundColor',
      ),
      radius: runtime.unpackOptionalField<double>(data, 'radius'),
      minRadius: runtime.unpackOptionalField<double>(data, 'minRadius'),
      maxRadius: runtime.unpackOptionalField<double>(data, 'maxRadius'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
