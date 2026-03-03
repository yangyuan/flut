from typing import override

from flut._flut.engine import call_dart_static, named_constructor, _flut_pack_value

from flut.flutter.widgets.framework import Widget
from flut.flutter.widgets.basic import SizedBox


class Visibility(Widget):
    _flut_type = "Visibility"

    def __init__(
        self,
        *,
        key=None,
        replacement=SizedBox.shrink(),
        visible: bool = True,
        maintainState: bool = False,
        maintainAnimation: bool = False,
        maintainSize: bool = False,
        maintainSemantics: bool = False,
        maintainInteractivity: bool = False,
        maintainFocusability: bool = False,
        child,
    ):
        super().__init__(key=key)
        self.replacement = replacement
        self.visible = visible
        self.maintainState = maintainState
        self.maintainAnimation = maintainAnimation
        self.maintainSize = maintainSize
        self.maintainSemantics = maintainSemantics
        self.maintainInteractivity = maintainInteractivity
        self.maintainFocusability = maintainFocusability
        self.child = child

    @named_constructor
    def maintain(cls, *, key=None, visible: bool = True, child):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.replacement = SizedBox.shrink()
        instance.visible = visible
        instance.maintainState = True
        instance.maintainAnimation = True
        instance.maintainSize = True
        instance.maintainSemantics = True
        instance.maintainInteractivity = True
        instance.maintainFocusability = True
        instance.child = child
        return instance

    @staticmethod
    def of(context) -> bool:
        return call_dart_static("Visibility", "of", context._flut_pack())

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["visible"] = _flut_pack_value(self.visible)
        result["maintainState"] = _flut_pack_value(self.maintainState)
        result["maintainAnimation"] = _flut_pack_value(self.maintainAnimation)
        result["maintainSize"] = _flut_pack_value(self.maintainSize)
        result["maintainSemantics"] = _flut_pack_value(self.maintainSemantics)
        result["maintainInteractivity"] = _flut_pack_value(self.maintainInteractivity)
        result["maintainFocusability"] = _flut_pack_value(self.maintainFocusability)
        result["replacement"] = _flut_pack_value(self.replacement)
        result["child"] = _flut_pack_value(self.child)
        return result
