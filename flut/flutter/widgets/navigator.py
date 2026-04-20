from typing import Any, Callable, Optional, override

from flut._flut.engine import (
    FlutRealtimeObject,
    FlutValueObject,
    Future,
    call_dart_static,
    pack_static_callable,
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


class NavigatorState(FlutRealtimeObject):
    _flut_type = "NavigatorState"

    def push(self, route) -> Future:
        return self._flut_call("push", route)

    def pushReplacement(self, newRoute, *, result=None) -> Future:
        if result is not None:
            return self._flut_call("pushReplacement", newRoute, result=result)
        return self._flut_call("pushReplacement", newRoute)

    def pushAndRemoveUntil(self, newRoute, predicate: Callable[[Any], bool]) -> Future:
        return self._flut_call(
            "pushAndRemoveUntil",
            newRoute,
            self._register_action(predicate, "RoutePredicate"),
        )

    def pushNamed(self, routeName: str, *, arguments: Optional[Any] = None) -> Future:
        if arguments is not None:
            return self._flut_call("pushNamed", routeName, arguments=arguments)
        return self._flut_call("pushNamed", routeName)

    def pushReplacementNamed(
        self,
        routeName: str,
        *,
        result: Optional[Any] = None,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if result is not None:
            kwargs["result"] = result
        if arguments is not None:
            kwargs["arguments"] = arguments
        return self._flut_call("pushReplacementNamed", routeName, **kwargs)

    def pushNamedAndRemoveUntil(
        self,
        newRouteName: str,
        predicate: Callable[[Any], bool],
        *,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if arguments is not None:
            kwargs["arguments"] = arguments
        return self._flut_call(
            "pushNamedAndRemoveUntil",
            newRouteName,
            self._register_action(predicate, "RoutePredicate"),
            **kwargs,
        )

    def popAndPushNamed(
        self,
        routeName: str,
        *,
        result: Optional[Any] = None,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if result is not None:
            kwargs["result"] = result
        if arguments is not None:
            kwargs["arguments"] = arguments
        return self._flut_call("popAndPushNamed", routeName, **kwargs)

    def pop(self, result=None) -> None:
        if result is not None:
            self._flut_call("pop", result)
        else:
            self._flut_call("pop")

    def maybePop(self, result=None) -> Future:
        if result is not None:
            return self._flut_call("maybePop", result)
        return self._flut_call("maybePop")

    def popUntil(self, predicate: Callable[[Any], bool]) -> None:
        self._flut_call(
            "popUntil",
            self._register_action(predicate, "RoutePredicate"),
        )

    def canPop(self) -> bool:
        return bool(self._flut_call("canPop"))

    def replace(self, *, oldRoute, newRoute) -> None:
        self._flut_call("replace", oldRoute=oldRoute, newRoute=newRoute)

    def replaceRouteBelow(self, *, anchorRoute, newRoute) -> None:
        self._flut_call("replaceRouteBelow", anchorRoute=anchorRoute, newRoute=newRoute)

    def removeRoute(self, route) -> None:
        self._flut_call("removeRoute", route)

    def removeRouteBelow(self, anchorRoute) -> None:
        self._flut_call("removeRouteBelow", anchorRoute)

    def finalizeRoute(self, route) -> None:
        self._flut_call("finalizeRoute", route)


class Navigator:
    @staticmethod
    def of(context, *, rootNavigator: bool = False) -> NavigatorState:
        return call_dart_static(
            "Navigator", "of", context._flut_pack(), rootNavigator=rootNavigator
        )

    @staticmethod
    def maybeOf(context, *, rootNavigator: bool = False) -> Optional[NavigatorState]:
        return call_dart_static(
            "Navigator",
            "maybeOf",
            context._flut_pack(),
            rootNavigator=rootNavigator,
        )

    @staticmethod
    def push(context, route) -> Future:
        return call_dart_static(
            "Navigator", "push", context._flut_pack(), _flut_pack_value(route)
        )

    @staticmethod
    def pushReplacement(context, newRoute, *, result=None) -> Future:
        kwargs: dict[str, Any] = {}
        if result is not None:
            kwargs["result"] = _flut_pack_value(result)
        return call_dart_static(
            "Navigator",
            "pushReplacement",
            context._flut_pack(),
            _flut_pack_value(newRoute),
            **kwargs,
        )

    @staticmethod
    def pushAndRemoveUntil(
        context, newRoute, predicate: Callable[[Any], bool]
    ) -> Future:
        return call_dart_static(
            "Navigator",
            "pushAndRemoveUntil",
            context._flut_pack(),
            _flut_pack_value(newRoute),
            pack_static_callable(predicate, "RoutePredicate"),
        )

    @staticmethod
    def pushNamed(
        context, routeName: str, *, arguments: Optional[Any] = None
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if arguments is not None:
            kwargs["arguments"] = _flut_pack_value(arguments)
        return call_dart_static(
            "Navigator", "pushNamed", context._flut_pack(), routeName, **kwargs
        )

    @staticmethod
    def pushReplacementNamed(
        context,
        routeName: str,
        *,
        result: Optional[Any] = None,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if result is not None:
            kwargs["result"] = _flut_pack_value(result)
        if arguments is not None:
            kwargs["arguments"] = _flut_pack_value(arguments)
        return call_dart_static(
            "Navigator",
            "pushReplacementNamed",
            context._flut_pack(),
            routeName,
            **kwargs,
        )

    @staticmethod
    def pushNamedAndRemoveUntil(
        context,
        newRouteName: str,
        predicate: Callable[[Any], bool],
        *,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if arguments is not None:
            kwargs["arguments"] = _flut_pack_value(arguments)
        return call_dart_static(
            "Navigator",
            "pushNamedAndRemoveUntil",
            context._flut_pack(),
            newRouteName,
            pack_static_callable(predicate, "RoutePredicate"),
            **kwargs,
        )

    @staticmethod
    def popAndPushNamed(
        context,
        routeName: str,
        *,
        result: Optional[Any] = None,
        arguments: Optional[Any] = None,
    ) -> Future:
        kwargs: dict[str, Any] = {}
        if result is not None:
            kwargs["result"] = _flut_pack_value(result)
        if arguments is not None:
            kwargs["arguments"] = _flut_pack_value(arguments)
        return call_dart_static(
            "Navigator",
            "popAndPushNamed",
            context._flut_pack(),
            routeName,
            **kwargs,
        )

    @staticmethod
    def pop(context, result=None) -> None:
        if result is not None:
            call_dart_static(
                "Navigator", "pop", context._flut_pack(), _flut_pack_value(result)
            )
        else:
            call_dart_static("Navigator", "pop", context._flut_pack())

    @staticmethod
    def maybePop(context, result=None) -> Future:
        if result is not None:
            return call_dart_static(
                "Navigator",
                "maybePop",
                context._flut_pack(),
                _flut_pack_value(result),
            )
        return call_dart_static("Navigator", "maybePop", context._flut_pack())

    @staticmethod
    def popUntil(context, predicate: Callable[[Any], bool]) -> None:
        call_dart_static(
            "Navigator",
            "popUntil",
            context._flut_pack(),
            pack_static_callable(predicate, "RoutePredicate"),
        )

    @staticmethod
    def canPop(context) -> bool:
        return bool(call_dart_static("Navigator", "canPop", context._flut_pack()))

    @staticmethod
    def replace(context, *, oldRoute, newRoute) -> None:
        call_dart_static(
            "Navigator",
            "replace",
            context._flut_pack(),
            oldRoute=_flut_pack_value(oldRoute),
            newRoute=_flut_pack_value(newRoute),
        )

    @staticmethod
    def replaceRouteBelow(context, *, anchorRoute, newRoute) -> None:
        call_dart_static(
            "Navigator",
            "replaceRouteBelow",
            context._flut_pack(),
            anchorRoute=_flut_pack_value(anchorRoute),
            newRoute=_flut_pack_value(newRoute),
        )

    @staticmethod
    def removeRoute(context, route) -> None:
        call_dart_static(
            "Navigator",
            "removeRoute",
            context._flut_pack(),
            _flut_pack_value(route),
        )

    @staticmethod
    def removeRouteBelow(context, anchorRoute) -> None:
        call_dart_static(
            "Navigator",
            "removeRouteBelow",
            context._flut_pack(),
            _flut_pack_value(anchorRoute),
        )
