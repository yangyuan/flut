from flut._flut.engine import FlutValueObject


class ImageProvider(FlutValueObject):
    _flut_type = "ImageProvider"

    def __init__(self):
        super().__init__()
