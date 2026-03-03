import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';

class FlutPopupMenuPosition extends FlutEnumObject<PopupMenuPosition> {
  const FlutPopupMenuPosition()
    : super('PopupMenuPosition', const {
        'over': PopupMenuPosition.over,
        'under': PopupMenuPosition.under,
      });
}
