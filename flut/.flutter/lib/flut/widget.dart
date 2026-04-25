import 'package:flutter/material.dart';
import 'package:flut/flut/native.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

final _pidFinalizer = Finalizer<List<dynamic>>((token) {
  try {
    final native = token[0] as FlutNative;
    final pid = token[1] as int;
    native.invokeNativeAsync('release_packing', {'pid': pid});
  } catch (_) {}
});

@immutable
class _FlutClassKey extends LocalKey {
  const _FlutClassKey(this.className, this.originalKey);

  final String className;
  final Key? originalKey;

  @override
  bool operator ==(Object other) {
    return other is _FlutClassKey &&
        other.className == className &&
        other.originalKey == originalKey;
  }

  @override
  int get hashCode => Object.hash(className, originalKey);

  @override
  String toString() =>
      '_FlutClassKey($className${originalKey == null ? '' : ', $originalKey'})';
}

Key _innerHostKey(String className, Key? userKey) {
  if (userKey is GlobalKey) return userKey;
  return _FlutClassKey(className, userKey);
}

class FlutStatefulWidget extends StatelessWidget {
  final int flutPid;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;
  final Key? userKey;

  FlutStatefulWidget({
    required this.flutPid,
    required this.className,
    required this.native,
    required this.runtime,
    Key? key,
  }) : userKey = key,
       super(key: key is GlobalKey ? null : key) {
    _pidFinalizer.attach(this, [native, flutPid]);
  }

  @override
  Widget build(BuildContext context) {
    return _FlutStatefulHost(
      key: _innerHostKey(className, userKey),
      flutPid: flutPid,
      className: className,
      native: native,
      runtime: runtime,
    );
  }
}

class _FlutStatefulHost extends StatefulWidget {
  final int flutPid;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;

  const _FlutStatefulHost({
    required this.flutPid,
    required this.className,
    required this.native,
    required this.runtime,
    super.key,
  });

  @override
  State<_FlutStatefulHost> createState() => _FlutStatefulHostState();
}

class _FlutStatefulHostState extends State<_FlutStatefulHost>
    with
        FlutRealtimeObject<State<_FlutStatefulHost>>,
        TickerProviderStateMixin,
        AutomaticKeepAliveClientMixin {
  int? _buildActionId;
  late int _lastProcessedPid;
  bool _wantKeepAlive = false;
  bool _keepAliveMixinActive = false;

  @override
  bool get wantKeepAlive => _wantKeepAlive;

  @override
  void initState() {
    super.initState();
    _lastProcessedPid = widget.flutPid;
    final oid = widget.runtime.generateOid();
    initRealtimeFromObject(
      runtime: widget.runtime,
      oid: oid,
      type: 'State',
      target: this,
    );
    widget.runtime.objectRegistry[oid] = this;
  }

  @override
  void dispose() {
    _buildActionId = null;
    if (widget.runtime.objectRegistry.containsKey(flutOid)) {
      flutDispose();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_keepAliveMixinActive) {
      super.build(context);
    }
    try {
      if (_buildActionId == null) {
        final payload = <String, dynamic>{
          'args': [flutOid, widget.runtime.encodeValue(context)],
        };
        final rawResult = widget.runtime.invokeAction(
          widget.flutPid,
          payload: payload,
        );

        if (rawResult == null) {
          debugPrint(
            '[Flut] StatefulWidget init returned null for pid=${widget.flutPid} class=${widget.className}',
          );
          return ErrorWidget.withDetails(
            message: 'init callback returned null',
          );
        }
        if (rawResult['_flut_error'] != null) {
          debugPrint(
            '[Flut] StatefulWidget init error for pid=${widget.flutPid} class=${widget.className}: ${rawResult['_flut_error']}',
          );
          return ErrorWidget.withDetails(
            message: rawResult['_flut_error'].toString(),
          );
        }

        final initResult = rawResult['_flut_result'];
        if (initResult == null || initResult is! Map<String, dynamic>) {
          debugPrint(
            '[Flut] StatefulWidget init result invalid for pid=${widget.flutPid} class=${widget.className}: $initResult',
          );
          return ErrorWidget.withDetails(
            message: 'init callback returned invalid result',
          );
        }

        _buildActionId = initResult['build_action'] as int?;
        final subtree = initResult['subtree'];

        final mixins = initResult['_flut_mixins'] as List<dynamic>?;
        if (mixins != null) {
          if (mixins.contains('AutomaticKeepAliveClientMixin')) {
            _keepAliveMixinActive = true;
            _wantKeepAlive = true;
            updateKeepAlive();
          }
        }

        if (subtree == null) {
          debugPrint(
            '[Flut] StatefulWidget init build returned null subtree for pid=${widget.flutPid} class=${widget.className}',
          );
          return ErrorWidget.withDetails(message: 'init build returned null');
        }

        if (subtree is Map<String, dynamic>) {
          return widget.runtime.buildWidgetFromJson(subtree);
        }
        if (subtree is Widget) return subtree;
        debugPrint(
          '[Flut] StatefulWidget init unexpected subtree type ${subtree.runtimeType} for pid=${widget.flutPid} class=${widget.className}',
        );
        return ErrorWidget.withDetails(message: 'Unexpected subtree type');
      }

      final payload = <String, dynamic>{
        'args': [widget.runtime.encodeValue(context)],
      };
      if (widget.flutPid != _lastProcessedPid) {
        payload['kwargs'] = {'new_pid': widget.flutPid};
        _lastProcessedPid = widget.flutPid;
      }

      final rawResult = widget.runtime.invokeAction(
        _buildActionId!,
        payload: payload,
      );

      if (rawResult == null) {
        debugPrint(
          '[Flut] StatefulWidget build returned null for oid=$flutOid class=${widget.className}',
        );
        return ErrorWidget.withDetails(message: 'build returned null');
      }
      if (rawResult['_flut_error'] != null) {
        debugPrint(
          '[Flut] StatefulWidget build error for oid=$flutOid class=${widget.className}: ${rawResult['_flut_error']}',
        );
        return ErrorWidget.withDetails(
          message: rawResult['_flut_error'].toString(),
        );
      }

      final subtree = rawResult['_flut_result'];

      if (subtree == null) {
        debugPrint(
          '[Flut] StatefulWidget build returned null subtree for oid=$flutOid class=${widget.className}',
        );
        return ErrorWidget.withDetails(message: 'build returned null subtree');
      }

      if (subtree is Map<String, dynamic>) {
        return widget.runtime.buildWidgetFromJson(subtree);
      }
      if (subtree is Widget) return subtree;
      debugPrint(
        '[Flut] StatefulWidget build unexpected subtree type ${subtree.runtimeType} for oid=$flutOid class=${widget.className}',
      );
      return ErrorWidget.withDetails(message: 'Unexpected subtree type');
    } catch (e, st) {
      debugPrint(
        '[Flut] StatefulWidget exception for pid=${widget.flutPid} class=${widget.className}: $e',
      );
      debugPrint(st.toString());
      return ErrorWidget.withDetails(message: e.toString());
    }
  }

  @override
  dynamic getRawProperty(String property) {
    return null;
  }

  @override
  Map<String, dynamic> flutEncode() {
    return {'_flut_type': 'BuildContext', '_flut_oid': flutOid};
  }

  @override
  bool setProperty(String property, dynamic value) {
    return false;
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    if (method == 'setState') {
      setState(() {});
      return null;
    }
    if (method == 'updateKeepAlive') {
      _wantKeepAlive = args[0] as bool;
      updateKeepAlive();
      return null;
    }
    return null;
  }
}

class FlutStatelessWidget extends StatelessWidget {
  final int flutPid;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;
  final Key? userKey;

  FlutStatelessWidget({
    required this.flutPid,
    required this.className,
    required this.native,
    required this.runtime,
    Key? key,
  }) : userKey = key,
       super(key: key is GlobalKey ? null : key) {
    _pidFinalizer.attach(this, [native, flutPid]);
  }

  @override
  Widget build(BuildContext context) {
    return _FlutStatelessHost(
      key: _innerHostKey(className, userKey),
      flutPid: flutPid,
      className: className,
      native: native,
      runtime: runtime,
    );
  }
}

class _FlutStatelessHost extends StatelessWidget {
  final int flutPid;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;

  const _FlutStatelessHost({
    required this.flutPid,
    required this.className,
    required this.native,
    required this.runtime,
    super.key,
  });

  @override
  StatelessElement createElement() => _FlutStatelessHostElement(this);

  @override
  Widget build(BuildContext context) {
    throw StateError('_FlutStatelessHost.build should not be called directly.');
  }
}

class _FlutStatelessHostElement extends StatelessElement
    with FlutRealtimeObject<StatelessElement> {
  int? _buildActionId;
  late int _lastProcessedPid;

  _FlutStatelessHostElement(_FlutStatelessHost super.widget);

  _FlutStatelessHost get _flutWidget => widget as _FlutStatelessHost;

  @override
  void mount(Element? parent, Object? newSlot) {
    _lastProcessedPid = _flutWidget.flutPid;
    final oid = _flutWidget.runtime.generateOid();
    initRealtimeFromObject(
      runtime: _flutWidget.runtime,
      oid: oid,
      type: 'StatelessElement',
      target: this,
    );
    _flutWidget.runtime.objectRegistry[oid] = this;
    super.mount(parent, newSlot);
  }

  @override
  void unmount() {
    _buildActionId = null;
    if (_flutWidget.runtime.objectRegistry.containsKey(flutOid)) {
      flutDispose();
    }
    super.unmount();
  }

  @override
  Widget build() {
    try {
      if (_buildActionId == null) {
        final payload = <String, dynamic>{
          'args': [flutOid, _flutWidget.runtime.encodeValue(this)],
        };
        final rawResult = _flutWidget.runtime.invokeAction(
          _flutWidget.flutPid,
          payload: payload,
        );

        if (rawResult == null) {
          debugPrint(
            '[Flut] StatelessWidget init returned null for pid=${_flutWidget.flutPid} class=${_flutWidget.className}',
          );
          return ErrorWidget.withDetails(
            message: 'init callback returned null',
          );
        }
        if (rawResult['_flut_error'] != null) {
          debugPrint(
            '[Flut] StatelessWidget init error for pid=${_flutWidget.flutPid} class=${_flutWidget.className}: ${rawResult['_flut_error']}',
          );
          return ErrorWidget.withDetails(
            message: rawResult['_flut_error'].toString(),
          );
        }

        final initResult = rawResult['_flut_result'];
        if (initResult == null || initResult is! Map<String, dynamic>) {
          debugPrint(
            '[Flut] StatelessWidget init result invalid for pid=${_flutWidget.flutPid} class=${_flutWidget.className}: $initResult',
          );
          return ErrorWidget.withDetails(
            message: 'init callback returned invalid result',
          );
        }

        _buildActionId = initResult['build_action'] as int?;
        final subtree = initResult['subtree'];

        if (subtree == null) {
          debugPrint(
            '[Flut] StatelessWidget init build returned null subtree for pid=${_flutWidget.flutPid} class=${_flutWidget.className}',
          );
          return ErrorWidget.withDetails(message: 'init build returned null');
        }

        if (subtree is Map<String, dynamic>) {
          return _flutWidget.runtime.buildWidgetFromJson(subtree);
        }
        if (subtree is Widget) return subtree;
        debugPrint(
          '[Flut] StatelessWidget init unexpected subtree type ${subtree.runtimeType} for pid=${_flutWidget.flutPid} class=${_flutWidget.className}',
        );
        return ErrorWidget.withDetails(message: 'Unexpected subtree type');
      }

      final payload = <String, dynamic>{
        'args': [_flutWidget.runtime.encodeValue(this)],
      };
      if (_flutWidget.flutPid != _lastProcessedPid) {
        payload['kwargs'] = {'new_pid': _flutWidget.flutPid};
        _lastProcessedPid = _flutWidget.flutPid;
      }

      final rawResult = _flutWidget.runtime.invokeAction(
        _buildActionId!,
        payload: payload,
      );

      if (rawResult == null) {
        debugPrint(
          '[Flut] StatelessWidget build returned null for oid=$flutOid class=${_flutWidget.className}',
        );
        return ErrorWidget.withDetails(message: 'build returned null');
      }
      if (rawResult['_flut_error'] != null) {
        debugPrint(
          '[Flut] StatelessWidget build error for oid=$flutOid class=${_flutWidget.className}: ${rawResult['_flut_error']}',
        );
        return ErrorWidget.withDetails(
          message: rawResult['_flut_error'].toString(),
        );
      }

      final subtree = rawResult['_flut_result'];

      if (subtree == null) {
        debugPrint(
          '[Flut] StatelessWidget build returned null subtree for oid=$flutOid class=${_flutWidget.className}',
        );
        return ErrorWidget.withDetails(message: 'build returned null subtree');
      }

      if (subtree is Map<String, dynamic>) {
        return _flutWidget.runtime.buildWidgetFromJson(subtree);
      }
      if (subtree is Widget) return subtree;
      debugPrint(
        '[Flut] StatelessWidget build unexpected subtree type ${subtree.runtimeType} for oid=$flutOid class=${_flutWidget.className}',
      );
      return ErrorWidget.withDetails(message: 'Unexpected subtree type');
    } catch (e, st) {
      debugPrint(
        '[Flut] StatelessWidget exception for pid=${_flutWidget.flutPid} class=${_flutWidget.className}: $e',
      );
      debugPrint(st.toString());
      return ErrorWidget.withDetails(message: e.toString());
    }
  }

  @override
  dynamic getRawProperty(String property) {
    return null;
  }

  @override
  Map<String, dynamic> flutEncode() {
    return {'_flut_type': 'BuildContext', '_flut_oid': flutOid};
  }

  @override
  bool setProperty(String property, dynamic value) {
    return false;
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    if (method == 'setState') {
      markNeedsBuild();
      return null;
    }
    return null;
  }
}

class _FlutInheritedScopeMarker extends InheritedWidget {
  final String scopeName;
  final int version;

  const _FlutInheritedScopeMarker({
    required this.scopeName,
    required this.version,
    required super.child,
  });

  @override
  bool updateShouldNotify(covariant _FlutInheritedScopeMarker oldWidget) {
    return version != oldWidget.version;
  }
}

class FlutInheritedScopeWidget extends StatelessWidget {
  final int flutPid;
  final String scopeName;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;
  final Key? userKey;

  FlutInheritedScopeWidget({
    required this.flutPid,
    required this.scopeName,
    required this.className,
    required this.native,
    required this.runtime,
    Key? key,
  }) : userKey = key,
       super(key: key is GlobalKey ? null : key) {
    _pidFinalizer.attach(this, [native, flutPid]);
  }

  @override
  Widget build(BuildContext context) {
    return _FlutInheritedScopeHost(
      key: _innerHostKey(className, userKey),
      flutPid: flutPid,
      scopeName: scopeName,
      className: className,
      native: native,
      runtime: runtime,
    );
  }
}

class _FlutInheritedScopeHost extends StatefulWidget {
  final int flutPid;
  final String scopeName;
  final String className;
  final FlutNative native;
  final FlutRuntime runtime;

  const _FlutInheritedScopeHost({
    required this.flutPid,
    required this.scopeName,
    required this.className,
    required this.native,
    required this.runtime,
    super.key,
  });

  @override
  State<_FlutInheritedScopeHost> createState() => _FlutInheritedScopeState();
}

class _FlutInheritedScopeState extends State<_FlutInheritedScopeHost>
    with FlutRealtimeObject<State<_FlutInheritedScopeHost>> {
  int? _buildActionId;
  late int _lastProcessedPid;
  int _version = 0;

  @override
  void initState() {
    super.initState();
    _lastProcessedPid = widget.flutPid;
    final oid = widget.runtime.generateOid();
    initRealtimeFromObject(
      runtime: widget.runtime,
      oid: oid,
      type: 'InheritedScopeState',
      target: this,
    );
    widget.runtime.objectRegistry[oid] = this;
  }

  @override
  void dispose() {
    _buildActionId = null;
    if (widget.runtime.objectRegistry.containsKey(flutOid)) {
      flutDispose();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    try {
      if (_buildActionId == null) {
        final payload = <String, dynamic>{
          'args': [flutOid, widget.runtime.encodeValue(context)],
        };
        final rawResult = widget.runtime.invokeAction(
          widget.flutPid,
          payload: payload,
        );

        if (rawResult == null || rawResult['_flut_error'] != null) {
          debugPrint(
            '[Flut] InheritedWidget init error for '
            'pid=${widget.flutPid} class=${widget.className}',
          );
          return ErrorWidget.withDetails(
            message:
                rawResult?['_flut_error']?.toString() ?? 'init returned null',
          );
        }

        final initResult = rawResult['_flut_result'];
        if (initResult == null || initResult is! Map<String, dynamic>) {
          return ErrorWidget.withDetails(
            message: 'init callback returned invalid result',
          );
        }

        _buildActionId = initResult['build_action'] as int?;
        final subtree = initResult['subtree'];

        if (subtree == null) {
          return ErrorWidget.withDetails(
            message: 'init build returned null subtree',
          );
        }

        final child = subtree is Map<String, dynamic>
            ? widget.runtime.buildWidgetFromJson(subtree)
            : (subtree is Widget ? subtree : const SizedBox.shrink());

        return _FlutInheritedScopeMarker(
          scopeName: widget.scopeName,
          version: _version,
          child: child,
        );
      }

      final payload = <String, dynamic>{
        'args': [widget.runtime.encodeValue(context)],
      };
      if (widget.flutPid != _lastProcessedPid) {
        payload['kwargs'] = {'new_pid': widget.flutPid};
        _lastProcessedPid = widget.flutPid;
      }

      final rawResult = widget.runtime.invokeAction(
        _buildActionId!,
        payload: payload,
      );

      if (rawResult == null || rawResult['_flut_error'] != null) {
        return ErrorWidget.withDetails(
          message:
              rawResult?['_flut_error']?.toString() ?? 'build returned null',
        );
      }

      final buildResult = rawResult['_flut_result'];
      if (buildResult == null || buildResult is! Map<String, dynamic>) {
        return ErrorWidget.withDetails(
          message: 'build returned invalid result',
        );
      }

      final shouldNotify = buildResult['_flut_should_notify'] as bool? ?? false;
      if (shouldNotify) {
        _version++;
      }

      final subtree = buildResult['subtree'];
      if (subtree == null) {
        return ErrorWidget.withDetails(message: 'build returned null subtree');
      }

      final child = subtree is Map<String, dynamic>
          ? widget.runtime.buildWidgetFromJson(subtree)
          : (subtree is Widget ? subtree : const SizedBox.shrink());

      return _FlutInheritedScopeMarker(
        scopeName: widget.scopeName,
        version: _version,
        child: child,
      );
    } catch (e, st) {
      debugPrint(
        '[Flut] InheritedWidget exception for '
        'pid=${widget.flutPid} class=${widget.className}: $e',
      );
      debugPrint(st.toString());
      return ErrorWidget.withDetails(message: e.toString());
    }
  }

  @override
  dynamic getRawProperty(String property) => null;

  @override
  Map<String, dynamic> flutEncode() {
    return {'_flut_type': 'BuildContext', '_flut_oid': flutOid};
  }

  @override
  bool setProperty(String property, dynamic value) => false;

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    if (method == 'setState') {
      setState(() {});
      return null;
    }
    return null;
  }
}

class FlutInheritedScope {
  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('FlutInheritedScope.of', _of);
  }

  static dynamic _of(
    FlutRuntime runtime,
    BuildContext context,
    String scopeName,
  ) {
    _FlutInheritedScopeMarker? found;
    InheritedElement? foundElement;

    context.visitAncestorElements((element) {
      if (element is InheritedElement &&
          element.widget is _FlutInheritedScopeMarker) {
        final marker = element.widget as _FlutInheritedScopeMarker;
        if (marker.scopeName == scopeName) {
          found = marker;
          foundElement = element;
          return false;
        }
      }
      return true;
    });

    if (found == null || foundElement == null) return null;

    context.dependOnInheritedElement(foundElement!);

    final stateElement = foundElement!
        .findAncestorStateOfType<_FlutInheritedScopeState>();
    if (stateElement == null) return null;

    return stateElement.flutOid;
  }
}
