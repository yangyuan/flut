import 'package:flutter/widgets.dart';
import 'package:flut/dart/ui.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutTextSelectionToolbarAnchors extends FlutValueObject {
  final TextSelectionToolbarAnchors anchors;

  const FlutTextSelectionToolbarAnchors(this.anchors)
    : super('TextSelectionToolbarAnchors');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['primaryAnchor'] = FlutOffset(anchors.primaryAnchor).flutEncode();
    if (anchors.secondaryAnchor != null) {
      result['secondaryAnchor'] = FlutOffset(
        anchors.secondaryAnchor!,
      ).flutEncode();
    }
    return result;
  }

  static TextSelectionToolbarAnchors? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return TextSelectionToolbarAnchors(
      primaryAnchor: runtime.unpackRequiredField<Offset>(data, 'primaryAnchor'),
      secondaryAnchor: runtime.unpackOptionalField<Offset>(
        data,
        'secondaryAnchor',
      ),
    );
  }
}
