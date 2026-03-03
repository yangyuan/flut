from typing import Callable, Optional, override

from flut._flut.engine import _flut_pack_value
from flut.flutter.gestures.recognizer import DragStartBehavior
from flut.flutter.painting.alignment import AlignmentDirectional
from flut.flutter.widgets.framework import Widget


class Scaffold(Widget):
    _flut_type = "Scaffold"

    def __init__(
        self,
        *,
        key=None,
        appBar: Optional[Widget] = None,
        body: Optional[Widget] = None,
        floatingActionButton: Optional[Widget] = None,
        floatingActionButtonLocation=None,
        floatingActionButtonAnimator=None,
        persistentFooterButtons: Optional[list[Widget]] = None,
        persistentFooterAlignment=AlignmentDirectional.centerEnd,
        persistentFooterDecoration=None,
        drawer: Optional[Widget] = None,
        onDrawerChanged: Optional[Callable] = None,
        endDrawer: Optional[Widget] = None,
        onEndDrawerChanged: Optional[Callable] = None,
        bottomNavigationBar: Optional[Widget] = None,
        bottomSheet: Optional[Widget] = None,
        backgroundColor=None,
        resizeToAvoidBottomInset: Optional[bool] = None,
        primary: bool = True,
        drawerDragStartBehavior=DragStartBehavior.start,
        extendBody: bool = False,
        drawerBarrierDismissible: bool = True,
        extendBodyBehindAppBar: bool = False,
        drawerScrimColor=None,
        drawerEdgeDragWidth: Optional[float] = None,
        drawerEnableOpenDragGesture: bool = True,
        endDrawerEnableOpenDragGesture: bool = True,
        restorationId: Optional[str] = None,
    ):
        super().__init__(key=key)
        self.appBar = appBar
        self.body = body
        self.floatingActionButton = floatingActionButton
        self.floatingActionButtonLocation = floatingActionButtonLocation
        self.floatingActionButtonAnimator = floatingActionButtonAnimator
        self.persistentFooterButtons = persistentFooterButtons
        self.persistentFooterAlignment = persistentFooterAlignment
        self.persistentFooterDecoration = persistentFooterDecoration
        self.drawer = drawer
        self.onDrawerChanged = onDrawerChanged
        self.endDrawer = endDrawer
        self.onEndDrawerChanged = onEndDrawerChanged
        self.bottomNavigationBar = bottomNavigationBar
        self.bottomSheet = bottomSheet
        self.backgroundColor = backgroundColor
        self.resizeToAvoidBottomInset = resizeToAvoidBottomInset
        self.primary = primary
        self.drawerDragStartBehavior = drawerDragStartBehavior
        self.extendBody = extendBody
        self.drawerBarrierDismissible = drawerBarrierDismissible
        self.extendBodyBehindAppBar = extendBodyBehindAppBar
        self.drawerScrimColor = drawerScrimColor
        self.drawerEdgeDragWidth = drawerEdgeDragWidth
        self.drawerEnableOpenDragGesture = drawerEnableOpenDragGesture
        self.endDrawerEnableOpenDragGesture = endDrawerEnableOpenDragGesture
        self.restorationId = restorationId

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.appBar is not None:
            result["appBar"] = _flut_pack_value(self.appBar)
        if self.body is not None:
            result["body"] = _flut_pack_value(self.body)
        if self.floatingActionButton is not None:
            result["floatingActionButton"] = _flut_pack_value(self.floatingActionButton)
        if self.floatingActionButtonLocation is not None:
            result["floatingActionButtonLocation"] = _flut_pack_value(
                self.floatingActionButtonLocation
            )
        if self.floatingActionButtonAnimator is not None:
            result["floatingActionButtonAnimator"] = _flut_pack_value(
                self.floatingActionButtonAnimator
            )
        if self.persistentFooterButtons is not None:
            result["persistentFooterButtons"] = _flut_pack_value(
                self.persistentFooterButtons
            )
        result["persistentFooterAlignment"] = _flut_pack_value(
            self.persistentFooterAlignment
        )
        if self.persistentFooterDecoration is not None:
            result["persistentFooterDecoration"] = _flut_pack_value(
                self.persistentFooterDecoration
            )
        if self.drawer is not None:
            result["drawer"] = _flut_pack_value(self.drawer)
        if self.onDrawerChanged is not None:
            result["onDrawerChanged"] = self._register_action(
                self.onDrawerChanged, "DrawerCallback"
            )._flut_pack()
        if self.endDrawer is not None:
            result["endDrawer"] = _flut_pack_value(self.endDrawer)
        if self.onEndDrawerChanged is not None:
            result["onEndDrawerChanged"] = self._register_action(
                self.onEndDrawerChanged, "DrawerCallback"
            )._flut_pack()
        if self.bottomNavigationBar is not None:
            result["bottomNavigationBar"] = _flut_pack_value(self.bottomNavigationBar)
        if self.bottomSheet is not None:
            result["bottomSheet"] = _flut_pack_value(self.bottomSheet)
        if self.backgroundColor is not None:
            result["backgroundColor"] = _flut_pack_value(self.backgroundColor)
        if self.resizeToAvoidBottomInset is not None:
            result["resizeToAvoidBottomInset"] = _flut_pack_value(
                self.resizeToAvoidBottomInset
            )
        result["primary"] = _flut_pack_value(self.primary)
        result["drawerDragStartBehavior"] = _flut_pack_value(
            self.drawerDragStartBehavior
        )
        result["extendBody"] = _flut_pack_value(self.extendBody)
        result["drawerBarrierDismissible"] = _flut_pack_value(
            self.drawerBarrierDismissible
        )
        result["extendBodyBehindAppBar"] = _flut_pack_value(self.extendBodyBehindAppBar)
        if self.drawerScrimColor is not None:
            result["drawerScrimColor"] = _flut_pack_value(self.drawerScrimColor)
        if self.drawerEdgeDragWidth is not None:
            result["drawerEdgeDragWidth"] = _flut_pack_value(self.drawerEdgeDragWidth)
        result["drawerEnableOpenDragGesture"] = _flut_pack_value(
            self.drawerEnableOpenDragGesture
        )
        result["endDrawerEnableOpenDragGesture"] = _flut_pack_value(
            self.endDrawerEnableOpenDragGesture
        )
        if self.restorationId is not None:
            result["restorationId"] = _flut_pack_value(self.restorationId)
        return result
