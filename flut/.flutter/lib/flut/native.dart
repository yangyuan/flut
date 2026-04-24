import 'dart:async';
import 'dart:convert';
import 'dart:ffi' as ffi;
import 'package:flutter/material.dart';
import 'package:ffi/ffi.dart';
import 'package:flut/main.dart' show flutRuntime;
import 'package:flut/flut/runtime.dart' show FlutCallableRef;

// When Dart calls Python, used by invokeNativeSync
typedef _NativePythonFunction = ffi.Pointer<Utf8> Function(ffi.Pointer<Utf8>);

// When Python calls Dart, used for callbacks
typedef _NativePythonToDartFunction =
    ffi.Pointer<Utf8> Function(ffi.Pointer<Utf8>);

// When Python notifies Dart of set state
typedef _NativeSetStateFunction = ffi.Void Function(ffi.Pointer<Utf8>);

// DartApi DL table structs for walking NativeApi.initializeApiDLData
final class _DartApiEntry extends ffi.Struct {
  external ffi.Pointer<ffi.Char> name;
  external ffi.Pointer<ffi.Void> function;
}

final class _DartApi extends ffi.Struct {
  @ffi.Int32()
  external int major;
  @ffi.Int32()
  external int minor;
  external ffi.Pointer<_DartApiEntry> functions;
}

abstract class FlutNative {
  dynamic invokeNativeSync(String type, Map<String, dynamic> data);
  Future<dynamic> invokeNativeAsync(String type, Map<String, dynamic> data);

  void dispose();
}

class FlutFfiNative implements FlutNative {
  static FlutFfiNative? _instance;
  static ffi.Pointer<Utf8>? _orphanResponseBuffer;

  final int nativeCallbackAddr;

  // FFI Resources
  ffi.NativeCallable<_NativePythonToDartFunction>? _dartCallCallable;
  ffi.NativeCallable<_NativeSetStateFunction>? _setStateCallable;
  ffi.Pointer<Utf8>? _callResponseBuffer;
  static int _processedNotifyCount = 0;

  final Completer<void> _userInitDone = Completer<void>();
  Future<void> get userInitDone => _userInitDone.future;

  FlutFfiNative(this.nativeCallbackAddr) {
    if (_instance != null) {
      throw Exception("FlutFfiNative already initialized");
    }
    _instance = this;
  }

  void bootstrap() {
    try {
      _registerDartCallbackWithPython();
    } catch (_) {
      _dartCallCallable?.close();
      _setStateCallable?.close();
      _dartCallCallable = null;
      _setStateCallable = null;
      _instance = null;
      rethrow;
    }
  }

  @override
  void dispose() {
    _dartCallCallable?.close();
    _setStateCallable?.close();
    _dartCallCallable = null;
    _setStateCallable = null;

    _instance = null;
    if (_callResponseBuffer != null) {
      calloc.free(_callResponseBuffer!);
      _callResponseBuffer = null;
    }
    if (_orphanResponseBuffer != null) {
      calloc.free(_orphanResponseBuffer!);
      _orphanResponseBuffer = null;
    }
  }

  // ===========================================================================
  // FFI Invocation
  // ===========================================================================

  @override
  dynamic invokeNativeSync(String type, Map<String, dynamic> data) {
    final req = jsonEncode({
      "type": type,
      "data": data,
      "_ack": _processedNotifyCount,
    });
    final reqPtr = req.toNativeUtf8();

    try {
      final ptr =
          ffi.Pointer<ffi.NativeFunction<_NativePythonFunction>>.fromAddress(
            nativeCallbackAddr,
          );
      final function = ptr.asFunction<_NativePythonFunction>();
      final resPtr = function(reqPtr);

      if (resPtr == ffi.nullptr) return null;

      final resJson = resPtr.toDartString();
      return jsonDecode(resJson);
    } finally {
      calloc.free(reqPtr);
    }
  }

  /// Invoke the native callback asynchronously and return the result.
  /// Dart UI doesn't block, but Python processes on main thread where call_dart works.
  @override
  Future<dynamic> invokeNativeAsync(String type, Map<String, dynamic> data) {
    return Future<dynamic>(() {
      try {
        return invokeNativeSync(type, data);
      } catch (e, st) {
        debugPrint('Error in invokeNativeAsync($type): $e');
        assert(() {
          debugPrint(st.toString());
          return true;
        }());
        rethrow;
      }
    });
  }

  // ===========================================================================
  // Callbacks
  // ===========================================================================

  void _registerDartCallbackWithPython() {
    _dartCallCallable =
        ffi.NativeCallable<_NativePythonToDartFunction>.isolateLocal(
          _handlePythonCallImpl,
        );

    final callCallbackAddr = _dartCallCallable!.nativeFunction.address;
    final callReg = invokeNativeSync('register_dart_callback', {
      'callback_addr': callCallbackAddr,
    });
    if (callReg is! Map || callReg['success'] != true) {
      throw Exception('Failed to register Dart callback with Python');
    }

    _setStateCallable = ffi.NativeCallable<_NativeSetStateFunction>.listener(
      _onSetState,
    );

    final notifyCallbackAddr = _setStateCallable!.nativeFunction.address;
    final notifyReg = invokeNativeSync('register_set_state_callback', {
      'callback_addr': notifyCallbackAddr,
    });
    if (notifyReg is! Map || notifyReg['success'] != true) {
      throw Exception('Failed to register setState callback with Python');
    }

    _registerIsolateFunctions();
  }

  void _registerIsolateFunctions() {
    final apiData = ffi.NativeApi.initializeApiDLData.cast<_DartApi>();
    var entry = apiData.ref.functions;

    int? enterAddr;
    int? exitAddr;
    int? currentAddr;

    while (entry.ref.name != ffi.nullptr) {
      final name = entry.ref.name.cast<Utf8>().toDartString();
      if (name == 'Dart_EnterIsolate') {
        enterAddr = entry.ref.function.address;
      } else if (name == 'Dart_ExitIsolate') {
        exitAddr = entry.ref.function.address;
      } else if (name == 'Dart_CurrentIsolate') {
        currentAddr = entry.ref.function.address;
      }
      if (enterAddr != null && exitAddr != null && currentAddr != null) break;
      entry = ffi.Pointer.fromAddress(
        entry.address + ffi.sizeOf<_DartApiEntry>(),
      );
    }

    if (enterAddr == null || exitAddr == null || currentAddr == null) {
      throw Exception('Could not find isolate functions in DL table');
    }

    final currentIsolateFn =
        ffi.Pointer<
              ffi.NativeFunction<ffi.Pointer<ffi.Void> Function()>
            >.fromAddress(currentAddr)
            .asFunction<ffi.Pointer<ffi.Void> Function()>();
    final isolateHandle = currentIsolateFn();

    final isolateReg = invokeNativeSync('register_isolate_functions', {
      'enter': enterAddr,
      'exit': exitAddr,
      'current': currentAddr,
      'isolate': isolateHandle.address,
    });
    if (isolateReg is! Map || isolateReg['success'] != true) {
      throw Exception('Failed to register isolate functions with Python');
    }
  }

  static ffi.Pointer<Utf8> _handlePythonCallImpl(ffi.Pointer<Utf8> requestPtr) {
    if (_instance == null) {
      if (_orphanResponseBuffer != null) {
        calloc.free(_orphanResponseBuffer!);
      }
      _orphanResponseBuffer = '{"_flut_error": "No bridge active"}'
          .toNativeUtf8();
      return _orphanResponseBuffer!;
    }

    final instance = _instance!;

    try {
      final reqJson = requestPtr.toDartString();
      final request = jsonDecode(reqJson) as Map<String, dynamic>;
      final callType = request['type'] as String?;
      final data = request['data'] as Map<String, dynamic>? ?? {};

      Map<String, dynamic>? response;

      if (callType == 'get') {
        response = _getProperty(instance, data);
      } else if (callType == 'set') {
        response = _setProperty(instance, data);
      } else if (callType == 'call') {
        response = _callMethod(instance, data);
      } else if (callType == 'static') {
        response = _staticCall(instance, data);
      } else if (callType == 'release') {
        response = _releaseObjects(instance, data);
      } else if (callType == 'createObject') {
        final oid = flutRuntime.createObject(data);
        response = {'_flut_oid': oid};
      } else {
        response = {'_flut_error': 'Unknown call type', 'type': callType};
      }

      // Buffer management...
      if (instance._callResponseBuffer != null) {
        calloc.free(instance._callResponseBuffer!);
      }

      final responseJson = jsonEncode(response);
      instance._callResponseBuffer = responseJson.toNativeUtf8();
      return instance._callResponseBuffer!;
    } catch (e) {
      debugPrint('Error handling Python call: $e');
      if (instance._callResponseBuffer != null) {
        calloc.free(instance._callResponseBuffer!);
      }
      instance._callResponseBuffer = '{"_flut_error": "exception"}'
          .toNativeUtf8();
      return instance._callResponseBuffer!;
    }
  }

  static void _onSetState(ffi.Pointer<Utf8> dataPtr) {
    if (_instance == null) return;

    String jsonStr;
    try {
      jsonStr = dataPtr.toDartString();
    } catch (e) {
      debugPrint(
        'Notify buffer freed before Dart read it (keepalive overflow): $e',
      );
      return;
    }
    _processedNotifyCount++;
    if (jsonStr.isEmpty) return;

    try {
      final decoded = jsonDecode(jsonStr);
      if (decoded is Map<String, dynamic>) {
        final type = decoded['_type'] as String?;
        if (type == 'set') {
          _setProperty(_instance!, decoded);
        } else if (type == 'call') {
          _callMethod(_instance!, decoded);
        } else if (type == 'release') {
          _releaseObjects(_instance!, decoded);
        } else if (type == 'lifecycle') {
          final event = decoded['event'] as String?;
          if (event == 'user_init_done' &&
              !_instance!._userInitDone.isCompleted) {
            _instance!._userInitDone.complete();
          }
        }
      }
    } catch (e) {
      debugPrint('Error handling Python notify: $e');
    }
  }

  // ===========================================================================
  // Generic Property Access (by oid)
  // ===========================================================================

  static Map<String, dynamic> _getProperty(
    FlutFfiNative instance,
    Map<String, dynamic> data,
  ) {
    final oid = data['_flut_oid'] as int?;
    final property = data['_flut_property'] as String?;

    if (oid == null || property == null) {
      return {'_flut_error': 'Missing oid or property'};
    }

    final obj = flutRuntime.objectRegistry[oid];
    if (obj == null) {
      return {'_flut_error': 'Object not found', '_flut_oid': oid};
    }

    final value = obj.getProperty(property);
    return {'_flut_value': value};
  }

  static Map<String, dynamic> _setProperty(
    FlutFfiNative instance,
    Map<String, dynamic> data,
  ) {
    final oid = data['_flut_oid'] as int?;
    final property = data['_flut_property'] as String?;
    var value = data['_flut_value'];

    if (oid == null || property == null) {
      return {'_flut_error': 'Missing oid or property'};
    }

    final obj = flutRuntime.objectRegistry[oid];
    if (obj == null) {
      return {'_flut_error': 'Object not found', '_flut_oid': oid};
    }

    if (value is Map<String, dynamic>) {
      if (value['_flut_type'] == 'Callable') {
        final callable = FlutCallableRef.flutDecode(flutRuntime, value);
        if (callable != null) {
          value = flutRuntime.adaptCallableByType(callable);
        }
      } else {
        final argOid = value['_flut_oid'] as int?;
        if (argOid != null) {
          final resolved = flutRuntime.objectRegistry[argOid];
          if (resolved != null) {
            value = resolved.flutTarget;
          }
        } else {
          value = flutRuntime.decodeObject(value);
        }
      }
    }

    if (obj.setProperty(property, value)) {
      return {'success': true};
    }
    return {'_flut_error': 'Unknown property', '_flut_property': property};
  }

  static Map<String, dynamic> _callMethod(
    FlutFfiNative instance,
    Map<String, dynamic> data,
  ) {
    final oid = data['_flut_oid'] as int?;
    final method = data['_flut_method'] as String?;
    final args = data['args'] as List<dynamic>? ?? [];
    final kwargs = data['kwargs'] as Map<String, dynamic>? ?? {};

    if (oid == null || method == null) {
      return {'_flut_error': 'Missing oid or method'};
    }

    final obj = flutRuntime.objectRegistry[oid];
    if (obj == null) {
      return {'_flut_error': 'Object not found', '_flut_oid': oid};
    }

    final resolvedArgs = args.map((arg) {
      if (arg is Map<String, dynamic>) {
        if (arg['_flut_type'] == 'Callable') {
          final callable = FlutCallableRef.flutDecode(flutRuntime, arg);
          if (callable != null) {
            return flutRuntime.adaptCallableByType(callable);
          }
        }
        final argOid = arg['_flut_oid'] as int?;
        if (argOid != null) {
          final resolved = flutRuntime.objectRegistry[argOid];
          if (resolved != null) return resolved.flutTarget;
        }
        return flutRuntime.decodeObject(arg);
      }
      return arg;
    }).toList();

    final resolvedKwargs = kwargs.map((key, value) {
      if (value is Map<String, dynamic>) {
        if (value['_flut_type'] == 'Callable') {
          final callable = FlutCallableRef.flutDecode(flutRuntime, value);
          if (callable != null) {
            return MapEntry(key, flutRuntime.adaptCallableByType(callable));
          }
        }
        final argOid = value['_flut_oid'] as int?;
        if (argOid != null) {
          final resolved = flutRuntime.objectRegistry[argOid];
          if (resolved != null) return MapEntry(key, resolved.flutTarget);
        }
        return MapEntry(key, flutRuntime.decodeObject(value));
      }
      return MapEntry(key, value);
    });

    final result = obj.callMethod(method, resolvedArgs, resolvedKwargs);
    return {'_flut_value': flutRuntime.encodeValue(result)};
  }

  /// Handle static function calls (e.g., Theme.of, MediaQuery.of)
  /// Generic layer - routes to runtime for actual implementation
  static Map<String, dynamic> _staticCall(
    FlutFfiNative instance,
    Map<String, dynamic> data,
  ) {
    final name = data['name'] as String?;
    final args = data['args'] as List<dynamic>? ?? [];
    final kwargs = data['kwargs'] as Map<String, dynamic>?;

    if (name == null) {
      return {'_flut_error': 'Missing function name'};
    }

    return flutRuntime.handleStaticCall(name, args, kwargs);
  }

  static Map<String, dynamic> _releaseObjects(
    FlutFfiNative instance,
    Map<String, dynamic> data,
  ) {
    final oids = data['oids'] as List<dynamic>?;
    if (oids == null) {
      return {'_flut_error': 'Missing oids'};
    }

    int released = 0;
    for (final oid in oids) {
      if (oid is int) {
        final obj = flutRuntime.objectRegistry[oid];
        if (obj != null) {
          flutRuntime.releaseObject(oid);
          released++;
        }
      }
    }
    return {'released': released};
  }
}
