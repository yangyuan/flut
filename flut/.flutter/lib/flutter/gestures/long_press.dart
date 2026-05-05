import 'package:flut/flut/error.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';
import 'package:flut/flut/runtime.dart';

class FlutLongPressDownDetails extends FlutValueObject {
  final LongPressDownDetails details;

  const FlutLongPressDownDetails(this.details) : super('LongPressDownDetails');

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

  static LongPressDownDetails? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return LongPressDownDetails(
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      localPosition: runtime.unpackOptionalField<Offset>(data, 'localPosition'),
      kind: runtime.unpackOptionalField<PointerDeviceKind>(data, 'kind'),
    );
  }
}

class FlutLongPressStartDetails extends FlutValueObject {
  final LongPressStartDetails details;

  const FlutLongPressStartDetails(this.details)
    : super('LongPressStartDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    return result;
  }
}

class FlutLongPressMoveUpdateDetails extends FlutValueObject {
  final LongPressMoveUpdateDetails details;

  const FlutLongPressMoveUpdateDetails(this.details)
    : super('LongPressMoveUpdateDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['offsetFromOrigin'] = FlutOffset(
      details.offsetFromOrigin,
    ).flutEncode();
    result['localOffsetFromOrigin'] = FlutOffset(
      details.localOffsetFromOrigin,
    ).flutEncode();
    return result;
  }
}

class FlutLongPressEndDetails extends FlutValueObject {
  final LongPressEndDetails details;

  const FlutLongPressEndDetails(this.details) : super('LongPressEndDetails');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(details.globalPosition).flutEncode();
    result['localPosition'] = FlutOffset(details.localPosition).flutEncode();
    result['velocity'] = FlutVelocity(details.velocity).flutEncode();
    return result;
  }
}

class FlutLongPressGestureRecognizer
    with FlutRealtimeObject<LongPressGestureRecognizer> {
  FlutLongPressGestureRecognizer.createFromData({
    required FlutRuntime runtime,
    required Map<String, dynamic> data,
    required LongPressGestureRecognizer target,
  }) {
    initRealtimeFromData(runtime: runtime, data: data, target: target);
  }

  FlutLongPressGestureRecognizer.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required LongPressGestureRecognizer target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'LongPressGestureRecognizer',
      target: target,
    );
  }

  static FlutLongPressGestureRecognizer flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final allowedButtonsFilter = runtime.unpackOptionalCallback(
      data,
      'allowedButtonsFilter',
    );
    final LongPressGestureRecognizer target = allowedButtonsFilter != null
        ? LongPressGestureRecognizer(
            duration: runtime.unpackOptionalField<Duration>(data, 'duration'),
            debugOwner: runtime.unpackOptionalField<Object>(data, 'debugOwner'),
            supportedDevices: runtime
                .unpackOptionalField<Set<PointerDeviceKind>>(
                  data,
                  'supportedDevices',
                ),
            allowedButtonsFilter: allowedButtonsFilter,
            postAcceptSlopTolerance: runtime.unpackOptionalField<double>(
              data,
              'postAcceptSlopTolerance',
            ),
          )
        : LongPressGestureRecognizer(
            duration: runtime.unpackOptionalField<Duration>(data, 'duration'),
            debugOwner: runtime.unpackOptionalField<Object>(data, 'debugOwner'),
            supportedDevices: runtime
                .unpackOptionalField<Set<PointerDeviceKind>>(
                  data,
                  'supportedDevices',
                ),
            postAcceptSlopTolerance: runtime.unpackOptionalField<double>(
              data,
              'postAcceptSlopTolerance',
            ),
          );
    return FlutLongPressGestureRecognizer.createFromData(
      runtime: runtime,
      data: data,
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'onLongPressDown':
        return flutTarget.onLongPressDown;
      case 'onLongPressCancel':
        return flutTarget.onLongPressCancel;
      case 'onLongPress':
        return flutTarget.onLongPress;
      case 'onLongPressStart':
        return flutTarget.onLongPressStart;
      case 'onLongPressMoveUpdate':
        return flutTarget.onLongPressMoveUpdate;
      case 'onLongPressUp':
        return flutTarget.onLongPressUp;
      case 'onLongPressEnd':
        return flutTarget.onLongPressEnd;
      case 'onSecondaryLongPressDown':
        return flutTarget.onSecondaryLongPressDown;
      case 'onSecondaryLongPressCancel':
        return flutTarget.onSecondaryLongPressCancel;
      case 'onSecondaryLongPress':
        return flutTarget.onSecondaryLongPress;
      case 'onSecondaryLongPressStart':
        return flutTarget.onSecondaryLongPressStart;
      case 'onSecondaryLongPressMoveUpdate':
        return flutTarget.onSecondaryLongPressMoveUpdate;
      case 'onSecondaryLongPressUp':
        return flutTarget.onSecondaryLongPressUp;
      case 'onSecondaryLongPressEnd':
        return flutTarget.onSecondaryLongPressEnd;
      case 'onTertiaryLongPressDown':
        return flutTarget.onTertiaryLongPressDown;
      case 'onTertiaryLongPressCancel':
        return flutTarget.onTertiaryLongPressCancel;
      case 'onTertiaryLongPress':
        return flutTarget.onTertiaryLongPress;
      case 'onTertiaryLongPressStart':
        return flutTarget.onTertiaryLongPressStart;
      case 'onTertiaryLongPressMoveUpdate':
        return flutTarget.onTertiaryLongPressMoveUpdate;
      case 'onTertiaryLongPressUp':
        return flutTarget.onTertiaryLongPressUp;
      case 'onTertiaryLongPressEnd':
        return flutTarget.onTertiaryLongPressEnd;
      case 'debugOwner':
        return flutTarget.debugOwner;
      case 'supportedDevices':
        return flutTarget.supportedDevices;
      case 'allowedButtonsFilter':
        return flutTarget.allowedButtonsFilter;
      case 'postAcceptSlopTolerance':
        return flutTarget.postAcceptSlopTolerance;
    }
    throw FlutUnknownPropertyException('LongPressGestureRecognizer', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    switch (property) {
      case 'onLongPressDown':
        flutTarget.onLongPressDown = value as GestureLongPressDownCallback?;
        return true;
      case 'onLongPressCancel':
        flutTarget.onLongPressCancel = value as GestureLongPressCancelCallback?;
        return true;
      case 'onLongPress':
        flutTarget.onLongPress = value as GestureLongPressCallback?;
        return true;
      case 'onLongPressStart':
        flutTarget.onLongPressStart = value as GestureLongPressStartCallback?;
        return true;
      case 'onLongPressMoveUpdate':
        flutTarget.onLongPressMoveUpdate =
            value as GestureLongPressMoveUpdateCallback?;
        return true;
      case 'onLongPressUp':
        flutTarget.onLongPressUp = value as GestureLongPressUpCallback?;
        return true;
      case 'onLongPressEnd':
        flutTarget.onLongPressEnd = value as GestureLongPressEndCallback?;
        return true;
      case 'onSecondaryLongPressDown':
        flutTarget.onSecondaryLongPressDown =
            value as GestureLongPressDownCallback?;
        return true;
      case 'onSecondaryLongPressCancel':
        flutTarget.onSecondaryLongPressCancel =
            value as GestureLongPressCancelCallback?;
        return true;
      case 'onSecondaryLongPress':
        flutTarget.onSecondaryLongPress = value as GestureLongPressCallback?;
        return true;
      case 'onSecondaryLongPressStart':
        flutTarget.onSecondaryLongPressStart =
            value as GestureLongPressStartCallback?;
        return true;
      case 'onSecondaryLongPressMoveUpdate':
        flutTarget.onSecondaryLongPressMoveUpdate =
            value as GestureLongPressMoveUpdateCallback?;
        return true;
      case 'onSecondaryLongPressUp':
        flutTarget.onSecondaryLongPressUp =
            value as GestureLongPressUpCallback?;
        return true;
      case 'onSecondaryLongPressEnd':
        flutTarget.onSecondaryLongPressEnd =
            value as GestureLongPressEndCallback?;
        return true;
      case 'onTertiaryLongPressDown':
        flutTarget.onTertiaryLongPressDown =
            value as GestureLongPressDownCallback?;
        return true;
      case 'onTertiaryLongPressCancel':
        flutTarget.onTertiaryLongPressCancel =
            value as GestureLongPressCancelCallback?;
        return true;
      case 'onTertiaryLongPress':
        flutTarget.onTertiaryLongPress = value as GestureLongPressCallback?;
        return true;
      case 'onTertiaryLongPressStart':
        flutTarget.onTertiaryLongPressStart =
            value as GestureLongPressStartCallback?;
        return true;
      case 'onTertiaryLongPressMoveUpdate':
        flutTarget.onTertiaryLongPressMoveUpdate =
            value as GestureLongPressMoveUpdateCallback?;
        return true;
      case 'onTertiaryLongPressUp':
        flutTarget.onTertiaryLongPressUp = value as GestureLongPressUpCallback?;
        return true;
      case 'onTertiaryLongPressEnd':
        flutTarget.onTertiaryLongPressEnd =
            value as GestureLongPressEndCallback?;
        return true;
    }
    throw FlutUnknownPropertyException('LongPressGestureRecognizer', property);
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
