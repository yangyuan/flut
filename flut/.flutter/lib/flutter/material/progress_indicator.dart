import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutCircularProgressIndicator {
  FlutCircularProgressIndicator._();

  static CircularProgressIndicator? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CircularProgressIndicator(
      key: runtime.decodeKey(data),
      value: runtime.unpackOptionalField<double>(data, 'value'),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      valueColor: runtime.unpackOptionalField<Animation<Color?>>(
        data,
        'valueColor',
      ),
      strokeWidth: runtime.unpackRequiredField<double>(data, 'strokeWidth'),
      strokeAlign: runtime.unpackOptionalField<double>(data, 'strokeAlign'),
      semanticsLabel: runtime.unpackOptionalField<String>(
        data,
        'semanticsLabel',
      ),
      semanticsValue: runtime.unpackOptionalField<String>(
        data,
        'semanticsValue',
      ),
      strokeCap: runtime.unpackOptionalField<StrokeCap>(data, 'strokeCap'),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      trackGap: runtime.unpackOptionalField<double>(data, 'trackGap'),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      controller: runtime.unpackOptionalField<AnimationController>(
        data,
        'controller',
      ),
    );
  }
}

class FlutLinearProgressIndicator {
  FlutLinearProgressIndicator._();

  static LinearProgressIndicator? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return LinearProgressIndicator(
      key: runtime.decodeKey(data),
      value: runtime.unpackOptionalField<double>(data, 'value'),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      valueColor: runtime.unpackOptionalField<Animation<Color?>>(
        data,
        'valueColor',
      ),
      minHeight: runtime.unpackOptionalField<double>(data, 'minHeight'),
      semanticsLabel: runtime.unpackOptionalField<String>(
        data,
        'semanticsLabel',
      ),
      semanticsValue: runtime.unpackOptionalField<String>(
        data,
        'semanticsValue',
      ),
      borderRadius: runtime.unpackOptionalField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
      stopIndicatorColor: runtime.unpackOptionalField<Color>(
        data,
        'stopIndicatorColor',
      ),
      stopIndicatorRadius: runtime.unpackOptionalField<double>(
        data,
        'stopIndicatorRadius',
      ),
      trackGap: runtime.unpackOptionalField<double>(data, 'trackGap'),
      controller: runtime.unpackOptionalField<AnimationController>(
        data,
        'controller',
      ),
    );
  }
}
