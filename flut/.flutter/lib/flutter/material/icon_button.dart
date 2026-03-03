import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutIconButton {
  FlutIconButton._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('IconButton.styleFrom', styleFrom);
  }

  static dynamic styleFrom(
    FlutRuntime runtime, {
    Color? foregroundColor,
    Color? backgroundColor,
    Color? disabledForegroundColor,
    Color? disabledBackgroundColor,
    Color? focusColor,
    Color? hoverColor,
    Color? highlightColor,
    Color? shadowColor,
    Color? surfaceTintColor,
    Color? overlayColor,
    double? elevation,
    Size? minimumSize,
    Size? fixedSize,
    Size? maximumSize,
    double? iconSize,
    BorderSide? side,
    OutlinedBorder? shape,
    EdgeInsetsGeometry? padding,
    MouseCursor? enabledMouseCursor,
    MouseCursor? disabledMouseCursor,
    VisualDensity? visualDensity,
    MaterialTapTargetSize? tapTargetSize,
    Duration? animationDuration,
    bool? enableFeedback,
    AlignmentGeometry? alignment,
    InteractiveInkFeatureFactory? splashFactory,
  }) {
    return IconButton.styleFrom(
      foregroundColor: foregroundColor,
      backgroundColor: backgroundColor,
      disabledForegroundColor: disabledForegroundColor,
      disabledBackgroundColor: disabledBackgroundColor,
      focusColor: focusColor,
      hoverColor: hoverColor,
      highlightColor: highlightColor,
      shadowColor: shadowColor,
      surfaceTintColor: surfaceTintColor,
      overlayColor: overlayColor,
      elevation: elevation,
      minimumSize: minimumSize,
      fixedSize: fixedSize,
      maximumSize: maximumSize,
      iconSize: iconSize,
      side: side,
      shape: shape,
      padding: padding,
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

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return IconButton(
      key: runtime.decodeKey(data),
      iconSize: runtime.unpackOptionalField<double>(data, 'iconSize'),
      padding: runtime.unpackOptionalField<EdgeInsetsGeometry>(data, 'padding'),
      alignment: runtime.unpackOptionalField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      splashRadius: runtime.unpackOptionalField<double>(data, 'splashRadius'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      highlightColor: runtime.unpackOptionalField<Color>(
        data,
        'highlightColor',
      ),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      disabledColor: runtime.unpackOptionalField<Color>(data, 'disabledColor'),
      onPressed: runtime.unpackNullableRequiredCallback(data, 'onPressed'),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      tooltip: runtime.unpackOptionalField<String>(data, 'tooltip'),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
      isSelected: runtime.unpackOptionalField<bool>(data, 'isSelected'),
      selectedIcon: runtime.unpackOptionalField<Widget>(data, 'selectedIcon'),
      icon: runtime.unpackRequiredField<Widget>(data, 'icon'),
    );
  }
}
