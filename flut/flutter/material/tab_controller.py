from typing import Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.foundation.change_notifier import ChangeNotifier
from flut.flutter.widgets.framework import Widget
from flut.flutter.animation.curves import Curve, Curves
from flut.dart.core import Duration


class TabController(ChangeNotifier):
    _flut_type = "TabController"

    def __init__(
        self,
        *,
        initialIndex: int = 0,
        animationDuration: Optional[Duration] = None,
        length: int,
        vsync,
    ):
        super().__init__()
        props = {
            "initialIndex": initialIndex,
            "length": length,
            "vsync": vsync._flut_pack(),
        }
        if animationDuration is not None:
            props["animationDuration"] = animationDuration._flut_pack()
        self._flut_create(props=props)

    @property
    def index(self) -> int:
        return self._flut_get("index")

    @index.setter
    def index(self, value: int):
        self._flut_set("index", value)

    @property
    def length(self) -> int:
        return self._flut_get("length")

    @property
    def previousIndex(self) -> int:
        return self._flut_get("previousIndex")

    @property
    def indexIsChanging(self) -> bool:
        return bool(self._flut_get("indexIsChanging"))

    def animateTo(
        self,
        value: int,
        *,
        duration: Optional[Duration] = None,
        curve: Curve = Curves.ease,
    ):
        self._flut_call(
            "animateTo",
            value,
            duration=_flut_pack_value(duration),
            curve=_flut_pack_value(curve),
        )

    def dispose(self):
        self._flut_call("dispose")


class DefaultTabController(Widget):
    _flut_type = "DefaultTabController"

    def __init__(
        self,
        *,
        key=None,
        length: int,
        initialIndex: int = 0,
        animationDuration: Optional[Duration] = None,
        child: Widget,
    ):
        super().__init__(key=key)
        self.length = length
        self.initialIndex = initialIndex
        self.animationDuration = animationDuration
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["length"] = _flut_pack_value(self.length)
        result["initialIndex"] = _flut_pack_value(self.initialIndex)
        if self.animationDuration is not None:
            result["animationDuration"] = _flut_pack_value(self.animationDuration)
        result["child"] = _flut_pack_value(self.child)
        return result
