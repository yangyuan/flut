import 'dart:typed_data';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flutter/material.dart';

class FlutMatrix4 extends FlutValueObject {
  final Matrix4 matrix;
  const FlutMatrix4(this.matrix) : super('Matrix4');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['storage'] = matrix.storage.toList();
    return result;
  }

  static Matrix4? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final storage = data['storage'] as List<dynamic>;
    return Matrix4.fromFloat64List(
      Float64List.fromList(
        storage.cast<num>().map((e) => e.toDouble()).toList(),
      ),
    );
  }
}
