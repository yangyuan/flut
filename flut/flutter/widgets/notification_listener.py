from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value

from flut.flutter.widgets.framework import Widget


class NotificationListener(Widget):
    _flut_type = "NotificationListener"

    def __init__(
        self,
        *,
        key=None,
        onNotification: Optional[Callable] = None,
        child: Widget,
    ):
        super().__init__(key=key)
        self.onNotification = onNotification
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["child"] = _flut_pack_value(self.child)
        if self.onNotification is not None:
            result["onNotification"] = self._register_action(
                self.onNotification, "NotificationListenerCallback"
            )._flut_pack()
        return result
