import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';

class FlutScrollController extends FlutChangeNotifier<ScrollController> {
  FlutScrollController.createFromData({
    required super.runtime,
    required super.data,
    required super.target,
  }) : super.createFromData();

  FlutScrollController.createFromObject({
    required super.runtime,
    required super.oid,
    required super.target,
  }) : super.createFromObject(type: 'ScrollController');

  static FlutScrollController flutCreate(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutScrollController.createFromData(
      runtime: runtime,
      data: data,
      target: ScrollController(
        initialScrollOffset: runtime.unpackRequiredField<double>(
          data,
          'initialScrollOffset',
        ),
      ),
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'offset':
        return flutTarget.offset;
      case 'hasClients':
        return flutTarget.hasClients;
      case 'position':
        return flutTarget.position;
    }
    return super.getRawProperty(property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'jumpTo':
        flutTarget.jumpTo((args[0] as num).toDouble());
        return null;
      case 'animateTo':
        flutTarget.animateTo(
          (args[0] as num).toDouble(),
          duration: runtime.decodeObject<Duration>(kwargs['duration'])!,
          curve: runtime.decodeObject<Curve>(kwargs['curve'])!,
        );
        return null;
    }
    return super.callMethod(method, args, kwargs);
  }
}
