import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/text_painter.dart';

class FlutTextStyle extends FlutValueObject {
  final TextStyle textStyle;

  const FlutTextStyle(this.textStyle) : super('TextStyle');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['inherit'] = textStyle.inherit;
    if (textStyle.color != null) {
      result['color'] = FlutColor(textStyle.color!).flutEncode();
    }
    if (textStyle.backgroundColor != null) {
      result['backgroundColor'] = FlutColor(
        textStyle.backgroundColor!,
      ).flutEncode();
    }
    if (textStyle.fontSize != null) result['fontSize'] = textStyle.fontSize;
    if (textStyle.fontWeight != null) {
      result['fontWeight'] = FlutFontWeight(textStyle.fontWeight!).flutEncode();
    }
    if (textStyle.fontStyle != null) {
      result['fontStyle'] = const FlutFontStyle().flutEncode(
        textStyle.fontStyle!,
      );
    }
    if (textStyle.letterSpacing != null) {
      result['letterSpacing'] = textStyle.letterSpacing;
    }
    if (textStyle.wordSpacing != null) {
      result['wordSpacing'] = textStyle.wordSpacing;
    }
    if (textStyle.textBaseline != null) {
      result['textBaseline'] = const FlutTextBaseline().flutEncode(
        textStyle.textBaseline!,
      );
    }
    if (textStyle.height != null) result['height'] = textStyle.height;
    if (textStyle.leadingDistribution != null) {
      result['leadingDistribution'] = const FlutTextLeadingDistribution()
          .flutEncode(textStyle.leadingDistribution!);
    }
    if (textStyle.foreground != null) {
      result['foreground'] = FlutPaint(textStyle.foreground!).flutEncode();
    }
    if (textStyle.background != null) {
      result['background'] = FlutPaint(textStyle.background!).flutEncode();
    }
    if (textStyle.shadows != null) {
      result['shadows'] = textStyle.shadows!
          .map((s) => FlutShadow(s).flutEncode())
          .toList();
    }
    if (textStyle.fontFamily != null) {
      result['fontFamily'] = textStyle.fontFamily;
    }
    if (textStyle.fontFamilyFallback != null) {
      result['fontFamilyFallback'] = textStyle.fontFamilyFallback;
    }
    if (textStyle.decoration != null) {
      result['decoration'] = FlutTextDecoration(
        textStyle.decoration!,
      ).flutEncode();
    }
    if (textStyle.decorationColor != null) {
      result['decorationColor'] = FlutColor(
        textStyle.decorationColor!,
      ).flutEncode();
    }
    if (textStyle.decorationStyle != null) {
      result['decorationStyle'] = const FlutTextDecorationStyle().flutEncode(
        textStyle.decorationStyle!,
      );
    }
    if (textStyle.decorationThickness != null) {
      result['decorationThickness'] = textStyle.decorationThickness;
    }
    if (textStyle.overflow != null) {
      result['overflow'] = const FlutTextOverflow().flutEncode(
        textStyle.overflow!,
      );
    }
    return result;
  }

  static TextStyle? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TextStyle(
      inherit: runtime.unpackRequiredField<bool>(data, 'inherit'),
      fontSize: runtime.unpackOptionalField<double>(data, 'fontSize'),
      fontWeight: runtime.unpackOptionalField<FontWeight>(data, 'fontWeight'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      fontStyle: runtime.unpackOptionalField<FontStyle>(data, 'fontStyle'),
      letterSpacing: runtime.unpackOptionalField<double>(data, 'letterSpacing'),
      wordSpacing: runtime.unpackOptionalField<double>(data, 'wordSpacing'),
      textBaseline: runtime.unpackOptionalField<TextBaseline>(
        data,
        'textBaseline',
      ),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      leadingDistribution: runtime.unpackOptionalField<TextLeadingDistribution>(
        data,
        'leadingDistribution',
      ),
      foreground: runtime.unpackOptionalField<Paint>(data, 'foreground'),
      background: runtime.unpackOptionalField<Paint>(data, 'background'),
      shadows: runtime.unpackOptionalField<List<Shadow>>(data, 'shadows'),
      fontFamily: runtime.unpackOptionalField<String>(data, 'fontFamily'),
      fontFamilyFallback: runtime.unpackOptionalField<List<String>>(
        data,
        'fontFamilyFallback',
      ),
      decoration: runtime.unpackOptionalField<TextDecoration>(
        data,
        'decoration',
      ),
      decorationColor: runtime.unpackOptionalField<Color>(
        data,
        'decorationColor',
      ),
      decorationStyle: runtime.unpackOptionalField<TextDecorationStyle>(
        data,
        'decorationStyle',
      ),
      decorationThickness: runtime.unpackOptionalField<double>(
        data,
        'decorationThickness',
      ),
      overflow: runtime.unpackOptionalField<TextOverflow>(data, 'overflow'),
    );
  }
}
