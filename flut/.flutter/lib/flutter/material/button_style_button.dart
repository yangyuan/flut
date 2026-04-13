import 'package:flut/flut/object.dart';
import 'package:flutter/material.dart';

class FlutIconAlignment extends FlutEnumObject<IconAlignment> {
  const FlutIconAlignment()
    : super('IconAlignment', const {
        'start': IconAlignment.start,
        'end': IconAlignment.end,
      });
}
