import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/border_radius.dart';
import 'package:flut/flutter/painting/box_border.dart';
import 'package:flut/flutter/painting/box_shadow.dart';
import 'package:flut/flutter/painting/gradient.dart';

class FlutBoxDecoration extends FlutValueObject {
  final BoxDecoration boxDecoration;

  const FlutBoxDecoration(this.boxDecoration) : super('BoxDecoration');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (boxDecoration.color != null) {
      result['color'] = FlutColor(boxDecoration.color!).flutEncode();
    }
    if (boxDecoration.border != null && boxDecoration.border is Border) {
      result['border'] = FlutBorder(
        boxDecoration.border! as Border,
      ).flutEncode();
    }
    if (boxDecoration.borderRadius != null &&
        boxDecoration.borderRadius is BorderRadius) {
      result['borderRadius'] = FlutBorderRadius(
        boxDecoration.borderRadius! as BorderRadius,
      ).flutEncode();
    }
    if (boxDecoration.boxShadow != null) {
      result['boxShadow'] = boxDecoration.boxShadow!
          .map((s) => FlutBoxShadow(s).flutEncode())
          .toList();
    }
    if (boxDecoration.gradient != null) {
      if (boxDecoration.gradient is LinearGradient) {
        result['gradient'] = FlutLinearGradient(
          boxDecoration.gradient! as LinearGradient,
        ).flutEncode();
      } else if (boxDecoration.gradient is RadialGradient) {
        result['gradient'] = FlutRadialGradient(
          boxDecoration.gradient! as RadialGradient,
        ).flutEncode();
      } else if (boxDecoration.gradient is SweepGradient) {
        result['gradient'] = FlutSweepGradient(
          boxDecoration.gradient! as SweepGradient,
        ).flutEncode();
      }
    }
    return result;
  }

  static BoxDecoration? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    List<BoxShadow>? boxShadow;
    final boxShadowData = data['boxShadow'] as List<dynamic>?;
    if (boxShadowData != null) {
      boxShadow = boxShadowData
          .map(
            (s) =>
                FlutBoxShadow.flutDecode(runtime, s as Map<String, dynamic>)!,
          )
          .toList();
    }
    Gradient? gradient;
    final gradientData = data['gradient'] as Map<String, dynamic>?;
    if (gradientData != null) {
      gradient = runtime.decodeObject<Gradient>(gradientData);
    }
    return BoxDecoration(
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      border: runtime.unpackOptionalField<Border>(data, 'border'),
      borderRadius: runtime.unpackOptionalField<BorderRadius>(
        data,
        'borderRadius',
      ),
      boxShadow: boxShadow,
      gradient: gradient,
      backgroundBlendMode: runtime.unpackOptionalField<BlendMode>(
        data,
        'backgroundBlendMode',
      ),
      shape: runtime.unpackRequiredField<BoxShape>(data, 'shape'),
    );
  }
}
