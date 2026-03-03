import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutFloatingActionButton {
  FlutFloatingActionButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return FloatingActionButton(
      key: runtime.decodeKey(data),
      tooltip: runtime.unpackOptionalField<String>(data, 'tooltip'),
      foregroundColor: runtime.unpackOptionalField<Color>(
        data,
        'foregroundColor',
      ),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      focusElevation: runtime.unpackOptionalField<double>(
        data,
        'focusElevation',
      ),
      hoverElevation: runtime.unpackOptionalField<double>(
        data,
        'hoverElevation',
      ),
      highlightElevation: runtime.unpackOptionalField<double>(
        data,
        'highlightElevation',
      ),
      disabledElevation: runtime.unpackOptionalField<double>(
        data,
        'disabledElevation',
      ),
      onPressed: runtime.unpackNullableRequiredCallback(data, 'onPressed'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      mini: runtime.unpackRequiredField<bool>(data, 'mini'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      materialTapTargetSize: runtime.unpackOptionalField<MaterialTapTargetSize>(
        data,
        'materialTapTargetSize',
      ),
      isExtended: runtime.unpackRequiredField<bool>(data, 'isExtended'),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
