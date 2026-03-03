import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutDropdownButton {
  FlutDropdownButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return DropdownButton<dynamic>(
      key: runtime.decodeKey(data),
      items: runtime
          .unpackNullableRequiredField<List<DropdownMenuItem<dynamic>>>(
            data,
            'items',
          ),
      value: runtime.unpackDynamicOptionalField(data, 'value'),
      hint: runtime.unpackOptionalField<Widget>(data, 'hint'),
      disabledHint: runtime.unpackOptionalField<Widget>(data, 'disabledHint'),
      onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      selectedItemBuilder: runtime.unpackOptionalCallback(
        data,
        'selectedItemBuilder',
      ),
      elevation: runtime.unpackRequiredField<int>(data, 'elevation'),
      style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
      underline: runtime.unpackOptionalField<Widget>(data, 'underline'),
      icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
      iconDisabledColor: runtime.unpackOptionalField<Color>(
        data,
        'iconDisabledColor',
      ),
      iconEnabledColor: runtime.unpackOptionalField<Color>(
        data,
        'iconEnabledColor',
      ),
      iconSize: runtime.unpackRequiredField<double>(data, 'iconSize'),
      isDense: runtime.unpackRequiredField<bool>(data, 'isDense'),
      isExpanded: runtime.unpackRequiredField<bool>(data, 'isExpanded'),
      itemHeight: runtime.unpackOptionalField<double>(data, 'itemHeight'),
      menuWidth: runtime.unpackOptionalField<double>(data, 'menuWidth'),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      dropdownColor: runtime.unpackOptionalField<Color>(data, 'dropdownColor'),
      menuMaxHeight: runtime.unpackOptionalField<double>(data, 'menuMaxHeight'),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      alignment: runtime.unpackRequiredField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      borderRadius: runtime.unpackOptionalField<BorderRadius>(
        data,
        'borderRadius',
      ),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      barrierDismissible: runtime.unpackRequiredField<bool>(
        data,
        'barrierDismissible',
      ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      dropdownMenuItemMouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'dropdownMenuItemMouseCursor',
      ),
    );
  }
}

class FlutDropdownMenuItem {
  FlutDropdownMenuItem._();

  static DropdownMenuItem<dynamic>? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DropdownMenuItem<dynamic>(
      key: runtime.decodeKey(data),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      value: runtime.unpackDynamicOptionalField(data, 'value'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      alignment: runtime.unpackRequiredField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
