from typing import Optional, override

from flut._flut.engine import (
    FlutAbstractObject,
    call_dart_static,
    named_constructor,
    _flut_pack_value,
)
from flut.flutter.widgets.framework import Widget


class SelectionRegistrar(FlutAbstractObject):
    _flut_type = "SelectionRegistrar"

    def add(self, selectable: "Selectable") -> None:
        raise NotImplementedError

    def remove(self, selectable: "Selectable") -> None:
        raise NotImplementedError

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionRegistrar":
        raise NotImplementedError(
            "SelectionRegistrar has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "SelectionRegistrar has no concrete wire form. Pass a concrete subtype."
        )


class SelectionContainerDelegate(SelectionRegistrar):
    _flut_type = "SelectionContainerDelegate"

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionContainerDelegate":
        raise NotImplementedError(
            "SelectionContainerDelegate has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "SelectionContainerDelegate has no concrete wire form. Pass a concrete subtype."
        )


class MultiSelectableSelectionContainerDelegate(SelectionContainerDelegate):
    _flut_type = "MultiSelectableSelectionContainerDelegate"

    @staticmethod
    def _flut_unpack(data: dict) -> "MultiSelectableSelectionContainerDelegate":
        raise NotImplementedError(
            "MultiSelectableSelectionContainerDelegate has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "MultiSelectableSelectionContainerDelegate has no concrete wire form. Pass a concrete subtype."
        )


class StaticSelectionContainerDelegate(MultiSelectableSelectionContainerDelegate):
    _flut_type = "StaticSelectionContainerDelegate"

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _flut_unpack(data: dict) -> "StaticSelectionContainerDelegate":
        return StaticSelectionContainerDelegate()

    @override
    def _flut_pack(self) -> dict[str, object]:
        return self._flut_base_props()


class SelectionContainer(Widget):
    _flut_type = "SelectionContainer"

    def __init__(
        self,
        *,
        delegate: "SelectionContainerDelegate",
        child: Widget,
        key: Optional["Key"] = None,
        registrar: Optional["SelectionRegistrar"] = None,
    ) -> None:
        super().__init__(key=key)
        self.registrar = registrar
        self.delegate = delegate
        self.child = child

    @named_constructor
    def disabled(
        cls, *, child: Widget, key: Optional["Key"] = None
    ) -> "SelectionContainer":
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.registrar = None
        instance.delegate = None
        instance.child = child
        return instance

    @staticmethod
    def maybeOf(context: "BuildContext") -> Optional[SelectionRegistrar]:
        return call_dart_static("SelectionContainer", "maybeOf", context._flut_pack())

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self._flut_init != "disabled":
            if self.registrar is not None:
                result["registrar"] = _flut_pack_value(self.registrar)
            result["delegate"] = _flut_pack_value(self.delegate)
        result["child"] = _flut_pack_value(self.child)
        return result


class SelectionRegistrarScope(Widget):
    _flut_type = "SelectionRegistrarScope"

    def __init__(
        self,
        *,
        registrar: SelectionRegistrar,
        child: Widget,
        key: Optional["Key"] = None,
    ) -> None:
        super().__init__(key=key)
        self.registrar = registrar
        self.child = child

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["registrar"] = _flut_pack_value(self.registrar)
        result["child"] = _flut_pack_value(self.child)
        return result
