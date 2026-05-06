import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flut/flut/runtime.dart';

class FlutAdaptiveTextSelectionToolbar {
  FlutAdaptiveTextSelectionToolbar._();

  static AdaptiveTextSelectionToolbar? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'buttonItems':
        return AdaptiveTextSelectionToolbar.buttonItems(
          key: runtime.decodeKey(data),
          buttonItems: runtime
              .unpackNullableRequiredField<List<ContextMenuButtonItem>>(
                data,
                'buttonItems',
              ),
          anchors: runtime.unpackRequiredField<TextSelectionToolbarAnchors>(
            data,
            'anchors',
          ),
        );
      case 'editable':
        return AdaptiveTextSelectionToolbar.editable(
          key: runtime.decodeKey(data),
          clipboardStatus: runtime.unpackRequiredField<ClipboardStatus>(
            data,
            'clipboardStatus',
          ),
          onCopy: runtime.unpackNullableRequiredCallback(data, 'onCopy'),
          onCut: runtime.unpackNullableRequiredCallback(data, 'onCut'),
          onPaste: runtime.unpackNullableRequiredCallback(data, 'onPaste'),
          onSelectAll: runtime.unpackNullableRequiredCallback(
            data,
            'onSelectAll',
          ),
          onLookUp: runtime.unpackNullableRequiredCallback(data, 'onLookUp'),
          onSearchWeb: runtime.unpackNullableRequiredCallback(
            data,
            'onSearchWeb',
          ),
          onShare: runtime.unpackNullableRequiredCallback(data, 'onShare'),
          onLiveTextInput: runtime.unpackNullableRequiredCallback(
            data,
            'onLiveTextInput',
          ),
          anchors: runtime.unpackRequiredField<TextSelectionToolbarAnchors>(
            data,
            'anchors',
          ),
        );
      case 'editableText':
        return AdaptiveTextSelectionToolbar.editableText(
          key: runtime.decodeKey(data),
          editableTextState: runtime.unpackRequiredField<EditableTextState>(
            data,
            'editableTextState',
          ),
        );
      case 'selectable':
        return AdaptiveTextSelectionToolbar.selectable(
          key: runtime.decodeKey(data),
          onCopy: runtime.unpackRequiredCallback(data, 'onCopy'),
          onSelectAll: runtime.unpackRequiredCallback(data, 'onSelectAll'),
          onShare: runtime.unpackNullableRequiredCallback(data, 'onShare'),
          selectionGeometry: runtime.unpackRequiredField<SelectionGeometry>(
            data,
            'selectionGeometry',
          ),
          anchors: runtime.unpackRequiredField<TextSelectionToolbarAnchors>(
            data,
            'anchors',
          ),
        );
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

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic(
      'AdaptiveTextSelectionToolbar.getButtonLabel',
      getButtonLabel,
    );
    runtime.registerStatic(
      'AdaptiveTextSelectionToolbar.getAdaptiveButtons',
      getAdaptiveButtons,
    );
  }

  static String getButtonLabel(
    FlutRuntime runtime,
    BuildContext context,
    ContextMenuButtonItem buttonItem,
  ) {
    return AdaptiveTextSelectionToolbar.getButtonLabel(context, buttonItem);
  }

  static List<Widget> getAdaptiveButtons(
    FlutRuntime runtime,
    BuildContext context,
    List<dynamic> buttonItems,
  ) {
    final items = runtime.decodeList<List<ContextMenuButtonItem>>(buttonItems)!;
    return AdaptiveTextSelectionToolbar.getAdaptiveButtons(
      context,
      items,
    ).toList();
  }
}
