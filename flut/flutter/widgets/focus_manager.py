from flut._flut.engine import _flut_pack_value, FlutEnumObject
from flut.flutter.foundation.change_notifier import ChangeNotifier
from flut.flutter.widgets.focus_traversal import TraversalEdgeBehavior


class KeyEventResult(FlutEnumObject):
    handled: "KeyEventResult"
    ignored: "KeyEventResult"
    skipRemainingHandlers: "KeyEventResult"


class FocusNode(ChangeNotifier):
    _flut_type = "FocusNode"

    def __init__(self, onKeyEvent=None):
        super().__init__()
        self._flut_create(
            bindings=[
                ("onKeyEvent", onKeyEvent, "FocusOnKeyEventCallback"),
            ],
        )

    @property
    def onKeyEvent(self):
        return self._flut_get("onKeyEvent")

    @onKeyEvent.setter
    def onKeyEvent(self, callback):
        self._flut_set("onKeyEvent", callback, "FocusOnKeyEventCallback")

    @property
    def hasFocus(self):
        return self._flut_get("hasFocus")

    @property
    def hasPrimaryFocus(self):
        return self._flut_get("hasPrimaryFocus")

    def dispose(self):
        self._flut_call("dispose")

    def requestFocus(self):
        self._flut_call("requestFocus")

    def unfocus(self):
        self._flut_call("unfocus")


class FocusScopeNode(FocusNode):
    _flut_type = "FocusScopeNode"

    def __init__(
        self,
        *,
        onKeyEvent=None,
        debugLabel=None,
        skipTraversal=False,
        canRequestFocus=True,
        traversalEdgeBehavior=TraversalEdgeBehavior.closedLoop,
        directionalTraversalEdgeBehavior=TraversalEdgeBehavior.stop,
    ):
        ChangeNotifier.__init__(self)
        props = {}
        if debugLabel is not None:
            props["debugLabel"] = debugLabel
        props["skipTraversal"] = skipTraversal
        props["canRequestFocus"] = canRequestFocus
        props["traversalEdgeBehavior"] = _flut_pack_value(traversalEdgeBehavior)
        props["directionalTraversalEdgeBehavior"] = _flut_pack_value(
            directionalTraversalEdgeBehavior
        )
        self._flut_create(
            bindings=[
                ("onKeyEvent", onKeyEvent, "FocusOnKeyEventCallback"),
            ],
            props=props,
        )
