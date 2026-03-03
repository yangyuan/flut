from flut._flut.engine import call_dart_static
from flut.flutter.material.theme_data import ThemeData


class Theme:

    @staticmethod
    def of(context) -> ThemeData:
        return call_dart_static("Theme", "of", context._flut_pack())
