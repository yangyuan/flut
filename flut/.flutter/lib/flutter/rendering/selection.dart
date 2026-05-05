import 'package:flut/dart/ui.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flutter/rendering.dart';

class FlutSelectionResult extends FlutEnumObject<SelectionResult> {
  const FlutSelectionResult()
    : super('SelectionResult', const {
        'next': SelectionResult.next,
        'previous': SelectionResult.previous,
        'end': SelectionResult.end,
        'pending': SelectionResult.pending,
        'none': SelectionResult.none,
      });
}

class FlutSelectionEventType extends FlutEnumObject<SelectionEventType> {
  const FlutSelectionEventType()
    : super('SelectionEventType', const {
        'startEdgeUpdate': SelectionEventType.startEdgeUpdate,
        'endEdgeUpdate': SelectionEventType.endEdgeUpdate,
        'clear': SelectionEventType.clear,
        'selectAll': SelectionEventType.selectAll,
        'selectWord': SelectionEventType.selectWord,
        'selectParagraph': SelectionEventType.selectParagraph,
        'granularlyExtendSelection':
            SelectionEventType.granularlyExtendSelection,
        'directionallyExtendSelection':
            SelectionEventType.directionallyExtendSelection,
      });
}

class FlutTextGranularity extends FlutEnumObject<TextGranularity> {
  const FlutTextGranularity()
    : super('TextGranularity', const {
        'character': TextGranularity.character,
        'word': TextGranularity.word,
        'paragraph': TextGranularity.paragraph,
        'line': TextGranularity.line,
        'document': TextGranularity.document,
      });
}

class FlutSelectionExtendDirection
    extends FlutEnumObject<SelectionExtendDirection> {
  const FlutSelectionExtendDirection()
    : super('SelectionExtendDirection', const {
        'previousLine': SelectionExtendDirection.previousLine,
        'nextLine': SelectionExtendDirection.nextLine,
        'forward': SelectionExtendDirection.forward,
        'backward': SelectionExtendDirection.backward,
      });
}

class FlutTextSelectionHandleType
    extends FlutEnumObject<TextSelectionHandleType> {
  const FlutTextSelectionHandleType()
    : super('TextSelectionHandleType', const {
        'left': TextSelectionHandleType.left,
        'right': TextSelectionHandleType.right,
        'collapsed': TextSelectionHandleType.collapsed,
      });
}

class FlutSelectedContent extends FlutValueObject {
  final SelectedContent selectedContent;

  const FlutSelectedContent(this.selectedContent) : super('SelectedContent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['plainText'] = selectedContent.plainText;
    return result;
  }

  static SelectedContent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectedContent(
      plainText: runtime.unpackRequiredField<String>(data, 'plainText'),
    );
  }
}

class FlutSelectedContentRange extends FlutValueObject {
  final SelectedContentRange range;

  const FlutSelectedContentRange(this.range) : super('SelectedContentRange');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['startOffset'] = range.startOffset;
    result['endOffset'] = range.endOffset;
    return result;
  }

  static SelectedContentRange? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectedContentRange(
      startOffset: runtime.unpackRequiredField<int>(data, 'startOffset'),
      endOffset: runtime.unpackRequiredField<int>(data, 'endOffset'),
    );
  }
}

class FlutSelectionPoint extends FlutValueObject {
  final SelectionPoint point;

  const FlutSelectionPoint(this.point) : super('SelectionPoint');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['localPosition'] = FlutOffset(point.localPosition).flutEncode();
    result['lineHeight'] = point.lineHeight;
    result['handleType'] = const FlutTextSelectionHandleType().flutEncode(
      point.handleType,
    );
    return result;
  }

  static SelectionPoint? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectionPoint(
      localPosition: runtime.unpackRequiredField<Offset>(data, 'localPosition'),
      lineHeight: runtime.unpackRequiredField<double>(data, 'lineHeight'),
      handleType: runtime.unpackRequiredField<TextSelectionHandleType>(
        data,
        'handleType',
      ),
    );
  }
}

class FlutSelectionGeometry extends FlutValueObject {
  final SelectionGeometry geometry;

  const FlutSelectionGeometry(this.geometry) : super('SelectionGeometry');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (geometry.startSelectionPoint != null) {
      result['startSelectionPoint'] = FlutSelectionPoint(
        geometry.startSelectionPoint!,
      ).flutEncode();
    }
    if (geometry.endSelectionPoint != null) {
      result['endSelectionPoint'] = FlutSelectionPoint(
        geometry.endSelectionPoint!,
      ).flutEncode();
    }
    result['selectionRects'] = geometry.selectionRects
        .map((rect) => FlutRect(rect).flutEncode())
        .toList();
    result['status'] = const FlutSelectionStatus().flutEncode(geometry.status);
    result['hasContent'] = geometry.hasContent;
    return result;
  }

  static SelectionGeometry? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectionGeometry(
      startSelectionPoint: runtime.unpackOptionalField<SelectionPoint>(
        data,
        'startSelectionPoint',
      ),
      endSelectionPoint: runtime.unpackOptionalField<SelectionPoint>(
        data,
        'endSelectionPoint',
      ),
      selectionRects: runtime
          .unpackRequiredField<List<dynamic>>(data, 'selectionRects')
          .cast<Rect>(),
      status: runtime.unpackRequiredField<SelectionStatus>(data, 'status'),
      hasContent: runtime.unpackRequiredField<bool>(data, 'hasContent'),
    );
  }
}

class FlutSelectAllSelectionEvent extends FlutValueObject {
  final SelectAllSelectionEvent event;

  const FlutSelectAllSelectionEvent(this.event)
    : super('SelectAllSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() => flutBaseProps();

  static SelectAllSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return const SelectAllSelectionEvent();
  }
}

class FlutClearSelectionEvent extends FlutValueObject {
  final ClearSelectionEvent event;

  const FlutClearSelectionEvent(this.event) : super('ClearSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() => flutBaseProps();

  static ClearSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return const ClearSelectionEvent();
  }
}

class FlutSelectWordSelectionEvent extends FlutValueObject {
  final SelectWordSelectionEvent event;

  const FlutSelectWordSelectionEvent(this.event)
    : super('SelectWordSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(event.globalPosition).flutEncode();
    return result;
  }

  static SelectWordSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectWordSelectionEvent(
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
    );
  }
}

class FlutSelectParagraphSelectionEvent extends FlutValueObject {
  final SelectParagraphSelectionEvent event;

  const FlutSelectParagraphSelectionEvent(this.event)
    : super('SelectParagraphSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['globalPosition'] = FlutOffset(event.globalPosition).flutEncode();
    result['absorb'] = event.absorb;
    return result;
  }

  static SelectParagraphSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectParagraphSelectionEvent(
      globalPosition: runtime.unpackRequiredField<Offset>(
        data,
        'globalPosition',
      ),
      absorb: runtime.unpackRequiredField<bool>(data, 'absorb'),
    );
  }
}

class FlutSelectionEdgeUpdateEvent extends FlutValueObject {
  final SelectionEdgeUpdateEvent event;

  const FlutSelectionEdgeUpdateEvent(this.event)
    : super('SelectionEdgeUpdateEvent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['type'] = const FlutSelectionEventType().flutEncode(event.type);
    result['globalPosition'] = FlutOffset(event.globalPosition).flutEncode();
    result['granularity'] = const FlutTextGranularity().flutEncode(
      event.granularity,
    );
    return result;
  }

  static SelectionEdgeUpdateEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final type = runtime.unpackRequiredField<SelectionEventType>(data, 'type');
    final globalPosition = runtime.unpackRequiredField<Offset>(
      data,
      'globalPosition',
    );
    final granularity = runtime.unpackRequiredField<TextGranularity>(
      data,
      'granularity',
    );
    return switch (type) {
      SelectionEventType.startEdgeUpdate => SelectionEdgeUpdateEvent.forStart(
        globalPosition: globalPosition,
        granularity: granularity,
      ),
      SelectionEventType.endEdgeUpdate => SelectionEdgeUpdateEvent.forEnd(
        globalPosition: globalPosition,
        granularity: granularity,
      ),
      _ => throw ArgumentError('Invalid SelectionEdgeUpdateEvent type: $type'),
    };
  }
}

class FlutGranularlyExtendSelectionEvent extends FlutValueObject {
  final GranularlyExtendSelectionEvent event;

  const FlutGranularlyExtendSelectionEvent(this.event)
    : super('GranularlyExtendSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['forward'] = event.forward;
    result['isEnd'] = event.isEnd;
    result['granularity'] = const FlutTextGranularity().flutEncode(
      event.granularity,
    );
    return result;
  }

  static GranularlyExtendSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return GranularlyExtendSelectionEvent(
      forward: runtime.unpackRequiredField<bool>(data, 'forward'),
      isEnd: runtime.unpackRequiredField<bool>(data, 'isEnd'),
      granularity: runtime.unpackRequiredField<TextGranularity>(
        data,
        'granularity',
      ),
    );
  }
}

class FlutDirectionallyExtendSelectionEvent extends FlutValueObject {
  final DirectionallyExtendSelectionEvent event;

  const FlutDirectionallyExtendSelectionEvent(this.event)
    : super('DirectionallyExtendSelectionEvent');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['dx'] = event.dx;
    result['isEnd'] = event.isEnd;
    result['direction'] = const FlutSelectionExtendDirection().flutEncode(
      event.direction,
    );
    return result;
  }

  static DirectionallyExtendSelectionEvent? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return DirectionallyExtendSelectionEvent(
      dx: runtime.unpackRequiredField<double>(data, 'dx'),
      isEnd: runtime.unpackRequiredField<bool>(data, 'isEnd'),
      direction: runtime.unpackRequiredField<SelectionExtendDirection>(
        data,
        'direction',
      ),
    );
  }
}

class FlutSelectionStatus extends FlutEnumObject<SelectionStatus> {
  const FlutSelectionStatus()
    : super('SelectionStatus', const {
        'uncollapsed': SelectionStatus.uncollapsed,
        'collapsed': SelectionStatus.collapsed,
        'none': SelectionStatus.none,
      });
}
