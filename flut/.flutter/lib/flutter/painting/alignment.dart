import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutAlignmentGeometry extends FlutValueObject {
  final AlignmentGeometry alignmentGeometry;

  const FlutAlignmentGeometry(this.alignmentGeometry)
    : super('AlignmentGeometry');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'Mixed AlignmentGeometry values are not supported yet. '
      'Only Alignment and AlignmentDirectional are supported.',
    );
  }
}

class FlutAlignment extends FlutValueObject {
  final Alignment alignment;

  const FlutAlignment(this.alignment) : super('Alignment');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['x'] = alignment.x;
    result['start'] = 0.0;
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
    result['x'] = 0.0;
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
