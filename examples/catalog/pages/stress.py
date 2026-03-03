import asyncio
import time

from flut.dart import Color, Brightness
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Expanded,
    Icon,
    GestureDetector,
    MouseRegion,
    Wrap,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Icons,
    CircularProgressIndicator,
    Theme,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BorderRadius,
    BoxDecoration,
    Border,
)
from flut.flutter.foundation import ValueKey
from utils import CODE_FONT_FAMILY
from widgets import CatalogPage, SplitViewTile, CodeArea

SAMPLE_TEXT = (
    "The quick brown fox jumps over the lazy dog. "
    "Flutter's widget composition model makes it really powerful for building "
    "cross-platform UIs. Each widget is a lightweight description of part of "
    "the user interface, and the framework handles all the rendering and "
    "layout efficiently. When using Flut, Python code maps almost one-to-one "
    "with Dart's Flutter API, enabling developers to leverage Python's "
    "ecosystem while building beautiful native applications. "
    "Async streaming is a common pattern for LLM integrations, where tokens "
    "arrive one at a time and must be displayed incrementally to the user."
)


class _StreamDemo(StatefulWidget):
    def createState(self):
        return _StreamDemoState()


class _StreamDemoState(State[_StreamDemo]):

    def initState(self):
        self.tokens = []
        self.streaming = False
        self.stream_done = False
        self.token_count = 0
        self.last_update_time = ""
        self.start_time = 0.0
        self.elapsed = 0.0
        self.updates_received = 0

    async def _start_stream(self):
        if self.streaming:
            return

        async def _stream_task():
            self.streaming = True
            self.stream_done = False
            self.tokens = []
            self.token_count = 0
            self.updates_received = 0
            self.start_time = time.monotonic()
            self.setState(lambda: None)

            words = SAMPLE_TEXT.split(" ")
            for i, word in enumerate(words):
                if not self.streaming:
                    break

                self.tokens.append(word)
                self.token_count = i + 1
                now = time.monotonic()
                self.elapsed = now - self.start_time
                self.last_update_time = f"{self.elapsed:.2f}s"
                self.updates_received += 1
                self.setState(lambda: None)

                await asyncio.sleep(0.05)

            self.streaming = False
            self.stream_done = True
            self.elapsed = time.monotonic() - self.start_time
            self.last_update_time = f"{self.elapsed:.2f}s"
            self.setState(lambda: None)

        asyncio.create_task(_stream_task())

    def _stop_stream(self):
        self.streaming = False
        self.setState(lambda: None)

    def _reset(self):
        self.tokens = []
        self.streaming = False
        self.stream_done = False
        self.token_count = 0
        self.last_update_time = ""
        self.elapsed = 0.0
        self.updates_received = 0
        self.setState(lambda: None)

    def build(self, context):
        theme = Theme.of(context)
        streamed_text = " ".join(self.tokens) if self.tokens else ""

        status_color = (
            Colors.orange
            if self.streaming
            else (Colors.green if self.stream_done else Colors.grey)
        )
        status_text = (
            f"Streaming... token {self.token_count} | "
            f"elapsed: {self.last_update_time} | "
            f"updates: {self.updates_received}"
            if self.streaming
            else (
                f"Done! {self.token_count} tokens in {self.last_update_time} | "
                f"updates: {self.updates_received}"
                if self.stream_done
                else "Idle — press Start to begin streaming"
            )
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Row(
                                children=[
                                    Icon(Icons.play_arrow),
                                    SizedBox(width=6),
                                    Text("Start Stream"),
                                ],
                            ),
                            onPressed=(None if self.streaming else self._start_stream),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Row(
                                children=[
                                    Icon(Icons.stop),
                                    SizedBox(width=6),
                                    Text("Stop"),
                                ],
                            ),
                            onPressed=(self._stop_stream if self.streaming else None),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Text("Reset"),
                            onPressed=None if self.streaming else self._reset,
                        ),
                    ],
                ),
                SizedBox(height=16),
                Row(
                    children=[
                        (
                            SizedBox(
                                width=16.0,
                                height=16.0,
                                child=CircularProgressIndicator(),
                            )
                            if self.streaming
                            else SizedBox()
                        ),
                        SizedBox(width=8 if self.streaming else 0),
                        Text(
                            status_text,
                            style=TextStyle(
                                fontSize=14,
                                fontWeight=FontWeight.bold,
                                color=status_color,
                                fontFamily=CODE_FONT_FAMILY,
                            ),
                        ),
                    ],
                ),
                SizedBox(height=16),
                Container(
                    width=700.0,
                    padding=EdgeInsets.all(16),
                    decoration=BoxDecoration(
                        color=Colors.grey.withValues(alpha=0.1),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Text(
                        streamed_text if streamed_text else "Waiting for stream...",
                        style=TextStyle(
                            fontSize=14,
                            height=1.6,
                            color=(None if streamed_text else Colors.grey),
                        ),
                    ),
                ),
            ],
        )


class _TickingChild(StatefulWidget):
    def __init__(self, label, tick, key=None):
        super().__init__(key=key)
        self.label = label
        self.tick = tick

    def createState(self):
        return _TickingChildState()


class _TickingChildState(State["_TickingChild"]):

    def initState(self):
        self.local_count = 0

    def _increment(self):
        self.local_count += 1
        self.setState(lambda: None)

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark
        w = self.widget
        bg = Color(0xFF2C2C2C) if is_dark else Color(0xFFF5F5F5)
        border_color = Color(0xFF555555) if is_dark else Color(0xFFE0E0E0)
        return GestureDetector(
            onTap=self._increment,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=12, vertical=8),
                margin=EdgeInsets.only(bottom=4),
                decoration=BoxDecoration(
                    color=bg,
                    borderRadius=BorderRadius.circular(6),
                    border=Border.all(width=1, color=border_color),
                ),
                child=Row(
                    children=[
                        Text(
                            w.label,
                            style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(width=8),
                        Text(
                            f"parent tick: {w.tick}",
                            style=TextStyle(fontSize=12, color=Colors.grey),
                        ),
                        SizedBox(width=8),
                        Text(
                            f"local taps: {self.local_count}",
                            style=TextStyle(fontSize=12, color=Colors.blue),
                        ),
                    ],
                ),
            ),
        )


class _HoverChild(StatefulWidget):
    def __init__(self, label, color, key=None):
        super().__init__(key=key)
        self.label = label
        self.color = color

    def createState(self):
        return _HoverChildState()


class _HoverChildState(State["_HoverChild"]):

    def initState(self):
        self._hovered = False

    def _on_enter(self, event=None):
        self._hovered = True
        self.setState(lambda: None)

    def _on_exit(self, event=None):
        self._hovered = False
        self.setState(lambda: None)

    def build(self, context):
        w = self.widget
        bg = Color(0xFFFFFFFF) if self._hovered else w.color
        text_color = Colors.black if self._hovered else Colors.white
        return MouseRegion(
            onEnter=self._on_enter,
            onExit=self._on_exit,
            child=Container(
                padding=EdgeInsets.all(10),
                margin=EdgeInsets.only(right=8, bottom=8),
                decoration=BoxDecoration(
                    color=bg,
                    borderRadius=BorderRadius.circular(8),
                    border=Border.all(
                        width=2,
                        color=w.color if self._hovered else Color(0x00000000),
                    ),
                ),
                child=Text(
                    w.label,
                    style=TextStyle(fontSize=12, color=text_color),
                ),
            ),
        )


class _KeyedChildrenDemo(StatefulWidget):
    def createState(self):
        return _KeyedChildrenDemoState()


class _KeyedChildrenDemoState(State["_KeyedChildrenDemo"]):

    def initState(self):
        self.parent_tick = 0
        self.auto_ticking = False
        self._tick_task = None
        self.item_count = 8
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-30:]

    def _start_auto_tick(self):
        if self.auto_ticking:
            return
        self.auto_ticking = True
        self.setState(lambda: None)
        self._tick_task = asyncio.create_task(self._tick_loop())

    def _stop_auto_tick(self):
        self.auto_ticking = False
        if self._tick_task and not self._tick_task.done():
            self._tick_task.cancel()
        self._tick_task = None
        self.setState(lambda: None)

    async def _tick_loop(self):
        try:
            while self.auto_ticking:
                await asyncio.sleep(0.05)
                self.parent_tick += 1
                self._add_log(f"tick {self.parent_tick}")
                self.setState(lambda: None)
        except asyncio.CancelledError:
            pass

    def _manual_tick(self):
        self.parent_tick += 1
        self._add_log(f"manual tick {self.parent_tick}")
        self.setState(lambda: None)

    def _add_item(self):
        self.item_count += 1
        self._add_log(f"items: {self.item_count}")
        self.setState(lambda: None)

    def _remove_item(self):
        if self.item_count > 1:
            self.item_count -= 1
            self._add_log(f"items: {self.item_count}")
            self.setState(lambda: None)

    def _reset(self):
        self._stop_auto_tick()
        self.parent_tick = 0
        self.item_count = 8
        self.log_lines = []
        self.setState(lambda: None)

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark
        log_bg = Color(0xFF1E1E1E) if is_dark else Color(0xFFFAFAFA)
        log_border = Color(0xFF555555) if is_dark else Color(0xFFE0E0E0)
        log_text_color = Color(0xFFCCCCCC) if is_dark else Color(0xFF424242)

        keyed_children = [
            _TickingChild(
                label=f"Child {i}",
                tick=self.parent_tick,
                key=ValueKey(f"stress_child_{i}"),
            )
            for i in range(self.item_count)
        ]

        log_text = "\n".join(self.log_lines) if self.log_lines else "(no events yet)"

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            onPressed=self._manual_tick,
                            child=Text("Tick Once"),
                        ),
                        ElevatedButton(
                            onPressed=(
                                self._stop_auto_tick
                                if self.auto_ticking
                                else self._start_auto_tick
                            ),
                            child=Text(
                                "Stop Auto" if self.auto_ticking else "Start Auto"
                            ),
                        ),
                        ElevatedButton(
                            onPressed=self._add_item,
                            child=Text("+Item"),
                        ),
                        ElevatedButton(
                            onPressed=self._remove_item,
                            child=Text("-Item"),
                        ),
                        ElevatedButton(
                            onPressed=self._reset,
                            child=Text("Reset"),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"Parent tick: {self.parent_tick}  |  "
                    f"Items: {self.item_count}  |  "
                    f"Auto: {'ON' if self.auto_ticking else 'OFF'}",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=8),
                Column(children=keyed_children),
                SizedBox(height=8),
                Text(
                    "Event log (last 30):",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
                SizedBox(height=4),
                Container(
                    padding=EdgeInsets.all(8),
                    width=350.0,
                    decoration=BoxDecoration(
                        color=log_bg,
                        borderRadius=BorderRadius.circular(4),
                        border=Border.all(width=1, color=log_border),
                    ),
                    child=Text(
                        log_text,
                        style=TextStyle(fontSize=11, color=log_text_color),
                    ),
                ),
            ],
        )


class _HoverChipsDemo(StatefulWidget):
    def createState(self):
        return _HoverChipsDemoState()


class _HoverChipsDemoState(State["_HoverChipsDemo"]):

    def initState(self):
        self.hover_rebuilds = 0

    def _simulate_hover_rebuild(self):
        self.hover_rebuilds += 1
        self.setState(lambda: None)

    def build(self, context):
        colors = [
            Color(0xFF2196F3),
            Color(0xFF4CAF50),
            Color(0xFFFF9800),
            Color(0xFF9C27B0),
            Color(0xFFE91E63),
            Color(0xFF00BCD4),
        ]
        hover_chips = [
            _HoverChild(
                label=f"Chip {i}",
                color=colors[i % len(colors)],
                key=ValueKey(f"hover_chip_{i}"),
            )
            for i in range(6)
        ]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._simulate_hover_rebuild,
                            child=Text("Simulate Hover Rebuild"),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"Hover rebuilds: {self.hover_rebuilds}",
                            style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Row(children=hover_chips),
            ],
        )


class _BugReproNotice(StatelessWidget):
    def build(self, context):
        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Color(0xFFFFF3E0),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Row(
                children=[
                    Icon(Icons.warning_amber, color=Colors.orange),
                    SizedBox(width=8),
                    Expanded(
                        child=Text(
                            "BUG REPRO: Start the stream, then click and hold "
                            "the window title bar or a resize edge. Watch the "
                            "elapsed timer and token counter freeze. Release the "
                            "mouse — updates resume in a burst.",
                            style=TextStyle(fontSize=13, color=Color(0xFFE65100)),
                        ),
                    ),
                ],
            ),
        )


class StressPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Async Stream Stress Test",
            description=(
                "Exercises the rendering pipeline with rapid async updates, making "
                "it easier to spot throughput issues, jank, and state behavior "
                "under sustained load."
            ),
            children=[
                SplitViewTile(
                    title="Token Stream",
                    description=(
                        "An async task splits sample text into words and streams "
                        "them one at a time with a 50ms delay between each token. "
                        "A live status line shows token count, elapsed time, and "
                        "total setState calls."
                    ),
                    instruction=(
                        "Click Start Stream to begin. Tokens appear one by one in "
                        "the output area. Use Stop to halt mid-stream and Reset to "
                        "clear. The status line updates on every token."
                    ),
                    visible=_StreamDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "async def start_stream():\n"
                            "    words = SAMPLE_TEXT.split(' ')\n"
                            "    for i, word in enumerate(words):\n"
                            "        tokens.append(word)\n"
                            "        token_count = i + 1\n"
                            "        elapsed = time.monotonic() - start_time\n"
                            "        setState(lambda: None)\n"
                            "        await asyncio.sleep(0.05)\n"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Window-Drag Freeze Bug",
                    description=(
                        "Demonstrates a known issue where holding the window title "
                        "bar or resize edge blocks the event loop, causing async "
                        "updates to freeze and then burst-replay on release."
                    ),
                    instruction=(
                        "Start the stream in the tile above, then click and hold "
                        "the window title bar or a resize edge. The elapsed timer "
                        "and token counter will freeze. Release the mouse to see "
                        "updates resume in a burst."
                    ),
                    visible=_BugReproNotice(),
                    code=CodeArea(
                        language="python",
                        code=("asyncio.create_task(stream_task())\n"),
                    ),
                ),
                SplitViewTile(
                    title="Keyed Children + Auto Tick",
                    description=(
                        "Each child is a keyed StatefulWidget that receives the parent tick count "
                        "as a prop. Stable keys ensure children survive parent rebuilds and "
                        "preserve their own local tap count across re-renders."
                    ),
                    instruction=(
                        "Click 'Tick Once' to increment the parent tick counter. "
                        "Use 'Start Auto (50ms)' for rapid rebuilds. "
                        "Tap any child row to increment its local tap count \u2014 "
                        "local state should survive parent rebuilds. "
                        "Use +Item / -Item to change the list size."
                    ),
                    visible=_KeyedChildrenDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class TickingChild(StatefulWidget):\n"
                            "    def __init__(self, label, tick, key=None):\n"
                            "        super().__init__(key=key)\n"
                            "        self.label = label\n"
                            "        self.tick = tick\n"
                            "\n"
                            "children = [\n"
                            "    TickingChild(\n"
                            "        label=f'Child {i}',\n"
                            "        tick=parent_tick,\n"
                            "        key=ValueKey(f'stress_child_{i}'),\n"
                            "    )\n"
                            "    for i in range(item_count)\n"
                            "]"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Hover Chips (MouseRegion)",
                    description=(
                        "Each chip uses MouseRegion with onEnter/onExit to toggle hover state "
                        "via setState. This pattern mirrors DraggableDivider and validates that "
                        "hover-triggered rebuilds don't conflict with parent rebuilds."
                    ),
                    instruction=(
                        "Hover over the colored chips to toggle their highlight. "
                        "Click 'Simulate Hover Rebuild' to trigger a parent rebuild. "
                        "No console errors should appear."
                    ),
                    visible=_HoverChipsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class HoverChild(StatefulWidget):\n"
                            "    def __init__(self, label, color, key=None):\n"
                            "        super().__init__(key=key)\n"
                            "        self.label = label\n"
                            "        self.color = color\n"
                            "\n"
                            "MouseRegion(\n"
                            "    onEnter=on_enter,\n"
                            "    onExit=on_exit,\n"
                            "    child=Container(\n"
                            "        decoration=BoxDecoration(\n"
                            "            color=Color(0xFFFFFFFF) if hovered else color,\n"
                            "            borderRadius=BorderRadius.circular(8),\n"
                            "        ),\n"
                            "        child=Text(label),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
