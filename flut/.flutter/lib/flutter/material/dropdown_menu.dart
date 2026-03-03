import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutDropdownMenuEntry extends FlutValueObject {
  final DropdownMenuEntry entry;
  const FlutDropdownMenuEntry(this.entry) : super('DropdownMenuEntry');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['value'] = entry.value;
    result['label'] = entry.label;
    result['enabled'] = entry.enabled;
    return result;
  }

  static DropdownMenuEntry? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DropdownMenuEntry(
      value: runtime.unpackDynamicRequiredField(data, 'value'),
      label: runtime.unpackRequiredField<String>(data, 'label'),
      labelWidget: runtime.unpackOptionalField<Widget>(data, 'labelWidget'),
      leadingIcon: runtime.unpackOptionalField<Widget>(data, 'leadingIcon'),
      trailingIcon: runtime.unpackOptionalField<Widget>(data, 'trailingIcon'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      style: runtime.unpackOptionalField<ButtonStyle>(data, 'style'),
    );
  }
}

class FlutDropdownMenuCloseBehavior
    extends FlutEnumObject<DropdownMenuCloseBehavior> {
  const FlutDropdownMenuCloseBehavior()
    : super('DropdownMenuCloseBehavior', const {
        'all': DropdownMenuCloseBehavior.all,
        'self': DropdownMenuCloseBehavior.self,
        'none': DropdownMenuCloseBehavior.none,
      });
}

class FlutDropdownMenu {
  FlutDropdownMenu._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return DropdownMenu<dynamic>(
      key: runtime.decodeKey(data),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      width: runtime.unpackOptionalField<double>(data, 'width'),
      menuHeight: runtime.unpackOptionalField<double>(data, 'menuHeight'),
      leadingIcon: runtime.unpackOptionalField<Widget>(data, 'leadingIcon'),
      trailingIcon: runtime.unpackOptionalField<Widget>(data, 'trailingIcon'),
      showTrailingIcon: runtime.unpackRequiredField<bool>(
        data,
        'showTrailingIcon',
      ),
      trailingIconFocusNode: runtime.unpackOptionalField<FocusNode>(
        data,
        'trailingIconFocusNode',
      ),
      label: runtime.unpackOptionalField<Widget>(data, 'label'),
      hintText: runtime.unpackOptionalField<String>(data, 'hintText'),
      helperText: runtime.unpackOptionalField<String>(data, 'helperText'),
      errorText: runtime.unpackOptionalField<String>(data, 'errorText'),
      selectedTrailingIcon: runtime.unpackOptionalField<Widget>(
        data,
        'selectedTrailingIcon',
      ),
      enableFilter: runtime.unpackRequiredField<bool>(data, 'enableFilter'),
      enableSearch: runtime.unpackRequiredField<bool>(data, 'enableSearch'),
      keyboardType: runtime.unpackOptionalField<TextInputType>(
        data,
        'keyboardType',
      ),
      textStyle: runtime.unpackOptionalField<TextStyle>(data, 'textStyle'),
      textAlign: runtime.unpackRequiredField<TextAlign>(data, 'textAlign'),
      inputDecorationTheme: runtime.unpackOptionalField<InputDecorationTheme>(
        data,
        'inputDecorationTheme',
      ),
      menuStyle: runtime.unpackOptionalField<MenuStyle>(data, 'menuStyle'),
      controller: runtime.unpackOptionalField<TextEditingController>(
        data,
        'controller',
      ),
      initialSelection: runtime.unpackDynamicOptionalField(
        data,
        'initialSelection',
      ),
      onSelected: runtime.unpackOptionalCallback(data, 'onSelected'),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      requestFocusOnTap: runtime.unpackOptionalField<bool>(
        data,
        'requestFocusOnTap',
      ),
      selectOnly: runtime.unpackRequiredField<bool>(data, 'selectOnly'),
      expandedInsets: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'expandedInsets',
      ),
      alignmentOffset: runtime.unpackOptionalField<Offset>(
        data,
        'alignmentOffset',
      ),
      dropdownMenuEntries: runtime
          .unpackRequiredField<List<DropdownMenuEntry<dynamic>>>(
            data,
            'dropdownMenuEntries',
          ),
      inputFormatters: runtime.unpackOptionalField<List<TextInputFormatter>>(
        data,
        'inputFormatters',
      ),
      closeBehavior: runtime.unpackRequiredField<DropdownMenuCloseBehavior>(
        data,
        'closeBehavior',
      ),
      maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
      textInputAction: runtime.unpackOptionalField<TextInputAction>(
        data,
        'textInputAction',
      ),
      cursorHeight: runtime.unpackOptionalField<double>(data, 'cursorHeight'),
      restorationId: runtime.unpackOptionalField<String>(data, 'restorationId'),
      menuController: runtime.unpackOptionalField<MenuController>(
        data,
        'menuController',
      ),
      decorationBuilder: runtime.unpackOptionalCallback(
        data,
        'decorationBuilder',
      ),
      filterCallback: runtime.unpackOptionalCallback(data, 'filterCallback'),
      searchCallback: runtime.unpackOptionalCallback(data, 'searchCallback'),
    );
  }
}
