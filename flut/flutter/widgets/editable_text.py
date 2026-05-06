from flut._flut.engine import FlutRealtimeObject
from flut.flutter.foundation.change_notifier import Listenable, ValueNotifier


class EditableTextState(FlutRealtimeObject):
    _flut_type = "EditableTextState"


class TextEditingController(ValueNotifier):
    _flut_type = "TextEditingController"

    def __init__(self, text=None):
        props = {}
        if text is not None:
            props["text"] = text
        self._flut_init_props = props
        self._flut_init_bindings = [
            (
                "buildTextSpan",
                self.buildTextSpan,
                TextEditingController,
                "buildTextSpan",
            ),
        ]
        Listenable.__init__(self)

    @property
    def text(self):
        return self._flut_get("text")

    @text.setter
    def text(self, value):
        self._flut_set("text", value)

    def clear(self):
        self._flut_call("clear")

    def dispose(self):
        self._flut_call("dispose")

    def buildTextSpan(self, *, context, style, withComposing):
        raise NotImplementedError()
