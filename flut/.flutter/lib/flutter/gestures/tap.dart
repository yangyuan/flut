import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutTapDownDetails extends FlutValueObject {
  final TapDownDetails details;

  const FlutTapDownDetails(this.details) : super('TapDownDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    if (details.kind != null) {
      result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind!);
    }
    return result;
  }
}

class FlutTapUpDetails extends FlutValueObject {
  final TapUpDetails details;

  const FlutTapUpDetails(this.details) : super('TapUpDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind);
    return result;
  }
}
