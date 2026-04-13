from typing import Optional

from flut.dart.core import Duration
from flut.dart.ui import Color, Size
from flut._flut.engine import FlutRealtimeObject, _flut_pack_value
from flut.flutter.material.button_style_button import IconAlignment
from flut.flutter.material.ink_well import InteractiveInkFeatureFactory
from flut.flutter.material.theme_data import MaterialTapTargetSize, VisualDensity
from flut.flutter.painting.alignment import AlignmentGeometry
from flut.flutter.painting.borders import BorderSide, OutlinedBorder
from flut.flutter.painting.edge_insets import EdgeInsetsGeometry
from flut.flutter.painting.text_style import TextStyle
from flut.flutter.services.mouse_cursor import MouseCursor
from flut.flutter.widgets.widget_state import WidgetStateProperty


class ButtonStyle(FlutRealtimeObject):
    _flut_type = "ButtonStyle"

    def __init__(
        self,
        *,
        textStyle: Optional[WidgetStateProperty[TextStyle | None]] = None,
        backgroundColor: Optional[WidgetStateProperty[Color | None]] = None,
        foregroundColor: Optional[WidgetStateProperty[Color | None]] = None,
        overlayColor: Optional[WidgetStateProperty[Color | None]] = None,
        shadowColor: Optional[WidgetStateProperty[Color | None]] = None,
        surfaceTintColor: Optional[WidgetStateProperty[Color | None]] = None,
        elevation: Optional[WidgetStateProperty[float | None]] = None,
        padding: Optional[WidgetStateProperty[EdgeInsetsGeometry | None]] = None,
        minimumSize: Optional[WidgetStateProperty[Size | None]] = None,
        fixedSize: Optional[WidgetStateProperty[Size | None]] = None,
        maximumSize: Optional[WidgetStateProperty[Size | None]] = None,
        iconColor: Optional[WidgetStateProperty[Color | None]] = None,
        iconSize: Optional[WidgetStateProperty[float | None]] = None,
        iconAlignment: Optional[IconAlignment] = None,
        side: Optional[WidgetStateProperty[BorderSide | None]] = None,
        shape: Optional[WidgetStateProperty[OutlinedBorder | None]] = None,
        mouseCursor: Optional[WidgetStateProperty[MouseCursor | None]] = None,
        visualDensity: Optional[VisualDensity] = None,
        tapTargetSize: Optional[MaterialTapTargetSize] = None,
        animationDuration: Optional[Duration] = None,
        enableFeedback: Optional[bool] = None,
        alignment: Optional[AlignmentGeometry] = None,
        splashFactory: Optional[InteractiveInkFeatureFactory] = None,
    ) -> None:
        super().__init__()
        props = {}
        if textStyle is not None:
            props["textStyle"] = _flut_pack_value(textStyle)
        if backgroundColor is not None:
            props["backgroundColor"] = _flut_pack_value(backgroundColor)
        if foregroundColor is not None:
            props["foregroundColor"] = _flut_pack_value(foregroundColor)
        if overlayColor is not None:
            props["overlayColor"] = _flut_pack_value(overlayColor)
        if shadowColor is not None:
            props["shadowColor"] = _flut_pack_value(shadowColor)
        if surfaceTintColor is not None:
            props["surfaceTintColor"] = _flut_pack_value(surfaceTintColor)
        if elevation is not None:
            props["elevation"] = _flut_pack_value(elevation)
        if padding is not None:
            props["padding"] = _flut_pack_value(padding)
        if minimumSize is not None:
            props["minimumSize"] = _flut_pack_value(minimumSize)
        if fixedSize is not None:
            props["fixedSize"] = _flut_pack_value(fixedSize)
        if maximumSize is not None:
            props["maximumSize"] = _flut_pack_value(maximumSize)
        if iconColor is not None:
            props["iconColor"] = _flut_pack_value(iconColor)
        if iconSize is not None:
            props["iconSize"] = _flut_pack_value(iconSize)
        if iconAlignment is not None:
            props["iconAlignment"] = _flut_pack_value(iconAlignment)
        if side is not None:
            props["side"] = _flut_pack_value(side)
        if shape is not None:
            props["shape"] = _flut_pack_value(shape)
        if mouseCursor is not None:
            props["mouseCursor"] = _flut_pack_value(mouseCursor)
        if visualDensity is not None:
            props["visualDensity"] = _flut_pack_value(visualDensity)
        if tapTargetSize is not None:
            props["tapTargetSize"] = _flut_pack_value(tapTargetSize)
        if animationDuration is not None:
            props["animationDuration"] = _flut_pack_value(animationDuration)
        if enableFeedback is not None:
            props["enableFeedback"] = _flut_pack_value(enableFeedback)
        if alignment is not None:
            props["alignment"] = _flut_pack_value(alignment)
        if splashFactory is not None:
            props["splashFactory"] = _flut_pack_value(splashFactory)
        self._flut_create(props=props)
