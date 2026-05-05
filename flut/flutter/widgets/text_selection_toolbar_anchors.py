from typing import Optional, override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field
from flut.dart.ui import Offset


class TextSelectionToolbarAnchors(FlutValueObject):
    _flut_type = "TextSelectionToolbarAnchors"

    def __init__(
        self,
        *,
        primaryAnchor: Offset,
        secondaryAnchor: Optional[Offset] = None,
    ) -> None:
        super().__init__()
        self.primaryAnchor = primaryAnchor
        self.secondaryAnchor = secondaryAnchor

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSelectionToolbarAnchors":
        return TextSelectionToolbarAnchors(
            primaryAnchor=_flut_unpack_required_field(data, "primaryAnchor"),
            secondaryAnchor=_flut_unpack_optional_field(data, "secondaryAnchor"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["primaryAnchor"] = _flut_pack_value(self.primaryAnchor)
        if self.secondaryAnchor is not None:
            result["secondaryAnchor"] = _flut_pack_value(self.secondaryAnchor)
        return result
