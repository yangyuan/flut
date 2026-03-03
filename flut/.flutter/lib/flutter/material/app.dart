import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutThemeMode extends FlutEnumObject<ThemeMode> {
  const FlutThemeMode()
    : super('ThemeMode', const {
        'system': ThemeMode.system,
        'light': ThemeMode.light,
        'dark': ThemeMode.dark,
      });
}

class FlutMaterialApp {
  FlutMaterialApp._();

  static MaterialApp? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return MaterialApp(
      key: runtime.decodeKey(data),
      title: runtime.unpackRequiredField<String>(data, 'title'),
      theme: runtime.unpackOptionalField<ThemeData>(data, 'theme'),
      darkTheme: runtime.unpackOptionalField<ThemeData>(data, 'darkTheme'),
      highContrastTheme: runtime.unpackOptionalField<ThemeData>(
        data,
        'highContrastTheme',
      ),
      highContrastDarkTheme: runtime.unpackOptionalField<ThemeData>(
        data,
        'highContrastDarkTheme',
      ),
      themeMode: runtime.unpackOptionalField<ThemeMode>(data, 'themeMode'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      debugShowCheckedModeBanner: runtime.unpackRequiredField<bool>(
        data,
        'debugShowCheckedModeBanner',
      ),
      home: runtime.unpackOptionalField<Widget>(data, 'home'),
    );
  }
}
