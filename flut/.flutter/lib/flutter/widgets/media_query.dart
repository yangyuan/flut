import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/edge_insets.dart';
import 'package:flut/flutter/gestures/gesture_settings.dart';
import 'package:flut/flutter/painting/text_scaler.dart';

class FlutMediaQueryData extends FlutValueObject {
  final MediaQueryData data;
  const FlutMediaQueryData(this.data) : super('MediaQueryData');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['size'] = FlutSize(data.size).flutEncode();
    result['devicePixelRatio'] = data.devicePixelRatio;
    result['textScaler'] = FlutTextScaler(data.textScaler).flutEncode();
    result['platformBrightness'] = const FlutBrightness().flutEncode(
      data.platformBrightness,
    );
    result['padding'] = FlutEdgeInsets(data.padding).flutEncode();
    result['viewInsets'] = FlutEdgeInsets(data.viewInsets).flutEncode();
    result['systemGestureInsets'] = FlutEdgeInsets(
      data.systemGestureInsets,
    ).flutEncode();
    result['viewPadding'] = FlutEdgeInsets(data.viewPadding).flutEncode();
    result['alwaysUse24HourFormat'] = data.alwaysUse24HourFormat;
    result['accessibleNavigation'] = data.accessibleNavigation;
    result['invertColors'] = data.invertColors;
    result['highContrast'] = data.highContrast;
    result['onOffSwitchLabels'] = data.onOffSwitchLabels;
    result['disableAnimations'] = data.disableAnimations;
    result['boldText'] = data.boldText;
    result['supportsShowingSystemContextMenu'] =
        data.supportsShowingSystemContextMenu;
    result['supportsAnnounce'] = data.supportsAnnounce;
    result['navigationMode'] = const FlutNavigationMode().flutEncode(
      data.navigationMode,
    );
    result['gestureSettings'] = FlutDeviceGestureSettings(
      data.gestureSettings,
    ).flutEncode();
    if (data.lineHeightScaleFactorOverride != null) {
      result['lineHeightScaleFactorOverride'] =
          data.lineHeightScaleFactorOverride;
    }
    if (data.letterSpacingOverride != null) {
      result['letterSpacingOverride'] = data.letterSpacingOverride;
    }
    if (data.wordSpacingOverride != null) {
      result['wordSpacingOverride'] = data.wordSpacingOverride;
    }
    if (data.paragraphSpacingOverride != null) {
      result['paragraphSpacingOverride'] = data.paragraphSpacingOverride;
    }
    return result;
  }

  static MediaQueryData? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return MediaQueryData(
      size: runtime.unpackRequiredField<Size>(data, 'size'),
      devicePixelRatio: runtime.unpackRequiredField<double>(
        data,
        'devicePixelRatio',
      ),
      textScaler: runtime.unpackRequiredField<TextScaler>(data, 'textScaler'),
      platformBrightness: runtime.unpackRequiredField<Brightness>(
        data,
        'platformBrightness',
      ),
      padding: runtime.unpackRequiredField<EdgeInsets>(data, 'padding'),
      viewInsets: runtime.unpackRequiredField<EdgeInsets>(data, 'viewInsets'),
      systemGestureInsets: runtime.unpackRequiredField<EdgeInsets>(
        data,
        'systemGestureInsets',
      ),
      viewPadding: runtime.unpackRequiredField<EdgeInsets>(data, 'viewPadding'),
      alwaysUse24HourFormat: runtime.unpackRequiredField<bool>(
        data,
        'alwaysUse24HourFormat',
      ),
      accessibleNavigation: runtime.unpackRequiredField<bool>(
        data,
        'accessibleNavigation',
      ),
      invertColors: runtime.unpackRequiredField<bool>(data, 'invertColors'),
      highContrast: runtime.unpackRequiredField<bool>(data, 'highContrast'),
      onOffSwitchLabels: runtime.unpackRequiredField<bool>(
        data,
        'onOffSwitchLabels',
      ),
      disableAnimations: runtime.unpackRequiredField<bool>(
        data,
        'disableAnimations',
      ),
      boldText: runtime.unpackRequiredField<bool>(data, 'boldText'),
      supportsShowingSystemContextMenu: runtime.unpackRequiredField<bool>(
        data,
        'supportsShowingSystemContextMenu',
      ),
      supportsAnnounce: runtime.unpackRequiredField<bool>(
        data,
        'supportsAnnounce',
      ),
      navigationMode: runtime.unpackRequiredField<NavigationMode>(
        data,
        'navigationMode',
      ),
      gestureSettings: runtime.unpackRequiredField<DeviceGestureSettings>(
        data,
        'gestureSettings',
      ),
      lineHeightScaleFactorOverride: runtime.unpackOptionalField<double>(
        data,
        'lineHeightScaleFactorOverride',
      ),
      letterSpacingOverride: runtime.unpackOptionalField<double>(
        data,
        'letterSpacingOverride',
      ),
      wordSpacingOverride: runtime.unpackOptionalField<double>(
        data,
        'wordSpacingOverride',
      ),
      paragraphSpacingOverride: runtime.unpackOptionalField<double>(
        data,
        'paragraphSpacingOverride',
      ),
    );
  }
}

class FlutMediaQuery {
  FlutMediaQuery._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('MediaQuery.of', of);
  }

  static MediaQueryData of(FlutRuntime runtime, BuildContext context) {
    return MediaQuery.of(context);
  }
}

class FlutOrientation extends FlutEnumObject<Orientation> {
  const FlutOrientation()
    : super('Orientation', const {
        'portrait': Orientation.portrait,
        'landscape': Orientation.landscape,
      });
}

class FlutNavigationMode extends FlutEnumObject<NavigationMode> {
  const FlutNavigationMode()
    : super('NavigationMode', const {
        'traditional': NavigationMode.traditional,
        'directional': NavigationMode.directional,
      });
}
