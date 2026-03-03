from typing import Optional

from flut._flut.engine import call_dart_static
from flut.flutter.foundation.change_notifier import ChangeNotifier


class ExpansibleController(ChangeNotifier):
    _flut_type = "ExpansibleController"

    def __init__(self):
        super().__init__()
        self._flut_create(props={})

    @property
    def isExpanded(self) -> bool:
        return bool(self._flut_get("isExpanded"))

    def expand(self):
        self._flut_call("expand")

    def collapse(self):
        self._flut_call("collapse")

    def dispose(self):
        self._flut_call("dispose")

    @staticmethod
    def of(context) -> "ExpansibleController":
        return call_dart_static("ExpansibleController", "of", context._flut_pack())

    @staticmethod
    def maybeOf(context) -> "Optional[ExpansibleController]":
        return call_dart_static("ExpansibleController", "maybeOf", context._flut_pack())
