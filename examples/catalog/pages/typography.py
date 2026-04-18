from flut.flutter.painting import TextOverflow
from utils import CODE_FONT_FAMILY
from flut.dart import Color, TextAlign
from flut.flutter.widgets import (
    StatelessWidget,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Expanded,
    Padding,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    Theme,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    TextSpan,
    BorderRadius,
    BoxDecoration,
)
from flut.dart.ui import (
    TextDirection,
    FontStyle,
    TextDecoration,
    TextDecorationStyle,
    TextLeadingDistribution,
)
from flut.flutter.painting import TextWidthBasis
from widgets import CatalogPage, SplitViewTile, CodeArea

WEIGHTS = [
    ("w100", FontWeight.w100, "Thin"),
    ("w200", FontWeight.w200, "Extra Light"),
    ("w300", FontWeight.w300, "Light"),
    ("w400 (normal)", FontWeight.w400, "Normal / Regular"),
    ("w500", FontWeight.w500, "Medium"),
    ("w600", FontWeight.w600, "Semi Bold"),
    ("w700 (bold)", FontWeight.w700, "Bold"),
    ("w800", FontWeight.w800, "Extra Bold"),
    ("w900", FontWeight.w900, "Black"),
]

FONT_SIZES = [10, 12, 14, 16, 18, 20, 24, 28, 32]


class _FontWeightsDemo(StatelessWidget):
    def build(self, context):
        sample_text = "The quick brown fox jumps over the lazy dog"
        rows = []
        for name, weight, description in WEIGHTS:
            rows.append(
                Padding(
                    padding=EdgeInsets.symmetric(vertical=6),
                    child=Row(
                        crossAxisAlignment=CrossAxisAlignment.center,
                        children=[
                            Container(
                                width=140.0,
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            name,
                                            style=TextStyle(
                                                fontSize=13,
                                                fontWeight=FontWeight.bold,
                                                color=Colors.blue,
                                            ),
                                        ),
                                        Text(
                                            description,
                                            style=TextStyle(
                                                fontSize=11, color=Colors.grey
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            Expanded(
                                child=Text(
                                    sample_text,
                                    style=TextStyle(
                                        fontSize=16,
                                        fontWeight=weight,
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
            )
        return Container(
            padding=EdgeInsets.all(16),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.03),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=rows,
            ),
        )


class _FontSizesDemo(StatelessWidget):
    def build(self, context):
        rows = []
        for size in FONT_SIZES:
            rows.append(
                Padding(
                    padding=EdgeInsets.symmetric(vertical=4),
                    child=Row(
                        crossAxisAlignment=CrossAxisAlignment.center,
                        children=[
                            Container(
                                width=60.0,
                                child=Text(
                                    f"{size}px",
                                    style=TextStyle(
                                        fontSize=12,
                                        color=Colors.grey,
                                        fontFamily=CODE_FONT_FAMILY,
                                    ),
                                ),
                            ),
                            Text(
                                "Hello, Flut!",
                                style=TextStyle(fontSize=float(size)),
                            ),
                        ],
                    ),
                ),
            )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=rows,
        )


class _ThemeTextStyleDemo(StatelessWidget):
    def build(self, context):
        theme_data = Theme.of(context)
        text_theme = theme_data.textTheme
        styles = [
            ("displayLarge", text_theme.displayLarge),
            ("displayMedium", text_theme.displayMedium),
            ("displaySmall", text_theme.displaySmall),
            ("headlineLarge", text_theme.headlineLarge),
            ("headlineMedium", text_theme.headlineMedium),
            ("headlineSmall", text_theme.headlineSmall),
            ("titleLarge", text_theme.titleLarge),
            ("titleMedium", text_theme.titleMedium),
            ("titleSmall", text_theme.titleSmall),
            ("bodyLarge", text_theme.bodyLarge),
            ("bodyMedium", text_theme.bodyMedium),
            ("bodySmall", text_theme.bodySmall),
            ("labelLarge", text_theme.labelLarge),
            ("labelMedium", text_theme.labelMedium),
            ("labelSmall", text_theme.labelSmall),
        ]
        rows = []
        for name, style in styles:
            if style:
                rows.append(
                    Padding(
                        padding=EdgeInsets.symmetric(vertical=2),
                        child=Text(
                            name,
                            style=style,
                        ),
                    ),
                )
        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.05),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=rows,
            ),
        )


class _RichTextDemo(StatelessWidget):
    def build(self, context):
        on_surface = Theme.of(context).colorScheme.onSurface
        return Container(
            padding=EdgeInsets.all(16),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.03),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text.rich(
                        TextSpan(
                            children=[
                                TextSpan(
                                    text="Hello ",
                                    style=TextStyle(fontSize=18, color=on_surface),
                                ),
                                TextSpan(
                                    text="bold ",
                                    style=TextStyle(
                                        fontSize=18,
                                        fontWeight=FontWeight.bold,
                                        color=Colors.blue,
                                    ),
                                ),
                                TextSpan(
                                    text="world!",
                                    style=TextStyle(fontSize=18, color=on_surface),
                                ),
                            ],
                        ),
                    ),
                    SizedBox(height=12),
                    Text.rich(
                        TextSpan(
                            text="Mixed styles: ",
                            style=TextStyle(fontSize=16),
                            children=[
                                TextSpan(
                                    text="red",
                                    style=TextStyle(
                                        color=Colors.red,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                TextSpan(text=", "),
                                TextSpan(
                                    text="green",
                                    style=TextStyle(
                                        color=Colors.green,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                TextSpan(text=", and "),
                                TextSpan(
                                    text="blue",
                                    style=TextStyle(
                                        color=Colors.blue,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                TextSpan(text="."),
                            ],
                        ),
                    ),
                    SizedBox(height=12),
                    Text.rich(
                        TextSpan(
                            children=[
                                TextSpan(
                                    text="Small ",
                                    style=TextStyle(fontSize=12),
                                ),
                                TextSpan(
                                    text="Medium ",
                                    style=TextStyle(fontSize=18),
                                ),
                                TextSpan(
                                    text="Large",
                                    style=TextStyle(
                                        fontSize=28,
                                        fontWeight=FontWeight.w900,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


class _TextStylePropertiesDemo(StatelessWidget):
    def build(self, context):
        return Container(
            padding=EdgeInsets.all(16),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.03),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        "Letter Spacing: 4.0",
                        style=TextStyle(fontSize=16, letterSpacing=4.0),
                    ),
                    SizedBox(height=8),
                    Text(
                        "Word Spacing: 12.0",
                        style=TextStyle(fontSize=16, wordSpacing=12.0),
                    ),
                    SizedBox(height=8),
                    Text(
                        "Background Color",
                        style=TextStyle(
                            fontSize=16,
                            backgroundColor=Colors.yellow.withValues(alpha=0.5),
                        ),
                    ),
                    SizedBox(height=8),
                    Text(
                        "Height: 2.5 — This text has extra line\nheight applied between lines.",
                        style=TextStyle(fontSize=16, height=2.5),
                    ),
                ],
            ),
        )


class _TextPropertiesDemo(StatelessWidget):
    def build(self, context):
        return Container(
            padding=EdgeInsets.all(16),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.03),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        "Right-to-left text direction\u200f \u0645\u0631\u062d\u0628\u0627",
                        style=TextStyle(fontSize=16),
                        textDirection=TextDirection.rtl,
                    ),
                    SizedBox(height=8),
                    Text(
                        "Max 1 line with overflow ellipsis — this text is intentionally very long to demonstrate truncation behavior",
                        style=TextStyle(fontSize=16),
                        maxLines=1,
                        overflow=TextOverflow.ellipsis,
                    ),
                    SizedBox(height=8),
                    Text(
                        "Semantic label for accessibility",
                        style=TextStyle(fontSize=16),
                        semanticsLabel="Custom semantic label",
                    ),
                ],
            ),
        )


def _overflow_box(label, overflow):
    return Container(
        width=130.0,
        padding=EdgeInsets.all(6),
        decoration=BoxDecoration(
            color=Color(0xFFF5F5F5),
            borderRadius=BorderRadius.circular(6),
        ),
        child=Text(
            f"{label}: This is a long text that will overflow the container",
            maxLines=1,
            overflow=overflow,
            style=TextStyle(fontSize=12),
        ),
    )


class TypographyPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Typography & FontWeight",
            description=(
                "Explores text hierarchy through weight, size, color, theme styles, "
                "and rich spans so typography choices are easy to compare visually."
            ),
            children=[
                SplitViewTile(
                    title="Font Weights",
                    description="All 9 FontWeight values from w100 (Thin) to w900 (Black), each rendering the same sample sentence.",
                    instruction="Compare how each weight renders the sample text from thinnest to heaviest.",
                    visible=_FontWeightsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Hello, Flut!',\n"
                            "    style=TextStyle(\n"
                            "        fontSize=16,\n"
                            "        fontWeight=FontWeight.w700,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Font Sizes",
                    description="Text rendered at sizes from 10px to 32px to preview the available size range.",
                    instruction="Observe how text scales across different pixel sizes.",
                    visible=_FontSizesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Hello, Flut!',\n"
                            "    style=TextStyle(fontSize=24.0),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Text Colors",
                    description="Text rendered in different Material colors using the color property of TextStyle.",
                    instruction="View each color name rendered in its corresponding Material color.",
                    visible=Row(
                        children=[
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Red",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.red,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Blue",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.blue,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Green",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.green,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Orange",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.orange,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Purple",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.purple,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Teal",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.teal,
                                    ),
                                ),
                            ),
                            Padding(
                                padding=EdgeInsets.only(right=16, bottom=4),
                                child=Text(
                                    "Grey",
                                    style=TextStyle(
                                        fontSize=15,
                                        fontWeight=FontWeight.w600,
                                        color=Colors.grey,
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Red',\n"
                            "    style=TextStyle(\n"
                            "        fontSize=15,\n"
                            "        fontWeight=FontWeight.w600,\n"
                            "        color=Colors.red,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Theme TextStyle",
                    description="All 15 Material 3 text styles from the current ThemeData, each rendered in its own resolved style.",
                    instruction="Each label renders using its own theme style. Switch between light and dark theme to see how styles change.",
                    visible=_ThemeTextStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "theme = Theme.of(context)\n"
                            "text_theme = theme.textTheme\n\n"
                            "Text('headlineMedium', style=text_theme.headlineMedium)\n"
                            "Text('bodyLarge', style=text_theme.bodyLarge)\n"
                            "Text('labelSmall', style=text_theme.labelSmall)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextStyle Properties",
                    description="TextStyle supports letterSpacing, wordSpacing, backgroundColor, and height for fine-grained text layout control.",
                    instruction="Observe letter spacing widening characters, word spacing widening gaps, background highlight behind text, and increased line height.",
                    visible=_TextStylePropertiesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextStyle(fontSize=16, letterSpacing=4.0)\n"
                            "TextStyle(fontSize=16, wordSpacing=12.0)\n"
                            "TextStyle(fontSize=16, backgroundColor=Colors.yellow)\n"
                            "TextStyle(fontSize=16, height=2.5)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextDecoration",
                    description=(
                        "TextDecoration is a bitmask value with four built-in constants — "
                        "none, underline, overline, lineThrough — that can be combined with "
                        "the | operator or TextDecoration.combine([...]) to apply multiple "
                        "lines simultaneously. Pair with decorationColor / decorationStyle / "
                        "decorationThickness to customize each line."
                    ),
                    instruction=(
                        "Compare each decoration: single lines (underline, overline, "
                        "lineThrough), the combined underline | overline, and a styled "
                        "wavy red underline using decorationStyle and decorationColor."
                    ),
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "TextDecoration.none — plain text",
                                style=TextStyle(
                                    fontSize=16, decoration=TextDecoration.none
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "TextDecoration.underline",
                                style=TextStyle(
                                    fontSize=16, decoration=TextDecoration.underline
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "TextDecoration.overline",
                                style=TextStyle(
                                    fontSize=16, decoration=TextDecoration.overline
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "TextDecoration.lineThrough",
                                style=TextStyle(
                                    fontSize=16, decoration=TextDecoration.lineThrough
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "underline | overline (combined via | operator)",
                                style=TextStyle(
                                    fontSize=16,
                                    decoration=TextDecoration.underline
                                    | TextDecoration.overline,
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "TextDecoration.combine([underline, lineThrough])",
                                style=TextStyle(
                                    fontSize=16,
                                    decoration=TextDecoration.combine(
                                        [
                                            TextDecoration.underline,
                                            TextDecoration.lineThrough,
                                        ]
                                    ),
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "Wavy red underline (decorationStyle + decorationColor)",
                                style=TextStyle(
                                    fontSize=16,
                                    decoration=TextDecoration.underline,
                                    decorationStyle=TextDecorationStyle.wavy,
                                    decorationColor=Colors.red,
                                    decorationThickness=2.0,
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextStyle(decoration=TextDecoration.underline)\n"
                            "TextStyle(decoration=TextDecoration.overline)\n"
                            "TextStyle(decoration=TextDecoration.lineThrough)\n\n"
                            "# Combine multiple decorations\n"
                            "TextStyle(\n"
                            "    decoration=TextDecoration.underline | TextDecoration.overline,\n"
                            ")\n"
                            "TextStyle(\n"
                            "    decoration=TextDecoration.combine([\n"
                            "        TextDecoration.underline,\n"
                            "        TextDecoration.lineThrough,\n"
                            "    ]),\n"
                            ")\n\n"
                            "# Style the decoration line\n"
                            "TextStyle(\n"
                            "    decoration=TextDecoration.underline,\n"
                            "    decorationStyle=TextDecorationStyle.wavy,\n"
                            "    decorationColor=Colors.red,\n"
                            "    decorationThickness=2.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Text Properties",
                    description="Text supports textDirection for RTL rendering, maxLines with overflow for truncation, and semanticsLabel for accessibility.",
                    instruction="Observe the RTL arabic text rendering right-to-left, the long text truncated with ellipsis, and the semantics label (visible to screen readers).",
                    visible=_TextPropertiesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'RTL text',\n"
                            "    textDirection=TextDirection.rtl,\n"
                            ")\n\n"
                            "Text(\n"
                            "    'Long text...',\n"
                            "    maxLines=1,\n"
                            "    overflow=TextOverflow.ellipsis,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Rich Text (Text.rich)",
                    description="Text.rich renders a paragraph from multiple TextSpan children, each with independent styling for color, weight, and size.",
                    instruction="Observe how multiple styles combine in a single text run: bold colored words, mixed colors, and varying sizes.",
                    visible=_RichTextDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text.rich(\n"
                            "    TextSpan(\n"
                            "        text='Mixed: ',\n"
                            "        style=TextStyle(fontSize=16),\n"
                            "        children=[\n"
                            "            TextSpan(\n"
                            "                text='red',\n"
                            "                style=TextStyle(\n"
                            "                    color=Colors.red,\n"
                            "                    fontWeight=FontWeight.bold,\n"
                            "                ),\n"
                            "            ),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FontStyle",
                    description="FontStyle controls whether text uses normal (upright) or italic glyphs.",
                    instruction="Compare the normal upright text with the italic text below it.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "FontStyle.normal — upright glyphs",
                                style=TextStyle(
                                    fontSize=16, fontStyle=FontStyle.normal
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "FontStyle.italic — cursive glyphs",
                                style=TextStyle(
                                    fontSize=16, fontStyle=FontStyle.italic
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextStyle(fontStyle=FontStyle.normal)\n"
                            "TextStyle(fontStyle=FontStyle.italic)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextWidthBasis",
                    description="TextWidthBasis controls how text width is measured: parent takes full width, longestLine sizes to the longest line.",
                    instruction="Compare the two containers: 'parent' fills the available width, 'longestLine' shrinks to fit the longest line.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Container(
                                color=Colors.blue.withValues(alpha=0.1),
                                child=Text(
                                    "Short line\nThis is a longer line of text",
                                    style=TextStyle(fontSize=14),
                                    textWidthBasis=TextWidthBasis.parent,
                                ),
                            ),
                            SizedBox(height=12),
                            Container(
                                color=Colors.green.withValues(alpha=0.1),
                                child=Text(
                                    "Short line\nThis is a longer line of text",
                                    style=TextStyle(fontSize=14),
                                    textWidthBasis=TextWidthBasis.longestLine,
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Short\\nLong line',\n"
                            "    textWidthBasis=TextWidthBasis.parent,\n"
                            ")\n\n"
                            "Text(\n"
                            "    'Short\\nLong line',\n"
                            "    textWidthBasis=TextWidthBasis.longestLine,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextOverflow Variants",
                    description=(
                        "Controls how overflowing text is clipped: fade gradually blends out, "
                        "clip hard-cuts at the boundary, ellipsis appends '...'."
                    ),
                    instruction="Each box contains text that exceeds its container width.",
                    visible=Row(
                        children=[
                            _overflow_box("fade", TextOverflow.fade),
                            SizedBox(width=8),
                            _overflow_box("clip", TextOverflow.clip),
                            SizedBox(width=8),
                            _overflow_box("ellipsis", TextOverflow.ellipsis),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Long text that overflows...',\n"
                            "    maxLines=1,\n"
                            "    overflow=TextOverflow.ellipsis,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextAlign.justify",
                    description="Justified text spreads words to fill the full width of its container.",
                    instruction="The text stretches across the 300px container with even word spacing.",
                    visible=Container(
                        width=300.0,
                        child=Text(
                            "This text is justified so it spreads evenly "
                            "across the full width of its container for "
                            "demonstration purposes.",
                            textAlign=TextAlign.justify,
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text(\n"
                            "    'Justified text content...',\n"
                            "    textAlign=TextAlign.justify,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
