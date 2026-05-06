from typing import Callable, Optional, override

from flut._flut.engine import FlutAbstractObject, FlutEnumObject
from flut.dart.ui import Offset, Rect, Size
from flut.flutter.rendering.selection import TextSelectionHandleType
from flut.flutter.widgets.framework import BuildContext, Widget


class ClipboardStatus(FlutEnumObject):
    pasteable: "ClipboardStatus"
    unknown: "ClipboardStatus"
    notPasteable: "ClipboardStatus"


class TextSelectionControls(FlutAbstractObject):
    _flut_type = "TextSelectionControls"

    def buildHandle(
        self,
        context: BuildContext,
        type: TextSelectionHandleType,
        textLineHeight: float,
        onTap: Optional[Callable[[], None]] = None,
    ) -> Widget:
        raise NotImplementedError

    def getHandleAnchor(
        self, type: TextSelectionHandleType, textLineHeight: float
    ) -> Offset:
        raise NotImplementedError

    def buildToolbar(
        self,
        context: BuildContext,
        globalEditableRegion: Rect,
        textLineHeight: float,
        selectionMidpoint: Offset,
        endpoints: list["TextSelectionPoint"],
        delegate: "TextSelectionDelegate",
        clipboardStatus: Optional["ValueListenable[ClipboardStatus]"],
        lastSecondaryTapDownPosition: Optional[Offset],
    ) -> Widget:
        raise NotImplementedError

    def getHandleSize(self, textLineHeight: float) -> Size:
        raise NotImplementedError

    def canCut(self, delegate: "TextSelectionDelegate") -> bool:
        raise NotImplementedError

    def canCopy(self, delegate: "TextSelectionDelegate") -> bool:
        raise NotImplementedError

    def canPaste(self, delegate: "TextSelectionDelegate") -> bool:
        raise NotImplementedError

    def canSelectAll(self, delegate: "TextSelectionDelegate") -> bool:
        raise NotImplementedError

    def handleCut(self, delegate: "TextSelectionDelegate") -> None:
        raise NotImplementedError

    def handleCopy(self, delegate: "TextSelectionDelegate") -> None:
        raise NotImplementedError

    async def handlePaste(self, delegate: "TextSelectionDelegate") -> None:
        raise NotImplementedError

    def handleSelectAll(self, delegate: "TextSelectionDelegate") -> None:
        raise NotImplementedError

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSelectionControls":
        raise NotImplementedError(
            "TextSelectionControls has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "TextSelectionControls has no concrete wire form. Pass a concrete subtype."
        )


class TextSelectionHandleControls(TextSelectionControls):
    _flut_type = "TextSelectionHandleControls"

    @staticmethod
    def _flut_unpack(data: dict) -> "TextSelectionHandleControls":
        raise NotImplementedError(
            "TextSelectionHandleControls has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "TextSelectionHandleControls has no concrete wire form. Pass a concrete subtype."
        )


class EmptyTextSelectionControls(TextSelectionControls):
    _flut_type = "EmptyTextSelectionControls"

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _flut_unpack(data: dict) -> "EmptyTextSelectionControls":
        return EmptyTextSelectionControls()

    @override
    def _flut_pack(self) -> dict[str, object]:
        return self._flut_base_props()


emptyTextSelectionControls = EmptyTextSelectionControls()
