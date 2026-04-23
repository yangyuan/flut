from typing import override

from flut._flut.engine import (
    FlutAbstractObject,
    FlutEnumObject,
    FlutValueObject,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_required_field
from flut.flutter.widgets.framework import Widget


class TraversalDirection(FlutEnumObject):
    up: "TraversalDirection"
    right: "TraversalDirection"
    down: "TraversalDirection"
    left: "TraversalDirection"


class TraversalEdgeBehavior(FlutEnumObject):
    closedLoop: "TraversalEdgeBehavior"
    leaveFlutterView: "TraversalEdgeBehavior"
    parentScope: "TraversalEdgeBehavior"
    stop: "TraversalEdgeBehavior"


class FocusTraversalPolicy(FlutAbstractObject):
    _flut_type = "FocusTraversalPolicy"

    def __init__(self, *, requestFocusCallback=None):
        super().__init__()
        self.requestFocusCallback = requestFocusCallback

    def sortDescendants(self, descendants, currentNode):
        raise NotImplementedError

    def invalidateScopeData(self, node):
        pass

    def changedScope(self, *, node=None, oldScope=None):
        pass

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.requestFocusCallback is not None:
            result["requestFocusCallback"] = _flut_pack_value(self.requestFocusCallback)
        sort_callable = self._register_action(
            self.sortDescendants,
            base_class=FocusTraversalPolicy,
            method_name="sortDescendants",
        )
        if sort_callable is not None:
            result["sortDescendants"] = sort_callable._flut_pack()
        invalidate_callable = self._register_action(
            self.invalidateScopeData,
            base_class=FocusTraversalPolicy,
            method_name="invalidateScopeData",
        )
        if invalidate_callable is not None:
            result["invalidateScopeData"] = invalidate_callable._flut_pack()
        changed_callable = self._register_action(
            self.changedScope,
            base_class=FocusTraversalPolicy,
            method_name="changedScope",
        )
        if changed_callable is not None:
            result["changedScope"] = changed_callable._flut_pack()
        return result


class ReadingOrderTraversalPolicy(FocusTraversalPolicy):
    _flut_type = "ReadingOrderTraversalPolicy"

    def __init__(self, *, requestFocusCallback=None):
        super().__init__(requestFocusCallback=requestFocusCallback)


class OrderedTraversalPolicy(FocusTraversalPolicy):
    _flut_type = "OrderedTraversalPolicy"

    def __init__(self, *, secondary=None, requestFocusCallback=None):
        super().__init__(requestFocusCallback=requestFocusCallback)
        self.secondary = secondary

    @override
    def _flut_pack(self) -> dict:
        result = super()._flut_pack()
        if self.secondary is not None:
            result["secondary"] = _flut_pack_value(self.secondary)
        return result


class WidgetOrderTraversalPolicy(FocusTraversalPolicy):
    _flut_type = "WidgetOrderTraversalPolicy"

    def __init__(self, *, requestFocusCallback=None):
        super().__init__(requestFocusCallback=requestFocusCallback)


class FocusOrder(FlutValueObject):
    _flut_type = "FocusOrder"

    def __init__(self):
        super().__init__()


class NumericFocusOrder(FocusOrder):
    _flut_type = "NumericFocusOrder"

    def __init__(self, order: float):
        super().__init__()
        self.order = order

    @staticmethod
    def _flut_unpack(data: dict) -> "NumericFocusOrder":
        return NumericFocusOrder(
            order=_flut_unpack_required_field(data, "order"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["order"] = _flut_pack_value(self.order)
        return result


class FocusTraversalGroup(Widget):
    _flut_type = "FocusTraversalGroup"

    def __init__(
        self,
        *,
        key=None,
        policy=None,
        descendantsAreFocusable: bool = True,
        descendantsAreTraversable: bool = True,
        onFocusNodeCreated=None,
        child: Widget,
    ):
        super().__init__(key=key)
        self.policy = policy
        self.descendantsAreFocusable = descendantsAreFocusable
        self.descendantsAreTraversable = descendantsAreTraversable
        self.onFocusNodeCreated = onFocusNodeCreated
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.policy is not None:
            result["policy"] = _flut_pack_value(self.policy)
        result["descendantsAreFocusable"] = _flut_pack_value(
            self.descendantsAreFocusable
        )
        result["descendantsAreTraversable"] = _flut_pack_value(
            self.descendantsAreTraversable
        )
        if self.onFocusNodeCreated is not None:
            result["onFocusNodeCreated"] = self._register_action(
                self.onFocusNodeCreated, "void Function(FocusNode)"
            )._flut_pack()
        result["child"] = _flut_pack_value(self.child)
        return result


class FocusTraversalOrder(Widget):
    _flut_type = "FocusTraversalOrder"

    def __init__(self, *, key=None, order, child: Widget):
        super().__init__(key=key)
        self.order = order
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["order"] = _flut_pack_value(self.order)
        result["child"] = _flut_pack_value(self.child)
        return result
