import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutScrollDecelerationRate
    extends FlutEnumObject<ScrollDecelerationRate> {
  const FlutScrollDecelerationRate()
    : super('ScrollDecelerationRate', const {
        'normal': ScrollDecelerationRate.normal,
        'fast': ScrollDecelerationRate.fast,
      });
}

class FlutScrollPhysics extends FlutValueObject {
  final ScrollPhysics value;
  const FlutScrollPhysics(this.value) : super('ScrollPhysics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (value.parent != null) {
      result['parent'] = FlutScrollPhysics(value.parent!).flutEncode();
    }
    return result;
  }

  static ScrollPhysics? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ScrollPhysics(
      parent: runtime.unpackOptionalField<ScrollPhysics>(data, 'parent'),
    );
  }
}

class FlutBouncingScrollPhysics extends FlutValueObject {
  final BouncingScrollPhysics value;
  const FlutBouncingScrollPhysics(this.value) : super('BouncingScrollPhysics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['decelerationRate'] = const FlutScrollDecelerationRate().flutEncode(
      value.decelerationRate,
    )!;
    if (value.parent != null) {
      result['parent'] = FlutScrollPhysics(value.parent!).flutEncode();
    }
    return result;
  }

  static BouncingScrollPhysics? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return BouncingScrollPhysics(
      decelerationRate: runtime.unpackRequiredField<ScrollDecelerationRate>(
        data,
        'decelerationRate',
      ),
      parent: runtime.unpackOptionalField<ScrollPhysics>(data, 'parent'),
    );
  }
}

class FlutClampingScrollPhysics extends FlutValueObject {
  final ClampingScrollPhysics value;
  const FlutClampingScrollPhysics(this.value) : super('ClampingScrollPhysics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (value.parent != null) {
      result['parent'] = FlutScrollPhysics(value.parent!).flutEncode();
    }
    return result;
  }

  static ClampingScrollPhysics? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ClampingScrollPhysics(
      parent: runtime.unpackOptionalField<ScrollPhysics>(data, 'parent'),
    );
  }
}

class FlutNeverScrollableScrollPhysics extends FlutValueObject {
  final NeverScrollableScrollPhysics value;
  const FlutNeverScrollableScrollPhysics(this.value)
    : super('NeverScrollableScrollPhysics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (value.parent != null) {
      result['parent'] = FlutScrollPhysics(value.parent!).flutEncode();
    }
    return result;
  }

  static NeverScrollableScrollPhysics? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return NeverScrollableScrollPhysics(
      parent: runtime.unpackOptionalField<ScrollPhysics>(data, 'parent'),
    );
  }
}

class FlutAlwaysScrollableScrollPhysics extends FlutValueObject {
  final AlwaysScrollableScrollPhysics value;
  const FlutAlwaysScrollableScrollPhysics(this.value)
    : super('AlwaysScrollableScrollPhysics');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (value.parent != null) {
      result['parent'] = FlutScrollPhysics(value.parent!).flutEncode();
    }
    return result;
  }

  static AlwaysScrollableScrollPhysics? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AlwaysScrollableScrollPhysics(
      parent: runtime.unpackOptionalField<ScrollPhysics>(data, 'parent'),
    );
  }
}
