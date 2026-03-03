import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/dart/ui.dart';

class FlutCustomPainter extends CustomPainter with FlutAbstractObject {
  @override
  final FlutRuntime runtime;
  final int paintId;
  final int? shouldRepaintId;

  FlutCustomPainter._(this.runtime, this.paintId, this.shouldRepaintId);

  static FlutCustomPainter? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final paintId = runtime.unpackOptionalField<int>(data, 'paint');
    if (paintId == null) return null;
    return FlutCustomPainter._(
      runtime,
      paintId,
      runtime.unpackOptionalField<int>(data, 'shouldRepaint'),
    );
  }

  @override
  void paint(Canvas canvas, Size size) {
    final wrapper = runtime.wrapObject(
      canvas,
      (oid) => FlutCanvas.createFromObject(
        runtime: runtime,
        oid: oid,
        target: canvas,
      ),
    );
    runtime.callAction(paintId, args: [wrapper, size]);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    if (shouldRepaintId == null) return true;
    return runtime.callAction<bool>(shouldRepaintId!) ?? true;
  }
}
