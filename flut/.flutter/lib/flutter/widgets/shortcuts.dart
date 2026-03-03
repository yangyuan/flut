import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/widgets/actions.dart';

class FlutLockState extends FlutEnumObject<LockState> {
  const FlutLockState()
    : super('LockState', const {
        'ignored': LockState.ignored,
        'locked': LockState.locked,
        'unlocked': LockState.unlocked,
      });
}

class FlutSingleActivator extends FlutValueObject {
  final SingleActivator activator;
  const FlutSingleActivator(this.activator) : super('SingleActivator');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['trigger'] = encodeLogicalKey(activator.trigger);
    result['control'] = activator.control;
    result['shift'] = activator.shift;
    result['alt'] = activator.alt;
    result['meta'] = activator.meta;
    result['numLock'] = const FlutLockState().flutEncode(activator.numLock);
    result['includeRepeats'] = activator.includeRepeats;
    return result;
  }

  static Map<String, dynamic> encodeLogicalKey(LogicalKeyboardKey key) {
    return {'_flut_type': 'LogicalKeyboardKey', 'keyId': key.keyId};
  }

  static SingleActivator? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SingleActivator(
      runtime.unpackRequiredField<LogicalKeyboardKey>(data, 'trigger'),
      control: runtime.unpackRequiredField<bool>(data, 'control'),
      shift: runtime.unpackRequiredField<bool>(data, 'shift'),
      alt: runtime.unpackRequiredField<bool>(data, 'alt'),
      meta: runtime.unpackRequiredField<bool>(data, 'meta'),
      numLock: runtime.unpackRequiredField<LockState>(data, 'numLock'),
      includeRepeats: runtime.unpackRequiredField<bool>(data, 'includeRepeats'),
    );
  }
}

class FlutCharacterActivator extends FlutValueObject {
  final CharacterActivator activator;
  const FlutCharacterActivator(this.activator) : super('CharacterActivator');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['character'] = activator.character;
    result['control'] = activator.control;
    result['meta'] = activator.meta;
    result['alt'] = activator.alt;
    result['includeRepeats'] = activator.includeRepeats;
    return result;
  }

  static CharacterActivator? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CharacterActivator(
      runtime.unpackRequiredField<String>(data, 'character'),
      control: runtime.unpackRequiredField<bool>(data, 'control'),
      meta: runtime.unpackRequiredField<bool>(data, 'meta'),
      alt: runtime.unpackRequiredField<bool>(data, 'alt'),
      includeRepeats: runtime.unpackRequiredField<bool>(data, 'includeRepeats'),
    );
  }
}

/// Bridge intent used by FlutShortcuts to link Shortcuts → FlutActionScope.
class _FlutShortcutIntent extends Intent {
  final String intentName;
  final Map<String, dynamic>? intentData;
  const _FlutShortcutIntent(this.intentName, [this.intentData]);
}

class FlutShortcuts {
  FlutShortcuts._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final shortcutsList = data['shortcuts'] as List<dynamic>;
    final Map<ShortcutActivator, Intent> shortcuts = {};
    for (final item in shortcutsList) {
      final itemMap = item as Map<String, dynamic>;
      final activatorData = itemMap['activator'] as Map<String, dynamic>;
      final activator = _decodeActivator(runtime, activatorData);
      final intentName = itemMap['intentName'] as String;
      final intentData = itemMap['intentData'] as Map<String, dynamic>?;
      if (activator != null) {
        shortcuts[activator] = _FlutShortcutIntent(intentName, intentData);
      }
    }

    return Shortcuts(
      key: runtime.decodeKey(data),
      shortcuts: shortcuts,
      debugLabel: runtime.unpackOptionalField<String>(data, 'debugLabel'),
      includeSemantics: runtime.unpackRequiredField<bool>(
        data,
        'includeSemantics',
      ),
      child: Actions(
        actions: <Type, Action<Intent>>{
          _FlutShortcutIntent: CallbackAction<_FlutShortcutIntent>(
            onInvoke: (intent) {
              final ctx = primaryFocus?.context;
              if (ctx != null) {
                FlutActionScope.invokeHandler(
                  ctx,
                  runtime,
                  intent.intentName,
                  intent.intentData,
                );
              }
              return null;
            },
          ),
        },
        child: runtime.unpackRequiredField<Widget>(data, 'child'),
      ),
    );
  }
}

class FlutCallbackShortcuts {
  FlutCallbackShortcuts._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final bindingsList = data['bindings'] as List<dynamic>;
    final Map<ShortcutActivator, VoidCallback> bindings = {};
    for (final item in bindingsList) {
      final itemMap = item as Map<String, dynamic>;
      final activatorData = itemMap['activator'] as Map<String, dynamic>;
      final activator = _decodeActivator(runtime, activatorData);
      final callbackData = itemMap['callback'] as Map<String, dynamic>;
      final callableRef = FlutCallableRef.flutDecode(runtime, callbackData);
      if (activator != null && callableRef != null) {
        final adapted = runtime.adaptCallableByType(callableRef);
        bindings[activator] = adapted as VoidCallback;
      }
    }

    return CallbackShortcuts(
      key: runtime.decodeKey(data),
      bindings: bindings,
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

/// Decode a ShortcutActivator from wire data.
ShortcutActivator? _decodeActivator(
  FlutRuntime runtime,
  Map<String, dynamic> data,
) {
  final type = data['_flut_type'] as String?;
  switch (type) {
    case 'SingleActivator':
      return FlutSingleActivator.flutDecode(runtime, data);
    case 'CharacterActivator':
      return FlutCharacterActivator.flutDecode(runtime, data);
    default:
      return null;
  }
}
