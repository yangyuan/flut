import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutScrollBehavior extends FlutValueObject {
  final ScrollBehavior value;
  const FlutScrollBehavior(this.value) : super('ScrollBehavior');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static ScrollBehavior? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return const ScrollBehavior();
  }
}
