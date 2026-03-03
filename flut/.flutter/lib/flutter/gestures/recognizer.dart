import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';

class FlutDragStartBehavior extends FlutEnumObject<DragStartBehavior> {
  const FlutDragStartBehavior()
    : super('DragStartBehavior', const {
        'down': DragStartBehavior.down,
        'start': DragStartBehavior.start,
      });
}
