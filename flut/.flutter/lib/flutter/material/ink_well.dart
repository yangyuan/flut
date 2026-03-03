import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutInkWell {
  FlutInkWell._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return InkWell(
      key: runtime.decodeKey(data),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onDoubleTap: runtime.unpackOptionalCallback(data, 'onDoubleTap'),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      onLongPressUp: runtime.unpackOptionalCallback(data, 'onLongPressUp'),
      onTapDown: runtime.unpackOptionalCallback(data, 'onTapDown'),
      onTapUp: runtime.unpackOptionalCallback(data, 'onTapUp'),
      onTapCancel: runtime.unpackOptionalCallback(data, 'onTapCancel'),
      onSecondaryTap: runtime.unpackOptionalCallback(data, 'onSecondaryTap'),
      onSecondaryTapUp: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapUp',
      ),
      onSecondaryTapDown: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapDown',
      ),
      onSecondaryTapCancel: runtime.unpackOptionalCallback(
        data,
        'onSecondaryTapCancel',
      ),
      onHighlightChanged: runtime.unpackOptionalCallback(
        data,
        'onHighlightChanged',
      ),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      highlightColor: runtime.unpackOptionalField<Color>(
        data,
        'highlightColor',
      ),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      splashFactory: runtime.unpackOptionalField<InteractiveInkFeatureFactory>(
        data,
        'splashFactory',
      ),
      radius: runtime.unpackOptionalField<double>(data, 'radius'),
      borderRadius: runtime.unpackOptionalField<BorderRadius>(
        data,
        'borderRadius',
      ),
      customBorder: runtime.unpackOptionalField<ShapeBorder>(
        data,
        'customBorder',
      ),
      enableFeedback: runtime.unpackRequiredField<bool>(data, 'enableFeedback'),
      excludeFromSemantics: runtime.unpackRequiredField<bool>(
        data,
        'excludeFromSemantics',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      canRequestFocus: runtime.unpackRequiredField<bool>(
        data,
        'canRequestFocus',
      ),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      statesController: runtime.unpackOptionalField<WidgetStatesController>(
        data,
        'statesController',
      ),
      hoverDuration: runtime.unpackOptionalField<Duration>(
        data,
        'hoverDuration',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
