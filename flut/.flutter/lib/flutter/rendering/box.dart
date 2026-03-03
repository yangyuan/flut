import 'package:flutter/rendering.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/error.dart';

class FlutBoxConstraints extends FlutValueObject {
  final BoxConstraints constraints;
  const FlutBoxConstraints(this.constraints) : super('BoxConstraints');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['minWidth'] = FlutDouble.encode(constraints.minWidth);
    result['maxWidth'] = FlutDouble.encode(constraints.maxWidth);
    result['minHeight'] = FlutDouble.encode(constraints.minHeight);
    result['maxHeight'] = FlutDouble.encode(constraints.maxHeight);
    return result;
  }

  static BoxConstraints? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BoxConstraints(
      minWidth: runtime.unpackRequiredField<double>(data, 'minWidth'),
      maxWidth: runtime.unpackRequiredField<double>(data, 'maxWidth'),
      minHeight: runtime.unpackRequiredField<double>(data, 'minHeight'),
      maxHeight: runtime.unpackRequiredField<double>(data, 'maxHeight'),
    );
  }
}

class FlutRenderBox with FlutRealtimeObject<RenderBox> {
  FlutRenderBox.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required RenderBox target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'RenderBox',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    switch (property) {
      case 'size':
        return flutTarget.size;
    }
    throw FlutUnknownPropertyException('RenderBox', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('RenderBox', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'localToGlobal':
        return flutTarget.localToGlobal(args[0]);
      case 'globalToLocal':
        return flutTarget.globalToLocal(args[0]);
    }
    throw FlutUnknownMethodException(method);
  }
}
