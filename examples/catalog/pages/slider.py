from utils import CODE_FONT_FAMILY
from flut.dart import Color
from flut.dart.ui import FontWeight, StrokeCap
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    Wrap,
    SizedBox,
    Container,
    Center,
    Expanded,
    Icon,
    FocusNode,
    GestureDetector,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    BoxConstraints,
)
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Icons,
    LinearProgressIndicator,
    CircularProgressIndicator,
    Slider,
    SliderInteraction,
    ShowValueIndicator,
)
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
)

from widgets import CatalogPage, SplitViewTile, CodeArea


class _SliderDemo(StatefulWidget):
    def createState(self):
        return _SliderDemoState()


class _SliderDemoState(State[_SliderDemo]):
    def initState(self):
        self.slider_value = 0.5

    def _on_changed(self, value):
        self.slider_value = value
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Slider(
                    value=self.slider_value,
                    onChanged=self._on_changed,
                    min=0.0,
                    max=1.0,
                    divisions=10,
                    label=f"{self.slider_value:.1f}",
                    activeColor=Colors.blue,
                ),
                Text(f"Value: {self.slider_value:.2f}"),
            ],
        )


class _ProgressDemo(StatefulWidget):
    def createState(self):
        return _ProgressDemoState()


class _ProgressDemoState(State[_ProgressDemo]):
    def initState(self):
        self.progress = 0.3

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("-10%"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "progress", max(0.0, self.progress - 0.1)
                                )
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("+10%"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "progress", min(1.0, self.progress + 0.1)
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"{self.progress * 100:.0f}%",
                            style=TextStyle(fontSize=14),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    width=400.0,
                    child=LinearProgressIndicator(
                        value=self.progress,
                        backgroundColor=Color(0xFFE0E0E0),
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(4),
                    ),
                ),
            ],
        )


class _SliderInteractionDemo(StatefulWidget):
    def createState(self):
        return _SliderInteractionDemoState()


class _SliderInteractionDemoState(State[_SliderInteractionDemo]):
    def initState(self):
        self.values = {
            "tapAndSlide": 0.5,
            "tapOnly": 0.5,
            "slideOnly": 0.5,
            "slideThumb": 0.5,
        }

    def _make_handler(self, key):
        def handler(value):
            self.values[key] = value
            self.setState(lambda: None)

        return handler

    def build(self, context):
        interactions = [
            ("tapAndSlide", SliderInteraction.tapAndSlide),
            ("tapOnly", SliderInteraction.tapOnly),
            ("slideOnly", SliderInteraction.slideOnly),
            ("slideThumb", SliderInteraction.slideThumb),
        ]
        rows = []
        for name, interaction in interactions:
            rows.append(
                Row(
                    children=[
                        Container(
                            width=100.0,
                            child=Text(
                                name,
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                        ),
                        Expanded(
                            child=Slider(
                                value=self.values[name],
                                onChanged=self._make_handler(name),
                                min=0.0,
                                max=1.0,
                                allowedInteraction=interaction,
                            ),
                        ),
                        Container(
                            width=40.0,
                            child=Text(
                                f"{self.values[name]:.1f}", style=TextStyle(fontSize=12)
                            ),
                        ),
                    ],
                ),
            )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=rows,
        )


class _ShowValueIndicatorDemo(StatefulWidget):
    def createState(self):
        return _ShowValueIndicatorDemoState()


class _ShowValueIndicatorDemoState(State[_ShowValueIndicatorDemo]):
    def initState(self):
        self.slider_value = 0.5
        self.mode_index = 0
        self.modes = [
            ("onlyForDiscrete", ShowValueIndicator.onlyForDiscrete),
            ("onlyForContinuous", ShowValueIndicator.onlyForContinuous),
            ("always", ShowValueIndicator.always),
            ("never", ShowValueIndicator.never),
        ]

    def _on_slider_changed(self, value):
        self.slider_value = value
        self.setState(lambda: None)

    def _next_mode(self):
        self.mode_index = (self.mode_index + 1) % len(self.modes)
        self.setState(lambda: None)

    def build(self, context):
        name, mode = self.modes[self.mode_index]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._next_mode,
                            child=Text(f"Mode: {name}"),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Slider(
                    value=self.slider_value,
                    onChanged=self._on_slider_changed,
                    min=0.0,
                    max=1.0,
                    divisions=10,
                    label=f"{self.slider_value:.1f}",
                    showValueIndicator=mode,
                ),
                Text(
                    f"Value: {self.slider_value:.1f}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _SliderSecondaryTrackDemo(StatefulWidget):
    def createState(self):
        return _SliderSecondaryTrackDemoState()


class _SliderSecondaryTrackDemoState(State[_SliderSecondaryTrackDemo]):
    def initState(self):
        self.value = 0.3
        self.buffer = 0.7

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Slider(
                    value=self.value,
                    secondaryTrackValue=self.buffer,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    min=0.0,
                    max=1.0,
                ),
                Text(
                    f"Value: {self.value:.2f}  Buffer: {self.buffer:.2f}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _SliderSemanticFormatterDemo(StatefulWidget):
    def createState(self):
        return _SliderSemanticFormatterDemoState()


class _SliderSemanticFormatterDemoState(State[_SliderSemanticFormatterDemo]):
    def initState(self):
        self.value = 0.5

    def _format_value(self, value):
        return f"{int(value * 100)}%"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Slider(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    min=0.0,
                    max=1.0,
                    divisions=20,
                    label=f"{int(self.value * 100)}%",
                    semanticFormatterCallback=self._format_value,
                ),
                Text(
                    f"Formatted: {int(self.value * 100)}%",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _SliderOverlayDemo(StatefulWidget):
    def createState(self):
        return _SliderOverlayDemoState()


class _SliderOverlayDemoState(State[_SliderOverlayDemo]):
    def initState(self):
        self.value = 0.5

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Slider(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    overlayColor=WidgetStatePropertyAll(Color(0x3300C853)),
                    padding=EdgeInsets.symmetric(horizontal=20),
                ),
                Text(
                    f"Value: {self.value:.2f}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _CircularProgressVariantsDemo(StatefulWidget):
    def createState(self):
        return _CircularProgressVariantsDemoState()


class _CircularProgressVariantsDemoState(State[_CircularProgressVariantsDemo]):
    def initState(self):
        self.variant_index = 0

    def build(self, context):
        variants = [
            (
                "Styling",
                "Compare backgroundColor, strokeCap, strokeAlign, and base ring colors.",
            ),
            (
                "Track Gap",
                "Inspect how trackGap, padding, and constraints change ring geometry.",
            ),
            (
                "Size & Padding",
                "Compare the default spinner against constrained and padded versions.",
            ),
        ]
        _, caption = variants[self.variant_index]

        chips = []
        for i, (label, _) in enumerate(variants):
            is_selected = i == self.variant_index
            chips.append(
                GestureDetector(
                    onTap=lambda idx=i: self.setState(
                        lambda: setattr(self, "variant_index", idx)
                    ),
                    child=Container(
                        padding=EdgeInsets.symmetric(horizontal=10, vertical=6),
                        decoration=BoxDecoration(
                            color=(Colors.blue if is_selected else Color(0xFFECEFF1)),
                            borderRadius=BorderRadius.circular(999),
                        ),
                        child=Text(
                            label,
                            style=TextStyle(
                                fontSize=12,
                                color=(Colors.white if is_selected else Colors.black),
                            ),
                        ),
                    ),
                )
            )

        if self.variant_index == 0:
            preview = Row(
                children=[
                    CircularProgressIndicator(
                        value=0.6,
                        backgroundColor=Color(0xFFE0E0E0),
                        strokeCap=StrokeCap.round,
                        color=Colors.blue,
                    ),
                    SizedBox(width=24),
                    CircularProgressIndicator(
                        value=0.4,
                        strokeAlign=1.0,
                        color=Colors.green,
                    ),
                    SizedBox(width=24),
                    CircularProgressIndicator(
                        value=0.8,
                        color=Colors.purple,
                    ),
                ],
            )
        elif self.variant_index == 1:
            preview = Center(
                child=CircularProgressIndicator(
                    value=0.5,
                    trackGap=8.0,
                    padding=EdgeInsets.all(20),
                    constraints=BoxConstraints(
                        minWidth=80,
                        minHeight=80,
                    ),
                    color=Colors.orange,
                    backgroundColor=Color(0xFFE0E0E0),
                ),
            )
        else:
            preview = Row(
                children=[
                    Column(
                        children=[
                            CircularProgressIndicator(),
                            SizedBox(height=8),
                            Text(
                                "default",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                    SizedBox(width=24),
                    Column(
                        children=[
                            CircularProgressIndicator(
                                constraints=BoxConstraints(
                                    minWidth=80,
                                    minHeight=80,
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "80x80",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                    SizedBox(width=24),
                    Column(
                        children=[
                            CircularProgressIndicator(
                                padding=EdgeInsets.all(20),
                            ),
                            SizedBox(height=8),
                            Text(
                                "padded",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                ],
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(spacing=8, runSpacing=8, children=chips),
                SizedBox(height=10),
                Text(
                    caption,
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
                SizedBox(height=12),
                preview,
            ],
        )


class SliderPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Slider & Progress",
            description=(
                "Shows continuous and discrete value input alongside progress "
                "indicators, so changes in state are reflected immediately in the "
                "UI."
            ),
            children=[
                SplitViewTile(
                    title="Slider",
                    description="A continuous or discrete input for selecting a value from a range.",
                    instruction="Drag the slider to change the value. Uses divisions=10 for discrete snapping.",
                    visible=_SliderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Slider(\n"
                            "    value=slider_value,\n"
                            "    onChanged=on_slider_changed,\n"
                            "    min=0.0, max=1.0, divisions=10,\n"
                            "    label=f'{slider_value:.1f}',\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="LinearProgressIndicator",
                    description="A horizontal bar that fills to indicate progress from 0.0 to 1.0.",
                    instruction="Use the buttons to adjust the progress value between 0% and 100%.",
                    visible=_ProgressDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "LinearProgressIndicator(\n"
                            "    value=progress,\n"
                            "    backgroundColor=Color(0xFFE0E0E0),\n"
                            "    color=Colors.blue,\n"
                            "    borderRadius=BorderRadius.circular(4),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SliderInteraction",
                    description=(
                        "SliderInteraction controls how users can interact with a Slider: "
                        "tapAndSlide (default), tapOnly, slideOnly, or slideThumb."
                    ),
                    instruction="Drag each slider to feel the difference between interaction modes.",
                    visible=_SliderInteractionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    allowedInteraction=SliderInteraction.tapAndSlide,\n"
                            ")\n\n"
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    allowedInteraction=SliderInteraction.tapOnly,\n"
                            ")\n\n"
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    allowedInteraction=SliderInteraction.slideOnly,\n"
                            ")\n\n"
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    allowedInteraction=SliderInteraction.slideThumb,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ShowValueIndicator",
                    description=(
                        "ShowValueIndicator controls when the value-indicator bubble "
                        "appears on a Slider: onlyForDiscrete, onlyForContinuous, always, or never."
                    ),
                    instruction="Toggle the mode and drag the slider to see when the bubble appears.",
                    visible=_ShowValueIndicatorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    divisions=10,\n"
                            "    label=f'{val:.1f}',\n"
                            "    showValueIndicator=ShowValueIndicator.always,\n"
                            ")\n\n"
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    showValueIndicator=ShowValueIndicator.never,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Slider secondaryTrackValue",
                    description=(
                        "Slider with secondaryTrackValue showing a buffer/preload indicator. "
                        "The secondary track fills independently of the primary value."
                    ),
                    instruction="Drag the slider and observe the secondary track at 0.7.",
                    visible=_SliderSecondaryTrackDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Slider(\n"
                            "    value=0.3,\n"
                            "    secondaryTrackValue=0.7,\n"
                            "    onChanged=on_changed,\n"
                            "    min=0.0, max=1.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Slider overlayColor & focusNode",
                    description=(
                        "Slider with a green overlay color and horizontal padding. "
                        "The drag overlay appears green."
                    ),
                    instruction="Drag the slider to see the green overlay.",
                    visible=_SliderOverlayDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Slider(\n"
                            "    value=0.5,\n"
                            "    onChanged=on_changed,\n"
                            "    overlayColor=WidgetStatePropertyAll(\n"
                            "        Color(0x3300C853),\n"
                            "    ),\n"
                            "    padding=EdgeInsets.symmetric(horizontal=20),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Slider semanticFormatterCallback",
                    description=(
                        "Slider with semanticFormatterCallback formatting the value as a "
                        "percentage string for accessibility and display."
                    ),
                    instruction="Drag the slider to see the value displayed as a percentage.",
                    visible=_SliderSemanticFormatterDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "def format_value(value):\n"
                            "    return f'{int(value * 100)}%'\n\n"
                            "Slider(\n"
                            "    value=val,\n"
                            "    onChanged=on_changed,\n"
                            "    divisions=20,\n"
                            "    label=f'{int(val * 100)}%',\n"
                            "    semanticFormatterCallback=format_value,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CircularProgressIndicator variants",
                    description=(
                        "Merges styling, track geometry, and size/padding into one "
                        "switchable demo so all circular progress options are compared in context."
                    ),
                    instruction="Use the chips to switch between styling, track-gap, and size/padding variants.",
                    visible=_CircularProgressVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "# Styling\n"
                            "CircularProgressIndicator(\n"
                            "    value=0.6,\n"
                            "    backgroundColor=Color(0xFFE0E0E0),\n"
                            "    strokeCap=StrokeCap.round,\n"
                            ")\n\n"
                            "# Track geometry\n"
                            "CircularProgressIndicator(\n"
                            "    value=0.5,\n"
                            "    trackGap=8.0,\n"
                            "    padding=EdgeInsets.all(20),\n"
                            "    constraints=BoxConstraints(\n"
                            "        minWidth=80, minHeight=80,\n"
                            "    ),\n"
                            ")\n\n"
                            "# Size & padding\n"
                            "CircularProgressIndicator()\n"
                            "CircularProgressIndicator(\n"
                            "    constraints=BoxConstraints(\n"
                            "        minWidth=80, minHeight=80,\n"
                            "    ),\n"
                            ")\n"
                            "CircularProgressIndicator(\n"
                            "    padding=EdgeInsets.all(20),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="LinearProgressIndicator stopIndicator & trackGap",
                    description=(
                        "LinearProgressIndicator with value=0.6, red stopIndicatorColor, "
                        "stopIndicatorRadius=4, and trackGap=6."
                    ),
                    instruction="Observe the visible stop dot and track gap in the indicator.",
                    visible=Container(
                        width=400.0,
                        child=LinearProgressIndicator(
                            value=0.6,
                            stopIndicatorColor=Colors.red,
                            stopIndicatorRadius=4,
                            trackGap=6,
                            color=Colors.blue,
                            backgroundColor=Color(0xFFE0E0E0),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "LinearProgressIndicator(\n"
                            "    value=0.6,\n"
                            "    stopIndicatorColor=Colors.red,\n"
                            "    stopIndicatorRadius=4,\n"
                            "    trackGap=6,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Determinate Progress Indicators",
                    description=(
                        "CircularProgressIndicator and LinearProgressIndicator with an explicit "
                        "value show fixed progress instead of an indeterminate spinner."
                    ),
                    instruction="Static indicators at 65% (circular) and 40% (linear).",
                    visible=Row(
                        children=[
                            CircularProgressIndicator(
                                value=0.65, color=Colors.green, strokeWidth=6.0
                            ),
                            SizedBox(width=16),
                            LinearProgressIndicator(
                                value=0.4,
                                color=Colors.deepPurple,
                                minHeight=8.0,
                                borderRadius=BorderRadius.circular(4),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CircularProgressIndicator(value=0.65, strokeWidth=6.0)\n"
                            "LinearProgressIndicator(value=0.4, minHeight=8.0)"
                        ),
                    ),
                ),
            ],
        )
