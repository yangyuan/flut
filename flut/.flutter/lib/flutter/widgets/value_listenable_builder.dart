import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:flut/flut/runtime.dart';

class FlutValueListenableBuilder {
  FlutValueListenableBuilder._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ValueListenableBuilder<dynamic>(
      key: runtime.decodeKey(data),
      valueListenable: runtime.unpackRequiredField<ValueListenable<dynamic>>(
        data,
        'valueListenable',
      ),
      builder: runtime.unpackRequiredCallback(data, 'builder'),
    );
  }
}
