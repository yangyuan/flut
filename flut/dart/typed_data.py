import base64
from typing import override
from flut._flut.engine import FlutValueObject


class Uint8List(FlutValueObject):
    _flut_type = "Uint8List"

    def __init__(self, data: bytes = b""):
        super().__init__()
        if isinstance(data, (bytes, bytearray)):
            self._data = bytes(data)
        elif isinstance(data, list):
            self._data = bytes(data)
        else:
            self._data = bytes(data)

    @staticmethod
    def _flut_unpack(data: dict) -> "Uint8List":
        return Uint8List(base64.b64decode(data["data"]))

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["data"] = base64.b64encode(self._data).decode("ascii")
        return result

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __bytes__(self):
        return self._data

    def __repr__(self):
        return (
            f"Uint8List({list(self._data[:8])}{'...' if len(self._data) > 8 else ''})"
        )

    def __eq__(self, other):
        if isinstance(other, Uint8List):
            return self._data == other._data
        return False

    def __hash__(self):
        return hash(self._data)
