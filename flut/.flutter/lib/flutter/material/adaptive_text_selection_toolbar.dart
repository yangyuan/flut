import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutAdaptiveTextSelectionToolbar {
  FlutAdaptiveTextSelectionToolbar._();

  static AdaptiveTextSelectionToolbar? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'selectableRegion':
        return AdaptiveTextSelectionToolbar.selectableRegion(
          key: runtime.decodeKey(data),
          selectableRegionState: runtime
              .unpackRequiredField<SelectableRegionState>(
                data,
                'selectableRegionState',
              ),
        );
      default:
        return AdaptiveTextSelectionToolbar(
          key: runtime.decodeKey(data),
          anchors: runtime.unpackRequiredField<TextSelectionToolbarAnchors>(
            data,
            'anchors',
          ),
          children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
        );
    }
  }
}
