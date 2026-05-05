import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutSelectableRegionState with FlutRealtimeObject<SelectableRegionState> {
  FlutSelectableRegionState.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required SelectableRegionState target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'SelectableRegionState',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('SelectableRegionState', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('SelectableRegionState', property);
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

class FlutSelectableRegion {
  FlutSelectableRegion._();

  static SelectableRegion? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectableRegion(
      key: runtime.decodeKey(data),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      selectionControls: runtime.unpackRequiredField<TextSelectionControls>(
        data,
        'selectionControls',
      ),
      contextMenuBuilder: runtime.unpackOptionalCallback(
        data,
        'contextMenuBuilder',
      ),
      magnifierConfiguration: runtime
          .unpackRequiredField<TextMagnifierConfiguration>(
            data,
            'magnifierConfiguration',
          ),
      onSelectionChanged: runtime.unpackOptionalCallback(
        data,
        'onSelectionChanged',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutSelectableRegionSelectionStatus
    extends FlutEnumObject<SelectableRegionSelectionStatus> {
  const FlutSelectableRegionSelectionStatus()
    : super('SelectableRegionSelectionStatus', const {
        'changing': SelectableRegionSelectionStatus.changing,
        'finalized': SelectableRegionSelectionStatus.finalized,
      });
}
