import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutSelectionArea {
  FlutSelectionArea._();

  static SelectionArea? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectionArea(
      key: runtime.decodeKey(data),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      selectionControls: runtime.unpackOptionalField<TextSelectionControls>(
        data,
        'selectionControls',
      ),
      contextMenuBuilder: runtime.unpackOptionalCallback(
        data,
        'contextMenuBuilder',
      ),
      magnifierConfiguration: runtime
          .unpackOptionalField<TextMagnifierConfiguration>(
            data,
            'magnifierConfiguration',
          ),
      onSelectionChanged: runtime.unpackOptionalCallback(
        data,
        'onSelectionChanged',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
