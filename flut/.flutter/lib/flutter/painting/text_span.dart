import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/text_style.dart';

class FlutTextSpan extends FlutValueObject {
  final TextSpan textSpan;

  const FlutTextSpan(this.textSpan) : super('TextSpan');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (textSpan.text != null) {
      result['text'] = textSpan.text;
    }
    if (textSpan.style != null) {
      result['style'] = FlutTextStyle(textSpan.style!).flutEncode();
    }
    if (textSpan.children != null && textSpan.children!.isNotEmpty) {
      result['children'] = textSpan.children!
          .map((child) {
            if (child is TextSpan) return FlutTextSpan(child).flutEncode();
            return null;
          })
          .where((e) => e != null)
          .toList();
    }
    if (textSpan.semanticsLabel != null) {
      result['semanticsLabel'] = textSpan.semanticsLabel;
    }
    if (textSpan.semanticsIdentifier != null) {
      result['semanticsIdentifier'] = textSpan.semanticsIdentifier;
    }
    if (textSpan.spellOut != null) {
      result['spellOut'] = textSpan.spellOut;
    }
    return result;
  }

  static TextSpan? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TextSpan(
      text: runtime.unpackOptionalField<String>(data, 'text'),
      style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
      children: runtime.unpackOptionalField<List<InlineSpan>>(data, 'children'),
      recognizer: runtime.unpackOptionalField<GestureRecognizer>(
        data,
        'recognizer',
      ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      onEnter: runtime.unpackOptionalCallback(data, 'onEnter'),
      onExit: runtime.unpackOptionalCallback(data, 'onExit'),
      semanticsLabel: runtime.unpackOptionalField<String>(
        data,
        'semanticsLabel',
      ),
      semanticsIdentifier: runtime.unpackOptionalField<String>(
        data,
        'semanticsIdentifier',
      ),
      locale: runtime.unpackOptionalField<Locale>(data, 'locale'),
      spellOut: runtime.unpackOptionalField<bool>(data, 'spellOut'),
    );
  }
}
