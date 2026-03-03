import 'package:flutter/painting.dart';
import 'package:flut/flut/object.dart';

class FlutAxis extends FlutEnumObject<Axis> {
  const FlutAxis()
    : super('Axis', const {
        'horizontal': Axis.horizontal,
        'vertical': Axis.vertical,
      });
}

class FlutAxisDirection extends FlutEnumObject<AxisDirection> {
  const FlutAxisDirection()
    : super('AxisDirection', const {
        'up': AxisDirection.up,
        'right': AxisDirection.right,
        'down': AxisDirection.down,
        'left': AxisDirection.left,
      });
}

class FlutVerticalDirection extends FlutEnumObject<VerticalDirection> {
  const FlutVerticalDirection()
    : super('VerticalDirection', const {
        'up': VerticalDirection.up,
        'down': VerticalDirection.down,
      });
}
