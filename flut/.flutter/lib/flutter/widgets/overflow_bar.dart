import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';

class FlutOverflowBarAlignment extends FlutEnumObject<OverflowBarAlignment> {
  const FlutOverflowBarAlignment()
    : super('OverflowBarAlignment', const {
        'start': OverflowBarAlignment.start,
        'end': OverflowBarAlignment.end,
        'center': OverflowBarAlignment.center,
      });
}
