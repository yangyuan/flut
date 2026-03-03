import 'package:flutter/rendering.dart';
import 'package:flut/flut/object.dart';

class FlutStackFit extends FlutEnumObject<StackFit> {
  const FlutStackFit()
    : super('StackFit', const {
        'loose': StackFit.loose,
        'expand': StackFit.expand,
        'passthrough': StackFit.passthrough,
      });
}
