from typing import Callable, Optional, override

from flut._flut.engine import wrap_value_widget_builder, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class ValueListenableBuilder(Widget):
    _flut_type = "ValueListenableBuilder"

    def __init__(
        self,
        *,
        key=None,
        valueListenable,
        builder: Callable,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.valueListenable = valueListenable
        self.builder = builder
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["valueListenable"] = _flut_pack_value(self.valueListenable)
        captured_child = self.child
        captured_builder = self.builder

        def _builder_wrapper(context, value):
            return captured_builder(context, value, captured_child)

        result["builder"] = self._register_build_action(
            wrap_value_widget_builder(_builder_wrapper), "ValueWidgetBuilder"
        )._flut_pack()
        return result
