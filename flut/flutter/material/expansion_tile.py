from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.dart.ui import Color
from flut.flutter.painting.alignment import Alignment
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.rendering.flex import CrossAxisAlignment
from flut.flutter.animation.animation_style import AnimationStyle
from flut.flutter.widgets.expansible import ExpansibleController
from flut.flutter.widgets.framework import Widget


class ExpansionTile(Widget):
    _flut_type = "ExpansionTile"

    def __init__(
        self,
        *,
        key=None,
        leading: Optional[Widget] = None,
        title: Widget,
        subtitle: Optional[Widget] = None,
        onExpansionChanged: Optional[Callable[[bool], None]] = None,
        trailing: Optional[Widget] = None,
        showTrailingIcon: bool = True,
        initiallyExpanded: bool = False,
        maintainState: bool = False,
        tilePadding: Optional[EdgeInsets] = None,
        expandedCrossAxisAlignment: Optional[CrossAxisAlignment] = None,
        expandedAlignment: Optional[Alignment] = None,
        childrenPadding: Optional[EdgeInsets] = None,
        backgroundColor: Optional[Color] = None,
        collapsedBackgroundColor: Optional[Color] = None,
        textColor: Optional[Color] = None,
        collapsedTextColor: Optional[Color] = None,
        iconColor: Optional[Color] = None,
        collapsedIconColor: Optional[Color] = None,
        shape=None,
        collapsedShape=None,
        clipBehavior=None,
        controlAffinity=None,
        controller: Optional[ExpansibleController] = None,
        dense: Optional[bool] = None,
        splashColor: Optional[Color] = None,
        visualDensity=None,
        minTileHeight: Optional[float] = None,
        enableFeedback: Optional[bool] = True,
        enabled: bool = True,
        expansionAnimationStyle: Optional[AnimationStyle] = None,
        internalAddSemanticForOnTap: bool = False,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.leading = leading
        self.title = title
        self.subtitle = subtitle
        self.onExpansionChanged = onExpansionChanged
        self.trailing = trailing
        self.showTrailingIcon = showTrailingIcon
        self.initiallyExpanded = initiallyExpanded
        self.maintainState = maintainState
        self.tilePadding = tilePadding
        self.expandedCrossAxisAlignment = expandedCrossAxisAlignment
        self.expandedAlignment = expandedAlignment
        self.childrenPadding = childrenPadding
        self.backgroundColor = backgroundColor
        self.collapsedBackgroundColor = collapsedBackgroundColor
        self.textColor = textColor
        self.collapsedTextColor = collapsedTextColor
        self.iconColor = iconColor
        self.collapsedIconColor = collapsedIconColor
        self.shape = shape
        self.collapsedShape = collapsedShape
        self.clipBehavior = clipBehavior
        self.controlAffinity = controlAffinity
        self.controller = controller
        self.dense = dense
        self.splashColor = splashColor
        self.visualDensity = visualDensity
        self.minTileHeight = minTileHeight
        self.enableFeedback = enableFeedback
        self.enabled = enabled
        self.expansionAnimationStyle = expansionAnimationStyle
        self.internalAddSemanticForOnTap = internalAddSemanticForOnTap
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["title"] = _flut_pack_value(self.title)
        result["children"] = _flut_pack_value(self.children)
        result["showTrailingIcon"] = _flut_pack_value(self.showTrailingIcon)
        result["initiallyExpanded"] = _flut_pack_value(self.initiallyExpanded)
        result["maintainState"] = _flut_pack_value(self.maintainState)
        result["enabled"] = _flut_pack_value(self.enabled)
        result["internalAddSemanticForOnTap"] = _flut_pack_value(
            self.internalAddSemanticForOnTap
        )
        if self.leading is not None:
            result["leading"] = _flut_pack_value(self.leading)
        if self.subtitle is not None:
            result["subtitle"] = _flut_pack_value(self.subtitle)
        if self.onExpansionChanged is not None:
            result["onExpansionChanged"] = self._register_action(
                self.onExpansionChanged, "ValueChanged<bool>"
            )._flut_pack()
        if self.trailing is not None:
            result["trailing"] = _flut_pack_value(self.trailing)
        if self.tilePadding is not None:
            result["tilePadding"] = _flut_pack_value(self.tilePadding)
        if self.expandedCrossAxisAlignment is not None:
            result["expandedCrossAxisAlignment"] = _flut_pack_value(
                self.expandedCrossAxisAlignment
            )
        if self.expandedAlignment is not None:
            result["expandedAlignment"] = _flut_pack_value(self.expandedAlignment)
        if self.childrenPadding is not None:
            result["childrenPadding"] = _flut_pack_value(self.childrenPadding)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.collapsedBackgroundColor is not None:
            result["collapsedBackgroundColor"] = _flut_pack_value(
                self.collapsedBackgroundColor
            )
        if self.textColor is not None:
            result["textColor"] = _flut_pack_value(self.textColor)
        if self.collapsedTextColor is not None:
            result["collapsedTextColor"] = _flut_pack_value(self.collapsedTextColor)
        if self.iconColor is not None:
            result["iconColor"] = _flut_pack_value(self.iconColor)
        if self.collapsedIconColor is not None:
            result["collapsedIconColor"] = _flut_pack_value(self.collapsedIconColor)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.collapsedShape is not None:
            result["collapsedShape"] = _flut_pack_value(self.collapsedShape)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.controlAffinity is not None:
            result["controlAffinity"] = _flut_pack_value(self.controlAffinity)
        if self.controller is not None:
            result["controller"] = _flut_pack_value(self.controller)
        if self.dense is not None:
            result["dense"] = _flut_pack_value(self.dense)
        if self.splashColor is not None:
            result["splashColor"] = _flut_pack_value(self.splashColor)
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        if self.minTileHeight is not None:
            result["minTileHeight"] = _flut_pack_value(self.minTileHeight)
        if self.enableFeedback is not None:
            result["enableFeedback"] = _flut_pack_value(self.enableFeedback)
        if self.expansionAnimationStyle is not None:
            result["expansionAnimationStyle"] = _flut_pack_value(
                self.expansionAnimationStyle
            )
        return result
