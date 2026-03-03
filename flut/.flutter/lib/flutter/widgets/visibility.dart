import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutVisibility {
  FlutVisibility._();

  static Visibility? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return Visibility(
      key: runtime.decodeKey(data),
      visible: runtime.unpackRequiredField<bool>(data, 'visible'),
      maintainState: runtime.unpackRequiredField<bool>(data, 'maintainState'),
      maintainAnimation: runtime.unpackRequiredField<bool>(
        data,
        'maintainAnimation',
      ),
      maintainSize: runtime.unpackRequiredField<bool>(data, 'maintainSize'),
      maintainSemantics: runtime.unpackRequiredField<bool>(
        data,
        'maintainSemantics',
      ),
      maintainInteractivity: runtime.unpackRequiredField<bool>(
        data,
        'maintainInteractivity',
      ),
      maintainFocusability: runtime.unpackRequiredField<bool>(
        data,
        'maintainFocusability',
      ),
      replacement: runtime.unpackRequiredField<Widget>(data, 'replacement'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Visibility.of', _of);
  }

  static dynamic _of(FlutRuntime runtime, BuildContext context) {
    return Visibility.of(context);
  }
}
