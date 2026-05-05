import 'package:flutter/services.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextSelection extends FlutValueObject {
  final TextSelection selection;

  const FlutTextSelection(this.selection) : super('TextSelection');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['baseOffset'] = selection.baseOffset;
    result['extentOffset'] = selection.extentOffset;
    result['affinity'] = const FlutTextAffinity().flutEncode(
      selection.affinity,
    );
    result['isDirectional'] = selection.isDirectional;
    return result;
  }

  static TextSelection? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextSelection(
      baseOffset: runtime.unpackRequiredField<int>(data, 'baseOffset'),
      extentOffset: runtime.unpackRequiredField<int>(data, 'extentOffset'),
      affinity: runtime.unpackRequiredField<TextAffinity>(data, 'affinity'),
      isDirectional: runtime.unpackRequiredField<bool>(data, 'isDirectional'),
    );
  }
}
