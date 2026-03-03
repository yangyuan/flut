import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutOutlinedButton {
  FlutOutlinedButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return OutlinedButton(
      key: runtime.decodeKey(data),
      onPressed: runtime.unpackNullableRequiredCallback(data, 'onPressed'),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      statesController: runtime.unpackOptionalField<WidgetStatesController>(
        data,
        'statesController',
      ),
      child: runtime.unpackNullableRequiredField<Widget>(data, 'child'),
    );
  }
}
