from flut.dart import Brightness
from flut.dart.ui import Color, FontWeight
from flut.flutter.material import (
    Colors,
    ColorScheme,
    DynamicSchemeVariant,
    Theme,
)
from flut.flutter.painting import BorderRadius, BoxDecoration, EdgeInsets, TextStyle
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.widgets import (
    Column,
    Container,
    Row,
    SizedBox,
    State,
    StatefulWidget,
    StatelessWidget,
    Text,
    Wrap,
)
from widgets import CatalogPage, CodeArea, SplitViewTile

_SURFACE_TONES = [
    ("surfaceContainerLowest", lambda cs: cs.surfaceContainerLowest),
    ("surfaceContainerLow", lambda cs: cs.surfaceContainerLow),
    ("surfaceContainer", lambda cs: cs.surfaceContainer),
    ("surfaceContainerHigh", lambda cs: cs.surfaceContainerHigh),
    ("surfaceContainerHighest", lambda cs: cs.surfaceContainerHighest),
]


_VARIANTS = [
    ("tonalSpot", DynamicSchemeVariant.tonalSpot),
    ("fidelity", DynamicSchemeVariant.fidelity),
    ("monochrome", DynamicSchemeVariant.monochrome),
    ("neutral", DynamicSchemeVariant.neutral),
    ("vibrant", DynamicSchemeVariant.vibrant),
    ("expressive", DynamicSchemeVariant.expressive),
    ("content", DynamicSchemeVariant.content),
    ("rainbow", DynamicSchemeVariant.rainbow),
    ("fruitSalad", DynamicSchemeVariant.fruitSalad),
]


def _swatch(color, label, *, on_color=None, width=120.0, height=56.0):
    text_color = on_color or Colors.black
    return Column(
        crossAxisAlignment=CrossAxisAlignment.start,
        children=[
            Container(
                width=width,
                height=height,
                decoration=BoxDecoration(
                    color=color,
                    borderRadius=BorderRadius.circular(8),
                ),
                padding=EdgeInsets.all(8),
                child=Text(
                    label,
                    style=TextStyle(
                        fontSize=11,
                        fontWeight=FontWeight.w600,
                        color=text_color,
                    ),
                ),
            ),
            SizedBox(height=4),
        ],
    )


class _SurfaceContainerDemo(StatelessWidget):
    def build(self, context):
        cs = Theme.of(context).colorScheme
        return Wrap(
            spacing=12,
            runSpacing=12,
            children=[
                _swatch(getter(cs), name, on_color=cs.onSurface)
                for name, getter in _SURFACE_TONES
            ],
        )


class _VariantSwatchRow(StatelessWidget):
    def __init__(self, *, name, scheme, key=None):
        super().__init__(key=key)
        self.name = name
        self.scheme = scheme

    def build(self, context):
        cs = self.scheme
        cells = [
            (cs.primary, cs.onPrimary, "primary"),
            (cs.secondary, cs.onSecondary, "secondary"),
            (cs.tertiary, cs.onTertiary, "tertiary"),
            (cs.surfaceContainerHigh, cs.onSurface, "surfaceContainerHigh"),
        ]
        return Row(
            crossAxisAlignment=CrossAxisAlignment.center,
            children=[
                Container(
                    width=120,
                    child=Text(
                        self.name,
                        style=TextStyle(
                            fontSize=12,
                            fontWeight=FontWeight.w600,
                        ),
                    ),
                ),
                SizedBox(width=8),
                Row(
                    children=[
                        Container(
                            width=110,
                            height=44,
                            margin=EdgeInsets.only(right=6),
                            decoration=BoxDecoration(
                                color=bg,
                                borderRadius=BorderRadius.circular(6),
                            ),
                            padding=EdgeInsets.all(6),
                            child=Text(
                                label,
                                style=TextStyle(
                                    fontSize=10,
                                    color=fg,
                                    fontWeight=FontWeight.w500,
                                ),
                            ),
                        )
                        for bg, fg, label in cells
                    ],
                ),
            ],
        )


class _DynamicSchemeVariantDemo(StatefulWidget):
    def createState(self):
        return _DynamicSchemeVariantDemoState()


class _DynamicSchemeVariantDemoState(State[_DynamicSchemeVariantDemo]):
    def initState(self):
        self.seed = Colors.blue
        self.brightness = Brightness.light
        self.schemes = self._build_schemes()

    def _build_schemes(self):
        return [
            (
                name,
                ColorScheme.fromSeed(
                    seedColor=self.seed,
                    brightness=self.brightness,
                    dynamicSchemeVariant=variant,
                ),
            )
            for name, variant in _VARIANTS
        ]

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "Seed: Colors.blue, brightness: light",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Container(
                            margin=EdgeInsets.only(bottom=8),
                            child=_VariantSwatchRow(name=name, scheme=scheme),
                        )
                        for name, scheme in self.schemes
                    ],
                ),
            ],
        )


class ThemePage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Theme",
            description=(
                "Material 3 ColorScheme features: surface container tonal layers "
                "and DynamicSchemeVariant generation algorithms."
            ),
            children=[
                SplitViewTile(
                    title="Surface Container Tones",
                    description=(
                        "Material 3 defines five surface container tones used "
                        "to elevate UI surfaces without shadows. Read them from "
                        "Theme.of(context).colorScheme."
                    ),
                    instruction=(
                        "Toggle dark mode in the app bar to see how each tone "
                        "shifts. surfaceContainerHigh sits between Container "
                        "and ContainerHighest in elevation."
                    ),
                    visible=_SurfaceContainerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "cs = Theme.of(context).colorScheme\n"
                            "Container(\n"
                            "    color=cs.surfaceContainerHigh,\n"
                            "    child=Text('Card', style=TextStyle(\n"
                            "        color=cs.onSurface,\n"
                            "    )),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DynamicSchemeVariant",
                    description=(
                        "ColorScheme.fromSeed accepts a dynamicSchemeVariant "
                        "to control how the palette is derived from the seed. "
                        "Each variant uses a different Material You algorithm: "
                        "monochrome strips hue entirely, vibrant boosts "
                        "saturation, fidelity stays close to the seed, etc."
                    ),
                    instruction=(
                        "Each row shows primary / secondary / tertiary / "
                        "surfaceContainerHigh produced by ColorScheme.fromSeed "
                        "with the same seed but a different variant."
                    ),
                    visible=_DynamicSchemeVariantDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.material import (\n"
                            "    ColorScheme, DynamicSchemeVariant,\n"
                            ")\n\n"
                            "ColorScheme.fromSeed(\n"
                            "    seedColor=Colors.blue,\n"
                            "    brightness=Brightness.light,\n"
                            "    dynamicSchemeVariant=\n"
                            "        DynamicSchemeVariant.monochrome,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
