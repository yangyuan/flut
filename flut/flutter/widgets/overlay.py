from typing import Callable, Optional

from flut._flut.engine import FlutRealtimeObject, call_dart_static, wrap_widget_builder
from flut.flutter.foundation.change_notifier import Listenable
from flut.flutter.widgets.framework import Widget, BuildContext


class OverlayEntry(Listenable):
    _flut_type = "OverlayEntry"

    def __init__(
        self,
        *,
        builder: Callable[[BuildContext], Widget],
        opaque: bool = False,
        maintainState: bool = False,
        canSizeOverlay: bool = False,
    ):
        self._flut_init_props = {
            "opaque": opaque,
            "maintainState": maintainState,
            "canSizeOverlay": canSizeOverlay,
        }
        self._flut_init_bindings = [
            ("builder", wrap_widget_builder(builder), "build_scope"),
        ]
        Listenable.__init__(self)

    @property
    def mounted(self) -> bool:
        return bool(self._flut_get("mounted"))

    def remove(self):
        self._flut_call("remove")

    def markNeedsBuild(self):
        self._flut_call("markNeedsBuild")

    def dispose(self):
        self._flut_call("dispose")


class OverlayState(FlutRealtimeObject):
    _flut_type = "OverlayState"

    def insert(
        self,
        entry: OverlayEntry,
        *,
        below: Optional[OverlayEntry] = None,
        above: Optional[OverlayEntry] = None,
    ):
        kwargs = {}
        if below is not None:
            kwargs["below"] = below._flut_pack()
        if above is not None:
            kwargs["above"] = above._flut_pack()
        self._flut_call("insert", entry._flut_pack(), **kwargs)

    def insertAll(
        self,
        entries,
        *,
        below: Optional[OverlayEntry] = None,
        above: Optional[OverlayEntry] = None,
    ):
        packed = [e._flut_pack() for e in entries]
        kwargs = {}
        if below is not None:
            kwargs["below"] = below._flut_pack()
        if above is not None:
            kwargs["above"] = above._flut_pack()
        self._flut_call("insertAll", packed, **kwargs)

    def rearrange(
        self,
        newEntries,
        *,
        below: Optional[OverlayEntry] = None,
        above: Optional[OverlayEntry] = None,
    ):
        packed = [e._flut_pack() for e in newEntries]
        kwargs = {}
        if below is not None:
            kwargs["below"] = below._flut_pack()
        if above is not None:
            kwargs["above"] = above._flut_pack()
        self._flut_call("rearrange", packed, **kwargs)


class Overlay:
    @staticmethod
    def of(context, *, rootOverlay: bool = False) -> OverlayState:
        return call_dart_static("Overlay", "of", context._flut_pack(), rootOverlay)
