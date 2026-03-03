import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutAnimatedContainer {
  FlutAnimatedContainer._();

  static AnimatedContainer? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AnimatedContainer(
      key: runtime.decodeKey(data),
      alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      decoration: runtime.unpackOptionalField<BoxDecoration>(
        data,
        'decoration',
      ),
      foregroundDecoration: runtime.unpackOptionalField<BoxDecoration>(
        data,
        'foregroundDecoration',
      ),
      width: runtime.unpackOptionalField<double>(data, 'width'),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
      transform: runtime.unpackOptionalField<Matrix4>(data, 'transform'),
      transformAlignment: runtime.unpackOptionalField<Alignment>(
        data,
        'transformAlignment',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      curve: runtime.unpackRequiredField<Curve>(data, 'curve'),
      duration: runtime.unpackRequiredField<Duration>(data, 'duration'),
      onEnd: runtime.unpackOptionalCallback(data, 'onEnd'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutAnimatedOpacity {
  FlutAnimatedOpacity._();

  static AnimatedOpacity? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AnimatedOpacity(
      key: runtime.decodeKey(data),
      opacity: runtime.unpackRequiredField<double>(data, 'opacity'),
      curve: runtime.unpackRequiredField<Curve>(data, 'curve'),
      duration: runtime.unpackRequiredField<Duration>(data, 'duration'),
      onEnd: runtime.unpackOptionalCallback(data, 'onEnd'),
      alwaysIncludeSemantics: runtime.unpackRequiredField<bool>(
        data,
        'alwaysIncludeSemantics',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
