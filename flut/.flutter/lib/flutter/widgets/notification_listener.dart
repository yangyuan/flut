import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutNotificationListener {
  FlutNotificationListener._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return NotificationListener<ScrollNotification>(
      key: runtime.decodeKey(data),
      onNotification: runtime.unpackOptionalCallback(data, 'onNotification'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
