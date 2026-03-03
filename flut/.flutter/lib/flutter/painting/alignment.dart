import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutAlignment extends FlutValueObject {
  final Alignment alignment;

  const FlutAlignment(this.alignment) : super('Alignment');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['x'] = alignment.x;
    result['y'] = alignment.y;
    return result;
  }

  static Alignment? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Alignment(
      runtime.unpackRequiredField<double>(data, 'x'),
      runtime.unpackRequiredField<double>(data, 'y'),
    );
  }
}

class FlutAlignmentDirectional extends FlutValueObject {
  final AlignmentDirectional alignmentDirectional;

  const FlutAlignmentDirectional(this.alignmentDirectional)
    : super('AlignmentDirectional');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['start'] = alignmentDirectional.start;
    result['y'] = alignmentDirectional.y;
    return result;
  }

  static AlignmentDirectional? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AlignmentDirectional(
      runtime.unpackRequiredField<double>(data, 'start'),
      runtime.unpackRequiredField<double>(data, 'y'),
    );
  }
}
