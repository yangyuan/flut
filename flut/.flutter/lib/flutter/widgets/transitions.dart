import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutListenableBuilder {
  FlutListenableBuilder._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ListenableBuilder(
      key: runtime.decodeKey(data),
      listenable: runtime.unpackRequiredField<Listenable>(data, 'listenable'),
      builder: runtime.unpackRequiredCallback(data, 'builder'),
    );
  }
}

class FlutAnimatedBuilder {
  FlutAnimatedBuilder._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return AnimatedBuilder(
      key: runtime.decodeKey(data),
      animation: runtime.unpackRequiredField<Listenable>(data, 'animation'),
      builder: runtime.unpackRequiredCallback(data, 'builder'),
    );
  }
}
