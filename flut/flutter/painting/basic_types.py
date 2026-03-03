from flut._flut.engine import FlutEnumObject


class Axis(FlutEnumObject):
    horizontal: "Axis"
    vertical: "Axis"


class AxisDirection(FlutEnumObject):
    up: "AxisDirection"
    right: "AxisDirection"
    down: "AxisDirection"
    left: "AxisDirection"


class VerticalDirection(FlutEnumObject):
    up: "VerticalDirection"
    down: "VerticalDirection"
