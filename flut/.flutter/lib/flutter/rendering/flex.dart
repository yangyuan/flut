import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutMainAxisSize extends FlutEnumObject<MainAxisSize> {
  const FlutMainAxisSize()
    : super('MainAxisSize', const {
        'min': MainAxisSize.min,
        'max': MainAxisSize.max,
      });
}

class FlutMainAxisAlignment extends FlutEnumObject<MainAxisAlignment> {
  const FlutMainAxisAlignment()
    : super('MainAxisAlignment', const {
        'start': MainAxisAlignment.start,
        'end': MainAxisAlignment.end,
        'center': MainAxisAlignment.center,
        'spaceBetween': MainAxisAlignment.spaceBetween,
        'spaceAround': MainAxisAlignment.spaceAround,
        'spaceEvenly': MainAxisAlignment.spaceEvenly,
      });
}

class FlutCrossAxisAlignment extends FlutEnumObject<CrossAxisAlignment> {
  const FlutCrossAxisAlignment()
    : super('CrossAxisAlignment', const {
        'start': CrossAxisAlignment.start,
        'end': CrossAxisAlignment.end,
        'center': CrossAxisAlignment.center,
        'stretch': CrossAxisAlignment.stretch,
        'baseline': CrossAxisAlignment.baseline,
      });
}

class FlutFlexFit extends FlutEnumObject<FlexFit> {
  const FlutFlexFit()
    : super('FlexFit', const {'tight': FlexFit.tight, 'loose': FlexFit.loose});
}
