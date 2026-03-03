from typing import override

from flut._flut.engine import _flut_pack_value
from flut.flutter.widgets.framework import Widget


class Spacer(Widget):
    _flut_type = "Spacer"

    def __init__(self, *, key=None, flex: int = 1):
        super().__init__(key=key)
        self.flex = flex

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["flex"] = _flut_pack_value(self.flex)
        return result
