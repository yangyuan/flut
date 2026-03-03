import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutWrapAlignment extends FlutEnumObject<WrapAlignment> {
  const FlutWrapAlignment()
    : super('WrapAlignment', const {
        'start': WrapAlignment.start,
        'end': WrapAlignment.end,
        'center': WrapAlignment.center,
        'spaceBetween': WrapAlignment.spaceBetween,
        'spaceAround': WrapAlignment.spaceAround,
        'spaceEvenly': WrapAlignment.spaceEvenly,
      });
}

class FlutWrapCrossAlignment extends FlutEnumObject<WrapCrossAlignment> {
  const FlutWrapCrossAlignment()
    : super('WrapCrossAlignment', const {
        'start': WrapCrossAlignment.start,
        'end': WrapCrossAlignment.end,
        'center': WrapCrossAlignment.center,
      });
}
