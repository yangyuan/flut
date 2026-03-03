import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flutter/painting/borders.dart';
import 'package:flut/flutter/painting/border_radius.dart';

class FlutRoundedRectangleBorder extends FlutValueObject {
  final RoundedRectangleBorder value;
  const FlutRoundedRectangleBorder(this.value)
    : super('RoundedRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadius(
      value.borderRadius as BorderRadius,
    ).flutEncode();
    return result;
  }

  static RoundedRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return RoundedRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadius>(
        data,
        'borderRadius',
      ),
    );
  }
}

class FlutCircleBorder extends FlutValueObject {
  final CircleBorder value;
  const FlutCircleBorder(this.value) : super('CircleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['eccentricity'] = value.eccentricity;
    return result;
  }

  static CircleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CircleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      eccentricity: runtime.unpackRequiredField<double>(data, 'eccentricity'),
    );
  }
}

class FlutStadiumBorder extends FlutValueObject {
  final StadiumBorder value;
  const FlutStadiumBorder(this.value) : super('StadiumBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    return result;
  }

  static StadiumBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return StadiumBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
    );
  }
}

class FlutBeveledRectangleBorder extends FlutValueObject {
  final BeveledRectangleBorder value;
  const FlutBeveledRectangleBorder(this.value)
    : super('BeveledRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadius(
      value.borderRadius as BorderRadius,
    ).flutEncode();
    return result;
  }

  static BeveledRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BeveledRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadius>(
        data,
        'borderRadius',
      ),
    );
  }
}

class FlutContinuousRectangleBorder extends FlutValueObject {
  final ContinuousRectangleBorder value;
  const FlutContinuousRectangleBorder(this.value)
    : super('ContinuousRectangleBorder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['side'] = FlutBorderSide(value.side).flutEncode();
    result['borderRadius'] = FlutBorderRadius(
      value.borderRadius as BorderRadius,
    ).flutEncode();
    return result;
  }

  static ContinuousRectangleBorder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ContinuousRectangleBorder(
      side: runtime.unpackRequiredField<BorderSide>(data, 'side'),
      borderRadius: runtime.unpackRequiredField<BorderRadius>(
        data,
        'borderRadius',
      ),
    );
  }
}
