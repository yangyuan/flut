import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

class _FlutTextEditingController extends TextEditingController {
  final FlutRuntime _runtime;
  final int? _buildTextSpanId;

  _FlutTextEditingController({
    required FlutRuntime runtime,
    super.text,
    int? buildTextSpanId,
  }) : _runtime = runtime,
       _buildTextSpanId = buildTextSpanId;

  @override
  TextSpan buildTextSpan({
    required BuildContext context,
    TextStyle? style,
    required bool withComposing,
  }) {
    final buildTextSpanId = _buildTextSpanId;
    if (buildTextSpanId != null) {
      final decoded = _runtime.callAction<TextSpan>(
        buildTextSpanId,
        kwargs: {
          'context': context,
          'style': style,
          'withComposing': withComposing,
        },
      );
      if (decoded != null) {
        return decoded;
      }
    }
    return super.buildTextSpan(
      context: context,
      style: style,
      withComposing: withComposing,
    );
  }
}

class FlutTextEditingController
    extends FlutChangeNotifier<TextEditingController> {
  FlutTextEditingController.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  static FlutTextEditingController flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutTextEditingController.createFromData(
      runtime: runtime,
      data: data,
      target: _FlutTextEditingController(
        runtime: runtime,
        text: runtime.unpackOptionalField<String>(data, 'text'),
        buildTextSpanId: runtime.unpackOptionalField<int>(
          data,
          'buildTextSpan',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'text':
        return flutTarget.text;
    }
    return super.getRawProperty(property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'text':
        flutTarget.text = (value as String?) ?? '';
        return true;
    }
    return super.setProperty(property, value);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'clear':
        flutTarget.clear();
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}
