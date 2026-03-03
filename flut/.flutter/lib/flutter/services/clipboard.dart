import 'package:flutter/services.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutClipboardData extends FlutValueObject {
  final ClipboardData data;
  const FlutClipboardData(this.data) : super('ClipboardData');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['text'] = data.text;
    return result;
  }

  static ClipboardData flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ClipboardData(
      text: runtime.unpackRequiredField<String>(data, 'text'),
    );
  }
}

class FlutClipboard {
  FlutClipboard._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Clipboard.setData', setData);
    runtime.registerStatic('Clipboard.getData', getData);
  }

  static dynamic setData(FlutRuntime runtime, ClipboardData data) {
    Clipboard.setData(data);
  }

  static dynamic getData(FlutRuntime runtime, String format) {
    return Clipboard.getData(format);
  }
}
