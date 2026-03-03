import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutIconThemeData extends FlutValueObject {
  final IconThemeData value;
  const FlutIconThemeData(this.value) : super('IconThemeData');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (value.size != null) result['size'] = value.size;
    if (value.fill != null) result['fill'] = value.fill;
    if (value.weight != null) result['weight'] = value.weight;
    if (value.grade != null) result['grade'] = value.grade;
    if (value.opticalSize != null) result['opticalSize'] = value.opticalSize;
    if (value.color != null) {
      result['color'] = FlutColor(value.color!).flutEncode();
    }
    if (value.opacity != null) result['opacity'] = value.opacity;
    if (value.shadows != null) {
      result['shadows'] = value.shadows!
          .map((s) => FlutShadow(s).flutEncode())
          .toList();
    }
    if (value.applyTextScaling != null) {
      result['applyTextScaling'] = value.applyTextScaling;
    }
    return result;
  }

  static IconThemeData? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return IconThemeData(
      size: runtime.unpackOptionalField<double>(data, 'size'),
      fill: runtime.unpackOptionalField<double>(data, 'fill'),
      weight: runtime.unpackOptionalField<double>(data, 'weight'),
      grade: runtime.unpackOptionalField<double>(data, 'grade'),
      opticalSize: runtime.unpackOptionalField<double>(data, 'opticalSize'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      opacity: runtime.unpackOptionalField<double>(data, 'opacity'),
      shadows: runtime.unpackOptionalField<List<Shadow>>(data, 'shadows'),
      applyTextScaling: runtime.unpackOptionalField<bool>(
        data,
        'applyTextScaling',
      ),
    );
  }
}
