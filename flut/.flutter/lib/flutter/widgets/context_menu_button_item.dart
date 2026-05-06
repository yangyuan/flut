import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutContextMenuButtonType extends FlutEnumObject<ContextMenuButtonType> {
  const FlutContextMenuButtonType()
    : super('ContextMenuButtonType', const {
        'cut': ContextMenuButtonType.cut,
        'copy': ContextMenuButtonType.copy,
        'paste': ContextMenuButtonType.paste,
        'selectAll': ContextMenuButtonType.selectAll,
        'delete': ContextMenuButtonType.delete,
        'lookUp': ContextMenuButtonType.lookUp,
        'searchWeb': ContextMenuButtonType.searchWeb,
        'share': ContextMenuButtonType.share,
        'liveTextInput': ContextMenuButtonType.liveTextInput,
        'custom': ContextMenuButtonType.custom,
      });
}

class FlutContextMenuButtonItem extends FlutValueObject {
  final ContextMenuButtonItem item;

  const FlutContextMenuButtonItem(this.item) : super('ContextMenuButtonItem');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['type'] = const FlutContextMenuButtonType().flutEncode(item.type);
    if (item.label != null) {
      result['label'] = item.label;
    }
    return result;
  }

  static ContextMenuButtonItem? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final onPressed = runtime.unpackOptionalCallback(data, 'onPressed');
    return ContextMenuButtonItem(
      onPressed: onPressed,
      type: runtime.unpackRequiredField<ContextMenuButtonType>(data, 'type'),
      label: runtime.unpackOptionalField<String>(data, 'label'),
    );
  }
}
