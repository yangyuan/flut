from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class _TextScaler(FlutValueObject):
    _flut_type = "TextScaler"

    def __init__(self, textScaleFactor: float):
        super().__init__()
        self._textScaleFactor = textScaleFactor

    def scale(self, fontSize: float) -> float:
        return fontSize * self._textScaleFactor

    def clamp(
        self, *, minScaleFactor: float = 0, maxScaleFactor: float = float("inf")
    ) -> "_TextScaler":
        factor = max(minScaleFactor, min(self._textScaleFactor, maxScaleFactor))
        return _TextScaler(textScaleFactor=factor)

    @staticmethod
    def _flut_unpack(data: dict) -> "_TextScaler":
        return _TextScaler(
            textScaleFactor=_flut_unpack_required_field(data, "textScaleFactor"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["textScaleFactor"] = _flut_pack_value(self._textScaleFactor)
        return result


class TextScaler(_TextScaler):
    noScaling = _TextScaler(textScaleFactor=1.0)

    @staticmethod
    def linear(textScaleFactor: float) -> "TextScaler":
        return TextScaler(textScaleFactor=textScaleFactor)
