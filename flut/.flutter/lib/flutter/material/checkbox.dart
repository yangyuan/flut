import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutCheckbox {
  FlutCheckbox._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'adaptive':
        return Checkbox.adaptive(
          key: runtime.decodeKey(data),
          value: runtime.unpackNullableRequiredField<bool>(data, 'value'),
          tristate: runtime.unpackRequiredField<bool>(data, 'tristate'),
          onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
          mouseCursor: runtime.unpackOptionalField<MouseCursor>(
            data,
            'mouseCursor',
          ),
          activeColor: runtime.unpackOptionalField<Color>(data, 'activeColor'),
          fillColor: runtime
              .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
                data,
                'fillColor',
              ),
          checkColor: runtime.unpackOptionalField<Color>(data, 'checkColor'),
          focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
          hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
          overlayColor: runtime
              .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
                data,
                'overlayColor',
              ),
          splashRadius: runtime.unpackOptionalField<double>(
            data,
            'splashRadius',
          ),
          materialTapTargetSize: runtime
              .unpackOptionalField<MaterialTapTargetSize>(
                data,
                'materialTapTargetSize',
              ),
          visualDensity: runtime.unpackOptionalField<VisualDensity>(
            data,
            'visualDensity',
          ),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          shape: runtime.unpackOptionalField<OutlinedBorder>(data, 'shape'),
          side: runtime.unpackOptionalField<BorderSide>(data, 'side'),
          isError: runtime.unpackRequiredField<bool>(data, 'isError'),
          semanticLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticLabel',
          ),
        );
      default:
        return Checkbox(
          key: runtime.decodeKey(data),
          value: runtime.unpackNullableRequiredField<bool>(data, 'value'),
          tristate: runtime.unpackRequiredField<bool>(data, 'tristate'),
          onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
          mouseCursor: runtime.unpackOptionalField<MouseCursor>(
            data,
            'mouseCursor',
          ),
          activeColor: runtime.unpackOptionalField<Color>(data, 'activeColor'),
          fillColor: runtime
              .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
                data,
                'fillColor',
              ),
          checkColor: runtime.unpackOptionalField<Color>(data, 'checkColor'),
          focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
          hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
          overlayColor: runtime
              .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
                data,
                'overlayColor',
              ),
          splashRadius: runtime.unpackOptionalField<double>(
            data,
            'splashRadius',
          ),
          materialTapTargetSize: runtime
              .unpackOptionalField<MaterialTapTargetSize>(
                data,
                'materialTapTargetSize',
              ),
          visualDensity: runtime.unpackOptionalField<VisualDensity>(
            data,
            'visualDensity',
          ),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          shape: runtime.unpackOptionalField<OutlinedBorder>(data, 'shape'),
          side: runtime.unpackOptionalField<BorderSide>(data, 'side'),
          isError: runtime.unpackRequiredField<bool>(data, 'isError'),
          semanticLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticLabel',
          ),
        );
    }
  }
}
