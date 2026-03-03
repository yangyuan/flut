import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutMaterialTapTargetSize extends FlutEnumObject<MaterialTapTargetSize> {
  const FlutMaterialTapTargetSize()
    : super('MaterialTapTargetSize', const {
        'padded': MaterialTapTargetSize.padded,
        'shrinkWrap': MaterialTapTargetSize.shrinkWrap,
      });
}

class FlutVisualDensity extends FlutValueObject {
  final VisualDensity value;
  const FlutVisualDensity(this.value) : super('VisualDensity');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['horizontal'] = FlutDouble.encode(value.horizontal);
    result['vertical'] = FlutDouble.encode(value.vertical);
    return result;
  }

  static VisualDensity? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return VisualDensity(
      horizontal: runtime.unpackRequiredField<double>(data, 'horizontal'),
      vertical: runtime.unpackRequiredField<double>(data, 'vertical'),
    );
  }
}

class FlutThemeData with FlutRealtimeObject<ThemeData> {
  FlutThemeData.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ThemeData target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutThemeData.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ThemeData target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ThemeData',
      target: target,
    );
  }

  static FlutThemeData flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutThemeData.createFromData(
      runtime: runtime,
      data: data,
      target: ThemeData(
        colorScheme: runtime.unpackOptionalField<ColorScheme>(
          data,
          'colorScheme',
        ),
        brightness: runtime.unpackOptionalField<Brightness>(data, 'brightness'),
        colorSchemeSeed: runtime.unpackOptionalField<Color>(
          data,
          'colorSchemeSeed',
        ),
        useMaterial3: runtime.unpackOptionalField<bool>(data, 'useMaterial3'),
        textTheme: runtime.unpackOptionalField<TextTheme>(data, 'textTheme'),
        primaryTextTheme: runtime.unpackOptionalField<TextTheme>(
          data,
          'primaryTextTheme',
        ),
        fontFamily: runtime.unpackOptionalField<String>(data, 'fontFamily'),
        fontFamilyFallback: runtime.unpackOptionalField<List<String>>(
          data,
          'fontFamilyFallback',
        ),
        primaryColor: runtime.unpackOptionalField<Color>(data, 'primaryColor'),
        primaryColorDark: runtime.unpackOptionalField<Color>(
          data,
          'primaryColorDark',
        ),
        primaryColorLight: runtime.unpackOptionalField<Color>(
          data,
          'primaryColorLight',
        ),
        canvasColor: runtime.unpackOptionalField<Color>(data, 'canvasColor'),
        cardColor: runtime.unpackOptionalField<Color>(data, 'cardColor'),
        scaffoldBackgroundColor: runtime.unpackOptionalField<Color>(
          data,
          'scaffoldBackgroundColor',
        ),
        dividerColor: runtime.unpackOptionalField<Color>(data, 'dividerColor'),
        focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
        highlightColor: runtime.unpackOptionalField<Color>(
          data,
          'highlightColor',
        ),
        hintColor: runtime.unpackOptionalField<Color>(data, 'hintColor'),
        hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
        shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
        splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
        disabledColor: runtime.unpackOptionalField<Color>(
          data,
          'disabledColor',
        ),
        unselectedWidgetColor: runtime.unpackOptionalField<Color>(
          data,
          'unselectedWidgetColor',
        ),
        secondaryHeaderColor: runtime.unpackOptionalField<Color>(
          data,
          'secondaryHeaderColor',
        ),
        materialTapTargetSize: runtime
            .unpackOptionalField<MaterialTapTargetSize>(
              data,
              'materialTapTargetSize',
            ),
        platform: runtime.unpackOptionalField<TargetPlatform>(data, 'platform'),
        applyElevationOverlayColor: runtime.unpackOptionalField<bool>(
          data,
          'applyElevationOverlayColor',
        ),
        useSystemColors: runtime.unpackOptionalField<bool>(
          data,
          'useSystemColors',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'brightness':
        return flutTarget.brightness;
      case 'colorScheme':
        return flutTarget.colorScheme;
      case 'useMaterial3':
        return flutTarget.useMaterial3;
      case 'textTheme':
        return flutTarget.textTheme;
      case 'primaryColor':
        return flutTarget.primaryColor;
      case 'primaryColorDark':
        return flutTarget.primaryColorDark;
      case 'primaryColorLight':
        return flutTarget.primaryColorLight;
      case 'canvasColor':
        return flutTarget.canvasColor;
      case 'cardColor':
        return flutTarget.cardColor;
      case 'scaffoldBackgroundColor':
        return flutTarget.scaffoldBackgroundColor;
      case 'dividerColor':
        return flutTarget.dividerColor;
      case 'focusColor':
        return flutTarget.focusColor;
      case 'highlightColor':
        return flutTarget.highlightColor;
      case 'hintColor':
        return flutTarget.hintColor;
      case 'hoverColor':
        return flutTarget.hoverColor;
      case 'shadowColor':
        return flutTarget.shadowColor;
      case 'splashColor':
        return flutTarget.splashColor;
      case 'disabledColor':
        return flutTarget.disabledColor;
      case 'unselectedWidgetColor':
        return flutTarget.unselectedWidgetColor;
      case 'secondaryHeaderColor':
        return flutTarget.secondaryHeaderColor;
      case 'primaryTextTheme':
        return flutTarget.primaryTextTheme;
      case 'iconTheme':
        return flutTarget.iconTheme;
      case 'primaryIconTheme':
        return flutTarget.primaryIconTheme;
      case 'platform':
        return flutTarget.platform;
      case 'materialTapTargetSize':
        return flutTarget.materialTapTargetSize;
      case 'applyElevationOverlayColor':
        return flutTarget.applyElevationOverlayColor;
      case 'visualDensity':
        return flutTarget.visualDensity;
      case 'typography':
        return flutTarget.typography;
    }
    throw FlutUnknownPropertyException('ThemeData', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ThemeData', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    throw FlutUnknownMethodException(method);
  }
}
