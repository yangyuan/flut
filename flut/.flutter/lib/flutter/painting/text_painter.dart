import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutTextOverflow extends FlutEnumObject<TextOverflow> {
  const FlutTextOverflow()
    : super('TextOverflow', const {
        'clip': TextOverflow.clip,
        'fade': TextOverflow.fade,
        'ellipsis': TextOverflow.ellipsis,
        'visible': TextOverflow.visible,
      });
}

class FlutTextWidthBasis extends FlutEnumObject<TextWidthBasis> {
  const FlutTextWidthBasis()
    : super('TextWidthBasis', const {
        'parent': TextWidthBasis.parent,
        'longestLine': TextWidthBasis.longestLine,
      });
}
