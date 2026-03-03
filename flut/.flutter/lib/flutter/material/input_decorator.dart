import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/painting/edge_insets.dart';
import 'package:flut/flutter/material/input_border.dart';

class FlutFloatingLabelBehavior extends FlutEnumObject<FloatingLabelBehavior> {
  const FlutFloatingLabelBehavior()
    : super('FloatingLabelBehavior', const {
        'never': FloatingLabelBehavior.never,
        'auto': FloatingLabelBehavior.auto,
        'always': FloatingLabelBehavior.always,
      });
}

class FlutInputDecoration extends FlutValueObject {
  final InputDecoration inputDecoration;

  const FlutInputDecoration(this.inputDecoration) : super('InputDecoration');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (inputDecoration.hintText != null) {
      result['hintText'] = inputDecoration.hintText;
    }
    if (inputDecoration.contentPadding != null &&
        inputDecoration.contentPadding is EdgeInsets) {
      result['contentPadding'] = FlutEdgeInsets(
        inputDecoration.contentPadding! as EdgeInsets,
      ).flutEncode();
    }
    if (inputDecoration.filled != null) {
      result['filled'] = inputDecoration.filled;
    }
    if (inputDecoration.fillColor != null) {
      result['fillColor'] = FlutColor(inputDecoration.fillColor!).flutEncode();
    }
    if (inputDecoration.border != null) {
      result['border'] = FlutInputBorder(inputDecoration.border!).flutEncode();
    }
    return result;
  }

  static InputDecoration? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return InputDecoration(
      icon: runtime.unpackOptionalField<Widget>(data, 'icon'),
      iconColor: runtime.unpackOptionalField<Color>(data, 'iconColor'),
      label: runtime.unpackOptionalField<Widget>(data, 'label'),
      labelText: runtime.unpackOptionalField<String>(data, 'labelText'),
      labelStyle: runtime.unpackOptionalField<TextStyle>(data, 'labelStyle'),
      floatingLabelStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'floatingLabelStyle',
      ),
      helper: runtime.unpackOptionalField<Widget>(data, 'helper'),
      helperText: runtime.unpackOptionalField<String>(data, 'helperText'),
      helperStyle: runtime.unpackOptionalField<TextStyle>(data, 'helperStyle'),
      helperMaxLines: runtime.unpackOptionalField<int>(data, 'helperMaxLines'),
      hintText: runtime.unpackOptionalField<String>(data, 'hintText'),
      hint: runtime.unpackOptionalField<Widget>(data, 'hint'),
      hintStyle: runtime.unpackOptionalField<TextStyle>(data, 'hintStyle'),
      hintTextDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'hintTextDirection',
      ),
      hintMaxLines: runtime.unpackOptionalField<int>(data, 'hintMaxLines'),
      hintFadeDuration: runtime.unpackOptionalField<Duration>(
        data,
        'hintFadeDuration',
      ),
      maintainHintSize: runtime.unpackRequiredField<bool>(
        data,
        'maintainHintSize',
      ),
      maintainLabelSize: runtime.unpackRequiredField<bool>(
        data,
        'maintainLabelSize',
      ),
      error: runtime.unpackOptionalField<Widget>(data, 'error'),
      errorText: runtime.unpackOptionalField<String>(data, 'errorText'),
      errorStyle: runtime.unpackOptionalField<TextStyle>(data, 'errorStyle'),
      errorMaxLines: runtime.unpackOptionalField<int>(data, 'errorMaxLines'),
      floatingLabelBehavior: runtime.unpackOptionalField<FloatingLabelBehavior>(
        data,
        'floatingLabelBehavior',
      ),
      isCollapsed: runtime.unpackOptionalField<bool>(data, 'isCollapsed'),
      isDense: runtime.unpackOptionalField<bool>(data, 'isDense'),
      contentPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'contentPadding',
      ),
      prefixIcon: runtime.unpackOptionalField<Widget>(data, 'prefixIcon'),
      prefixIconConstraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'prefixIconConstraints',
      ),
      prefix: runtime.unpackOptionalField<Widget>(data, 'prefix'),
      prefixText: runtime.unpackOptionalField<String>(data, 'prefixText'),
      prefixStyle: runtime.unpackOptionalField<TextStyle>(data, 'prefixStyle'),
      prefixIconColor: runtime.unpackOptionalField<Color>(
        data,
        'prefixIconColor',
      ),
      suffixIcon: runtime.unpackOptionalField<Widget>(data, 'suffixIcon'),
      suffix: runtime.unpackOptionalField<Widget>(data, 'suffix'),
      suffixText: runtime.unpackOptionalField<String>(data, 'suffixText'),
      suffixStyle: runtime.unpackOptionalField<TextStyle>(data, 'suffixStyle'),
      suffixIconColor: runtime.unpackOptionalField<Color>(
        data,
        'suffixIconColor',
      ),
      suffixIconConstraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'suffixIconConstraints',
      ),
      counter: runtime.unpackOptionalField<Widget>(data, 'counter'),
      counterText: runtime.unpackOptionalField<String>(data, 'counterText'),
      counterStyle: runtime.unpackOptionalField<TextStyle>(
        data,
        'counterStyle',
      ),
      filled: runtime.unpackOptionalField<bool>(data, 'filled'),
      fillColor: runtime.unpackOptionalField<Color>(data, 'fillColor'),
      focusColor: runtime.unpackOptionalField<Color>(data, 'focusColor'),
      hoverColor: runtime.unpackOptionalField<Color>(data, 'hoverColor'),
      errorBorder: runtime.unpackOptionalField<InputBorder>(
        data,
        'errorBorder',
      ),
      focusedBorder: runtime.unpackOptionalField<InputBorder>(
        data,
        'focusedBorder',
      ),
      focusedErrorBorder: runtime.unpackOptionalField<InputBorder>(
        data,
        'focusedErrorBorder',
      ),
      disabledBorder: runtime.unpackOptionalField<InputBorder>(
        data,
        'disabledBorder',
      ),
      enabledBorder: runtime.unpackOptionalField<InputBorder>(
        data,
        'enabledBorder',
      ),
      border: runtime.unpackOptionalField<InputBorder>(data, 'border'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      semanticCounterText: runtime.unpackOptionalField<String>(
        data,
        'semanticCounterText',
      ),
      alignLabelWithHint: runtime.unpackOptionalField<bool>(
        data,
        'alignLabelWithHint',
      ),
      constraints: runtime.unpackOptionalField<BoxConstraints>(
        data,
        'constraints',
      ),
    );
  }
}
