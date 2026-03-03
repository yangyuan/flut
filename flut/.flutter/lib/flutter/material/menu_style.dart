import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutMenuStyle extends FlutValueObject {
  final MenuStyle menuStyle;
  const FlutMenuStyle(this.menuStyle) : super('MenuStyle');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static MenuStyle? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MenuStyle(
      backgroundColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'backgroundColor',
          ),
      shadowColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'shadowColor',
          ),
      surfaceTintColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'surfaceTintColor',
          ),
      elevation: runtime
          .unpackGenericField<WidgetStateProperty<double?>, double?>(
            data,
            'elevation',
          ),
      padding: runtime
          .unpackGenericField<
            WidgetStateProperty<EdgeInsetsGeometry?>,
            EdgeInsetsGeometry?
          >(data, 'padding'),
      minimumSize: runtime
          .unpackGenericField<WidgetStateProperty<Size?>, Size?>(
            data,
            'minimumSize',
          ),
      fixedSize: runtime.unpackGenericField<WidgetStateProperty<Size?>, Size?>(
        data,
        'fixedSize',
      ),
      maximumSize: runtime
          .unpackGenericField<WidgetStateProperty<Size?>, Size?>(
            data,
            'maximumSize',
          ),
      side: runtime
          .unpackGenericField<WidgetStateProperty<BorderSide?>, BorderSide?>(
            data,
            'side',
          ),
      shape: runtime
          .unpackGenericField<
            WidgetStateProperty<OutlinedBorder?>,
            OutlinedBorder?
          >(data, 'shape'),
      mouseCursor: runtime
          .unpackGenericField<WidgetStateProperty<MouseCursor?>, MouseCursor?>(
            data,
            'mouseCursor',
          ),
      visualDensity: runtime.unpackOptionalField<VisualDensity>(
        data,
        'visualDensity',
      ),
      alignment: runtime.unpackOptionalField<AlignmentGeometry>(
        data,
        'alignment',
      ),
    );
  }
}
