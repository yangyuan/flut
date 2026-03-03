from typing import Callable, Optional, override

from flut._flut.engine import FlutObject, wrap_widget_builder, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class ListenableBuilder(Widget):
    _flut_type = "ListenableBuilder"

    def __init__(
        self,
        *,
        key=None,
        listenable,
        builder: Callable,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.listenable = listenable
        self.builder = builder
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["listenable"] = _flut_pack_value(self.listenable)
        captured_child = self.child
        captured_builder = self.builder

        def _builder_wrapper(context):
            return captured_builder(context, captured_child)

        result["builder"] = self._register_build_action(
            wrap_widget_builder(_builder_wrapper), "TransitionBuilder"
        )._flut_pack()
        return result


class AnimatedBuilder(Widget):
    _flut_type = "AnimatedBuilder"

    def __init__(
        self,
        *,
        key=None,
        animation,
        builder: Callable,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.animation = animation
        self.builder = builder
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["animation"] = _flut_pack_value(self.animation)
        captured_child = self.child
        captured_builder = self.builder

        def _builder_wrapper(context):
            return captured_builder(context, captured_child)

        result["builder"] = self._register_build_action(
            wrap_widget_builder(_builder_wrapper), "TransitionBuilder"
        )._flut_pack()
        return result
