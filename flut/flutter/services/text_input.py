from typing import override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field


class TextInputAction(FlutEnumObject):
    none: "TextInputAction"
    unspecified: "TextInputAction"
    done: "TextInputAction"
    go: "TextInputAction"
    search: "TextInputAction"
    send: "TextInputAction"
    next: "TextInputAction"
    previous: "TextInputAction"
    continueAction: "TextInputAction"
    join: "TextInputAction"
    route: "TextInputAction"
    emergencyCall: "TextInputAction"
    newline: "TextInputAction"


class _TextInputType(FlutValueObject):
    _flut_type = "TextInputType"

    def __init__(self, _name: str):
        super().__init__()
        self._name = _name

    @staticmethod
    def _flut_unpack(data: dict) -> "_TextInputType":
        return _TextInputType(
            _name=_flut_unpack_required_field(data, "name"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["name"] = self._name
        return result


class TextInputType(_TextInputType):
    text = _TextInputType("text")
    multiline = _TextInputType("multiline")
    number = _TextInputType("number")
    phone = _TextInputType("phone")
    datetime = _TextInputType("datetime")
    emailAddress = _TextInputType("emailAddress")
    url = _TextInputType("url")
    visiblePassword = _TextInputType("visiblePassword")
    name = _TextInputType("name")
    streetAddress = _TextInputType("streetAddress")
    none = _TextInputType("none")
