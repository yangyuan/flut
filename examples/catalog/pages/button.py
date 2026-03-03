from flut.dart import Color, Size
from flut.dart.ui import Clip
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Icon,
    Container,
    WidgetStatePropertyAll,
    Wrap,
)
from flut.flutter.rendering import CrossAxisAlignment, BoxConstraints
from flut.flutter.material import (
    ButtonStyle,
    Colors,
    ElevatedButton,
    FloatingActionButton,
    Icons,
    IconButton,
    TextButton,
    OutlinedButton,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Alignment,
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    BorderSide,
)
from flut.flutter.services import SystemMouseCursors
from widgets import CatalogPage, SplitViewTile, CodeArea


class _ElevatedButtonDemo(StatefulWidget):
    def createState(self):
        return _ElevatedButtonDemoState()


class _ElevatedButtonDemoState(State[_ElevatedButtonDemo]):
    def initState(self):
        self.count = 0

    def build(self, context):
        return Row(
            children=[
                ElevatedButton(
                    child=Text("Increment"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "count", self.count + 1)
                    ),
                ),
                SizedBox(width=12),
                ElevatedButton(
                    child=Text("Reset"),
                    onPressed=lambda: self.setState(lambda: setattr(self, "count", 0)),
                ),
                SizedBox(width=16),
                Text(f"Count: {self.count}", style=TextStyle(fontSize=16)),
            ],
        )


class _IconButtonDemo(StatefulWidget):
    def createState(self):
        return _IconButtonDemoState()


class _IconButtonDemoState(State[_IconButtonDemo]):
    def initState(self):
        self.count = 0

    def build(self, context):
        return Row(
            children=[
                IconButton(
                    icon=Icon(Icons.add),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "count", self.count + 1)
                    ),
                ),
                IconButton(
                    icon=Icon(Icons.remove),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "count", self.count - 1)
                    ),
                ),
                SizedBox(width=8),
                Text(f"{self.count}", style=TextStyle(fontSize=18)),
            ],
        )


class _IconButtonSelectedDemo(StatefulWidget):
    def createState(self):
        return _IconButtonSelectedState()


class _IconButtonSelectedState(State[_IconButtonSelectedDemo]):
    def initState(self):
        self.selected = False

    def build(self, context):
        return Row(
            children=[
                IconButton(
                    icon=Icon(Icons.star_border),
                    isSelected=self.selected,
                    selectedIcon=Icon(Icons.star, color=Colors.amber),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "selected", not self.selected)
                    ),
                    tooltip="Toggle star",
                ),
                SizedBox(width=8),
                Text(
                    f"Selected: {self.selected}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _ButtonVariantsDemo(StatefulWidget):
    def createState(self):
        return _ButtonVariantsDemoState()


class _ButtonVariantsDemoState(State[_ButtonVariantsDemo]):
    def initState(self):
        self.button_log = ""

    def build(self, context):
        return Row(
            children=[
                TextButton(
                    child=Text("TextButton"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "button_log", "TextButton pressed")
                    ),
                ),
                SizedBox(width=12),
                OutlinedButton(
                    child=Text("OutlinedButton"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "button_log", "OutlinedButton pressed")
                    ),
                ),
                SizedBox(width=12),
                FloatingActionButton(
                    tooltip="Add",
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "button_log", "FAB pressed")
                    ),
                    child=Icon(Icons.add),
                ),
                SizedBox(width=16),
                Text(
                    self.button_log,
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _FloatingActionButtonVariantsDemo(StatefulWidget):
    def createState(self):
        return _FloatingActionButtonVariantsDemoState()


class _FloatingActionButtonVariantsDemoState(State[_FloatingActionButtonVariantsDemo]):
    def initState(self):
        self.section = "colors"
        self.color_index = 0
        self.elevation_index = 1
        self.size_index = 1

    def _select_section(self, section):
        self.setState(lambda: setattr(self, "section", section))

    def _build_section_selector(self):
        options = [
            ("colors", "Colors"),
            ("elevation", "Elevation"),
            ("size", "Size"),
        ]
        return Wrap(
            spacing=8,
            runSpacing=8,
            children=[
                (
                    ElevatedButton(
                        onPressed=lambda value=value: self._select_section(value),
                        child=Text(label),
                    )
                    if self.section == value
                    else OutlinedButton(
                        onPressed=lambda value=value: self._select_section(value),
                        child=Text(label),
                    )
                )
                for value, label in options
            ],
        )

    def _build_colors_demo(self):
        presets = [
            ("Teal", Icons.add, Colors.white, Color(0xFF009688)),
            ("Purple", Icons.edit, Color(0xFFFFEB3B), Color(0xFF673AB7)),
            ("Red", Icons.delete, Colors.white, Color(0xFFF44336)),
        ]
        label, icon, foreground, background = presets[self.color_index]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        (
                            ElevatedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "color_index", idx)
                                ),
                                child=Text(name),
                            )
                            if i == self.color_index
                            else OutlinedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "color_index", idx)
                                ),
                                child=Text(name),
                            )
                        )
                        for i, (name, _, _, _) in enumerate(presets)
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        FloatingActionButton(
                            child=Icon(icon),
                            foregroundColor=foreground,
                            backgroundColor=background,
                            onPressed=lambda: None,
                            tooltip=f"{label} FAB",
                        ),
                        SizedBox(width=16),
                        Text(
                            f"{label}: foregroundColor + backgroundColor",
                            style=TextStyle(fontSize=13, color=Colors.grey),
                        ),
                    ],
                ),
            ],
        )

    def _build_elevation_demo(self):
        presets = [
            ("Flat", 0.0, Icons.layers_clear),
            ("Default", 6.0, Icons.layers),
            ("High", 12.0, Icons.layers),
        ]
        label, elevation, icon = presets[self.elevation_index]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        (
                            ElevatedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "elevation_index", idx)
                                ),
                                child=Text(name),
                            )
                            if i == self.elevation_index
                            else OutlinedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "elevation_index", idx)
                                ),
                                child=Text(name),
                            )
                        )
                        for i, (name, _, _) in enumerate(presets)
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        FloatingActionButton(
                            child=Icon(icon),
                            elevation=elevation,
                            onPressed=lambda: None,
                            tooltip=f"{label} elevation",
                        ),
                        SizedBox(width=16),
                        Text(
                            f"{label}: elevation={elevation:.1f}",
                            style=TextStyle(fontSize=13, color=Colors.grey),
                        ),
                    ],
                ),
            ],
        )

    def _build_size_demo(self):
        options = ["mini", "regular", "extended"]
        labels = {
            "mini": "mini=True shrinks the FAB for secondary actions.",
            "regular": "The default FAB size fits a primary icon action.",
            "extended": "isExtended=True adds room for icon + label content.",
        }
        selected = options[self.size_index]
        if selected == "mini":
            preview = FloatingActionButton(
                child=Icon(Icons.remove),
                mini=True,
                onPressed=lambda: None,
                tooltip="mini FAB",
            )
        elif selected == "extended":
            preview = FloatingActionButton(
                child=Row(
                    mainAxisAlignment=MainAxisAlignment.center,
                    children=[
                        Icon(Icons.navigation),
                        SizedBox(width=8),
                        Text("Navigate"),
                    ],
                ),
                isExtended=True,
                onPressed=lambda: None,
                tooltip="extended FAB",
            )
        else:
            preview = FloatingActionButton(
                child=Icon(Icons.add),
                onPressed=lambda: None,
                tooltip="regular FAB",
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        (
                            ElevatedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "size_index", idx)
                                ),
                                child=Text(name.capitalize()),
                            )
                            if i == self.size_index
                            else OutlinedButton(
                                onPressed=lambda idx=i: self.setState(
                                    lambda: setattr(self, "size_index", idx)
                                ),
                                child=Text(name.capitalize()),
                            )
                        )
                        for i, name in enumerate(options)
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        preview,
                        SizedBox(width=16),
                        Expanded(
                            child=Text(
                                labels[selected],
                                style=TextStyle(fontSize=13, color=Colors.grey),
                            ),
                        ),
                    ],
                ),
            ],
        )

    def build(self, context):
        if self.section == "colors":
            preview = self._build_colors_demo()
        elif self.section == "elevation":
            preview = self._build_elevation_demo()
        else:
            preview = self._build_size_demo()

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                self._build_section_selector(),
                SizedBox(height=12),
                preview,
            ],
        )


class _IconButtonVariantsDemo(StatefulWidget):
    def createState(self):
        return _IconButtonVariantsDemoState()


class _IconButtonVariantsDemoState(State[_IconButtonVariantsDemo]):
    def initState(self):
        self.variant = "basic"
        self.count = 0

    def _select_variant(self, variant):
        self.variant = variant
        self.setState(lambda: None)

    def _build_selectors(self):
        options = [
            ("basic", "Basic"),
            ("padding", "Padding"),
            ("overlay", "Overlay"),
            ("disabled", "Disabled"),
            ("constraints", "Constraints"),
        ]
        return Wrap(
            spacing=8,
            runSpacing=8,
            children=[
                (
                    ElevatedButton(
                        onPressed=lambda key=key: self._select_variant(key),
                        child=Text(label),
                    )
                    if self.variant == key
                    else OutlinedButton(
                        onPressed=lambda key=key: self._select_variant(key),
                        child=Text(label),
                    )
                )
                for key, label in options
            ],
        )

    def _build_preview(self):
        if self.variant == "basic":
            return Row(
                children=[
                    IconButton(
                        icon=Icon(Icons.add),
                        onPressed=lambda: self.setState(
                            lambda: setattr(self, "count", self.count + 1)
                        ),
                    ),
                    IconButton(
                        icon=Icon(Icons.remove),
                        onPressed=lambda: self.setState(
                            lambda: setattr(self, "count", self.count - 1)
                        ),
                    ),
                    SizedBox(width=8),
                    Text(f"{self.count}", style=TextStyle(fontSize=18)),
                ],
            )
        if self.variant == "padding":
            return Row(
                children=[
                    Column(
                        children=[
                            Container(
                                decoration=BoxDecoration(
                                    borderRadius=BorderRadius.circular(4),
                                    color=Color(0x220000FF),
                                ),
                                child=IconButton(
                                    icon=Icon(Icons.home),
                                    padding=EdgeInsets.all(0),
                                    onPressed=lambda: None,
                                ),
                            ),
                            SizedBox(height=4),
                            Text("pad=0", style=TextStyle(fontSize=11)),
                        ],
                    ),
                    SizedBox(width=16),
                    Column(
                        children=[
                            Container(
                                decoration=BoxDecoration(
                                    borderRadius=BorderRadius.circular(4),
                                    color=Color(0x220000FF),
                                ),
                                child=IconButton(
                                    icon=Icon(Icons.home),
                                    padding=EdgeInsets.all(8),
                                    onPressed=lambda: None,
                                ),
                            ),
                            SizedBox(height=4),
                            Text("pad=8", style=TextStyle(fontSize=11)),
                        ],
                    ),
                    SizedBox(width=16),
                    Column(
                        children=[
                            Container(
                                decoration=BoxDecoration(
                                    borderRadius=BorderRadius.circular(4),
                                    color=Color(0x220000FF),
                                ),
                                child=IconButton(
                                    icon=Icon(Icons.home),
                                    padding=EdgeInsets.all(24),
                                    onPressed=lambda: None,
                                ),
                            ),
                            SizedBox(height=4),
                            Text("pad=24", style=TextStyle(fontSize=11)),
                        ],
                    ),
                ],
            )
        if self.variant == "overlay":
            return Row(
                children=[
                    Column(
                        children=[
                            IconButton(
                                icon=Icon(Icons.palette),
                                focusColor=Color(0x4400FF00),
                                onPressed=lambda: None,
                            ),
                            Text("focusColor", style=TextStyle(fontSize=11)),
                        ],
                    ),
                    SizedBox(width=24),
                    Column(
                        children=[
                            IconButton(
                                icon=Icon(Icons.palette),
                                hoverColor=Color(0x44FF9800),
                                highlightColor=Color(0x44FF5722),
                                splashColor=Color(0x66FF9800),
                                onPressed=lambda: None,
                            ),
                            Text("hoverColor", style=TextStyle(fontSize=11)),
                        ],
                    ),
                ],
            )
        if self.variant == "disabled":
            return Row(
                children=[
                    Column(
                        children=[
                            IconButton(
                                icon=Icon(Icons.block),
                                disabledColor=Colors.red,
                                onPressed=None,
                            ),
                            Text(
                                "disabled",
                                style=TextStyle(fontSize=11, color=Colors.red),
                            ),
                        ],
                    ),
                    SizedBox(width=24),
                    Column(
                        children=[
                            IconButton(
                                icon=Icon(Icons.water_drop),
                                splashRadius=30.0,
                                onPressed=lambda: None,
                            ),
                            Text("splashRadius=30", style=TextStyle(fontSize=11)),
                        ],
                    ),
                ],
            )
        return Row(
            children=[
                Container(
                    decoration=BoxDecoration(
                        borderRadius=BorderRadius.circular(8),
                        color=Color(0x11000000),
                    ),
                    child=IconButton(
                        icon=Icon(Icons.fullscreen, color=Colors.white),
                        constraints=BoxConstraints(minWidth=60.0, minHeight=60.0),
                        style=ButtonStyle(
                            backgroundColor=WidgetStatePropertyAll(Color(0xFF009688)),
                        ),
                        onPressed=lambda: None,
                    ),
                ),
                SizedBox(width=16),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text("minWidth=60", style=TextStyle(fontSize=12)),
                        Text("minHeight=60", style=TextStyle(fontSize=12)),
                        Text("backgroundColor=teal", style=TextStyle(fontSize=12)),
                    ],
                ),
            ],
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                self._build_selectors(),
                SizedBox(height=12),
                self._build_preview(),
            ],
        )


class ButtonPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Buttons",
            description=(
                "Compares the main button patterns, how they signal emphasis, and "
                "how theming and state-aware styling change interaction feedback."
            ),
            children=[
                SplitViewTile(
                    title="ElevatedButton",
                    description="A filled button with elevation that lifts on press. The primary call-to-action button style.",
                    instruction="Click Increment to increase the counter and Reset to set it back to zero.",
                    visible=_ElevatedButtonDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ElevatedButton(\n"
                            "    child=Text('Increment'),\n"
                            "    onPressed=on_pressed,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconButton variants",
                    description=(
                        "Shows the main IconButton property groups in one place: basic taps, "
                        "padding, overlay colors, disabled or splash behavior, and larger constrained styling."
                    ),
                    instruction="Choose a preset, then interact with the preview to compare how each property set changes the button.",
                    visible=_IconButtonVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "preset = 'constraints'\n\n"
                            "IconButton(\n"
                            "    icon=Icon(Icons.fullscreen),\n"
                            "    padding=EdgeInsets.all(24) if preset == 'padding' else None,\n"
                            "    focusColor=Color(0x4400FF00) if preset == 'overlay' else None,\n"
                            "    hoverColor=Color(0x44FF9800) if preset == 'overlay' else None,\n"
                            "    disabledColor=Colors.red if preset == 'disabled' else None,\n"
                            "    splashRadius=30.0 if preset == 'disabled' else None,\n"
                            "    constraints=BoxConstraints(minWidth=60, minHeight=60)\n"
                            "        if preset == 'constraints' else None,\n"
                            "    style=ButtonStyle(\n"
                            "        backgroundColor=WidgetStatePropertyAll(Color(0xFF009688))\n"
                            "    ) if preset == 'constraints' else None,\n"
                            "    onPressed=None if preset == 'disabled' else on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextButton & OutlinedButton",
                    description=(
                        "TextButton is a flat button for low-emphasis actions. "
                        "OutlinedButton adds a border for medium-emphasis actions."
                    ),
                    instruction="Click either button to see its press effect.",
                    visible=Row(
                        children=[
                            TextButton(
                                child=Text("TextButton"),
                                onPressed=lambda: None,
                            ),
                            SizedBox(width=12),
                            OutlinedButton(
                                child=Text("OutlinedButton"),
                                onPressed=lambda: None,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextButton(child=Text('TextButton'), onPressed=on_tap)\n"
                            "OutlinedButton(child=Text('OutlinedButton'), onPressed=on_tap)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ButtonStyle",
                    description=(
                        "Customize padding, colors, sizes, and borders via ButtonStyle. "
                        "Uses WidgetStatePropertyWith to resolve values for different widget states."
                    ),
                    instruction="Compare the different button style customizations: compact sizing, custom colors, extra padding, red border, and zero-padding text.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Row(
                                children=[
                                    ElevatedButton(
                                        child=Text("Compact"),
                                        onPressed=lambda: None,
                                        style=ButtonStyle(
                                            padding=WidgetStatePropertyAll(
                                                EdgeInsets.symmetric(
                                                    horizontal=8, vertical=4
                                                )
                                            ),
                                            minimumSize=WidgetStatePropertyAll(
                                                Size(0, 0)
                                            ),
                                        ),
                                    ),
                                    SizedBox(width=12),
                                    ElevatedButton(
                                        child=Text("Custom Colors"),
                                        onPressed=lambda: None,
                                        style=ButtonStyle(
                                            backgroundColor=WidgetStatePropertyAll(
                                                Color(0xFF5C6BC0)
                                            ),
                                            foregroundColor=WidgetStatePropertyAll(
                                                Colors.white
                                            ),
                                        ),
                                    ),
                                    SizedBox(width=12),
                                    ElevatedButton(
                                        child=Text("Large Padding"),
                                        onPressed=lambda: None,
                                        style=ButtonStyle(
                                            padding=WidgetStatePropertyAll(
                                                EdgeInsets.symmetric(
                                                    horizontal=32, vertical=16
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(height=12),
                            Row(
                                children=[
                                    OutlinedButton(
                                        child=Text("Red Border"),
                                        onPressed=lambda: None,
                                        style=ButtonStyle(
                                            side=WidgetStatePropertyAll(
                                                BorderSide(color=Colors.red, width=2)
                                            ),
                                            foregroundColor=WidgetStatePropertyAll(
                                                Colors.red
                                            ),
                                        ),
                                    ),
                                    SizedBox(width=12),
                                    TextButton(
                                        child=Text("No Padding"),
                                        onPressed=lambda: None,
                                        style=ButtonStyle(
                                            padding=WidgetStatePropertyAll(
                                                EdgeInsets.all(0)
                                            ),
                                            minimumSize=WidgetStatePropertyAll(
                                                Size(0, 0)
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ElevatedButton(\n"
                            "    child=Text('Compact'),\n"
                            "    onPressed=on_tap,\n"
                            "    style=ButtonStyle(\n"
                            "        padding=WidgetStatePropertyWith(\n"
                            "            lambda s: EdgeInsets.symmetric(\n"
                            "                horizontal=8, vertical=4\n"
                            "            )\n"
                            "        ),\n"
                            "        minimumSize=WidgetStatePropertyWith(\n"
                            "            lambda s: Size(0, 0)\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ElevatedButton.icon",
                    description="ElevatedButton.icon() creates a button with a leading icon and a label. iconAlignment controls icon position.",
                    instruction="See buttons with leading icons and text labels.",
                    visible=Row(
                        children=[
                            ElevatedButton.icon(
                                icon=Icon(Icons.send),
                                label=Text("Send"),
                                onPressed=lambda: None,
                            ),
                            SizedBox(width=12),
                            ElevatedButton.icon(
                                icon=Icon(Icons.download),
                                label=Text("Download"),
                                onPressed=lambda: None,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ElevatedButton.icon(\n"
                            "    icon=Icon(Icons.send),\n"
                            "    label=Text('Send'),\n"
                            "    onPressed=on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ButtonStyle mouseCursor",
                    description="ButtonStyle.mouseCursor overrides the cursor shown when hovering over a button.",
                    instruction="Hover over each button and observe the cursor change: forbidden cursor on the left, cell/crosshair on the right.",
                    visible=Row(
                        children=[
                            ElevatedButton(
                                child=Text("Forbidden"),
                                onPressed=lambda: None,
                                style=ButtonStyle(
                                    mouseCursor=WidgetStatePropertyAll(
                                        SystemMouseCursors.forbidden
                                    ),
                                ),
                            ),
                            SizedBox(width=12),
                            ElevatedButton(
                                child=Text("Cell"),
                                onPressed=lambda: None,
                                style=ButtonStyle(
                                    mouseCursor=WidgetStatePropertyAll(
                                        SystemMouseCursors.cell
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ElevatedButton(\n"
                            "    child=Text('Forbidden'),\n"
                            "    onPressed=on_tap,\n"
                            "    style=ButtonStyle(\n"
                            "        mouseCursor=WidgetStatePropertyAll(\n"
                            "            SystemMouseCursors.forbidden\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconButton isSelected & selectedIcon",
                    description="Toggle between icon and selectedIcon using the isSelected property. Great for favorite/bookmark patterns.",
                    instruction="Tap the star icon to toggle between outlined and filled states.",
                    visible=_IconButtonSelectedDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "IconButton(\n"
                            "    icon=Icon(Icons.star_border),\n"
                            "    isSelected=self.selected,\n"
                            "    selectedIcon=Icon(\n"
                            "        Icons.star, color=Colors.amber\n"
                            "    ),\n"
                            "    onPressed=toggle,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextButton focusNode & clipBehavior",
                    description="Assign a FocusNode for programmatic focus control. clipBehavior controls how content is clipped at the button boundary.",
                    instruction="The button uses Clip.antiAlias. Notice the smooth clipped edges on the styled button.",
                    visible=Row(
                        children=[
                            TextButton(
                                child=Container(
                                    padding=EdgeInsets.symmetric(
                                        horizontal=24, vertical=12
                                    ),
                                    decoration=BoxDecoration(
                                        color=Color(0xFF673AB7),
                                        borderRadius=BorderRadius.circular(20),
                                    ),
                                    child=Text(
                                        "Clipped AntiAlias",
                                        style=TextStyle(color=Colors.white),
                                    ),
                                ),
                                clipBehavior=Clip.antiAlias,
                                onPressed=lambda: None,
                                style=ButtonStyle(
                                    padding=WidgetStatePropertyAll(EdgeInsets.all(0)),
                                ),
                            ),
                            SizedBox(width=16),
                            TextButton(
                                child=Text("Default clip"),
                                onPressed=lambda: None,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextButton(\n"
                            "    child=Text('Clipped'),\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            "    onPressed=on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="OutlinedButton focusNode & clipBehavior",
                    description="OutlinedButton with clipBehavior=Clip.hardEdge clips overflow content with hard pixel edges, compared to the default.",
                    instruction="Compare the hard-clipped button on the left with the default on the right.",
                    visible=Row(
                        children=[
                            OutlinedButton(
                                child=Container(
                                    padding=EdgeInsets.symmetric(
                                        horizontal=24, vertical=12
                                    ),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFFF5722),
                                        borderRadius=BorderRadius.circular(20),
                                    ),
                                    child=Text(
                                        "Hard Edge Clip",
                                        style=TextStyle(color=Colors.white),
                                    ),
                                ),
                                clipBehavior=Clip.hardEdge,
                                onPressed=lambda: None,
                                style=ButtonStyle(
                                    padding=WidgetStatePropertyAll(EdgeInsets.all(0)),
                                ),
                            ),
                            SizedBox(width=16),
                            OutlinedButton(
                                child=Text("Default clip"),
                                onPressed=lambda: None,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "OutlinedButton(\n"
                            "    child=Text('Hard Edge'),\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    onPressed=on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FloatingActionButton variants",
                    description=(
                        "One interactive demo for the most common FloatingActionButton "
                        "customizations: colors, elevation, and size or extended layout."
                    ),
                    instruction=(
                        "Switch between Colors, Elevation, and Size, then use the chips "
                        "below to compare each FAB variant in one place."
                    ),
                    visible=_FloatingActionButtonVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "section = 'colors'\n\n"
                            "FloatingActionButton(\n"
                            "    child=Icon(Icons.add),\n"
                            "    foregroundColor=Colors.white,\n"
                            "    backgroundColor=Color(0xFF009688),\n"
                            "    elevation=6.0,\n"
                            "    mini=False,\n"
                            "    isExtended=False,\n"
                            "    onPressed=on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Button Variants",
                    description=(
                        "Flutter provides multiple button styles: TextButton for low-emphasis actions, "
                        "OutlinedButton for medium-emphasis, and FloatingActionButton for primary actions."
                    ),
                    instruction="Click each button variant to see which one was pressed.",
                    visible=_ButtonVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextButton(child=Text('Text'), onPressed=on_tap)\n"
                            "OutlinedButton(child=Text('Outlined'), onPressed=on_tap)\n"
                            "FloatingActionButton(child=Icon(Icons.add), onPressed=on_tap)"
                        ),
                    ),
                ),
            ],
        )
