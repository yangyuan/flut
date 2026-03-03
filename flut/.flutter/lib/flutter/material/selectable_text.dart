import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutSelectableText {
  FlutSelectableText._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'rich':
        return SelectableText.rich(
          runtime.unpackRequiredField<TextSpan>(data, 'textSpan'),
          key: runtime.decodeKey(data),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
          strutStyle: runtime.unpackOptionalField<StrutStyle>(
            data,
            'strutStyle',
          ),
          textAlign: runtime.unpackOptionalField<TextAlign>(data, 'textAlign'),
          textDirection: runtime.unpackOptionalField<TextDirection>(
            data,
            'textDirection',
          ),
          textScaler: runtime.unpackOptionalField<TextScaler>(
            data,
            'textScaler',
          ),
          showCursor: runtime.unpackRequiredField<bool>(data, 'showCursor'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          minLines: runtime.unpackOptionalField<int>(data, 'minLines'),
          maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
          cursorWidth: runtime.unpackRequiredField<double>(data, 'cursorWidth'),
          cursorHeight: runtime.unpackOptionalField<double>(
            data,
            'cursorHeight',
          ),
          cursorRadius: runtime.unpackOptionalField<Radius>(
            data,
            'cursorRadius',
          ),
          cursorColor: runtime.unpackOptionalField<Color>(data, 'cursorColor'),
          selectionColor: runtime.unpackOptionalField<Color>(
            data,
            'selectionColor',
          ),
          selectionHeightStyle: runtime.unpackOptionalField<BoxHeightStyle>(
            data,
            'selectionHeightStyle',
          ),
          selectionWidthStyle: runtime.unpackOptionalField<BoxWidthStyle>(
            data,
            'selectionWidthStyle',
          ),
          dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
            data,
            'dragStartBehavior',
          ),
          enableInteractiveSelection: runtime.unpackRequiredField<bool>(
            data,
            'enableInteractiveSelection',
          ),
          selectionControls: runtime.unpackOptionalField<TextSelectionControls>(
            data,
            'selectionControls',
          ),
          onTap: runtime.unpackOptionalCallback(data, 'onTap'),
          scrollPhysics: runtime.unpackOptionalField<ScrollPhysics>(
            data,
            'scrollPhysics',
          ),
          semanticsLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticsLabel',
          ),
          textHeightBehavior: runtime.unpackOptionalField<TextHeightBehavior>(
            data,
            'textHeightBehavior',
          ),
          textWidthBasis: runtime.unpackOptionalField<TextWidthBasis>(
            data,
            'textWidthBasis',
          ),
          onSelectionChanged: runtime.unpackOptionalCallback(
            data,
            'onSelectionChanged',
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
          scrollBehavior: runtime.unpackOptionalField<ScrollBehavior>(
            data,
            'scrollBehavior',
          ),
        );
      default:
        return SelectableText(
          runtime.unpackRequiredField<String>(data, 'data'),
          key: runtime.decodeKey(data),
          focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
          style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
          strutStyle: runtime.unpackOptionalField<StrutStyle>(
            data,
            'strutStyle',
          ),
          textAlign: runtime.unpackOptionalField<TextAlign>(data, 'textAlign'),
          textDirection: runtime.unpackOptionalField<TextDirection>(
            data,
            'textDirection',
          ),
          textScaler: runtime.unpackOptionalField<TextScaler>(
            data,
            'textScaler',
          ),
          showCursor: runtime.unpackRequiredField<bool>(data, 'showCursor'),
          autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
          minLines: runtime.unpackOptionalField<int>(data, 'minLines'),
          maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
          cursorWidth: runtime.unpackRequiredField<double>(data, 'cursorWidth'),
          cursorHeight: runtime.unpackOptionalField<double>(
            data,
            'cursorHeight',
          ),
          cursorRadius: runtime.unpackOptionalField<Radius>(
            data,
            'cursorRadius',
          ),
          cursorColor: runtime.unpackOptionalField<Color>(data, 'cursorColor'),
          selectionColor: runtime.unpackOptionalField<Color>(
            data,
            'selectionColor',
          ),
          selectionHeightStyle: runtime.unpackOptionalField<BoxHeightStyle>(
            data,
            'selectionHeightStyle',
          ),
          selectionWidthStyle: runtime.unpackOptionalField<BoxWidthStyle>(
            data,
            'selectionWidthStyle',
          ),
          dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
            data,
            'dragStartBehavior',
          ),
          enableInteractiveSelection: runtime.unpackRequiredField<bool>(
            data,
            'enableInteractiveSelection',
          ),
          selectionControls: runtime.unpackOptionalField<TextSelectionControls>(
            data,
            'selectionControls',
          ),
          onTap: runtime.unpackOptionalCallback(data, 'onTap'),
          scrollPhysics: runtime.unpackOptionalField<ScrollPhysics>(
            data,
            'scrollPhysics',
          ),
          semanticsLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticsLabel',
          ),
          textHeightBehavior: runtime.unpackOptionalField<TextHeightBehavior>(
            data,
            'textHeightBehavior',
          ),
          textWidthBasis: runtime.unpackOptionalField<TextWidthBasis>(
            data,
            'textWidthBasis',
          ),
          onSelectionChanged: runtime.unpackOptionalCallback(
            data,
            'onSelectionChanged',
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
          scrollBehavior: runtime.unpackOptionalField<ScrollBehavior>(
            data,
            'scrollBehavior',
          ),
        );
    }
  }
}
