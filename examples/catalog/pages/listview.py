from utils import CODE_FONT_FAMILY
from flut.dart import Duration, Color
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
    Icon,
    ListView,
    CustomScrollView,
    SliverToBoxAdapter,
    SliverPadding,
    ScrollController,
    Padding,
    NotificationListener,
    AutomaticKeepAliveClientMixin,
    Wrap,
    FocusNode,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Icons,
    ListTile,
    CircleAvatar,
    Switch,
    Checkbox,
)
from flut.dart.ui import Clip, FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BorderRadius,
    BoxDecoration,
    RoundedRectangleBorder,
)
from flut.flutter.services import SystemMouseCursors
from flut.flutter.animation import Curves
from flut.flutter.scheduler import SchedulerBinding
from widgets import CatalogPage, SplitViewTile, CodeArea


class _ListItem(StatefulWidget):
    def __init__(self, index):
        super().__init__()
        self.index = index

    def createState(self):
        return _ListItemState()


class _ListItemState(State["_ListItem"]):
    def build(self, context):
        return Container(
            padding=EdgeInsets.symmetric(horizontal=16, vertical=10),
            child=Row(
                children=[
                    Container(
                        width=32.0,
                        height=32.0,
                        decoration=BoxDecoration(
                            color=Colors.blue.withValues(alpha=0.1),
                            borderRadius=BorderRadius.circular(16),
                        ),
                        child=Center(
                            child=Text(
                                str(self.widget.index),
                                style=TextStyle(fontSize=12, color=Colors.blue),
                            ),
                        ),
                    ),
                    SizedBox(width=12),
                    Text(f"Stateful item {self.widget.index}"),
                ],
            ),
        )


class _CounterItem(StatefulWidget):
    def __init__(self, index):
        super().__init__()
        self.index = index

    def createState(self):
        return _CounterItemState()


class _CounterItemState(State["_CounterItem"]):
    def initState(self):
        self.count = 0

    def build(self, context):
        return Container(
            padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
            child=Row(
                children=[
                    Text(f"Item {self.widget.index}", style=TextStyle(fontSize=14)),
                    SizedBox(width=12),
                    ElevatedButton(
                        child=Text(f"Taps: {self.count}"),
                        onPressed=lambda: self.setState(
                            lambda: setattr(self, "count", self.count + 1)
                        ),
                    ),
                ],
            ),
        )


class _KeepAliveCounterItem(StatefulWidget):
    def __init__(self, index):
        super().__init__()
        self.index = index

    def createState(self):
        return _KeepAliveCounterItemState()


class _KeepAliveCounterItemState(
    State["_KeepAliveCounterItem"], AutomaticKeepAliveClientMixin
):
    def initState(self):
        self.count = 0

    def build(self, context):
        return Container(
            padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
            child=Row(
                children=[
                    Text(f"Item {self.widget.index}", style=TextStyle(fontSize=14)),
                    SizedBox(width=12),
                    ElevatedButton(
                        child=Text(f"Taps: {self.count}"),
                        onPressed=lambda: self.setState(
                            lambda: setattr(self, "count", self.count + 1)
                        ),
                    ),
                    SizedBox(width=8),
                    Text(
                        "(kept alive)", style=TextStyle(fontSize=11, color=Colors.green)
                    ),
                ],
            ),
        )


class _ScrollControllerDemo(StatefulWidget):
    def createState(self):
        return _ScrollControllerDemoState()


class _ScrollControllerDemoState(State["_ScrollControllerDemo"]):
    def initState(self):
        self.scroll_controller = ScrollController()
        self.item_count = 40
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-10:]
        self.setState(lambda: None)

    def _print_scroll_info(self):
        offset = self.scroll_controller.offset
        has_clients = self.scroll_controller.hasClients
        self._add_log(f"offset: {offset:.1f}  hasClients: {has_clients}")
        pos = self.scroll_controller.position
        if pos:
            self._add_log(
                f"  pixels: {pos.pixels:.1f}  "
                f"min: {pos.minScrollExtent:.1f}  "
                f"max: {pos.maxScrollExtent:.1f}"
            )
            self._add_log(
                f"  viewport: {pos.viewportDimension:.1f}  atEdge: {pos.atEdge}"
            )

    def _scroll_to_top(self):
        self.scroll_controller.jumpTo(0)
        self._add_log("Jumped to top")

    def _scroll_to_bottom(self):
        pos = self.scroll_controller.position
        if pos:
            max_ext = pos.maxScrollExtent
            pos.animateTo(
                max_ext, duration=Duration(milliseconds=500), curve=Curves.fastOutSlowIn
            )
            self._add_log(f"Animating to bottom (max={max_ext:.1f})")

    def _scroll_to_middle(self):
        pos = self.scroll_controller.position
        if pos:
            mid = pos.maxScrollExtent / 2
            pos.animateTo(
                mid, duration=Duration(milliseconds=400), curve=Curves.easeInOut
            )
            self._add_log(f"Animating to middle ({mid:.1f})")

    def _add_items(self):
        self.item_count += 10
        self._add_log(f"Added 10 items \u2192 {self.item_count} total")

        label = "scroll_to_new"

        def _scroll_to_new(_):
            if self.scroll_controller.hasClients:
                max_ext = self.scroll_controller.position.maxScrollExtent
                self.scroll_controller.jumpTo(max_ext)
                self._add_log(
                    f"postFrameCallback '{label}' fired \u2192 scrolled to {max_ext:.1f}"
                )

        SchedulerBinding.instance.addPostFrameCallback(_scroll_to_new, debugLabel=label)

    def _remove_items(self):
        if self.item_count > 10:
            self.item_count -= 10
            self._add_log(f"Removed 10 items \u2192 {self.item_count} total")

    def _clear_log(self):
        self.log_lines = []
        self.setState(lambda: None)

    def build(self, context):
        items = []
        for i in range(self.item_count):
            items.append(_ListItem(index=i))

        log_widgets = []
        for line in self.log_lines:
            log_widgets.append(
                Text(line, style=TextStyle(fontSize=11, fontFamily=CODE_FONT_FAMILY)),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "Use buttons to interact with the scroll controller.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Text("Info"),
                            onPressed=self._print_scroll_info,
                        ),
                        ElevatedButton(
                            child=Text("Top"),
                            onPressed=self._scroll_to_top,
                        ),
                        ElevatedButton(
                            child=Text("Middle"),
                            onPressed=self._scroll_to_middle,
                        ),
                        ElevatedButton(
                            child=Text("Bottom"),
                            onPressed=self._scroll_to_bottom,
                        ),
                        ElevatedButton(
                            child=Text("+10 items"),
                            onPressed=self._add_items,
                        ),
                        ElevatedButton(
                            child=Text("-10 items"),
                            onPressed=self._remove_items,
                        ),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    height=300.0,
                    decoration=BoxDecoration(
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=ListView(
                        controller=self.scroll_controller,
                        children=items,
                    ),
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Colors.grey.withValues(alpha=0.05),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Row(
                                children=[
                                    Text(
                                        "Scroll Log",
                                        style=TextStyle(
                                            fontSize=14,
                                            fontWeight=FontWeight.bold,
                                        ),
                                    ),
                                    SizedBox(width=8),
                                    ElevatedButton(
                                        child=Text("Clear"),
                                        onPressed=self._clear_log,
                                    ),
                                ],
                            ),
                            SizedBox(height=8),
                            *log_widgets,
                        ],
                    ),
                ),
            ],
        )


class _NotificationListenerDemo(StatefulWidget):
    def createState(self):
        return _NotificationListenerDemoState()


class _NotificationListenerDemoState(State["_NotificationListenerDemo"]):
    def initState(self):
        self.last_event = ""
        self.pixels = 0.0
        self.max_extent = 0.0
        self.event_count = 0

    def _on_notification(self, notification):
        n_type = type(notification).__name__
        m = notification.metrics
        self.event_count += 1
        extra = ""
        if (
            hasattr(notification, "scrollDelta")
            and notification.scrollDelta is not None
        ):
            extra = f"  delta={notification.scrollDelta:.1f}"
        elif hasattr(notification, "overscroll"):
            extra = f"  overscroll={notification.overscroll:.1f}"

        def update():
            self.last_event = f"{n_type}{extra}"
            self.pixels = m.pixels
            self.max_extent = m.maxScrollExtent

        self.setState(update)
        return False

    def build(self, context):
        progress = self.pixels / self.max_extent * 100 if self.max_extent > 0 else 0

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Text(
                            f"Events: {self.event_count}",
                            style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                        ),
                        SizedBox(width=16),
                        Text(
                            f"Position: {self.pixels:.0f}/{self.max_extent:.0f} ({progress:.0f}%)",
                            style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    (
                        f"Last: {self.last_event}"
                        if self.last_event
                        else "Scroll the list below"
                    ),
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.blue if self.last_event else Colors.grey,
                    ),
                ),
                SizedBox(height=8),
                NotificationListener(
                    onNotification=self._on_notification,
                    child=Container(
                        height=180.0,
                        child=ListView(
                            children=[
                                Container(
                                    padding=EdgeInsets.symmetric(
                                        horizontal=16, vertical=10
                                    ),
                                    child=Text(
                                        f"Item {i}", style=TextStyle(fontSize=13)
                                    ),
                                )
                                for i in range(40)
                            ],
                        ),
                    ),
                ),
            ],
        )


def _build_colored_item(context, index):
    colors = [Colors.blue, Colors.green, Colors.orange, Colors.purple, Colors.red]
    color = colors[index % len(colors)]
    return Container(
        padding=EdgeInsets.symmetric(horizontal=16, vertical=10),
        child=Row(
            children=[
                Container(
                    width=32.0,
                    height=32.0,
                    decoration=BoxDecoration(
                        color=color.withValues(alpha=0.15),
                        borderRadius=BorderRadius.circular(16),
                    ),
                    child=Center(
                        child=Text(
                            str(index),
                            style=TextStyle(
                                fontSize=12,
                                color=color,
                                fontWeight=FontWeight.bold,
                            ),
                        ),
                    ),
                ),
                SizedBox(width=12),
                Text(f"Builder item {index}"),
            ],
        ),
    )


class _ScrollMetricsDetailDemo(StatefulWidget):
    def createState(self):
        return _ScrollMetricsDetailDemoState()


class _ScrollMetricsDetailDemoState(State["_ScrollMetricsDetailDemo"]):
    def initState(self):
        self.axis_direction = ""
        self.extent_before = 0.0
        self.extent_after = 0.0
        self.out_of_range = False
        self.pixels = 0.0
        self.viewport = 0.0
        self.event_count = 0

    def _on_notification(self, notification):
        m = notification.metrics
        self.event_count += 1

        def update():
            self.axis_direction = str(m.axisDirection) if m.axisDirection else "down"
            self.extent_before = m.extentBefore
            self.extent_after = m.extentAfter
            self.out_of_range = m.outOfRange
            self.pixels = m.pixels
            self.viewport = m.viewportDimension

        self.setState(update)
        return False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=Colors.grey.withValues(alpha=0.05),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "ScrollMetrics (live)",
                                style=TextStyle(
                                    fontSize=14,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                f"axisDirection: {self.axis_direction}",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            Text(
                                f"extentBefore: {self.extent_before:.1f}",
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=Colors.blue,
                                ),
                            ),
                            Text(
                                f"extentAfter: {self.extent_after:.1f}",
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=Colors.green,
                                ),
                            ),
                            Text(
                                f"outOfRange: {self.out_of_range}",
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=(
                                        Colors.red if self.out_of_range else Colors.grey
                                    ),
                                ),
                            ),
                            Text(
                                f"pixels: {self.pixels:.1f}  viewport: {self.viewport:.1f}",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            Text(
                                f"events: {self.event_count}",
                                style=TextStyle(
                                    fontSize=12,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=Colors.grey,
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                NotificationListener(
                    onNotification=self._on_notification,
                    child=Container(
                        height=200.0,
                        child=ListView(
                            children=[
                                Container(
                                    padding=EdgeInsets.symmetric(
                                        horizontal=16, vertical=10
                                    ),
                                    child=Text(
                                        f"Item {i}", style=TextStyle(fontSize=13)
                                    ),
                                )
                                for i in range(50)
                            ],
                        ),
                    ),
                ),
            ],
        )


class _ListTileShapeDemo(StatefulWidget):
    def createState(self):
        return _ListTileShapeDemoState()


class _ListTileShapeDemoState(State[_ListTileShapeDemo]):
    def initState(self):
        self.selected = False

    def build(self, context):
        return Container(
            width=500.0,
            child=ListTile(
                shape=RoundedRectangleBorder(
                    borderRadius=BorderRadius.circular(20),
                ),
                selected=self.selected,
                selectedColor=Colors.green,
                selectedTileColor=Color(0xFFE8F5E9),
                title=Text("Shaped ListTile"),
                subtitle=Text("Toggle selected state"),
                trailing=Switch(
                    value=self.selected,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "selected", v)
                    ),
                ),
            ),
        )


class _ListTileAdvancedDemo(StatefulWidget):
    def createState(self):
        return _ListTileAdvancedDemoState()


class _ListTileAdvancedDemoState(State["_ListTileAdvancedDemo"]):

    def initState(self):
        self.long_press_log = ""

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=440.0,
                    child=Column(
                        children=[
                            ListTile(
                                leading=Icon(Icons.compress),
                                title=Text("Dense tile"),
                                subtitle=Text("dense=True, tileColor"),
                                dense=True,
                                tileColor=Color(0xFFF5F5F5),
                                onTap=lambda: self.setState(
                                    lambda: setattr(
                                        self, "long_press_log", "Dense tile tapped"
                                    )
                                ),
                            ),
                            ListTile(
                                title=Text("Custom styles + onLongPress"),
                                titleTextStyle=TextStyle(
                                    fontSize=16,
                                    color=Colors.deepPurple,
                                    fontWeight=FontWeight.bold,
                                ),
                                subtitleTextStyle=TextStyle(
                                    fontSize=11, color=Colors.grey
                                ),
                                subtitle=Text("Long-press me"),
                                contentPadding=EdgeInsets.symmetric(horizontal=24),
                                onLongPress=lambda: self.setState(
                                    lambda: setattr(
                                        self, "long_press_log", "Long pressed!"
                                    )
                                ),
                            ),
                            ListTile(
                                title=Text("Disabled tile"),
                                subtitle=Text("enabled=False"),
                                enabled=False,
                            ),
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(
                    self.long_press_log,
                    style=TextStyle(fontSize=12, color=Colors.blue),
                ),
            ],
        )


class ListViewPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="ListView & Scrolling",
            description=(
                "Demonstrates building scrollable content efficiently, observing "
                "scroll state, composing slivers, and preserving item state across "
                "rebuilds and reuse."
            ),
            children=[
                SplitViewTile(
                    title="ListView + ScrollController",
                    description=(
                        "ScrollController provides programmatic control over a ListView's "
                        "scroll position. Access offset, pixels, viewport dimensions, and "
                        "use jumpTo/animateTo for navigation. addPostFrameCallback ensures "
                        "scroll happens after the frame is built."
                    ),
                    instruction=(
                        "Use the buttons to jump or animate to different scroll positions. "
                        "Add or remove items to change the list length. "
                        "Press Info to inspect ScrollPosition properties in the log panel."
                    ),
                    visible=_ScrollControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "controller = ScrollController()\n\n"
                            "ListView(\n"
                            "    controller=controller,\n"
                            "    children=[...],\n"
                            ")\n\n"
                            "controller.jumpTo(0)\n"
                            "controller.position.animateTo(\n"
                            "    target,\n"
                            "    duration=Duration(milliseconds=500),\n"
                            "    curve=Curves.fastOutSlowIn,\n"
                            ")\n"
                            "\n"
                            "SchedulerBinding.instance.addPostFrameCallback(\n"
                            "    scroll_to_new,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListView.builder",
                    description=(
                        "Builds items lazily on demand via itemBuilder. "
                        "Only visible items are constructed, making it efficient "
                        "for large lists."
                    ),
                    instruction=(
                        "Scroll through 1000 items. Each is built on demand "
                        "with a colored index badge."
                    ),
                    visible=Container(
                        height=300.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=ListView.builder(
                            itemCount=1000,
                            itemBuilder=_build_colored_item,
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListView.builder(\n"
                            "    itemCount=1000,\n"
                            "    itemBuilder=build_item,\n"
                            ")\n\n"
                            "def build_item(context, index):\n"
                            "    return Text(f'Item {index}')"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomScrollView + Slivers",
                    description=(
                        "CustomScrollView composes scrollable areas from sliver widgets. "
                        "SliverToBoxAdapter wraps regular widgets for use inside a sliver "
                        "list, and SliverPadding adds insets around a sliver child."
                    ),
                    instruction=(
                        "Scroll through the sliver-based list with a padded header "
                        "and 15 content items."
                    ),
                    visible=Container(
                        height=300.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=CustomScrollView(
                            slivers=[
                                SliverPadding(
                                    padding=EdgeInsets.all(8),
                                    sliver=SliverToBoxAdapter(
                                        child=Container(
                                            padding=EdgeInsets.all(16),
                                            decoration=BoxDecoration(
                                                color=Color(0xFFE3F2FD),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=Text(
                                                "SliverToBoxAdapter inside SliverPadding",
                                                style=TextStyle(
                                                    fontSize=14,
                                                    fontWeight=FontWeight.bold,
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                *[
                                    SliverToBoxAdapter(
                                        child=Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=16, vertical=8
                                            ),
                                            child=Text(f"Sliver item {i}"),
                                        ),
                                    )
                                    for i in range(15)
                                ],
                                SliverToBoxAdapter(
                                    child=Center(
                                        child=Padding(
                                            padding=EdgeInsets.all(16),
                                            child=Text(
                                                "End of slivers",
                                                style=TextStyle(color=Colors.grey),
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
                            "CustomScrollView(\n"
                            "    slivers=[\n"
                            "        SliverPadding(\n"
                            "            padding=EdgeInsets.all(8),\n"
                            "            sliver=SliverToBoxAdapter(\n"
                            "                child=Text('Header'),\n"
                            "            ),\n"
                            "        ),\n"
                            "        SliverToBoxAdapter(\n"
                            "            child=Text('Content'),\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListView itemExtent",
                    description=(
                        "ListView itemExtent forces all children to a fixed extent "
                        "along the scroll axis, improving performance and ensuring uniform sizing."
                    ),
                    instruction="Compare the two lists: the left uses itemExtent=80 for uniform tall items, the right has variable heights.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "itemExtent=80",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=180.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=ListView(
                                                itemExtent=80.0,
                                                shrinkWrap=True,
                                                children=[
                                                    Container(
                                                        color=Colors.blue.withValues(
                                                            alpha=0.1 + i * 0.12
                                                        ),
                                                        child=Center(
                                                            child=Text(
                                                                f"Fixed {i + 1}",
                                                                style=TextStyle(
                                                                    fontSize=12
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                    for i in range(5)
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=12),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "No itemExtent (variable)",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=180.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=ListView(
                                                shrinkWrap=True,
                                                children=[
                                                    Container(
                                                        height=20.0 + i * 15.0,
                                                        color=Colors.green.withValues(
                                                            alpha=0.1 + i * 0.12
                                                        ),
                                                        child=Center(
                                                            child=Text(
                                                                f"Var {i + 1} (h={20 + i * 15})",
                                                                style=TextStyle(
                                                                    fontSize=12
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                    for i in range(5)
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListView(\n"
                            "    itemExtent=80.0,\n"
                            "    children=[\n"
                            "        Container(child=Text('Fixed height')),\n"
                            "    ],\n"
                            ")\n\n"
                            "ListView(\n"
                            "    children=[\n"
                            "        Container(height=20, child=Text('Variable')),\n"
                            "        Container(height=50, child=Text('Variable')),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListView clipBehavior",
                    description=(
                        "ListView clipBehavior=Clip.none allows overflowing items "
                        "to paint outside the list's bounds."
                    ),
                    instruction="The list items bleed outside the container because clipBehavior=Clip.none.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "clipBehavior=Clip.none",
                                style=TextStyle(
                                    fontSize=11, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                height=80.0,
                                width=300.0,
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=ListView(
                                    clipBehavior=Clip.none,
                                    shrinkWrap=True,
                                    children=[
                                        Container(
                                            height=40.0,
                                            color=Colors.red.withValues(
                                                alpha=0.15 + i * 0.1
                                            ),
                                            child=Center(
                                                child=Text(
                                                    f"Bleeds {i + 1}",
                                                    style=TextStyle(fontSize=12),
                                                ),
                                            ),
                                        )
                                        for i in range(6)
                                    ],
                                ),
                            ),
                            SizedBox(height=30),
                            Text(
                                "Items overflow the 80px container height.",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    height=80,\n"
                            "    child=ListView(\n"
                            "        clipBehavior=Clip.none,\n"
                            "        children=[\n"
                            "            Container(height=40, child=Text('Bleeds')),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomScrollView physics & anchor",
                    description=(
                        "CustomScrollView anchor offsets the zero scroll position. "
                        "anchor=0.5 centers the content, allowing scrolling in both directions."
                    ),
                    instruction="Content starts in the middle of the viewport. Scroll up or down to see items in both directions.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "anchor=0.5 (centered start)",
                                style=TextStyle(
                                    fontSize=11, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                height=200.0,
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=CustomScrollView(
                                    anchor=0.5,
                                    slivers=[
                                        SliverToBoxAdapter(
                                            child=Container(
                                                height=50.0,
                                                color=[
                                                    Colors.red,
                                                    Colors.orange,
                                                    Colors.green,
                                                    Colors.blue,
                                                    Colors.purple,
                                                    Colors.teal,
                                                    Colors.pink,
                                                ][i].withValues(alpha=0.3),
                                                child=Center(
                                                    child=Text(
                                                        f"Sliver {i + 1}",
                                                        style=TextStyle(fontSize=13),
                                                    ),
                                                ),
                                            ),
                                        )
                                        for i in range(7)
                                    ],
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CustomScrollView(\n"
                            "    anchor=0.5,\n"
                            "    slivers=[\n"
                            "        SliverToBoxAdapter(\n"
                            "            child=Container(height=50, child=Text('Item')),\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NotificationListener",
                    description=(
                        "Intercepts scroll notifications bubbling up from child "
                        "scrollables. Provides access to ScrollMetrics including pixels, "
                        "maxScrollExtent, scrollDelta, and overscroll values."
                    ),
                    instruction=(
                        "Scroll the list to see live event count, scroll position, "
                        "and the last notification type with delta or overscroll values."
                    ),
                    visible=_NotificationListenerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NotificationListener(\n"
                            "    onNotification=on_scroll,\n"
                            "    child=ListView(children=[...]),\n"
                            ")\n\n"
                            "def on_scroll(notification):\n"
                            "    m = notification.metrics\n"
                            "    pixels = m.pixels\n"
                            "    max_ext = m.maxScrollExtent\n"
                            "    return False"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AutomaticKeepAliveClientMixin",
                    description=(
                        "Mixin that prevents a StatefulWidget's state from being disposed "
                        "when scrolled off screen. Without it, ListView disposes items to "
                        "save memory, resetting any local state like tap counters."
                    ),
                    instruction=(
                        "Tap counters on items 0-2 in both lists, then scroll past item 20 "
                        "and back up. Left list (no mixin): counters reset. "
                        "Right list (with mixin): counters survive."
                    ),
                    visible=Container(
                        height=300.0,
                        child=Row(
                            children=[
                                Expanded(
                                    child=Column(
                                        crossAxisAlignment=CrossAxisAlignment.start,
                                        children=[
                                            Text(
                                                "No keep-alive",
                                                style=TextStyle(
                                                    fontSize=14,
                                                    fontWeight=FontWeight.bold,
                                                ),
                                            ),
                                            SizedBox(height=4),
                                            Expanded(
                                                child=ListView.builder(
                                                    itemCount=30,
                                                    itemBuilder=lambda ctx, i: _CounterItem(
                                                        index=i
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                SizedBox(width=16),
                                Expanded(
                                    child=Column(
                                        crossAxisAlignment=CrossAxisAlignment.start,
                                        children=[
                                            Text(
                                                "With keep-alive",
                                                style=TextStyle(
                                                    fontSize=14,
                                                    fontWeight=FontWeight.bold,
                                                    color=Colors.green,
                                                ),
                                            ),
                                            SizedBox(height=4),
                                            Expanded(
                                                child=ListView.builder(
                                                    itemCount=30,
                                                    itemBuilder=lambda ctx, i: _KeepAliveCounterItem(
                                                        index=i
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class ItemState(\n"
                            "    State['Item'],\n"
                            "    AutomaticKeepAliveClientMixin,\n"
                            "):\n"
                            "    def build(self, context):\n"
                            "        return Text('Kept alive')"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ScrollMetrics Detail",
                    description=(
                        "NotificationListener exposes ScrollMetrics on every scroll "
                        "event. Properties include axisDirection, extentBefore, "
                        "extentAfter, and outOfRange for detailed scroll tracking."
                    ),
                    instruction=(
                        "Scroll the list and watch the metrics panel update in real "
                        "time. extentBefore and extentAfter show how much content is "
                        "above and below the viewport. outOfRange indicates overscroll."
                    ),
                    visible=_ScrollMetricsDetailDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NotificationListener(\n"
                            "    onNotification=on_scroll,\n"
                            "    child=ListView(children=[...]),\n"
                            ")\n\n"
                            "def on_scroll(notification):\n"
                            "    m = notification.metrics\n"
                            "    m.axisDirection\n"
                            "    m.extentBefore\n"
                            "    m.extentAfter\n"
                            "    m.outOfRange\n"
                            "    return False"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile & CircleAvatar",
                    description=(
                        "ListTile provides a fixed-height row with leading, title, subtitle, "
                        "and trailing slots. CircleAvatar renders a circular badge, commonly used as the leading widget."
                    ),
                    instruction="A static demo showing two list items with avatars, selection state, and trailing icons.",
                    visible=Container(
                        width=500.0,
                        child=Column(
                            children=[
                                ListTile(
                                    leading=CircleAvatar(
                                        backgroundColor=Colors.blue,
                                        child=Text(
                                            "AB",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=14
                                            ),
                                        ),
                                    ),
                                    title=Text("Alice Brown"),
                                    subtitle=Text("Software Engineer"),
                                    trailing=Icon(Icons.chevron_right),
                                ),
                                ListTile(
                                    leading=CircleAvatar(
                                        backgroundColor=Colors.teal,
                                        child=Icon(Icons.person, color=Colors.white),
                                    ),
                                    title=Text("Bob Smith"),
                                    subtitle=Text("Designer"),
                                    trailing=Icon(Icons.chevron_right),
                                    selected=True,
                                    selectedTileColor=Color(0xFFE3F2FD),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    leading=CircleAvatar(\n"
                            "        backgroundColor=Colors.blue,\n"
                            "        child=Text('AB'),\n"
                            "    ),\n"
                            "    title=Text('Alice Brown'),\n"
                            "    subtitle=Text('Software Engineer'),\n"
                            "    trailing=Icon(Icons.chevron_right),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile shape & selectedColor",
                    description=(
                        "ListTile with RoundedRectangleBorder(borderRadius=20) and "
                        "selectedColor=Colors.green. Toggle selected to see the color change."
                    ),
                    instruction="Toggle the switch to see the selected state with green color.",
                    visible=_ListTileShapeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    shape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(20),\n"
                            "    ),\n"
                            "    selected=True,\n"
                            "    selectedColor=Colors.green,\n"
                            "    selectedTileColor=Color(0xFFE8F5E9),\n"
                            "    title=Text('Shaped ListTile'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile mouseCursor & colors",
                    description=(
                        "ListTile with custom mouseCursor, focusColor, hoverColor, "
                        "and splashColor for colorful interactions."
                    ),
                    instruction="Hover over the tile to see amber color, tap for red splash.",
                    visible=Container(
                        width=500.0,
                        child=ListTile(
                            title=Text("Custom colors"),
                            subtitle=Text("Hover and tap to see effects"),
                            mouseCursor=SystemMouseCursors.cell,
                            focusColor=Color(0xFFBBDEFB),
                            hoverColor=Color(0xFFFFF8E1),
                            splashColor=Color(0x33FF0000),
                            leading=Icon(Icons.palette, color=Colors.blue),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    title=Text('Custom colors'),\n"
                            "    mouseCursor=SystemMouseCursors.cell,\n"
                            "    focusColor=Color(0xFFBBDEFB),\n"
                            "    hoverColor=Color(0xFFFFF8E1),\n"
                            "    splashColor=Color(0x33FF0000),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile focusNode & enableFeedback",
                    description=(
                        "ListTile with autofocus=True and enableFeedback=False. "
                        "The tile starts focused."
                    ),
                    instruction="The tile should appear focused on load.",
                    visible=Container(
                        width=500.0,
                        child=ListTile(
                            title=Text("Auto-focused tile"),
                            subtitle=Text("enableFeedback=False"),
                            autofocus=True,
                            enableFeedback=False,
                            leading=Icon(Icons.center_focus_strong),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    title=Text('Auto-focused tile'),\n"
                            "    autofocus=True,\n"
                            "    enableFeedback=False,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile horizontalTitleGap & minTileHeight",
                    description=(
                        "Three ListTiles: default, horizontalTitleGap=0 (tight gap), "
                        "and minTileHeight=80 (tall tile)."
                    ),
                    instruction="Compare the spacing and height differences.",
                    visible=Container(
                        width=500.0,
                        child=Column(
                            children=[
                                ListTile(
                                    leading=Icon(Icons.looks_one),
                                    title=Text("Default gap"),
                                ),
                                ListTile(
                                    leading=Icon(Icons.looks_two),
                                    title=Text("horizontalTitleGap=0"),
                                    horizontalTitleGap=0,
                                ),
                                ListTile(
                                    leading=Icon(Icons.looks_3),
                                    title=Text("minTileHeight=80"),
                                    minTileHeight=80,
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    leading=Icon(Icons.looks_one),\n"
                            "    title=Text('Default gap'),\n"
                            ")\n\n"
                            "ListTile(\n"
                            "    leading=Icon(Icons.looks_two),\n"
                            "    title=Text('Tight gap'),\n"
                            "    horizontalTitleGap=0,\n"
                            ")\n\n"
                            "ListTile(\n"
                            "    leading=Icon(Icons.looks_3),\n"
                            "    title=Text('Tall tile'),\n"
                            "    minTileHeight=80,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile isThreeLine",
                    description=(
                        "ListTile with isThreeLine=True showing title, subtitle, "
                        "and extended body text for an expanded layout."
                    ),
                    instruction="Observe the three-line layout with extended subtitle.",
                    visible=Container(
                        width=500.0,
                        child=ListTile(
                            isThreeLine=True,
                            leading=CircleAvatar(
                                backgroundColor=Colors.indigo,
                                child=Text(
                                    "3L",
                                    style=TextStyle(color=Colors.white, fontSize=14),
                                ),
                            ),
                            title=Text("Three-line ListTile"),
                            subtitle=Text(
                                "This is an extended subtitle that spans multiple lines "
                                "to demonstrate the isThreeLine property which allows "
                                "the tile to accommodate more content."
                            ),
                            trailing=Icon(Icons.more_vert),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    isThreeLine=True,\n"
                            "    leading=CircleAvatar(\n"
                            "        child=Text('3L'),\n"
                            "    ),\n"
                            "    title=Text('Three-line ListTile'),\n"
                            "    subtitle=Text(\n"
                            "        'Extended subtitle that spans '\n"
                            "        'multiple lines...'\n"
                            "    ),\n"
                            "    trailing=Icon(Icons.more_vert),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListTile Advanced",
                    description=(
                        "ListTile supports dense mode, custom text styles, tileColor, "
                        "contentPadding, onLongPress, and enabled/disabled states."
                    ),
                    instruction="Tap the dense tile and long-press the second tile to see the log update below.",
                    visible=_ListTileAdvancedDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ListTile(\n"
                            "    leading=Icon(Icons.compress),\n"
                            "    title=Text('Dense tile'),\n"
                            "    dense=True,\n"
                            "    tileColor=Color(0xFFF5F5F5),\n"
                            "    onTap=on_tap,\n"
                            ")\n"
                            "\n"
                            "ListTile(\n"
                            "    title=Text('Disabled tile'),\n"
                            "    enabled=False,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CircleAvatar Radius & Colors",
                    description=(
                        "CircleAvatar supports fixed radius, or minRadius/maxRadius for "
                        "responsive sizing, plus custom background and foreground colors."
                    ),
                    instruction="Two avatars: one with fixed radius=30, one with minRadius=15 / maxRadius=40.",
                    visible=Row(
                        children=[
                            CircleAvatar(
                                radius=30,
                                backgroundColor=Colors.blue,
                                foregroundColor=Colors.white,
                                child=Icon(Icons.person),
                            ),
                            SizedBox(width=12),
                            CircleAvatar(
                                minRadius=15,
                                maxRadius=40,
                                backgroundColor=Colors.teal,
                                foregroundColor=Colors.white,
                                child=Text("SM"),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CircleAvatar(\n"
                            "    radius=30,\n"
                            "    backgroundColor=Colors.blue,\n"
                            "    foregroundColor=Colors.white,\n"
                            "    child=Icon(Icons.person),\n"
                            ")\n"
                            "\n"
                            "CircleAvatar(\n"
                            "    minRadius=15, maxRadius=40,\n"
                            "    backgroundColor=Colors.teal,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
