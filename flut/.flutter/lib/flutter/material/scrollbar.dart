import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutScrollbar {
  FlutScrollbar._();

  static Scrollbar? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Scrollbar(
      key: runtime.decodeKey(data),
      controller: runtime.unpackOptionalField<ScrollController>(
        data,
        'controller',
      ),
      thumbVisibility: runtime.unpackOptionalField<bool>(
        data,
        'thumbVisibility',
      ),
      trackVisibility: runtime.unpackOptionalField<bool>(
        data,
        'trackVisibility',
      ),
      thickness: runtime.unpackOptionalField<double>(data, 'thickness'),
      radius: runtime.unpackOptionalField<Radius>(data, 'radius'),
      interactive: runtime.unpackOptionalField<bool>(data, 'interactive'),
      scrollbarOrientation: runtime.unpackOptionalField<ScrollbarOrientation>(
        data,
        'scrollbarOrientation',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
