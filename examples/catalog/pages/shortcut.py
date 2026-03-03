from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Builder,
    Intent,
    CallbackAction,
    Actions,
    ActionDispatcher,
    Shortcuts,
    CallbackShortcuts,
    SingleActivator,
    LockState,
    FocusNode,
    KeyEventResult,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    TextField,
    InputDecoration,
    InputBorder,
    ElevatedButton,
    Colors,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    TextStyle,
    BoxDecoration,
    BorderRadius,
    EdgeInsets,
)
from flut.flutter.services.keyboard_key import LogicalKeyboardKey
from flut.flutter.services import (
    KeyEvent,
    KeyDownEvent,
    KeyUpEvent,
    KeyRepeatEvent,
    PhysicalKeyboardKey,
)
from flut.dart import Color
from utils import CODE_FONT_FAMILY

from widgets import CatalogPage, SplitViewTile, CodeArea


class IncrementIntent(Intent):
    def __init__(self, amount=1):
        super().__init__()
        self.amount = amount


class DecrementIntent(Intent):
    def __init__(self, amount=1):
        super().__init__()
        self.amount = amount


class ResetIntent(Intent):
    pass


class _CounterMixin:
    def _init_counter(self):
        self.counter = 0
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-8:]

    def _increment(self, intent=None):
        amount = getattr(intent, "amount", 1) if intent else 1

        def _update():
            self.counter += amount
            self._add_log(f"Increment({amount}) \u2192 {self.counter}")

        self.setState(_update)

    def _decrement(self, intent=None):
        amount = getattr(intent, "amount", 1) if intent else 1

        def _update():
            self.counter -= amount
            self._add_log(f"Decrement({amount}) \u2192 {self.counter}")

        self.setState(_update)

    def _reset(self, intent=None):
        def _update():
            self.counter = 0
            self._add_log("Reset \u2192 0")

        self.setState(_update)


class _CallbackShortcutsDemo(StatefulWidget):
    def createState(self):
        return _CallbackShortcutsDemoState()


class _CallbackShortcutsDemoState(_CounterMixin, State["_CallbackShortcutsDemo"]):
    def initState(self):
        self._init_counter()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Counter: {self.counter}",
                    style=TextStyle(fontSize=24, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=12),
                CallbackShortcuts(
                    bindings={
                        SingleActivator(
                            LogicalKeyboardKey.arrowUp, control=True
                        ): self._increment,
                        SingleActivator(
                            LogicalKeyboardKey.arrowDown, control=True
                        ): self._decrement,
                    },
                    child=TextField(
                        decoration=InputDecoration(
                            hintText="Click here and press Ctrl+Up/Down",
                        ),
                    ),
                ),
                SizedBox(height=8),
                *[Text(f"  {line}") for line in self.log_lines],
            ],
        )


class _IntentShortcutsDemo(StatefulWidget):
    def createState(self):
        return _IntentShortcutsDemoState()


class _IntentShortcutsDemoState(_CounterMixin, State["_IntentShortcutsDemo"]):
    def initState(self):
        self._init_counter()

    def build(self, context):
        return Shortcuts(
            shortcuts={
                SingleActivator(LogicalKeyboardKey.keyI): IncrementIntent(),
                SingleActivator(LogicalKeyboardKey.keyD): DecrementIntent(),
                SingleActivator(LogicalKeyboardKey.keyR): ResetIntent(),
            },
            child=Actions(
                actions={
                    IncrementIntent: CallbackAction(onInvoke=self._increment),
                    DecrementIntent: CallbackAction(onInvoke=self._decrement),
                    ResetIntent: CallbackAction(onInvoke=self._reset),
                },
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            f"Counter: {self.counter}",
                            style=TextStyle(fontSize=24, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=12),
                        TextField(
                            decoration=InputDecoration(
                                hintText="Click here and press I / D / R",
                            ),
                        ),
                        SizedBox(height=8),
                        *[Text(f"  {line}") for line in self.log_lines],
                    ],
                ),
            ),
        )


class _IntentDataDemo(StatefulWidget):
    def createState(self):
        return _IntentDataDemoState()


class _IntentDataDemoState(_CounterMixin, State["_IntentDataDemo"]):
    def initState(self):
        self._init_counter()

    def build(self, context):
        return Shortcuts(
            shortcuts={
                SingleActivator(LogicalKeyboardKey.arrowUp): IncrementIntent(amount=5),
                SingleActivator(LogicalKeyboardKey.arrowDown): DecrementIntent(
                    amount=5
                ),
                SingleActivator(
                    LogicalKeyboardKey.arrowUp, shift=True
                ): IncrementIntent(amount=10),
                SingleActivator(
                    LogicalKeyboardKey.arrowDown, shift=True
                ): DecrementIntent(amount=10),
            },
            child=Actions(
                actions={
                    IncrementIntent: CallbackAction(onInvoke=self._increment),
                    DecrementIntent: CallbackAction(onInvoke=self._decrement),
                },
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            f"Counter: {self.counter}",
                            style=TextStyle(fontSize=24, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=12),
                        TextField(
                            decoration=InputDecoration(
                                hintText="Click here and press Up/Down or Shift+Up/Down",
                            ),
                        ),
                        SizedBox(height=8),
                        Text("Log:"),
                        *[Text(f"  {line}") for line in self.log_lines],
                    ],
                ),
            ),
        )


class _NestedActionsDemo(StatefulWidget):
    def createState(self):
        return _NestedActionsDemoState()


class _NestedActionsDemoState(_CounterMixin, State["_NestedActionsDemo"]):
    def initState(self):
        self._init_counter()

    def build(self, context):
        return Shortcuts(
            shortcuts={
                SingleActivator(LogicalKeyboardKey.keyI): IncrementIntent(),
                SingleActivator(LogicalKeyboardKey.keyD): DecrementIntent(),
            },
            child=Actions(
                actions={
                    DecrementIntent: CallbackAction(onInvoke=self._decrement),
                },
                child=Actions(
                    actions={
                        IncrementIntent: CallbackAction(onInvoke=self._increment),
                    },
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                f"Counter: {self.counter}",
                                style=TextStyle(
                                    fontSize=24, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=12),
                            TextField(
                                decoration=InputDecoration(
                                    hintText="Click here and press I / D",
                                ),
                            ),
                            SizedBox(height=8),
                            Text("Log:"),
                            *[Text(f"  {line}") for line in self.log_lines],
                        ],
                    ),
                ),
            ),
        )


class _NumLockIntent(Intent):
    def __init__(self, key_name, lock_mode):
        super().__init__()
        self.key_name = key_name
        self.lock_mode = lock_mode


class _NumLockDemo(StatefulWidget):
    def createState(self):
        return _NumLockDemoState()


class _NumLockDemoState(State["_NumLockDemo"]):
    def initState(self):
        self.log_lines = []

    def _on_shortcut(self, intent):
        def _update():
            entry = f"{intent.key_name} fired (numLock={intent.lock_mode})"
            self.log_lines = (self.log_lines + [entry])[-8:]

        self.setState(_update)

    def build(self, context):
        return Shortcuts(
            shortcuts={
                SingleActivator(
                    LogicalKeyboardKey.keyA, numLock=LockState.ignored
                ): _NumLockIntent("A", "ignored"),
                SingleActivator(
                    LogicalKeyboardKey.keyB, numLock=LockState.locked
                ): _NumLockIntent("B", "locked"),
                SingleActivator(
                    LogicalKeyboardKey.keyC, numLock=LockState.unlocked
                ): _NumLockIntent("C", "unlocked"),
            },
            child=Actions(
                actions={
                    _NumLockIntent: CallbackAction(onInvoke=self._on_shortcut),
                },
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        TextField(
                            decoration=InputDecoration(
                                hintText="Click here, then press A / B / C",
                            ),
                        ),
                        SizedBox(height=8),
                        Text(
                            "A = ignored (always fires) | "
                            "B = locked (fires only when NumLock ON) | "
                            "C = unlocked (fires only when NumLock OFF)",
                            style=TextStyle(fontSize=12),
                        ),
                        SizedBox(height=4),
                        Text(
                            "Toggle NumLock on your keyboard to test B vs C.",
                            style=TextStyle(fontSize=12),
                        ),
                        SizedBox(height=8),
                        Text("Log:"),
                        *[Text(f"  {line}") for line in self.log_lines],
                    ],
                ),
            ),
        )


class _SaveIntent(Intent):
    pass


class _IncludeSemanticsDemo(StatefulWidget):
    def createState(self):
        return _IncludeSemanticsDemoState()


class _IncludeSemanticsDemoState(State["_IncludeSemanticsDemo"]):
    def initState(self):
        self.counter_with = 0
        self.counter_without = 0

    def _increment_with(self, intent):
        def _update():
            self.counter_with += 1

        self.setState(_update)

    def _increment_without(self, intent):
        def _update():
            self.counter_without += 1

        self.setState(_update)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "includeSemantics=True (default)",
                    style=TextStyle(fontWeight=FontWeight.bold),
                ),
                Shortcuts(
                    includeSemantics=True,
                    shortcuts={
                        SingleActivator(
                            LogicalKeyboardKey.keyS, control=True
                        ): _SaveIntent(),
                    },
                    child=Actions(
                        actions={
                            _SaveIntent: CallbackAction(onInvoke=self._increment_with),
                        },
                        child=TextField(
                            decoration=InputDecoration(
                                hintText=f"Ctrl+S count: {self.counter_with}",
                            ),
                        ),
                    ),
                ),
                SizedBox(height=16),
                Text(
                    "includeSemantics=False",
                    style=TextStyle(fontWeight=FontWeight.bold),
                ),
                Shortcuts(
                    includeSemantics=False,
                    shortcuts={
                        SingleActivator(
                            LogicalKeyboardKey.keyS, control=True
                        ): _SaveIntent(),
                    },
                    child=Actions(
                        actions={
                            _SaveIntent: CallbackAction(
                                onInvoke=self._increment_without
                            ),
                        },
                        child=TextField(
                            decoration=InputDecoration(
                                hintText=f"Ctrl+S count: {self.counter_without}",
                            ),
                        ),
                    ),
                ),
            ],
        )


class _DispatchLogIntent(Intent):
    pass


class _LoggingDispatcher(ActionDispatcher):
    def __init__(self, on_log):
        super().__init__()
        self._on_log = on_log

    def invokeAction(self, action, intent, context=None):
        self._on_log(type(intent).__name__)
        return super().invokeAction(action, intent, context)


class _ActionDispatcherDemo(StatefulWidget):
    def createState(self):
        return _ActionDispatcherDemoState()


class _ActionDispatcherDemoState(State["_ActionDispatcherDemo"]):
    def initState(self):
        self.dispatch_log = []
        self.counter = 0
        self._dispatcher = _LoggingDispatcher(on_log=self._add_log)

    def _add_log(self, intent_name):
        def _update():
            self.counter += 1
            entry = f"Dispatched: {intent_name} (#{self.counter})"
            self.dispatch_log = (self.dispatch_log + [entry])[-8:]

        self.setState(_update)

    def _on_invoke(self, intent):
        pass

    def build(self, context):
        return Actions(
            dispatcher=self._dispatcher,
            actions={
                _DispatchLogIntent: CallbackAction(onInvoke=self._on_invoke),
            },
            child=Builder(
                builder=lambda ctx: Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        ElevatedButton(
                            onPressed=lambda: Actions.invoke(ctx, _DispatchLogIntent()),
                            child=Text("Dispatch _DispatchLogIntent"),
                        ),
                        SizedBox(height=8),
                        Text(
                            f"Total dispatches: {self.counter}",
                            style=TextStyle(fontSize=18, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=8),
                        Text("Dispatch log:"),
                        *[Text(f"  {line}") for line in self.dispatch_log],
                    ],
                ),
            ),
        )


class _KeyEventsDemo(StatefulWidget):
    def createState(self):
        return _KeyEventsDemoState()


class _KeyEventsDemoState(State[_KeyEventsDemo]):
    def initState(self):
        self.key_events = []
        self.focus_node = FocusNode(onKeyEvent=self._on_key_event)

    def _on_key_event(self, event: KeyEvent):
        event_type = type(event).__name__
        logical = event.logicalKey.keyLabel
        physical = f"0x{event.physicalKey.usbHidUsage:08X}"
        info = f"{event_type}: {logical} (physical={physical})"
        if isinstance(event, (KeyDownEvent, KeyRepeatEvent)) and event.character:
            info += f" char='{event.character}'"
        self.key_events = (self.key_events + [info])[-6:]
        self.setState(lambda: None)
        return KeyEventResult.ignored

    def build(self, context):
        key_log_widgets = []
        for ev in self.key_events:
            color = Colors.grey
            if "KeyDownEvent" in ev:
                color = Colors.blue
            elif "KeyUpEvent" in ev:
                color = Colors.green
            elif "KeyRepeatEvent" in ev:
                color = Colors.orange
            key_log_widgets.append(
                Text(
                    ev,
                    style=TextStyle(
                        fontSize=11, fontFamily=CODE_FONT_FAMILY, color=color
                    ),
                ),
            )
        if not key_log_widgets:
            key_log_widgets.append(
                Text(
                    "Click the text field and press keys to see events.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=400.0,
                    child=TextField(
                        focusNode=self.focus_node,
                        decoration=InputDecoration(
                            hintText="Type here to generate key events...",
                            border=InputBorder.none,
                            filled=True,
                            fillColor=Color(0xFFF5F5F5),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Container(
                    width=500.0,
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=key_log_widgets,
                    ),
                ),
            ],
        )


class ShortcutsPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Shortcuts & Actions",
            description=(
                "Demonstrates keyboard command handling, from simple key bindings "
                "to intent-driven actions that can be scoped, overridden, and "
                "routed through focused widgets."
            ),
            children=[
                SplitViewTile(
                    title="CallbackShortcuts",
                    description=(
                        "Maps key combinations directly to void callbacks. "
                        "The simplest way to add keyboard shortcuts to a focusable widget."
                    ),
                    instruction="Click the text field to focus it, then press Ctrl+Up to increment or Ctrl+Down to decrement.",
                    visible=_CallbackShortcutsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CallbackShortcuts(\n"
                            "    bindings={\n"
                            "        SingleActivator(\n"
                            "            LogicalKeyboardKey.arrowUp, control=True\n"
                            "        ): on_increment,\n"
                            "        SingleActivator(\n"
                            "            LogicalKeyboardKey.arrowDown, control=True\n"
                            "        ): on_decrement,\n"
                            "    },\n"
                            "    child=TextField(),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Shortcuts + Actions (Intent dispatch)",
                    description=(
                        "Separates key bindings from behaviour. Shortcuts maps keys to Intent objects, "
                        "Actions maps Intent types to CallbackAction handlers. This decoupling lets "
                        "different parts of the tree override how an Intent is handled."
                    ),
                    instruction="Click the text field, then press I to increment, D to decrement, or R to reset.",
                    visible=_IntentShortcutsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Shortcuts(\n"
                            "    shortcuts={\n"
                            "        SingleActivator(LogicalKeyboardKey.keyI): IncrementIntent(),\n"
                            "        SingleActivator(LogicalKeyboardKey.keyD): DecrementIntent(),\n"
                            "        SingleActivator(LogicalKeyboardKey.keyR): ResetIntent(),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={\n"
                            "            IncrementIntent: CallbackAction(onInvoke=on_increment),\n"
                            "            DecrementIntent: CallbackAction(onInvoke=on_decrement),\n"
                            "            ResetIntent: CallbackAction(onInvoke=on_reset),\n"
                            "        },\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Intent with data fields",
                    description=(
                        "Intents can carry data fields (e.g. amount) that the Action callback "
                        "receives via the intent parameter in onInvoke. This lets a single Action "
                        "handle multiple key bindings with different parameters."
                    ),
                    instruction="Click the text field, then press Up/Down for \u00b15, or Shift+Up/Down for \u00b110.",
                    visible=_IntentDataDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class IncrementIntent(Intent):\n"
                            "    def __init__(self, amount=1):\n"
                            "        super().__init__()\n"
                            "        self.amount = amount\n"
                            "\n"
                            "Shortcuts(\n"
                            "    shortcuts={\n"
                            "        SingleActivator(LogicalKeyboardKey.arrowUp): IncrementIntent(amount=5),\n"
                            "        SingleActivator(LogicalKeyboardKey.arrowUp, shift=True): IncrementIntent(amount=10),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={\n"
                            "            IncrementIntent: CallbackAction(\n"
                            "                onInvoke=lambda intent: increment(intent.amount)\n"
                            "            ),\n"
                            "        },\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Nested Actions",
                    description=(
                        "When Actions widgets are nested, the innermost one that handles a given "
                        "Intent type wins. Unhandled intents bubble up to outer Actions widgets. "
                        "This enables local overrides of global shortcuts."
                    ),
                    instruction="Click the text field, then press I (handled by inner Actions) or D (handled by outer Actions).",
                    visible=_NestedActionsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Actions(\n"
                            "    actions={\n"
                            "        DecrementIntent: CallbackAction(onInvoke=on_decrement),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={\n"
                            "            IncrementIntent: CallbackAction(onInvoke=on_increment),\n"
                            "        },\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SingleActivator numLock",
                    description=(
                        "SingleActivator supports a numLock parameter with LockState values: "
                        "ignored (fires regardless), locked (only when NumLock is on), "
                        "and unlocked (only when NumLock is off)."
                    ),
                    instruction="Click the text field, then press A (always works), B (only with NumLock on), or C (only with NumLock off).",
                    visible=_NumLockDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Shortcuts(\n"
                            "    shortcuts={\n"
                            "        SingleActivator(\n"
                            "            LogicalKeyboardKey.keyA,\n"
                            "            numLock=LockState.ignored,\n"
                            "        ): MyIntent('A'),\n"
                            "        SingleActivator(\n"
                            "            LogicalKeyboardKey.keyB,\n"
                            "            numLock=LockState.locked,\n"
                            "        ): MyIntent('B'),\n"
                            "        SingleActivator(\n"
                            "            LogicalKeyboardKey.keyC,\n"
                            "            numLock=LockState.unlocked,\n"
                            "        ): MyIntent('C'),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={MyIntent: CallbackAction(onInvoke=handler)},\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Shortcuts includeSemantics",
                    description=(
                        "The includeSemantics parameter controls whether Shortcuts adds "
                        "accessibility labels for its key bindings. True (default) annotates "
                        "the semantics tree; False suppresses accessibility info."
                    ),
                    instruction="Click each text field then press Ctrl+S. Both respond, but only the first adds semantic annotations.",
                    visible=_IncludeSemanticsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Shortcuts(\n"
                            "    includeSemantics=True,\n"
                            "    shortcuts={\n"
                            "        SingleActivator(LogicalKeyboardKey.keyS, control=True): SaveIntent(),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={SaveIntent: CallbackAction(onInvoke=on_save)},\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")\n"
                            "\n"
                            "Shortcuts(\n"
                            "    includeSemantics=False,\n"
                            "    shortcuts={\n"
                            "        SingleActivator(LogicalKeyboardKey.keyS, control=True): SaveIntent(),\n"
                            "    },\n"
                            "    child=Actions(\n"
                            "        actions={SaveIntent: CallbackAction(onInvoke=on_save)},\n"
                            "        child=TextField(),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Actions dispatcher",
                    description=(
                        "ActionDispatcher intercepts every action dispatch. Subclass it to add "
                        "logging, analytics, or custom pre/post processing. Pass the dispatcher "
                        "to Actions(dispatcher=...) to activate it."
                    ),
                    instruction="Press the button to dispatch an intent. Each press is logged by the custom ActionDispatcher.",
                    visible=_ActionDispatcherDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class LoggingDispatcher(ActionDispatcher):\n"
                            "    def __init__(self, on_log):\n"
                            "        super().__init__()\n"
                            "        self._on_log = on_log\n"
                            "\n"
                            "    def invokeAction(self, action, intent, context=None):\n"
                            "        self._on_log(type(intent).__name__)\n"
                            "        return super().invokeAction(action, intent, context)\n"
                            "\n"
                            "Actions(\n"
                            "    dispatcher=LoggingDispatcher(on_log=add_to_log),\n"
                            "    actions={\n"
                            "        MyIntent: CallbackAction(onInvoke=handler),\n"
                            "    },\n"
                            "    child=ElevatedButton(\n"
                            "        onPressed=lambda: Actions.invoke(context, MyIntent()),\n"
                            "        child=Text('Dispatch'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Key Events",
                    description=(
                        "FocusNode.onKeyEvent receives KeyDownEvent, KeyUpEvent, and KeyRepeatEvent "
                        "with logicalKey labels and physicalKey USB HID codes."
                    ),
                    instruction="Click the text field and press keys to see color-coded events logged below.",
                    visible=_KeyEventsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "focus_node = FocusNode(onKeyEvent=on_key)\n\n"
                            "def on_key(event):\n"
                            "    label = event.logicalKey.keyLabel\n"
                            "    hid = event.physicalKey.usbHidUsage\n"
                            "    return KeyEventResult.ignored"
                        ),
                    ),
                ),
            ],
        )
