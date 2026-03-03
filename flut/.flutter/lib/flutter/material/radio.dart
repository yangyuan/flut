import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutRadio {
  FlutRadio._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Radio<dynamic>(
      key: runtime.decodeKey(data),
      value: runtime.unpackDynamicRequiredField(data, 'value'),
      groupValue: runtime.unpackDynamicOptionalField(data, 'groupValue'),
      onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      toggleable: runtime.unpackRequiredField<bool>(data, 'toggleable'),
      activeColor: runtime.unpackOptionalField<Color>(data, 'activeColor'),
      fillColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'fillColor',
          ),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      splashRadius: runtime.unpackOptionalField<double>(data, 'splashRadius'),
      materialTapTargetSize: runtime.unpackOptionalField<MaterialTapTargetSize>(
        data,
        'materialTapTargetSize',
      ),
      visualDensity: runtime.unpackOptionalField<VisualDensity>(
        data,
        'visualDensity',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      enabled: runtime.unpackOptionalField<bool>(data, 'enabled'),
      backgroundColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'backgroundColor',
          ),
      side: runtime.unpackOptionalField<BorderSide>(data, 'side'),
      innerRadius: runtime
          .unpackGenericField<WidgetStateProperty<double?>, double?>(
            data,
            'innerRadius',
          ),
    );
  }
}
