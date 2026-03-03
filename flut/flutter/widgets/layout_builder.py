from typing import Callable, override

from flut._flut.engine import wrap_layout_widget_builder
from flut.flutter.widgets.framework import Widget, BuildContext
from flut.flutter.rendering.box import BoxConstraints


class LayoutBuilder(Widget):
    _flut_type = "LayoutBuilder"

    def __init__(
        self,
        *,
        key=None,
        builder: Callable[[BuildContext, BoxConstraints], Widget],
    ):
        super().__init__(key=key)
        self.builder = builder

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["builder"] = self._register_build_action(
            wrap_layout_widget_builder(self.builder), "LayoutWidgetBuilder"
        )._flut_pack()
        return result
