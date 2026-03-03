import 'package:flut/flut/runtime.dart';
import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutScrollPosition with FlutRealtimeObject<ScrollPosition> {
  FlutScrollPosition.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required ScrollPosition target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'ScrollPosition',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'pixels':
        return flutTarget.pixels;
      case 'minScrollExtent':
        return flutTarget.minScrollExtent;
      case 'maxScrollExtent':
        return flutTarget.maxScrollExtent;
      case 'viewportDimension':
        return flutTarget.viewportDimension;
      case 'hasContentDimensions':
        return flutTarget.hasContentDimensions;
      case 'hasPixels':
        return flutTarget.hasPixels;
      case 'atEdge':
        return flutTarget.atEdge;
    }
    throw FlutUnknownPropertyException('ScrollPosition', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('ScrollPosition', property);
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
    throw FlutUnknownMethodException(method);
  }
}
