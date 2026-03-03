import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutLayoutBuilder {
  FlutLayoutBuilder._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return LayoutBuilder(
      key: runtime.decodeKey(data),
      builder: runtime.unpackRequiredCallback(data, 'builder'),
    );
  }
}
