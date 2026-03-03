import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutSwitch {
  FlutSwitch._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Switch(
      key: runtime.decodeKey(data),
      value: runtime.unpackRequiredField<bool>(data, 'value'),
      onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
      activeThumbColor: runtime.unpackOptionalField<Color>(
        data,
        'activeThumbColor',
      ),
      activeTrackColor: runtime.unpackOptionalField<Color>(
        data,
        'activeTrackColor',
      ),
      inactiveThumbColor: runtime.unpackOptionalField<Color>(
        data,
        'inactiveThumbColor',
      ),
      inactiveTrackColor: runtime.unpackOptionalField<Color>(
        data,
        'inactiveTrackColor',
      ),
      activeThumbImage: runtime.unpackOptionalField<ImageProvider>(
        data,
        'activeThumbImage',
      ),
      onActiveThumbImageError: runtime.unpackOptionalCallback(
        data,
        'onActiveThumbImageError',
      ),
      inactiveThumbImage: runtime.unpackOptionalField<ImageProvider>(
        data,
        'inactiveThumbImage',
      ),
      onInactiveThumbImageError: runtime.unpackOptionalCallback(
        data,
        'onInactiveThumbImageError',
      ),
      thumbColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'thumbColor',
          ),
      trackColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'trackColor',
          ),
      trackOutlineColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'trackOutlineColor',
          ),
      trackOutlineWidth: runtime
          .unpackGenericField<WidgetStateProperty<double?>, double?>(
            data,
            'trackOutlineWidth',
          ),
      thumbIcon: runtime.unpackGenericField<WidgetStateProperty<Icon?>, Icon?>(
        data,
        'thumbIcon',
      ),
      materialTapTargetSize: runtime.unpackOptionalField<MaterialTapTargetSize>(
        data,
        'materialTapTargetSize',
      ),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      splashRadius: runtime.unpackOptionalField<double>(data, 'splashRadius'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
    );
  }
}
