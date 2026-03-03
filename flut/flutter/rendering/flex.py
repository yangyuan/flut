from flut._flut.engine import FlutEnumObject


class MainAxisSize(FlutEnumObject):
    min: "MainAxisSize"
    max: "MainAxisSize"


class MainAxisAlignment(FlutEnumObject):
    start: "MainAxisAlignment"
    end: "MainAxisAlignment"
    center: "MainAxisAlignment"
    spaceBetween: "MainAxisAlignment"
    spaceAround: "MainAxisAlignment"
    spaceEvenly: "MainAxisAlignment"


class CrossAxisAlignment(FlutEnumObject):
    start: "CrossAxisAlignment"
    end: "CrossAxisAlignment"
    center: "CrossAxisAlignment"
    stretch: "CrossAxisAlignment"
    baseline: "CrossAxisAlignment"


class FlexFit(FlutEnumObject):
    tight: "FlexFit"
    loose: "FlexFit"
