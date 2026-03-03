import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutSpacer {
  FlutSpacer._();

  static Spacer? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Spacer(
      key: runtime.decodeKey(data),
      flex: runtime.unpackRequiredField<int>(data, 'flex'),
    );
  }
}
