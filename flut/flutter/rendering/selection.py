from typing import override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class SelectionResult(FlutEnumObject):
    next: "SelectionResult"
    previous: "SelectionResult"
    end: "SelectionResult"
    pending: "SelectionResult"
    none: "SelectionResult"


class SelectionEventType(FlutEnumObject):
    startEdgeUpdate: "SelectionEventType"
    endEdgeUpdate: "SelectionEventType"
    clear: "SelectionEventType"
    selectAll: "SelectionEventType"
    selectWord: "SelectionEventType"
    selectParagraph: "SelectionEventType"
    granularlyExtendSelection: "SelectionEventType"
    directionallyExtendSelection: "SelectionEventType"


class TextGranularity(FlutEnumObject):
    character: "TextGranularity"
    word: "TextGranularity"
    paragraph: "TextGranularity"
    line: "TextGranularity"
    document: "TextGranularity"


class SelectionExtendDirection(FlutEnumObject):
    previousLine: "SelectionExtendDirection"
    nextLine: "SelectionExtendDirection"
    forward: "SelectionExtendDirection"
    backward: "SelectionExtendDirection"


class TextSelectionHandleType(FlutEnumObject):
    left: "TextSelectionHandleType"
    right: "TextSelectionHandleType"
    collapsed: "TextSelectionHandleType"


class SelectedContent(FlutValueObject):
    _flut_type = "SelectedContent"

    def __init__(self, *, plainText: str) -> None:
        super().__init__()
        self.plainText = plainText

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectedContent":
        return SelectedContent(
            plainText=_flut_unpack_required_field(data, "plainText"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["plainText"] = _flut_pack_value(self.plainText)
        return result


class SelectedContentRange(FlutValueObject):
    _flut_type = "SelectedContentRange"

    def __init__(self, *, startOffset: int, endOffset: int) -> None:
        super().__init__()
        self.startOffset = startOffset
        self.endOffset = endOffset

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectedContentRange":
        return SelectedContentRange(
            startOffset=_flut_unpack_required_field(data, "startOffset"),
            endOffset=_flut_unpack_required_field(data, "endOffset"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["startOffset"] = _flut_pack_value(self.startOffset)
        result["endOffset"] = _flut_pack_value(self.endOffset)
        return result


class SelectionPoint(FlutValueObject):
    _flut_type = "SelectionPoint"

    def __init__(self, *, localPosition, lineHeight: float, handleType) -> None:
        super().__init__()
        self.localPosition = localPosition
        self.lineHeight = lineHeight
        self.handleType = handleType

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionPoint":
        return SelectionPoint(
            localPosition=_flut_unpack_required_field(data, "localPosition"),
            lineHeight=_flut_unpack_required_field(data, "lineHeight"),
            handleType=_flut_unpack_required_field(data, "handleType"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["localPosition"] = _flut_pack_value(self.localPosition)
        result["lineHeight"] = _flut_pack_value(self.lineHeight)
        result["handleType"] = _flut_pack_value(self.handleType)
        return result


class SelectionGeometry(FlutValueObject):
    _flut_type = "SelectionGeometry"

    def __init__(
        self,
        *,
        status,
        hasContent: bool,
        startSelectionPoint: SelectionPoint | None = None,
        endSelectionPoint: SelectionPoint | None = None,
        selectionRects: list["Rect"] = [],
    ) -> None:
        super().__init__()
        self.startSelectionPoint = startSelectionPoint
        self.endSelectionPoint = endSelectionPoint
        self.selectionRects = selectionRects
        self.status = status
        self.hasContent = hasContent

    @property
    def hasSelection(self) -> bool:
        return self.status != SelectionStatus.none

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionGeometry":
        return SelectionGeometry(
            startSelectionPoint=_flut_unpack_optional_field(
                data, "startSelectionPoint"
            ),
            endSelectionPoint=_flut_unpack_optional_field(data, "endSelectionPoint"),
            selectionRects=_flut_unpack_required_field(data, "selectionRects"),
            status=_flut_unpack_required_field(data, "status"),
            hasContent=_flut_unpack_required_field(data, "hasContent"),
        )

    def copyWith(
        self,
        *,
        startSelectionPoint: SelectionPoint | None = None,
        endSelectionPoint: SelectionPoint | None = None,
        selectionRects: list | None = None,
        status=None,
        hasContent: bool | None = None,
    ) -> "SelectionGeometry":
        return SelectionGeometry(
            startSelectionPoint=startSelectionPoint or self.startSelectionPoint,
            endSelectionPoint=endSelectionPoint or self.endSelectionPoint,
            selectionRects=selectionRects or self.selectionRects,
            status=status or self.status,
            hasContent=self.hasContent if hasContent is None else hasContent,
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        if self.startSelectionPoint is not None:
            result["startSelectionPoint"] = _flut_pack_value(self.startSelectionPoint)
        if self.endSelectionPoint is not None:
            result["endSelectionPoint"] = _flut_pack_value(self.endSelectionPoint)
        result["selectionRects"] = _flut_pack_value(self.selectionRects)
        result["status"] = _flut_pack_value(self.status)
        result["hasContent"] = _flut_pack_value(self.hasContent)
        return result


class SelectionEvent(FlutValueObject):
    _flut_type = "SelectionEvent"

    def __init__(self, type) -> None:
        super().__init__()
        self.type = type

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionEvent":
        raise NotImplementedError(
            "SelectionEvent has no concrete wire form. Pass a concrete subtype."
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        raise NotImplementedError(
            "SelectionEvent has no concrete wire form. Pass a concrete subtype."
        )


class SelectAllSelectionEvent(SelectionEvent):
    _flut_type = "SelectAllSelectionEvent"

    def __init__(self) -> None:
        super().__init__(SelectionEventType.selectAll)

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectAllSelectionEvent":
        return SelectAllSelectionEvent()

    @override
    def _flut_pack(self) -> dict[str, object]:
        return self._flut_base_props()


class ClearSelectionEvent(SelectionEvent):
    _flut_type = "ClearSelectionEvent"

    def __init__(self) -> None:
        super().__init__(SelectionEventType.clear)

    @staticmethod
    def _flut_unpack(data: dict) -> "ClearSelectionEvent":
        return ClearSelectionEvent()

    @override
    def _flut_pack(self) -> dict[str, object]:
        return self._flut_base_props()


class SelectWordSelectionEvent(SelectionEvent):
    _flut_type = "SelectWordSelectionEvent"

    def __init__(self, *, globalPosition) -> None:
        super().__init__(SelectionEventType.selectWord)
        self.globalPosition = globalPosition

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectWordSelectionEvent":
        return SelectWordSelectionEvent(
            globalPosition=_flut_unpack_required_field(data, "globalPosition")
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        return result


class SelectParagraphSelectionEvent(SelectionEvent):
    _flut_type = "SelectParagraphSelectionEvent"

    def __init__(self, *, globalPosition, absorb: bool = False) -> None:
        super().__init__(SelectionEventType.selectParagraph)
        self.globalPosition = globalPosition
        self.absorb = absorb

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectParagraphSelectionEvent":
        return SelectParagraphSelectionEvent(
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            absorb=_flut_unpack_required_field(data, "absorb"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["absorb"] = _flut_pack_value(self.absorb)
        return result


class SelectionEdgeUpdateEvent(SelectionEvent):
    _flut_type = "SelectionEdgeUpdateEvent"

    def __init__(self, *, type, globalPosition, granularity=None) -> None:
        super().__init__(type)
        self.globalPosition = globalPosition
        self.granularity = granularity or TextGranularity.character

    @staticmethod
    def forStart(*, globalPosition, granularity=None) -> "SelectionEdgeUpdateEvent":
        return SelectionEdgeUpdateEvent(
            type=SelectionEventType.startEdgeUpdate,
            globalPosition=globalPosition,
            granularity=granularity,
        )

    @staticmethod
    def forEnd(*, globalPosition, granularity=None) -> "SelectionEdgeUpdateEvent":
        return SelectionEdgeUpdateEvent(
            type=SelectionEventType.endEdgeUpdate,
            globalPosition=globalPosition,
            granularity=granularity,
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "SelectionEdgeUpdateEvent":
        return SelectionEdgeUpdateEvent(
            type=_flut_unpack_required_field(data, "type"),
            globalPosition=_flut_unpack_required_field(data, "globalPosition"),
            granularity=_flut_unpack_required_field(data, "granularity"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["type"] = _flut_pack_value(self.type)
        result["globalPosition"] = _flut_pack_value(self.globalPosition)
        result["granularity"] = _flut_pack_value(self.granularity)
        return result


class GranularlyExtendSelectionEvent(SelectionEvent):
    _flut_type = "GranularlyExtendSelectionEvent"

    def __init__(self, *, forward: bool, isEnd: bool, granularity) -> None:
        super().__init__(SelectionEventType.granularlyExtendSelection)
        self.forward = forward
        self.isEnd = isEnd
        self.granularity = granularity

    @staticmethod
    def _flut_unpack(data: dict) -> "GranularlyExtendSelectionEvent":
        return GranularlyExtendSelectionEvent(
            forward=_flut_unpack_required_field(data, "forward"),
            isEnd=_flut_unpack_required_field(data, "isEnd"),
            granularity=_flut_unpack_required_field(data, "granularity"),
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["forward"] = _flut_pack_value(self.forward)
        result["isEnd"] = _flut_pack_value(self.isEnd)
        result["granularity"] = _flut_pack_value(self.granularity)
        return result


class DirectionallyExtendSelectionEvent(SelectionEvent):
    _flut_type = "DirectionallyExtendSelectionEvent"

    def __init__(self, *, dx: float, isEnd: bool, direction) -> None:
        super().__init__(SelectionEventType.directionallyExtendSelection)
        self.dx = dx
        self.isEnd = isEnd
        self.direction = direction

    @staticmethod
    def _flut_unpack(data: dict) -> "DirectionallyExtendSelectionEvent":
        return DirectionallyExtendSelectionEvent(
            dx=_flut_unpack_required_field(data, "dx"),
            isEnd=_flut_unpack_required_field(data, "isEnd"),
            direction=_flut_unpack_required_field(data, "direction"),
        )

    def copyWith(
        self, *, dx: float | None = None, isEnd: bool | None = None, direction=None
    ) -> "DirectionallyExtendSelectionEvent":
        return DirectionallyExtendSelectionEvent(
            dx=self.dx if dx is None else dx,
            isEnd=self.isEnd if isEnd is None else isEnd,
            direction=direction or self.direction,
        )

    @override
    def _flut_pack(self) -> dict[str, object]:
        result = self._flut_base_props()
        result["dx"] = _flut_pack_value(self.dx)
        result["isEnd"] = _flut_pack_value(self.isEnd)
        result["direction"] = _flut_pack_value(self.direction)
        return result


class SelectionStatus(FlutEnumObject):
    uncollapsed: "SelectionStatus"
    collapsed: "SelectionStatus"
    none: "SelectionStatus"
