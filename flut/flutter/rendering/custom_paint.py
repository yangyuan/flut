from typing import override

from flut._flut.engine import FlutAbstractObject
from flut.dart.ui import Canvas, Size


class CustomPainter(FlutAbstractObject):
    _flut_type = "CustomPainter"

    def __init__(self):
        super().__init__()

    def paint(self, canvas: Canvas, size: Size):
        raise NotImplementedError

    def shouldRepaint(self, oldDelegate: "CustomPainter") -> bool:
        raise NotImplementedError

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        paint_callable = self._register_action(
            self.paint, base_class=CustomPainter, method_name="paint"
        )
        if paint_callable is not None:
            result["paint"] = paint_callable._flut_pack()
        should_repaint_callable = self._register_action(
            self.shouldRepaint, base_class=CustomPainter, method_name="shouldRepaint"
        )
        if should_repaint_callable is not None:
            result["shouldRepaint"] = should_repaint_callable._flut_pack()
        return result
