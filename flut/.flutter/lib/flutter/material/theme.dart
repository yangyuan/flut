import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutTheme {
  FlutTheme._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Theme.of', of);
  }

  static ThemeData of(FlutRuntime runtime, BuildContext context) {
    return Theme.of(context);
  }
}
