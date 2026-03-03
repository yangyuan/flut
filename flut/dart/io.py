from typing import override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class File(FlutValueObject):
    _flut_type = "File"

    def __init__(self, path: str):
        super().__init__()
        self.path = path

    @staticmethod
    def _flut_unpack(data: dict) -> "File":
        return File(path=_flut_unpack_required_field(data, "path"))

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["path"] = _flut_pack_value(self.path)
        return result

    def __repr__(self):
        return f"File('{self.path}')"
