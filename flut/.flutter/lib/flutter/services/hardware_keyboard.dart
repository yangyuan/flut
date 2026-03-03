import 'package:flutter/services.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';
import 'package:flut/dart/core.dart';
import 'package:flut/flutter/services/keyboard_key.dart';

class _FlutKeyEvent extends KeyEvent {
  const _FlutKeyEvent({
    required super.physicalKey,
    required super.logicalKey,
    super.character,
    required super.timeStamp,
    super.synthesized,
  });
}

class FlutKeyEvent extends FlutValueObject {
  final KeyEvent event;

  FlutKeyEvent(this.event) : super('KeyEvent');

  FlutKeyEvent._(this.event, String type) : super(type);

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['logicalKey'] = FlutLogicalKeyboardKey(
      event.logicalKey,
    ).flutEncode();
    result['physicalKey'] = FlutPhysicalKeyboardKey(
      event.physicalKey,
    ).flutEncode();
    result['character'] = event.character;
    result['timeStamp'] = FlutDuration(event.timeStamp).flutEncode();
    result['synthesized'] = event.synthesized;
    return result;
  }

  static KeyEvent? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return _FlutKeyEvent(
      physicalKey: runtime.unpackRequiredField<PhysicalKeyboardKey>(
        data,
        'physicalKey',
      ),
      logicalKey: runtime.unpackRequiredField<LogicalKeyboardKey>(
        data,
        'logicalKey',
      ),
      character: runtime.unpackOptionalField<String>(data, 'character'),
      timeStamp: runtime.unpackRequiredField<Duration>(data, 'timeStamp'),
      synthesized: runtime.unpackRequiredField<bool>(data, 'synthesized'),
    );
  }
}

class FlutKeyDownEvent extends FlutKeyEvent {
  FlutKeyDownEvent(KeyDownEvent event) : super._(event, 'KeyDownEvent');

  static KeyDownEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return KeyDownEvent(
      physicalKey: runtime.unpackRequiredField<PhysicalKeyboardKey>(
        data,
        'physicalKey',
      ),
      logicalKey: runtime.unpackRequiredField<LogicalKeyboardKey>(
        data,
        'logicalKey',
      ),
      character: runtime.unpackOptionalField<String>(data, 'character'),
      timeStamp: runtime.unpackRequiredField<Duration>(data, 'timeStamp'),
      synthesized: runtime.unpackRequiredField<bool>(data, 'synthesized'),
    );
  }
}

class FlutKeyUpEvent extends FlutKeyEvent {
  FlutKeyUpEvent(KeyUpEvent event) : super._(event, 'KeyUpEvent');

  static KeyUpEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return KeyUpEvent(
      physicalKey: runtime.unpackRequiredField<PhysicalKeyboardKey>(
        data,
        'physicalKey',
      ),
      logicalKey: runtime.unpackRequiredField<LogicalKeyboardKey>(
        data,
        'logicalKey',
      ),
      timeStamp: runtime.unpackRequiredField<Duration>(data, 'timeStamp'),
      synthesized: runtime.unpackRequiredField<bool>(data, 'synthesized'),
    );
  }
}

class FlutKeyRepeatEvent extends FlutKeyEvent {
  FlutKeyRepeatEvent(KeyRepeatEvent event) : super._(event, 'KeyRepeatEvent');

  static KeyRepeatEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return KeyRepeatEvent(
      physicalKey: runtime.unpackRequiredField<PhysicalKeyboardKey>(
        data,
        'physicalKey',
      ),
      logicalKey: runtime.unpackRequiredField<LogicalKeyboardKey>(
        data,
        'logicalKey',
      ),
      character: runtime.unpackOptionalField<String>(data, 'character'),
      timeStamp: runtime.unpackRequiredField<Duration>(data, 'timeStamp'),
    );
  }
}

class FlutHardwareKeyboard with FlutRealtimeObject<HardwareKeyboard> {
  FlutHardwareKeyboard.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required HardwareKeyboard target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'HardwareKeyboard',
      target: target,
    );
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('HardwareKeyboard.instance', instance);
  }

  static FlutHardwareKeyboard instance(FlutRuntime runtime) {
    final keyboard = HardwareKeyboard.instance;
    return runtime.wrapObject<FlutHardwareKeyboard>(
      keyboard,
      (oid) => FlutHardwareKeyboard.createFromObject(
        runtime: runtime,
        oid: oid,
        target: keyboard,
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'physicalKeysPressed':
        return flutTarget.physicalKeysPressed
            .map((k) => k.usbHidUsage)
            .toList();
      case 'logicalKeysPressed':
        return flutTarget.logicalKeysPressed.map((k) => k.keyId).toList();
      case 'isShiftPressed':
        return flutTarget.isShiftPressed;
      case 'isControlPressed':
        return flutTarget.isControlPressed;
      case 'isAltPressed':
        return flutTarget.isAltPressed;
      case 'isMetaPressed':
        return flutTarget.isMetaPressed;
    }
    throw FlutUnknownPropertyException('HardwareKeyboard', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('HardwareKeyboard', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'isPhysicalKeyPressed':
        return flutTarget.isPhysicalKeyPressed(
          runtime.decodeObject<PhysicalKeyboardKey>(
            args[0] as Map<String, dynamic>,
          )!,
        );
      case 'isLogicalKeyPressed':
        return flutTarget.isLogicalKeyPressed(
          runtime.decodeObject<LogicalKeyboardKey>(
            args[0] as Map<String, dynamic>,
          )!,
        );
    }
    throw FlutUnknownMethodException(method);
  }
}
