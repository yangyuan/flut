from flut._flut.engine import FlutRealtimeObject, _flut_pack_value


class ButtonStyle(FlutRealtimeObject):
    _flut_type = "ButtonStyle"

    def __init__(
        self,
        *,
        textStyle=None,
        backgroundColor=None,
        foregroundColor=None,
        overlayColor=None,
        shadowColor=None,
        surfaceTintColor=None,
        elevation=None,
        padding=None,
        minimumSize=None,
        fixedSize=None,
        maximumSize=None,
        iconColor=None,
        iconSize=None,
        iconAlignment=None,
        side=None,
        shape=None,
        mouseCursor=None,
        visualDensity=None,
        tapTargetSize=None,
        animationDuration=None,
        enableFeedback=None,
        alignment=None,
        splashFactory=None,
        backgroundBuilder=None,
        foregroundBuilder=None,
    ):
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
        if backgroundBuilder is not None:
            props["backgroundBuilder"] = _flut_pack_value(backgroundBuilder)
        if foregroundBuilder is not None:
            props["foregroundBuilder"] = _flut_pack_value(foregroundBuilder)
        self._flut_create(props=props)
