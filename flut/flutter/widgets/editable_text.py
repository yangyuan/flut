from flut.flutter.foundation.change_notifier import ChangeNotifier


class TextEditingController(ChangeNotifier):
    _flut_type = "TextEditingController"

    def __init__(self, text=None):
        super().__init__()
        props = {}
        if text is not None:
            props["text"] = text
        self._flut_create(
            props=props,
            bindings=[
                (
                    "buildTextSpan",
                    self.buildTextSpan,
                    TextEditingController,
                    "buildTextSpan",
                ),
            ],
        )

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
