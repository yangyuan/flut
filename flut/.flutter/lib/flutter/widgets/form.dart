import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutAutovalidateMode extends FlutEnumObject<AutovalidateMode> {
  const FlutAutovalidateMode()
    : super('AutovalidateMode', const {
        'disabled': AutovalidateMode.disabled,
        'always': AutovalidateMode.always,
        'onUserInteraction': AutovalidateMode.onUserInteraction,
        'onUnfocus': AutovalidateMode.onUnfocus,
        'onUserInteractionIfError': AutovalidateMode.onUserInteractionIfError,
      });
}

class FlutForm {
  FlutForm._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Form(
      key: runtime.decodeKey(data),
      onChanged: runtime.unpackOptionalCallback(data, 'onChanged'),
      autovalidateMode: runtime.unpackOptionalField<AutovalidateMode>(
        data,
        'autovalidateMode',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Form.of', _of);
  }

  static dynamic _of(FlutRuntime runtime, BuildContext context) {
    return Form.of(context);
  }
}

class FlutFormState with FlutRealtimeObject<FormState> {
  FlutFormState.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required FormState target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'FormState',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('FormState', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('FormState', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'validate':
        return flutTarget.validate();
      case 'validateGranularly':
        return flutTarget.validateGranularly().toList();
      case 'save':
        flutTarget.save();
        return null;
      case 'reset':
        flutTarget.reset();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}

class FlutFormFieldState with FlutRealtimeObject<FormFieldState> {
  FlutFormFieldState.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required FormFieldState target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'FormFieldState',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'value':
        return flutTarget.value;
      case 'hasError':
        return flutTarget.hasError;
      case 'errorText':
        return flutTarget.errorText;
      case 'isValid':
        return flutTarget.isValid;
      case 'hasInteractedByUser':
        return flutTarget.hasInteractedByUser;
    }
    throw FlutUnknownPropertyException('FormFieldState', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('FormFieldState', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'validate':
        return flutTarget.validate();
      case 'save':
        flutTarget.save();
        return null;
      case 'reset':
        flutTarget.reset();
        return null;
      case 'didChange':
        flutTarget.didChange(args.isNotEmpty ? args[0] : null);
        return null;
      case 'setValue':
        // ignore: invalid_use_of_protected_member
        flutTarget.setValue(args.isNotEmpty ? args[0] : null);
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
