import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutListTileControlAffinity
    extends FlutEnumObject<ListTileControlAffinity> {
  const FlutListTileControlAffinity()
    : super('ListTileControlAffinity', const {
        'leading': ListTileControlAffinity.leading,
        'trailing': ListTileControlAffinity.trailing,
        'platform': ListTileControlAffinity.platform,
      });
}

class FlutListTile {
  FlutListTile._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ListTile(
      key: runtime.decodeKey(data),
      leading: runtime.unpackOptionalField<Widget>(data, 'leading'),
      title: runtime.unpackOptionalField<Widget>(data, 'title'),
      subtitle: runtime.unpackOptionalField<Widget>(data, 'subtitle'),
      trailing: runtime.unpackOptionalField<Widget>(data, 'trailing'),
      isThreeLine: runtime.unpackOptionalField<bool>(data, 'isThreeLine'),
      dense: runtime.unpackOptionalField<bool>(data, 'dense'),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      selectedColor: runtime.unpackOptionalField<Color>(data, 'selectedColor'),
      iconColor: runtime.unpackOptionalField<Color>(data, 'iconColor'),
      textColor: runtime.unpackOptionalField<Color>(data, 'textColor'),
      titleTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'titleTextStyle',
      ),
      subtitleTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'subtitleTextStyle',
      ),
      leadingAndTrailingTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'leadingAndTrailingTextStyle',
      ),
      contentPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'contentPadding',
      ),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      onLongPress: runtime.unpackOptionalCallback(data, 'onLongPress'),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      selected: runtime.unpackRequiredField<bool>(data, 'selected'),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      tileColor: runtime.unpackOptionalField<Color>(data, 'tileColor'),
      selectedTileColor: runtime.unpackOptionalField<Color>(
        data,
        'selectedTileColor',
      ),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      horizontalTitleGap: runtime.unpackOptionalField<double>(
        data,
        'horizontalTitleGap',
      ),
      minVerticalPadding: runtime.unpackOptionalField<double>(
        data,
        'minVerticalPadding',
      ),
      minLeadingWidth: runtime.unpackOptionalField<double>(
        data,
        'minLeadingWidth',
      ),
      minTileHeight: runtime.unpackOptionalField<double>(data, 'minTileHeight'),
    );
  }
}
