from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value, call_dart_static
from flut.dart.ui import Color
from flut.flutter.painting.edge_insets import EdgeInsets
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.widgets.framework import Widget, StatelessWidget, BuildContext


class AlertDialog(Widget):
    _flut_type = "AlertDialog"

    def __init__(
        self,
        *,
        key=None,
        icon: Optional[Widget] = None,
        iconPadding: Optional[EdgeInsets] = None,
        iconColor: Optional[Color] = None,
        title: Optional[Widget] = None,
        titlePadding: Optional[EdgeInsets] = None,
        titleTextStyle: Optional[TextStyle] = None,
        content: Optional[Widget] = None,
        contentPadding: Optional[EdgeInsets] = None,
        contentTextStyle: Optional[TextStyle] = None,
        actions: Optional[list[Widget]] = None,
        actionsPadding: Optional[EdgeInsets] = None,
        actionsAlignment=None,
        actionsOverflowAlignment=None,
        actionsOverflowDirection=None,
        actionsOverflowButtonSpacing: Optional[float] = None,
        buttonPadding: Optional[EdgeInsets] = None,
        backgroundColor: Optional[Color] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        semanticLabel: Optional[str] = None,
        insetPadding: Optional[EdgeInsets] = None,
        clipBehavior=None,
        shape=None,
        alignment=None,
        constraints=None,
        scrollable: bool = False,
    ):
        super().__init__(key=key)
        self.icon = icon
        self.iconPadding = iconPadding
        self.iconColor = iconColor
        self.title = title
        self.titlePadding = titlePadding
        self.titleTextStyle = titleTextStyle
        self.content = content
        self.contentPadding = contentPadding
        self.contentTextStyle = contentTextStyle
        self.actions = actions
        self.actionsPadding = actionsPadding
        self.actionsAlignment = actionsAlignment
        self.actionsOverflowAlignment = actionsOverflowAlignment
        self.actionsOverflowDirection = actionsOverflowDirection
        self.actionsOverflowButtonSpacing = actionsOverflowButtonSpacing
        self.buttonPadding = buttonPadding
        self.backgroundColor = backgroundColor
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.semanticLabel = semanticLabel
        self.insetPadding = insetPadding
        self.clipBehavior = clipBehavior
        self.shape = shape
        self.alignment = alignment
        self.constraints = constraints
        self.scrollable = scrollable

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["scrollable"] = _flut_pack_value(self.scrollable)
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.iconPadding is not None:
            result["iconPadding"] = _flut_pack_value(self.iconPadding)
        if self.iconColor is not None:
            result["iconColor"] = _flut_pack_value(self.iconColor)
        if self.title is not None:
            result["title"] = _flut_pack_value(self.title)
        if self.titlePadding is not None:
            result["titlePadding"] = _flut_pack_value(self.titlePadding)
        if self.titleTextStyle is not None:
            result["titleTextStyle"] = _flut_pack_value(self.titleTextStyle)
        if self.content is not None:
            result["content"] = _flut_pack_value(self.content)
        if self.contentPadding is not None:
            result["contentPadding"] = _flut_pack_value(self.contentPadding)
        if self.contentTextStyle is not None:
            result["contentTextStyle"] = _flut_pack_value(self.contentTextStyle)
        if self.actions is not None:
            result["actions"] = _flut_pack_value(self.actions)
        if self.actionsPadding is not None:
            result["actionsPadding"] = _flut_pack_value(self.actionsPadding)
        if self.actionsAlignment is not None:
            result["actionsAlignment"] = _flut_pack_value(self.actionsAlignment)
        if self.actionsOverflowAlignment is not None:
            result["actionsOverflowAlignment"] = _flut_pack_value(
                self.actionsOverflowAlignment
            )
        if self.actionsOverflowDirection is not None:
            result["actionsOverflowDirection"] = _flut_pack_value(
                self.actionsOverflowDirection
            )
        if self.actionsOverflowButtonSpacing is not None:
            result["actionsOverflowButtonSpacing"] = _flut_pack_value(
                self.actionsOverflowButtonSpacing
            )
        if self.buttonPadding is not None:
            result["buttonPadding"] = _flut_pack_value(self.buttonPadding)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        if self.insetPadding is not None:
            result["insetPadding"] = _flut_pack_value(self.insetPadding)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        return result


class Dialog(Widget):
    _flut_type = "Dialog"

    def __init__(
        self,
        *,
        key=None,
        backgroundColor: Optional[Color] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        insetAnimationDuration=None,
        insetAnimationCurve=None,
        insetPadding: Optional[EdgeInsets] = None,
        clipBehavior=None,
        shape=None,
        alignment=None,
        constraints=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.backgroundColor = backgroundColor
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.insetAnimationDuration = insetAnimationDuration
        self.insetAnimationCurve = insetAnimationCurve
        self.insetPadding = insetPadding
        self.clipBehavior = clipBehavior
        self.shape = shape
        self.alignment = alignment
        self.constraints = constraints
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.insetAnimationDuration is not None:
            result["insetAnimationDuration"] = _flut_pack_value(
                self.insetAnimationDuration
            )
        if self.insetAnimationCurve is not None:
            result["insetAnimationCurve"] = _flut_pack_value(self.insetAnimationCurve)
        if self.insetPadding is not None:
            result["insetPadding"] = _flut_pack_value(self.insetPadding)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class SimpleDialog(Widget):
    _flut_type = "SimpleDialog"

    def __init__(
        self,
        *,
        key=None,
        title: Optional[Widget] = None,
        titlePadding: Optional[EdgeInsets] = None,
        titleTextStyle: Optional[TextStyle] = None,
        children: Optional[list[Widget]] = None,
        contentPadding: Optional[EdgeInsets] = None,
        backgroundColor: Optional[Color] = None,
        elevation: Optional[float] = None,
        shadowColor: Optional[Color] = None,
        surfaceTintColor: Optional[Color] = None,
        semanticLabel: Optional[str] = None,
        insetPadding: Optional[EdgeInsets] = None,
        clipBehavior=None,
        shape=None,
        alignment=None,
        constraints=None,
    ):
        super().__init__(key=key)
        self.title = title
        self.titlePadding = titlePadding
        self.titleTextStyle = titleTextStyle
        self.children = children
        self.contentPadding = contentPadding
        self.backgroundColor = backgroundColor
        self.elevation = elevation
        self.shadowColor = shadowColor
        self.surfaceTintColor = surfaceTintColor
        self.semanticLabel = semanticLabel
        self.insetPadding = insetPadding
        self.clipBehavior = clipBehavior
        self.shape = shape
        self.alignment = alignment
        self.constraints = constraints

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.title is not None:
            result["title"] = _flut_pack_value(self.title)
        if self.titlePadding is not None:
            result["titlePadding"] = _flut_pack_value(self.titlePadding)
        if self.titleTextStyle is not None:
            result["titleTextStyle"] = _flut_pack_value(self.titleTextStyle)
        if self.contentPadding is not None:
            result["contentPadding"] = _flut_pack_value(self.contentPadding)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.elevation is not None:
            result["elevation"] = _flut_pack_value(self.elevation)
        if self.shadowColor is not None:
            result["shadowColor"] = _flut_pack_value(self.shadowColor)
        if self.surfaceTintColor is not None:
            result["surfaceTintColor"] = _flut_pack_value(self.surfaceTintColor)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        if self.insetPadding is not None:
            result["insetPadding"] = _flut_pack_value(self.insetPadding)
        if self.clipBehavior is not None:
            result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.shape is not None:
            result["shape"] = _flut_pack_value(self.shape)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.children is not None:
            result["children"] = _flut_pack_value(self.children)
        return result


class SimpleDialogOption(Widget):
    _flut_type = "SimpleDialogOption"

    def __init__(
        self,
        *,
        key=None,
        onPressed=None,
        padding: Optional[EdgeInsets] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onPressed = onPressed
        self.padding = padding
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.onPressed is not None:
            result["onPressed"] = self._register_action(
                self.onPressed, "VoidCallback"
            )._flut_pack()
        if self.padding is not None:
            result["padding"] = _flut_pack_value(self.padding)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class _ShowDialogScope(StatelessWidget):
    def __init__(self, builder):
        super().__init__()
        self._builder = builder

    def build(self, context):
        return self._builder(context)


def showDialog(
    *,
    context,
    builder: Callable[[BuildContext], Widget],
    barrierDismissible: bool = True,
    barrierColor: Optional[Color] = None,
    useSafeArea: bool = True,
    useRootNavigator: bool = True,
    routeSettings=None,
    anchorPoint=None,
    traversalEdgeBehavior=None,
):
    scope = _ShowDialogScope(builder)
    kwargs = {
        "barrierDismissible": barrierDismissible,
        "useSafeArea": useSafeArea,
        "useRootNavigator": useRootNavigator,
    }
    if barrierColor is not None:
        kwargs["barrierColor"] = barrierColor._flut_pack()
    if routeSettings is not None:
        kwargs["routeSettings"] = routeSettings._flut_pack()
    if anchorPoint is not None:
        kwargs["anchorPoint"] = anchorPoint._flut_pack()
    if traversalEdgeBehavior is not None:
        kwargs["traversalEdgeBehavior"] = traversalEdgeBehavior._flut_pack()
    return call_dart_static(
        "showDialog", "showDialog", context._flut_pack(), scope._flut_pack(), **kwargs
    )
