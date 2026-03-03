import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

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

class FlutTextEditingController with FlutRealtimeObject<TextEditingController> {
  FlutTextEditingController.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required TextEditingController target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

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
      case 'hasListeners':
        // ignore: invalid_use_of_protected_member
        return flutTarget.hasListeners;
    }
    throw FlutUnknownPropertyException('TextEditingController', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'text':
        flutTarget.text = (value as String?) ?? '';
        return true;
    }
    throw FlutUnknownPropertyException('TextEditingController', property);
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
      case 'notifyListeners':
        // ignore: invalid_use_of_visible_for_testing_member, invalid_use_of_protected_member
        flutTarget.notifyListeners();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
