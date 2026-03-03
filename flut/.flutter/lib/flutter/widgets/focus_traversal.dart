import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutTraversalDirection extends FlutEnumObject<TraversalDirection> {
  const FlutTraversalDirection()
    : super('TraversalDirection', const {
        'up': TraversalDirection.up,
        'right': TraversalDirection.right,
        'down': TraversalDirection.down,
        'left': TraversalDirection.left,
      });
}

class FlutTraversalEdgeBehavior extends FlutEnumObject<TraversalEdgeBehavior> {
  const FlutTraversalEdgeBehavior()
    : super('TraversalEdgeBehavior', const {
        'closedLoop': TraversalEdgeBehavior.closedLoop,
        'leaveFlutterView': TraversalEdgeBehavior.leaveFlutterView,
        'parentScope': TraversalEdgeBehavior.parentScope,
        'stop': TraversalEdgeBehavior.stop,
      });
}

class FlutFocusTraversalPolicy extends FocusTraversalPolicy
    with FlutAbstractObject {
  @override
  final FlutRuntime runtime;
  final int? sortDescendantsId;
  final int? invalidateScopeDataId;
  final int? changedScopeId;

  FlutFocusTraversalPolicy._(
    this.runtime,
    this.sortDescendantsId,
    this.invalidateScopeDataId,
    this.changedScopeId,
  );

  @override
  Iterable<FocusNode> sortDescendants(
    Iterable<FocusNode> descendants,
    FocusNode currentNode,
  ) {
    if (sortDescendantsId == null) return descendants;
    final result = runtime.callAction<List<dynamic>>(
      sortDescendantsId!,
      args: [descendants.toList(), currentNode],
    );
    if (result == null) return descendants;
    return result
        .map((item) => runtime.decodeObject<FocusNode>(item))
        .nonNulls
        .toList();
  }

  @override
  void invalidateScopeData(FocusScopeNode node) {
    super.invalidateScopeData(node);
    if (invalidateScopeDataId == null) return;
    runtime.callAction(invalidateScopeDataId!, args: [node]);
  }

  @override
  void changedScope({FocusNode? node, FocusScopeNode? oldScope}) {
    super.changedScope(node: node, oldScope: oldScope);
    if (changedScopeId == null) return;
    runtime.callAction(changedScopeId!, args: [node, oldScope]);
  }

  @override
  FocusNode? findFirstFocusInDirection(
    FocusNode currentNode,
    TraversalDirection direction,
  ) {
    throw UnimplementedError(
      'findFirstFocusInDirection is not supported in custom Python traversal policies',
    );
  }

  @override
  bool inDirection(FocusNode currentNode, TraversalDirection direction) {
    throw UnimplementedError(
      'inDirection is not supported in custom Python traversal policies',
    );
  }

  static FocusTraversalPolicy? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FlutFocusTraversalPolicy._(
      runtime,
      runtime.unpackOptionalField<int>(data, 'sortDescendants'),
      runtime.unpackOptionalField<int>(data, 'invalidateScopeData'),
      runtime.unpackOptionalField<int>(data, 'changedScope'),
    );
  }
}

class FlutReadingOrderTraversalPolicy {
  FlutReadingOrderTraversalPolicy._();

  static ReadingOrderTraversalPolicy? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ReadingOrderTraversalPolicy();
  }
}

class FlutOrderedTraversalPolicy {
  FlutOrderedTraversalPolicy._();

  static OrderedTraversalPolicy? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return OrderedTraversalPolicy(
      secondary: runtime.unpackOptionalField<FocusTraversalPolicy>(
        data,
        'secondary',
      ),
    );
  }
}

class FlutWidgetOrderTraversalPolicy {
  FlutWidgetOrderTraversalPolicy._();

  static WidgetOrderTraversalPolicy? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return WidgetOrderTraversalPolicy();
  }
}

class FlutNumericFocusOrder extends FlutValueObject {
  final NumericFocusOrder order;
  const FlutNumericFocusOrder(this.order) : super('NumericFocusOrder');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['order'] = order.order;
    return result;
  }

  static NumericFocusOrder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return NumericFocusOrder(
      runtime.unpackRequiredField<double>(data, 'order'),
    );
  }
}

class FlutFocusTraversalGroup {
  FlutFocusTraversalGroup._();

  static FocusTraversalGroup? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FocusTraversalGroup(
      key: runtime.decodeKey(data),
      policy: runtime.unpackOptionalField<FocusTraversalPolicy>(data, 'policy'),
      descendantsAreFocusable: runtime.unpackRequiredField<bool>(
        data,
        'descendantsAreFocusable',
      ),
      descendantsAreTraversable: runtime.unpackRequiredField<bool>(
        data,
        'descendantsAreTraversable',
      ),
      onFocusNodeCreated: runtime.unpackOptionalCallback(
        data,
        'onFocusNodeCreated',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutFocusTraversalOrder {
  FlutFocusTraversalOrder._();

  static FocusTraversalOrder? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FocusTraversalOrder(
      key: runtime.decodeKey(data),
      order: runtime.unpackRequiredField<FocusOrder>(data, 'order'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
