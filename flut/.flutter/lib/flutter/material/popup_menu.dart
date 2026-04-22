import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutPopupMenuItem {
  FlutPopupMenuItem._();

  static PopupMenuItem<dynamic>? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PopupMenuItem<dynamic>(
      key: runtime.decodeKey(data),
      value: runtime.unpackDynamicOptionalField(data, 'value'),
      onTap: runtime.unpackOptionalCallback(data, 'onTap'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      height: runtime.unpackRequiredField<double>(data, 'height'),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      textStyle: runtime.unpackOptionalField<TextStyle>(data, 'textStyle'),
      labelTextStyle: runtime
          .unpackGenericField<WidgetStateProperty<TextStyle?>, TextStyle?>(
            data,
            'labelTextStyle',
          ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutPopupMenuButton {
  FlutPopupMenuButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return PopupMenuButton<dynamic>(
      key: runtime.decodeKey(data),
      itemBuilder: runtime.unpackRequiredCallback(data, 'itemBuilder'),
      initialValue: runtime.unpackDynamicOptionalField(data, 'initialValue'),
      onOpened: runtime.unpackOptionalCallback(data, 'onOpened'),
      onSelected: runtime.unpackOptionalCallback(data, 'onSelected'),
      onCanceled: runtime.unpackOptionalCallback(data, 'onCanceled'),
      tooltip: runtime.unpackOptionalField<String>(data, 'tooltip'),
      elevation: runtime.unpackOptionalField<double>(data, 'elevation'),
      shadowColor: runtime.unpackOptionalField<Color>(data, 'shadowColor'),
      surfaceTintColor: runtime.unpackOptionalField<Color>(
        data,
        'surfaceTintColor',
      ),
      padding: runtime.unpackRequiredField<EdgeInsets>(data, 'padding'),
      menuPadding: runtime.unpackOptionalField<EdgeInsets>(data, 'menuPadding'),
      borderRadius: runtime.unpackOptionalField<BorderRadius>(
        data,
        'borderRadius',
      ),
      splashRadius: runtime.unpackOptionalField<double>(data, 'splashRadius'),
      icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
      iconSize: runtime.unpackOptionalField<double>(data, 'iconSize'),
      offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      color: runtime.unpackOptionalField<Color>(data, 'color'),
      iconColor: runtime.unpackOptionalField<Color>(data, 'iconColor'),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      position: runtime.unpackOptionalField<PopupMenuPosition>(
        data,
        'position',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      useRootNavigator: runtime.unpackRequiredField<bool>(
        data,
        'useRootNavigator',
      ),
      popUpAnimationStyle: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'popUpAnimationStyle',
      ),
      routeSettings: runtime.unpackOptionalField<RouteSettings>(
        data,
        'routeSettings',
      ),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
      requestFocus: runtime.unpackOptionalField<bool>(data, 'requestFocus'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutShowMenu {
  FlutShowMenu._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('showMenu.showMenu', _showMenu);
  }

  static dynamic _showMenu(
    FlutRuntime runtime,
    BuildContext context, {
    RelativeRect? position,
    required List<dynamic> items,
    dynamic initialValue,
    double? elevation,
    Color? shadowColor,
    Color? surfaceTintColor,
    String? semanticLabel,
    ShapeBorder? shape,
    EdgeInsetsGeometry? menuPadding,
    Color? color,
    bool useRootNavigator = false,
    BoxConstraints? constraints,
    Clip clipBehavior = Clip.none,
    RouteSettings? routeSettings,
    AnimationStyle? popUpAnimationStyle,
    bool? requestFocus,
  }) {
    return showMenu<dynamic>(
      context: context,
      position: position,
      items: items
          .map((item) => runtime.resolveArg(item) as PopupMenuEntry<dynamic>)
          .toList(),
      initialValue: initialValue,
      elevation: elevation,
      shadowColor: shadowColor,
      surfaceTintColor: surfaceTintColor,
      semanticLabel: semanticLabel,
      shape: shape,
      menuPadding: menuPadding,
      color: color,
      useRootNavigator: useRootNavigator,
      constraints: constraints,
      clipBehavior: clipBehavior,
      routeSettings: routeSettings,
      popUpAnimationStyle: popUpAnimationStyle,
      requestFocus: requestFocus,
    );
  }
}
