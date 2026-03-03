import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flut/flut/runtime.dart';

class FlutMenuBar {
  FlutMenuBar._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MenuBar(
      key: runtime.decodeKey(data),
      style: runtime.unpackOptionalField<MenuStyle>(data, 'style'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      controller: runtime.unpackOptionalField<MenuController>(
        data,
        'controller',
      ),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutMenuAnchor {
  FlutMenuAnchor._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MenuAnchor(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<MenuController>(
        data,
        'controller',
      ),
      childFocusNode: runtime.unpackOptionalField<FocusNode>(
        data,
        'childFocusNode',
      ),
      style: runtime.unpackOptionalField<MenuStyle>(data, 'style'),
      alignmentOffset: runtime.unpackRequiredField<Offset>(
        data,
        'alignmentOffset',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      consumeOutsideTap: runtime.unpackRequiredField<bool>(
        data,
        'consumeOutsideTap',
      ),
      onOpen: runtime.unpackOptionalCallback(data, 'onOpen'),
      onClose: runtime.unpackOptionalCallback(data, 'onClose'),
      crossAxisUnconstrained: runtime.unpackRequiredField<bool>(
        data,
        'crossAxisUnconstrained',
      ),
      useRootOverlay: runtime.unpackRequiredField<bool>(data, 'useRootOverlay'),
      menuChildren: runtime.unpackRequiredField<List<Widget>>(
        data,
        'menuChildren',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutMenuItemButton {
  FlutMenuItemButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MenuItemButton(
      key: runtime.decodeKey(data),
      onPressed: runtime.unpackOptionalCallback(data, 'onPressed'),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      requestFocusOnHover: runtime.unpackRequiredField<bool>(
        data,
        'requestFocusOnHover',
      ),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      shortcut: runtime.unpackOptionalField<MenuSerializableShortcut>(
        data,
        'shortcut',
      ),
      semanticsLabel: runtime.unpackOptionalField<String>(
        data,
        'semanticsLabel',
      ),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
      statesController: runtime.unpackOptionalField<WidgetStatesController>(
        data,
        'statesController',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      leadingIcon: runtime.unpackOptionalField<Widget>(data, 'leadingIcon'),
      trailingIcon: runtime.unpackOptionalField<Widget>(data, 'trailingIcon'),
      closeOnActivate: runtime.unpackRequiredField<bool>(
        data,
        'closeOnActivate',
      ),
      overflowAxis: runtime.unpackRequiredField<Axis>(data, 'overflowAxis'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutSubmenuButton {
  FlutSubmenuButton._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return SubmenuButton(
      key: runtime.decodeKey(data),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      onFocusChange: runtime.unpackOptionalCallback(data, 'onFocusChange'),
      onOpen: runtime.unpackOptionalCallback(data, 'onOpen'),
      onClose: runtime.unpackOptionalCallback(data, 'onClose'),
      controller: runtime.unpackOptionalField<MenuController>(
        data,
        'controller',
      ),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
      menuStyle: runtime.unpackOptionalField<MenuStyle>(data, 'menuStyle'),
      alignmentOffset: runtime.unpackOptionalField<Offset>(
        data,
        'alignmentOffset',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      statesController: runtime.unpackOptionalField<WidgetStatesController>(
        data,
        'statesController',
      ),
      leadingIcon: runtime.unpackOptionalField<Widget>(data, 'leadingIcon'),
      trailingIcon: runtime.unpackOptionalField<Widget>(data, 'trailingIcon'),
      useRootOverlay: runtime.unpackRequiredField<bool>(data, 'useRootOverlay'),
      menuChildren: runtime.unpackRequiredField<List<Widget>>(
        data,
        'menuChildren',
      ),
      child: runtime.unpackNullableRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutMenuAcceleratorLabel {
  FlutMenuAcceleratorLabel._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MenuAcceleratorLabel(
      runtime.unpackRequiredField<String>(data, 'label'),
      key: runtime.decodeKey(data),
    );
  }
}
