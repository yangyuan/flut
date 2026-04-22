import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';

class FlutScrollbarOrientation extends FlutEnumObject<ScrollbarOrientation> {
  const FlutScrollbarOrientation()
    : super('ScrollbarOrientation', const {
        'left': ScrollbarOrientation.left,
        'right': ScrollbarOrientation.right,
        'top': ScrollbarOrientation.top,
        'bottom': ScrollbarOrientation.bottom,
      });
}
