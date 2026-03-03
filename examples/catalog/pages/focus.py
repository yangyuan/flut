from utils import CODE_FONT_FAMILY
from flut.dart import Color
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Wrap,
    Center,
    Expanded,
    GestureDetector,
    Icon,
    FocusNode,
    FocusScopeNode,
    FocusTraversalGroup,
    FocusTraversalOrder,
    FocusTraversalPolicy,
    OrderedTraversalPolicy,
    ReadingOrderTraversalPolicy,
    WidgetOrderTraversalPolicy,
    NumericFocusOrder,
    TraversalDirection,
    TraversalEdgeBehavior,
    CallbackShortcuts,
    SingleActivator,
    Visibility,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    IconButton,
    TextButton,
    OutlinedButton,
    Switch,
    Chip,
    Icons,
    TextField,
    InputDecoration,
    InputBorder,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Border,
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
)
from flut.flutter.services import (
    KeyEvent,
    KeyDownEvent,
    SystemMouseCursors,
)
from flut.flutter.widgets import KeyEventResult
from flut.flutter.services.keyboard_key import (
    LogicalKeyboardKey,
    PhysicalKeyboardKey,
)
from flut.dart.core import Duration
from widgets import CatalogPage, SplitViewTile, CodeArea


def func_a(event: KeyEvent):
    label = event.logicalKey.keyLabel
    return f"A: {label}"


def func_b(event: KeyEvent):
    label = event.logicalKey.keyLabel
    return f"B: {label}"


class _FocusNodeDemo(StatefulWidget):
    def createState(self):
        return _FocusNodeDemoState()


class _FocusNodeDemoState(State[_FocusNodeDemo]):

    def initState(self):
        self.focus_node = FocusNode(onKeyEvent=self._handle_key_a)
        self.log = []
        self.handler_label = "func_A"

    def _handle_key_a(self, event: KeyEvent):
        if not isinstance(event, KeyDownEvent):
            return KeyEventResult.ignored
        msg = func_a(event)
        self.log = (self.log + [msg])[-12:]
        self.setState(lambda: None)
        return KeyEventResult.handled

    def _handle_key_b(self, event: KeyEvent):
        if not isinstance(event, KeyDownEvent):
            return KeyEventResult.ignored
        msg = func_b(event)
        self.log = (self.log + [msg])[-12:]
        self.setState(lambda: None)
        return KeyEventResult.handled

    def _switch_to_a(self):
        self.focus_node.onKeyEvent = self._handle_key_a
        self.handler_label = "func_A"
        self.log = self.log + ["-- switched to func_A --"]
        self.setState(lambda: None)

    def _switch_to_b(self):
        self.focus_node.onKeyEvent = self._handle_key_b
        self.handler_label = "func_B"
        self.log = self.log + ["-- switched to func_B --"]
        self.setState(lambda: None)

    def _clear_handler(self):
        self.focus_node.onKeyEvent = None
        self.handler_label = "None"
        self.log = self.log + ["-- cleared onKeyEvent --"]
        self.setState(lambda: None)

    def _call_directly(self):
        cb = self.focus_node.onKeyEvent
        if cb is not None:
            result = cb(
                KeyDownEvent(
                    physicalKey=PhysicalKeyboardKey(0x00070004),
                    logicalKey=LogicalKeyboardKey(0x78),
                    timeStamp=Duration(),
                )
            )
            self.log = self.log + [f"direct call -> {result}"]
        else:
            self.log = self.log + ["onKeyEvent is None"]
        self.setState(lambda: None)

    def build(self, context):
        log_widgets = []
        for entry in self.log[-12:]:
            color = Colors.blue
            if entry.startswith("B:"):
                color = Colors.green
            elif entry.startswith("--"):
                color = Colors.orange
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=color,
                    ),
                ),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "Click the text field and press keys.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Current handler: {self.handler_label}",
                    style=TextStyle(fontSize=13),
                ),
                SizedBox(height=8),
                Container(
                    width=400.0,
                    child=TextField(
                        focusNode=self.focus_node,
                        decoration=InputDecoration(
                            hintText="Click here and type to fire key events...",
                            border=InputBorder.none,
                        ),
                        readOnly=True,
                    ),
                ),
                SizedBox(height=12),
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("func_A"),
                            onPressed=self._switch_to_a,
                        ),
                        ElevatedButton(
                            child=Text("func_B"),
                            onPressed=self._switch_to_b,
                        ),
                        ElevatedButton(
                            child=Text("None"),
                            onPressed=self._clear_handler,
                        ),
                        ElevatedButton(
                            child=Text("Call directly"),
                            onPressed=self._call_directly,
                        ),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Colors.black12,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=log_widgets,
                    ),
                ),
            ],
        )


class _IconButtonFocusDemo(StatefulWidget):
    def createState(self):
        return _IconButtonFocusDemoState()


class _IconButtonFocusDemoState(State[_IconButtonFocusDemo]):
    def initState(self):
        self.focus_node = FocusNode()
        self.tap_count = 0

    def _on_pressed(self):
        self.setState(lambda: setattr(self, "tap_count", self.tap_count + 1))

    def _request_focus(self):
        self.focus_node.requestFocus()

    def _unfocus(self):
        self.focus_node.unfocus()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Column(
                            children=[
                                IconButton(
                                    icon=Icon(Icons.center_focus_strong),
                                    focusNode=self.focus_node,
                                    onPressed=self._on_pressed,
                                    tooltip="Has focusNode",
                                ),
                                Text("focusNode", style=TextStyle(fontSize=11)),
                            ],
                        ),
                        SizedBox(width=24),
                        Column(
                            children=[
                                IconButton(
                                    icon=Icon(Icons.auto_fix_high),
                                    autofocus=True,
                                    onPressed=lambda: None,
                                    tooltip="autofocus=True",
                                ),
                                Text("autofocus", style=TextStyle(fontSize=11)),
                            ],
                        ),
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Request Focus"),
                            onPressed=self._request_focus,
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Unfocus"),
                            onPressed=self._unfocus,
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"taps: {self.tap_count}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _TextButtonHoverFocusDemo(StatefulWidget):
    def createState(self):
        return _TextButtonHoverFocusState()


class _TextButtonHoverFocusState(State[_TextButtonHoverFocusDemo]):
    def initState(self):
        self.hovered = False
        self.focused = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                TextButton(
                    child=Text("Hover or focus me"),
                    onPressed=lambda: None,
                    onHover=lambda val: self.setState(
                        lambda: setattr(self, "hovered", val)
                    ),
                    onFocusChange=lambda val: self.setState(
                        lambda: setattr(self, "focused", val)
                    ),
                ),
                SizedBox(height=8),
                Text(
                    f"Hovered: {self.hovered}, Focused: {self.focused}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _OutlinedButtonHoverFocusDemo(StatefulWidget):
    def createState(self):
        return _OutlinedButtonHoverFocusState()


class _OutlinedButtonHoverFocusState(State[_OutlinedButtonHoverFocusDemo]):
    def initState(self):
        self.hovered = False
        self.focused = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                OutlinedButton(
                    child=Text("Hover or focus me"),
                    onPressed=lambda: None,
                    onHover=lambda val: self.setState(
                        lambda: setattr(self, "hovered", val)
                    ),
                    onFocusChange=lambda val: self.setState(
                        lambda: setattr(self, "focused", val)
                    ),
                ),
                SizedBox(height=8),
                Text(
                    f"Hovered: {self.hovered}, Focused: {self.focused}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _SwitchFocusNodeDemo(StatefulWidget):
    def createState(self):
        return _SwitchFocusNodeDemoState()


class _SwitchFocusNodeDemoState(State[_SwitchFocusNodeDemo]):
    def initState(self):
        self.value = False
        self.focus_node = FocusNode()

    def build(self, context):
        return Row(
            children=[
                Switch(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    focusNode=self.focus_node,
                    mouseCursor=SystemMouseCursors.grab,
                    focusColor=Colors.green,
                    hoverColor=Color(0xFFE8F5E9),
                ),
                SizedBox(width=12),
                Text(
                    f"Switch is {'ON' if self.value else 'OFF'}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _ChipAutoFocusDemo(StatefulWidget):
    def createState(self):
        return _ChipAutoFocusDemoState()


class _ChipAutoFocusDemoState(State[_ChipAutoFocusDemo]):
    def initState(self):
        self.focus_node = FocusNode()

    def build(self, context):
        return Row(
            children=[
                Chip(
                    label=Text("Auto-focused"),
                    autofocus=True,
                    focusNode=self.focus_node,
                    mouseCursor=SystemMouseCursors.click,
                    backgroundColor=Color(0xFFE3F2FD),
                ),
                SizedBox(width=12),
                Chip(
                    label=Text("Not focused"),
                    backgroundColor=Color(0xFFF5F5F5),
                ),
            ],
        )


class _FocusScopeNodeDemo(StatefulWidget):
    def createState(self):
        return _FocusScopeNodeDemoState()


class _FocusScopeNodeDemoState(State[_FocusScopeNodeDemo]):

    def initState(self):
        self.scope_node = FocusScopeNode()
        self.can_focus = True
        self.focus_log = []

    def _toggle_focusability(self):
        self.can_focus = not self.can_focus
        self.focus_log = self.focus_log + [
            f"descendantsAreFocusable = {self.can_focus}"
        ]
        self.setState(lambda: None)

    def _request_focus(self):
        self.scope_node.requestFocus()
        self.focus_log = self.focus_log + ["requestFocus() called on scope node"]
        self.setState(lambda: None)

    def _unfocus(self):
        self.scope_node.unfocus()
        self.focus_log = self.focus_log + ["unfocus() called on scope node"]
        self.setState(lambda: None)

    def build(self, context):
        log_widgets = []
        for entry in self.focus_log[-8:]:
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.blue if "True" in entry else Colors.orange,
                    ),
                ),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "Toggle focusability and try clicking the fields.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"descendantsAreFocusable: {self.can_focus}",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=8),
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Focusability"),
                            onPressed=self._toggle_focusability,
                        ),
                        ElevatedButton(
                            child=Text("Request Focus"),
                            onPressed=self._request_focus,
                        ),
                        ElevatedButton(
                            child=Text("Unfocus"),
                            onPressed=self._unfocus,
                        ),
                    ],
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    descendantsAreFocusable=self.can_focus,
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Container(
                                width=300.0,
                                child=TextField(
                                    focusNode=self.scope_node,
                                    decoration=InputDecoration(
                                        hintText="Field A (scope node attached)",
                                    ),
                                ),
                            ),
                            SizedBox(height=8),
                            Container(
                                width=300.0,
                                child=TextField(
                                    decoration=InputDecoration(
                                        hintText="Field B",
                                    ),
                                ),
                            ),
                            SizedBox(height=8),
                            Container(
                                width=300.0,
                                child=TextField(
                                    decoration=InputDecoration(
                                        hintText="Field C",
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Colors.black12,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=log_widgets,
                    ),
                ),
            ],
        )


class _TraversalEdgeBehaviorDemo(StatefulWidget):
    def createState(self):
        return _TraversalEdgeBehaviorDemoState()


class _TraversalEdgeBehaviorDemoState(State[_TraversalEdgeBehaviorDemo]):

    def initState(self):
        self.use_closed_loop = True
        self.tab_count = 0

    def _toggle_mode(self):
        self.use_closed_loop = not self.use_closed_loop
        self.tab_count = 0
        self.setState(lambda: None)

    def _on_tab(self):
        self.tab_count += 1
        self.setState(lambda: None)

    def build(self, context):
        mode_label = "closedLoop" if self.use_closed_loop else "stop"
        mode_color = Colors.green if self.use_closed_loop else Colors.red

        buttons = []
        for i in range(4):
            buttons.append(
                ElevatedButton(
                    child=Text(f"Button {i + 1}"),
                    onPressed=self._on_tab,
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Text("Mode: ", style=TextStyle(fontSize=13)),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=mode_color,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                mode_label,
                                style=TextStyle(color=Colors.white, fontSize=13),
                            ),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Text("Toggle Mode"),
                            onPressed=self._toggle_mode,
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"Tab presses: {self.tab_count}",
                    style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    policy=ReadingOrderTraversalPolicy(),
                    descendantsAreTraversable=True,
                    child=Wrap(
                        spacing=8,
                        runSpacing=8,
                        children=buttons,
                    ),
                ),
                SizedBox(height=12),
                Text(
                    "closedLoop: Tab wraps from last to first button.\n"
                    "stop: Tab stops at the last button and does not wrap.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            ],
        )


class _TraversalDirectionDemo(StatefulWidget):
    def createState(self):
        return _TraversalDirectionDemoState()


class _TraversalDirectionDemoState(State[_TraversalDirectionDemo]):

    def initState(self):
        self.focused_idx = -1
        self.last_direction = ""
        self.nodes = [FocusNode() for _ in range(9)]

    def dispose(self):
        for n in self.nodes:
            n.dispose()
        super().dispose()

    def _make_cell(self, idx, color):
        is_focused = self.focused_idx == idx

        def on_key(event):
            if isinstance(event, KeyDownEvent):
                key = event.logicalKey
                if key == LogicalKeyboardKey.arrowUp:
                    self.last_direction = "up"
                elif key == LogicalKeyboardKey.arrowDown:
                    self.last_direction = "down"
                elif key == LogicalKeyboardKey.arrowLeft:
                    self.last_direction = "left"
                elif key == LogicalKeyboardKey.arrowRight:
                    self.last_direction = "right"
                else:
                    return KeyEventResult.ignored
                self.setState(lambda: None)
            return KeyEventResult.ignored

        self.nodes[idx].onKeyEvent = on_key

        return SizedBox(
            width=70.0,
            height=50.0,
            child=ElevatedButton(
                focusNode=self.nodes[idx],
                onPressed=lambda i=idx: self.setState(
                    lambda: setattr(self, "focused_idx", i)
                ),
                child=Text(
                    str(idx + 1),
                    style=TextStyle(fontSize=16, fontWeight=FontWeight.bold),
                ),
            ),
        )

    def build(self, context):
        rows = []
        for r in range(3):
            cells = []
            for c in range(3):
                idx = r * 3 + c
                if c > 0:
                    cells.append(SizedBox(width=8))
                cells.append(self._make_cell(idx, None))
            rows.append(Row(children=cells))
            if r < 2:
                rows.append(SizedBox(height=8))

        direction_color = Colors.grey
        direction_arrow = ""
        if self.last_direction == "up":
            direction_color = Colors.blue
            direction_arrow = "\u2191"
        elif self.last_direction == "down":
            direction_color = Colors.green
            direction_arrow = "\u2193"
        elif self.last_direction == "left":
            direction_color = Colors.orange
            direction_arrow = "\u2190"
        elif self.last_direction == "right":
            direction_color = Colors.purple
            direction_arrow = "\u2192"

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    (
                        f"{direction_arrow} TraversalDirection.{self.last_direction}"
                        if self.last_direction
                        else "Click a cell, then use arrow keys"
                    ),
                    style=TextStyle(
                        fontSize=14, fontWeight=FontWeight.bold, color=direction_color
                    ),
                ),
                SizedBox(height=8),
                FocusTraversalGroup(
                    child=Column(children=rows),
                ),
            ],
        )


class _ReversedPolicy(FocusTraversalPolicy):
    def sortDescendants(self, descendants, currentNode):
        return list(reversed(descendants))


class _ScopeNodeParamsDemo(StatefulWidget):
    def createState(self):
        return _ScopeNodeParamsDemoState()


class _ScopeNodeParamsDemoState(State[_ScopeNodeParamsDemo]):

    def initState(self):
        self.skip_traversal = False
        self.can_request_focus = True
        self.scope_node = FocusScopeNode(
            debugLabel="demo-scope",
            skipTraversal=False,
            canRequestFocus=True,
        )
        self.status = "Ready"

    def _toggle_skip(self):
        self.skip_traversal = not self.skip_traversal
        self.scope_node = FocusScopeNode(
            debugLabel="demo-scope",
            skipTraversal=self.skip_traversal,
            canRequestFocus=self.can_request_focus,
        )
        self.status = f"skipTraversal = {self.skip_traversal}"
        self.setState(lambda: None)

    def _toggle_can_focus(self):
        self.can_request_focus = not self.can_request_focus
        self.scope_node = FocusScopeNode(
            debugLabel="demo-scope",
            skipTraversal=self.skip_traversal,
            canRequestFocus=self.can_request_focus,
        )
        self.status = f"canRequestFocus = {self.can_request_focus}"
        self.setState(lambda: None)

    def _try_request_focus(self):
        self.scope_node.requestFocus()
        if self.can_request_focus:
            self.status = "requestFocus() called successfully"
        else:
            self.status = "requestFocus() blocked (canRequestFocus=False)"
        self.setState(lambda: None)

    def build(self, context):
        skip_color = Colors.red if self.skip_traversal else Colors.green
        focus_color = Colors.green if self.can_request_focus else Colors.red
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "debugLabel: demo-scope",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                Row(
                    children=[
                        Text("skipTraversal: ", style=TextStyle(fontSize=13)),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=skip_color,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                str(self.skip_traversal),
                                style=TextStyle(color=Colors.white, fontSize=13),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=4),
                Row(
                    children=[
                        Text("canRequestFocus: ", style=TextStyle(fontSize=13)),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=focus_color,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                str(self.can_request_focus),
                                style=TextStyle(color=Colors.white, fontSize=13),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("Toggle skipTraversal"),
                            onPressed=self._toggle_skip,
                        ),
                        ElevatedButton(
                            child=Text("Toggle canRequestFocus"),
                            onPressed=self._toggle_can_focus,
                        ),
                        ElevatedButton(
                            child=Text("Request Focus"),
                            onPressed=self._try_request_focus,
                        ),
                    ],
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Container(
                                width=300.0,
                                child=TextField(
                                    focusNode=self.scope_node,
                                    decoration=InputDecoration(
                                        hintText="Field 1 (scope node)",
                                    ),
                                ),
                            ),
                            SizedBox(height=8),
                            Container(
                                width=300.0,
                                child=TextField(
                                    decoration=InputDecoration(
                                        hintText="Field 2",
                                    ),
                                ),
                            ),
                            SizedBox(height=8),
                            Container(
                                width=300.0,
                                child=TextField(
                                    decoration=InputDecoration(
                                        hintText="Field 3",
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                Container(
                    padding=EdgeInsets.all(8),
                    decoration=BoxDecoration(
                        color=Colors.black12,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Text(
                        self.status,
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    ),
                ),
            ],
        )


class _ScopeEdgeBehaviorDemo(StatefulWidget):
    def createState(self):
        return _ScopeEdgeBehaviorDemoState()


class _ScopeEdgeBehaviorDemoState(State[_ScopeEdgeBehaviorDemo]):

    def initState(self):
        self.use_closed_loop = True
        self.use_dir_closed_loop = False
        self.scope_node = FocusScopeNode(
            traversalEdgeBehavior=TraversalEdgeBehavior.closedLoop,
            directionalTraversalEdgeBehavior=TraversalEdgeBehavior.stop,
        )
        self.press_count = 0

    def _toggle_traversal(self):
        self.use_closed_loop = not self.use_closed_loop
        behavior = (
            TraversalEdgeBehavior.closedLoop
            if self.use_closed_loop
            else TraversalEdgeBehavior.stop
        )
        dir_behavior = (
            TraversalEdgeBehavior.closedLoop
            if self.use_dir_closed_loop
            else TraversalEdgeBehavior.stop
        )
        self.scope_node = FocusScopeNode(
            traversalEdgeBehavior=behavior,
            directionalTraversalEdgeBehavior=dir_behavior,
        )
        self.setState(lambda: None)

    def _toggle_directional(self):
        self.use_dir_closed_loop = not self.use_dir_closed_loop
        behavior = (
            TraversalEdgeBehavior.closedLoop
            if self.use_closed_loop
            else TraversalEdgeBehavior.stop
        )
        dir_behavior = (
            TraversalEdgeBehavior.closedLoop
            if self.use_dir_closed_loop
            else TraversalEdgeBehavior.stop
        )
        self.scope_node = FocusScopeNode(
            traversalEdgeBehavior=behavior,
            directionalTraversalEdgeBehavior=dir_behavior,
        )
        self.setState(lambda: None)

    def _on_button_press(self):
        self.press_count += 1
        self.setState(lambda: None)

    def build(self, context):
        edge_label = "closedLoop" if self.use_closed_loop else "stop"
        dir_label = "closedLoop" if self.use_dir_closed_loop else "stop"
        edge_color = Colors.green if self.use_closed_loop else Colors.red
        dir_color = Colors.green if self.use_dir_closed_loop else Colors.red

        buttons = []
        for i in range(3):
            buttons.append(
                ElevatedButton(
                    child=Text(f"Button {i + 1}"),
                    onPressed=self._on_button_press,
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Text("traversalEdgeBehavior: ", style=TextStyle(fontSize=13)),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=edge_color,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                edge_label,
                                style=TextStyle(color=Colors.white, fontSize=13),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=4),
                Row(
                    children=[
                        Text(
                            "directionalTraversalEdgeBehavior: ",
                            style=TextStyle(fontSize=13),
                        ),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=dir_color,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                dir_label,
                                style=TextStyle(color=Colors.white, fontSize=13),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"Button presses: {self.press_count}",
                    style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                ),
                SizedBox(height=8),
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Traversal Edge"),
                            onPressed=self._toggle_traversal,
                        ),
                        ElevatedButton(
                            child=Text("Toggle Directional Edge"),
                            onPressed=self._toggle_directional,
                        ),
                    ],
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    policy=ReadingOrderTraversalPolicy(),
                    child=Wrap(spacing=8, runSpacing=8, children=buttons),
                ),
                SizedBox(height=8),
                Text(
                    "closedLoop: Tab wraps from last to first.\n"
                    "stop: Tab stops at the last button.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            ],
        )


class _FocusNodeCreatedDemo(StatefulWidget):
    def createState(self):
        return _FocusNodeCreatedDemoState()


class _FocusNodeCreatedDemoState(State[_FocusNodeCreatedDemo]):

    def initState(self):
        self.visible_count = 0
        self.created_log = []

    def _on_focus_node_created(self, node):
        label = f"FocusNode #{len(self.created_log) + 1} created"
        self.created_log = self.created_log + [label]
        self.setState(lambda: None)

    def _add_button(self):
        if self.visible_count < 4:
            self.visible_count += 1
            self.setState(lambda: None)

    def _reset(self):
        self.visible_count = 0
        self.created_log = []
        self.setState(lambda: None)

    def build(self, context):
        button_widgets = []
        for i in range(4):
            button_widgets.append(
                Visibility(
                    visible=i < self.visible_count,
                    child=ElevatedButton(
                        child=Text(f"Button {i + 1}"),
                        onPressed=lambda: None,
                    ),
                ),
            )

        log_widgets = []
        for entry in self.created_log[-10:]:
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.green,
                    ),
                ),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "No nodes created yet.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Visible buttons: {self.visible_count} / 4",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=8),
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("Add Button"),
                            onPressed=self._add_button,
                        ),
                        ElevatedButton(
                            child=Text("Reset"),
                            onPressed=self._reset,
                        ),
                    ],
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    onFocusNodeCreated=self._on_focus_node_created,
                    child=Wrap(
                        spacing=8,
                        runSpacing=8,
                        children=button_widgets,
                    ),
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(8),
                    decoration=BoxDecoration(
                        color=Colors.black12,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=log_widgets,
                    ),
                ),
            ],
        )


class _OrderedSecondaryDemo(StatefulWidget):
    def createState(self):
        return _OrderedSecondaryDemoState()


class _OrderedSecondaryDemoState(State[_OrderedSecondaryDemo]):

    def initState(self):
        self.focused_label = "None"
        self.focus_order_log = []

    def _on_focus(self, label):
        self.focused_label = label
        self.focus_order_log = (self.focus_order_log + [label])[-10:]
        self.setState(lambda: None)

    def build(self, context):
        log_text = (
            " -> ".join(self.focus_order_log)
            if self.focus_order_log
            else "Tab through buttons to see order"
        )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Current focus: {self.focused_label}",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                Container(
                    padding=EdgeInsets.all(8),
                    decoration=BoxDecoration(
                        color=Colors.black12,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Text(
                        log_text,
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    ),
                ),
                SizedBox(height=12),
                FocusTraversalGroup(
                    policy=OrderedTraversalPolicy(
                        secondary=WidgetOrderTraversalPolicy(),
                    ),
                    child=Wrap(
                        spacing=8,
                        runSpacing=8,
                        children=[
                            FocusTraversalOrder(
                                order=NumericFocusOrder(3),
                                child=ElevatedButton(
                                    child=Text("A (order=3)"),
                                    onPressed=lambda: self._on_focus("A"),
                                ),
                            ),
                            ElevatedButton(
                                child=Text("B (no order)"),
                                onPressed=lambda: self._on_focus("B"),
                            ),
                            FocusTraversalOrder(
                                order=NumericFocusOrder(1),
                                child=ElevatedButton(
                                    child=Text("C (order=1)"),
                                    onPressed=lambda: self._on_focus("C"),
                                ),
                            ),
                            ElevatedButton(
                                child=Text("D (no order)"),
                                onPressed=lambda: self._on_focus("D"),
                            ),
                            FocusTraversalOrder(
                                order=NumericFocusOrder(2),
                                child=ElevatedButton(
                                    child=Text("E (order=2)"),
                                    onPressed=lambda: self._on_focus("E"),
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "Ordered: C(1) -> E(2) -> A(3), then unordered: B, D (widget order via secondary)",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            ],
        )


class FocusPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Focus & Traversal",
            description=(
                "Explores keyboard focus, key event handling, and traversal order "
                "so desktop-style interactions stay predictable across complex "
                "widget trees."
            ),
            children=[
                SplitViewTile(
                    title="FocusNode Key Events",
                    description=(
                        "FocusNode.onKeyEvent is a mutable property. You can swap "
                        "the handler at runtime, set it to None, or invoke it directly "
                        "from Python code without an actual keyboard event."
                    ),
                    instruction=(
                        "Click the text field then press any key — the event log "
                        "shows which handler processed it. Use the buttons to swap "
                        "between func_A / func_B, clear the handler, or call "
                        "onKeyEvent directly with a synthetic KeyDownEvent."
                    ),
                    visible=_FocusNodeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "focus_node = FocusNode(onKeyEvent=handle_key)\n"
                            "\n"
                            "def handle_key(event):\n"
                            "    if not isinstance(event, KeyDownEvent):\n"
                            "        return KeyEventResult.ignored\n"
                            "    label = event.logicalKey.keyLabel\n"
                            "    return KeyEventResult.handled\n"
                            "\n"
                            "focus_node.onKeyEvent = other_handler\n"
                            "focus_node.onKeyEvent = None\n"
                            "\n"
                            "cb = focus_node.onKeyEvent\n"
                            "if cb is not None:\n"
                            "    cb(KeyDownEvent(...))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconButton focusNode & autofocus",
                    description=(
                        "focusNode gives programmatic control over focus "
                        "(requestFocus / unfocus). autofocus=True requests "
                        "focus automatically on first build."
                    ),
                    instruction=(
                        "Click Request Focus to focus the first IconButton "
                        "(shows a focus ring). Click Unfocus to remove it. "
                        "The second button grabs focus automatically on mount."
                    ),
                    visible=_IconButtonFocusDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "node = FocusNode()\n"
                            "\n"
                            "IconButton(\n"
                            "    icon=Icon(Icons.center_focus_strong),\n"
                            "    focusNode=node,\n"
                            "    onPressed=on_tap,\n"
                            ")\n"
                            "\n"
                            "node.requestFocus()   # show focus ring\n"
                            "node.unfocus()         # remove it\n"
                            "\n"
                            "# autofocus grabs focus on first build:\n"
                            "IconButton(\n"
                            "    icon=Icon(Icons.auto_fix_high),\n"
                            "    autofocus=True,\n"
                            "    onPressed=on_tap,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Switch focusNode & mouseCursor",
                    description=(
                        "Switch with a FocusNode, mouseCursor=SystemMouseCursors.grab, green focusColor, "
                        "and green hoverColor."
                    ),
                    instruction="Hover or tab-focus the switch to see the green highlight.",
                    visible=_SwitchFocusNodeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Switch(\n"
                            "    value=False,\n"
                            "    onChanged=on_changed,\n"
                            "    focusNode=focus_node,\n"
                            "    mouseCursor=SystemMouseCursors.grab,\n"
                            "    focusColor=Colors.green,\n"
                            "    hoverColor=Color(0xFFE8F5E9),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Chip focusNode & autofocus",
                    description=(
                        "A Chip with autofocus=True and mouseCursor=SystemMouseCursors.click. "
                        "The first chip auto-focuses on load."
                    ),
                    instruction="The first chip should be focused when the page loads.",
                    visible=_ChipAutoFocusDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Chip(\n"
                            "    label=Text('Auto-focused'),\n"
                            "    autofocus=True,\n"
                            "    focusNode=focus_node,\n"
                            "    mouseCursor=SystemMouseCursors.click,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextButton onHover & onFocusChange",
                    description="Track hover and focus state changes with callback properties that receive a bool value.",
                    instruction="Hover over the button and tab to focus it. The text below updates in real time.",
                    visible=_TextButtonHoverFocusDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextButton(\n"
                            "    child=Text('Hover or focus me'),\n"
                            "    onPressed=on_tap,\n"
                            "    onHover=lambda val: set_hover(val),\n"
                            "    onFocusChange=lambda val: set_focus(val),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="OutlinedButton onHover & onFocusChange",
                    description="OutlinedButton also exposes onHover and onFocusChange callbacks for tracking interaction state.",
                    instruction="Hover over the button and tab to focus it. The text below shows real-time state.",
                    visible=_OutlinedButtonHoverFocusDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "OutlinedButton(\n"
                            "    child=Text('Hover or focus me'),\n"
                            "    onPressed=on_tap,\n"
                            "    onHover=lambda val: set_hover(val),\n"
                            "    onFocusChange=lambda val: set_focus(val),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Ordered Traversal",
                    description=(
                        "FocusTraversalGroup with OrderedTraversalPolicy assigns "
                        "an explicit numeric order to each child via "
                        "FocusTraversalOrder + NumericFocusOrder, overriding the "
                        "default widget-tree order."
                    ),
                    instruction=(
                        "Press Tab to move focus between the three fields. "
                        "Despite visual order 1-2-3, tab order is reversed: "
                        "Field 3 (order=1) -> Field 2 (order=2) -> Field 1 (order=3)."
                    ),
                    visible=FocusTraversalGroup(
                        policy=OrderedTraversalPolicy(),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                FocusTraversalOrder(
                                    order=NumericFocusOrder(3),
                                    child=Container(
                                        width=300.0,
                                        child=TextField(
                                            decoration=InputDecoration(
                                                hintText="Field 1 (order=3, last in tab)",
                                            ),
                                        ),
                                    ),
                                ),
                                SizedBox(height=8),
                                FocusTraversalOrder(
                                    order=NumericFocusOrder(2),
                                    child=Container(
                                        width=300.0,
                                        child=TextField(
                                            decoration=InputDecoration(
                                                hintText="Field 2 (order=2, middle)",
                                            ),
                                        ),
                                    ),
                                ),
                                SizedBox(height=8),
                                FocusTraversalOrder(
                                    order=NumericFocusOrder(1),
                                    child=Container(
                                        width=300.0,
                                        child=TextField(
                                            decoration=InputDecoration(
                                                hintText="Field 3 (order=1, first in tab)",
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "FocusTraversalGroup(\n"
                            "    policy=OrderedTraversalPolicy(),\n"
                            "    child=Column(children=[\n"
                            "        FocusTraversalOrder(\n"
                            "            order=NumericFocusOrder(3),\n"
                            "            child=TextField(hintText='Field 1'),\n"
                            "        ),\n"
                            "        FocusTraversalOrder(\n"
                            "            order=NumericFocusOrder(1),\n"
                            "            child=TextField(hintText='Field 3'),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Reading-Order Traversal",
                    description=(
                        "ReadingOrderTraversalPolicy is the default policy. "
                        "It traverses focusable children in reading order: "
                        "left to right, top to bottom."
                    ),
                    instruction=(
                        "Press Tab to move between the two side-by-side fields. "
                        "Focus moves from left to right as expected."
                    ),
                    visible=FocusTraversalGroup(
                        policy=ReadingOrderTraversalPolicy(),
                        child=Row(
                            children=[
                                Container(
                                    width=170.0,
                                    child=TextField(
                                        decoration=InputDecoration(
                                            hintText="Left field",
                                        ),
                                    ),
                                ),
                                SizedBox(width=12),
                                Container(
                                    width=170.0,
                                    child=TextField(
                                        decoration=InputDecoration(
                                            hintText="Right field",
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "FocusTraversalGroup(\n"
                            "    policy=ReadingOrderTraversalPolicy(),\n"
                            "    child=Row(children=[\n"
                            "        TextField(hintText='Left field'),\n"
                            "        TextField(hintText='Right field'),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Custom FocusTraversalPolicy",
                    description=(
                        "A Python subclass of FocusTraversalPolicy that reverses "
                        "the default traversal order by overriding sortDescendants. "
                        "Tab goes bottom to top instead of top to bottom."
                    ),
                    instruction=(
                        "Press Tab to cycle through Fields A, B, C. Because the "
                        "custom policy reverses the list, focus starts at Field C "
                        "(bottom) and moves upward to Field A (top)."
                    ),
                    visible=FocusTraversalGroup(
                        policy=_ReversedPolicy(),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Container(
                                    width=300.0,
                                    child=TextField(
                                        decoration=InputDecoration(
                                            hintText="Field A (last in reversed tab)",
                                        ),
                                    ),
                                ),
                                SizedBox(height=8),
                                Container(
                                    width=300.0,
                                    child=TextField(
                                        decoration=InputDecoration(
                                            hintText="Field B",
                                        ),
                                    ),
                                ),
                                SizedBox(height=8),
                                Container(
                                    width=300.0,
                                    child=TextField(
                                        decoration=InputDecoration(
                                            hintText="Field C (first in reversed tab)",
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class ReversedPolicy(FocusTraversalPolicy):\n"
                            "    def sortDescendants(self, descendants, currentNode):\n"
                            "        return list(reversed(descendants))\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    policy=ReversedPolicy(),\n"
                            "    child=Column(children=[\n"
                            "        TextField(hintText='Field A'),\n"
                            "        TextField(hintText='Field B'),\n"
                            "        TextField(hintText='Field C'),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FocusScopeNode",
                    description=(
                        "FocusScopeNode extends FocusNode and groups focusable children. "
                        "Combined with FocusTraversalGroup's descendantsAreFocusable, you "
                        "can toggle whether children can receive focus at all."
                    ),
                    instruction=(
                        "Click Toggle Focusability to block or allow focus on the three "
                        "text fields. Use Request Focus to focus the scope node's field, "
                        "and Unfocus to clear it."
                    ),
                    visible=_FocusScopeNodeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "scope_node = FocusScopeNode()\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    descendantsAreFocusable=can_focus,\n"
                            "    child=Column(children=[\n"
                            "        TextField(focusNode=scope_node),\n"
                            "        TextField(),\n"
                            "    ]),\n"
                            ")\n"
                            "\n"
                            "scope_node.requestFocus()\n"
                            "scope_node.unfocus()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TraversalEdgeBehavior",
                    description=(
                        "TraversalEdgeBehavior controls what happens when focus "
                        "traversal reaches the edge of a group. closedLoop wraps "
                        "around, stop halts at the boundary."
                    ),
                    instruction=(
                        "Toggle between closedLoop and stop modes. "
                        "Tab through the buttons — in closedLoop, focus wraps from last to first. "
                        "Note: TraversalEdgeBehavior param on FocusScopeNode is not yet wired."
                    ),
                    visible=_TraversalEdgeBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TraversalEdgeBehavior.closedLoop\n"
                            "TraversalEdgeBehavior.stop\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    policy=ReadingOrderTraversalPolicy(),\n"
                            "    child=Row(children=[\n"
                            "        ElevatedButton(child=Text('Btn 1')),\n"
                            "        ElevatedButton(child=Text('Btn 2')),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TraversalDirection",
                    description=(
                        "TraversalDirection represents the direction of focus movement. "
                        "Arrow keys inside a FocusTraversalGroup move focus between "
                        "widgets in the corresponding direction: up, down, left, right."
                    ),
                    instruction=(
                        "Click any numbered cell to focus it, then press arrow keys. "
                        "The display shows which direction key was pressed. "
                        "Note: Focus widget not yet available — visual focus highlight is manual."
                    ),
                    visible=_TraversalDirectionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "node = FocusNode()\n\n"
                            "def on_key(event):\n"
                            "    if isinstance(event, KeyDownEvent):\n"
                            "        if event.logicalKey == LogicalKeyboardKey.arrowUp:\n"
                            "            direction = TraversalDirection.up\n"
                            "    return KeyEventResult.ignored\n\n"
                            "node.onKeyEvent = on_key\n\n"
                            "FocusTraversalGroup(\n"
                            "    child=grid_of_focusable_widgets,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FocusScopeNode Constructor Params",
                    description=(
                        "FocusScopeNode accepts debugLabel, skipTraversal, and "
                        "canRequestFocus constructor parameters. skipTraversal "
                        "excludes the scope from Tab traversal. canRequestFocus "
                        "controls whether requestFocus() is allowed."
                    ),
                    instruction=(
                        "Toggle skipTraversal and canRequestFocus with the buttons. "
                        "When skipTraversal is True, Tab skips the scope fields. "
                        "When canRequestFocus is False, Request Focus has no effect."
                    ),
                    visible=_ScopeNodeParamsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "scope = FocusScopeNode(\n"
                            "    debugLabel='demo-scope',\n"
                            "    skipTraversal=False,\n"
                            "    canRequestFocus=True,\n"
                            ")\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    child=Column(children=[\n"
                            "        TextField(focusNode=scope),\n"
                            "        TextField(),\n"
                            "        TextField(),\n"
                            "    ]),\n"
                            ")\n"
                            "\n"
                            "scope.requestFocus()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FocusScopeNode traversalEdgeBehavior",
                    description=(
                        "FocusScopeNode supports traversalEdgeBehavior and "
                        "directionalTraversalEdgeBehavior to control what happens "
                        "when Tab or arrow keys reach the edge of the scope."
                    ),
                    instruction=(
                        "Toggle between closedLoop and stop for both traversal "
                        "and directional edge behaviors. Tab through the buttons "
                        "to see wrapping vs stopping at the last button."
                    ),
                    visible=_ScopeEdgeBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "scope = FocusScopeNode(\n"
                            "    traversalEdgeBehavior=\n"
                            "        TraversalEdgeBehavior.closedLoop,\n"
                            "    directionalTraversalEdgeBehavior=\n"
                            "        TraversalEdgeBehavior.stop,\n"
                            ")\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    policy=ReadingOrderTraversalPolicy(),\n"
                            "    child=Wrap(children=[\n"
                            "        ElevatedButton(child=Text('Btn 1')),\n"
                            "        ElevatedButton(child=Text('Btn 2')),\n"
                            "        ElevatedButton(child=Text('Btn 3')),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FocusTraversalGroup onFocusNodeCreated",
                    description=(
                        "FocusTraversalGroup accepts an onFocusNodeCreated callback "
                        "that fires each time a new FocusNode is created within the "
                        "group. Useful for tracking or configuring nodes dynamically."
                    ),
                    instruction=(
                        "Click Add Button to reveal buttons one at a time. Each "
                        "new button triggers onFocusNodeCreated, and the log below "
                        "grows. Click Reset to start over."
                    ),
                    visible=_FocusNodeCreatedDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "def on_node_created(node):\n"
                            "    print(f'Created: {node}')\n"
                            "\n"
                            "FocusTraversalGroup(\n"
                            "    onFocusNodeCreated=on_node_created,\n"
                            "    child=Wrap(children=[\n"
                            "        Visibility(\n"
                            "            visible=show_btn,\n"
                            "            child=ElevatedButton(...),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="OrderedTraversalPolicy secondary",
                    description=(
                        "OrderedTraversalPolicy accepts a secondary policy used for "
                        "children without an explicit FocusOrder. Children with "
                        "NumericFocusOrder are sorted first, then unordered children "
                        "fall back to the secondary policy (e.g. WidgetOrderTraversalPolicy)."
                    ),
                    instruction=(
                        "Tab through the 5 buttons. Buttons A, C, E have numeric "
                        "orders (3, 1, 2) so they tab as C -> E -> A. Buttons B and D "
                        "have no order and follow widget creation order via the secondary policy."
                    ),
                    visible=_OrderedSecondaryDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "FocusTraversalGroup(\n"
                            "    policy=OrderedTraversalPolicy(\n"
                            "        secondary=WidgetOrderTraversalPolicy(),\n"
                            "    ),\n"
                            "    child=Wrap(children=[\n"
                            "        FocusTraversalOrder(\n"
                            "            order=NumericFocusOrder(3),\n"
                            "            child=ElevatedButton(child=Text('A')),\n"
                            "        ),\n"
                            "        ElevatedButton(child=Text('B')),\n"
                            "        FocusTraversalOrder(\n"
                            "            order=NumericFocusOrder(1),\n"
                            "            child=ElevatedButton(child=Text('C')),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
