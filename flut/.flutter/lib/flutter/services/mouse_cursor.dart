import 'package:flutter/services.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutMouseCursor extends MouseCursor with FlutAbstractObject {
  final String _debugDescription;
  @override
  final FlutRuntime runtime;

  const FlutMouseCursor._(this._debugDescription, this.runtime);

  @override
  MouseCursorSession createSession(int device) {
    throw UnimplementedError();
  }

  @override
  String get debugDescription => _debugDescription;

  static MouseCursor? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final debugDescription = runtime.unpackRequiredField<String>(
      data,
      'debugDescription',
    );
    if (debugDescription == 'defer') return MouseCursor.defer;
    if (debugDescription == 'uncontrolled') return MouseCursor.uncontrolled;
    return FlutMouseCursor._(debugDescription, runtime);
  }
}

class FlutSystemMouseCursor {
  FlutSystemMouseCursor._();

  static const _cursors = <String, SystemMouseCursor>{
    'none': SystemMouseCursors.none,
    'basic': SystemMouseCursors.basic,
    'click': SystemMouseCursors.click,
    'forbidden': SystemMouseCursors.forbidden,
    'wait': SystemMouseCursors.wait,
    'progress': SystemMouseCursors.progress,
    'contextMenu': SystemMouseCursors.contextMenu,
    'help': SystemMouseCursors.help,
    'text': SystemMouseCursors.text,
    'verticalText': SystemMouseCursors.verticalText,
    'cell': SystemMouseCursors.cell,
    'precise': SystemMouseCursors.precise,
    'move': SystemMouseCursors.move,
    'grab': SystemMouseCursors.grab,
    'grabbing': SystemMouseCursors.grabbing,
    'noDrop': SystemMouseCursors.noDrop,
    'alias': SystemMouseCursors.alias,
    'copy': SystemMouseCursors.copy,
    'disappearing': SystemMouseCursors.disappearing,
    'allScroll': SystemMouseCursors.allScroll,
    'resizeLeftRight': SystemMouseCursors.resizeLeftRight,
    'resizeUpDown': SystemMouseCursors.resizeUpDown,
    'resizeUpLeftDownRight': SystemMouseCursors.resizeUpLeftDownRight,
    'resizeUpRightDownLeft': SystemMouseCursors.resizeUpRightDownLeft,
    'resizeUp': SystemMouseCursors.resizeUp,
    'resizeDown': SystemMouseCursors.resizeDown,
    'resizeLeft': SystemMouseCursors.resizeLeft,
    'resizeRight': SystemMouseCursors.resizeRight,
    'resizeUpLeft': SystemMouseCursors.resizeUpLeft,
    'resizeUpRight': SystemMouseCursors.resizeUpRight,
    'resizeDownLeft': SystemMouseCursors.resizeDownLeft,
    'resizeDownRight': SystemMouseCursors.resizeDownRight,
    'resizeColumn': SystemMouseCursors.resizeColumn,
    'resizeRow': SystemMouseCursors.resizeRow,
    'zoomIn': SystemMouseCursors.zoomIn,
    'zoomOut': SystemMouseCursors.zoomOut,
  };

  static MouseCursor? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final kind = runtime.unpackRequiredField<String>(data, 'kind');
    return _cursors[kind]!;
  }
}
