from typing import override

from flut._flut.engine import (
    FlutValueObject,
    Future,
    call_dart_static,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_optional_field


class RouteSettings(FlutValueObject):
    _flut_type = "RouteSettings"

    def __init__(self, *, name=None, arguments=None):
        super().__init__()
        self.name = name
        self.arguments = arguments

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.name is not None:
            result["name"] = _flut_pack_value(self.name)
        if self.arguments is not None:
            result["arguments"] = _flut_pack_value(self.arguments)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "RouteSettings":
        return RouteSettings(
            name=_flut_unpack_optional_field(data, "name"),
            arguments=_flut_unpack_optional_field(data, "arguments"),
        )


class Navigator:
    @staticmethod
    def push(context, route) -> Future:
        return call_dart_static(
            "Navigator", "push", context._flut_pack(), route._flut_pack()
        )

    @staticmethod
    def pop(context, result=None):
        if result is not None:
            return call_dart_static(
                "Navigator", "pop", context._flut_pack(), _flut_pack_value(result)
            )
        return call_dart_static("Navigator", "pop", context._flut_pack())

    @staticmethod
    def canPop(context) -> bool:
        return call_dart_static("Navigator", "canPop", context._flut_pack())

    @staticmethod
    def pushReplacement(context, route, *, result=None) -> Future:
        if result is not None:
            return call_dart_static(
                "Navigator",
                "pushReplacement",
                context._flut_pack(),
                route._flut_pack(),
                result=_flut_pack_value(result),
            )
        return call_dart_static(
            "Navigator",
            "pushReplacement",
            context._flut_pack(),
            route._flut_pack(),
        )
