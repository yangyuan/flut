import 'package:flutter/services.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutTextInputAction extends FlutEnumObject<TextInputAction> {
  const FlutTextInputAction()
    : super('TextInputAction', const {
        'none': TextInputAction.none,
        'unspecified': TextInputAction.unspecified,
        'done': TextInputAction.done,
        'go': TextInputAction.go,
        'search': TextInputAction.search,
        'send': TextInputAction.send,
        'next': TextInputAction.next,
        'previous': TextInputAction.previous,
        'continueAction': TextInputAction.continueAction,
        'join': TextInputAction.join,
        'route': TextInputAction.route,
        'emergencyCall': TextInputAction.emergencyCall,
        'newline': TextInputAction.newline,
      });
}

class FlutTextInputType extends FlutValueObject {
  final TextInputType value;
  const FlutTextInputType(this.value) : super('TextInputType');

  @override
  Map<String, dynamic> flutEncode() {
    if (value == TextInputType.text) {
      final result = flutBaseProps();
      result['name'] = 'text';
      return result;
    }
    if (value == TextInputType.multiline) {
      final result = flutBaseProps();
      result['name'] = 'multiline';
      return result;
    }
    if (value == TextInputType.number) {
      final result = flutBaseProps();
      result['name'] = 'number';
      return result;
    }
    if (value == TextInputType.phone) {
      final result = flutBaseProps();
      result['name'] = 'phone';
      return result;
    }
    if (value == TextInputType.datetime) {
      final result = flutBaseProps();
      result['name'] = 'datetime';
      return result;
    }
    if (value == TextInputType.emailAddress) {
      final result = flutBaseProps();
      result['name'] = 'emailAddress';
      return result;
    }
    if (value == TextInputType.url) {
      final result = flutBaseProps();
      result['name'] = 'url';
      return result;
    }
    if (value == TextInputType.visiblePassword) {
      final result = flutBaseProps();
      result['name'] = 'visiblePassword';
      return result;
    }
    if (value == TextInputType.name) {
      final result = flutBaseProps();
      result['name'] = 'name';
      return result;
    }
    if (value == TextInputType.streetAddress) {
      final result = flutBaseProps();
      result['name'] = 'streetAddress';
      return result;
    }
    if (value == TextInputType.none) {
      final result = flutBaseProps();
      result['name'] = 'none';
      return result;
    }
    throw ArgumentError('Unknown TextInputType: $value');
  }

  static TextInputType? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final name = runtime.unpackRequiredField<String>(data, 'name');
    if (name == 'text') return TextInputType.text;
    if (name == 'multiline') return TextInputType.multiline;
    if (name == 'number') return TextInputType.number;
    if (name == 'phone') return TextInputType.phone;
    if (name == 'datetime') return TextInputType.datetime;
    if (name == 'emailAddress') return TextInputType.emailAddress;
    if (name == 'url') return TextInputType.url;
    if (name == 'visiblePassword') return TextInputType.visiblePassword;
    if (name == 'name') return TextInputType.name;
    if (name == 'streetAddress') return TextInputType.streetAddress;
    if (name == 'none') return TextInputType.none;
    throw ArgumentError('Unknown TextInputType name: $name');
  }
}
