from flut._flut.engine import FlutEnumObject


class WrapAlignment(FlutEnumObject):
    start: "WrapAlignment"
    end: "WrapAlignment"
    center: "WrapAlignment"
    spaceBetween: "WrapAlignment"
    spaceAround: "WrapAlignment"
    spaceEvenly: "WrapAlignment"


class WrapCrossAlignment(FlutEnumObject):
    start: "WrapCrossAlignment"
    end: "WrapCrossAlignment"
    center: "WrapCrossAlignment"
