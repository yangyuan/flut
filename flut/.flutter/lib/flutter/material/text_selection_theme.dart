import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/dart/ui.dart';

class FlutTextSelectionThemeData extends FlutValueObject {
  final TextSelectionThemeData data;

  const FlutTextSelectionThemeData(this.data) : super('TextSelectionThemeData');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (data.cursorColor != null) {
      result['cursorColor'] = FlutColor(data.cursorColor!).flutEncode();
    }
    if (data.selectionColor != null) {
      result['selectionColor'] = FlutColor(data.selectionColor!).flutEncode();
    }
    if (data.selectionHandleColor != null) {
      result['selectionHandleColor'] = FlutColor(
        data.selectionHandleColor!,
      ).flutEncode();
    }
    return result;
  }

  static TextSelectionThemeData? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextSelectionThemeData(
      cursorColor: runtime.unpackOptionalField<Color>(data, 'cursorColor'),
      selectionColor: runtime.unpackOptionalField<Color>(
        data,
        'selectionColor',
      ),
      selectionHandleColor: runtime.unpackOptionalField<Color>(
        data,
        'selectionHandleColor',
      ),
    );
  }
}

class FlutTextSelectionTheme {
  FlutTextSelectionTheme._();

  static TextSelectionTheme? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextSelectionTheme(
      key: runtime.decodeKey(data),
      data: runtime.unpackRequiredField<TextSelectionThemeData>(data, 'data'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('TextSelectionTheme.of', of);
  }

  static TextSelectionThemeData of(FlutRuntime runtime, BuildContext context) {
    return TextSelectionTheme.of(context);
  }
}
