import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextSelectionControls extends FlutValueObject {
  const FlutTextSelectionControls() : super('TextSelectionControls');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'TextSelectionControls has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static TextSelectionControls? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'TextSelectionControls has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutTextSelectionHandleControls extends FlutValueObject {
  const FlutTextSelectionHandleControls()
    : super('TextSelectionHandleControls');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'TextSelectionHandleControls has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static TextSelectionControls? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'TextSelectionHandleControls has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutEmptyTextSelectionControls extends FlutValueObject {
  final EmptyTextSelectionControls controls;

  const FlutEmptyTextSelectionControls(this.controls)
    : super('EmptyTextSelectionControls');

  @override
  Map<String, dynamic> flutEncode() => flutBaseProps();

  static EmptyTextSelectionControls? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return EmptyTextSelectionControls();
  }
}
