import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutEdgeInsetsGeometry extends FlutValueObject {
  final EdgeInsetsGeometry edgeInsetsGeometry;

  const FlutEdgeInsetsGeometry(this.edgeInsetsGeometry)
    : super('EdgeInsetsGeometry');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (edgeInsetsGeometry is EdgeInsets) {
      final edgeInsets = edgeInsetsGeometry as EdgeInsets;
      result['left'] = edgeInsets.left;
      result['top'] = edgeInsets.top;
      result['right'] = edgeInsets.right;
      result['bottom'] = edgeInsets.bottom;
      result['start'] = 0.0;
      result['end'] = 0.0;
      return result;
    }
    if (edgeInsetsGeometry is EdgeInsetsDirectional) {
      final edgeInsets = edgeInsetsGeometry as EdgeInsetsDirectional;
      result['left'] = 0.0;
      result['top'] = edgeInsets.top;
      result['right'] = 0.0;
      result['bottom'] = edgeInsets.bottom;
      result['start'] = edgeInsets.start;
      result['end'] = edgeInsets.end;
      return result;
    }

    final resolved = edgeInsetsGeometry.resolve(TextDirection.ltr);
    result['left'] = resolved.left;
    result['top'] = resolved.top;
    result['right'] = resolved.right;
    result['bottom'] = resolved.bottom;
    result['start'] = 0.0;
    result['end'] = 0.0;
    return result;
  }

  static EdgeInsetsGeometry? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final left = runtime.unpackOptionalField<double>(data, 'left') ?? 0.0;
    final top = runtime.unpackOptionalField<double>(data, 'top') ?? 0.0;
    final right = runtime.unpackOptionalField<double>(data, 'right') ?? 0.0;
    final bottom = runtime.unpackOptionalField<double>(data, 'bottom') ?? 0.0;
    final start = runtime.unpackOptionalField<double>(data, 'start') ?? 0.0;
    final end = runtime.unpackOptionalField<double>(data, 'end') ?? 0.0;

    if (start == 0.0 && end == 0.0) {
      return EdgeInsets.fromLTRB(left, top, right, bottom);
    }
    if (left == 0.0 && right == 0.0) {
      return EdgeInsetsDirectional.fromSTEB(start, top, end, bottom);
    }

    return EdgeInsets.fromLTRB(
      left,
      top,
      right,
      bottom,
    ).add(EdgeInsetsDirectional.fromSTEB(start, 0.0, end, 0.0));
  }
}

class FlutEdgeInsets extends FlutValueObject {
  final EdgeInsets edgeInsets;

  const FlutEdgeInsets(this.edgeInsets) : super('EdgeInsets');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = edgeInsets.left;
    result['top'] = edgeInsets.top;
    result['right'] = edgeInsets.right;
    result['bottom'] = edgeInsets.bottom;
    return result;
  }

  static EdgeInsets? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return EdgeInsets.fromLTRB(
      runtime.unpackRequiredField<double>(data, 'left'),
      runtime.unpackRequiredField<double>(data, 'top'),
      runtime.unpackRequiredField<double>(data, 'right'),
      runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}

class FlutEdgeInsetsDirectional extends FlutValueObject {
  final EdgeInsetsDirectional edgeInsetsDirectional;

  const FlutEdgeInsetsDirectional(this.edgeInsetsDirectional)
    : super('EdgeInsetsDirectional');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['start'] = edgeInsetsDirectional.start;
    result['top'] = edgeInsetsDirectional.top;
    result['end'] = edgeInsetsDirectional.end;
    result['bottom'] = edgeInsetsDirectional.bottom;
    return result;
  }

  static EdgeInsetsDirectional? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return EdgeInsetsDirectional.fromSTEB(
      runtime.unpackRequiredField<double>(data, 'start'),
      runtime.unpackRequiredField<double>(data, 'top'),
      runtime.unpackRequiredField<double>(data, 'end'),
      runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}
