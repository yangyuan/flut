import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutDynamicSchemeVariant extends FlutEnumObject<DynamicSchemeVariant> {
  const FlutDynamicSchemeVariant()
    : super('DynamicSchemeVariant', const {
        'tonalSpot': DynamicSchemeVariant.tonalSpot,
        'fidelity': DynamicSchemeVariant.fidelity,
        'monochrome': DynamicSchemeVariant.monochrome,
        'neutral': DynamicSchemeVariant.neutral,
        'vibrant': DynamicSchemeVariant.vibrant,
        'expressive': DynamicSchemeVariant.expressive,
        'content': DynamicSchemeVariant.content,
        'rainbow': DynamicSchemeVariant.rainbow,
        'fruitSalad': DynamicSchemeVariant.fruitSalad,
      });
}

class FlutColorScheme with FlutRealtimeObject<ColorScheme> {
  FlutColorScheme.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ColorScheme target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutColorScheme.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ColorScheme target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ColorScheme',
      target: target,
    );
  }

  static FlutColorScheme flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'fromSeed':
        return FlutColorScheme.createFromData(
          runtime: runtime,
          data: data,
          target: ColorScheme.fromSeed(
            seedColor: runtime.unpackRequiredField<Color>(data, 'seedColor'),
            brightness: runtime.unpackRequiredField<Brightness>(
              data,
              'brightness',
            ),
            dynamicSchemeVariant: runtime
                .unpackRequiredField<DynamicSchemeVariant>(
                  data,
                  'dynamicSchemeVariant',
                ),
            contrastLevel: runtime.unpackRequiredField<double>(
              data,
              'contrastLevel',
            ),
            primary: runtime.unpackOptionalField<Color>(data, 'primary'),
            onPrimary: runtime.unpackOptionalField<Color>(data, 'onPrimary'),
            primaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'primaryContainer',
            ),
            onPrimaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryContainer',
            ),
            primaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'primaryFixed',
            ),
            primaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'primaryFixedDim',
            ),
            onPrimaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryFixed',
            ),
            onPrimaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryFixedVariant',
            ),
            secondary: runtime.unpackOptionalField<Color>(data, 'secondary'),
            onSecondary: runtime.unpackOptionalField<Color>(
              data,
              'onSecondary',
            ),
            secondaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'secondaryContainer',
            ),
            onSecondaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryContainer',
            ),
            secondaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'secondaryFixed',
            ),
            secondaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'secondaryFixedDim',
            ),
            onSecondaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryFixed',
            ),
            onSecondaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryFixedVariant',
            ),
            tertiary: runtime.unpackOptionalField<Color>(data, 'tertiary'),
            onTertiary: runtime.unpackOptionalField<Color>(data, 'onTertiary'),
            tertiaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryContainer',
            ),
            onTertiaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryContainer',
            ),
            tertiaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryFixed',
            ),
            tertiaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryFixedDim',
            ),
            onTertiaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryFixed',
            ),
            onTertiaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryFixedVariant',
            ),
            error: runtime.unpackOptionalField<Color>(data, 'error'),
            onError: runtime.unpackOptionalField<Color>(data, 'onError'),
            errorContainer: runtime.unpackOptionalField<Color>(
              data,
              'errorContainer',
            ),
            onErrorContainer: runtime.unpackOptionalField<Color>(
              data,
              'onErrorContainer',
            ),
            outline: runtime.unpackOptionalField<Color>(data, 'outline'),
            outlineVariant: runtime.unpackOptionalField<Color>(
              data,
              'outlineVariant',
            ),
            surface: runtime.unpackOptionalField<Color>(data, 'surface'),
            onSurface: runtime.unpackOptionalField<Color>(data, 'onSurface'),
            surfaceDim: runtime.unpackOptionalField<Color>(data, 'surfaceDim'),
            surfaceBright: runtime.unpackOptionalField<Color>(
              data,
              'surfaceBright',
            ),
            surfaceContainerLowest: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerLowest',
            ),
            surfaceContainerLow: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerLow',
            ),
            surfaceContainer: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainer',
            ),
            surfaceContainerHigh: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerHigh',
            ),
            surfaceContainerHighest: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerHighest',
            ),
            onSurfaceVariant: runtime.unpackOptionalField<Color>(
              data,
              'onSurfaceVariant',
            ),
            inverseSurface: runtime.unpackOptionalField<Color>(
              data,
              'inverseSurface',
            ),
            onInverseSurface: runtime.unpackOptionalField<Color>(
              data,
              'onInverseSurface',
            ),
            inversePrimary: runtime.unpackOptionalField<Color>(
              data,
              'inversePrimary',
            ),
            shadow: runtime.unpackOptionalField<Color>(data, 'shadow'),
            scrim: runtime.unpackOptionalField<Color>(data, 'scrim'),
            surfaceTint: runtime.unpackOptionalField<Color>(
              data,
              'surfaceTint',
            ),
          ),
        );
      default:
        return FlutColorScheme.createFromData(
          runtime: runtime,
          data: data,
          target: ColorScheme(
            brightness: runtime.unpackRequiredField<Brightness>(
              data,
              'brightness',
            ),
            primary: runtime.unpackRequiredField<Color>(data, 'primary'),
            onPrimary: runtime.unpackRequiredField<Color>(data, 'onPrimary'),
            primaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'primaryContainer',
            ),
            onPrimaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryContainer',
            ),
            primaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'primaryFixed',
            ),
            primaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'primaryFixedDim',
            ),
            onPrimaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryFixed',
            ),
            onPrimaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onPrimaryFixedVariant',
            ),
            secondary: runtime.unpackRequiredField<Color>(data, 'secondary'),
            onSecondary: runtime.unpackRequiredField<Color>(
              data,
              'onSecondary',
            ),
            secondaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'secondaryContainer',
            ),
            onSecondaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryContainer',
            ),
            secondaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'secondaryFixed',
            ),
            secondaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'secondaryFixedDim',
            ),
            onSecondaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryFixed',
            ),
            onSecondaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onSecondaryFixedVariant',
            ),
            tertiary: runtime.unpackOptionalField<Color>(data, 'tertiary'),
            onTertiary: runtime.unpackOptionalField<Color>(data, 'onTertiary'),
            tertiaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryContainer',
            ),
            onTertiaryContainer: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryContainer',
            ),
            tertiaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryFixed',
            ),
            tertiaryFixedDim: runtime.unpackOptionalField<Color>(
              data,
              'tertiaryFixedDim',
            ),
            onTertiaryFixed: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryFixed',
            ),
            onTertiaryFixedVariant: runtime.unpackOptionalField<Color>(
              data,
              'onTertiaryFixedVariant',
            ),
            error: runtime.unpackRequiredField<Color>(data, 'error'),
            onError: runtime.unpackRequiredField<Color>(data, 'onError'),
            errorContainer: runtime.unpackOptionalField<Color>(
              data,
              'errorContainer',
            ),
            onErrorContainer: runtime.unpackOptionalField<Color>(
              data,
              'onErrorContainer',
            ),
            surface: runtime.unpackRequiredField<Color>(data, 'surface'),
            onSurface: runtime.unpackRequiredField<Color>(data, 'onSurface'),
            surfaceDim: runtime.unpackOptionalField<Color>(data, 'surfaceDim'),
            surfaceBright: runtime.unpackOptionalField<Color>(
              data,
              'surfaceBright',
            ),
            surfaceContainerLowest: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerLowest',
            ),
            surfaceContainerLow: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerLow',
            ),
            surfaceContainer: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainer',
            ),
            surfaceContainerHigh: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerHigh',
            ),
            surfaceContainerHighest: runtime.unpackOptionalField<Color>(
              data,
              'surfaceContainerHighest',
            ),
            onSurfaceVariant: runtime.unpackOptionalField<Color>(
              data,
              'onSurfaceVariant',
            ),
            outline: runtime.unpackOptionalField<Color>(data, 'outline'),
            outlineVariant: runtime.unpackOptionalField<Color>(
              data,
              'outlineVariant',
            ),
            shadow: runtime.unpackOptionalField<Color>(data, 'shadow'),
            scrim: runtime.unpackOptionalField<Color>(data, 'scrim'),
            inverseSurface: runtime.unpackOptionalField<Color>(
              data,
              'inverseSurface',
            ),
            onInverseSurface: runtime.unpackOptionalField<Color>(
              data,
              'onInverseSurface',
            ),
            inversePrimary: runtime.unpackOptionalField<Color>(
              data,
              'inversePrimary',
            ),
            surfaceTint: runtime.unpackOptionalField<Color>(
              data,
              'surfaceTint',
            ),
          ),
        );
    }
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'brightness':
        return flutTarget.brightness;
      case 'primary':
        return flutTarget.primary;
      case 'onPrimary':
        return flutTarget.onPrimary;
      case 'primaryContainer':
        return flutTarget.primaryContainer;
      case 'onPrimaryContainer':
        return flutTarget.onPrimaryContainer;
      case 'primaryFixed':
        return flutTarget.primaryFixed;
      case 'primaryFixedDim':
        return flutTarget.primaryFixedDim;
      case 'onPrimaryFixed':
        return flutTarget.onPrimaryFixed;
      case 'onPrimaryFixedVariant':
        return flutTarget.onPrimaryFixedVariant;
      case 'secondary':
        return flutTarget.secondary;
      case 'onSecondary':
        return flutTarget.onSecondary;
      case 'secondaryContainer':
        return flutTarget.secondaryContainer;
      case 'onSecondaryContainer':
        return flutTarget.onSecondaryContainer;
      case 'secondaryFixed':
        return flutTarget.secondaryFixed;
      case 'secondaryFixedDim':
        return flutTarget.secondaryFixedDim;
      case 'onSecondaryFixed':
        return flutTarget.onSecondaryFixed;
      case 'onSecondaryFixedVariant':
        return flutTarget.onSecondaryFixedVariant;
      case 'tertiary':
        return flutTarget.tertiary;
      case 'onTertiary':
        return flutTarget.onTertiary;
      case 'tertiaryContainer':
        return flutTarget.tertiaryContainer;
      case 'onTertiaryContainer':
        return flutTarget.onTertiaryContainer;
      case 'tertiaryFixed':
        return flutTarget.tertiaryFixed;
      case 'tertiaryFixedDim':
        return flutTarget.tertiaryFixedDim;
      case 'onTertiaryFixed':
        return flutTarget.onTertiaryFixed;
      case 'onTertiaryFixedVariant':
        return flutTarget.onTertiaryFixedVariant;
      case 'error':
        return flutTarget.error;
      case 'onError':
        return flutTarget.onError;
      case 'errorContainer':
        return flutTarget.errorContainer;
      case 'onErrorContainer':
        return flutTarget.onErrorContainer;
      case 'surface':
        return flutTarget.surface;
      case 'onSurface':
        return flutTarget.onSurface;
      case 'surfaceDim':
        return flutTarget.surfaceDim;
      case 'surfaceBright':
        return flutTarget.surfaceBright;
      case 'surfaceContainerLowest':
        return flutTarget.surfaceContainerLowest;
      case 'surfaceContainerLow':
        return flutTarget.surfaceContainerLow;
      case 'surfaceContainer':
        return flutTarget.surfaceContainer;
      case 'surfaceContainerHigh':
        return flutTarget.surfaceContainerHigh;
      case 'surfaceContainerHighest':
        return flutTarget.surfaceContainerHighest;
      case 'onSurfaceVariant':
        return flutTarget.onSurfaceVariant;
      case 'outline':
        return flutTarget.outline;
      case 'outlineVariant':
        return flutTarget.outlineVariant;
      case 'shadow':
        return flutTarget.shadow;
      case 'scrim':
        return flutTarget.scrim;
      case 'inversePrimary':
        return flutTarget.inversePrimary;
      case 'inverseSurface':
        return flutTarget.inverseSurface;
      case 'onInverseSurface':
        return flutTarget.onInverseSurface;
      case 'surfaceTint':
        return flutTarget.surfaceTint;
    }
    throw FlutUnknownPropertyException('ColorScheme', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ColorScheme', property);
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
