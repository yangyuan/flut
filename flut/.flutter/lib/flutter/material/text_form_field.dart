import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextFormField {
  FlutTextFormField._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TextFormField(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<TextEditingController>(
        data,
        'controller',
      ),
      initialValue: runtime.unpackOptionalField<String>(data, 'initialValue'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      decoration: runtime.unpackOptionalField<InputDecoration>(
        data,
        'decoration',
      ),
      style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
      textAlign: runtime.unpackRequiredField<TextAlign>(data, 'textAlign'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      readOnly: runtime.unpackRequiredField<bool>(data, 'readOnly'),
      obscureText: runtime.unpackRequiredField<bool>(data, 'obscureText'),
      maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
      minLines: runtime.unpackOptionalField<int>(data, 'minLines'),
      maxLength: runtime.unpackOptionalField<int>(data, 'maxLength'),
      onChanged: runtime.unpackOptionalCallback(data, 'onChanged'),
      onFieldSubmitted: runtime.unpackOptionalCallback(
        data,
        'onFieldSubmitted',
      ),
      onSaved: runtime.unpackOptionalCallback(data, 'onSaved'),
      validator: runtime.unpackOptionalCallback(data, 'validator'),
      enabled: runtime.unpackOptionalField<bool>(data, 'enabled'),
      autovalidateMode: runtime.unpackOptionalField<AutovalidateMode>(
        data,
        'autovalidateMode',
      ),
    );
  }
}
