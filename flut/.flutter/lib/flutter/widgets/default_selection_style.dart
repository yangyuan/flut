import 'package:flutter/widgets.dart';
import 'package:flut/flut/runtime.dart';

class FlutDefaultSelectionStyle {
  FlutDefaultSelectionStyle._();

  static DefaultSelectionStyle? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DefaultSelectionStyle(
      key: runtime.decodeKey(data),
      cursorColor: runtime.unpackOptionalField<Color>(data, 'cursorColor'),
      selectionColor: runtime.unpackOptionalField<Color>(
        data,
        'selectionColor',
      ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
