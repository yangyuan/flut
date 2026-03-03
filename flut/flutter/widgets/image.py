from typing import Optional, override

from flut._flut.engine import named_constructor, _flut_pack_value

from flut.flutter.widgets.framework import Widget
from flut.flutter.painting.box_fit import BoxFit
from flut.flutter.painting.decoration_image import ImageRepeat
from flut.flutter.painting.alignment import Alignment
from flut.dart.ui import Color, BlendMode, FilterQuality
from flut.dart.io import File
from flut.dart.typed_data import Uint8List


class Image(Widget):
    _flut_type = "Image"

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "Image has no default constructor. "
            "Use Image.network(), Image.file(), or Image.memory()."
        )

    @named_constructor
    def network(
        cls,
        src: str,
        *,
        key=None,
        scale: float = 1.0,
        semanticLabel: Optional[str] = None,
        excludeFromSemantics: bool = False,
        width: Optional[float] = None,
        height: Optional[float] = None,
        color: Optional[Color] = None,
        colorBlendMode: Optional[BlendMode] = None,
        fit: Optional[BoxFit] = None,
        alignment: Alignment = Alignment.center,
        repeat: ImageRepeat = ImageRepeat.noRepeat,
        matchTextDirection: bool = False,
        gaplessPlayback: bool = False,
        filterQuality: FilterQuality = FilterQuality.medium,
        isAntiAlias: bool = False,
        headers: Optional[dict] = None,
        cacheWidth: Optional[int] = None,
        cacheHeight: Optional[int] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.src = src
        instance.scale = scale
        instance.semanticLabel = semanticLabel
        instance.excludeFromSemantics = excludeFromSemantics
        instance.width = width
        instance.height = height
        instance.color = color
        instance.colorBlendMode = colorBlendMode
        instance.fit = fit
        instance.alignment = alignment
        instance.repeat = repeat
        instance.matchTextDirection = matchTextDirection
        instance.gaplessPlayback = gaplessPlayback
        instance.filterQuality = filterQuality
        instance.isAntiAlias = isAntiAlias
        instance.headers = headers
        instance.cacheWidth = cacheWidth
        instance.cacheHeight = cacheHeight
        return instance

    @named_constructor
    def file(
        cls,
        file: File,
        *,
        key=None,
        scale: float = 1.0,
        semanticLabel: Optional[str] = None,
        excludeFromSemantics: bool = False,
        width: Optional[float] = None,
        height: Optional[float] = None,
        color: Optional[Color] = None,
        colorBlendMode: Optional[BlendMode] = None,
        fit: Optional[BoxFit] = None,
        alignment: Alignment = Alignment.center,
        repeat: ImageRepeat = ImageRepeat.noRepeat,
        matchTextDirection: bool = False,
        gaplessPlayback: bool = False,
        filterQuality: FilterQuality = FilterQuality.medium,
        isAntiAlias: bool = False,
        cacheWidth: Optional[int] = None,
        cacheHeight: Optional[int] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.file = file
        instance.scale = scale
        instance.semanticLabel = semanticLabel
        instance.excludeFromSemantics = excludeFromSemantics
        instance.width = width
        instance.height = height
        instance.color = color
        instance.colorBlendMode = colorBlendMode
        instance.fit = fit
        instance.alignment = alignment
        instance.repeat = repeat
        instance.matchTextDirection = matchTextDirection
        instance.gaplessPlayback = gaplessPlayback
        instance.filterQuality = filterQuality
        instance.isAntiAlias = isAntiAlias
        instance.cacheWidth = cacheWidth
        instance.cacheHeight = cacheHeight
        return instance

    @named_constructor
    def memory(
        cls,
        bytes: Uint8List,
        *,
        key=None,
        scale: float = 1.0,
        semanticLabel: Optional[str] = None,
        excludeFromSemantics: bool = False,
        width: Optional[float] = None,
        height: Optional[float] = None,
        color: Optional[Color] = None,
        colorBlendMode: Optional[BlendMode] = None,
        fit: Optional[BoxFit] = None,
        alignment: Alignment = Alignment.center,
        repeat: ImageRepeat = ImageRepeat.noRepeat,
        matchTextDirection: bool = False,
        gaplessPlayback: bool = False,
        filterQuality: FilterQuality = FilterQuality.medium,
        isAntiAlias: bool = False,
        cacheWidth: Optional[int] = None,
        cacheHeight: Optional[int] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.bytes = bytes
        instance.scale = scale
        instance.semanticLabel = semanticLabel
        instance.excludeFromSemantics = excludeFromSemantics
        instance.width = width
        instance.height = height
        instance.color = color
        instance.colorBlendMode = colorBlendMode
        instance.fit = fit
        instance.alignment = alignment
        instance.repeat = repeat
        instance.matchTextDirection = matchTextDirection
        instance.gaplessPlayback = gaplessPlayback
        instance.filterQuality = filterQuality
        instance.isAntiAlias = isAntiAlias
        instance.cacheWidth = cacheWidth
        instance.cacheHeight = cacheHeight
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["scale"] = _flut_pack_value(self.scale)
        if self.semanticLabel is not None:
            result["semanticLabel"] = _flut_pack_value(self.semanticLabel)
        result["excludeFromSemantics"] = _flut_pack_value(self.excludeFromSemantics)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        if self.color is not None:
            result["color"] = _flut_pack_value(self.color)
        if self.colorBlendMode is not None:
            result["colorBlendMode"] = _flut_pack_value(self.colorBlendMode)
        if self.fit is not None:
            result["fit"] = _flut_pack_value(self.fit)
        result["alignment"] = _flut_pack_value(self.alignment)
        result["repeat"] = _flut_pack_value(self.repeat)
        result["matchTextDirection"] = _flut_pack_value(self.matchTextDirection)
        result["gaplessPlayback"] = _flut_pack_value(self.gaplessPlayback)
        result["filterQuality"] = _flut_pack_value(self.filterQuality)
        result["isAntiAlias"] = _flut_pack_value(self.isAntiAlias)
        if self.cacheWidth is not None:
            result["cacheWidth"] = _flut_pack_value(self.cacheWidth)
        if self.cacheHeight is not None:
            result["cacheHeight"] = _flut_pack_value(self.cacheHeight)
        if self._flut_init == "network":
            result["src"] = _flut_pack_value(self.src)
            if self.headers is not None:
                result["headers"] = _flut_pack_value(self.headers)
        if self._flut_init == "file":
            result["file"] = _flut_pack_value(self.file)
        if self._flut_init == "memory":
            result["bytes"] = _flut_pack_value(self.bytes)
        return result
