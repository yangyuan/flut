import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutRadioGroup {
  FlutRadioGroup._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return RadioGroup<dynamic>(
      key: runtime.decodeKey(data),
      groupValue: runtime.unpackDynamicOptionalField(data, 'groupValue'),
      onChanged: runtime.unpackRequiredCallback(data, 'onChanged'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
