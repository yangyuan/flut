from typing import override

from flut._flut.engine import FlutValueObject


class ScrollBehavior(FlutValueObject):
    _flut_type = "ScrollBehavior"

    def __init__(self):
        super().__init__()

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ScrollBehavior":
        return ScrollBehavior()
