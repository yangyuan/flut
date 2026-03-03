from flut._flut.engine import FlutEnumObject


class HitTestBehavior(FlutEnumObject):
    deferToChild: "HitTestBehavior"
    opaque: "HitTestBehavior"
    translucent: "HitTestBehavior"
