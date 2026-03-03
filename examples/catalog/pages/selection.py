from utils import CODE_FONT_FAMILY
from flut.dart import Color, Duration
from flut.dart.ui import Clip
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Center,
    Expanded,
    Wrap,
    Padding,
    Icon,
    MouseRegion,
    RadioGroup,
    WidgetStatePropertyAll,
    IconThemeData,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    BoxConstraints,
    MainAxisAlignment,
)
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Icons,
    Switch,
    Radio,
    Chip,
    ChipAnimationStyle,
    Checkbox,
    MaterialTapTargetSize,
    ExpansionTile,
    ListTile,
    TextButton,
)
from flut.flutter.material.theme_data import VisualDensity
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    BorderSide,
    Border,
    RoundedRectangleBorder,
    Alignment,
    VerticalDirection,
)
from flut.flutter.animation import AnimationStyle

from widgets import CatalogPage, SplitViewTile, CodeArea


class _RadioDemo(StatefulWidget):
    def createState(self):
        return _RadioDemoState()


class _RadioDemoState(State[_RadioDemo]):
    def initState(self):
        self.radio_value = "apple"

    def _on_changed(self, value):
        self.radio_value = value
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                RadioGroup(
                    groupValue=self.radio_value,
                    onChanged=self._on_changed,
                    child=Row(
                        children=[
                            Radio(value="apple"),
                            Text("Apple"),
                            SizedBox(width=16),
                            Radio(value="banana"),
                            Text("Banana"),
                            SizedBox(width=16),
                            Radio(value="cherry"),
                            Text("Cherry"),
                        ],
                    ),
                ),
                Text(f"Selected: {self.radio_value}"),
            ],
        )


class _ChipDemo(StatefulWidget):
    def createState(self):
        return _ChipDemoState()


class _ChipDemoState(State[_ChipDemo]):
    def initState(self):
        self.chips = ["Flutter", "Python", "Dart"]

    def _delete_chip(self, label):
        self.chips = [c for c in self.chips if c != label]
        self.setState(lambda: None)

    def build(self, context):
        return Row(
            children=(
                [
                    *(
                        Padding(
                            padding=EdgeInsets.only(right=8),
                            child=Chip(
                                label=Text(label),
                                backgroundColor=Color(0xFFE3F2FD),
                                onDeleted=lambda l=label: self._delete_chip(l),
                            ),
                        )
                        for label in self.chips
                    )
                ]
                if self.chips
                else [Text("All chips deleted!")]
            ),
        )


class _SwitchDemo(StatefulWidget):
    def createState(self):
        return _SwitchDemoState()


class _SwitchDemoState(State[_SwitchDemo]):
    def initState(self):
        self.switch_value = False

    def build(self, context):
        return Row(
            children=[
                Switch(
                    value=self.switch_value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "switch_value", v)
                    ),
                    activeTrackColor=Colors.blue,
                ),
                SizedBox(width=12),
                Text(
                    f"Switch is {'ON' if self.switch_value else 'OFF'}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _RadioFillColorDemo(StatefulWidget):
    def createState(self):
        return _RadioFillColorDemoState()


class _RadioFillColorDemoState(State[_RadioFillColorDemo]):
    def initState(self):
        self.value = "red"

    def build(self, context):
        return Row(
            children=[
                RadioGroup(
                    groupValue=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    child=Row(
                        children=[
                            Radio(
                                value="red",
                                fillColor=WidgetStatePropertyAll(Colors.red),
                            ),
                            Text("Red"),
                            SizedBox(width=12),
                            Radio(
                                value="green",
                                fillColor=WidgetStatePropertyAll(Colors.green),
                            ),
                            Text("Green"),
                            SizedBox(width=12),
                            Radio(
                                value="blue",
                                fillColor=WidgetStatePropertyAll(Colors.blue),
                            ),
                            Text("Blue"),
                        ],
                    ),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.value}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _RadioSizeDemo(StatefulWidget):
    def createState(self):
        return _RadioSizeDemoState()


class _RadioSizeDemoState(State[_RadioSizeDemo]):
    def initState(self):
        self.standard_value = "a"
        self.compact_value = "a"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "Standard", style=TextStyle(fontSize=12, fontWeight=FontWeight.bold)
                ),
                RadioGroup(
                    groupValue=self.standard_value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "standard_value", v)
                    ),
                    child=Row(
                        children=[
                            Radio(value="a"),
                            Text("A"),
                            SizedBox(width=8),
                            Radio(value="b"),
                            Text("B"),
                        ],
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "Compact + shrinkWrap",
                    style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                ),
                RadioGroup(
                    groupValue=self.compact_value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "compact_value", v)
                    ),
                    child=Row(
                        children=[
                            Radio(
                                value="a",
                                visualDensity=VisualDensity.compact,
                                materialTapTargetSize=MaterialTapTargetSize.shrinkWrap,
                            ),
                            Text("A"),
                            SizedBox(width=8),
                            Radio(
                                value="b",
                                visualDensity=VisualDensity.compact,
                                materialTapTargetSize=MaterialTapTargetSize.shrinkWrap,
                            ),
                            Text("B"),
                        ],
                    ),
                ),
            ],
        )


class _RadioDisabledDemo(StatefulWidget):
    def createState(self):
        return _RadioDisabledDemoState()


class _RadioDisabledDemoState(State[_RadioDisabledDemo]):
    def initState(self):
        self.value = "enabled"

    def build(self, context):
        return Row(
            children=[
                RadioGroup(
                    groupValue=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    child=Row(
                        children=[
                            Radio(value="disabled", enabled=False),
                            Text("Disabled", style=TextStyle(color=Colors.grey)),
                            SizedBox(width=12),
                            Radio(
                                value="enabled",
                                side=BorderSide(color=Colors.orange, width=2),
                            ),
                            Text("Styled border"),
                        ],
                    ),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.value}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _SwitchThumbColorDemo(StatefulWidget):
    def createState(self):
        return _SwitchThumbColorDemoState()


class _SwitchThumbColorDemoState(State[_SwitchThumbColorDemo]):
    def initState(self):
        self.value = True

    def build(self, context):
        return Row(
            children=[
                Switch(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    thumbColor=WidgetStatePropertyAll(Colors.purple),
                    trackColor=WidgetStatePropertyAll(Color(0xFFE1BEE7)),
                    trackOutlineColor=WidgetStatePropertyAll(Colors.purple),
                ),
                SizedBox(width=12),
                Text(
                    f"Switch is {'ON' if self.value else 'OFF'}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _SwitchThumbIconDemo(StatefulWidget):
    def createState(self):
        return _SwitchThumbIconDemoState()


class _SwitchThumbIconDemoState(State[_SwitchThumbIconDemo]):
    def initState(self):
        self.value = False

    def build(self, context):
        return Row(
            children=[
                Switch(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    thumbIcon=WidgetStatePropertyAll(
                        Icon(Icons.check, size=16)
                        if self.value
                        else Icon(Icons.close, size=16)
                    ),
                ),
                SizedBox(width=12),
                Text(
                    f"Switch is {'ON' if self.value else 'OFF'}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _SwitchOverlayDemo(StatefulWidget):
    def createState(self):
        return _SwitchOverlayDemoState()


class _SwitchOverlayDemoState(State[_SwitchOverlayDemo]):
    def initState(self):
        self.value = True

    def build(self, context):
        return Row(
            children=[
                Switch(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    overlayColor=WidgetStatePropertyAll(Color(0x33FF0000)),
                    splashRadius=25.0,
                    padding=EdgeInsets.all(12),
                ),
                SizedBox(width=12),
                Text(
                    f"Switch is {'ON' if self.value else 'OFF'}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _ChipDeleteIconDemo(StatefulWidget):
    def createState(self):
        return _ChipDeleteIconDemoState()


class _ChipDeleteIconDemoState(State[_ChipDeleteIconDemo]):
    def initState(self):
        self.visible = True

    def _delete(self):
        self.visible = False
        self.setState(lambda: None)

    def _reset(self):
        self.visible = True
        self.setState(lambda: None)

    def build(self, context):
        if not self.visible:
            return Row(
                children=[
                    Text(
                        "Chip removed!", style=TextStyle(fontSize=13, color=Colors.grey)
                    ),
                    SizedBox(width=8),
                    TextButton(onPressed=self._reset, child=Text("Reset")),
                ],
            )
        return Chip(
            label=Text("Removable"),
            deleteIcon=Icon(Icons.cancel, size=18),
            deleteButtonTooltipMessage="Remove item",
            onDeleted=self._delete,
            backgroundColor=Color(0xFFE3F2FD),
        )


class _ChipAnimationStyleDemo(StatefulWidget):
    def createState(self):
        return _ChipAnimationStyleDemoState()


class _ChipAnimationStyleDemoState(State[_ChipAnimationStyleDemo]):
    def initState(self):
        self.default_enabled = True
        self.no_anim_enabled = True

    def _toggle_both(self):
        self.default_enabled = not self.default_enabled
        self.no_anim_enabled = not self.no_anim_enabled
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._toggle_both,
                            child=Text("Toggle Both"),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Text(
                                    "Default animation",
                                    style=TextStyle(
                                        fontSize=12, fontWeight=FontWeight.bold
                                    ),
                                ),
                                SizedBox(height=4),
                                *(
                                    [
                                        Chip(
                                            label=Text("Animated"),
                                            backgroundColor=Color(0xFFE3F2FD),
                                        ),
                                    ]
                                    if self.default_enabled
                                    else [
                                        Text(
                                            "(disabled)",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        )
                                    ]
                                ),
                            ],
                        ),
                        SizedBox(width=24),
                        Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Text(
                                    "No animation",
                                    style=TextStyle(
                                        fontSize=12, fontWeight=FontWeight.bold
                                    ),
                                ),
                                SizedBox(height=4),
                                *(
                                    [
                                        Chip(
                                            label=Text("No Anim"),
                                            backgroundColor=Color(0xFFFCE4EC),
                                            chipAnimationStyle=ChipAnimationStyle(
                                                enableAnimation=AnimationStyle.noAnimation,
                                            ),
                                        ),
                                    ]
                                    if self.no_anim_enabled
                                    else [
                                        Text(
                                            "(disabled)",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        )
                                    ]
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )


class _ListTileControlAffinityDemo(StatefulWidget):
    def createState(self):
        return _ListTileControlAffinityDemoState()


class _ListTileControlAffinityDemoState(State[_ListTileControlAffinityDemo]):
    def initState(self):
        self.leading_checked = False
        self.trailing_checked = True
        self.platform_checked = False

    def build(self, context):
        return Container(
            width=500.0,
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    ListTile(
                        leading=Checkbox(
                            value=self.leading_checked,
                            onChanged=lambda v: self.setState(
                                lambda: setattr(self, "leading_checked", v)
                            ),
                        ),
                        title=Text("Leading affinity"),
                        subtitle=Text("Checkbox on the left"),
                    ),
                    ListTile(
                        title=Text("Trailing affinity"),
                        subtitle=Text("Checkbox on the right"),
                        trailing=Checkbox(
                            value=self.trailing_checked,
                            onChanged=lambda v: self.setState(
                                lambda: setattr(self, "trailing_checked", v)
                            ),
                        ),
                    ),
                    ListTile(
                        leading=Checkbox(
                            value=self.platform_checked,
                            onChanged=lambda v: self.setState(
                                lambda: setattr(self, "platform_checked", v)
                            ),
                        ),
                        title=Text("Platform affinity"),
                        subtitle=Text("Defaults to leading on this platform"),
                    ),
                ],
            ),
        )


class _TristateCheckboxDemo(StatefulWidget):
    def createState(self):
        return _TristateCheckboxDemoState()


class _TristateCheckboxDemoState(State["_TristateCheckboxDemo"]):

    def initState(self):
        self.tri_value = None

    def build(self, context):
        return Row(
            children=[
                Text("Tristate Checkbox:", style=TextStyle(fontSize=13)),
                SizedBox(width=8),
                Checkbox(
                    value=self.tri_value,
                    tristate=True,
                    activeColor=Colors.deepPurple,
                    checkColor=Colors.white,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "tri_value", v)
                    ),
                ),
                SizedBox(width=4),
                Text(
                    f"= {self.tri_value}",
                    style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                ),
            ],
        )


class _ColoredSwitchDemo(StatefulWidget):
    def createState(self):
        return _ColoredSwitchDemoState()


class _ColoredSwitchDemoState(State["_ColoredSwitchDemo"]):

    def initState(self):
        self.switch_val = False

    def build(self, context):
        return Row(
            children=[
                Text("Switch with colors:", style=TextStyle(fontSize=13)),
                SizedBox(width=8),
                Switch(
                    value=self.switch_val,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "switch_val", v)
                    ),
                    activeThumbColor=Colors.green,
                    activeTrackColor=Color(0xFFA5D6A7),
                    inactiveThumbColor=Colors.red,
                    inactiveTrackColor=Color(0xFFEF9A9A),
                ),
            ],
        )


class _SwitchColorVariantsDemo(StatefulWidget):
    def createState(self):
        return _SwitchColorVariantsDemoState()


class _SwitchColorVariantsDemoState(State[_SwitchColorVariantsDemo]):
    def initState(self):
        self.variant = "theme"
        self.value = True

    def _select_variant(self, variant):
        self.variant = variant
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        (
                            ElevatedButton(
                                onPressed=lambda: self._select_variant("theme"),
                                child=Text("Theme"),
                            )
                            if self.variant == "theme"
                            else TextButton(
                                onPressed=lambda: self._select_variant("theme"),
                                child=Text("Theme"),
                            )
                        ),
                        (
                            ElevatedButton(
                                onPressed=lambda: self._select_variant("states"),
                                child=Text("Active / Inactive"),
                            )
                            if self.variant == "states"
                            else TextButton(
                                onPressed=lambda: self._select_variant("states"),
                                child=Text("Active / Inactive"),
                            )
                        ),
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        Switch(
                            value=self.value,
                            onChanged=lambda v: self.setState(
                                lambda: setattr(self, "value", v)
                            ),
                            thumbColor=(
                                WidgetStatePropertyAll(Colors.purple)
                                if self.variant == "theme"
                                else None
                            ),
                            trackColor=(
                                WidgetStatePropertyAll(Color(0xFFE1BEE7))
                                if self.variant == "theme"
                                else None
                            ),
                            trackOutlineColor=(
                                WidgetStatePropertyAll(Colors.purple)
                                if self.variant == "theme"
                                else None
                            ),
                            activeThumbColor=(
                                Colors.green if self.variant == "states" else None
                            ),
                            activeTrackColor=(
                                Color(0xFFA5D6A7) if self.variant == "states" else None
                            ),
                            inactiveThumbColor=(
                                Colors.red if self.variant == "states" else None
                            ),
                            inactiveTrackColor=(
                                Color(0xFFEF9A9A) if self.variant == "states" else None
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"Switch is {'ON' if self.value else 'OFF'}",
                            style=TextStyle(fontSize=14),
                        ),
                    ],
                ),
            ],
        )


class SelectionPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Selection",
            description=(
                "Compares common choice controls for single, multiple, and toggle "
                "selection, with visible state changes and grouped interactions."
            ),
            children=[
                SplitViewTile(
                    title="RadioGroup + Radio",
                    description=(
                        "RadioGroup wraps a set of Radio widgets with shared "
                        "groupValue and onChanged, so you don't pass them to each Radio."
                    ),
                    instruction="Select a fruit. The groupValue tracks which radio is active.",
                    visible=_RadioDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "RadioGroup(\n"
                            "    groupValue=radio_value,\n"
                            "    onChanged=on_radio_changed,\n"
                            "    child=Row(children=[\n"
                            "        Radio(value='apple'), Text('Apple'),\n"
                            "        Radio(value='banana'), Text('Banana'),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip",
                    description="A compact element representing an attribute, input, or action. Supports optional delete.",
                    instruction="Click the X on each chip to remove it from the list.",
                    visible=_ChipDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    label=Text('Flutter'),\n"
                            "    backgroundColor=Color(0xFFE3F2FD),\n"
                            "    onDeleted=lambda: delete_chip('Flutter'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Switch",
                    description="A toggling control that switches between on and off states.",
                    instruction="Toggle the switch on and off.",
                    visible=_SwitchDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Switch(\n"
                            "    value=switch_value,\n"
                            "    onChanged=on_switch_changed,\n"
                            "    activeTrackColor=Colors.blue,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTileControlAffinity",
                    description=(
                        "ListTileControlAffinity determines whether a control widget "
                        "(like a Checkbox) appears at the leading or trailing edge of a ListTile. "
                        "Demonstrated here by placing Checkbox as leading vs trailing."
                    ),
                    instruction="Toggle the checkboxes to see them in leading and trailing positions.",
                    visible=_ListTileControlAffinityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    leading=Checkbox(value=val, onChanged=on_changed),\n"
                            "    title=Text('Leading affinity'),\n"
                            ")\n\n"
                            "ListTile(\n"
                            "    title=Text('Trailing affinity'),\n"
                            "    trailing=Checkbox(value=val, onChanged=on_changed),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ChipAnimationStyle",
                    description=(
                        "ChipAnimationStyle controls how Chip widgets animate when "
                        "their state changes. Use AnimationStyle.noAnimation to disable transitions."
                    ),
                    instruction="Toggle both chips to compare the default animation with no animation.",
                    visible=_ChipAnimationStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    label=Text('Animated'),\n"
                            "    backgroundColor=Color(0xFFE3F2FD),\n"
                            ")\n\n"
                            "Chip(\n"
                            "    label=Text('No Anim'),\n"
                            "    backgroundColor=Color(0xFFFCE4EC),\n"
                            "    chipAnimationStyle=ChipAnimationStyle(\n"
                            "        enableAnimation=AnimationStyle.noAnimation,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip deleteIcon & tooltip",
                    description=(
                        "Chip with a custom deleteIcon and deleteButtonTooltipMessage. "
                        "Click the X to remove the chip, then click Reset to restore it."
                    ),
                    instruction="Click the delete icon to remove the chip. Hover over it to see the tooltip.",
                    visible=_ChipDeleteIconDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    label=Text('Removable'),\n"
                            "    deleteIcon=Icon(Icons.cancel, size=18),\n"
                            "    deleteButtonTooltipMessage='Remove item',\n"
                            "    onDeleted=on_delete,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip shape & side",
                    description=(
                        "Three Chips demonstrating default styling, a custom side (red border), "
                        "and a custom shape (small border radius)."
                    ),
                    instruction="Compare the three chip outlines: default, red border, and squared shape.",
                    visible=Row(
                        children=[
                            Chip(label=Text("Default")),
                            SizedBox(width=8),
                            Chip(
                                label=Text("Red border"),
                                side=BorderSide(color=Colors.red, width=2),
                            ),
                            SizedBox(width=8),
                            Chip(
                                label=Text("Squared"),
                                shape=RoundedRectangleBorder(
                                    borderRadius=BorderRadius.circular(4),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(label=Text('Default'))\n\n"
                            "Chip(\n"
                            "    label=Text('Red border'),\n"
                            "    side=BorderSide(color=Colors.red, width=2),\n"
                            ")\n\n"
                            "Chip(\n"
                            "    label=Text('Squared'),\n"
                            "    shape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(4),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip clipBehavior & color",
                    description=(
                        "Chip with clipBehavior=Clip.antiAlias and a solid amber color "
                        "via WidgetStatePropertyAll."
                    ),
                    instruction="Observe the amber-colored chip with anti-alias clipping.",
                    visible=Chip(
                        label=Text("Amber Chip"),
                        clipBehavior=Clip.antiAlias,
                        color=WidgetStatePropertyAll(Colors.amber),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    label=Text('Amber Chip'),\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            "    color=WidgetStatePropertyAll(Colors.amber),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip visualDensity & materialTapTargetSize",
                    description=(
                        "Three chips: standard, compact visualDensity, and shrinkWrap "
                        "materialTapTargetSize for increasingly tight layout."
                    ),
                    instruction="Compare the sizes of the three chips from standard to most compact.",
                    visible=Row(
                        children=[
                            Chip(label=Text("Standard")),
                            SizedBox(width=8),
                            Chip(
                                label=Text("Compact"),
                                visualDensity=VisualDensity.compact,
                            ),
                            SizedBox(width=8),
                            Chip(
                                label=Text("ShrinkWrap"),
                                materialTapTargetSize=MaterialTapTargetSize.shrinkWrap,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(label=Text('Standard'))\n\n"
                            "Chip(\n"
                            "    label=Text('Compact'),\n"
                            "    visualDensity=VisualDensity.compact,\n"
                            ")\n\n"
                            "Chip(\n"
                            "    label=Text('ShrinkWrap'),\n"
                            "    materialTapTargetSize=MaterialTapTargetSize.shrinkWrap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip iconTheme & boxConstraints",
                    description=(
                        "Chip with iconTheme setting green icons at size 20, and "
                        "avatarBoxConstraints=BoxConstraints.tightFor(width=32, height=32)."
                    ),
                    instruction="Observe the sized avatar area with green icon theme.",
                    visible=Chip(
                        avatar=Icon(Icons.person),
                        label=Text("Themed icon"),
                        iconTheme=IconThemeData(color=Colors.green, size=20),
                        avatarBoxConstraints=BoxConstraints(
                            minWidth=32, maxWidth=32, minHeight=32, maxHeight=32
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    avatar=Icon(Icons.person),\n"
                            "    label=Text('Themed icon'),\n"
                            "    iconTheme=IconThemeData(color=Colors.green, size=20),\n"
                            "    avatarBoxConstraints=BoxConstraints(\n"
                            "        minWidth=32, maxWidth=32,\n"
                            "        minHeight=32, maxHeight=32,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Switch color theming",
                    description=(
                        "Compares two common color strategies for Switch: a single themed palette "
                        "and separate active or inactive colors for stronger state contrast."
                    ),
                    instruction="Choose Theme or Active / Inactive, then toggle the switch to compare the color behavior.",
                    visible=_SwitchColorVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "variant = 'states'\n\n"
                            "Switch(\n"
                            "    value=switch_val,\n"
                            "    onChanged=on_changed,\n"
                            "    thumbColor=WidgetStatePropertyAll(Colors.purple)\n"
                            "        if variant == 'theme' else None,\n"
                            "    trackColor=WidgetStatePropertyAll(Color(0xFFE1BEE7))\n"
                            "        if variant == 'theme' else None,\n"
                            "    activeThumbColor=Colors.green\n"
                            "        if variant == 'states' else None,\n"
                            "    inactiveThumbColor=Colors.red\n"
                            "        if variant == 'states' else None,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Switch thumbIcon",
                    description=(
                        "Switch whose thumb displays Icons.check when on and Icons.close when off "
                        "via thumbIcon with WidgetStatePropertyAll."
                    ),
                    instruction="Toggle the switch to see the icon inside the thumb change.",
                    visible=_SwitchThumbIconDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Switch(\n"
                            "    value=is_on,\n"
                            "    onChanged=on_changed,\n"
                            "    thumbIcon=WidgetStatePropertyAll(\n"
                            "        Icon(Icons.check) if is_on\n"
                            "        else Icon(Icons.close),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Switch overlayColor & splashRadius & padding",
                    description=(
                        "Switch with red overlay, splashRadius=25, and extra padding. "
                        "The splash area is larger and colored."
                    ),
                    instruction="Tap the switch to see the large red splash effect.",
                    visible=_SwitchOverlayDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Switch(\n"
                            "    value=True,\n"
                            "    onChanged=on_changed,\n"
                            "    overlayColor=WidgetStatePropertyAll(\n"
                            "        Color(0x33FF0000),\n"
                            "    ),\n"
                            "    splashRadius=25.0,\n"
                            "    padding=EdgeInsets.all(12),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Radio fillColor & overlayColor",
                    description=(
                        "Three Radio buttons with different fillColor values (red, green, blue) "
                        "via WidgetStatePropertyAll."
                    ),
                    instruction="Select each radio to see the colored fill.",
                    visible=_RadioFillColorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Radio(\n"
                            "    value='red',\n"
                            "    fillColor=WidgetStatePropertyAll(Colors.red),\n"
                            ")\n\n"
                            "Radio(\n"
                            "    value='green',\n"
                            "    fillColor=WidgetStatePropertyAll(Colors.green),\n"
                            ")\n\n"
                            "Radio(\n"
                            "    value='blue',\n"
                            "    fillColor=WidgetStatePropertyAll(Colors.blue),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Radio materialTapTargetSize & visualDensity",
                    description=(
                        "Compare standard Radio size vs shrinkWrap+compact Radio. "
                        "The compact variant takes less space."
                    ),
                    instruction="Observe the size difference between standard and compact radios.",
                    visible=_RadioSizeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Radio(value='a')\n\n"
                            "Radio(\n"
                            "    value='a',\n"
                            "    visualDensity=VisualDensity.compact,\n"
                            "    materialTapTargetSize=\n"
                            "        MaterialTapTargetSize.shrinkWrap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Radio innerRadius & enabled",
                    description=(
                        "A disabled Radio (greyed out) next to one with a custom "
                        "side=BorderSide for styled appearance."
                    ),
                    instruction="The first radio is disabled; the second has an orange border.",
                    visible=_RadioDisabledDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Radio(value='disabled', enabled=False)\n\n"
                            "Radio(\n"
                            "    value='enabled',\n"
                            "    side=BorderSide(\n"
                            "        color=Colors.orange, width=2,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Tristate Checkbox",
                    description=(
                        "A Checkbox with tristate=True cycles through True, False, "
                        "and None (indeterminate dash)."
                    ),
                    instruction="Click the checkbox repeatedly to cycle through all three states.",
                    visible=_TristateCheckboxDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Checkbox(\n"
                            "    value=tri_value,\n"
                            "    tristate=True,\n"
                            "    activeColor=Colors.deepPurple,\n"
                            "    onChanged=on_changed,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
