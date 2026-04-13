import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutOutlinedButton {
  FlutOutlinedButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'icon':
        return OutlinedButton.icon(
          key: runtime.decodeKey(data),
          onPressed: runtime.unpackNullableRequiredCallback(data, 'onPressed'),
          onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
          onHover: runtime.unpackOptionalCallback(data, 'onHover'),
          onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
          style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
          statesController: runtime.unpackOptionalField<WidgetStatesController>(
            data,
            'statesController',
          ),
          icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
          label: runtime.unpackRequiredField<Widget>(data, 'label'),
          iconAlignment: runtime.unpackOptionalField<IconAlignment>(
            data,
            'iconAlignment',
          ),
        );
      default:
        return OutlinedButton(
          key: runtime.decodeKey(data),
          onPressed: runtime.unpackNullableRequiredCallback(data, 'onPressed'),
          onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
          onHover: runtime.unpackOptionalCallback(data, 'onHover'),
          onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
          style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
          statesController: runtime.unpackOptionalField<WidgetStatesController>(
            data,
            'statesController',
          ),
          child: runtime.unpackNullableRequiredField<Widget>(data, 'child'),
        );
    }
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('OutlinedButton.styleFrom', styleFrom);
  }

  static dynamic styleFrom(
    FlutRuntime runtime, {
    Color? foregroundColor,
    Color? backgroundColor,
    Color? disabledForegroundColor,
    Color? disabledBackgroundColor,
    Color? shadowColor,
    Color? surfaceTintColor,
    Color? iconColor,
    double? iconSize,
    IconAlignment? iconAlignment,
    Color? disabledIconColor,
    Color? overlayColor,
    double? elevation,
    TextStyle? textStyle,
    EdgeInsetsGeometry? padding,
    Size? minimumSize,
    Size? fixedSize,
    Size? maximumSize,
    BorderSide? side,
    OutlinedBorder? shape,
    MouseCursor? enabledMouseCursor,
    MouseCursor? disabledMouseCursor,
    VisualDensity? visualDensity,
    MaterialTapTargetSize? tapTargetSize,
    Duration? animationDuration,
    bool? enableFeedback,
    AlignmentGeometry? alignment,
    InteractiveInkFeatureFactory? splashFactory,
  }) {
    return OutlinedButton.styleFrom(
      foregroundColor: foregroundColor,
      backgroundColor: backgroundColor,
      disabledForegroundColor: disabledForegroundColor,
      disabledBackgroundColor: disabledBackgroundColor,
      shadowColor: shadowColor,
      surfaceTintColor: surfaceTintColor,
      iconColor: iconColor,
      iconSize: iconSize,
      iconAlignment: iconAlignment,
      disabledIconColor: disabledIconColor,
      overlayColor: overlayColor,
      elevation: elevation,
      textStyle: textStyle,
      padding: padding,
      minimumSize: minimumSize,
      fixedSize: fixedSize,
      maximumSize: maximumSize,
      side: side,
      shape: shape,
      enabledMouseCursor: enabledMouseCursor,
      disabledMouseCursor: disabledMouseCursor,
      visualDensity: visualDensity,
      tapTargetSize: tapTargetSize,
      animationDuration: animationDuration,
      enableFeedback: enableFeedback,
      alignment: alignment,
      splashFactory: splashFactory,
    );
  }
}
