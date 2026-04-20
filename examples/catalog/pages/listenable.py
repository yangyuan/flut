from flut.flutter.foundation import (
    ChangeNotifier,
    Listenable,
    ValueNotifier,
)
from flut.flutter.widgets import (
    StatelessWidget,
    StatefulWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Icon,
    ListenableBuilder,
    ValueListenableBuilder,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.material import Colors, ElevatedButton, IconButton, Icons
from flut.flutter.painting import TextStyle
from flut.dart.ui import FontWeight

from widgets import CatalogPage, SplitViewTile, CodeArea


class Counter(ChangeNotifier):
    def __init__(self, initial: int = 0):
        super().__init__()
        self._value = initial

    @property
    def value(self) -> int:
        return self._value

    def increment(self):
        self._value += 1
        self.notifyListeners()

    def decrement(self):
        self._value -= 1
        self.notifyListeners()

    def reset(self):
        if self._value != 0:
            self._value = 0
            self.notifyListeners()


class _CounterDemo(StatefulWidget):
    def createState(self):
        return _CounterDemoState()


class _CounterDemoState(State[_CounterDemo]):
    def initState(self):
        self.counter = Counter()

    def dispose(self):
        self.counter.dispose()

    def build(self, context):
        return ListenableBuilder(
            listenable=self.counter,
            builder=lambda context, _: Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        f"value = {self.counter.value}",
                        style=TextStyle(fontSize=20, fontWeight=FontWeight.bold),
                    ),
                    SizedBox(height=12),
                    Row(
                        mainAxisAlignment=MainAxisAlignment.start,
                        children=[
                            ElevatedButton(
                                onPressed=self.counter.decrement,
                                child=Text("−"),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                onPressed=self.counter.increment,
                                child=Text("+"),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                onPressed=self.counter.reset,
                                child=Text("reset"),
                            ),
                        ],
                    ),
                ],
            ),
        )


class _SharedCounterDemo(StatefulWidget):
    def createState(self):
        return _SharedCounterDemoState()


class _SharedCounterDemoState(State[_SharedCounterDemo]):
    def initState(self):
        self.counter = Counter(initial=10)

    def dispose(self):
        self.counter.dispose()

    def _badge(self, label, color):
        return ListenableBuilder(
            listenable=self.counter,
            builder=lambda context, _: Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(label, style=TextStyle(color=Colors.grey)),
                    Text(
                        str(self.counter.value),
                        style=TextStyle(
                            fontSize=24,
                            fontWeight=FontWeight.bold,
                            color=color,
                        ),
                    ),
                ],
            ),
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        self._badge("View A", Colors.indigo),
                        SizedBox(width=32),
                        self._badge("View B", Colors.deepOrange),
                    ],
                ),
                SizedBox(height=16),
                Row(
                    children=[
                        IconButton(
                            icon=Icon(Icons.remove),
                            onPressed=self.counter.decrement,
                        ),
                        IconButton(
                            icon=Icon(Icons.add),
                            onPressed=self.counter.increment,
                        ),
                    ],
                ),
            ],
        )


class _MergedListenableDemo(StatefulWidget):
    def createState(self):
        return _MergedListenableDemoState()


class _MergedListenableDemoState(State[_MergedListenableDemo]):
    def initState(self):
        self.left = Counter()
        self.right = Counter()
        self.merged = Listenable.merge([self.left, self.right])

    def dispose(self):
        self.left.dispose()
        self.right.dispose()

    def build(self, context):
        return ListenableBuilder(
            listenable=self.merged,
            builder=lambda context, _: Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        f"sum = {self.left.value + self.right.value}",
                        style=TextStyle(fontSize=20, fontWeight=FontWeight.bold),
                    ),
                    SizedBox(height=12),
                    Row(
                        children=[
                            Text(f"left = {self.left.value}"),
                            SizedBox(width=8),
                            IconButton(
                                icon=Icon(Icons.add),
                                onPressed=self.left.increment,
                            ),
                            SizedBox(width=24),
                            Text(f"right = {self.right.value}"),
                            SizedBox(width=8),
                            IconButton(
                                icon=Icon(Icons.add),
                                onPressed=self.right.increment,
                            ),
                        ],
                    ),
                ],
            ),
        )


class _ValueNotifierDemo(StatefulWidget):
    def createState(self):
        return _ValueNotifierDemoState()


class _ValueNotifierDemoState(State[_ValueNotifierDemo]):
    def initState(self):
        self.notifier = ValueNotifier(0)

    def dispose(self):
        self.notifier.dispose()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ValueListenableBuilder(
                    valueListenable=self.notifier,
                    builder=lambda context, value, _: Text(
                        f"value = {value}",
                        style=TextStyle(fontSize=20, fontWeight=FontWeight.bold),
                    ),
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=lambda: setattr(
                                self.notifier, "value", self.notifier.value - 1
                            ),
                            child=Text("−"),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=lambda: setattr(
                                self.notifier, "value", self.notifier.value + 1
                            ),
                            child=Text("+"),
                        ),
                    ],
                ),
            ],
        )


_COUNTER_CODE = (
    "from flut.flutter.foundation import ChangeNotifier\n"
    "\n"
    "class Counter(ChangeNotifier):\n"
    "    def __init__(self, initial: int = 0):\n"
    "        super().__init__()\n"
    "        self._value = initial\n"
    "\n"
    "    @property\n"
    "    def value(self) -> int:\n"
    "        return self._value\n"
    "\n"
    "    def increment(self):\n"
    "        self._value += 1\n"
    "        self.notifyListeners()\n"
    "\n"
    "# Use it in widgets:\n"
    "ListenableBuilder(\n"
    "    listenable=counter,\n"
    "    builder=lambda context, _: Text(f'{counter.value}'),\n"
    ")"
)


class ListenablePage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Listenable",
            description=(
                "`Listenable` is Flutter's observer contract: anything that "
                "fires `notifyListeners()` and supports `addListener` / "
                "`removeListener`. In flut you can subclass `ChangeNotifier` "
                "in pure Python, combine listenables with `Listenable.merge`, "
                "or use the built-in `ValueNotifier` — and rebuild any number "
                "of widgets via `ListenableBuilder` / `ValueListenableBuilder`."
            ),
            children=[
                SplitViewTile(
                    title="Custom ChangeNotifier",
                    description=(
                        "Subclass `ChangeNotifier` and call `notifyListeners()`. "
                        "Flut auto-creates the matching Dart wrapper; the "
                        "Python object owns the state."
                    ),
                    instruction="Press +, −, or reset to mutate the model.",
                    visible=_CounterDemo(),
                    code=CodeArea(language="python", code=_COUNTER_CODE),
                ),
                SplitViewTile(
                    title="Shared Listenable",
                    description=(
                        "Two independent `ListenableBuilder` subscribers share "
                        "the same `Counter` instance. Updating once rebuilds "
                        "both views."
                    ),
                    instruction="Tap + or − and watch both badges update.",
                    visible=_SharedCounterDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "counter = Counter(initial=10)\n"
                            "\n"
                            "ListenableBuilder(\n"
                            "    listenable=counter,\n"
                            "    builder=lambda c, _: Text(str(counter.value)),\n"
                            ")\n"
                            "# ... another ListenableBuilder elsewhere\n"
                            "# subscribed to the SAME `counter`."
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Listenable.merge",
                    description=(
                        "Combine multiple listenables into one. The builder "
                        "rebuilds whenever ANY of the underlying notifiers "
                        "fires."
                    ),
                    instruction="Increment either side; `sum` updates from a single builder.",
                    visible=_MergedListenableDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "left = Counter()\n"
                            "right = Counter()\n"
                            "merged = Listenable.merge([left, right])\n"
                            "\n"
                            "ListenableBuilder(\n"
                            "    listenable=merged,\n"
                            "    builder=lambda c, _: Text(\n"
                            "        f'sum = {left.value + right.value}',\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ValueNotifier",
                    description=(
                        "Built-in `Listenable` that wraps a single mutable "
                        "value. `ValueListenableBuilder` receives the value "
                        "directly and rebuilds when it changes."
                    ),
                    instruction="Press + or − to mutate `notifier.value`.",
                    visible=_ValueNotifierDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "notifier = ValueNotifier(0)\n"
                            "\n"
                            "ValueListenableBuilder(\n"
                            "    valueListenable=notifier,\n"
                            "    builder=lambda c, value, _: Text(f'{value}'),\n"
                            ")\n"
                            "\n"
                            "# Mutate via the `.value` setter:\n"
                            "notifier.value += 1"
                        ),
                    ),
                ),
            ],
        )
