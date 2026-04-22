import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutPointerEvent extends FlutValueObject {
  final PointerEvent event;

  FlutPointerEvent(this.event) : super('PointerEvent');

  FlutPointerEvent._(this.event, String type) : super(type);

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['position'] = FlutOffset(event.position).flutEncode();
    result['localPosition'] = FlutOffset(event.localPosition).flutEncode();
    result['delta'] = FlutOffset(event.delta).flutEncode();
    result['localDelta'] = FlutOffset(event.localDelta).flutEncode();
    result['buttons'] = event.buttons;
    result['down'] = event.down;
    result['pointer'] = event.pointer;
    result['device'] = event.device;
    return result;
  }
}

class FlutPointerEnterEvent extends FlutPointerEvent {
  FlutPointerEnterEvent(PointerEnterEvent event)
    : super._(event, 'PointerEnterEvent');
}

class FlutPointerExitEvent extends FlutPointerEvent {
  FlutPointerExitEvent(PointerExitEvent event)
    : super._(event, 'PointerExitEvent');
}

class FlutPointerDownEvent extends FlutPointerEvent {
  FlutPointerDownEvent(PointerDownEvent event)
    : super._(event, 'PointerDownEvent');
}

class FlutPointerUpEvent extends FlutPointerEvent {
  FlutPointerUpEvent(PointerUpEvent event) : super._(event, 'PointerUpEvent');
}
