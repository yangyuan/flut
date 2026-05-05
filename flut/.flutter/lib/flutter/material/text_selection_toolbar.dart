import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextSelectionToolbar {
  FlutTextSelectionToolbar._();

  static TextSelectionToolbar? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextSelectionToolbar(
      key: runtime.decodeKey(data),
      anchorAbove: runtime.unpackRequiredField<Offset>(data, 'anchorAbove'),
      anchorBelow: runtime.unpackRequiredField<Offset>(data, 'anchorBelow'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}
