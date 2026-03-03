import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutButtonStyle with FlutRealtimeObject<ButtonStyle> {
  FlutButtonStyle.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required ButtonStyle target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutButtonStyle.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ButtonStyle target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ButtonStyle',
      target: target,
    );
  }

  static FlutButtonStyle flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutButtonStyle.createFromData(
      runtime: runtime,
      data: data,
      target: ButtonStyle(
        textStyle: runtime
            .unpackGenericField<WidgetStateProperty<TextStyle?>, TextStyle?>(
              data,
              'textStyle',
            ),
        backgroundColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'backgroundColor',
            ),
        foregroundColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'foregroundColor',
            ),
        overlayColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'overlayColor',
            ),
        shadowColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'shadowColor',
            ),
        surfaceTintColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'surfaceTintColor',
            ),
        elevation: runtime
            .unpackGenericField<WidgetStateProperty<double?>, double?>(
              data,
              'elevation',
            ),
        padding: runtime
            .unpackGenericField<
              WidgetStateProperty<EdgeInsetsGeometry?>,
              EdgeInsetsGeometry?
            >(data, 'padding'),
        minimumSize: runtime
            .unpackGenericField<WidgetStateProperty<Size?>, Size?>(
              data,
              'minimumSize',
            ),
        fixedSize: runtime
            .unpackGenericField<WidgetStateProperty<Size?>, Size?>(
              data,
              'fixedSize',
            ),
        maximumSize: runtime
            .unpackGenericField<WidgetStateProperty<Size?>, Size?>(
              data,
              'maximumSize',
            ),
        iconColor: runtime
            .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
              data,
              'iconColor',
            ),
        iconSize: runtime
            .unpackGenericField<WidgetStateProperty<double?>, double?>(
              data,
              'iconSize',
            ),
        iconAlignment: runtime.unpackOptionalField<IconAlignment>(
          data,
          'iconAlignment',
        ),
        side: runtime
            .unpackGenericField<WidgetStateProperty<BorderSide?>, BorderSide?>(
              data,
              'side',
            ),
        shape: runtime
            .unpackGenericField<
              WidgetStateProperty<OutlinedBorder?>,
              OutlinedBorder?
            >(data, 'shape'),
        mouseCursor: runtime
            .unpackGenericField<
              WidgetStateProperty<MouseCursor?>,
              MouseCursor?
            >(data, 'mouseCursor'),
        visualDensity: runtime.unpackOptionalField<VisualDensity>(
          data,
          'visualDensity',
        ),
        tapTargetSize: runtime.unpackOptionalField<MaterialTapTargetSize>(
          data,
          'tapTargetSize',
        ),
        animationDuration: runtime.unpackOptionalField<Duration>(
          data,
          'animationDuration',
        ),
        enableFeedback: runtime.unpackOptionalField<bool>(
          data,
          'enableFeedback',
        ),
        alignment: runtime.unpackOptionalField<AlignmentGeometry>(
          data,
          'alignment',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'textStyle':
        return flutTarget.textStyle;
      case 'backgroundColor':
        return flutTarget.backgroundColor;
      case 'foregroundColor':
        return flutTarget.foregroundColor;
      case 'overlayColor':
        return flutTarget.overlayColor;
      case 'shadowColor':
        return flutTarget.shadowColor;
      case 'surfaceTintColor':
        return flutTarget.surfaceTintColor;
      case 'elevation':
        return flutTarget.elevation;
      case 'padding':
        return flutTarget.padding;
      case 'minimumSize':
        return flutTarget.minimumSize;
      case 'fixedSize':
        return flutTarget.fixedSize;
      case 'maximumSize':
        return flutTarget.maximumSize;
      case 'iconColor':
        return flutTarget.iconColor;
      case 'iconSize':
        return flutTarget.iconSize;
      case 'iconAlignment':
        return flutTarget.iconAlignment;
      case 'side':
        return flutTarget.side;
      case 'shape':
        return flutTarget.shape;
      case 'mouseCursor':
        return flutTarget.mouseCursor;
      case 'visualDensity':
        return flutTarget.visualDensity;
      case 'tapTargetSize':
        return flutTarget.tapTargetSize;
      case 'animationDuration':
        return flutTarget.animationDuration;
      case 'enableFeedback':
        return flutTarget.enableFeedback;
      case 'alignment':
        return flutTarget.alignment;
      case 'splashFactory':
        return flutTarget.splashFactory;
      case 'backgroundBuilder':
        return flutTarget.backgroundBuilder;
      case 'foregroundBuilder':
        return flutTarget.foregroundBuilder;
    }
    throw FlutUnknownPropertyException('ButtonStyle', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ButtonStyle', property);
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
