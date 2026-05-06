from typing import Callable, Optional, override

from flut._flut.engine import (
    FlutEnumObject,
    FlutValueObject,
    _flut_pack_value,
    pack_static_callable,
)
from flut._flut.runtime import (
    _flut_unpack_optional_field,
    _flut_unpack_required_field,
)


class ContextMenuButtonType(FlutEnumObject):
    cut: "ContextMenuButtonType"
    copy: "ContextMenuButtonType"
    paste: "ContextMenuButtonType"
    selectAll: "ContextMenuButtonType"
    delete: "ContextMenuButtonType"
    lookUp: "ContextMenuButtonType"
    searchWeb: "ContextMenuButtonType"
    share: "ContextMenuButtonType"
    liveTextInput: "ContextMenuButtonType"
    custom: "ContextMenuButtonType"


class ContextMenuButtonItem(FlutValueObject):
    _flut_type = "ContextMenuButtonItem"

    def __init__(
        self,
        *,
        onPressed: Optional[Callable[[], None]] = None,
        type: ContextMenuButtonType = ContextMenuButtonType.custom,
        label: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.onPressed = onPressed
        self.type = type
        self.label = label

    @staticmethod
    def _flut_unpack(data: dict) -> "ContextMenuButtonItem":
        return ContextMenuButtonItem(
            onPressed=_flut_unpack_optional_field(data, "onPressed"),
            type=_flut_unpack_required_field(data, "type"),
            label=_flut_unpack_optional_field(data, "label"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self.onPressed is not None:
            result["onPressed"] = pack_static_callable(self.onPressed, "VoidCallback")
        result["type"] = _flut_pack_value(self.type)
        if self.label is not None:
            result["label"] = _flut_pack_value(self.label)
        return result
