from typing import override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field


class TextSpan(FlutValueObject):
    _flut_type = "TextSpan"

    def __init__(
        self,
        text=None,
        children=None,
        style=None,
        recognizer=None,
        mouseCursor=None,
        onEnter=None,
        onExit=None,
        semanticsLabel=None,
        semanticsIdentifier=None,
        locale=None,
        spellOut=None,
    ):
        super().__init__()
        self.text = text
        self.children = children
        self.style = style
        self.recognizer = recognizer
        self.mouseCursor = mouseCursor
        self.onEnter = onEnter
        self.onExit = onExit
        self.semanticsLabel = semanticsLabel
        self.semanticsIdentifier = semanticsIdentifier
        self.locale = locale
        self.spellOut = spellOut

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSpan":
        return TextSpan(
            text=_flut_unpack_optional_field(data, "text"),
            children=_flut_unpack_optional_field(data, "children"),
            style=_flut_unpack_optional_field(data, "style"),
            recognizer=_flut_unpack_optional_field(data, "recognizer"),
            mouseCursor=_flut_unpack_optional_field(data, "mouseCursor"),
            semanticsLabel=_flut_unpack_optional_field(data, "semanticsLabel"),
            semanticsIdentifier=_flut_unpack_optional_field(
                data, "semanticsIdentifier"
            ),
            locale=_flut_unpack_optional_field(data, "locale"),
            spellOut=_flut_unpack_optional_field(data, "spellOut"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.text is not None:
            result["text"] = _flut_pack_value(self.text)
        if self.children is not None:
            result["children"] = _flut_pack_value(self.children)
        if self.style is not None:
            result["style"] = _flut_pack_value(self.style)
        if self.recognizer is not None:
            result["recognizer"] = _flut_pack_value(self.recognizer)
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.onEnter is not None:
            result["onEnter"] = self._register_action(
                self.onEnter, "PointerEnterEventListener"
            )._flut_pack()
        if self.onExit is not None:
            result["onExit"] = self._register_action(
                self.onExit, "PointerExitEventListener"
            )._flut_pack()
        if self.semanticsLabel is not None:
            result["semanticsLabel"] = _flut_pack_value(self.semanticsLabel)
        if self.semanticsIdentifier is not None:
            result["semanticsIdentifier"] = _flut_pack_value(self.semanticsIdentifier)
        if self.locale is not None:
            result["locale"] = _flut_pack_value(self.locale)
        if self.spellOut is not None:
            result["spellOut"] = _flut_pack_value(self.spellOut)
        return result
