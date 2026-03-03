import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/basic_types.dart';

class FlutScrollMetrics extends FlutValueObject {
  final ScrollMetrics metrics;
  const FlutScrollMetrics(this.metrics) : super('ScrollMetrics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['pixels'] = metrics.pixels;
    result['minScrollExtent'] = metrics.minScrollExtent;
    result['maxScrollExtent'] = metrics.maxScrollExtent;
    result['viewportDimension'] = metrics.viewportDimension;
    result['axisDirection'] = const FlutAxisDirection().flutEncode(
      metrics.axisDirection,
    );
    return result;
  }
}
