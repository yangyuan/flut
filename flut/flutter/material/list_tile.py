from typing import Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class ListTileControlAffinity(FlutEnumObject):
    leading: "ListTileControlAffinity"
    trailing: "ListTileControlAffinity"
    platform: "ListTileControlAffinity"


class ListTile(Widget):
    _flut_type = "ListTile"

    def __init__(
        self,
        *,
        key=None,
        leading: Optional[Widget] = None,
        title: Optional[Widget] = None,
        subtitle: Optional[Widget] = None,
        trailing: Optional[Widget] = None,
        isThreeLine: Optional[bool] = None,
        dense: Optional[bool] = None,
        shape=None,
        selectedColor=None,
        iconColor=None,
        textColor=None,
        titleTextStyle=None,
        subtitleTextStyle=None,
        leadingAndTrailingTextStyle=None,
        contentPadding=None,
        enabled: bool = True,
        onTap=None,
        onLongPress=None,
        mouseCursor=None,
        selected: bool = False,
        focusColor=None,
        hoverColor=None,
        splashColor=None,
        focusNode=None,
        autofocus: bool = False,
        tileColor=None,
        selectedTileColor=None,
        enableFeedback: Optional[bool] = None,
        horizontalTitleGap: Optional[float] = None,
        minVerticalPadding: Optional[float] = None,
        minLeadingWidth: Optional[float] = None,
        minTileHeight: Optional[float] = None,
    ):
        super().__init__(key=key)
        self.leading = leading
        self.title = title
        self.subtitle = subtitle
        self.trailing = trailing
        self.isThreeLine = isThreeLine
        self.dense = dense
        self.shape = shape
        self.selectedColor = selectedColor
        self.iconColor = iconColor
        self.textColor = textColor
        self.titleTextStyle = titleTextStyle
        self.subtitleTextStyle = subtitleTextStyle
        self.leadingAndTrailingTextStyle = leadingAndTrailingTextStyle
        self.contentPadding = contentPadding
        self.enabled = enabled
        self.onTap = onTap
        self.onLongPress = onLongPress
        self.mouseCursor = mouseCursor
        self.selected = selected
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.splashColor = splashColor
        self.focusNode = focusNode
        self.autofocus = autofocus
        self.tileColor = tileColor
        self.selectedTileColor = selectedTileColor
        self.enableFeedback = enableFeedback
        self.horizontalTitleGap = horizontalTitleGap
        self.minVerticalPadding = minVerticalPadding
        self.minLeadingWidth = minLeadingWidth
        self.minTileHeight = minTileHeight

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["enabled"] = _flut_pack_value(self.enabled)
        result["selected"] = _flut_pack_value(self.selected)
        result["autofocus"] = _flut_pack_value(self.autofocus)
        if self.leading is not None:
            result["leading"] = _flut_pack_value(self.leading)
        if self.title is not None:
            result["title"] = _flut_pack_value(self.title)
        if self.subtitle is not None:
            result["subtitle"] = _flut_pack_value(self.subtitle)
        if self.trailing is not None:
            result["trailing"] = _flut_pack_value(self.trailing)
        if self.isThreeLine is not None:
            result["isThreeLine"] = _flut_pack_value(self.isThreeLine)
        if self.dense is not None:
            result["dense"] = _flut_pack_value(self.dense)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.selectedColor is not None:
            result["selectedColor"] = _flut_pack_value(self.selectedColor)
        if self.iconColor is not None:
            result["iconColor"] = _flut_pack_value(self.iconColor)
        if self.textColor is not None:
            result["textColor"] = _flut_pack_value(self.textColor)
        if self.titleTextStyle is not None:
            result["titleTextStyle"] = _flut_pack_value(self.titleTextStyle)
        if self.subtitleTextStyle is not None:
            result["subtitleTextStyle"] = _flut_pack_value(self.subtitleTextStyle)
        if self.leadingAndTrailingTextStyle is not None:
            result["leadingAndTrailingTextStyle"] = _flut_pack_value(
                self.leadingAndTrailingTextStyle
            )
        if self.contentPadding is not None:
            result["contentPadding"] = _flut_pack_value(self.contentPadding)
        if self.onTap is not None:
            result["onTap"] = self._register_action(
                self.onTap, "GestureTapCallback"
            )._flut_pack()
        if self.onLongPress is not None:
            result["onLongPress"] = self._register_action(
                self.onLongPress, "GestureLongPressCallback"
            )._flut_pack()
        if self.mouseCursor is not None:
            result["mouseCursor"] = _flut_pack_value(self.mouseCursor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.splashColor is not None:
            result["splashColor"] = _flut_pack_value(self.splashColor)
        if self.focusNode is not None:
            result["focusNode"] = _flut_pack_value(self.focusNode)
        if self.tileColor is not None:
            result["tileColor"] = _flut_pack_value(self.tileColor)
        if self.selectedTileColor is not None:
            result["selectedTileColor"] = _flut_pack_value(self.selectedTileColor)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.horizontalTitleGap is not None:
            result["horizontalTitleGap"] = _flut_pack_value(self.horizontalTitleGap)
        if self.minVerticalPadding is not None:
            result["minVerticalPadding"] = _flut_pack_value(self.minVerticalPadding)
        if self.minLeadingWidth is not None:
            result["minLeadingWidth"] = _flut_pack_value(self.minLeadingWidth)
        if self.minTileHeight is not None:
            result["minTileHeight"] = _flut_pack_value(self.minTileHeight)
        return result
