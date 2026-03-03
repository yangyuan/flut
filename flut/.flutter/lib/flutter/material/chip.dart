import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutChip {
  FlutChip._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Chip(
      key: runtime.decodeKey(data),
      avatar: runtime.unpackOptionalField<Widget>(data, 'avatar'),
      label: runtime.unpackRequiredField<Widget>(data, 'label'),
      labelStyle: runtime.unpackOptionalField<TextStyle>(data, 'labelStyle'),
      labelPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'labelPadding',
      ),
      deleteIcon: runtime.unpackOptionalField<Widget>(data, 'deleteIcon'),
      onDeleted: runtime.unpackOptionalCallback(data, 'onDeleted'),
      deleteIconColor: runtime.unpackOptionalField<Color>(
        data,
        'deleteIconColor',
      ),
      deleteButtonTooltipMessage: runtime.unpackOptionalField<String>(
        data,
        'deleteButtonTooltipMessage',
      ),
      side: runtime.unpackOptionalField<BorderSide>(data, 'side'),
      shape: runtime.unpackOptionalField<OutlinedBorder>(data, 'shape'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      color: runtime.unpackGenericField<WidgetStateProperty<Color?>, Color?>(
        data,
        'color',
      ),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      visualDensity: runtime.unpackOptionalField<VisualDensity>(
        data,
        'visualDensity',
      ),
      materialTapTargetSize: runtime.unpackOptionalField<MaterialTapTargetSize>(
        data,
        'materialTapTargetSize',
      ),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      iconTheme: runtime.unpackOptionalField<IconThemeData>(data, 'iconTheme'),
      avatarBoxConstraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'avatarBoxConstraints',
      ),
      deleteIconBoxConstraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'deleteIconBoxConstraints',
      ),
      chipAnimationStyle: runtime.unpackOptionalField<ChipAnimationStyle>(
        data,
        'chipAnimationStyle',
      ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
    );
  }
}

class FlutChipAnimationStyle extends FlutValueObject {
  final ChipAnimationStyle value;
  const FlutChipAnimationStyle(this.value) : super('ChipAnimationStyle');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static ChipAnimationStyle? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ChipAnimationStyle(
      enableAnimation: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'enableAnimation',
      ),
      selectAnimation: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'selectAnimation',
      ),
      avatarDrawerAnimation: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'avatarDrawerAnimation',
      ),
      deleteDrawerAnimation: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'deleteDrawerAnimation',
      ),
    );
  }
}
