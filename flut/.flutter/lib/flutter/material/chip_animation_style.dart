import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

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
