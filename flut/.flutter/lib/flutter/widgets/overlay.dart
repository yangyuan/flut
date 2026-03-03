import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutOverlay {
  FlutOverlay._();

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('Overlay.of', _of);
  }

  static dynamic _of(
    FlutRuntime runtime,
    BuildContext context, [
    bool rootOverlay = false,
  ]) {
    return Overlay.of(context, rootOverlay: rootOverlay);
  }
}

class FlutOverlayState with FlutRealtimeObject<OverlayState> {
  FlutOverlayState.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required OverlayState target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'OverlayState',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('OverlayState', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('OverlayState', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'insert':
        final below = kwargs['below'] as OverlayEntry?;
        final above = kwargs['above'] as OverlayEntry?;
        flutTarget.insert(args[0] as OverlayEntry, below: below, above: above);
        return null;
      case 'insertAll':
        final entries = (args[0] as List).cast<OverlayEntry>();
        final below = kwargs['below'] as OverlayEntry?;
        final above = kwargs['above'] as OverlayEntry?;
        flutTarget.insertAll(entries, below: below, above: above);
        return null;
      case 'rearrange':
        final newEntries = (args[0] as List).cast<OverlayEntry>();
        final below = kwargs['below'] as OverlayEntry?;
        final above = kwargs['above'] as OverlayEntry?;
        flutTarget.rearrange(newEntries, below: below, above: above);
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}

class FlutOverlayEntry with FlutRealtimeObject<OverlayEntry> {
  FlutOverlayEntry.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required OverlayEntry target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  static FlutOverlayEntry flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final builderId = runtime.unpackOptionalField<int>(data, 'builder');
    final entry = OverlayEntry(
      builder: (context) {
        if (builderId == null) return const SizedBox.shrink();
        return runtime.callAction<Widget>(builderId, args: [context]) ??
            const SizedBox.shrink();
      },
      opaque: runtime.unpackRequiredField<bool>(data, 'opaque'),
      maintainState: runtime.unpackRequiredField<bool>(data, 'maintainState'),
      canSizeOverlay: runtime.unpackRequiredField<bool>(data, 'canSizeOverlay'),
    );
    return FlutOverlayEntry.createFromData(
      runtime: runtime,
      data: data,
      target: entry,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'mounted':
        return flutTarget.mounted;
    }
    throw FlutUnknownPropertyException('OverlayEntry', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('OverlayEntry', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'remove':
        flutTarget.remove();
        return null;
      case 'markNeedsBuild':
        flutTarget.markNeedsBuild();
        return null;
      case 'dispose':
        flutTarget.dispose();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
