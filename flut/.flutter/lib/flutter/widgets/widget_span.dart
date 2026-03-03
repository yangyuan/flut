import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/text_style.dart';

class FlutWidgetSpan extends FlutValueObject {
  final WidgetSpan widgetSpan;
  const FlutWidgetSpan(this.widgetSpan) : super('WidgetSpan');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['alignment'] = const FlutPlaceholderAlignment().flutEncode(
      widgetSpan.alignment,
    );
    if (widgetSpan.baseline != null) {
      result['baseline'] = const FlutTextBaseline().flutEncode(
        widgetSpan.baseline!,
      );
    }
    if (widgetSpan.style != null) {
      result['style'] = FlutTextStyle(widgetSpan.style!).flutEncode();
    }
    return result;
  }

  static WidgetSpan? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return WidgetSpan(
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
      alignment: runtime.unpackRequiredField<PlaceholderAlignment>(
        data,
        'alignment',
      ),
      baseline: runtime.unpackOptionalField<TextBaseline>(data, 'baseline'),
      style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic(
      'WidgetSpan.extractFromInlineSpan',
      extractFromInlineSpan,
    );
  }

  static dynamic extractFromInlineSpan(
    FlutRuntime runtime,
    InlineSpan span,
    TextScaler textScaler,
  ) {
    return WidgetSpan.extractFromInlineSpan(span, textScaler);
  }
}
