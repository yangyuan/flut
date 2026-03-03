import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/core.dart';
import 'package:flut/flutter/animation/curves.dart';

class FlutAnimationStyle extends FlutValueObject {
  final AnimationStyle style;

  const FlutAnimationStyle(this.style) : super('AnimationStyle');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (style.curve != null) {
      result['curve'] = FlutCurve(style.curve!).flutEncode();
    }
    if (style.duration != null) {
      result['duration'] = FlutDuration(style.duration!).flutEncode();
    }
    if (style.reverseCurve != null) {
      result['reverseCurve'] = FlutCurve(style.reverseCurve!).flutEncode();
    }
    if (style.reverseDuration != null) {
      result['reverseDuration'] = FlutDuration(
        style.reverseDuration!,
      ).flutEncode();
    }
    return result;
  }

  static AnimationStyle? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AnimationStyle(
      curve: runtime.unpackOptionalField<Curve>(data, 'curve'),
      duration: runtime.unpackOptionalField<Duration>(data, 'duration'),
      reverseCurve: runtime.unpackOptionalField<Curve>(data, 'reverseCurve'),
      reverseDuration: runtime.unpackOptionalField<Duration>(
        data,
        'reverseDuration',
      ),
    );
  }
}
