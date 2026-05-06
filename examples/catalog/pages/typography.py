from flut.flutter.painting import TextOverflow
from utils import CODE_FONT_FAMILY
from flut.dart import Color, TextAlign
from flut.dart.ui import Offset
from flut.flutter.widgets import (
    StatefulWidget,
    State,
    StatelessWidget,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Expanded,
    Padding,
    EmptyTextSelectionControls,
    SelectionContainer,
    SelectionRegistrarScope,
    SelectableRegion,
    StaticSelectionContainerDelegate,
    TextMagnifierConfiguration,
    TextSelectionToolbarAnchors,
    DefaultSelectionStyle,
    Builder,
    ContextMenuButtonItem,
    ContextMenuButtonType,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    Theme,
    SelectableText,
    SelectionArea,
    AdaptiveTextSelectionToolbar,
    TextSelectionTheme,
    TextSelectionThemeData,
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


class _SelectableRegionDemo(StatefulWidget):
    def createState(self):
        return _SelectableRegionDemoState()


class _SelectableRegionDemoState(State[_SelectableRegionDemo]):

    def initState(self):
        self.last_selection = ""

    def _on_selection_changed(self, content):
        def update():
            self.last_selection = content.plainText if content is not None else ""

        self.setState(update)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                SelectableRegion(
                    selectionControls=EmptyTextSelectionControls(),
                    onSelectionChanged=self._on_selection_changed,
                    child=Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=Colors.blue.withValues(alpha=0.08),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Text(
                                    "SelectableRegion wraps any subtree.",
                                    style=TextStyle(fontSize=14),
                                ),
                                SizedBox(height=4),
                                Text(
                                    "Drag across these lines to highlight text. "
                                    "EmptyTextSelectionControls is the placeholder "
                                    "implementation that draws no handles or toolbar.",
                                    style=TextStyle(fontSize=13, color=Colors.grey),
                                ),
                            ],
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    f"onSelectionChanged plainText: {self.last_selection!r}",
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _MagnifierBuilderDemo(StatefulWidget):
    def createState(self):
        return _MagnifierBuilderDemoState()


class _MagnifierBuilderDemoState(State[_MagnifierBuilderDemo]):
    def initState(self):
        self.last_invocation = "(magnifierBuilder has not been invoked yet)"

    def _magnifier_builder(self, context, controller, magnifier_info):
        # Note: SelectableRegion only invokes magnifierBuilder during touch-
        # based selection drags (Android / iOS). On desktop catalog the
        # magnifier path is wired but not visually triggered. Returning None
        # tells the framework "no magnifier"; returning a Widget would draw
        # one anchored to the touch position.
        def update():
            self.last_invocation = (
                "magnifierBuilder invoked " f"(controller.shown={controller.shown})"
            )

        self.setState(update)
        return None

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                SelectableRegion(
                    selectionControls=EmptyTextSelectionControls(),
                    magnifierConfiguration=TextMagnifierConfiguration(
                        magnifierBuilder=self._magnifier_builder,
                        shouldDisplayHandlesInMagnifier=True,
                    ),
                    child=Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=Colors.purple.withValues(alpha=0.08),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text(
                            "Drag across this text on a touch device to "
                            "trigger the magnifierBuilder callback.",
                            style=TextStyle(fontSize=13),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    self.last_invocation,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _SelectionContainerMaybeOfDemo(StatelessWidget):
    @staticmethod
    def _line(label, registrar):
        text = (
            f"SelectionContainer.maybeOf -> {type(registrar).__name__}"
            if registrar is not None
            else "SelectionContainer.maybeOf -> None"
        )
        return Row(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                SizedBox(
                    width=200.0,
                    child=Text(label, style=TextStyle(fontSize=13)),
                ),
                Expanded(
                    child=Text(
                        text,
                        style=TextStyle(
                            fontSize=12,
                            fontFamily=CODE_FONT_FAMILY,
                            color=Colors.grey,
                        ),
                    ),
                ),
            ],
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                SelectableRegion(
                    selectionControls=EmptyTextSelectionControls(),
                    child=Container(
                        padding=EdgeInsets.all(10),
                        decoration=BoxDecoration(
                            color=Colors.blue.withValues(alpha=0.08),
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Builder(
                            builder=lambda inner_ctx: self._line(
                                "Inside SelectableRegion:",
                                SelectionContainer.maybeOf(inner_ctx),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Container(
                    padding=EdgeInsets.all(10),
                    decoration=BoxDecoration(
                        color=Colors.grey.withValues(alpha=0.12),
                        borderRadius=BorderRadius.circular(6),
                    ),
                    child=Builder(
                        builder=lambda outer_ctx: self._line(
                            "Outside any SelectableRegion:",
                            SelectionContainer.maybeOf(outer_ctx),
                        ),
                    ),
                ),
            ],
        )


class _SelectionRegistrarScopeDemo(StatefulWidget):
    def createState(self):
        return _SelectionRegistrarScopeDemoState()


class _SelectionRegistrarScopeDemoState(State[_SelectionRegistrarScopeDemo]):
    def initState(self):
        self._delegate = StaticSelectionContainerDelegate()

    def build(self, context):
        return SelectionRegistrarScope(
            registrar=self._delegate,
            child=Container(
                padding=EdgeInsets.all(10),
                decoration=BoxDecoration(
                    color=Colors.teal.withValues(alpha=0.10),
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Builder(
                    builder=lambda inner_ctx: Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "Subtree under a manually placed "
                                "SelectionRegistrarScope:",
                                style=TextStyle(fontSize=13),
                            ),
                            SizedBox(height=4),
                            Text(
                                "SelectionContainer.maybeOf(context) -> "
                                + (
                                    type(SelectionContainer.maybeOf(inner_ctx)).__name__
                                    if SelectionContainer.maybeOf(inner_ctx) is not None
                                    else "None"
                                ),
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=Colors.grey,
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        )


class _DefaultSelectionStyleDemo(StatelessWidget):
    def build(self, context):
        return DefaultSelectionStyle(
            cursorColor=Colors.deepOrange,
            selectionColor=Colors.deepOrange.withValues(alpha=0.30),
            child=SelectableRegion(
                selectionControls=EmptyTextSelectionControls(),
                child=Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Colors.orange.withValues(alpha=0.06),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "DefaultSelectionStyle.defaultColor = "
                                f"0x{DefaultSelectionStyle.defaultColor.value:08X}",
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=Colors.grey,
                                ),
                            ),
                            SizedBox(height=6),
                            Text(
                                "Drag across this paragraph. The selection is "
                                "drawn in deep-orange instead of the default "
                                "grey because the surrounding "
                                "DefaultSelectionStyle overrides "
                                "selectionColor and cursorColor for the "
                                "entire subtree.",
                                style=TextStyle(fontSize=14),
                            ),
                        ],
                    ),
                ),
            ),
        )


class _TextSelectionThemeDemo(StatelessWidget):
    @staticmethod
    def _format_color(color):
        return "None" if color is None else f"0x{color.value:08X}"

    def build(self, context):
        custom_data = TextSelectionThemeData(
            cursorColor=Colors.purple,
            selectionColor=Colors.purple.withValues(alpha=0.25),
            selectionHandleColor=Colors.purple,
        )
        return TextSelectionTheme(
            data=custom_data,
            child=Builder(
                builder=lambda inner_ctx: Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Container(
                            padding=EdgeInsets.all(10),
                            decoration=BoxDecoration(
                                color=Colors.purple.withValues(alpha=0.05),
                                borderRadius=BorderRadius.circular(6),
                            ),
                            child=SelectableText(
                                "Tap or drag in this SelectableText to see "
                                "the purple cursor and selection color from "
                                "the surrounding TextSelectionTheme.",
                                style=TextStyle(fontSize=14),
                            ),
                        ),
                        SizedBox(height=8),
                        Text(
                            "TextSelectionTheme.of(context) returned "
                            f"cursorColor="
                            f"{self._format_color(TextSelectionTheme.of(inner_ctx).cursorColor)}, "
                            f"selectionColor="
                            f"{self._format_color(TextSelectionTheme.of(inner_ctx).selectionColor)}, "
                            f"selectionHandleColor="
                            f"{self._format_color(TextSelectionTheme.of(inner_ctx).selectionHandleColor)}",
                            style=TextStyle(
                                fontSize=12,
                                fontFamily=CODE_FONT_FAMILY,
                                color=Colors.grey,
                            ),
                        ),
                    ],
                ),
            ),
        )


class _AdaptiveToolbarButtonItemsDemo(StatefulWidget):
    def createState(self):
        return _AdaptiveToolbarButtonItemsDemoState()


class _AdaptiveToolbarButtonItemsDemoState(State[_AdaptiveToolbarButtonItemsDemo]):
    def initState(self):
        self.last_action = "(no toolbar button pressed yet)"

    def _make_handler(self, name):
        def handler():
            def update():
                self.last_action = f"{name} pressed"

            self.setState(update)

        return handler

    def _build_toolbar(self, ctx, state):
        return AdaptiveTextSelectionToolbar.buttonItems(
            anchors=TextSelectionToolbarAnchors(
                primaryAnchor=Offset(220, 220),
            ),
            buttonItems=[
                ContextMenuButtonItem(
                    type=ContextMenuButtonType.copy,
                    onPressed=self._make_handler("Copy"),
                ),
                ContextMenuButtonItem(
                    type=ContextMenuButtonType.selectAll,
                    onPressed=self._make_handler("Select All"),
                ),
                ContextMenuButtonItem(
                    label="Cheer",
                    onPressed=self._make_handler("Cheer"),
                ),
            ],
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                SelectionArea(
                    contextMenuBuilder=self._build_toolbar,
                    child=Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=Colors.indigo.withValues(alpha=0.06),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text(
                            "Drag to select, then right-click. The toolbar is "
                            "built from a Python list of ContextMenuButtonItem "
                            "via AdaptiveTextSelectionToolbar.buttonItems. The "
                            "first two items use ContextMenuButtonType.copy / "
                            "selectAll for platform-correct labels; the third "
                            "supplies its own label.",
                            style=TextStyle(fontSize=13),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    self.last_action,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _AdaptiveToolbarStaticsDemo(StatelessWidget):
    def build(self, context):
        types = [
            ("cut", ContextMenuButtonType.cut),
            ("copy", ContextMenuButtonType.copy),
            ("paste", ContextMenuButtonType.paste),
            ("selectAll", ContextMenuButtonType.selectAll),
            ("delete", ContextMenuButtonType.delete),
            ("lookUp", ContextMenuButtonType.lookUp),
            ("searchWeb", ContextMenuButtonType.searchWeb),
            ("share", ContextMenuButtonType.share),
            ("liveTextInput", ContextMenuButtonType.liveTextInput),
        ]

        def render(inner_ctx):
            label_rows = []
            for name, value in types:
                item = ContextMenuButtonItem(type=value)
                label = AdaptiveTextSelectionToolbar.getButtonLabel(inner_ctx, item)
                label_rows.append(
                    Padding(
                        padding=EdgeInsets.symmetric(vertical=2),
                        child=Row(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                SizedBox(
                                    width=140.0,
                                    child=Text(
                                        f"{name}:",
                                        style=TextStyle(
                                            fontSize=12,
                                            fontFamily=CODE_FONT_FAMILY,
                                            color=Colors.grey,
                                        ),
                                    ),
                                ),
                                Expanded(
                                    child=Text(
                                        repr(label),
                                        style=TextStyle(fontSize=12),
                                    ),
                                ),
                            ],
                        ),
                    )
                )
            label_rows.append(
                Padding(
                    padding=EdgeInsets.symmetric(vertical=2),
                    child=Row(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            SizedBox(
                                width=140.0,
                                child=Text(
                                    "custom (label='Hi'):",
                                    style=TextStyle(
                                        fontSize=12,
                                        fontFamily=CODE_FONT_FAMILY,
                                        color=Colors.grey,
                                    ),
                                ),
                            ),
                            Expanded(
                                child=Text(
                                    repr(
                                        AdaptiveTextSelectionToolbar.getButtonLabel(
                                            inner_ctx,
                                            ContextMenuButtonItem(
                                                type=ContextMenuButtonType.custom,
                                                label="Hi",
                                            ),
                                        )
                                    ),
                                    style=TextStyle(fontSize=12),
                                ),
                            ),
                        ],
                    ),
                )
            )
            return Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=label_rows,
            )

        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Colors.grey.withValues(alpha=0.05),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Builder(builder=render),
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
                SplitViewTile(
                    title="SelectableRegion + EmptyTextSelectionControls",
                    description=(
                        "SelectableRegion makes any subtree text-selectable. "
                        "selectionControls is required and accepts any "
                        "TextSelectionControls subclass; EmptyTextSelectionControls "
                        "is the no-op implementation that omits handles and toolbars. "
                        "onSelectionChanged delivers a SelectedContent (or None when "
                        "the selection clears)."
                    ),
                    instruction=(
                        "Drag across the highlighted block to select text. The line "
                        "below shows the plainText reported by onSelectionChanged."
                    ),
                    visible=_SelectableRegionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SelectableRegion(\n"
                            "    selectionControls=EmptyTextSelectionControls(),\n"
                            "    onSelectionChanged=lambda c: print(\n"
                            "        c.plainText if c else ''\n"
                            "    ),\n"
                            "    child=Text('Selectable text...'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SelectionArea default contextMenuBuilder)",
                    description=(
                        "SelectionArea is the Material wrapper around "
                        "SelectableRegion that, in Flutter, defaults its "
                        "`contextMenuBuilder` to `_defaultContextMenuBuilder`, "
                        "which returns AdaptiveTextSelectionToolbar.selectableRegion. "
                        "In flut the parameter currently maps to a plain "
                        "`Optional[...] = None`, so when Python omits it Dart "
                        "still passes `null` into the Flutter constructor and "
                        "Flutter's own default never kicks in."
                    ),
                    instruction=(
                        "Drag to select some of the text below, then RIGHT-CLICK "
                        "(desktop) on the highlighted block. Expected: the "
                        "adaptive selection toolbar (Copy / etc.) opens."
                    ),
                    visible=Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=Colors.red.withValues(alpha=0.06),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=SelectionArea(
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=[
                                    Text(
                                        "SelectionArea — no contextMenuBuilder "
                                        "supplied",
                                        style=TextStyle(
                                            fontSize=14,
                                            fontWeight=FontWeight.w600,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    Text(
                                        "Select any portion of this paragraph "
                                        "and right-click. In Flutter the "
                                        "AdaptiveTextSelectionToolbar opens "
                                        "automatically; in flut the default "
                                        "is dropped on the floor and Flutter "
                                        "force-unwraps the null builder.",
                                        style=TextStyle(fontSize=13),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "# Mirrors Flutter's `SelectionArea(child: ...)` —\n"
                            "# contextMenuBuilder is intentionally omitted so\n"
                            "# Flutter's default _defaultContextMenuBuilder\n"
                            "# should apply.\n"
                            "SelectionArea(\n"
                            "    child=Text('Right-click after selecting'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SelectionContainer (static & disabled)",
                    description=(
                        "SelectionContainer scopes selection behaviour for its "
                        "subtree. Pass StaticSelectionContainerDelegate when the "
                        "Selectables inside the subtree do not change at runtime — "
                        "it provides the standard multi-child selection semantics "
                        "without the bookkeeping for dynamic registration. "
                        "SelectionContainer.disabled opts a subtree out of any "
                        "enclosing SelectableRegion."
                    ),
                    instruction=(
                        "Both blocks live inside the same SelectableRegion above. "
                        "The first block is wrapped in a SelectionContainer with a "
                        "StaticSelectionContainerDelegate; selection works normally. "
                        "The second block uses SelectionContainer.disabled and "
                        "cannot be selected."
                    ),
                    visible=SelectableRegion(
                        selectionControls=EmptyTextSelectionControls(),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                SelectionContainer(
                                    delegate=StaticSelectionContainerDelegate(),
                                    child=Container(
                                        padding=EdgeInsets.all(8),
                                        decoration=BoxDecoration(
                                            color=Colors.green.withValues(alpha=0.1),
                                            borderRadius=BorderRadius.circular(6),
                                        ),
                                        child=Text(
                                            "Selectable: wrapped in "
                                            "SelectionContainer(delegate=Static…)",
                                            style=TextStyle(fontSize=13),
                                        ),
                                    ),
                                ),
                                SizedBox(height=8),
                                SelectionContainer.disabled(
                                    child=Container(
                                        padding=EdgeInsets.all(8),
                                        decoration=BoxDecoration(
                                            color=Colors.grey.withValues(alpha=0.15),
                                            borderRadius=BorderRadius.circular(6),
                                        ),
                                        child=Text(
                                            "Not selectable: "
                                            "SelectionContainer.disabled",
                                            style=TextStyle(fontSize=13),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SelectableRegion(\n"
                            "    selectionControls=EmptyTextSelectionControls(),\n"
                            "    child=Column(children=[\n"
                            "        SelectionContainer(\n"
                            "            delegate=StaticSelectionContainerDelegate(),\n"
                            "            child=Text('Selectable...'),\n"
                            "        ),\n"
                            "        SelectionContainer.disabled(\n"
                            "            child=Text('Not selectable'),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextMagnifierConfiguration + magnifierBuilder",
                    description=(
                        "Pass a Python `magnifierBuilder` callback through "
                        "TextMagnifierConfiguration. The callback receives "
                        "(BuildContext, MagnifierController, "
                        "ValueNotifier<MagnifierInfo>) and returns the magnifier "
                        "Widget to display, or None to suppress it. Returning "
                        "None still wires the controller through but avoids "
                        "drawing anything."
                    ),
                    instruction=(
                        "On Android / iOS, drag across this purple block to "
                        "trigger the magnifier path; magnifierBuilder is called "
                        "with a live MagnifierController. On desktop the "
                        "callback is reachable from the framework but not "
                        "visually triggered (Flutter only invokes it for "
                        "touch-based selection drags)."
                    ),
                    visible=_MagnifierBuilderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "def my_magnifier(context, controller, info):\n"
                            "    # info is ValueNotifier<MagnifierInfo>; read\n"
                            "    # info.value.globalGesturePosition / caretRect\n"
                            "    return None  # or return a custom Widget\n\n"
                            "SelectableRegion(\n"
                            "    selectionControls=EmptyTextSelectionControls(),\n"
                            "    magnifierConfiguration=TextMagnifierConfiguration(\n"
                            "        magnifierBuilder=my_magnifier,\n"
                            "        shouldDisplayHandlesInMagnifier=True,\n"
                            "    ),\n"
                            "    child=Text('Selectable text'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SelectionContainer.maybeOf",
                    description=(
                        "SelectionContainer.maybeOf(context) returns the nearest "
                        "ancestor SelectionRegistrar via "
                        "dependOnInheritedWidgetOfExactType<SelectionRegistrarScope>. "
                        "Returns None when no SelectableRegion / SelectionContainer "
                        "is above the context."
                    ),
                    instruction=(
                        "Both rows render the result of maybeOf(context). The first "
                        "context is inside a SelectableRegion (which installs a "
                        "registrar) and reports a non-null type; the second context "
                        "is outside any selection scope and reports None."
                    ),
                    visible=_SelectionContainerMaybeOfDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SelectableRegion(\n"
                            "    selectionControls=EmptyTextSelectionControls(),\n"
                            "    child=Builder(\n"
                            "        builder=lambda ctx: Text(\n"
                            "            'maybeOf -> ' + (\n"
                            "                type(SelectionContainer.maybeOf(ctx)).__name__\n"
                            "                if SelectionContainer.maybeOf(ctx) is not None\n"
                            "                else 'None'\n"
                            "            ),\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SelectionRegistrarScope (manual)",
                    description=(
                        "SelectionRegistrarScope is the InheritedWidget that "
                        "SelectionContainer normally inserts automatically. Placing "
                        "one manually lets a subtree expose a registrar without a "
                        "full SelectableRegion / SelectionContainer pair, so "
                        "SelectionContainer.maybeOf finds it via "
                        "dependOnInheritedWidgetOfExactType."
                    ),
                    instruction=(
                        "The block below is wrapped only in SelectionRegistrarScope "
                        "(no enclosing SelectableRegion). The line still reports "
                        "that maybeOf located the registrar, proving the inherited "
                        "lookup wires through correctly."
                    ),
                    visible=_SelectionRegistrarScopeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SelectionRegistrarScope(\n"
                            "    registrar=StaticSelectionContainerDelegate(),\n"
                            "    child=Builder(\n"
                            "        builder=lambda ctx: Text(\n"
                            "            'maybeOf saw ' + type(\n"
                            "                SelectionContainer.maybeOf(ctx)\n"
                            "            ).__name__,\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DefaultSelectionStyle (cursor + selection colors)",
                    description=(
                        "DefaultSelectionStyle is an InheritedTheme that lets a "
                        "subtree override the cursor color, selection color and "
                        "mouse cursor used by descendant EditableText widgets when "
                        "no explicit value is given. The class also exposes the "
                        "constant defaultColor (0x80808080) used as the framework "
                        "fallback."
                    ),
                    instruction=(
                        "Drag across the orange paragraph; the selection rectangle "
                        "is drawn in deep-orange instead of the default semi-"
                        "transparent grey because the surrounding "
                        "DefaultSelectionStyle overrides selectionColor / "
                        "cursorColor for the entire subtree."
                    ),
                    visible=_DefaultSelectionStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DefaultSelectionStyle(\n"
                            "    cursorColor=Colors.deepOrange,\n"
                            "    selectionColor=Colors.deepOrange.withValues(\n"
                            "        alpha=0.30,\n"
                            "    ),\n"
                            "    child=SelectableRegion(\n"
                            "        selectionControls=EmptyTextSelectionControls(),\n"
                            "        child=Text('Selectable paragraph...'),\n"
                            "    ),\n"
                            ")\n\n"
                            "# Static constant exposed by the class:\n"
                            "DefaultSelectionStyle.defaultColor"
                            "  # Color(0x80808080)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextSelectionTheme + TextSelectionThemeData",
                    description=(
                        "TextSelectionTheme propagates a TextSelectionThemeData "
                        "(cursorColor, selectionColor, selectionHandleColor) to "
                        "descendant TextField / SelectableText widgets. "
                        "TextSelectionTheme.of(context) returns the nearest "
                        "TextSelectionThemeData, falling back to "
                        "Theme.of(context).textSelectionTheme so the lookup is "
                        "always non-null."
                    ),
                    instruction=(
                        "Tap or drag inside the SelectableText to see purple "
                        "cursor / selection. The line below echoes the "
                        "cursorColor / selectionColor / selectionHandleColor as "
                        "read back via TextSelectionTheme.of(context)."
                    ),
                    visible=_TextSelectionThemeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextSelectionTheme(\n"
                            "    data=TextSelectionThemeData(\n"
                            "        cursorColor=Colors.purple,\n"
                            "        selectionColor=Colors.purple.withValues(\n"
                            "            alpha=0.25,\n"
                            "        ),\n"
                            "        selectionHandleColor=Colors.purple,\n"
                            "    ),\n"
                            "    child=SelectableText('Tap or drag...'),\n"
                            ")\n\n"
                            "# Read back from inside the subtree:\n"
                            "data = TextSelectionTheme.of(context)\n"
                            "data.cursorColor  # Color(...)\n"
                            "data.selectionColor  # Color(...)\n"
                            "data.selectionHandleColor  # Color(...)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AdaptiveTextSelectionToolbar.buttonItems + ContextMenuButtonItem",
                    description=(
                        "AdaptiveTextSelectionToolbar.buttonItems builds a "
                        "platform-adaptive selection toolbar from a Python list "
                        "of ContextMenuButtonItem. Each item carries a "
                        "ContextMenuButtonType (used to look up the localized "
                        "label) and an optional VoidCallback that fires when "
                        "the item is tapped."
                    ),
                    instruction=(
                        "Drag to select inside the indigo block, then "
                        "right-click to open the toolbar. Tapping any item "
                        "updates the line below with the action name."
                    ),
                    visible=_AdaptiveToolbarButtonItemsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SelectionArea(\n"
                            "    contextMenuBuilder=lambda ctx, state: (\n"
                            "        AdaptiveTextSelectionToolbar.buttonItems(\n"
                            "            anchors=TextSelectionToolbarAnchors(\n"
                            "                primaryAnchor=Offset(220, 220),\n"
                            "            ),\n"
                            "            buttonItems=[\n"
                            "                ContextMenuButtonItem(\n"
                            "                    type=ContextMenuButtonType.copy,\n"
                            "                    onPressed=lambda: ...,\n"
                            "                ),\n"
                            "                ContextMenuButtonItem(\n"
                            "                    label='Cheer',\n"
                            "                    onPressed=lambda: ...,\n"
                            "                ),\n"
                            "            ],\n"
                            "        )\n"
                            "    ),\n"
                            "    child=Text('Selectable content'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AdaptiveTextSelectionToolbar.getButtonLabel",
                    description=(
                        "AdaptiveTextSelectionToolbar.getButtonLabel(context, "
                        "item) returns the platform-localized label for a "
                        "ContextMenuButtonItem. When the item supplies its own "
                        "label, that string is returned directly; otherwise "
                        "the result is resolved through "
                        "MaterialLocalizations / CupertinoLocalizations based "
                        "on Theme.of(context).platform."
                    ),
                    instruction=(
                        "Each row shows a ContextMenuButtonType and the label "
                        "returned for it on the current platform. The last "
                        "row uses ContextMenuButtonType.custom with an "
                        "explicit label, which short-circuits the platform "
                        "lookup."
                    ),
                    visible=_AdaptiveToolbarStaticsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "label = AdaptiveTextSelectionToolbar.getButtonLabel(\n"
                            "    context,\n"
                            "    ContextMenuButtonItem(\n"
                            "        type=ContextMenuButtonType.copy,\n"
                            "    ),\n"
                            ")\n\n"
                            "# When the item provides a label, it is returned\n"
                            "# verbatim (the platform lookup is skipped):\n"
                            "AdaptiveTextSelectionToolbar.getButtonLabel(\n"
                            "    context,\n"
                            "    ContextMenuButtonItem(\n"
                            "        type=ContextMenuButtonType.custom,\n"
                            "        label='Hi',\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
