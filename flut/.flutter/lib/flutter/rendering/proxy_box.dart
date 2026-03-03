import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutHitTestBehavior extends FlutEnumObject<HitTestBehavior> {
  const FlutHitTestBehavior()
    : super('HitTestBehavior', const {
        'deferToChild': HitTestBehavior.deferToChild,
        'opaque': HitTestBehavior.opaque,
        'translucent': HitTestBehavior.translucent,
      });
}
