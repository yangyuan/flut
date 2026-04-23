from flut._flut.engine import wrap_widget_builder
from flut.flutter.widgets.pages import PageRoute
from flut.flutter.widgets.routes import ModalRoute


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
        props = {
            "maintainState": maintainState,
            "fullscreenDialog": fullscreenDialog,
        }
        if settings is not None:
            props["settings"] = settings._flut_pack()
        self._flut_init_props = props
        self._flut_init_bindings = [
            ("builder", wrap_widget_builder(builder), "build_scope"),
        ]
        ModalRoute.__init__(self)
