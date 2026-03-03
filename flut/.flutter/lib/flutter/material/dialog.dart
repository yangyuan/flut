import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutAlertDialog {
  FlutAlertDialog._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return AlertDialog(
      key: runtime.decodeKey(data),
      icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
      iconPadding: runtime.unpackOptionalField<EdgeInsets>(data, 'iconPadding'),
      iconColor: runtime.unpackOptionalField<Color>(data, 'iconColor'),
      title: runtime.unpackOptionalField<Widget>(data, 'title'),
      titlePadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'titlePadding',
      ),
      titleTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'titleTextStyle',
      ),
      content: runtime.unpackOptionalField<Widget>(data, 'content'),
      contentPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'contentPadding',
      ),
      contentTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'contentTextStyle',
      ),
      actions: runtime.unpackOptionalField<List<Widget>>(data, 'actions'),
      actionsPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'actionsPadding',
      ),
      actionsAlignment: runtime.unpackOptionalField<MainAxisAlignment>(
        data,
        'actionsAlignment',
      ),
      actionsOverflowAlignment: runtime
          .unpackOptionalField<OverflowBarAlignment>(
            data,
            'actionsOverflowAlignment',
          ),
      actionsOverflowDirection: runtime.unpackOptionalField<VerticalDirection>(
        data,
        'actionsOverflowDirection',
      ),
      actionsOverflowButtonSpacing: runtime.unpackOptionalField<double>(
        data,
        'actionsOverflowButtonSpacing',
      ),
      buttonPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'buttonPadding',
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
      semanticLabel: runtime.unpackOptionalField<String>(data, 'semanticLabel'),
      insetPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'insetPadding',
      ),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      alignment: runtime.unpackOptionalField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      scrollable: runtime.unpackRequiredField<bool>(data, 'scrollable'),
    );
  }
}

class FlutDialog {
  FlutDialog._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Dialog(
      key: runtime.decodeKey(data),
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
      insetAnimationDuration:
          runtime.unpackOptionalField<Duration>(
            data,
            'insetAnimationDuration',
          ) ??
          const Duration(milliseconds: 100),
      insetAnimationCurve:
          runtime.unpackOptionalField<Curve>(data, 'insetAnimationCurve') ??
          Curves.decelerate,
      insetPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'insetPadding',
      ),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      alignment: runtime.unpackOptionalField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutSimpleDialog {
  FlutSimpleDialog._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return SimpleDialog(
      key: runtime.decodeKey(data),
      title: runtime.unpackOptionalField<Widget>(data, 'title'),
      titlePadding:
          runtime.unpackOptionalField<EdgeInsetsGeometry>(
            data,
            'titlePadding',
          ) ??
          const EdgeInsets.fromLTRB(24.0, 24.0, 24.0, 0.0),
      titleTextStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'titleTextStyle',
      ),
      contentPadding:
          runtime.unpackOptionalField<EdgeInsetsGeometry>(
            data,
            'contentPadding',
          ) ??
          const EdgeInsets.fromLTRB(0.0, 12.0, 0.0, 16.0),
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
      semanticLabel: runtime.unpackOptionalField<String>(data, 'semanticLabel'),
      insetPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'insetPadding',
      ),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      alignment: runtime.unpackOptionalField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
      children: runtime.unpackOptionalField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutSimpleDialogOption {
  FlutSimpleDialogOption._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return SimpleDialogOption(
      key: runtime.decodeKey(data),
      onPressed:
          runtime.unpackOptionalCallback(data, 'onPressed') as VoidCallback?,
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutShowDialog {
  FlutShowDialog._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('showDialog.showDialog', _showDialog);
  }

  static dynamic _showDialog(
    FlutRuntime runtime,
    BuildContext context,
    Widget dialogScope, {
    bool barrierDismissible = true,
    Color? barrierColor,
    bool useSafeArea = true,
    bool useRootNavigator = true,
    RouteSettings? routeSettings,
    Offset? anchorPoint,
    TraversalEdgeBehavior? traversalEdgeBehavior,
  }) {
    return showDialog(
      context: context,
      builder: (ctx) => dialogScope,
      barrierDismissible: barrierDismissible,
      barrierColor: barrierColor,
      useSafeArea: useSafeArea,
      useRootNavigator: useRootNavigator,
      routeSettings: routeSettings,
      anchorPoint: anchorPoint,
      traversalEdgeBehavior:
          traversalEdgeBehavior ?? TraversalEdgeBehavior.closedLoop,
    );
  }
}
