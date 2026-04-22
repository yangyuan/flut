import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextField {
  FlutTextField._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TextField(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<TextEditingController>(
        data,
        'controller',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      decoration: runtime.unpackOptionalField<InputDecoration>(
        data,
        'decoration',
      ),
      style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
      textAlign: runtime.unpackRequiredField<TextAlign>(data, 'textAlign'),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      readOnly: runtime.unpackRequiredField<bool>(data, 'readOnly'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      obscureText: runtime.unpackRequiredField<bool>(data, 'obscureText'),
      maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
      minLines: runtime.unpackOptionalField<int>(data, 'minLines'),
      expands: runtime.unpackRequiredField<bool>(data, 'expands'),
      maxLength: runtime.unpackOptionalField<int>(data, 'maxLength'),
      onChanged: runtime.unpackOptionalCallback(data, 'onChanged'),
      onEditingComplete: runtime.unpackOptionalCallback(
        data,
        'onEditingComplete',
      ),
      onSubmitted: runtime.unpackOptionalCallback(data, 'onSubmitted'),
      enabled: runtime.unpackOptionalField<bool>(data, 'enabled'),
      cursorWidth: runtime.unpackRequiredField<double>(data, 'cursorWidth'),
      cursorHeight: runtime.unpackOptionalField<double>(data, 'cursorHeight'),
      cursorColor: runtime.unpackOptionalField<Color>(data, 'cursorColor'),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onTapOutside: runtime.unpackOptionalCallback(data, 'onTapOutside'),
      onTapUpOutside: runtime.unpackOptionalCallback(data, 'onTapUpOutside'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
    );
  }
}
