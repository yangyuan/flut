from typing import override

from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field


class TextTheme(FlutValueObject):
    _flut_type = "TextTheme"

    def __init__(
        self,
        *,
        displayLarge=None,
        displayMedium=None,
        displaySmall=None,
        headlineLarge=None,
        headlineMedium=None,
        headlineSmall=None,
        titleLarge=None,
        titleMedium=None,
        titleSmall=None,
        bodyLarge=None,
        bodyMedium=None,
        bodySmall=None,
        labelLarge=None,
        labelMedium=None,
        labelSmall=None,
    ):
        super().__init__()
        self.displayLarge = displayLarge
        self.displayMedium = displayMedium
        self.displaySmall = displaySmall
        self.headlineLarge = headlineLarge
        self.headlineMedium = headlineMedium
        self.headlineSmall = headlineSmall
        self.titleLarge = titleLarge
        self.titleMedium = titleMedium
        self.titleSmall = titleSmall
        self.bodyLarge = bodyLarge
        self.bodyMedium = bodyMedium
        self.bodySmall = bodySmall
        self.labelLarge = labelLarge
        self.labelMedium = labelMedium
        self.labelSmall = labelSmall

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.displayLarge is not None:
            result["displayLarge"] = _flut_pack_value(self.displayLarge)
        if self.displayMedium is not None:
            result["displayMedium"] = _flut_pack_value(self.displayMedium)
        if self.displaySmall is not None:
            result["displaySmall"] = _flut_pack_value(self.displaySmall)
        if self.headlineLarge is not None:
            result["headlineLarge"] = _flut_pack_value(self.headlineLarge)
        if self.headlineMedium is not None:
            result["headlineMedium"] = _flut_pack_value(self.headlineMedium)
        if self.headlineSmall is not None:
            result["headlineSmall"] = _flut_pack_value(self.headlineSmall)
        if self.titleLarge is not None:
            result["titleLarge"] = _flut_pack_value(self.titleLarge)
        if self.titleMedium is not None:
            result["titleMedium"] = _flut_pack_value(self.titleMedium)
        if self.titleSmall is not None:
            result["titleSmall"] = _flut_pack_value(self.titleSmall)
        if self.bodyLarge is not None:
            result["bodyLarge"] = _flut_pack_value(self.bodyLarge)
        if self.bodyMedium is not None:
            result["bodyMedium"] = _flut_pack_value(self.bodyMedium)
        if self.bodySmall is not None:
            result["bodySmall"] = _flut_pack_value(self.bodySmall)
        if self.labelLarge is not None:
            result["labelLarge"] = _flut_pack_value(self.labelLarge)
        if self.labelMedium is not None:
            result["labelMedium"] = _flut_pack_value(self.labelMedium)
        if self.labelSmall is not None:
            result["labelSmall"] = _flut_pack_value(self.labelSmall)
        return result

    @staticmethod
    def _flut_unpack(data: dict) -> "TextTheme":
        return TextTheme(
            displayLarge=_flut_unpack_optional_field(data, "displayLarge"),
            displayMedium=_flut_unpack_optional_field(data, "displayMedium"),
            displaySmall=_flut_unpack_optional_field(data, "displaySmall"),
            headlineLarge=_flut_unpack_optional_field(data, "headlineLarge"),
            headlineMedium=_flut_unpack_optional_field(data, "headlineMedium"),
            headlineSmall=_flut_unpack_optional_field(data, "headlineSmall"),
            titleLarge=_flut_unpack_optional_field(data, "titleLarge"),
            titleMedium=_flut_unpack_optional_field(data, "titleMedium"),
            titleSmall=_flut_unpack_optional_field(data, "titleSmall"),
            bodyLarge=_flut_unpack_optional_field(data, "bodyLarge"),
            bodyMedium=_flut_unpack_optional_field(data, "bodyMedium"),
            bodySmall=_flut_unpack_optional_field(data, "bodySmall"),
            labelLarge=_flut_unpack_optional_field(data, "labelLarge"),
            labelMedium=_flut_unpack_optional_field(data, "labelMedium"),
            labelSmall=_flut_unpack_optional_field(data, "labelSmall"),
        )
