from flut._flut.engine import wrap_widget_builder
from flut.flutter.widgets.pages import PageRoute


class MaterialPageRoute(PageRoute):
    _flut_type = "MaterialPageRoute"

    def __init__(
        self,
        *,
        builder,
        settings=None,
        maintainState: bool = True,
        fullscreenDialog: bool = False,
    ):
        super().__init__(settings=settings, fullscreenDialog=fullscreenDialog)
        props = {
            "maintainState": maintainState,
            "fullscreenDialog": fullscreenDialog,
        }
        if settings is not None:
            props["settings"] = settings._flut_pack()
        self._flut_create(
            props=props,
            bindings=[("builder", wrap_widget_builder(builder), "build_scope")],
        )
