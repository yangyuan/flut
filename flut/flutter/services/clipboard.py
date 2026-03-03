from typing import override

from flut._flut.engine import FlutValueObject, call_dart_static, _flut_pack_value


class ClipboardData(FlutValueObject):
    _flut_type = "ClipboardData"

    def __init__(self, *, text):
        super().__init__()
        self.text = text

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["text"] = _flut_pack_value(self.text)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ClipboardData":
        return ClipboardData(
            text=data["text"],
        )


class Clipboard:
    @staticmethod
    def setData(data: ClipboardData):
        call_dart_static("Clipboard", "setData", data._flut_pack())

    @staticmethod
    def getData(format: str):
        result = call_dart_static("Clipboard", "getData", format)
        if result is not None:
            return ClipboardData._flut_unpack(result)
        return None
