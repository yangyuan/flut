import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutTooltip {
  FlutTooltip._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Tooltip(
      key: runtime.decodeKey(data),
      message: runtime.unpackOptionalField<String>(data, 'message'),
      richMessage: runtime.unpackOptionalField<InlineSpan>(data, 'richMessage'),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      margin: runtime.unpackOptionalField<EdgeInsets>(data, 'margin'),
      verticalOffset: runtime.unpackOptionalField<double>(
        data,
        'verticalOffset',
      ),
      preferBelow: runtime.unpackOptionalField<bool>(data, 'preferBelow'),
      excludeFromSemantics: runtime.unpackOptionalField<bool>(
        data,
        'excludeFromSemantics',
      ),
      decoration: runtime.unpackOptionalField<Decoration>(data, 'decoration'),
      textStyle: runtime.unpackOptionalField<TextStyle>(data, 'textStyle'),
      textAlign: runtime.unpackOptionalField<TextAlign>(data, 'textAlign'),
      waitDuration: runtime.unpackOptionalField<Duration>(data, 'waitDuration'),
      showDuration: runtime.unpackOptionalField<Duration>(data, 'showDuration'),
      exitDuration: runtime.unpackOptionalField<Duration>(data, 'exitDuration'),
      enableTapToDismiss: runtime.unpackRequiredField<bool>(
        data,
        'enableTapToDismiss',
      ),
      triggerMode: runtime.unpackOptionalField<TooltipTriggerMode>(
        data,
        'triggerMode',
      ),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      onTriggered: runtime.unpackOptionalCallback(data, 'onTriggered'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      ignorePointer: runtime.unpackOptionalField<bool>(data, 'ignorePointer'),
      positionDelegate: runtime.unpackOptionalField<TooltipPositionDelegate>(
        data,
        'positionDelegate',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Tooltip.dismissAllToolTips', dismissAllToolTips);
  }

  static dynamic dismissAllToolTips(FlutRuntime runtime) {
    return Tooltip.dismissAllToolTips();
  }
}
