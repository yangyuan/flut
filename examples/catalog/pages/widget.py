import threading
import time

from utils import CODE_FONT_FAMILY
from flut.dart import Color, Brightness
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
    GestureDetector,
    GlobalKey,
    Overlay,
    OverlayEntry,
    InheritedWidget,
    SingleChildScrollView,
    WidgetState,
    WidgetStateColor,
    Builder,
    ListenableBuilder,
    ValueListenableBuilder,
    ExpansibleController,
    Padding,
    Center,
    Stack,
    Positioned,
    Visibility,
    IgnorePointer,
    ScrollController,
    ScrollbarOrientation,
)
from flut.flutter.material import Colors, ElevatedButton, Scrollbar
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.foundation import ValueNotifier, ValueKey, UniqueKey
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    Border,
    Alignment,
)
from flut.dart.ui import Offset, Clip, Radius
from flut.dart import Matrix4
from flut.flutter.widgets import InteractiveViewer, PanAxis
from flut.flutter.widgets.interactive_viewer import TransformationController
from flut.flutter.material import ExpansionTile, ListTile, ListTileControlAffinity
from flut.flutter.material import AppBar, Scaffold, Checkbox, Theme
from flut.flutter.material.theme_data import VisualDensity
from flut.flutter.painting import RoundedRectangleBorder

from widgets import CatalogPage, CodeArea, SplitViewTile


class _LogController:
    def __init__(self):
        self.lines = []
        self._notify = None

    def log(self, text):
        self.lines.append(text)
        if self._notify:
            self._notify()

    def clear(self):
        self.lines.clear()
        if self._notify:
            self._notify()


class _LogPanel(StatefulWidget):
    def __init__(self, *, controller, placeholder="", key=None):
        super().__init__(key=key)
        self.controller = controller
        self.placeholder = placeholder

    def createState(self):
        return _LogPanelState()


class _LogPanelState(State[_LogPanel]):
    def initState(self):
        self.widget.controller._notify = lambda: self.setState(lambda: None)

    def didUpdateWidget(self, oldWidget):
        if oldWidget.controller is not self.widget.controller:
            if oldWidget.controller._notify is not None:
                oldWidget.controller._notify = None
            self.widget.controller._notify = lambda: self.setState(lambda: None)

    def dispose(self):
        if self.widget.controller._notify is not None:
            self.widget.controller._notify = None

    def build(self, context):
        ctrl = self.widget.controller
        if not ctrl.lines:
            return Text(
                self.widget.placeholder,
                style=TextStyle(fontSize=13, color=Colors.grey),
            )
        children = [
            Text(line, style=TextStyle(fontSize=14, fontFamily=CODE_FONT_FAMILY))
            for line in ctrl.lines
        ]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=children,
        )


class _GlobalKeyMeasureDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _GlobalKeyMeasureDemoState()


class _GlobalKeyMeasureDemoState(State[_GlobalKeyMeasureDemo]):

    def initState(self):
        self.box_key = GlobalKey(debugLabel="measured-box")

    def _measure(self):
        ctrl = self.widget.controller
        ctrl.clear()
        ctx = self.box_key.currentContext
        if ctx is None:
            ctrl.log("No context (widget not mounted)")
            return
        render_box = ctx.findRenderObject()
        if render_box is None:
            ctrl.log("No render object")
            return
        size = render_box.size
        pos = render_box.localToGlobal(Offset(0, 0))
        ctrl.log(f"Size: {size.width:.0f} x {size.height:.0f}")
        ctrl.log(f"Position: ({pos.dx:.0f}, {pos.dy:.0f})")

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    key=self.box_key,
                    width=200.0,
                    height=100.0,
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=Container(
                        alignment=Alignment.center,
                        child=Text(
                            "Measured Box",
                            style=TextStyle(
                                color=Colors.white, fontWeight=FontWeight.bold
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                ElevatedButton(
                    onPressed=self._measure,
                    child=Text("Measure Size & Position"),
                ),
            ],
        )


class _CurrentWidgetDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _CurrentWidgetDemoState()


class _CurrentWidgetDemoState(State[_CurrentWidgetDemo]):

    def initState(self):
        self.widget_key = GlobalKey(debugLabel="tracked-widget")

    def _read_current_widget(self):
        ctrl = self.widget.controller
        ctrl.clear()
        widget = self.widget_key.currentWidget
        if widget is not None:
            ctrl.log(f"type: {type(widget).__name__}")
            ctrl.log(f"width: {widget.width}")
            ctrl.log(f"height: {widget.height}")
        else:
            ctrl.log("currentWidget: None (unmounted)")

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    key=self.widget_key,
                    width=180.0,
                    height=60.0,
                    decoration=BoxDecoration(
                        color=Colors.orange,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Container(
                        alignment=Alignment.center,
                        child=Text(
                            "Tracked Widget",
                            style=TextStyle(
                                color=Colors.white, fontWeight=FontWeight.bold
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                ElevatedButton(
                    onPressed=self._read_current_widget,
                    child=Text("Read currentWidget"),
                ),
            ],
        )


class _GlobalKeyStatefulDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _GlobalKeyStatefulDemoState()


class _GlobalKeyStatefulDemoState(State[_GlobalKeyStatefulDemo]):

    def initState(self):
        self.key_for_counter = GlobalKey(debugLabel="counter-widget")

    def _read_counter_state(self):
        ctrl = self.widget.controller
        ctrl.clear()
        state = self.key_for_counter.currentState
        if state is not None:
            count = getattr(state, "count", "?")
            ctrl.log(f"Counter State.count = {count}")
        else:
            ctrl.log("currentState: None")

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                _CounterWidget(key=self.key_for_counter),
                SizedBox(height=8),
                ElevatedButton(
                    onPressed=self._read_counter_state,
                    child=Text("Read Counter State"),
                ),
            ],
        )


class _CounterWidget(StatefulWidget):
    def createState(self):
        return _CounterWidgetState()


class _CounterWidgetState(State[_CounterWidget]):

    def initState(self):
        self.count = 0

    def _increment(self):
        self.setState(lambda: setattr(self, "count", self.count + 1))

    def build(self, context):
        return GestureDetector(
            onTap=self._increment,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                decoration=BoxDecoration(
                    color=Colors.teal,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Text(
                    f"Counter: {self.count} (tap to increment)",
                    style=TextStyle(color=Colors.white, fontSize=14),
                ),
            ),
        )


class _KeyDemoChild(StatefulWidget):
    def __init__(self, label, color, key=None):
        super().__init__(key=key)
        self.label = label
        self.color = color

    def createState(self):
        return _KeyDemoChildState()


class _KeyDemoChildState(State["_KeyDemoChild"]):

    def initState(self):
        self.tap_count = 0

    def _increment(self):
        self.tap_count += 1
        self.setState(lambda: None)

    def build(self, context):
        w = self.widget
        return GestureDetector(
            onTap=self._increment,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=10),
                decoration=BoxDecoration(
                    color=w.color,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Text(
                    f"{w.label}: {self.tap_count}",
                    style=TextStyle(color=Colors.white, fontSize=13),
                ),
            ),
        )


class _KeyEffectsDemo(StatefulWidget):
    def createState(self):
        return _KeyEffectsDemoState()


class _KeyEffectsDemoState(State["_KeyEffectsDemo"]):

    def initState(self):
        self.key_reversed = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Reverse Order"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "key_reversed", not self.key_reversed)
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "With ValueKey (state follows widget):",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                _key_demo_row(self.key_reversed, use_value_key=True),
                SizedBox(height=8),
                Text(
                    "With UniqueKey (state resets on rebuild):",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                _key_demo_row(self.key_reversed, use_value_key=False),
            ],
        )


class _OverlayDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _OverlayDemoState()


class _OverlayDemoState(State[_OverlayDemo]):

    def initState(self):
        self.entry = None
        self.is_showing = False

    def _show_overlay(self):
        if self.is_showing:
            return

        def build_overlay(ctx):
            return Container(
                alignment=Alignment.center,
                color=Color(0x88000000),
                child=GestureDetector(
                    onTap=self._hide_overlay,
                    child=Container(
                        width=250.0,
                        height=150.0,
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=Column(
                            mainAxisAlignment=MainAxisAlignment.center,
                            children=[
                                Text(
                                    "Overlay Content",
                                    style=TextStyle(
                                        fontSize=18,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                SizedBox(height=8),
                                Text(
                                    "Tap to dismiss",
                                    style=TextStyle(fontSize=13, color=Colors.grey),
                                ),
                            ],
                        ),
                    ),
                ),
            )

        self.entry = OverlayEntry(builder=build_overlay)
        overlay = Overlay.of(self._last_context)
        overlay.insert(self.entry)
        self.is_showing = True
        self.widget.controller.log("Overlay inserted")
        self.setState(lambda: None)

    def _hide_overlay(self):
        if self.entry is not None and self.is_showing:
            self.entry.remove()
            self.is_showing = False
            self.widget.controller.log("Overlay removed")
            self.setState(lambda: None)

    def build(self, context):
        self._last_context = context
        return ElevatedButton(
            onPressed=self._show_overlay,
            child=Text("Showing..." if self.is_showing else "Show Overlay"),
        )


class _MyTheme(InheritedWidget):
    def __init__(self, *, color, child, key=None):
        super().__init__(child=child, key=key)
        self.color = color

    def updateShouldNotify(self, old_widget):
        return self.color != old_widget.color

    @staticmethod
    def of(context):
        return InheritedWidget._of(context, "_MyTheme")


class _MyLocale(InheritedWidget):
    def __init__(self, *, locale, child, key=None):
        super().__init__(child=child, key=key)
        self.locale = locale

    def updateShouldNotify(self, old_widget):
        return self.locale != old_widget.locale

    @staticmethod
    def of(context):
        return InheritedWidget._of(context, "_MyLocale")


class _InheritedConsumer(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _InheritedConsumerState()


class _InheritedConsumerState(State[_InheritedConsumer]):
    def initState(self):
        self.build_count = 0

    def build(self, context):
        self.build_count += 1
        ctrl = self.widget.controller
        theme = _MyTheme.of(context)
        locale = _MyLocale.of(context)
        theme_color = theme.color if theme else "?"
        locale_val = locale.locale if locale else "?"
        ctrl.clear()
        ctrl.log(f"Theme color: {theme_color}")
        ctrl.log(f"Locale: {locale_val}")
        ctrl.log(f"Build count: {self.build_count}")
        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Color(0xFFE3F2FD),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(f"Theme color: {theme_color}", style=TextStyle(fontSize=14)),
                    Text(f"Locale: {locale_val}", style=TextStyle(fontSize=14)),
                    Text(
                        f"Build count: {self.build_count}",
                        style=TextStyle(
                            fontSize=12, color=Colors.grey, fontFamily=CODE_FONT_FAMILY
                        ),
                    ),
                ],
            ),
        )


class _InheritedWidgetDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _InheritedWidgetDemoState()


class _InheritedWidgetDemoState(State[_InheritedWidgetDemo]):
    def initState(self):
        self.color_index = 0
        self.locale_index = 0
        self.colors = ["blue", "red", "green", "purple"]
        self.locales = ["en", "fr", "de", "ja"]

    def _next_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.setState(lambda: None)

    def _next_locale(self):
        self.locale_index = (self.locale_index + 1) % len(self.locales)
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._next_color,
                            child=Text(f"Theme: {self.colors[self.color_index]}"),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._next_locale,
                            child=Text(f"Locale: {self.locales[self.locale_index]}"),
                        ),
                    ],
                ),
                SizedBox(height=12),
                _MyTheme(
                    color=self.colors[self.color_index],
                    child=_MyLocale(
                        locale=self.locales[self.locale_index],
                        child=_InheritedConsumer(controller=self.widget.controller),
                    ),
                ),
            ],
        )


class _RedCounter(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _RedCounterState()


class _RedCounterState(State[_RedCounter]):
    def initState(self):
        self.count = 0
        self.widget.controller.log("[Red] initState")

    def dispose(self):
        self.widget.controller.log("[Red] dispose")

    def _bump(self):
        self.setState(lambda: setattr(self, "count", self.count + 1))

    def build(self, context):
        return GestureDetector(
            onTap=self._bump,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=10),
                decoration=BoxDecoration(
                    color=Colors.red,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Text(
                    f"Red counter: {self.count} (+1 per tap)",
                    style=TextStyle(color=Colors.white, fontSize=14),
                ),
            ),
        )


class _BlueCounter(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _BlueCounterState()


class _BlueCounterState(State[_BlueCounter]):
    def initState(self):
        self.count = 0
        self.widget.controller.log("[Blue] initState")

    def dispose(self):
        self.widget.controller.log("[Blue] dispose")

    def _bump(self):
        self.setState(lambda: setattr(self, "count", self.count + 5))

    def build(self, context):
        return GestureDetector(
            onTap=self._bump,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=10),
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Text(
                    f"Blue counter: {self.count} (+5 per tap)",
                    style=TextStyle(color=Colors.white, fontSize=14),
                ),
            ),
        )


class _ClassIdentityStatefulDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _ClassIdentityStatefulDemoState()


class _ClassIdentityStatefulDemoState(State[_ClassIdentityStatefulDemo]):
    def initState(self):
        self.use_red = True

    def _toggle(self):
        self.widget.controller.clear()
        self.setState(lambda: setattr(self, "use_red", not self.use_red))

    def build(self, context):
        slot = (
            _RedCounter(controller=self.widget.controller)
            if self.use_red
            else _BlueCounter(controller=self.widget.controller)
        )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=self._toggle,
                    child=Text("Swap class in slot"),
                ),
                SizedBox(height=8),
                slot,
            ],
        )


class _StatelessProbeA(StatelessWidget):
    def __init__(self, *, child, key=None):
        super().__init__(key=key)
        self._child = child

    def build(self, context):
        return Container(
            padding=EdgeInsets.all(8),
            decoration=BoxDecoration(
                color=Color(0xFFFCE4EC),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        "Wrapper class: _StatelessProbeA",
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    ),
                    SizedBox(height=6),
                    self._child,
                ],
            ),
        )


class _StatelessProbeB(StatelessWidget):
    def __init__(self, *, child, key=None):
        super().__init__(key=key)
        self._child = child

    def build(self, context):
        return Container(
            padding=EdgeInsets.all(8),
            decoration=BoxDecoration(
                color=Color(0xFFE0F7FA),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        "Wrapper class: _StatelessProbeB",
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    ),
                    SizedBox(height=6),
                    self._child,
                ],
            ),
        )


class _ClassIdentityStatelessDemo(StatefulWidget):
    def createState(self):
        return _ClassIdentityStatelessDemoState()


class _ClassIdentityStatelessDemoState(State[_ClassIdentityStatelessDemo]):
    def initState(self):
        self.use_a = True

    def _toggle(self):
        self.setState(lambda: setattr(self, "use_a", not self.use_a))

    def build(self, context):
        inner = _CounterWidget(key=ValueKey("identity-stateless-counter"))
        wrapper = (
            _StatelessProbeA(child=inner)
            if self.use_a
            else _StatelessProbeB(child=inner)
        )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=self._toggle,
                    child=Text("Swap stateless wrapper class"),
                ),
                SizedBox(height=8),
                wrapper,
                SizedBox(height=6),
                Text(
                    "Counter has a stable ValueKey, but its State resets on every "
                    "swap because the wrapper class — and therefore the parent "
                    "Element — is replaced.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _AlphaScope(InheritedWidget):
    def __init__(self, *, value, child, key=None):
        super().__init__(child=child, key=key)
        self.value = value

    def updateShouldNotify(self, old_widget):
        return self.value != old_widget.value

    @staticmethod
    def of(context):
        return InheritedWidget._of(context, "_AlphaScope")


class _BetaScope(InheritedWidget):
    def __init__(self, *, value, child, key=None):
        super().__init__(child=child, key=key)
        self.value = value

    def updateShouldNotify(self, old_widget):
        return self.value != old_widget.value

    @staticmethod
    def of(context):
        return InheritedWidget._of(context, "_BetaScope")


class _ScopeReader(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _ScopeReaderState()


class _ScopeReaderState(State[_ScopeReader]):
    def build(self, context):
        ctrl = self.widget.controller
        ctrl.clear()
        alpha = _AlphaScope.of(context)
        beta = _BetaScope.of(context)
        ctrl.log("_AlphaScope.of(context) = " + (str(alpha.value) if alpha else "None"))
        ctrl.log("_BetaScope.of(context) = " + (str(beta.value) if beta else "None"))
        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Color(0xFFF3E5F5),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Text(
                "Reader rebuilt — check log",
                style=TextStyle(fontSize=13),
            ),
        )


class _ClassIdentityInheritedDemo(StatefulWidget):
    def __init__(self, *, controller, key=None):
        super().__init__(key=key)
        self.controller = controller

    def createState(self):
        return _ClassIdentityInheritedDemoState()


class _ClassIdentityInheritedDemoState(State[_ClassIdentityInheritedDemo]):
    def initState(self):
        self.use_alpha = True
        self.tick = 0

    def _toggle_class(self):
        self.tick += 1
        self.setState(lambda: setattr(self, "use_alpha", not self.use_alpha))

    def _bump_value(self):
        self.tick += 1
        self.setState(lambda: None)

    def build(self, context):
        reader = _ScopeReader(controller=self.widget.controller)
        if self.use_alpha:
            scope = _AlphaScope(value=f"alpha-{self.tick}", child=reader)
        else:
            scope = _BetaScope(value=f"beta-{self.tick}", child=reader)
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._toggle_class,
                            child=Text("Swap InheritedWidget class"),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._bump_value,
                            child=Text("Bump value"),
                        ),
                    ],
                ),
                SizedBox(height=8),
                scope,
            ],
        )


class _VisibilityMaintainDemo(StatefulWidget):
    def createState(self):
        return _VisibilityMaintainDemoState()


class _VisibilityMaintainDemoState(State[_VisibilityMaintainDemo]):
    def initState(self):
        self.vis_maintained = True

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle maintainState"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "vis_maintained", not self.vis_maintained
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            "visible" if self.vis_maintained else "hidden (space kept)"
                        ),
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        Container(
                            width=120.0,
                            height=60.0,
                            color=Colors.grey,
                            child=Center(child=Text("Before")),
                        ),
                        SizedBox(width=8),
                        Visibility(
                            visible=self.vis_maintained,
                            maintainState=True,
                            maintainAnimation=True,
                            maintainSize=True,
                            child=Container(
                                width=120.0,
                                height=60.0,
                                color=Colors.orange,
                                child=Center(
                                    child=Text(
                                        "Maintained",
                                        style=TextStyle(color=Colors.white),
                                    )
                                ),
                            ),
                        ),
                        SizedBox(width=8),
                        Container(
                            width=120.0,
                            height=60.0,
                            color=Colors.grey,
                            child=Center(child=Text("After")),
                        ),
                    ],
                ),
            ],
        )


class _VisibilityReplacementDemo(StatefulWidget):
    def createState(self):
        return _VisibilityReplacementDemoState()


class _VisibilityReplacementDemoState(State[_VisibilityReplacementDemo]):
    def initState(self):
        self.vis_replaced = True

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle replacement"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "vis_replaced", not self.vis_replaced)
                    ),
                ),
                SizedBox(height=12),
                Visibility(
                    visible=self.vis_replaced,
                    replacement=Container(
                        width=200.0,
                        height=60.0,
                        color=Colors.red,
                        child=Center(
                            child=Text(
                                "I'm the replacement!",
                                style=TextStyle(color=Colors.white),
                            )
                        ),
                    ),
                    child=Container(
                        width=200.0,
                        height=60.0,
                        color=Colors.green,
                        child=Center(
                            child=Text(
                                "I'm the original",
                                style=TextStyle(color=Colors.white),
                            )
                        ),
                    ),
                ),
            ],
        )


class _VisibilityOfDemo(StatefulWidget):
    def createState(self):
        return _VisibilityOfDemoState()


class _VisibilityOfDemoState(State[_VisibilityOfDemo]):
    def initState(self):
        self.show_child = True

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle nearest Visibility"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show_child", not self.show_child)
                    ),
                ),
                SizedBox(height=12),
                Visibility(
                    visible=self.show_child,
                    replacement=Builder(
                        builder=lambda ctx: Container(
                            width=260.0,
                            padding=EdgeInsets.all(12),
                            decoration=BoxDecoration(
                                color=Color(0xFFFFEBEE),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text(
                                f"Visibility.of(context) = {Visibility.of(ctx)}",
                                style=TextStyle(fontSize=14),
                            ),
                        )
                    ),
                    child=Builder(
                        builder=lambda ctx: Container(
                            width=260.0,
                            padding=EdgeInsets.all(12),
                            decoration=BoxDecoration(
                                color=Color(0xFFE8F5E9),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text(
                                f"Visibility.of(context) = {Visibility.of(ctx)}",
                                style=TextStyle(fontSize=14),
                            ),
                        )
                    ),
                ),
            ],
        )


class _InteractiveViewerCallbacksDemo(StatefulWidget):
    def createState(self):
        return _InteractiveViewerCallbacksDemoState()


class _InteractiveViewerCallbacksDemoState(State[_InteractiveViewerCallbacksDemo]):
    def initState(self):
        self.status = "Idle"
        self.scale = 1.0
        self.rotation = 0.0
        self.focal_point = ""
        self.velocity = ""

    def _on_start(self, details):
        def update():
            self.status = "Started"
            self.focal_point = (
                f"({details.focalPoint.dx:.1f}, {details.focalPoint.dy:.1f})"
            )

        self.setState(update)

    def _on_update(self, details):
        def update():
            self.status = "Updating"
            self.scale = details.scale
            self.rotation = details.rotation
            self.focal_point = (
                f"({details.focalPoint.dx:.1f}, {details.focalPoint.dy:.1f})"
            )

        self.setState(update)

    def _on_end(self, details):
        def update():
            self.status = "Ended"
            self.velocity = f"({details.velocity.pixelsPerSecond.dx:.1f}, {details.velocity.pixelsPerSecond.dy:.1f})"

        self.setState(update)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=350.0,
                    height=200.0,
                    decoration=BoxDecoration(
                        color=Color(0xFFE0E0E0),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=InteractiveViewer(
                        boundaryMargin=EdgeInsets.all(50),
                        minScale=0.5,
                        maxScale=4.0,
                        onInteractionStart=self._on_start,
                        onInteractionUpdate=self._on_update,
                        onInteractionEnd=self._on_end,
                        child=Container(
                            width=300.0,
                            height=300.0,
                            decoration=BoxDecoration(
                                color=Colors.deepPurple,
                                borderRadius=BorderRadius.circular(16),
                            ),
                            child=Container(
                                alignment=Alignment.center,
                                child=Text(
                                    "Drag / Pinch me",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontSize=18,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(10),
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                f"Status: {self.status}",
                                style=TextStyle(
                                    fontSize=14, fontWeight=FontWeight.bold
                                ),
                            ),
                            Text(
                                f"Focal Point: {self.focal_point}",
                                style=TextStyle(fontSize=13),
                            ),
                            Text(
                                f"Scale: {self.scale:.2f}", style=TextStyle(fontSize=13)
                            ),
                            Text(
                                f"Rotation: {self.rotation:.4f}",
                                style=TextStyle(fontSize=13),
                            ),
                            Text(
                                f"End Velocity: {self.velocity}",
                                style=TextStyle(fontSize=13),
                            ),
                        ],
                    ),
                ),
            ],
        )


class _InteractiveViewerControllerDemo(StatefulWidget):
    def createState(self):
        return _InteractiveViewerControllerDemoState()


class _InteractiveViewerControllerDemoState(State[_InteractiveViewerControllerDemo]):
    def initState(self):
        self.controller = TransformationController(Matrix4.identity())
        self.matrix_text = "Identity"

    def _update_matrix_text(self):
        m = self.controller.value
        if m is not None:
            s = m._storage
            self.matrix_text = (
                f"[{s[0]:.2f}, {s[4]:.2f}, {s[12]:.2f}]\n"
                f"[{s[1]:.2f}, {s[5]:.2f}, {s[13]:.2f}]\n"
                f"[{s[3]:.2f}, {s[7]:.2f}, {s[15]:.2f}]"
            )
        else:
            self.matrix_text = "None"

    def _reset(self):
        def update():
            self.controller.value = Matrix4.identity()
            self._update_matrix_text()

        self.setState(update)

    def _zoom_in(self):
        def update():
            self.controller.value = Matrix4.diagonal3Values(2.0, 2.0, 1.0)
            self._update_matrix_text()

        self.setState(update)

    def _zoom_out(self):
        def update():
            self.controller.value = Matrix4.diagonal3Values(0.5, 0.5, 1.0)
            self._update_matrix_text()

        self.setState(update)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=350.0,
                    height=200.0,
                    decoration=BoxDecoration(
                        color=Color(0xFFE0E0E0),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=InteractiveViewer(
                        transformationController=self.controller,
                        clipBehavior=Clip.hardEdge,
                        boundaryMargin=EdgeInsets.all(80),
                        minScale=0.2,
                        maxScale=5.0,
                        onInteractionEnd=lambda d: self.setState(
                            lambda: self._update_matrix_text()
                        ),
                        child=Container(
                            width=400.0,
                            height=400.0,
                            decoration=BoxDecoration(
                                color=Colors.indigo,
                                borderRadius=BorderRadius.circular(16),
                            ),
                            child=Container(
                                alignment=Alignment.center,
                                child=Text(
                                    "Zoomable Content",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontSize=20,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=10),
                Row(
                    children=[
                        ElevatedButton(onPressed=self._reset, child=Text("Reset")),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._zoom_in, child=Text("Zoom In 2x")
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._zoom_out, child=Text("Zoom Out 0.5x")
                        ),
                    ],
                ),
                SizedBox(height=10),
                Container(
                    padding=EdgeInsets.all(10),
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Text(
                        f"Transform Matrix:\n{self.matrix_text}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                ),
            ],
        )


class _ExpansionTileShapeDemo(StatefulWidget):
    def createState(self):
        return _ExpansionTileShapeDemoState()


class _ExpansionTileShapeDemoState(State[_ExpansionTileShapeDemo]):
    def initState(self):
        self.expanded_a = False
        self.expanded_b = False
        self.expanded_c = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=350.0,
                    child=ExpansionTile(
                        title=Text("Default Shape"),
                        subtitle=Text("No custom shape set"),
                        onExpansionChanged=lambda v: self.setState(
                            lambda: setattr(self, "expanded_a", v)
                        ),
                        initiallyExpanded=self.expanded_a,
                        children=[
                            Container(
                                padding=EdgeInsets.all(16),
                                child=Text(
                                    "Default ExpansionTile content. Uses standard shape and trailing arrow."
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=12),
                Container(
                    width=350.0,
                    child=ExpansionTile(
                        title=Text("Rounded Shape"),
                        subtitle=Text("borderRadius changes on expand"),
                        shape=RoundedRectangleBorder(
                            borderRadius=BorderRadius.circular(16)
                        ),
                        collapsedShape=RoundedRectangleBorder(
                            borderRadius=BorderRadius.circular(4)
                        ),
                        backgroundColor=Color(0xFFE8F5E9),
                        collapsedBackgroundColor=Color(0xFFF1F8E9),
                        onExpansionChanged=lambda v: self.setState(
                            lambda: setattr(self, "expanded_b", v)
                        ),
                        initiallyExpanded=self.expanded_b,
                        children=[
                            Container(
                                padding=EdgeInsets.all(16),
                                child=Text(
                                    "Expanded with borderRadius=16. Collapsed uses borderRadius=4."
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=12),
                Container(
                    width=350.0,
                    child=ExpansionTile(
                        title=Text("Compact + Leading Arrow"),
                        subtitle=Text("clipBehavior + controlAffinity + visualDensity"),
                        clipBehavior=Clip.antiAlias,
                        controlAffinity=ListTileControlAffinity.leading,
                        visualDensity=VisualDensity.compact,
                        backgroundColor=Color(0xFFE3F2FD),
                        collapsedBackgroundColor=Color(0xFFE8EAF6),
                        onExpansionChanged=lambda v: self.setState(
                            lambda: setattr(self, "expanded_c", v)
                        ),
                        initiallyExpanded=self.expanded_c,
                        children=[
                            Container(
                                padding=EdgeInsets.all(16),
                                child=Text(
                                    "Arrow is on the left (leading). VisualDensity is compact. clipBehavior=Clip.antiAlias."
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )


CONSTRAINTS = [
    ("WidgetState.hovered", WidgetState.hovered),
    ("WidgetState.focused", WidgetState.focused),
    ("WidgetState.pressed", WidgetState.pressed),
    ("WidgetState.dragged", WidgetState.dragged),
    ("WidgetState.selected", WidgetState.selected),
    ("WidgetState.scrolledUnder", WidgetState.scrolledUnder),
    ("WidgetState.disabled", WidgetState.disabled),
    ("WidgetState.error", WidgetState.error),
    (
        "WidgetState.hovered & WidgetState.focused",
        WidgetState.hovered & WidgetState.focused,
    ),
    (
        "WidgetState.hovered | WidgetState.focused",
        WidgetState.hovered | WidgetState.focused,
    ),
    ("~WidgetState.disabled", ~WidgetState.disabled),
    ("WidgetState.any", WidgetState.any),
]


class _WidgetStateDemo(StatefulWidget):
    def createState(self):
        return _WidgetStateDemoState()


class _WidgetStateDemoState(State[_WidgetStateDemo]):

    def initState(self):
        self.active_states = set()

    def _toggle_state(self, state):
        def toggle(v):
            new_states = set(self.active_states)
            if v:
                new_states.add(state)
            else:
                new_states.discard(state)
            self.setState(lambda: setattr(self, "active_states", new_states))

        return toggle

    def build(self, context):
        all_states = [
            WidgetState.hovered,
            WidgetState.focused,
            WidgetState.pressed,
            WidgetState.dragged,
            WidgetState.selected,
            WidgetState.scrolledUnder,
            WidgetState.disabled,
            WidgetState.error,
        ]

        state_toggles = []
        for state in all_states:
            state_toggles.append(
                Row(
                    children=[
                        Checkbox(
                            value=state in self.active_states,
                            onChanged=self._toggle_state(state),
                        ),
                        Text(state._flut_value, style=TextStyle(fontSize=13)),
                    ],
                )
            )

        constraint_rows = []
        for label, constraint in CONSTRAINTS:
            matched = constraint.isSatisfiedBy(self.active_states)
            constraint_rows.append(
                Container(
                    padding=EdgeInsets.symmetric(horizontal=12, vertical=8),
                    decoration=BoxDecoration(
                        color=Color(0xFFC8E6C9) if matched else Color(0xFFFFCDD2),
                        borderRadius=BorderRadius.circular(6),
                    ),
                    child=Row(
                        children=[
                            Text(
                                "MATCH" if matched else "NO",
                                style=TextStyle(
                                    fontSize=12,
                                    fontWeight=FontWeight.bold,
                                    color=(
                                        Color(0xFF2E7D32)
                                        if matched
                                        else Color(0xFFC62828)
                                    ),
                                ),
                            ),
                            SizedBox(width=12),
                            Text(
                                label,
                                style=TextStyle(
                                    fontSize=13, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                        ],
                    ),
                )
            )
            constraint_rows.append(SizedBox(height=6))

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=state_toggles[:4],
                        ),
                        SizedBox(width=24),
                        Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=state_toggles[4:],
                        ),
                    ],
                ),
                SizedBox(height=20),
                Text(
                    "Constraint Results",
                    style=TextStyle(fontSize=16, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=8),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=constraint_rows,
                ),
            ],
        )


class _ScrolledUnderDemo(StatelessWidget):
    def build(self, context):
        scrollable_list = []
        for i in range(20):
            scrollable_list.append(
                Container(
                    padding=EdgeInsets.symmetric(horizontal=16, vertical=12),
                    child=Text(f"List item {i + 1}", style=TextStyle(fontSize=14)),
                ),
            )

        return Container(
            height=250.0,
            decoration=BoxDecoration(
                borderRadius=BorderRadius.circular(8),
            ),
            child=Scaffold(
                appBar=AppBar(
                    title=Text(
                        "Scroll to see color change",
                        style=TextStyle(fontSize=14),
                    ),
                    backgroundColor=WidgetStateColor.fromMap(
                        {
                            WidgetState.scrolledUnder: Color(0xFFE3F2FD),
                            WidgetState.any: Colors.white,
                        }
                    ),
                    surfaceTintColor=Colors.transparent,
                    elevation=0.0,
                    scrolledUnderElevation=2.0,
                ),
                body=SingleChildScrollView(
                    child=Column(children=scrollable_list),
                ),
            ),
        )


class _SetStateDemo(StatefulWidget):
    def createState(self):
        return _SetStateDemoState()


class _SetStateDemoState(State[_SetStateDemo]):

    def initState(self):
        self.counter = 0
        self.last_method = ""
        self.callback_ran = False

    def _make_button(self, label, on_tap, color=None):
        return GestureDetector(
            onTap=on_tap,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                decoration=BoxDecoration(
                    color=color or Colors.blue,
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Text(
                    label,
                    style=TextStyle(color=Colors.white, fontSize=13),
                ),
            ),
        )

    def _increment_with_lambda(self):
        self.callback_ran = False
        self.setState(
            lambda: (
                setattr(self, "counter", self.counter + 1),
                setattr(self, "last_method", "setState(lambda: ...)"),
                setattr(self, "callback_ran", True),
            )
        )

    def _increment_with_none(self):
        self.callback_ran = False
        self.counter += 1
        self.last_method = "setState(None)"
        self.setState(None)

    def _increment_with_fn(self):
        self.callback_ran = False

        def update():
            self.counter += 1
            self.last_method = "setState(update)"
            self.callback_ran = True

        self.setState(update)

    def _reset_counter(self):
        self.setState(
            lambda: (
                setattr(self, "counter", 0),
                setattr(self, "last_method", ""),
                setattr(self, "callback_ran", False),
            )
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(f"Counter: {self.counter}", style=TextStyle(fontSize=16)),
                SizedBox(height=4),
                Text(
                    (
                        f"via: {self.last_method}"
                        if self.last_method
                        else "Click a button"
                    ),
                    style=TextStyle(
                        fontSize=13, fontFamily=CODE_FONT_FAMILY, color=Colors.grey
                    ),
                ),
                SizedBox(height=4),
                Text(
                    f"callback executed: {self.callback_ran}",
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.green if self.callback_ran else Color(0xFFFF9800),
                    ),
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        self._make_button("Lambda", self._increment_with_lambda),
                        SizedBox(width=8),
                        self._make_button("None", self._increment_with_none),
                        SizedBox(width=8),
                        self._make_button("Function", self._increment_with_fn),
                        SizedBox(width=8),
                        self._make_button(
                            "Reset", self._reset_counter, color=Colors.grey
                        ),
                    ],
                ),
            ],
        )


class _BackgroundSetStateDemo(StatefulWidget):
    def createState(self):
        return _BackgroundSetStateDemoState()


class _BackgroundSetStateDemoState(State[_BackgroundSetStateDemo]):

    def initState(self):
        self.thread_counter = 0
        self.thread_name = ""
        self.bg_running = False

    def _make_button(self, label, on_tap, color=None):
        return GestureDetector(
            onTap=on_tap,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                decoration=BoxDecoration(
                    color=color or Colors.blue,
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Text(
                    label,
                    style=TextStyle(color=Colors.white, fontSize=13),
                ),
            ),
        )

    def _start_background_counter(self):
        if self.bg_running:
            return

        def bg_work():
            for i in range(5):
                time.sleep(1)

                def update():
                    self.thread_counter += 1
                    self.thread_name = threading.current_thread().name

                self.setState(update)

            def done():
                self.bg_running = False

            self.setState(done)

        self.bg_running = True
        self.thread_name = ""
        self.thread_counter = 0
        self.setState(lambda: None)
        t = threading.Thread(target=bg_work, name="FlutBgWorker", daemon=True)
        t.start()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Background counter: {self.thread_counter}/5",
                    style=TextStyle(fontSize=16),
                ),
                SizedBox(height=4),
                Text(
                    (
                        f"Thread: {self.thread_name}"
                        if self.thread_name
                        else "Not started"
                    ),
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
                SizedBox(height=8),
                self._make_button(
                    "Running..." if self.bg_running else "Start background counter",
                    self._start_background_counter,
                    color=Colors.grey if self.bg_running else Colors.green,
                ),
            ],
        )


class _ChangeNotifierDemo(StatefulWidget):
    def createState(self):
        return _ChangeNotifierDemoState()


class _ChangeNotifierDemoState(State[_ChangeNotifierDemo]):

    def initState(self):
        from flut.flutter.widgets import ScrollController

        self.controller = ScrollController()
        self.listener_count = 0
        self.notify_count = 0
        self.listener_added = False

    def _make_button(self, label, on_tap, color=None):
        return GestureDetector(
            onTap=on_tap,
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                decoration=BoxDecoration(
                    color=color or Colors.blue,
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Text(
                    label,
                    style=TextStyle(color=Colors.white, fontSize=13),
                ),
            ),
        )

    def _on_scroll(self):
        self.notify_count += 1
        self.setState(lambda: None)

    def _add_listener(self):
        if not self.listener_added:
            self.controller.addListener(self._on_scroll)
            self.listener_added = True
            self.listener_count += 1
            self.setState(lambda: None)

    def _remove_listener(self):
        if self.listener_added:
            self.controller.removeListener(self._on_scroll)
            self.listener_added = False
            self.listener_count -= 1
            self.setState(lambda: None)

    def _scroll_down(self):
        if self.controller.hasClients:
            self.controller.jumpTo(self.controller.offset + 50)

    def dispose(self):
        self.controller.dispose()
        super().dispose()

    def build(self, context):
        from flut.flutter.widgets import ListView

        scroll_list = ListView(
            controller=self.controller,
            shrinkWrap=True,
            children=[
                Container(
                    padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                    child=Text(f"Item {i}", style=TextStyle(fontSize=13)),
                )
                for i in range(30)
            ],
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    f"Listeners: {self.listener_count}  |  Notifications: {self.notify_count}",
                    style=TextStyle(fontSize=14, fontFamily=CODE_FONT_FAMILY),
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        self._make_button(
                            (
                                "Add Listener"
                                if not self.listener_added
                                else "Listener Active"
                            ),
                            self._add_listener,
                            color=(
                                Colors.green if not self.listener_added else Colors.grey
                            ),
                        ),
                        SizedBox(width=8),
                        self._make_button(
                            "Remove Listener",
                            self._remove_listener,
                            color=Colors.red if self.listener_added else Colors.grey,
                        ),
                        SizedBox(width=8),
                        self._make_button("Scroll +50", self._scroll_down),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    height=150.0,
                    child=scroll_list,
                ),
            ],
        )


class _BuilderWithStateDemo(StatefulWidget):
    def createState(self):
        return _BuilderWithStateDemoState()


class _BuilderWithStateDemoState(State[_BuilderWithStateDemo]):
    def initState(self):
        self.count = 0

    def build(self, context):
        return Builder(
            builder=lambda ctx: Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(f"Counter value: {self.count}", style=TextStyle(fontSize=16)),
                    SizedBox(height=8),
                    Row(
                        children=[
                            ElevatedButton(
                                child=Text("Increment"),
                                onPressed=lambda: self.setState(
                                    lambda: setattr(self, "count", self.count + 1)
                                ),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                child=Text("Reset"),
                                onPressed=lambda: self.setState(
                                    lambda: setattr(self, "count", 0)
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )


class _ListenableBuilderDemo(StatefulWidget):
    def createState(self):
        return _ListenableBuilderDemoState()


class _ListenableBuilderDemoState(State[_ListenableBuilderDemo]):
    def initState(self):
        self.notifier = ValueNotifier(0)

    def build(self, context):
        theme = Theme.of(context)
        bg = (
            Color(0xFF2E3B2E)
            if theme.brightness == Brightness.dark
            else Color(0xFFE8F5E9)
        )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ListenableBuilder(
                    listenable=self.notifier,
                    builder=lambda ctx, child: Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=bg,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text(
                            f"Notifier value: {self.notifier.value}",
                            style=TextStyle(fontSize=14),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("+1"),
                            onPressed=lambda: setattr(
                                self.notifier, "value", self.notifier.value + 1
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reset"),
                            onPressed=lambda: setattr(self.notifier, "value", 0),
                        ),
                    ],
                ),
            ],
        )


class _ValueListenableBuilderDemo(StatefulWidget):
    def createState(self):
        return _ValueListenableBuilderDemoState()


class _ValueListenableBuilderDemoState(State[_ValueListenableBuilderDemo]):
    def initState(self):
        self.notifier = ValueNotifier(0)

    def build(self, context):
        return ValueListenableBuilder(
            valueListenable=self.notifier,
            builder=lambda ctx, value, child: Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(f"ValueNotifier value: {value}", style=TextStyle(fontSize=16)),
                    SizedBox(height=8),
                    Row(
                        children=[
                            ElevatedButton(
                                child=Text("+1"),
                                onPressed=lambda: setattr(
                                    self.notifier, "value", self.notifier.value + 1
                                ),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                child=Text("Reset"),
                                onPressed=lambda: setattr(self.notifier, "value", 0),
                            ),
                        ],
                    ),
                ],
            ),
        )


class _ValueListenableChildDemo(StatefulWidget):
    def createState(self):
        return _ValueListenableChildDemoState()


class _ValueListenableChildDemoState(State[_ValueListenableChildDemo]):
    def initState(self):
        self.notifier = ValueNotifier(0)

    def build(self, context):
        theme = Theme.of(context)
        cached_bg = (
            Color(0xFF3E3525)
            if theme.brightness == Brightness.dark
            else Color(0xFFFFF3E0)
        )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ValueListenableBuilder(
                    valueListenable=self.notifier,
                    child=Container(
                        padding=EdgeInsets.all(8),
                        decoration=BoxDecoration(
                            color=cached_bg,
                            borderRadius=BorderRadius.circular(4),
                        ),
                        child=Text("I'm the cached child"),
                    ),
                    builder=lambda ctx, value, child: Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(f"Counter: {value}"),
                            SizedBox(height=4),
                            child,
                        ],
                    ),
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("+1"),
                            onPressed=lambda: setattr(
                                self.notifier, "value", self.notifier.value + 1
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reset"),
                            onPressed=lambda: setattr(self.notifier, "value", 0),
                        ),
                    ],
                ),
            ],
        )


class _ExpansionTileDemo(StatefulWidget):
    def createState(self):
        return _ExpansionTileDemoState()


class _ExpansionTileDemoState(State[_ExpansionTileDemo]):
    def initState(self):
        self.expansion_controller = ExpansibleController()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Expand"),
                            onPressed=lambda: self.expansion_controller.expand(),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Collapse"),
                            onPressed=lambda: self.expansion_controller.collapse(),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    width=500.0,
                    child=ExpansionTile(
                        title=Text("Tap to expand"),
                        subtitle=Text("Or use the buttons above"),
                        controller=self.expansion_controller,
                        children=[
                            Padding(
                                padding=EdgeInsets.all(16),
                                child=Text(
                                    "This is the expanded content. "
                                    "ExpansibleController manages the state."
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                ExpansionTile(
                    title=Text("Simple ExpansionTile"),
                    initiallyExpanded=True,
                    iconColor=Colors.blue,
                    textColor=Colors.blue,
                    children=[
                        ListTile(title=Text("Item 1")),
                        ListTile(title=Text("Item 2")),
                        ListTile(title=Text("Item 3")),
                    ],
                ),
            ],
        )


class _PanAxisDemo(StatefulWidget):
    def createState(self):
        return _PanAxisDemoState()


class _PanAxisDemoState(State[_PanAxisDemo]):
    def initState(self):
        self.axis_index = 3

    def build(self, context):
        axes = [
            ("horizontal", PanAxis.horizontal),
            ("vertical", PanAxis.vertical),
            ("aligned", PanAxis.aligned),
            ("free", PanAxis.free),
        ]
        name, axis = axes[self.axis_index]

        selectors = []
        for i, (label, _) in enumerate(axes):
            is_selected = i == self.axis_index
            selectors.append(
                GestureDetector(
                    onTap=lambda idx=i: self.setState(
                        lambda: setattr(self, "axis_index", idx)
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

        grid_children = []
        grid_colors = [
            Colors.red,
            Colors.blue,
            Colors.green,
            Colors.orange,
            Colors.purple,
            Colors.teal,
        ]
        for row in range(4):
            for col in range(4):
                color = grid_colors[(row + col) % len(grid_colors)]
                grid_children.append(
                    Positioned(
                        left=col * 100.0,
                        top=row * 80.0,
                        child=Container(
                            width=95.0,
                            height=75.0,
                            color=color.withValues(alpha=0.3),
                            child=Center(
                                child=Text(
                                    f"({row},{col})",
                                    style=TextStyle(fontSize=11),
                                ),
                            ),
                        ),
                    )
                )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(spacing=8, runSpacing=8, children=selectors),
                SizedBox(height=8),
                Text(
                    f"PanAxis.{name}",
                    style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                ),
                SizedBox(height=8),
                Container(
                    width=350.0,
                    height=200.0,
                    decoration=BoxDecoration(
                        border=Border.all(color=Colors.grey, width=1.0),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=InteractiveViewer(
                        panAxis=axis,
                        constrained=False,
                        boundaryMargin=EdgeInsets.all(40),
                        minScale=0.5,
                        maxScale=3.0,
                        child=Container(
                            width=400.0,
                            height=320.0,
                            child=Stack(children=grid_children),
                        ),
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "Horizontal and vertical restrict panning, aligned locks to the dominant drag axis, and free allows both.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


def _key_demo_row(reversed_order, use_value_key):
    items = [
        ("Alpha", Colors.blue),
        ("Beta", Colors.teal),
        ("Gamma", Colors.deepPurple),
    ]
    if reversed_order:
        items = list(reversed(items))
    children = []
    for label, color in items:
        if use_value_key:
            key = ValueKey(f"keydemo_{label}")
        else:
            key = UniqueKey()
        if children:
            children.append(SizedBox(width=8))
        children.append(_KeyDemoChild(label, color, key=key))
    return Row(children=children)


class _IgnorePointerDemo(StatefulWidget):
    def createState(self):
        return _IgnorePointerDemoState()


class _IgnorePointerDemoState(State[_IgnorePointerDemo]):
    def initState(self):
        self.ignored = True
        self.tap_count = 0

    def _on_tap(self):
        self.tap_count = self.tap_count + 1
        self.setState(lambda: None)

    def _toggle(self):
        self.ignored = not self.ignored
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._toggle,
                            child=Text(
                                f"ignoring={self.ignored} (toggle)",
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"taps received: {self.tap_count}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                IgnorePointer(
                    ignoring=self.ignored,
                    child=ElevatedButton(
                        onPressed=self._on_tap,
                        child=Text("Try clicking me"),
                    ),
                ),
            ],
        )


class _ScrollbarDemo(StatefulWidget):
    def createState(self):
        return _ScrollbarDemoState()


class _ScrollbarDemoState(State[_ScrollbarDemo]):
    def initState(self):
        self.controller = ScrollController()
        self.orientation = ScrollbarOrientation.right

    def _set_orientation(self, value):
        self.orientation = value
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    children=[
                        ElevatedButton(
                            onPressed=lambda o=o: self._set_orientation(o),
                            child=Text(label),
                        )
                        for o, label in [
                            (ScrollbarOrientation.left, "left"),
                            (ScrollbarOrientation.right, "right"),
                            (ScrollbarOrientation.top, "top"),
                            (ScrollbarOrientation.bottom, "bottom"),
                        ]
                    ],
                ),
                SizedBox(height=8),
                Container(
                    height=200.0,
                    width=400.0,
                    decoration=BoxDecoration(
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Scrollbar(
                        controller=self.controller,
                        thumbVisibility=True,
                        trackVisibility=True,
                        thickness=10.0,
                        radius=Radius.circular(6.0),
                        interactive=True,
                        scrollbarOrientation=self.orientation,
                        child=SingleChildScrollView(
                            controller=self.controller,
                            child=Column(
                                children=[
                                    Padding(
                                        padding=EdgeInsets.all(8.0),
                                        child=Text(
                                            f"Line {i}",
                                            style=TextStyle(fontSize=14),
                                        ),
                                    )
                                    for i in range(40)
                                ],
                            ),
                        ),
                    ),
                ),
            ],
        )


class WidgetPage(StatelessWidget):
    def build(self, context):
        measure_ctrl = _LogController()
        current_widget_ctrl = _LogController()
        current_state_ctrl = _LogController()
        overlay_ctrl = _LogController()
        inherited_ctrl = _LogController()
        _identity_stateful_ctrl = _LogController()
        _identity_inherited_ctrl = _LogController()

        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark
        box_a = Color(0xFF3E2A2A) if is_dark else Color(0xFFFCE4EC)
        box_b = Color(0xFF2E3B2E) if is_dark else Color(0xFFE8F5E9)
        box_c = Color(0xFF3E3525) if is_dark else Color(0xFFFFF3E0)
        inline_bg = Color(0xFF1E3A50) if is_dark else Color(0xFFE3F2FD)

        return CatalogPage(
            title="Widget, State and Builder",
            description=(
                "Introduces core widget patterns: local state, builders, "
                "context-driven lookup, keys, overlays, and inherited data flowing "
                "through the tree."
            ),
            children=[
                SplitViewTile(
                    title="GlobalKey & Widget Measurement",
                    description=(
                        "GlobalKey gives access to a widget's BuildContext and RenderBox. "
                        "Use it to measure size and position after layout."
                    ),
                    visible=_GlobalKeyMeasureDemo(controller=measure_ctrl),
                    code=CodeArea(
                        language="python",
                        code=(
                            "box_key = GlobalKey(debugLabel='measured-box')\n"
                            "Container(key=box_key, ...)\n\n"
                            "ctx = box_key.currentContext\n"
                            "render_box = ctx.findRenderObject()\n"
                            "size = render_box.size\n"
                            "pos = render_box.localToGlobal(Offset(0, 0))"
                        ),
                    ),
                    instruction="Click 'Measure Size & Position' to read the blue box's rendered size and screen position.",
                    log=_LogPanel(controller=measure_ctrl),
                ),
                SplitViewTile(
                    title="GlobalKey.currentWidget",
                    description=(
                        "Access the Python widget instance attached to a GlobalKey. "
                        "Python tracks this locally \u2014 set on pack, cleared on unmount."
                    ),
                    visible=_CurrentWidgetDemo(controller=current_widget_ctrl),
                    code=CodeArea(
                        language="python",
                        code=(
                            "key = GlobalKey(debugLabel='tracked')\n"
                            "Container(key=key, width=180, height=60)\n\n"
                            "widget = key.currentWidget\n"
                            "print(type(widget).__name__)\n"
                            "print(widget.width, widget.height)"
                        ),
                    ),
                    instruction="Click 'Read currentWidget' to inspect the orange box's widget type and dimensions.",
                    log=_LogPanel(controller=current_widget_ctrl),
                ),
                SplitViewTile(
                    title="GlobalKey.currentState",
                    description=(
                        "Access a StatefulWidget's State from outside via GlobalKey. "
                        "Click the counter, then read its state from the parent."
                    ),
                    visible=_GlobalKeyStatefulDemo(controller=current_state_ctrl),
                    code=CodeArea(
                        language="python",
                        code=(
                            "key = GlobalKey(debugLabel='counter')\n"
                            "MyCounter(key=key)\n\n"
                            "state = key.currentState\n"
                            "print(state.count)"
                        ),
                    ),
                    instruction="Tap the counter to increment it, then click 'Read Counter State' to read its value from outside.",
                    log=_LogPanel(controller=current_state_ctrl),
                ),
                SplitViewTile(
                    title="Keys",
                    description=(
                        "ValueKey identifies a widget by a stable value for efficient reconciliation. "
                        "UniqueKey guarantees a widget is always treated as new."
                    ),
                    instruction="Each box displays its key type. The stateful counter demo below shows how those identities affect preserved state.",
                    visible=Row(
                        children=[
                            Container(
                                key=ValueKey("key_demo_a"),
                                padding=EdgeInsets.all(12),
                                decoration=BoxDecoration(
                                    color=Color(0xFFE8F5E9),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Text(
                                    "ValueKey('key_demo_a')",
                                    style=TextStyle(
                                        fontSize=12, fontFamily=CODE_FONT_FAMILY
                                    ),
                                ),
                            ),
                            SizedBox(width=8),
                            Container(
                                key=UniqueKey(),
                                padding=EdgeInsets.all(12),
                                decoration=BoxDecoration(
                                    color=Color(0xFFFFF3E0),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Text(
                                    "UniqueKey()",
                                    style=TextStyle(
                                        fontSize=12, fontFamily=CODE_FONT_FAMILY
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=("key=ValueKey('same-id')\n" "key=UniqueKey()"),
                    ),
                ),
                SplitViewTile(
                    title="Key Effects: ValueKey vs UniqueKey",
                    description=(
                        "ValueKey preserves widget State when the tree is reordered, because "
                        "Flutter matches the key to the existing Element. UniqueKey forces a "
                        "new State on every rebuild."
                    ),
                    instruction=(
                        "Tap each colored box to increment its counter, then press "
                        "Reverse Order. With ValueKey the counts follow the boxes; "
                        "with UniqueKey they reset."
                    ),
                    visible=_KeyEffectsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "items = [('Alpha', Colors.blue), ('Beta', Colors.teal)]\n"
                            "if reversed_order:\n"
                            "    items = list(reversed(items))\n"
                            "children = []\n"
                            "for label, color in items:\n"
                            "    key = ValueKey(f'demo_{label}')\n"
                            "    children.append(MyChild(label, color, key=key))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Overlay / OverlayEntry",
                    description=(
                        "Create an OverlayEntry with a builder, insert it via "
                        "Overlay.of(context).insert(entry), and remove it with entry.remove()."
                    ),
                    visible=_OverlayDemo(controller=overlay_ctrl),
                    code=CodeArea(
                        language="python",
                        code=(
                            "def build_overlay(ctx):\n"
                            "    return Container(\n"
                            "        alignment=Alignment.center,\n"
                            "        child=Text('Hello from overlay'),\n"
                            "    )\n\n"
                            "entry = OverlayEntry(builder=build_overlay)\n"
                            "Overlay.of(context).insert(entry)\n\n"
                            "entry.remove()"
                        ),
                    ),
                    instruction="Click 'Show Overlay' to insert a full-screen overlay. Tap the overlay to dismiss it.",
                    log=_LogPanel(controller=overlay_ctrl),
                ),
                SplitViewTile(
                    title="InheritedWidget",
                    description=(
                        "Two independent InheritedWidgets propagate data to a consumer. "
                        "Changing theme or locale rebuilds the consumer via updateShouldNotify."
                    ),
                    visible=_InheritedWidgetDemo(controller=inherited_ctrl),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class MyTheme(InheritedWidget):\n"
                            "    def __init__(self, *, color, child):\n"
                            "        super().__init__(child=child)\n"
                            "        self.color = color\n\n"
                            "    def updateShouldNotify(self, old):\n"
                            "        return self.color != old.color\n\n"
                            "    @staticmethod\n"
                            "    def of(context):\n"
                            "        return InheritedWidget._of(context, 'MyTheme')\n\n"
                            "theme = MyTheme.of(context)\n"
                            "print(theme.color)"
                        ),
                    ),
                    instruction="Click 'Theme' or 'Locale' buttons to change inherited values. Watch the consumer rebuild and the build count increment.",
                    log=_LogPanel(controller=inherited_ctrl),
                ),
                SplitViewTile(
                    title="Class Identity — StatefulWidget",
                    description=(
                        "Two different StatefulWidget Python classes share the same "
                        "parent slot. Swapping the class disposes the old State and "
                        "creates a fresh one — the count resets and initState/dispose "
                        "fire, just like vanilla Flutter would for two distinct "
                        "Dart widget classes."
                    ),
                    visible=_ClassIdentityStatefulDemo(
                        controller=_identity_stateful_ctrl
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class RedCounter(StatefulWidget):\n"
                            "    def createState(self): return RedCounterState()\n\n"
                            "class BlueCounter(StatefulWidget):\n"
                            "    def createState(self): return BlueCounterState()\n\n"
                            "slot = RedCounter() if use_red else BlueCounter()\n"
                            "Column(children=[toggle_button, slot])"
                        ),
                    ),
                    instruction=(
                        "Tap the colored counter to increment, then press 'Swap class "
                        "in slot'. The counter resets and the log shows the old class's "
                        "dispose followed by the new class's initState."
                    ),
                    log=_LogPanel(controller=_identity_stateful_ctrl),
                ),
                SplitViewTile(
                    title="Class Identity — StatelessWidget",
                    description=(
                        "Two different StatelessWidget Python classes wrap the same "
                        "child in the same parent slot. Swapping the wrapper class "
                        "replaces the parent Element, so even a child with a stable "
                        "ValueKey loses its State — same behavior as swapping two "
                        "distinct Dart StatelessWidget classes."
                    ),
                    visible=_ClassIdentityStatelessDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class ProbeA(StatelessWidget):\n"
                            "    def build(self, ctx): return Container(child=self._child)\n\n"
                            "class ProbeB(StatelessWidget):\n"
                            "    def build(self, ctx): return Container(child=self._child)\n\n"
                            "inner = MyCounter(key=ValueKey('keep'))\n"
                            "wrapper = ProbeA(child=inner) if use_a else ProbeB(child=inner)"
                        ),
                    ),
                    instruction=(
                        "Tap the counter, then press 'Swap stateless wrapper class'. "
                        "The wrapper label flips and the counter resets to 0 even "
                        "though it carries a stable ValueKey."
                    ),
                ),
                SplitViewTile(
                    title="Class Identity — InheritedWidget",
                    description=(
                        "Two different InheritedWidget Python classes occupy the same "
                        "parent slot. Each exposes its own .of(context) lookup. The "
                        "consumer below queries both — only the one currently in the "
                        "tree returns a value, proving the previous scope was fully "
                        "torn down."
                    ),
                    visible=_ClassIdentityInheritedDemo(
                        controller=_identity_inherited_ctrl
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class AlphaScope(InheritedWidget):\n"
                            "    @staticmethod\n"
                            "    def of(ctx): return InheritedWidget._of(ctx, 'AlphaScope')\n\n"
                            "class BetaScope(InheritedWidget):\n"
                            "    @staticmethod\n"
                            "    def of(ctx): return InheritedWidget._of(ctx, 'BetaScope')\n\n"
                            "scope = AlphaScope(value=v, child=reader) if use_alpha else \\\n"
                            "        BetaScope(value=v, child=reader)"
                        ),
                    ),
                    instruction=(
                        "Press 'Swap InheritedWidget class' to flip the ancestor "
                        "between AlphaScope and BetaScope. The log shows that only "
                        "the active class's .of(context) returns a value; the other "
                        "returns None. Press 'Bump value' to confirm same-class "
                        "updates still flow through updateShouldNotify."
                    ),
                    log=_LogPanel(controller=_identity_inherited_ctrl),
                ),
                SplitViewTile(
                    title="Visibility — maintainState + maintainSize",
                    description=(
                        "When maintainState, maintainAnimation, and maintainSize are True, "
                        "the widget is hidden but still occupies its layout space."
                    ),
                    instruction="Toggle visibility. The orange box disappears but the grey boxes stay in place — layout is preserved.",
                    visible=_VisibilityMaintainDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Visibility(\n"
                            "    visible=is_visible,\n"
                            "    maintainState=True,\n"
                            "    maintainAnimation=True,\n"
                            "    maintainSize=True,\n"
                            "    child=Container(width=120.0, height=60.0),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Visibility — replacement",
                    description="Shows a replacement widget when visibility is False instead of leaving empty space.",
                    instruction="Press Toggle replacement to swap between the original green box and the red replacement.",
                    visible=_VisibilityReplacementDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Visibility(\n"
                            "    visible=show_original,\n"
                            "    replacement=Container(color=Colors.red),\n"
                            "    child=Container(color=Colors.green),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Visibility.of",
                    description=(
                        "Visibility.of(context) reports the nearest Visibility ancestor's "
                        "visible state. This keeps the API with the rest of the Visibility demos."
                    ),
                    instruction=(
                        "Toggle the ancestor Visibility to compare the value returned by "
                        "Visibility.of(context) in the visible and replacement branches."
                    ),
                    visible=_VisibilityOfDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Visibility(\n"
                            "    visible=show_child,\n"
                            "    replacement=Builder(\n"
                            "        builder=lambda ctx: Text(\n"
                            "            f'Visibility.of(context) = {Visibility.of(ctx)}'\n"
                            "        ),\n"
                            "    ),\n"
                            "    child=Builder(\n"
                            "        builder=lambda ctx: Text(\n"
                            "            f'Visibility.of(context) = {Visibility.of(ctx)}'\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InteractiveViewer Callbacks",
                    description=(
                        "InteractiveViewer wrapping a large colored container. "
                        "Track onInteractionStart, onInteractionUpdate, and onInteractionEnd "
                        "to display live scale, rotation, focal point, and velocity values."
                    ),
                    visible=_InteractiveViewerCallbacksDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InteractiveViewer(\n"
                            "    minScale=0.5,\n"
                            "    maxScale=4.0,\n"
                            "    onInteractionStart=on_start,\n"
                            "    onInteractionUpdate=on_update,\n"
                            "    onInteractionEnd=on_end,\n"
                            "    child=Container(width=300, height=300),\n"
                            ")\n\n"
                            "def on_start(details):\n"
                            "    print(details.focalPoint)\n\n"
                            "def on_update(details):\n"
                            "    print(details.scale, details.rotation)\n\n"
                            "def on_end(details):\n"
                            "    print(details.velocity.pixelsPerSecond)"
                        ),
                    ),
                    instruction="Drag or pinch the purple box to see live scale, rotation, focal point, and end velocity values update in the panel below.",
                ),
                SplitViewTile(
                    title="InteractiveViewer TransformationController",
                    description=(
                        "InteractiveViewer with a TransformationController. "
                        "Use buttons to reset, zoom in (2x), or zoom out (0.5x). "
                        "The current transform matrix values are displayed below."
                    ),
                    visible=_InteractiveViewerControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "controller = TransformationController(\n"
                            "    Matrix4.identity()\n"
                            ")\n\n"
                            "InteractiveViewer(\n"
                            "    transformationController=controller,\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "controller.value = Matrix4.diagonal3Values(\n"
                            "    2.0, 2.0, 1.0\n"
                            ")\n\n"
                            "controller.value = Matrix4.identity()"
                        ),
                    ),
                    instruction="Use buttons or drag/pinch to transform the view. Observe the controller matrix values update below.",
                ),
                SplitViewTile(
                    title="ExpansionTile Shape & ClipBehavior",
                    description=(
                        "Three ExpansionTiles demonstrating different shapes, "
                        "clip behaviors, control affinity, and visual density settings."
                    ),
                    visible=_ExpansionTileShapeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ExpansionTile(\n"
                            "    title=Text('Default Shape'),\n"
                            "    children=[...],\n"
                            ")\n\n"
                            "ExpansionTile(\n"
                            "    title=Text('Rounded'),\n"
                            "    shape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(16),\n"
                            "    ),\n"
                            "    collapsedShape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(4),\n"
                            "    ),\n"
                            ")\n\n"
                            "ExpansionTile(\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            "    controlAffinity=ListTileControlAffinity.leading,\n"
                            "    visualDensity=VisualDensity.compact,\n"
                            ")"
                        ),
                    ),
                    instruction="Tap each tile to expand. Notice different shapes, arrow positions (trailing vs leading), and density.",
                ),
                SplitViewTile(
                    title="WidgetState Constraints",
                    description=(
                        "WidgetState represents visual states like hovered, pressed, and disabled. "
                        "Constraints combine states with & (all), | (any), and ~ (not) operators. "
                        "isSatisfiedBy checks whether a set of active states matches the constraint."
                    ),
                    instruction=(
                        "Toggle the checkboxes to activate states. "
                        "Each constraint below shows MATCH or NO based on the current selection."
                    ),
                    visible=_WidgetStateDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "hovered_and_focused = WidgetState.hovered & WidgetState.focused\n"
                            "hovered_or_focused = WidgetState.hovered | WidgetState.focused\n"
                            "not_disabled = ~WidgetState.disabled\n\n"
                            "active = {WidgetState.hovered, WidgetState.focused}\n"
                            "hovered_and_focused.isSatisfiedBy(active)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="WidgetStateColor + scrolledUnder",
                    description=(
                        "WidgetStateColor.fromMap resolves a color based on the widget's current states. "
                        "AppBar uses the scrolledUnder state to change its background when content scrolls beneath it."
                    ),
                    instruction="Scroll the list inside the embedded Scaffold to see the AppBar change from white to blue.",
                    visible=_ScrolledUnderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    backgroundColor=WidgetStateColor.fromMap({\n"
                            "        WidgetState.scrolledUnder: Color(0xFFE3F2FD),\n"
                            "        WidgetState.any: Colors.white,\n"
                            "    }),\n"
                            "    scrolledUnderElevation=2.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InteractiveViewer basics + panAxis",
                    description=(
                        "InteractiveViewer allows pan and zoom by default. This demo keeps the "
                        "same viewer while switching panAxis between horizontal, vertical, "
                        "aligned, and free movement."
                    ),
                    instruction=(
                        "Start with free movement for the basic behavior, then switch panAxis "
                        "with the chips to feel how each mode constrains dragging."
                    ),
                    visible=_PanAxisDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InteractiveViewer(\n"
                            "    minScale=0.5,\n"
                            "    maxScale=4.0,\n"
                            "    panAxis=PanAxis.horizontal,\n"
                            "    constrained=False,\n"
                            "    boundaryMargin=EdgeInsets.all(40),\n"
                            "    child=large_grid,\n"
                            ")\n\n"
                            "InteractiveViewer(\n"
                            "    panAxis=PanAxis.free,\n"
                            "    child=large_grid,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="setState Variants",
                    description=(
                        "setState accepts a lambda, a named function, or None. "
                        "Lambda and function variants run the callback synchronously before triggering a rebuild. "
                        "With None, you mutate state first and then call setState to notify."
                    ),
                    instruction=(
                        "Click Lambda, None, or Function to increment the counter. "
                        "Observe which method was used and whether the callback executed."
                    ),
                    visible=_SetStateDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "setState(lambda: setattr(self, 'counter', counter + 1))\n\n"
                            "counter += 1\n"
                            "setState(None)\n\n"
                            "def update():\n"
                            "    counter += 1\n"
                            "setState(update)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="setState from Background Thread",
                    description=(
                        "setState is thread-safe in Flut. A background thread can call setState "
                        "and the callback runs on the calling thread, while Dart is notified "
                        "asynchronously to rebuild on the UI thread."
                    ),
                    instruction=(
                        "Click the button to start a background thread that increments the counter "
                        "once per second for 5 seconds."
                    ),
                    visible=_BackgroundSetStateDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "def bg_work():\n"
                            "    for i in range(5):\n"
                            "        time.sleep(1)\n"
                            "        def update():\n"
                            "            thread_counter += 1\n"
                            "        setState(update)\n\n"
                            "Thread(target=bg_work, daemon=True).start()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ChangeNotifier (ScrollController)",
                    description=(
                        "ScrollController, TextEditingController, and FocusNode all extend ChangeNotifier. "
                        "Use addListener to subscribe to changes and removeListener to unsubscribe. "
                        "Bound methods work directly \u2014 no wrapper needed."
                    ),
                    instruction=(
                        "Add a listener, then click 'Scroll +50' to trigger scroll notifications. "
                        "Remove the listener to stop receiving updates."
                    ),
                    visible=_ChangeNotifierDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "controller = ScrollController()\n\n"
                            "controller.addListener(on_scroll)\n"
                            "controller.removeListener(on_scroll)\n\n"
                            "controller.jumpTo(controller.offset + 50)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Inline Builder",
                    description=(
                        "Builder takes a builder callback and invokes it with "
                        "the BuildContext at that point in the tree. Useful for "
                        "obtaining context-dependent data without creating a new widget class."
                    ),
                    instruction="A static container rendered entirely by the Builder callback.",
                    visible=Builder(
                        builder=lambda ctx: Container(
                            padding=EdgeInsets.all(16),
                            decoration=BoxDecoration(
                                color=inline_bg,
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text(
                                "This widget was built by a Builder callback",
                                style=TextStyle(fontSize=14),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Builder(\n"
                            "    builder=lambda ctx: Container(\n"
                            "        padding=EdgeInsets.all(16),\n"
                            "        child=Text('Built by a Builder callback'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Builder with State",
                    description=(
                        "Builder can read state from the enclosing StatefulWidget. "
                        "The builder callback re-runs on setState, showing updated values."
                    ),
                    instruction="Click Increment to increase the counter, or Reset to return to zero.",
                    visible=_BuilderWithStateDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Builder(\n"
                            "    builder=lambda ctx: Column(\n"
                            "        children=[\n"
                            "            Text(f'Counter: {count}'),\n"
                            "            ElevatedButton(\n"
                            "                child=Text('Increment'),\n"
                            "                onPressed=increment,\n"
                            "            ),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Multiple Builders",
                    description=(
                        "Multiple Builder widgets placed side by side, each with "
                        "its own builder callback producing an independent subtree."
                    ),
                    instruction="Three colored boxes, each produced by a separate Builder callback.",
                    visible=Row(
                        children=[
                            Builder(
                                builder=lambda ctx: Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=box_a,
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("Builder A"),
                                ),
                            ),
                            SizedBox(width=8),
                            Builder(
                                builder=lambda ctx: Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=box_b,
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("Builder B"),
                                ),
                            ),
                            SizedBox(width=8),
                            Builder(
                                builder=lambda ctx: Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=box_c,
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("Builder C"),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Row(\n"
                            "    children=[\n"
                            "        Builder(builder=lambda ctx: Container(\n"
                            "            child=Text('Builder A'),\n"
                            "        )),\n"
                            "        Builder(builder=lambda ctx: Container(\n"
                            "            child=Text('Builder B'),\n"
                            "        )),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ListenableBuilder",
                    description=(
                        "Rebuilds whenever a Listenable notifies. The notification "
                        "stays on the Dart side \u2014 only the builder callback crosses FFI."
                    ),
                    instruction="Click +1 to increment the ValueNotifier. The ListenableBuilder rebuilds automatically.",
                    visible=_ListenableBuilderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "notifier = ValueNotifier(0)\n\n"
                            "ListenableBuilder(\n"
                            "    listenable=notifier,\n"
                            "    builder=lambda ctx, child: Text(\n"
                            "        f'Value: {notifier.value}',\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ValueListenableBuilder",
                    description=(
                        "Rebuilds when a ValueNotifier's value changes. The current "
                        "value is passed directly to the builder \u2014 no manual state management needed."
                    ),
                    instruction="Click +1 to increment or Reset to clear. The value argument in the builder updates automatically.",
                    visible=_ValueListenableBuilderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "notifier = ValueNotifier(0)\n\n"
                            "ValueListenableBuilder(\n"
                            "    valueListenable=notifier,\n"
                            "    builder=lambda ctx, value, child: Text(\n"
                            "        f'Value: {value}',\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ValueListenableBuilder with child",
                    description=(
                        "The child parameter caches a widget subtree that does not "
                        "depend on the value. It is passed through to the builder on "
                        "every rebuild without being reconstructed."
                    ),
                    instruction="Click +1 to change the counter. The cached child widget stays the same across rebuilds.",
                    visible=_ValueListenableChildDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ValueListenableBuilder(\n"
                            "    valueListenable=notifier,\n"
                            "    child=Text('I am cached'),\n"
                            "    builder=lambda ctx, value, child: Column(\n"
                            "        children=[\n"
                            "            Text(f'Counter: {value}'),\n"
                            "            child,\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ExpansionTile",
                    description=(
                        "A list tile that expands to reveal children. "
                        "ExpansibleController allows programmatic expand/collapse from outside the tile."
                    ),
                    instruction="Use the buttons to expand/collapse programmatically, or tap the tile header directly.",
                    visible=_ExpansionTileDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ctrl = ExpansibleController()\n\n"
                            "ExpansionTile(\n"
                            "    title=Text('Details'),\n"
                            "    controller=ctrl,\n"
                            "    children=[Text('Expanded content')],\n"
                            ")\n\n"
                            "ctrl.expand()\n"
                            "ctrl.collapse()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InteractiveViewer",
                    description=(
                        "InteractiveViewer allows panning and zooming of its child within "
                        "configurable scale bounds and boundary margins."
                    ),
                    instruction="Scroll to zoom (0.5x\u20134x) and drag to pan the content area.",
                    visible=Container(
                        width=400.0,
                        height=220.0,
                        decoration=BoxDecoration(
                            border=Border.all(color=Colors.grey, width=1.0),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=InteractiveViewer(
                            boundaryMargin=EdgeInsets.all(60),
                            minScale=0.5,
                            maxScale=4.0,
                            child=Container(
                                width=500.0,
                                height=350.0,
                                color=Color(0xFFF5F5F5),
                                child=Stack(
                                    children=[
                                        Positioned(
                                            left=20,
                                            top=20,
                                            child=Text(
                                                "Scroll/pinch to zoom, drag to pan",
                                                style=TextStyle(
                                                    fontSize=14,
                                                    fontWeight=FontWeight.bold,
                                                ),
                                            ),
                                        ),
                                        Positioned(
                                            left=40,
                                            top=80,
                                            child=Container(
                                                width=120.0,
                                                height=80.0,
                                                decoration=BoxDecoration(
                                                    color=Colors.blue.withValues(
                                                        alpha=0.3
                                                    ),
                                                    borderRadius=BorderRadius.circular(
                                                        8
                                                    ),
                                                ),
                                                child=Center(
                                                    child=Text("Box A"),
                                                ),
                                            ),
                                        ),
                                        Positioned(
                                            left=200,
                                            top=120,
                                            child=Container(
                                                width=120.0,
                                                height=80.0,
                                                decoration=BoxDecoration(
                                                    color=Colors.teal.withValues(
                                                        alpha=0.3
                                                    ),
                                                    borderRadius=BorderRadius.circular(
                                                        8
                                                    ),
                                                ),
                                                child=Center(
                                                    child=Text("Box B"),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InteractiveViewer(\n"
                            "    boundaryMargin=EdgeInsets.all(60),\n"
                            "    minScale=0.5,\n"
                            "    maxScale=4.0,\n"
                            "    child=Container(width=500.0, height=350.0),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InteractiveViewer panAxis",
                    description=(
                        "InteractiveViewer can restrict panning to horizontal, vertical, "
                        "aligned, or free movement without changing the zoom behavior."
                    ),
                    instruction="Switch panAxis with the chips, then drag the canvas to feel how each mode constrains movement.",
                    visible=_PanAxisDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InteractiveViewer(\n"
                            "    panAxis=PanAxis.horizontal,\n"
                            "    constrained=False,\n"
                            "    boundaryMargin=EdgeInsets.all(40),\n"
                            "    child=large_grid,\n"
                            ")\n\n"
                            "InteractiveViewer(\n"
                            "    panAxis=PanAxis.free,\n"
                            "    child=large_grid,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IgnorePointer",
                    description=(
                        "IgnorePointer makes its subtree invisible to hit-testing. "
                        "Children still paint, but pointer events skip them."
                    ),
                    instruction="Toggle 'ignoring' and try clicking the inner button. Taps only register when ignoring=False.",
                    visible=_IgnorePointerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "IgnorePointer(\n"
                            "    ignoring=True,\n"
                            "    child=ElevatedButton(\n"
                            "        onPressed=on_tap,\n"
                            "        child=Text('Try clicking me'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Scrollbar & ScrollbarOrientation",
                    description=(
                        "Scrollbar wraps a scroll view to show a draggable thumb. "
                        "ScrollbarOrientation pins the bar to one of four edges."
                    ),
                    instruction="Pick an orientation, then drag the scrollbar thumb.",
                    visible=_ScrollbarDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ctrl = ScrollController()\n\n"
                            "Scrollbar(\n"
                            "    controller=ctrl,\n"
                            "    thumbVisibility=True,\n"
                            "    trackVisibility=True,\n"
                            "    thickness=10.0,\n"
                            "    radius=Radius.circular(6.0),\n"
                            "    interactive=True,\n"
                            "    scrollbarOrientation=\n"
                            "        ScrollbarOrientation.right,\n"
                            "    child=SingleChildScrollView(\n"
                            "        controller=ctrl,\n"
                            "        child=long_column,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
