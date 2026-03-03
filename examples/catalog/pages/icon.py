from flut.dart import BlendMode, Offset, Shadow, TextAlign, TextDirection
from flut.dart.ui import Color
from flut.flutter.material import Colors, Icons
from flut.flutter.painting import BorderRadius, BoxDecoration, EdgeInsets, TextStyle
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.widgets import (
    Center,
    Column,
    Container,
    Icon,
    Row,
    SizedBox,
    State,
    StatefulWidget,
    StatelessWidget,
    Text,
    Wrap,
)
from flut.flutter.widgets.icon_data import IconData
from widgets import CatalogPage, CodeArea, SplitViewTile


def _icon_card(child, label):
    return Column(
        children=[
            Container(
                width=72,
                height=72,
                decoration=BoxDecoration(
                    color=Color(0xFFF5F5F5),
                    borderRadius=BorderRadius.circular(12),
                ),
                child=Center(child=child),
            ),
            SizedBox(height=4),
            Text(label, style=TextStyle(fontSize=11, color=Colors.grey)),
        ],
    )


class _BasicIconDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=24,
            runSpacing=16,
            children=[
                _icon_card(Icon(Icons.home, size=32, color=Colors.blue), "home"),
                _icon_card(Icon(Icons.star, size=32, color=Colors.amber), "star"),
                _icon_card(
                    Icon(Icons.settings, size=32, color=Colors.grey), "settings"
                ),
                _icon_card(Icon(Icons.favorite, size=32, color=Colors.red), "favorite"),
                _icon_card(Icon(Icons.search, size=32, color=Colors.teal), "search"),
            ],
        )


class _IconSizeDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=24,
            runSpacing=16,
            children=[
                _icon_card(Icon(Icons.star, size=16, color=Colors.blue), "16"),
                _icon_card(Icon(Icons.star, size=24, color=Colors.blue), "24"),
                _icon_card(Icon(Icons.star, size=32, color=Colors.blue), "32"),
                _icon_card(Icon(Icons.star, size=48, color=Colors.blue), "48"),
                _icon_card(Icon(Icons.star, size=64, color=Colors.blue), "64"),
            ],
        )


class _IconColorDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=24,
            runSpacing=16,
            children=[
                _icon_card(Icon(Icons.circle, size=36, color=Colors.red), "red"),
                _icon_card(Icon(Icons.circle, size=36, color=Colors.green), "green"),
                _icon_card(Icon(Icons.circle, size=36, color=Colors.blue), "blue"),
                _icon_card(Icon(Icons.circle, size=36, color=Colors.orange), "orange"),
                _icon_card(Icon(Icons.circle, size=36, color=Colors.purple), "purple"),
                _icon_card(
                    Icon(Icons.circle, size=36, color=Color(0x80FF0000)),
                    "50% alpha",
                ),
            ],
        )


class _IconShadowsDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=32,
            runSpacing=16,
            children=[
                _icon_card(
                    Icon(
                        Icons.star,
                        size=40,
                        color=Colors.amber,
                        shadows=[
                            Shadow(
                                color=Color(0x66000000),
                                offset=Offset(2, 2),
                                blurRadius=4.0,
                            ),
                        ],
                    ),
                    "single shadow",
                ),
                _icon_card(
                    Icon(
                        Icons.star,
                        size=40,
                        color=Colors.blue,
                        shadows=[
                            Shadow(
                                color=Color(0x440000FF),
                                offset=Offset(0, 0),
                                blurRadius=12.0,
                            ),
                        ],
                    ),
                    "glow effect",
                ),
                _icon_card(
                    Icon(
                        Icons.star,
                        size=40,
                        color=Colors.red,
                        shadows=[
                            Shadow(
                                color=Color(0x66000000),
                                offset=Offset(1, 1),
                                blurRadius=2.0,
                            ),
                            Shadow(
                                color=Color(0x33FF0000),
                                offset=Offset(3, 3),
                                blurRadius=8.0,
                            ),
                        ],
                    ),
                    "double shadow",
                ),
            ],
        )


class _IconBlendModeDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=24,
            runSpacing=16,
            children=[
                _icon_card(
                    Icon(
                        Icons.favorite,
                        size=36,
                        color=Colors.red,
                        blendMode=BlendMode.srcOver,
                    ),
                    "srcOver",
                ),
                _icon_card(
                    Icon(
                        Icons.favorite,
                        size=36,
                        color=Colors.red,
                        blendMode=BlendMode.multiply,
                    ),
                    "multiply",
                ),
                _icon_card(
                    Icon(
                        Icons.favorite,
                        size=36,
                        color=Colors.red,
                        blendMode=BlendMode.screen,
                    ),
                    "screen",
                ),
                _icon_card(
                    Icon(
                        Icons.favorite,
                        size=36,
                        color=Colors.red,
                        blendMode=BlendMode.overlay,
                    ),
                    "overlay",
                ),
            ],
        )


_ARROW_BACK_DIRECTIONAL = IconData(
    0xE092, fontFamily="MaterialIcons", matchTextDirection=True
)


class _IconTextDirectionDemo(StatelessWidget):
    def build(self, context):
        return Wrap(
            spacing=32,
            runSpacing=16,
            children=[
                _icon_card(
                    Icon(
                        _ARROW_BACK_DIRECTIONAL,
                        size=36,
                        textDirection=TextDirection.ltr,
                    ),
                    "LTR",
                ),
                _icon_card(
                    Icon(
                        _ARROW_BACK_DIRECTIONAL,
                        size=36,
                        textDirection=TextDirection.rtl,
                    ),
                    "RTL",
                ),
            ],
        )


class _IconThemeDataDemo(StatefulWidget):
    def createState(self):
        return _IconThemeDataDemoState()


class _IconThemeDataDemoState(State["_IconThemeDataDemo"]):

    def initState(self):
        pass

    def build(self, context):
        configs = [
            ("Size 32\nBlue", Icons.home, 32.0, Colors.blue, 1.0),
            ("Size 48\nRed", Icons.star, 48.0, Colors.red, 1.0),
            ("Size 40\nGreen\n0.5 opacity", Icons.settings, 40.0, Colors.green, 0.5),
            ("Size 28\nPurple", Icons.favorite, 28.0, Colors.deepPurple, 1.0),
        ]
        children = []
        for i, (label, icon, size, color, opacity) in enumerate(configs):
            if i > 0:
                children.append(SizedBox(width=24))
            children.append(
                Column(
                    children=[
                        Icon(
                            icon,
                            size=size,
                            color=color.withValues(alpha=opacity),
                        ),
                        SizedBox(height=4),
                        Text(
                            label,
                            style=TextStyle(fontSize=10),
                            textAlign=TextAlign.center,
                        ),
                    ],
                ),
            )
        return Row(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=children,
        )


class IconPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Icon",
            description=(
                "Shows how icons communicate through size, color, directionality, "
                "theming, and visual effects across common interface states."
            ),
            children=[
                SplitViewTile(
                    title="Basic Icons",
                    description="The Icon widget renders a glyph from a font described by an IconData. Material Icons are provided by the Icons class.",
                    instruction="Five material icons are shown with different colors. Each uses Icons.<name> for its glyph.",
                    visible=_BasicIconDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Icon(Icons.home, size=32, color=Colors.blue)\n"
                            "Icon(Icons.star, size=32, color=Colors.amber)\n"
                            "Icon(Icons.favorite, size=32, color=Colors.red)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Icon Size",
                    description="The size parameter sets the icon's logical pixel size. Defaults to 24 if not specified.",
                    instruction="Compare the same icon rendered at sizes 16, 24, 32, 48, and 64.",
                    visible=_IconSizeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Icon(Icons.star, size=16)\n"
                            "Icon(Icons.star, size=48)\n"
                            "Icon(Icons.star, size=64)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Icon Color",
                    description="The color parameter sets the icon's foreground color. Supports named colors from Colors and arbitrary ARGB Color values including alpha transparency.",
                    instruction="Six circles show different named colors and one with 50% alpha.",
                    visible=_IconColorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Icon(Icons.circle, size=36, color=Colors.red)\n"
                            "Icon(Icons.circle, size=36,\n"
                            "     color=Color(0x80FF0000))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Icon Shadows",
                    description="The shadows parameter accepts a list of Shadow objects, each with color, offset, and blurRadius. Multiple shadows stack for richer effects.",
                    instruction="Three star icons demonstrate a drop shadow, a glow effect, and a double-shadow stack.",
                    visible=_IconShadowsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.dart import Shadow, Offset\n\n"
                            "Icon(\n"
                            "    Icons.star, size=40,\n"
                            "    color=Colors.amber,\n"
                            "    shadows=[\n"
                            "        Shadow(\n"
                            "            color=Color(0x66000000),\n"
                            "            offset=Offset(2, 2),\n"
                            "            blurRadius=4.0,\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Icon Blend Mode",
                    description="blendMode controls how the icon is composited against its background. Common modes include srcOver, multiply, screen, and overlay.",
                    instruction="Four hearts render with different blend modes over the default background.",
                    visible=_IconBlendModeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.dart import BlendMode\n\n"
                            "Icon(Icons.favorite, size=36,\n"
                            "     color=Colors.red,\n"
                            "     blendMode=BlendMode.multiply)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Icon Text Direction",
                    description="textDirection controls the reading direction for directional icons. The icon must have matchTextDirection=True in its IconData for this to take effect.",
                    instruction="The arrow_back icon is built with matchTextDirection=True. In LTR mode the arrow points left; in RTL mode it is mirrored to point right.",
                    visible=_IconTextDirectionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.dart import TextDirection\n"
                            "from flut.flutter.widgets.icon_data import IconData\n\n"
                            "arrow = IconData(\n"
                            "    0xE092,\n"
                            "    fontFamily='MaterialIcons',\n"
                            "    matchTextDirection=True,\n"
                            ")\n\n"
                            "Icon(arrow, size=36,\n"
                            "     textDirection=TextDirection.ltr)\n"
                            "Icon(arrow, size=36,\n"
                            "     textDirection=TextDirection.rtl)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconData fontFamilyFallback",
                    description="fontFamilyFallback provides an ordered list of font families to try when a glyph is not available in the primary fontFamily. This is useful for icons that may need platform-specific fallback fonts.",
                    instruction="Two icons are shown: one with only the primary fontFamily, and one with fontFamilyFallback specified. Both render the same Material Icons glyph.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Icon(
                                        IconData(
                                            0xE318,
                                            fontFamily="MaterialIcons",
                                        ),
                                        size=36,
                                    ),
                                    SizedBox(height=4),
                                    Text("No fallback", style=TextStyle(fontSize=11)),
                                ],
                            ),
                            SizedBox(width=24),
                            Column(
                                children=[
                                    Icon(
                                        IconData(
                                            0xE318,
                                            fontFamily="MaterialIcons",
                                            fontFamilyFallback=["Arial", "Roboto"],
                                        ),
                                        size=36,
                                    ),
                                    SizedBox(height=4),
                                    Text("With fallback", style=TextStyle(fontSize=11)),
                                ],
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets.icon_data import IconData\n\n"
                            "IconData(0xE318, fontFamily='MaterialIcons')\n\n"
                            "IconData(\n"
                            "    0xE318,\n"
                            "    fontFamily='MaterialIcons',\n"
                            "    fontFamilyFallback=['Arial', 'Roboto'],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconThemeData Effects",
                    description=(
                        "Icons rendered with varying size, color, and opacity to demonstrate "
                        "the visual properties that IconThemeData controls."
                    ),
                    instruction="Four icons displayed with different size, color, and opacity settings.",
                    visible=_IconThemeDataDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Icon(\n"
                            "    Icons.home,\n"
                            "    size=32.0,\n"
                            "    color=Colors.blue,\n"
                            ")\n"
                            "\n"
                            "IconThemeData(\n"
                            "    size=32.0,\n"
                            "    color=Colors.blue,\n"
                            "    opacity=1.0,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
