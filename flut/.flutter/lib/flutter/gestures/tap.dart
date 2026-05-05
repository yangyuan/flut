import 'package:flut/flut/error.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flut/runtime.dart';

class FlutTapDownDetails extends FlutValueObject {
  final TapDownDetails details;

  const FlutTapDownDetails(this.details) : super('TapDownDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    if (details.kind != null) {
      result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind!);
    }
    return result;
  }
}

class FlutTapUpDetails extends FlutValueObject {
  final TapUpDetails details;

  const FlutTapUpDetails(this.details) : super('TapUpDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind);
    return result;
  }
}

class FlutTapMoveDetails extends FlutValueObject {
  final TapMoveDetails details;

  const FlutTapMoveDetails(this.details) : super('TapMoveDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['kind'] = const FlutPointerDeviceKind().flutEncode(details.kind);
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['delta'] = FlutOffset(details.delta).flutEncode();
    return result;
  }

  static TapMoveDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TapMoveDetails(
      kind: runtime.unpackRequiredField<PointerDeviceKind>(data, 'kind'),
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      localPosition: runtime.unpackOptionalField<Offset>(data, 'localPosition'),
      delta: runtime.unpackRequiredField<Offset>(data, 'delta'),
    );
  }
}

class FlutTapGestureRecognizer with FlutRealtimeObject<TapGestureRecognizer> {
  FlutTapGestureRecognizer.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required TapGestureRecognizer target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutTapGestureRecognizer.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required TapGestureRecognizer target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'TapGestureRecognizer',
      target: target,
    );
  }

  static FlutTapGestureRecognizer flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final TapGestureRecognizer target = TapGestureRecognizer(
      debugOwner: runtime.unpackOptionalField<Object>(data, 'debugOwner'),
      supportedDevices: runtime.unpackOptionalField<Set<PointerDeviceKind>>(
        data,
        'supportedDevices',
      ),
      allowedButtonsFilter: runtime.unpackRequiredCallback(
        data,
        'allowedButtonsFilter',
      ),
      preAcceptSlopTolerance: runtime.unpackOptionalField<double>(
        data,
        'preAcceptSlopTolerance',
      ),
      postAcceptSlopTolerance: runtime.unpackOptionalField<double>(
        data,
        'postAcceptSlopTolerance',
      ),
    );
    return FlutTapGestureRecognizer.createFromData(
      runtime: runtime,
      data: data,
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'onTapDown':
        return flutTarget.onTapDown;
      case 'onTapUp':
        return flutTarget.onTapUp;
      case 'onTap':
        return flutTarget.onTap;
      case 'onTapMove':
        return flutTarget.onTapMove;
      case 'onTapCancel':
        return flutTarget.onTapCancel;
      case 'onSecondaryTap':
        return flutTarget.onSecondaryTap;
      case 'onSecondaryTapDown':
        return flutTarget.onSecondaryTapDown;
      case 'onSecondaryTapUp':
        return flutTarget.onSecondaryTapUp;
      case 'onSecondaryTapCancel':
        return flutTarget.onSecondaryTapCancel;
      case 'onTertiaryTapDown':
        return flutTarget.onTertiaryTapDown;
      case 'onTertiaryTapUp':
        return flutTarget.onTertiaryTapUp;
      case 'onTertiaryTapCancel':
        return flutTarget.onTertiaryTapCancel;
      case 'debugOwner':
        return flutTarget.debugOwner;
      case 'supportedDevices':
        return flutTarget.supportedDevices;
      case 'allowedButtonsFilter':
        return flutTarget.allowedButtonsFilter;
      case 'preAcceptSlopTolerance':
        return flutTarget.preAcceptSlopTolerance;
      case 'postAcceptSlopTolerance':
        return flutTarget.postAcceptSlopTolerance;
    }
    throw FlutUnknownPropertyException('TapGestureRecognizer', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onTapDown':
        flutTarget.onTapDown = value as GestureTapDownCallback?;
        return true;
      case 'onTapUp':
        flutTarget.onTapUp = value as GestureTapUpCallback?;
        return true;
      case 'onTap':
        flutTarget.onTap = value as GestureTapCallback?;
        return true;
      case 'onTapMove':
        flutTarget.onTapMove = value as GestureTapMoveCallback?;
        return true;
      case 'onTapCancel':
        flutTarget.onTapCancel = value as GestureTapCancelCallback?;
        return true;
      case 'onSecondaryTap':
        flutTarget.onSecondaryTap = value as GestureTapCallback?;
        return true;
      case 'onSecondaryTapDown':
        flutTarget.onSecondaryTapDown = value as GestureTapDownCallback?;
        return true;
      case 'onSecondaryTapUp':
        flutTarget.onSecondaryTapUp = value as GestureTapUpCallback?;
        return true;
      case 'onSecondaryTapCancel':
        flutTarget.onSecondaryTapCancel = value as GestureTapCancelCallback?;
        return true;
      case 'onTertiaryTapDown':
        flutTarget.onTertiaryTapDown = value as GestureTapDownCallback?;
        return true;
      case 'onTertiaryTapUp':
        flutTarget.onTertiaryTapUp = value as GestureTapUpCallback?;
        return true;
      case 'onTertiaryTapCancel':
        flutTarget.onTertiaryTapCancel = value as GestureTapCancelCallback?;
        return true;
    }
    throw FlutUnknownPropertyException('TapGestureRecognizer', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'dispose':
        flutTarget.dispose();
        flutDispose();
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
