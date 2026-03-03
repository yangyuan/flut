import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutScrollViewKeyboardDismissBehavior
    extends FlutEnumObject<ScrollViewKeyboardDismissBehavior> {
  const FlutScrollViewKeyboardDismissBehavior()
    : super('ScrollViewKeyboardDismissBehavior', const {
        'manual': ScrollViewKeyboardDismissBehavior.manual,
        'onDrag': ScrollViewKeyboardDismissBehavior.onDrag,
      });
}

class FlutListView {
  FlutListView._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'builder':
        return ListView.builder(
          key: runtime.decodeKey(data),
          scrollDirection: runtime.unpackRequiredField<Axis>(
            data,
            'scrollDirection',
          ),
          reverse: runtime.unpackRequiredField<bool>(data, 'reverse'),
          controller: runtime.unpackOptionalField<ScrollController>(
            data,
            'controller',
          ),
          primary: runtime.unpackOptionalField<bool>(data, 'primary'),
          physics: runtime.unpackOptionalField<ScrollPhysics>(data, 'physics'),
          shrinkWrap: runtime.unpackRequiredField<bool>(data, 'shrinkWrap'),
          padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
          itemExtent: runtime.unpackOptionalField<double>(data, 'itemExtent'),
          cacheExtent: runtime.unpackOptionalField<double>(data, 'cacheExtent'),
          itemCount: runtime.unpackOptionalField<int>(data, 'itemCount'),
          itemBuilder:
              runtime.unpackRequiredCallback(data, 'itemBuilder')
                  as NullableIndexedWidgetBuilder,
          dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
            data,
            'dragStartBehavior',
          ),
          clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
        );
      default:
        return ListView(
          key: runtime.decodeKey(data),
          scrollDirection: runtime.unpackRequiredField<Axis>(
            data,
            'scrollDirection',
          ),
          reverse: runtime.unpackRequiredField<bool>(data, 'reverse'),
          controller: runtime.unpackOptionalField<ScrollController>(
            data,
            'controller',
          ),
          primary: runtime.unpackOptionalField<bool>(data, 'primary'),
          physics: runtime.unpackOptionalField<ScrollPhysics>(data, 'physics'),
          shrinkWrap: runtime.unpackRequiredField<bool>(data, 'shrinkWrap'),
          padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
          itemExtent: runtime.unpackOptionalField<double>(data, 'itemExtent'),
          cacheExtent: runtime.unpackOptionalField<double>(data, 'cacheExtent'),
          dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
            data,
            'dragStartBehavior',
          ),
          clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
          children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
        );
    }
  }
}

class FlutCustomScrollView {
  FlutCustomScrollView._();

  static CustomScrollView? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CustomScrollView(
      key: runtime.decodeKey(data),
      scrollDirection: runtime.unpackRequiredField<Axis>(
        data,
        'scrollDirection',
      ),
      reverse: runtime.unpackRequiredField<bool>(data, 'reverse'),
      controller: runtime.unpackOptionalField<ScrollController>(
        data,
        'controller',
      ),
      primary: runtime.unpackOptionalField<bool>(data, 'primary'),
      physics: runtime.unpackOptionalField<ScrollPhysics>(data, 'physics'),
      shrinkWrap: runtime.unpackRequiredField<bool>(data, 'shrinkWrap'),
      anchor: runtime.unpackRequiredField<double>(data, 'anchor'),
      cacheExtent: runtime.unpackOptionalField<double>(data, 'cacheExtent'),
      semanticChildCount: runtime.unpackOptionalField<int>(
        data,
        'semanticChildCount',
      ),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      keyboardDismissBehavior: runtime
          .unpackOptionalField<ScrollViewKeyboardDismissBehavior>(
            data,
            'keyboardDismissBehavior',
          ),
      restorationId: runtime.unpackOptionalField<String>(data, 'restorationId'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      hitTestBehavior: runtime.unpackRequiredField<HitTestBehavior>(
        data,
        'hitTestBehavior',
      ),
      slivers: runtime.unpackRequiredField<List<Widget>>(data, 'slivers'),
    );
  }
}
