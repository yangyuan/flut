import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/alignment.dart';

class FlutGradientRotation extends FlutValueObject {
  final GradientRotation rotation;
  const FlutGradientRotation(this.rotation) : super('GradientRotation');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['radians'] = FlutDouble.encode(rotation.radians);
    return result;
  }

  static GradientRotation? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return GradientRotation(
      runtime.unpackRequiredField<double>(data, 'radians'),
    );
  }
}

class FlutLinearGradient extends FlutValueObject {
  final LinearGradient gradient;
  const FlutLinearGradient(this.gradient) : super('LinearGradient');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['begin'] = FlutAlignment(gradient.begin as Alignment).flutEncode();
    result['end'] = FlutAlignment(gradient.end as Alignment).flutEncode();
    result['colors'] = gradient.colors
        .map((c) => FlutColor(c).flutEncode())
        .toList();
    if (gradient.stops != null) {
      result['stops'] = gradient.stops;
    }
    result['tileMode'] = const FlutTileMode().flutEncode(gradient.tileMode)!;
    return result;
  }

  static LinearGradient? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final stops = data['stops'] as List<dynamic>?;
    return LinearGradient(
      begin: runtime.unpackRequiredField<Alignment>(data, 'begin'),
      end: runtime.unpackRequiredField<Alignment>(data, 'end'),
      colors: (data['colors'] as List<dynamic>)
          .map((c) => runtime.decodeObject<Color>(c)!)
          .toList(),
      stops: stops?.map((s) => (s as num).toDouble()).toList(),
      tileMode: runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
      transform: runtime.unpackOptionalField<GradientTransform>(
        data,
        'transform',
      ),
    );
  }
}

class FlutRadialGradient extends FlutValueObject {
  final RadialGradient gradient;
  const FlutRadialGradient(this.gradient) : super('RadialGradient');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['center'] = FlutAlignment(gradient.center as Alignment).flutEncode();
    result['radius'] = FlutDouble.encode(gradient.radius);
    result['colors'] = gradient.colors
        .map((c) => FlutColor(c).flutEncode())
        .toList();
    if (gradient.stops != null) {
      result['stops'] = gradient.stops;
    }
    result['tileMode'] = const FlutTileMode().flutEncode(gradient.tileMode)!;
    if (gradient.focal != null) {
      result['focal'] = FlutAlignment(
        gradient.focal! as Alignment,
      ).flutEncode();
    }
    result['focalRadius'] = FlutDouble.encode(gradient.focalRadius);
    return result;
  }

  static RadialGradient? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final stops = data['stops'] as List<dynamic>?;
    return RadialGradient(
      center: runtime.unpackRequiredField<Alignment>(data, 'center'),
      radius: runtime.unpackRequiredField<double>(data, 'radius'),
      colors: (data['colors'] as List<dynamic>)
          .map((c) => runtime.decodeObject<Color>(c)!)
          .toList(),
      stops: stops?.map((s) => (s as num).toDouble()).toList(),
      tileMode: runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
      focal: runtime.unpackOptionalField<Alignment>(data, 'focal'),
      focalRadius: runtime.unpackRequiredField<double>(data, 'focalRadius'),
      transform: runtime.unpackOptionalField<GradientTransform>(
        data,
        'transform',
      ),
    );
  }
}

class FlutSweepGradient extends FlutValueObject {
  final SweepGradient gradient;
  const FlutSweepGradient(this.gradient) : super('SweepGradient');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['center'] = FlutAlignment(gradient.center as Alignment).flutEncode();
    result['startAngle'] = FlutDouble.encode(gradient.startAngle);
    result['endAngle'] = FlutDouble.encode(gradient.endAngle);
    result['colors'] = gradient.colors
        .map((c) => FlutColor(c).flutEncode())
        .toList();
    if (gradient.stops != null) {
      result['stops'] = gradient.stops;
    }
    result['tileMode'] = const FlutTileMode().flutEncode(gradient.tileMode)!;
    return result;
  }

  static SweepGradient? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final stops = data['stops'] as List<dynamic>?;
    return SweepGradient(
      center: runtime.unpackRequiredField<Alignment>(data, 'center'),
      startAngle: runtime.unpackRequiredField<double>(data, 'startAngle'),
      endAngle: runtime.unpackRequiredField<double>(data, 'endAngle'),
      colors: (data['colors'] as List<dynamic>)
          .map((c) => runtime.decodeObject<Color>(c)!)
          .toList(),
      stops: stops?.map((s) => (s as num).toDouble()).toList(),
      tileMode: runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
      transform: runtime.unpackOptionalField<GradientTransform>(
        data,
        'transform',
      ),
    );
  }
}
