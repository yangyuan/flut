import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutCurve extends FlutValueObject {
  final Curve curve;

  const FlutCurve(this.curve) : super('Curve');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    String kind;
    if (curve == Curves.linear) {
      kind = 'linear';
    } else if (curve == Curves.decelerate) {
      kind = 'decelerate';
    } else if (curve == Curves.ease) {
      kind = 'ease';
    } else if (curve == Curves.easeIn) {
      kind = 'easeIn';
    } else if (curve == Curves.easeInSine) {
      kind = 'easeInSine';
    } else if (curve == Curves.easeInQuad) {
      kind = 'easeInQuad';
    } else if (curve == Curves.easeInCubic) {
      kind = 'easeInCubic';
    } else if (curve == Curves.easeInQuart) {
      kind = 'easeInQuart';
    } else if (curve == Curves.easeInQuint) {
      kind = 'easeInQuint';
    } else if (curve == Curves.easeInExpo) {
      kind = 'easeInExpo';
    } else if (curve == Curves.easeInCirc) {
      kind = 'easeInCirc';
    } else if (curve == Curves.easeInBack) {
      kind = 'easeInBack';
    } else if (curve == Curves.easeOut) {
      kind = 'easeOut';
    } else if (curve == Curves.easeOutSine) {
      kind = 'easeOutSine';
    } else if (curve == Curves.easeOutQuad) {
      kind = 'easeOutQuad';
    } else if (curve == Curves.easeOutCubic) {
      kind = 'easeOutCubic';
    } else if (curve == Curves.easeOutQuart) {
      kind = 'easeOutQuart';
    } else if (curve == Curves.easeOutQuint) {
      kind = 'easeOutQuint';
    } else if (curve == Curves.easeOutExpo) {
      kind = 'easeOutExpo';
    } else if (curve == Curves.easeOutCirc) {
      kind = 'easeOutCirc';
    } else if (curve == Curves.easeOutBack) {
      kind = 'easeOutBack';
    } else if (curve == Curves.easeInOut) {
      kind = 'easeInOut';
    } else if (curve == Curves.easeInOutSine) {
      kind = 'easeInOutSine';
    } else if (curve == Curves.easeInOutQuad) {
      kind = 'easeInOutQuad';
    } else if (curve == Curves.easeInOutCubic) {
      kind = 'easeInOutCubic';
    } else if (curve == Curves.easeInOutCubicEmphasized) {
      kind = 'easeInOutCubicEmphasized';
    } else if (curve == Curves.easeInOutQuart) {
      kind = 'easeInOutQuart';
    } else if (curve == Curves.easeInOutQuint) {
      kind = 'easeInOutQuint';
    } else if (curve == Curves.easeInOutExpo) {
      kind = 'easeInOutExpo';
    } else if (curve == Curves.easeInOutCirc) {
      kind = 'easeInOutCirc';
    } else if (curve == Curves.easeInOutBack) {
      kind = 'easeInOutBack';
    } else if (curve == Curves.fastOutSlowIn) {
      kind = 'fastOutSlowIn';
    } else if (curve == Curves.slowMiddle) {
      kind = 'slowMiddle';
    } else if (curve == Curves.bounceIn) {
      kind = 'bounceIn';
    } else if (curve == Curves.bounceOut) {
      kind = 'bounceOut';
    } else if (curve == Curves.bounceInOut) {
      kind = 'bounceInOut';
    } else if (curve == Curves.elasticIn) {
      kind = 'elasticIn';
    } else if (curve == Curves.elasticOut) {
      kind = 'elasticOut';
    } else if (curve == Curves.elasticInOut) {
      kind = 'elasticInOut';
    } else if (curve == Curves.easeInToLinear) {
      kind = 'easeInToLinear';
    } else if (curve == Curves.linearToEaseOut) {
      kind = 'linearToEaseOut';
    } else if (curve == Curves.fastLinearToSlowEaseIn) {
      kind = 'fastLinearToSlowEaseIn';
    } else if (curve == Curves.fastEaseInToSlowEaseOut) {
      kind = 'fastEaseInToSlowEaseOut';
    } else {
      throw ArgumentError('Cannot encode unknown Curve: $curve');
    }
    result['kind'] = kind;
    return result;
  }

  static Curve? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final kind = runtime.unpackRequiredField<String>(data, 'kind');
    switch (kind) {
      case 'linear':
        return Curves.linear;
      case 'decelerate':
        return Curves.decelerate;
      case 'ease':
        return Curves.ease;
      case 'easeIn':
        return Curves.easeIn;
      case 'easeInSine':
        return Curves.easeInSine;
      case 'easeInQuad':
        return Curves.easeInQuad;
      case 'easeInCubic':
        return Curves.easeInCubic;
      case 'easeInQuart':
        return Curves.easeInQuart;
      case 'easeInQuint':
        return Curves.easeInQuint;
      case 'easeInExpo':
        return Curves.easeInExpo;
      case 'easeInCirc':
        return Curves.easeInCirc;
      case 'easeInBack':
        return Curves.easeInBack;
      case 'easeOut':
        return Curves.easeOut;
      case 'easeOutSine':
        return Curves.easeOutSine;
      case 'easeOutQuad':
        return Curves.easeOutQuad;
      case 'easeOutCubic':
        return Curves.easeOutCubic;
      case 'easeOutQuart':
        return Curves.easeOutQuart;
      case 'easeOutQuint':
        return Curves.easeOutQuint;
      case 'easeOutExpo':
        return Curves.easeOutExpo;
      case 'easeOutCirc':
        return Curves.easeOutCirc;
      case 'easeOutBack':
        return Curves.easeOutBack;
      case 'easeInOut':
        return Curves.easeInOut;
      case 'easeInOutSine':
        return Curves.easeInOutSine;
      case 'easeInOutQuad':
        return Curves.easeInOutQuad;
      case 'easeInOutCubic':
        return Curves.easeInOutCubic;
      case 'easeInOutCubicEmphasized':
        return Curves.easeInOutCubicEmphasized;
      case 'easeInOutQuart':
        return Curves.easeInOutQuart;
      case 'easeInOutQuint':
        return Curves.easeInOutQuint;
      case 'easeInOutExpo':
        return Curves.easeInOutExpo;
      case 'easeInOutCirc':
        return Curves.easeInOutCirc;
      case 'easeInOutBack':
        return Curves.easeInOutBack;
      case 'fastOutSlowIn':
        return Curves.fastOutSlowIn;
      case 'slowMiddle':
        return Curves.slowMiddle;
      case 'bounceIn':
        return Curves.bounceIn;
      case 'bounceOut':
        return Curves.bounceOut;
      case 'bounceInOut':
        return Curves.bounceInOut;
      case 'elasticIn':
        return Curves.elasticIn;
      case 'elasticOut':
        return Curves.elasticOut;
      case 'elasticInOut':
        return Curves.elasticInOut;
      case 'easeInToLinear':
        return Curves.easeInToLinear;
      case 'linearToEaseOut':
        return Curves.linearToEaseOut;
      case 'fastLinearToSlowEaseIn':
        return Curves.fastLinearToSlowEaseIn;
      case 'fastEaseInToSlowEaseOut':
        return Curves.fastEaseInToSlowEaseOut;
    }
    throw ArgumentError('Unknown Curve kind: $kind');
  }
}
