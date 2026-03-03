from flut._flut.engine import FlutEnumObject


class ShowValueIndicator(FlutEnumObject):
    onlyForDiscrete: "ShowValueIndicator"
    onlyForContinuous: "ShowValueIndicator"
    always: "ShowValueIndicator"
    onDrag: "ShowValueIndicator"
    alwaysVisible: "ShowValueIndicator"
    never: "ShowValueIndicator"
