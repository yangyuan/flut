import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutAnimationStatus extends FlutEnumObject<AnimationStatus> {
  const FlutAnimationStatus()
    : super('AnimationStatus', const {
        'dismissed': AnimationStatus.dismissed,
        'forward': AnimationStatus.forward,
        'reverse': AnimationStatus.reverse,
        'completed': AnimationStatus.completed,
      });
}
