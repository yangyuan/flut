import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutPlatformProvidedMenuItemType
    extends FlutEnumObject<PlatformProvidedMenuItemType> {
  const FlutPlatformProvidedMenuItemType()
    : super('PlatformProvidedMenuItemType', const {
        'about': PlatformProvidedMenuItemType.about,
        'quit': PlatformProvidedMenuItemType.quit,
        'servicesSubmenu': PlatformProvidedMenuItemType.servicesSubmenu,
        'hide': PlatformProvidedMenuItemType.hide,
        'hideOtherApplications':
            PlatformProvidedMenuItemType.hideOtherApplications,
        'showAllApplications': PlatformProvidedMenuItemType.showAllApplications,
        'startSpeaking': PlatformProvidedMenuItemType.startSpeaking,
        'stopSpeaking': PlatformProvidedMenuItemType.stopSpeaking,
        'toggleFullScreen': PlatformProvidedMenuItemType.toggleFullScreen,
        'minimizeWindow': PlatformProvidedMenuItemType.minimizeWindow,
        'zoomWindow': PlatformProvidedMenuItemType.zoomWindow,
        'arrangeWindowsInFront':
            PlatformProvidedMenuItemType.arrangeWindowsInFront,
      });
}

class FlutPlatformMenuBar {
  FlutPlatformMenuBar._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return PlatformMenuBar(
      key: runtime.decodeKey(data),
      menus: runtime.unpackRequiredField<List<PlatformMenuItem>>(data, 'menus'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutPlatformMenu {
  FlutPlatformMenu._();

  static PlatformMenu? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PlatformMenu(
      label: runtime.unpackRequiredField<String>(data, 'label'),
      onOpen: runtime.unpackOptionalCallback(data, 'onOpen'),
      onClose: runtime.unpackOptionalCallback(data, 'onClose'),
      menus: runtime.unpackRequiredField<List<PlatformMenuItem>>(data, 'menus'),
    );
  }
}

class FlutPlatformMenuItem {
  FlutPlatformMenuItem._();

  static PlatformMenuItem? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PlatformMenuItem(
      label: runtime.unpackRequiredField<String>(data, 'label'),
      shortcut: runtime.unpackOptionalField<MenuSerializableShortcut>(
        data,
        'shortcut',
      ),
      onSelected: runtime.unpackOptionalCallback(data, 'onSelected'),
    );
  }
}

class FlutPlatformMenuItemGroup {
  FlutPlatformMenuItemGroup._();

  static PlatformMenuItemGroup? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PlatformMenuItemGroup(
      members: runtime.unpackRequiredField<List<PlatformMenuItem>>(
        data,
        'members',
      ),
    );
  }
}

class FlutPlatformProvidedMenuItem {
  FlutPlatformProvidedMenuItem._();

  static PlatformProvidedMenuItem? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return PlatformProvidedMenuItem(
      type: runtime.unpackRequiredField<PlatformProvidedMenuItemType>(
        data,
        'type',
      ),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
    );
  }
}
