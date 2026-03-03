from typing import override

from flut._flut.engine import FlutValueObject, FlutRealtimeObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class Key(FlutValueObject):
    _flut_type = "ValueKey"

    def __init__(self, value: str):
        super().__init__()
        self.value = value

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "Key":
        key_type = data.get("_flut_type")
        if key_type == "ValueKey":
            return ValueKey._flut_unpack(data)
        if key_type == "UniqueKey":
            return UniqueKey._flut_unpack(data)
        return ValueKey._flut_unpack(data)


class LocalKey(Key):

    def __init__(self):
        FlutValueObject.__init__(self)

    @override
    def _flut_pack(self) -> dict:
        return self._flut_base_props()


class UniqueKey(FlutRealtimeObject):
    _flut_type = "UniqueKey"

    def __init__(self):
        super().__init__()
        self._flut_create()

    @override
    def _flut_pack(self) -> dict:
        return self._flut_base_props()

    def __repr__(self):
        return f"UniqueKey({self._flut_oid})"


class ValueKey(LocalKey):
    _flut_type = "ValueKey"

    def __init__(self, value):
        super().__init__()
        self.value = value

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["value"] = _flut_pack_value(self.value)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "ValueKey":
        return ValueKey(value=_flut_unpack_required_field(data, "value"))

    def __eq__(self, other):
        if not isinstance(other, ValueKey):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"ValueKey({self.value!r})"
