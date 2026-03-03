import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutIconData extends FlutValueObject {
  final IconData iconData;

  const FlutIconData(this.iconData) : super('IconData');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['codePoint'] = iconData.codePoint;
    result['fontFamily'] = iconData.fontFamily;
    result['fontPackage'] = iconData.fontPackage;
    result['matchTextDirection'] = iconData.matchTextDirection;
    result['fontFamilyFallback'] = iconData.fontFamilyFallback;
    return result;
  }

  static IconData? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return IconData(
      runtime.unpackRequiredField<int>(data, 'codePoint'),
      fontFamily: runtime.unpackOptionalField<String>(data, 'fontFamily'),
      fontPackage: runtime.unpackOptionalField<String>(data, 'fontPackage'),
      matchTextDirection: runtime.unpackRequiredField<bool>(
        data,
        'matchTextDirection',
      ),
      fontFamilyFallback: runtime
          .unpackOptionalField<List<dynamic>>(data, 'fontFamilyFallback')
          ?.cast<String>(),
    );
  }
}
