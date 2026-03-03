import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutShowValueIndicator extends FlutEnumObject<ShowValueIndicator> {
  const FlutShowValueIndicator()
    : super('ShowValueIndicator', const {
        'onlyForDiscrete': ShowValueIndicator.onlyForDiscrete,
        'onlyForContinuous': ShowValueIndicator.onlyForContinuous,
        'always': ShowValueIndicator.always,
        'onDrag': ShowValueIndicator.onDrag,
        'alwaysVisible': ShowValueIndicator.alwaysVisible,
        'never': ShowValueIndicator.never,
      });
}
