from typing import override

from flut._flut.engine import (
    FlutEnumObject,
    FlutValueObject,
    call_dart_static,
    _flut_pack_value,
)
from flut._flut.runtime import _flut_unpack_required_field, _flut_unpack_optional_field
from flut.dart.ui import Size, Brightness
from flut.flutter.painting import EdgeInsets
from flut.flutter.painting.text_scaler import TextScaler
from flut.flutter.gestures.gesture_settings import DeviceGestureSettings


class Orientation(FlutEnumObject):
    portrait: "Orientation"
    landscape: "Orientation"


class NavigationMode(FlutEnumObject):
    traditional: "NavigationMode"
    directional: "NavigationMode"


class MediaQueryData(FlutValueObject):
    _flut_type = "MediaQueryData"

    def __init__(
        self,
        size: Size = Size.zero,
        devicePixelRatio: float = 1.0,
        textScaler=TextScaler.noScaling,
        platformBrightness=Brightness.light,
        padding: EdgeInsets = EdgeInsets.zero,
        viewInsets: EdgeInsets = EdgeInsets.zero,
        systemGestureInsets: EdgeInsets = EdgeInsets.zero,
        viewPadding: EdgeInsets = EdgeInsets.zero,
        alwaysUse24HourFormat: bool = False,
        accessibleNavigation: bool = False,
        invertColors: bool = False,
        highContrast: bool = False,
        onOffSwitchLabels: bool = False,
        disableAnimations: bool = False,
        boldText: bool = False,
        supportsShowingSystemContextMenu: bool = False,
        supportsAnnounce: bool = False,
        navigationMode=NavigationMode.traditional,
        gestureSettings=DeviceGestureSettings(),
        displayFeatures=None,
        lineHeightScaleFactorOverride=None,
        letterSpacingOverride=None,
        wordSpacingOverride=None,
        paragraphSpacingOverride=None,
    ):
        super().__init__()
        self.size = size
        self.devicePixelRatio = devicePixelRatio
        self.textScaler = textScaler
        self.platformBrightness = platformBrightness
        self.padding = padding
        self.viewInsets = viewInsets
        self.systemGestureInsets = systemGestureInsets
        self.viewPadding = viewPadding
        self.alwaysUse24HourFormat = alwaysUse24HourFormat
        self.accessibleNavigation = accessibleNavigation
        self.invertColors = invertColors
        self.highContrast = highContrast
        self.onOffSwitchLabels = onOffSwitchLabels
        self.disableAnimations = disableAnimations
        self.boldText = boldText
        self.supportsShowingSystemContextMenu = supportsShowingSystemContextMenu
        self.supportsAnnounce = supportsAnnounce
        self.navigationMode = navigationMode
        self.gestureSettings = gestureSettings
        self.displayFeatures = displayFeatures
        self.lineHeightScaleFactorOverride = lineHeightScaleFactorOverride
        self.letterSpacingOverride = letterSpacingOverride
        self.wordSpacingOverride = wordSpacingOverride
        self.paragraphSpacingOverride = paragraphSpacingOverride

    @property
    def orientation(self):
        return (
            Orientation.portrait
            if self.size.height > self.size.width
            else Orientation.landscape
        )

    def copyWith(
        self,
        *,
        size=None,
        devicePixelRatio=None,
        textScaler=None,
        platformBrightness=None,
        padding=None,
        viewPadding=None,
        viewInsets=None,
        systemGestureInsets=None,
        alwaysUse24HourFormat=None,
        accessibleNavigation=None,
        invertColors=None,
        highContrast=None,
        onOffSwitchLabels=None,
        disableAnimations=None,
        boldText=None,
        supportsShowingSystemContextMenu=None,
        supportsAnnounce=None,
        navigationMode=None,
        gestureSettings=None,
        displayFeatures=None,
        lineHeightScaleFactorOverride=None,
        letterSpacingOverride=None,
        wordSpacingOverride=None,
        paragraphSpacingOverride=None,
    ):
        return MediaQueryData(
            size=size if size is not None else self.size,
            devicePixelRatio=(
                devicePixelRatio
                if devicePixelRatio is not None
                else self.devicePixelRatio
            ),
            textScaler=textScaler if textScaler is not None else self.textScaler,
            platformBrightness=(
                platformBrightness
                if platformBrightness is not None
                else self.platformBrightness
            ),
            padding=padding if padding is not None else self.padding,
            viewInsets=viewInsets if viewInsets is not None else self.viewInsets,
            systemGestureInsets=(
                systemGestureInsets
                if systemGestureInsets is not None
                else self.systemGestureInsets
            ),
            viewPadding=viewPadding if viewPadding is not None else self.viewPadding,
            alwaysUse24HourFormat=(
                alwaysUse24HourFormat
                if alwaysUse24HourFormat is not None
                else self.alwaysUse24HourFormat
            ),
            accessibleNavigation=(
                accessibleNavigation
                if accessibleNavigation is not None
                else self.accessibleNavigation
            ),
            invertColors=(
                invertColors if invertColors is not None else self.invertColors
            ),
            highContrast=(
                highContrast if highContrast is not None else self.highContrast
            ),
            onOffSwitchLabels=(
                onOffSwitchLabels
                if onOffSwitchLabels is not None
                else self.onOffSwitchLabels
            ),
            disableAnimations=(
                disableAnimations
                if disableAnimations is not None
                else self.disableAnimations
            ),
            boldText=boldText if boldText is not None else self.boldText,
            supportsShowingSystemContextMenu=(
                supportsShowingSystemContextMenu
                if supportsShowingSystemContextMenu is not None
                else self.supportsShowingSystemContextMenu
            ),
            supportsAnnounce=(
                supportsAnnounce
                if supportsAnnounce is not None
                else self.supportsAnnounce
            ),
            navigationMode=(
                navigationMode if navigationMode is not None else self.navigationMode
            ),
            gestureSettings=(
                gestureSettings if gestureSettings is not None else self.gestureSettings
            ),
            displayFeatures=(
                displayFeatures if displayFeatures is not None else self.displayFeatures
            ),
            lineHeightScaleFactorOverride=(
                lineHeightScaleFactorOverride
                if lineHeightScaleFactorOverride is not None
                else self.lineHeightScaleFactorOverride
            ),
            letterSpacingOverride=(
                letterSpacingOverride
                if letterSpacingOverride is not None
                else self.letterSpacingOverride
            ),
            wordSpacingOverride=(
                wordSpacingOverride
                if wordSpacingOverride is not None
                else self.wordSpacingOverride
            ),
            paragraphSpacingOverride=(
                paragraphSpacingOverride
                if paragraphSpacingOverride is not None
                else self.paragraphSpacingOverride
            ),
        )

    def removePadding(
        self,
        *,
        removeLeft: bool = False,
        removeTop: bool = False,
        removeRight: bool = False,
        removeBottom: bool = False,
    ):
        if not (removeLeft or removeTop or removeRight or removeBottom):
            return self
        return self.copyWith(
            padding=self.padding.copyWith(
                left=0.0 if removeLeft else None,
                top=0.0 if removeTop else None,
                right=0.0 if removeRight else None,
                bottom=0.0 if removeBottom else None,
            ),
            viewPadding=self.viewPadding.copyWith(
                left=(
                    max(0.0, self.viewPadding.left - self.padding.left)
                    if removeLeft
                    else None
                ),
                top=(
                    max(0.0, self.viewPadding.top - self.padding.top)
                    if removeTop
                    else None
                ),
                right=(
                    max(0.0, self.viewPadding.right - self.padding.right)
                    if removeRight
                    else None
                ),
                bottom=(
                    max(0.0, self.viewPadding.bottom - self.padding.bottom)
                    if removeBottom
                    else None
                ),
            ),
        )

    def removeViewPadding(
        self,
        *,
        removeLeft: bool = False,
        removeTop: bool = False,
        removeRight: bool = False,
        removeBottom: bool = False,
    ):
        if not (removeLeft or removeTop or removeRight or removeBottom):
            return self
        return self.copyWith(
            padding=self.padding.copyWith(
                left=0.0 if removeLeft else None,
                top=0.0 if removeTop else None,
                right=0.0 if removeRight else None,
                bottom=0.0 if removeBottom else None,
            ),
            viewPadding=self.viewPadding.copyWith(
                left=0.0 if removeLeft else None,
                top=0.0 if removeTop else None,
                right=0.0 if removeRight else None,
                bottom=0.0 if removeBottom else None,
            ),
        )

    def removeViewInsets(
        self,
        *,
        removeLeft: bool = False,
        removeTop: bool = False,
        removeRight: bool = False,
        removeBottom: bool = False,
    ):
        if not (removeLeft or removeTop or removeRight or removeBottom):
            return self
        return self.copyWith(
            viewPadding=self.viewPadding.copyWith(
                left=(
                    max(0.0, self.viewPadding.left - self.viewInsets.left)
                    if removeLeft
                    else None
                ),
                top=(
                    max(0.0, self.viewPadding.top - self.viewInsets.top)
                    if removeTop
                    else None
                ),
                right=(
                    max(0.0, self.viewPadding.right - self.viewInsets.right)
                    if removeRight
                    else None
                ),
                bottom=(
                    max(0.0, self.viewPadding.bottom - self.viewInsets.bottom)
                    if removeBottom
                    else None
                ),
            ),
            viewInsets=self.viewInsets.copyWith(
                left=0.0 if removeLeft else None,
                top=0.0 if removeTop else None,
                right=0.0 if removeRight else None,
                bottom=0.0 if removeBottom else None,
            ),
        )

    def removeDisplayFeatures(self, subScreen):
        if (
            subScreen.size == self.size
            and subScreen.left == 0.0
            and subScreen.top == 0.0
        ):
            return self
        rightInset = self.size.width - subScreen.right
        bottomInset = self.size.height - subScreen.bottom
        return self.copyWith(
            padding=EdgeInsets(
                max(0.0, self.padding.left - subScreen.left),
                max(0.0, self.padding.top - subScreen.top),
                max(0.0, self.padding.right - rightInset),
                max(0.0, self.padding.bottom - bottomInset),
            ),
            viewPadding=EdgeInsets(
                max(0.0, self.viewPadding.left - subScreen.left),
                max(0.0, self.viewPadding.top - subScreen.top),
                max(0.0, self.viewPadding.right - rightInset),
                max(0.0, self.viewPadding.bottom - bottomInset),
            ),
            viewInsets=EdgeInsets(
                max(0.0, self.viewInsets.left - subScreen.left),
                max(0.0, self.viewInsets.top - subScreen.top),
                max(0.0, self.viewInsets.right - rightInset),
                max(0.0, self.viewInsets.bottom - bottomInset),
            ),
            displayFeatures=[
                f
                for f in self.displayFeatures
                if hasattr(f, "bounds") and _rectsOverlap(subScreen, f.bounds)
            ],
        )

    @staticmethod
    def _flut_unpack(data: dict) -> "MediaQueryData":
        return MediaQueryData(
            size=_flut_unpack_required_field(data, "size"),
            devicePixelRatio=_flut_unpack_required_field(data, "devicePixelRatio"),
            textScaler=_flut_unpack_required_field(data, "textScaler"),
            platformBrightness=_flut_unpack_required_field(data, "platformBrightness"),
            padding=_flut_unpack_required_field(data, "padding"),
            viewInsets=_flut_unpack_required_field(data, "viewInsets"),
            systemGestureInsets=_flut_unpack_required_field(
                data, "systemGestureInsets"
            ),
            viewPadding=_flut_unpack_required_field(data, "viewPadding"),
            alwaysUse24HourFormat=_flut_unpack_required_field(
                data, "alwaysUse24HourFormat"
            ),
            accessibleNavigation=_flut_unpack_required_field(
                data, "accessibleNavigation"
            ),
            invertColors=_flut_unpack_required_field(data, "invertColors"),
            highContrast=_flut_unpack_required_field(data, "highContrast"),
            onOffSwitchLabels=_flut_unpack_required_field(data, "onOffSwitchLabels"),
            disableAnimations=_flut_unpack_required_field(data, "disableAnimations"),
            boldText=_flut_unpack_required_field(data, "boldText"),
            supportsShowingSystemContextMenu=_flut_unpack_required_field(
                data, "supportsShowingSystemContextMenu"
            ),
            supportsAnnounce=_flut_unpack_required_field(data, "supportsAnnounce"),
            navigationMode=_flut_unpack_required_field(data, "navigationMode"),
            gestureSettings=_flut_unpack_required_field(data, "gestureSettings"),
            displayFeatures=_flut_unpack_optional_field(data, "displayFeatures"),
            lineHeightScaleFactorOverride=_flut_unpack_optional_field(
                data, "lineHeightScaleFactorOverride"
            ),
            letterSpacingOverride=_flut_unpack_optional_field(
                data, "letterSpacingOverride"
            ),
            wordSpacingOverride=_flut_unpack_optional_field(
                data, "wordSpacingOverride"
            ),
            paragraphSpacingOverride=_flut_unpack_optional_field(
                data, "paragraphSpacingOverride"
            ),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["size"] = _flut_pack_value(self.size)
        result["devicePixelRatio"] = _flut_pack_value(self.devicePixelRatio)
        result["textScaler"] = _flut_pack_value(self.textScaler)
        result["platformBrightness"] = _flut_pack_value(self.platformBrightness)
        result["padding"] = _flut_pack_value(self.padding)
        result["viewInsets"] = _flut_pack_value(self.viewInsets)
        result["systemGestureInsets"] = _flut_pack_value(self.systemGestureInsets)
        result["viewPadding"] = _flut_pack_value(self.viewPadding)
        result["alwaysUse24HourFormat"] = _flut_pack_value(self.alwaysUse24HourFormat)
        result["accessibleNavigation"] = _flut_pack_value(self.accessibleNavigation)
        result["invertColors"] = _flut_pack_value(self.invertColors)
        result["highContrast"] = _flut_pack_value(self.highContrast)
        result["onOffSwitchLabels"] = _flut_pack_value(self.onOffSwitchLabels)
        result["disableAnimations"] = _flut_pack_value(self.disableAnimations)
        result["boldText"] = _flut_pack_value(self.boldText)
        result["supportsShowingSystemContextMenu"] = _flut_pack_value(
            self.supportsShowingSystemContextMenu
        )
        result["supportsAnnounce"] = _flut_pack_value(self.supportsAnnounce)
        result["navigationMode"] = _flut_pack_value(self.navigationMode)
        result["gestureSettings"] = _flut_pack_value(self.gestureSettings)
        result["displayFeatures"] = _flut_pack_value(self.displayFeatures)
        if self.lineHeightScaleFactorOverride is not None:
            result["lineHeightScaleFactorOverride"] = _flut_pack_value(
                self.lineHeightScaleFactorOverride
            )
        if self.letterSpacingOverride is not None:
            result["letterSpacingOverride"] = _flut_pack_value(
                self.letterSpacingOverride
            )
        if self.wordSpacingOverride is not None:
            result["wordSpacingOverride"] = _flut_pack_value(self.wordSpacingOverride)
        if self.paragraphSpacingOverride is not None:
            result["paragraphSpacingOverride"] = _flut_pack_value(
                self.paragraphSpacingOverride
            )
        return result


def _rectsOverlap(a, b):
    return not (
        a.right <= b.left or b.right <= a.left or a.bottom <= b.top or b.bottom <= a.top
    )


class MediaQuery:

    @staticmethod
    def of(context) -> MediaQueryData:
        return call_dart_static("MediaQuery", "of", context._flut_pack())
