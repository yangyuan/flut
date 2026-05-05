from typing import Callable, override

from flut._flut.engine import (
    FlutRealtimeObject,
    FlutValueObject,
    _flut_pack_value,
    call_dart_static,
    wrap_widget_builder,
)
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class MagnifierInfo(FlutValueObject):
    _flut_type = "MagnifierInfo"

    def __init__(
        self,
        *,
        globalGesturePosition,
        caretRect,
        fieldBounds,
        currentLineBoundaries,
    ) -> None:
        super().__init__()
        self.globalGesturePosition = globalGesturePosition
        self.caretRect = caretRect
        self.fieldBounds = fieldBounds
        self.currentLineBoundaries = currentLineBoundaries

    @staticmethod
    def _flut_unpack(data: dict) -> "MagnifierInfo":
        return MagnifierInfo(
            globalGesturePosition=_flut_unpack_required_field(
                data, "globalGesturePosition"
            ),
            caretRect=_flut_unpack_required_field(data, "caretRect"),
            fieldBounds=_flut_unpack_required_field(data, "fieldBounds"),
            currentLineBoundaries=_flut_unpack_required_field(
                data, "currentLineBoundaries"
            ),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["globalGesturePosition"] = _flut_pack_value(self.globalGesturePosition)
        result["caretRect"] = _flut_pack_value(self.caretRect)
        result["fieldBounds"] = _flut_pack_value(self.fieldBounds)
        result["currentLineBoundaries"] = _flut_pack_value(self.currentLineBoundaries)
        return result


class MagnifierController(FlutRealtimeObject):
    _flut_type = "MagnifierController"

    def __init__(self, *, animationController=None) -> None:
        super().__init__()
        props = {}
        if animationController is not None:
            props["animationController"] = _flut_pack_value(animationController)
        self._flut_create(props=props or None)

    @property
    def animationController(self):
        return self._flut_get("animationController")

    @animationController.setter
    def animationController(self, value) -> None:
        self._flut_set("animationController", value)

    @property
    def overlayEntry(self):
        return self._flut_get("overlayEntry")

    @property
    def shown(self) -> bool:
        return bool(self._flut_get("shown"))

    def show(self, *, context, builder, debugRequiredFor=None, below=None):
        builder_callable = self._register_init_build_action(
            wrap_widget_builder(builder)
        )
        kwargs = {"context": context, "builder": builder_callable}
        if debugRequiredFor is not None:
            kwargs["debugRequiredFor"] = debugRequiredFor
        if below is not None:
            kwargs["below"] = below
        return self._flut_call("show", **kwargs)

    def hide(self, *, removeFromOverlay: bool = True):
        return self._flut_call("hide", removeFromOverlay=removeFromOverlay)

    def removeFromOverlay(self) -> None:
        self._flut_call("removeFromOverlay")

    @staticmethod
    def shiftWithinBounds(*, rect, bounds):
        return call_dart_static(
            "MagnifierController", "shiftWithinBounds", rect=rect, bounds=bounds
        )


class _TextMagnifierConfiguration(FlutValueObject):
    _flut_type = "TextMagnifierConfiguration"

    def __init__(
        self,
        *,
        magnifierBuilder: Callable | None = None,
        shouldDisplayHandlesInMagnifier: bool = True,
    ) -> None:
        super().__init__()
        self.magnifierBuilder = magnifierBuilder
        self.shouldDisplayHandlesInMagnifier = shouldDisplayHandlesInMagnifier

    @staticmethod
    def _flut_unpack(data: dict) -> "_TextMagnifierConfiguration":
        return _TextMagnifierConfiguration(
            magnifierBuilder=_flut_unpack_optional_field(data, "magnifierBuilder"),
            shouldDisplayHandlesInMagnifier=_flut_unpack_required_field(
                data, "shouldDisplayHandlesInMagnifier"
            ),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self.magnifierBuilder is not None:
            result["magnifierBuilder"] = self._register_action(
                self.magnifierBuilder, "MagnifierBuilder"
            )._flut_pack()
        result["shouldDisplayHandlesInMagnifier"] = _flut_pack_value(
            self.shouldDisplayHandlesInMagnifier
        )
        return result


class TextMagnifierConfiguration(_TextMagnifierConfiguration):
    disabled = _TextMagnifierConfiguration()
