import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutSingleChildScrollView {
  FlutSingleChildScrollView._();

  static SingleChildScrollView? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SingleChildScrollView(
      key: runtime.decodeKey(data),
      scrollDirection: runtime.unpackRequiredField<Axis>(
        data,
        'scrollDirection',
      ),
      reverse: runtime.unpackRequiredField<bool>(data, 'reverse'),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      primary: runtime.unpackOptionalField<bool>(data, 'primary'),
      physics: runtime.unpackOptionalField<ScrollPhysics>(data, 'physics'),
      controller: runtime.unpackOptionalField<ScrollController>(
        data,
        'controller',
      ),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      hitTestBehavior: runtime.unpackRequiredField<HitTestBehavior>(
        data,
        'hitTestBehavior',
      ),
      restorationId: runtime.unpackOptionalField<String>(data, 'restorationId'),
      keyboardDismissBehavior: runtime
          .unpackOptionalField<ScrollViewKeyboardDismissBehavior>(
            data,
            'keyboardDismissBehavior',
          ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
