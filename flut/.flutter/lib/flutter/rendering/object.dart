import 'package:flutter/rendering.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutRenderObject with FlutRealtimeObject<RenderObject> {
  FlutRenderObject.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required RenderObject target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'RenderObject',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'attached':
        return flutTarget.attached;
      case 'parent':
        return flutTarget.parent;
      case 'paintBounds':
        return flutTarget.paintBounds;
    }
    throw FlutUnknownPropertyException('RenderObject', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('RenderObject', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    throw FlutUnknownMethodException(method);
  }
}
