import 'package:flutter/painting.dart';
import 'package:flut/flut/object.dart';

class FlutBoxFit extends FlutEnumObject<BoxFit> {
  const FlutBoxFit()
    : super('BoxFit', const {
        'fill': BoxFit.fill,
        'contain': BoxFit.contain,
        'cover': BoxFit.cover,
        'fitWidth': BoxFit.fitWidth,
        'fitHeight': BoxFit.fitHeight,
        'none': BoxFit.none,
        'scaleDown': BoxFit.scaleDown,
      });
}
