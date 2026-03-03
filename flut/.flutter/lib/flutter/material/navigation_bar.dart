import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutNavigationDestinationLabelBehavior
    extends FlutEnumObject<NavigationDestinationLabelBehavior> {
  const FlutNavigationDestinationLabelBehavior()
    : super('NavigationDestinationLabelBehavior', const {
        'alwaysShow': NavigationDestinationLabelBehavior.alwaysShow,
        'alwaysHide': NavigationDestinationLabelBehavior.alwaysHide,
        'onlyShowSelected': NavigationDestinationLabelBehavior.onlyShowSelected,
      });
}

class FlutNavigationDestination {
  FlutNavigationDestination._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return NavigationDestination(
      key: runtime.decodeKey(data),
      icon: runtime.unpackRequiredField<Widget>(data, 'icon'),
      selectedIcon: runtime.unpackOptionalField<Widget>(data, 'selectedIcon'),
      label: runtime.unpackRequiredField<String>(data, 'label'),
      tooltip: runtime.unpackOptionalField<String>(data, 'tooltip'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
    );
  }
}

class FlutNavigationBar {
  FlutNavigationBar._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return NavigationBar(
      key: runtime.decodeKey(data),
      animationDuration: runtime.unpackOptionalField<Duration>(
        data,
        'animationDuration',
      ),
      selectedIndex: runtime.unpackRequiredField<int>(data, 'selectedIndex'),
      destinations: runtime.unpackRequiredField<List<Widget>>(
        data,
        'destinations',
      ),
      onDestinationSelected: runtime.unpackOptionalCallback(
        data,
        'onDestinationSelected',
      ),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      indicatorColor: runtime.unpackOptionalField<Color>(
        data,
        'indicatorColor',
      ),
      indicatorShape: runtime.unpackOptionalField<ShapeBorder>(
        data,
        'indicatorShape',
      ),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      labelBehavior: runtime
          .unpackOptionalField<NavigationDestinationLabelBehavior>(
            data,
            'labelBehavior',
          ),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      labelPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'labelPadding',
      ),
      labelTextStyle: runtime
          .unpackGenericField<WidgetStateProperty<TextStyle?>, TextStyle?>(
            data,
            'labelTextStyle',
          ),
      maintainBottomViewPadding: runtime.unpackRequiredField<bool>(
        data,
        'maintainBottomViewPadding',
      ),
    );
  }
}
