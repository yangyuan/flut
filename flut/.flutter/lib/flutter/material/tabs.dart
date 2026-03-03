import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutTabBar {
  FlutTabBar._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TabBar(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<TabController>(
        data,
        'controller',
      ),
      tabs: runtime.unpackRequiredField<List<Widget>>(data, 'tabs'),
      isScrollable: runtime.unpackRequiredField<bool>(data, 'isScrollable'),
      indicatorColor: runtime.unpackOptionalField<Color>(
        data,
        'indicatorColor',
      ),
      dividerColor: runtime.unpackOptionalField<Color>(data, 'dividerColor'),
      labelColor: runtime.unpackOptionalField<Color>(data, 'labelColor'),
      labelStyle: runtime.unpackOptionalField<TextStyle>(data, 'labelStyle'),
      unselectedLabelColor: runtime.unpackOptionalField<Color>(
        data,
        'unselectedLabelColor',
      ),
      unselectedLabelStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'unselectedLabelStyle',
      ),
      labelPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'labelPadding',
      ),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
    );
  }
}

class FlutTabBarView {
  FlutTabBarView._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return TabBarView(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<TabController>(
        data,
        'controller',
      ),
      physics: runtime.unpackOptionalField<ScrollPhysics>(data, 'physics'),
      dragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'dragStartBehavior',
      ),
      viewportFraction: runtime.unpackRequiredField<double>(
        data,
        'viewportFraction',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutTab {
  FlutTab._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Tab(
      key: runtime.decodeKey(data),
      text: runtime.unpackOptionalField<String>(data, 'text'),
      icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
      iconMargin: runtime.unpackOptionalField<EdgeInsets>(data, 'iconMargin'),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
