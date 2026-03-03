import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/text_style.dart';

class FlutTextTheme extends FlutValueObject {
  final TextTheme textTheme;

  const FlutTextTheme(this.textTheme) : super('TextTheme');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (textTheme.displayLarge != null) {
      result['displayLarge'] = FlutTextStyle(
        textTheme.displayLarge!,
      ).flutEncode();
    }
    if (textTheme.displayMedium != null) {
      result['displayMedium'] = FlutTextStyle(
        textTheme.displayMedium!,
      ).flutEncode();
    }
    if (textTheme.displaySmall != null) {
      result['displaySmall'] = FlutTextStyle(
        textTheme.displaySmall!,
      ).flutEncode();
    }
    if (textTheme.headlineLarge != null) {
      result['headlineLarge'] = FlutTextStyle(
        textTheme.headlineLarge!,
      ).flutEncode();
    }
    if (textTheme.headlineMedium != null) {
      result['headlineMedium'] = FlutTextStyle(
        textTheme.headlineMedium!,
      ).flutEncode();
    }
    if (textTheme.headlineSmall != null) {
      result['headlineSmall'] = FlutTextStyle(
        textTheme.headlineSmall!,
      ).flutEncode();
    }
    if (textTheme.titleLarge != null) {
      result['titleLarge'] = FlutTextStyle(textTheme.titleLarge!).flutEncode();
    }
    if (textTheme.titleMedium != null) {
      result['titleMedium'] = FlutTextStyle(
        textTheme.titleMedium!,
      ).flutEncode();
    }
    if (textTheme.titleSmall != null) {
      result['titleSmall'] = FlutTextStyle(textTheme.titleSmall!).flutEncode();
    }
    if (textTheme.bodyLarge != null) {
      result['bodyLarge'] = FlutTextStyle(textTheme.bodyLarge!).flutEncode();
    }
    if (textTheme.bodyMedium != null) {
      result['bodyMedium'] = FlutTextStyle(textTheme.bodyMedium!).flutEncode();
    }
    if (textTheme.bodySmall != null) {
      result['bodySmall'] = FlutTextStyle(textTheme.bodySmall!).flutEncode();
    }
    if (textTheme.labelLarge != null) {
      result['labelLarge'] = FlutTextStyle(textTheme.labelLarge!).flutEncode();
    }
    if (textTheme.labelMedium != null) {
      result['labelMedium'] = FlutTextStyle(
        textTheme.labelMedium!,
      ).flutEncode();
    }
    if (textTheme.labelSmall != null) {
      result['labelSmall'] = FlutTextStyle(textTheme.labelSmall!).flutEncode();
    }
    return result;
  }

  static TextTheme? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TextTheme(
      displayLarge: runtime.unpackOptionalField<TextStyle>(
        data,
        'displayLarge',
      ),
      displayMedium: runtime.unpackOptionalField<TextStyle>(
        data,
        'displayMedium',
      ),
      displaySmall: runtime.unpackOptionalField<TextStyle>(
        data,
        'displaySmall',
      ),
      headlineLarge: runtime.unpackOptionalField<TextStyle>(
        data,
        'headlineLarge',
      ),
      headlineMedium: runtime.unpackOptionalField<TextStyle>(
        data,
        'headlineMedium',
      ),
      headlineSmall: runtime.unpackOptionalField<TextStyle>(
        data,
        'headlineSmall',
      ),
      titleLarge: runtime.unpackOptionalField<TextStyle>(data, 'titleLarge'),
      titleMedium: runtime.unpackOptionalField<TextStyle>(data, 'titleMedium'),
      titleSmall: runtime.unpackOptionalField<TextStyle>(data, 'titleSmall'),
      bodyLarge: runtime.unpackOptionalField<TextStyle>(data, 'bodyLarge'),
      bodyMedium: runtime.unpackOptionalField<TextStyle>(data, 'bodyMedium'),
      bodySmall: runtime.unpackOptionalField<TextStyle>(data, 'bodySmall'),
      labelLarge: runtime.unpackOptionalField<TextStyle>(data, 'labelLarge'),
      labelMedium: runtime.unpackOptionalField<TextStyle>(data, 'labelMedium'),
      labelSmall: runtime.unpackOptionalField<TextStyle>(data, 'labelSmall'),
    );
  }
}
