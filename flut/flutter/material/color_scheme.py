from typing import Optional
from flut._flut.engine import FlutEnumObject, FlutRealtimeObject
from flut.dart.ui import Brightness, Color


class DynamicSchemeVariant(FlutEnumObject):
    tonalSpot: "DynamicSchemeVariant"
    fidelity: "DynamicSchemeVariant"
    monochrome: "DynamicSchemeVariant"
    neutral: "DynamicSchemeVariant"
    vibrant: "DynamicSchemeVariant"
    expressive: "DynamicSchemeVariant"
    content: "DynamicSchemeVariant"
    rainbow: "DynamicSchemeVariant"
    fruitSalad: "DynamicSchemeVariant"


class ColorScheme(FlutRealtimeObject):
    _flut_type = "ColorScheme"

    def __init__(
        self,
        *,
        brightness: Brightness,
        primary: Color,
        onPrimary: Color,
        primaryContainer: Optional[Color] = None,
        onPrimaryContainer: Optional[Color] = None,
        primaryFixed: Optional[Color] = None,
        primaryFixedDim: Optional[Color] = None,
        onPrimaryFixed: Optional[Color] = None,
        onPrimaryFixedVariant: Optional[Color] = None,
        secondary: Color,
        onSecondary: Color,
        secondaryContainer: Optional[Color] = None,
        onSecondaryContainer: Optional[Color] = None,
        secondaryFixed: Optional[Color] = None,
        secondaryFixedDim: Optional[Color] = None,
        onSecondaryFixed: Optional[Color] = None,
        onSecondaryFixedVariant: Optional[Color] = None,
        tertiary: Optional[Color] = None,
        onTertiary: Optional[Color] = None,
        tertiaryContainer: Optional[Color] = None,
        onTertiaryContainer: Optional[Color] = None,
        tertiaryFixed: Optional[Color] = None,
        tertiaryFixedDim: Optional[Color] = None,
        onTertiaryFixed: Optional[Color] = None,
        onTertiaryFixedVariant: Optional[Color] = None,
        error: Color,
        onError: Color,
        errorContainer: Optional[Color] = None,
        onErrorContainer: Optional[Color] = None,
        surface: Color,
        onSurface: Color,
        surfaceDim: Optional[Color] = None,
        surfaceBright: Optional[Color] = None,
        surfaceContainerLowest: Optional[Color] = None,
        surfaceContainerLow: Optional[Color] = None,
        surfaceContainer: Optional[Color] = None,
        surfaceContainerHigh: Optional[Color] = None,
        surfaceContainerHighest: Optional[Color] = None,
        onSurfaceVariant: Optional[Color] = None,
        outline: Optional[Color] = None,
        outlineVariant: Optional[Color] = None,
        shadow: Optional[Color] = None,
        scrim: Optional[Color] = None,
        inverseSurface: Optional[Color] = None,
        onInverseSurface: Optional[Color] = None,
        inversePrimary: Optional[Color] = None,
        surfaceTint: Optional[Color] = None,
    ):
        super().__init__()
        props = {
            "brightness": brightness._flut_pack(),
            "primary": primary._flut_pack(),
            "onPrimary": onPrimary._flut_pack(),
            "secondary": secondary._flut_pack(),
            "onSecondary": onSecondary._flut_pack(),
            "surface": surface._flut_pack(),
            "onSurface": onSurface._flut_pack(),
            "error": error._flut_pack(),
            "onError": onError._flut_pack(),
        }
        if primaryContainer is not None:
            props["primaryContainer"] = primaryContainer._flut_pack()
        if onPrimaryContainer is not None:
            props["onPrimaryContainer"] = onPrimaryContainer._flut_pack()
        if primaryFixed is not None:
            props["primaryFixed"] = primaryFixed._flut_pack()
        if primaryFixedDim is not None:
            props["primaryFixedDim"] = primaryFixedDim._flut_pack()
        if onPrimaryFixed is not None:
            props["onPrimaryFixed"] = onPrimaryFixed._flut_pack()
        if onPrimaryFixedVariant is not None:
            props["onPrimaryFixedVariant"] = onPrimaryFixedVariant._flut_pack()
        if secondaryContainer is not None:
            props["secondaryContainer"] = secondaryContainer._flut_pack()
        if onSecondaryContainer is not None:
            props["onSecondaryContainer"] = onSecondaryContainer._flut_pack()
        if secondaryFixed is not None:
            props["secondaryFixed"] = secondaryFixed._flut_pack()
        if secondaryFixedDim is not None:
            props["secondaryFixedDim"] = secondaryFixedDim._flut_pack()
        if onSecondaryFixed is not None:
            props["onSecondaryFixed"] = onSecondaryFixed._flut_pack()
        if onSecondaryFixedVariant is not None:
            props["onSecondaryFixedVariant"] = onSecondaryFixedVariant._flut_pack()
        if tertiary is not None:
            props["tertiary"] = tertiary._flut_pack()
        if onTertiary is not None:
            props["onTertiary"] = onTertiary._flut_pack()
        if tertiaryContainer is not None:
            props["tertiaryContainer"] = tertiaryContainer._flut_pack()
        if onTertiaryContainer is not None:
            props["onTertiaryContainer"] = onTertiaryContainer._flut_pack()
        if tertiaryFixed is not None:
            props["tertiaryFixed"] = tertiaryFixed._flut_pack()
        if tertiaryFixedDim is not None:
            props["tertiaryFixedDim"] = tertiaryFixedDim._flut_pack()
        if onTertiaryFixed is not None:
            props["onTertiaryFixed"] = onTertiaryFixed._flut_pack()
        if onTertiaryFixedVariant is not None:
            props["onTertiaryFixedVariant"] = onTertiaryFixedVariant._flut_pack()
        if errorContainer is not None:
            props["errorContainer"] = errorContainer._flut_pack()
        if onErrorContainer is not None:
            props["onErrorContainer"] = onErrorContainer._flut_pack()
        if surfaceDim is not None:
            props["surfaceDim"] = surfaceDim._flut_pack()
        if surfaceBright is not None:
            props["surfaceBright"] = surfaceBright._flut_pack()
        if surfaceContainerLowest is not None:
            props["surfaceContainerLowest"] = surfaceContainerLowest._flut_pack()
        if surfaceContainerLow is not None:
            props["surfaceContainerLow"] = surfaceContainerLow._flut_pack()
        if surfaceContainer is not None:
            props["surfaceContainer"] = surfaceContainer._flut_pack()
        if surfaceContainerHigh is not None:
            props["surfaceContainerHigh"] = surfaceContainerHigh._flut_pack()
        if surfaceContainerHighest is not None:
            props["surfaceContainerHighest"] = surfaceContainerHighest._flut_pack()
        if onSurfaceVariant is not None:
            props["onSurfaceVariant"] = onSurfaceVariant._flut_pack()
        if outline is not None:
            props["outline"] = outline._flut_pack()
        if outlineVariant is not None:
            props["outlineVariant"] = outlineVariant._flut_pack()
        if shadow is not None:
            props["shadow"] = shadow._flut_pack()
        if scrim is not None:
            props["scrim"] = scrim._flut_pack()
        if inverseSurface is not None:
            props["inverseSurface"] = inverseSurface._flut_pack()
        if onInverseSurface is not None:
            props["onInverseSurface"] = onInverseSurface._flut_pack()
        if inversePrimary is not None:
            props["inversePrimary"] = inversePrimary._flut_pack()
        if surfaceTint is not None:
            props["surfaceTint"] = surfaceTint._flut_pack()
        self._flut_create(props=props)

    @classmethod
    def fromSeed(
        cls,
        *,
        seedColor: Color,
        brightness: Brightness = Brightness.light,
        dynamicSchemeVariant: DynamicSchemeVariant = DynamicSchemeVariant.tonalSpot,
        contrastLevel: float = 0.0,
        primary: Optional[Color] = None,
        onPrimary: Optional[Color] = None,
        primaryContainer: Optional[Color] = None,
        onPrimaryContainer: Optional[Color] = None,
        primaryFixed: Optional[Color] = None,
        primaryFixedDim: Optional[Color] = None,
        onPrimaryFixed: Optional[Color] = None,
        onPrimaryFixedVariant: Optional[Color] = None,
        secondary: Optional[Color] = None,
        onSecondary: Optional[Color] = None,
        secondaryContainer: Optional[Color] = None,
        onSecondaryContainer: Optional[Color] = None,
        secondaryFixed: Optional[Color] = None,
        secondaryFixedDim: Optional[Color] = None,
        onSecondaryFixed: Optional[Color] = None,
        onSecondaryFixedVariant: Optional[Color] = None,
        tertiary: Optional[Color] = None,
        onTertiary: Optional[Color] = None,
        tertiaryContainer: Optional[Color] = None,
        onTertiaryContainer: Optional[Color] = None,
        tertiaryFixed: Optional[Color] = None,
        tertiaryFixedDim: Optional[Color] = None,
        onTertiaryFixed: Optional[Color] = None,
        onTertiaryFixedVariant: Optional[Color] = None,
        error: Optional[Color] = None,
        onError: Optional[Color] = None,
        errorContainer: Optional[Color] = None,
        onErrorContainer: Optional[Color] = None,
        outline: Optional[Color] = None,
        outlineVariant: Optional[Color] = None,
        surface: Optional[Color] = None,
        onSurface: Optional[Color] = None,
        surfaceDim: Optional[Color] = None,
        surfaceBright: Optional[Color] = None,
        surfaceContainerLowest: Optional[Color] = None,
        surfaceContainerLow: Optional[Color] = None,
        surfaceContainer: Optional[Color] = None,
        surfaceContainerHigh: Optional[Color] = None,
        surfaceContainerHighest: Optional[Color] = None,
        onSurfaceVariant: Optional[Color] = None,
        inverseSurface: Optional[Color] = None,
        onInverseSurface: Optional[Color] = None,
        inversePrimary: Optional[Color] = None,
        shadow: Optional[Color] = None,
        scrim: Optional[Color] = None,
        surfaceTint: Optional[Color] = None,
    ) -> "ColorScheme":
        instance = cls.__new__(cls)
        super(ColorScheme, instance).__init__()
        props = {
            "_flut_init": "fromSeed",
            "seedColor": seedColor._flut_pack(),
            "brightness": brightness._flut_pack(),
            "dynamicSchemeVariant": dynamicSchemeVariant._flut_pack(),
            "contrastLevel": contrastLevel,
        }
        if primary is not None:
            props["primary"] = primary._flut_pack()
        if onPrimary is not None:
            props["onPrimary"] = onPrimary._flut_pack()
        if primaryContainer is not None:
            props["primaryContainer"] = primaryContainer._flut_pack()
        if onPrimaryContainer is not None:
            props["onPrimaryContainer"] = onPrimaryContainer._flut_pack()
        if primaryFixed is not None:
            props["primaryFixed"] = primaryFixed._flut_pack()
        if primaryFixedDim is not None:
            props["primaryFixedDim"] = primaryFixedDim._flut_pack()
        if onPrimaryFixed is not None:
            props["onPrimaryFixed"] = onPrimaryFixed._flut_pack()
        if onPrimaryFixedVariant is not None:
            props["onPrimaryFixedVariant"] = onPrimaryFixedVariant._flut_pack()
        if secondary is not None:
            props["secondary"] = secondary._flut_pack()
        if onSecondary is not None:
            props["onSecondary"] = onSecondary._flut_pack()
        if secondaryContainer is not None:
            props["secondaryContainer"] = secondaryContainer._flut_pack()
        if onSecondaryContainer is not None:
            props["onSecondaryContainer"] = onSecondaryContainer._flut_pack()
        if secondaryFixed is not None:
            props["secondaryFixed"] = secondaryFixed._flut_pack()
        if secondaryFixedDim is not None:
            props["secondaryFixedDim"] = secondaryFixedDim._flut_pack()
        if onSecondaryFixed is not None:
            props["onSecondaryFixed"] = onSecondaryFixed._flut_pack()
        if onSecondaryFixedVariant is not None:
            props["onSecondaryFixedVariant"] = onSecondaryFixedVariant._flut_pack()
        if tertiary is not None:
            props["tertiary"] = tertiary._flut_pack()
        if onTertiary is not None:
            props["onTertiary"] = onTertiary._flut_pack()
        if tertiaryContainer is not None:
            props["tertiaryContainer"] = tertiaryContainer._flut_pack()
        if onTertiaryContainer is not None:
            props["onTertiaryContainer"] = onTertiaryContainer._flut_pack()
        if tertiaryFixed is not None:
            props["tertiaryFixed"] = tertiaryFixed._flut_pack()
        if tertiaryFixedDim is not None:
            props["tertiaryFixedDim"] = tertiaryFixedDim._flut_pack()
        if onTertiaryFixed is not None:
            props["onTertiaryFixed"] = onTertiaryFixed._flut_pack()
        if onTertiaryFixedVariant is not None:
            props["onTertiaryFixedVariant"] = onTertiaryFixedVariant._flut_pack()
        if error is not None:
            props["error"] = error._flut_pack()
        if onError is not None:
            props["onError"] = onError._flut_pack()
        if errorContainer is not None:
            props["errorContainer"] = errorContainer._flut_pack()
        if onErrorContainer is not None:
            props["onErrorContainer"] = onErrorContainer._flut_pack()
        if outline is not None:
            props["outline"] = outline._flut_pack()
        if outlineVariant is not None:
            props["outlineVariant"] = outlineVariant._flut_pack()
        if surface is not None:
            props["surface"] = surface._flut_pack()
        if onSurface is not None:
            props["onSurface"] = onSurface._flut_pack()
        if surfaceDim is not None:
            props["surfaceDim"] = surfaceDim._flut_pack()
        if surfaceBright is not None:
            props["surfaceBright"] = surfaceBright._flut_pack()
        if surfaceContainerLowest is not None:
            props["surfaceContainerLowest"] = surfaceContainerLowest._flut_pack()
        if surfaceContainerLow is not None:
            props["surfaceContainerLow"] = surfaceContainerLow._flut_pack()
        if surfaceContainer is not None:
            props["surfaceContainer"] = surfaceContainer._flut_pack()
        if surfaceContainerHigh is not None:
            props["surfaceContainerHigh"] = surfaceContainerHigh._flut_pack()
        if surfaceContainerHighest is not None:
            props["surfaceContainerHighest"] = surfaceContainerHighest._flut_pack()
        if onSurfaceVariant is not None:
            props["onSurfaceVariant"] = onSurfaceVariant._flut_pack()
        if inverseSurface is not None:
            props["inverseSurface"] = inverseSurface._flut_pack()
        if onInverseSurface is not None:
            props["onInverseSurface"] = onInverseSurface._flut_pack()
        if inversePrimary is not None:
            props["inversePrimary"] = inversePrimary._flut_pack()
        if shadow is not None:
            props["shadow"] = shadow._flut_pack()
        if scrim is not None:
            props["scrim"] = scrim._flut_pack()
        if surfaceTint is not None:
            props["surfaceTint"] = surfaceTint._flut_pack()
        instance._flut_create(props=props)
        return instance

    @property
    def brightness(self) -> Brightness:
        return self._flut_get("brightness")

    @property
    def primary(self) -> Color:
        return self._flut_get("primary")

    @property
    def onPrimary(self) -> Color:
        return self._flut_get("onPrimary")

    @property
    def primaryContainer(self) -> Color:
        return self._flut_get("primaryContainer")

    @property
    def onPrimaryContainer(self) -> Color:
        return self._flut_get("onPrimaryContainer")

    @property
    def primaryFixed(self) -> Color:
        return self._flut_get("primaryFixed")

    @property
    def primaryFixedDim(self) -> Color:
        return self._flut_get("primaryFixedDim")

    @property
    def onPrimaryFixed(self) -> Color:
        return self._flut_get("onPrimaryFixed")

    @property
    def onPrimaryFixedVariant(self) -> Color:
        return self._flut_get("onPrimaryFixedVariant")

    @property
    def secondary(self) -> Color:
        return self._flut_get("secondary")

    @property
    def onSecondary(self) -> Color:
        return self._flut_get("onSecondary")

    @property
    def secondaryContainer(self) -> Color:
        return self._flut_get("secondaryContainer")

    @property
    def onSecondaryContainer(self) -> Color:
        return self._flut_get("onSecondaryContainer")

    @property
    def secondaryFixed(self) -> Color:
        return self._flut_get("secondaryFixed")

    @property
    def secondaryFixedDim(self) -> Color:
        return self._flut_get("secondaryFixedDim")

    @property
    def onSecondaryFixed(self) -> Color:
        return self._flut_get("onSecondaryFixed")

    @property
    def onSecondaryFixedVariant(self) -> Color:
        return self._flut_get("onSecondaryFixedVariant")

    @property
    def tertiary(self) -> Color:
        return self._flut_get("tertiary")

    @property
    def onTertiary(self) -> Color:
        return self._flut_get("onTertiary")

    @property
    def tertiaryContainer(self) -> Color:
        return self._flut_get("tertiaryContainer")

    @property
    def onTertiaryContainer(self) -> Color:
        return self._flut_get("onTertiaryContainer")

    @property
    def tertiaryFixed(self) -> Color:
        return self._flut_get("tertiaryFixed")

    @property
    def tertiaryFixedDim(self) -> Color:
        return self._flut_get("tertiaryFixedDim")

    @property
    def onTertiaryFixed(self) -> Color:
        return self._flut_get("onTertiaryFixed")

    @property
    def onTertiaryFixedVariant(self) -> Color:
        return self._flut_get("onTertiaryFixedVariant")

    @property
    def error(self) -> Color:
        return self._flut_get("error")

    @property
    def onError(self) -> Color:
        return self._flut_get("onError")

    @property
    def errorContainer(self) -> Color:
        return self._flut_get("errorContainer")

    @property
    def onErrorContainer(self) -> Color:
        return self._flut_get("onErrorContainer")

    @property
    def surface(self) -> Color:
        return self._flut_get("surface")

    @property
    def onSurface(self) -> Color:
        return self._flut_get("onSurface")

    @property
    def surfaceDim(self) -> Color:
        return self._flut_get("surfaceDim")

    @property
    def surfaceBright(self) -> Color:
        return self._flut_get("surfaceBright")

    @property
    def surfaceContainerLowest(self) -> Color:
        return self._flut_get("surfaceContainerLowest")

    @property
    def surfaceContainerLow(self) -> Color:
        return self._flut_get("surfaceContainerLow")

    @property
    def surfaceContainer(self) -> Color:
        return self._flut_get("surfaceContainer")

    @property
    def surfaceContainerHigh(self) -> Color:
        return self._flut_get("surfaceContainerHigh")

    @property
    def surfaceContainerHighest(self) -> Color:
        return self._flut_get("surfaceContainerHighest")

    @property
    def onSurfaceVariant(self) -> Color:
        return self._flut_get("onSurfaceVariant")

    @property
    def outline(self) -> Color:
        return self._flut_get("outline")

    @property
    def outlineVariant(self) -> Color:
        return self._flut_get("outlineVariant")

    @property
    def shadow(self) -> Color:
        return self._flut_get("shadow")

    @property
    def scrim(self) -> Color:
        return self._flut_get("scrim")

    @property
    def inversePrimary(self) -> Color:
        return self._flut_get("inversePrimary")

    @property
    def inverseSurface(self) -> Color:
        return self._flut_get("inverseSurface")

    @property
    def onInverseSurface(self) -> Color:
        return self._flut_get("onInverseSurface")

    @property
    def surfaceTint(self) -> Color:
        return self._flut_get("surfaceTint")
