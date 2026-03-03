import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutAppBar {
  FlutAppBar._();

  static AppBar? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return AppBar(
      key: runtime.decodeKey(data),
      leading: runtime.unpackOptionalField<Widget>(data, 'leading'),
      automaticallyImplyLeading: runtime.unpackRequiredField<bool>(
        data,
        'automaticallyImplyLeading',
      ),
      title: runtime.unpackOptionalField<Widget>(data, 'title'),
      actions: runtime.unpackOptionalField<List<Widget>>(data, 'actions'),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      scrolledUnderElevation: runtime.unpackOptionalField<double>(
        data,
        'scrolledUnderElevation',
      ),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      foregroundColor: runtime.unpackOptionalField<Color>(
        data,
        'foregroundColor',
      ),
      primary: runtime.unpackRequiredField<bool>(data, 'primary'),
      centerTitle: runtime.unpackOptionalField<bool>(data, 'centerTitle'),
      titleSpacing: runtime.unpackOptionalField<double>(data, 'titleSpacing'),
      toolbarOpacity: runtime.unpackRequiredField<double>(
        data,
        'toolbarOpacity',
      ),
      bottomOpacity: runtime.unpackRequiredField<double>(data, 'bottomOpacity'),
      toolbarHeight: runtime.unpackOptionalField<double>(data, 'toolbarHeight'),
      leadingWidth: runtime.unpackOptionalField<double>(data, 'leadingWidth'),
      toolbarTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'toolbarTextStyle',
      ),
      titleTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'titleTextStyle',
      ),
      forceMaterialTransparency: runtime.unpackRequiredField<bool>(
        data,
        'forceMaterialTransparency',
      ),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      bottom: runtime.unpackOptionalField<PreferredSizeWidget>(data, 'bottom'),
    );
  }
}
