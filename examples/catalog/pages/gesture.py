from flut.dart import Brightness, Color, Duration, Offset
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    Expanded,
    SizedBox,
    Container,
    Stack,
    Positioned,
    GestureDetector,
    GestureRecognizerFactoryWithHandlers,
    RawGestureDetector,
    Align,
    Center,
    ClipRRect,
    Draggable,
    DragTarget,
    DraggableDetails,
    Icon,
    FocusNode,
    MouseRegion,
    WidgetStatePropertyAll,
)
from flut.flutter.gestures import (
    LongPressGestureRecognizer,
    TapGestureRecognizer,
    Velocity,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    MainAxisAlignment,
    HitTestBehavior,
)
from flut.flutter.material import (
    Colors,
    Theme,
    InkSplash,
    InkWell,
    Icons,
    IconButton,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Axis,
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    Alignment,
)
from flut.flutter.services import MouseCursor, SystemMouseCursors
from utils import CODE_FONT_FAMILY
from widgets import CatalogPage, SplitViewTile, CodeArea


class _DragVelocityDemo(StatefulWidget):
    def createState(self):
        return _DragVelocityDemoState()


class _DragVelocityDemoState(State[_DragVelocityDemo]):

    def initState(self):
        self.box_x = 100.0
        self.box_y = 100.0
        self.drag_start_global_x = 0.0
        self.drag_start_global_y = 0.0
        self.drag_start_box_x = 0.0
        self.drag_start_box_y = 0.0
        self.drag_status = "Drag the box around"
        self.velocity_text = ""
        self.start_text = ""

    def _on_pan_start(self, details):
        def update():
            self.drag_start_global_x = details.globalPosition.dx
            self.drag_start_global_y = details.globalPosition.dy
            self.drag_start_box_x = self.box_x
            self.drag_start_box_y = self.box_y
            kind_str = f" | Kind: {details.kind._flut_value}" if details.kind else ""
            ts_str = (
                f" | Timestamp: {details.sourceTimeStamp.inMicroseconds}µs"
                if details.sourceTimeStamp
                else ""
            )
            self.start_text = f"Start: ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f}){kind_str}{ts_str}"

        self.setState(update)

    def _on_pan_update(self, details):
        def update():
            self.box_x = self.drag_start_box_x + (
                details.globalPosition.dx - self.drag_start_global_x
            )
            self.box_y = self.drag_start_box_y + (
                details.globalPosition.dy - self.drag_start_global_y
            )
            self.drag_status = f"Position: ({self.box_x:.0f}, {self.box_y:.0f})"

        self.setState(update)

    def _on_pan_end(self, details):
        vel = details.velocity
        px = vel.pixelsPerSecond.dx
        py = vel.pixelsPerSecond.dy
        speed = (px**2 + py**2) ** 0.5

        def update():
            self.velocity_text = (
                f"Velocity: ({px:.0f}, {py:.0f}) px/s  |  Speed: {speed:.0f} px/s"
            )
            self.drag_status = f"Dropped at ({self.box_x:.0f}, {self.box_y:.0f})"

        self.setState(update)

    def _reset(self):
        def update():
            self.box_x = 100.0
            self.box_y = 100.0
            self.drag_status = "Drag the box around"
            self.velocity_text = ""
            self.start_text = ""

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        canvas_color = Color(0xFF2C2C2C) if is_dark else Color(0xFFF5F5F5)

        draggable_box = Positioned(
            left=self.box_x,
            top=self.box_y,
            child=GestureDetector(
                onPanStart=self._on_pan_start,
                onPanUpdate=self._on_pan_update,
                onPanEnd=self._on_pan_end,
                child=Container(
                    width=80.0,
                    height=80.0,
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=Align(
                        alignment=Alignment.center,
                        child=Text(
                            "Drag",
                            style=TextStyle(
                                color=Colors.white,
                                fontWeight=FontWeight.bold,
                            ),
                        ),
                    ),
                ),
            ),
        )

        canvas = Container(
            height=300.0,
            decoration=BoxDecoration(
                color=canvas_color,
                borderRadius=BorderRadius.circular(8),
            ),
            child=ClipRRect(
                borderRadius=BorderRadius.circular(8),
                child=Stack(
                    children=[
                        draggable_box,
                    ],
                ),
            ),
        )

        info_rows = [
            Text(self.drag_status, style=TextStyle(fontSize=14)),
        ]
        if self.start_text:
            info_rows.append(
                Text(self.start_text, style=TextStyle(fontSize=13, color=Colors.grey))
            )
        if self.velocity_text:
            info_rows.append(
                Text(
                    self.velocity_text, style=TextStyle(fontSize=13, color=Colors.grey)
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                canvas,
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=info_rows,
                ),
                SizedBox(height=16),
                GestureDetector(
                    onTap=self._reset,
                    child=Container(
                        padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                        decoration=BoxDecoration(
                            color=Colors.blue,
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Text(
                            "Reset Position",
                            style=TextStyle(color=Colors.white, fontSize=13),
                        ),
                    ),
                ),
            ],
        )


class _DragAndDropDemo(StatefulWidget):
    def createState(self):
        return _DragAndDropDemoState()


class _DragAndDropDemoState(State[_DragAndDropDemo]):

    def initState(self):
        self.items = ["Apple", "Banana", "Cherry"]
        self.accepted = []
        self.drag_status = ""

    def _on_accept(self, details):
        def update():
            item = details.data
            if item in self.items:
                self.items.remove(item)
            self.accepted.append(item)
            self.drag_status = f"Accepted: {item}"

        self.setState(update)

    def _on_will_accept(self, details):
        return True

    def _on_leave(self, data):
        def update():
            self.drag_status = "Left target"

        self.setState(update)

    def _reset(self):
        def update():
            self.items = ["Apple", "Banana", "Cherry"]
            self.accepted = []
            self.drag_status = ""

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark

        draggable_chips = []
        for item in self.items:
            chip = Draggable(
                data=item,
                feedback=Container(
                    padding=EdgeInsets.symmetric(horizontal=12, vertical=6),
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(16),
                    ),
                    child=Text(item, style=TextStyle(color=Colors.white, fontSize=13)),
                ),
                childWhenDragging=Container(
                    padding=EdgeInsets.symmetric(horizontal=12, vertical=6),
                    decoration=BoxDecoration(
                        color=Color(0xFFBDBDBD),
                        borderRadius=BorderRadius.circular(16),
                    ),
                    child=Text(item, style=TextStyle(color=Colors.white, fontSize=13)),
                ),
                onDragCompleted=lambda: None,
                child=Container(
                    padding=EdgeInsets.symmetric(horizontal=12, vertical=6),
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(16),
                    ),
                    child=Text(item, style=TextStyle(color=Colors.white, fontSize=13)),
                ),
            )
            draggable_chips.append(chip)
            draggable_chips.append(SizedBox(width=8))

        source_row = (
            Row(children=draggable_chips)
            if draggable_chips
            else Text(
                "All items dragged!",
                style=TextStyle(color=Colors.grey, fontSize=13),
            )
        )

        def _build_target(ctx, candidate_data, rejected_data):
            is_hovering = len(candidate_data) > 0 and candidate_data[0] is not None
            bg_color = (
                (Color(0xFF2E7D32) if is_hovering else Color(0xFF2C2C2C))
                if is_dark
                else (Color(0xFFE8F5E9) if is_hovering else Color(0xFFFAFAFA))
            )
            accepted_texts = [
                Container(
                    padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                    decoration=BoxDecoration(
                        color=Colors.green,
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=Text(
                        a,
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                )
                for a in self.accepted
            ]
            label = Text(
                "Drop here" if not self.accepted else f"{len(self.accepted)} items",
                style=TextStyle(fontSize=13, color=Colors.grey),
            )
            children = [label, SizedBox(height=8)]
            if accepted_texts:
                children.append(
                    Row(
                        mainAxisAlignment=MainAxisAlignment.center,
                        children=accepted_texts,
                    )
                )

            return Container(
                width=250.0,
                height=120.0,
                decoration=BoxDecoration(
                    color=bg_color,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Column(
                    mainAxisAlignment=MainAxisAlignment.center,
                    children=children,
                ),
            )

        target = DragTarget(
            builder=_build_target,
            onAcceptWithDetails=self._on_accept,
            onWillAcceptWithDetails=self._on_will_accept,
            onLeave=self._on_leave,
        )

        status_widgets = []
        if self.drag_status:
            status_widgets.append(
                Text(
                    self.drag_status,
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text("Drag these:", style=TextStyle(fontSize=14)),
                SizedBox(height=8),
                source_row,
                SizedBox(height=16),
                target,
                SizedBox(height=8),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=status_widgets,
                ),
                SizedBox(height=12),
                GestureDetector(
                    onTap=self._reset,
                    child=Container(
                        padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                        decoration=BoxDecoration(
                            color=Colors.blue,
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Text(
                            "Reset",
                            style=TextStyle(color=Colors.white, fontSize=13),
                        ),
                    ),
                ),
            ],
        )


class _ClampMagnitudeDemo(StatefulWidget):
    def createState(self):
        return _ClampMagnitudeDemoState()


class _ClampMagnitudeDemoState(State[_ClampMagnitudeDemo]):

    def initState(self):
        self.raw_text = ""
        self.clamped_text = ""
        self.ops_text = ""

    def _on_pan_end(self, details):
        vel = details.velocity
        raw_speed = (vel.pixelsPerSecond.dx**2 + vel.pixelsPerSecond.dy**2) ** 0.5
        clamped = vel.clampMagnitude(100.0, 500.0)
        clamped_speed = (
            clamped.pixelsPerSecond.dx**2 + clamped.pixelsPerSecond.dy**2
        ) ** 0.5

        negated = -vel
        added = vel + Velocity(pixelsPerSecond=Offset(100, 0))

        def update():
            self.raw_text = (
                f"Raw: ({vel.pixelsPerSecond.dx:.0f}, {vel.pixelsPerSecond.dy:.0f}) "
                f"| Speed: {raw_speed:.0f} px/s"
            )
            self.clamped_text = (
                f"Clamped [100..500]: ({clamped.pixelsPerSecond.dx:.0f}, {clamped.pixelsPerSecond.dy:.0f}) "
                f"| Speed: {clamped_speed:.0f} px/s"
            )
            self.ops_text = (
                f"Negated: ({negated.pixelsPerSecond.dx:.0f}, {negated.pixelsPerSecond.dy:.0f}) "
                f"| +100x: ({added.pixelsPerSecond.dx:.0f}, {added.pixelsPerSecond.dy:.0f})"
            )

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        canvas_color = Color(0xFF2C2C2C) if is_dark else Color(0xFFF5F5F5)

        info_rows = []
        if self.raw_text:
            info_rows.append(
                Text(self.raw_text, style=TextStyle(fontSize=13, color=Colors.grey))
            )
        if self.clamped_text:
            info_rows.append(
                Text(self.clamped_text, style=TextStyle(fontSize=13, color=Colors.blue))
            )
        if self.ops_text:
            info_rows.append(
                Text(self.ops_text, style=TextStyle(fontSize=13, color=Colors.grey))
            )
        if not info_rows:
            info_rows.append(
                Text(
                    "Swipe inside the box and release",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onPanEnd=self._on_pan_end,
                    child=Container(
                        width=300.0,
                        height=120.0,
                        decoration=BoxDecoration(
                            color=canvas_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Swipe here",
                                style=TextStyle(
                                    color=Colors.grey,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=info_rows,
                ),
            ],
        )


class _DraggableDetailsDemo(StatefulWidget):
    def createState(self):
        return _DraggableDetailsDemoState()


class _DraggableDetailsDemoState(State[_DraggableDetailsDemo]):

    def initState(self):
        self.was_accepted = ""
        self.velocity_text = ""
        self.offset_text = ""
        self.drag_count = 0

    def _on_drag_end(self, details):
        self.drag_count += 1
        vel = details.velocity
        px = vel.pixelsPerSecond.dx
        py = vel.pixelsPerSecond.dy

        def update():
            self.was_accepted = f"wasAccepted: {details.wasAccepted}"
            self.velocity_text = f"velocity: ({px:.0f}, {py:.0f}) px/s"
            self.offset_text = (
                f"offset: ({details.offset.dx:.0f}, {details.offset.dy:.0f})"
            )

        self.setState(update)

    def _on_accept(self, details):
        pass

    def _reset(self):
        def update():
            self.was_accepted = ""
            self.velocity_text = ""
            self.offset_text = ""
            self.drag_count = 0

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        canvas_color = Color(0xFF2C2C2C) if is_dark else Color(0xFFF5F5F5)

        circle = Draggable(
            data="circle",
            onDragEnd=self._on_drag_end,
            feedback=Container(
                width=60.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.blue.withValues(alpha=0.7),
                    borderRadius=BorderRadius.circular(30),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Drag",
                        style=TextStyle(
                            color=Colors.white,
                            fontSize=12,
                            fontWeight=FontWeight.bold,
                        ),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=60.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(30),
                ),
            ),
            child=Container(
                width=60.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(30),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Drag",
                        style=TextStyle(
                            color=Colors.white,
                            fontSize=12,
                            fontWeight=FontWeight.bold,
                        ),
                    ),
                ),
            ),
        )

        def _build_target(ctx, candidate_data, rejected_data):
            is_hovering = len(candidate_data) > 0 and candidate_data[0] is not None
            bg_color = (
                (Color(0xFF2E7D32) if is_hovering else Color(0xFF2C2C2C))
                if is_dark
                else (Color(0xFFE8F5E9) if is_hovering else Color(0xFFFAFAFA))
            )
            return Container(
                width=120.0,
                height=120.0,
                decoration=BoxDecoration(
                    color=bg_color,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Drop here",
                        style=TextStyle(fontSize=13, color=Colors.grey),
                    ),
                ),
            )

        target = DragTarget(
            builder=_build_target,
            onAcceptWithDetails=self._on_accept,
        )

        info_rows = []
        if self.was_accepted:
            info_rows.append(
                Text(
                    self.was_accepted,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.blue,
                    ),
                )
            )
        if self.velocity_text:
            info_rows.append(
                Text(
                    self.velocity_text,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.green,
                    ),
                )
            )
        if self.offset_text:
            info_rows.append(
                Text(
                    self.offset_text,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.orange,
                    ),
                )
            )
        if not info_rows:
            info_rows.append(
                Text(
                    "Drag the circle and release to see DraggableDetails",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        circle,
                        SizedBox(width=24),
                        target,
                    ],
                ),
                SizedBox(height=12),
                Container(
                    padding=EdgeInsets.all(12),
                    decoration=BoxDecoration(
                        color=canvas_color,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                f"DraggableDetails (drag #{self.drag_count})",
                                style=TextStyle(
                                    fontSize=14, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=4),
                            *info_rows,
                        ],
                    ),
                ),
                SizedBox(height=8),
                GestureDetector(
                    onTap=self._reset,
                    child=Container(
                        padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                        decoration=BoxDecoration(
                            color=Colors.blue,
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Text(
                            "Reset",
                            style=TextStyle(color=Colors.white, fontSize=13),
                        ),
                    ),
                ),
            ],
        )


class _TapLifecycleDemo(StatefulWidget):
    def createState(self):
        return _TapLifecycleDemoState()


class _TapLifecycleDemoState(State[_TapLifecycleDemo]):

    def initState(self):
        self.events = []

    def _on_tap_down(self, details):
        def update():
            self.events.append(
                f"onTapDown ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 3:
                self.events = self.events[-3:]

        self.setState(update)

    def _on_tap_up(self, details):
        def update():
            self.events.append(
                f"onTapUp ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 3:
                self.events = self.events[-3:]

        self.setState(update)

    def _on_tap_cancel(self):
        def update():
            self.events.append("onTapCancel")
            if len(self.events) > 3:
                self.events = self.events[-3:]

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF1565C0) if is_dark else Color(0xFF42A5F5)

        event_widgets = []
        for e in self.events:
            event_widgets.append(
                Text(
                    e,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                )
            )
        if not event_widgets:
            event_widgets.append(
                Text(
                    "Tap the box to see events",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onTapDown=self._on_tap_down,
                    onTapUp=self._on_tap_up,
                    onTapCancel=self._on_tap_cancel,
                    child=Container(
                        width=150.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Tap Me",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=event_widgets,
                ),
            ],
        )


class _IconButtonLongPressDemo(StatefulWidget):
    def createState(self):
        return _IconButtonLongPressState()


class _IconButtonLongPressState(State[_IconButtonLongPressDemo]):
    def initState(self):
        self.action = "None yet"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        IconButton(
                            icon=Icon(Icons.touch_app),
                            onPressed=lambda: self.setState(
                                lambda: setattr(self, "action", "Tapped!")
                            ),
                            onLongPress=lambda: self.setState(
                                lambda: setattr(self, "action", "Long-pressed!")
                            ),
                            tooltip="Tap or long-press",
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"Last action: {self.action}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _SecondaryTapDemo(StatefulWidget):
    def createState(self):
        return _SecondaryTapDemoState()


class _SecondaryTapDemoState(State[_SecondaryTapDemo]):

    def initState(self):
        self.events = []

    def _on_secondary_tap_down(self, details):
        def update():
            self.events.append(
                f"onSecondaryTapDown ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def _on_secondary_tap_up(self, details):
        def update():
            self.events.append(
                f"onSecondaryTapUp ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def _on_secondary_tap_cancel(self):
        def update():
            self.events.append("onSecondaryTapCancel")
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF6A1B9A) if is_dark else Color(0xFFAB47BC)

        event_widgets = []
        for e in self.events:
            event_widgets.append(
                Text(
                    e,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                )
            )
        if not event_widgets:
            event_widgets.append(
                Text(
                    "Right-click the box",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onSecondaryTapDown=self._on_secondary_tap_down,
                    onSecondaryTapUp=self._on_secondary_tap_up,
                    onSecondaryTapCancel=self._on_secondary_tap_cancel,
                    child=Container(
                        width=150.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Right Click",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=event_widgets,
                ),
            ],
        )


class _TertiaryTapDemo(StatefulWidget):
    def createState(self):
        return _TertiaryTapDemoState()


class _TertiaryTapDemoState(State[_TertiaryTapDemo]):

    def initState(self):
        self.events = []

    def _on_tertiary_tap_down(self, details):
        def update():
            self.events.append(
                f"onTertiaryTapDown ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def _on_tertiary_tap_up(self, details):
        def update():
            self.events.append(
                f"onTertiaryTapUp ({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def _on_tertiary_tap_cancel(self):
        def update():
            self.events.append("onTertiaryTapCancel")
            if len(self.events) > 5:
                self.events = self.events[-5:]

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF00695C) if is_dark else Color(0xFF26A69A)

        event_widgets = []
        for e in self.events:
            event_widgets.append(
                Text(
                    e,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                )
            )
        if not event_widgets:
            event_widgets.append(
                Text(
                    "Middle-click the box",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onTertiaryTapDown=self._on_tertiary_tap_down,
                    onTertiaryTapUp=self._on_tertiary_tap_up,
                    onTertiaryTapCancel=self._on_tertiary_tap_cancel,
                    child=Container(
                        width=150.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Middle Click",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=event_widgets,
                ),
            ],
        )


class _AxisDragDemo(StatefulWidget):
    def createState(self):
        return _AxisDragDemoState()


class _AxisDragDemoState(State[_AxisDragDemo]):

    def initState(self):
        self.vertical_delta = 0.0
        self.horizontal_delta = 0.0
        self.vertical_status = "Drag vertically"
        self.horizontal_status = "Drag horizontally"

    def _on_vertical_drag_start(self, details):
        def update():
            self.vertical_delta = 0.0
            self.vertical_status = "Vertical drag started"

        self.setState(update)

    def _on_vertical_drag_update(self, details):
        def update():
            self.vertical_delta += details.delta.dy
            self.vertical_status = f"V delta: {self.vertical_delta:.0f}"

        self.setState(update)

    def _on_vertical_drag_end(self, details):
        def update():
            self.vertical_status = f"V ended | delta: {self.vertical_delta:.0f}"

        self.setState(update)

    def _on_horizontal_drag_start(self, details):
        def update():
            self.horizontal_delta = 0.0
            self.horizontal_status = "Horizontal drag started"

        self.setState(update)

    def _on_horizontal_drag_update(self, details):
        def update():
            self.horizontal_delta += details.delta.dx
            self.horizontal_status = f"H delta: {self.horizontal_delta:.0f}"

        self.setState(update)

    def _on_horizontal_drag_end(self, details):
        def update():
            self.horizontal_status = f"H ended | delta: {self.horizontal_delta:.0f}"

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        v_color = Color(0xFF1B5E20) if is_dark else Color(0xFF66BB6A)
        h_color = Color(0xFFE65100) if is_dark else Color(0xFFFF9800)

        left_box = Expanded(
            child=GestureDetector(
                onVerticalDragStart=self._on_vertical_drag_start,
                onVerticalDragUpdate=self._on_vertical_drag_update,
                onVerticalDragEnd=self._on_vertical_drag_end,
                child=Container(
                    height=120.0,
                    decoration=BoxDecoration(
                        color=v_color,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Align(
                        alignment=Alignment.center,
                        child=Column(
                            mainAxisAlignment=MainAxisAlignment.center,
                            children=[
                                Text(
                                    "Vertical",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                SizedBox(height=4),
                                Text(
                                    self.vertical_status,
                                    style=TextStyle(color=Colors.white, fontSize=12),
                                ),
                            ],
                        ),
                    ),
                ),
            ),
        )

        right_box = Expanded(
            child=GestureDetector(
                onHorizontalDragStart=self._on_horizontal_drag_start,
                onHorizontalDragUpdate=self._on_horizontal_drag_update,
                onHorizontalDragEnd=self._on_horizontal_drag_end,
                child=Container(
                    height=120.0,
                    decoration=BoxDecoration(
                        color=h_color,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Align(
                        alignment=Alignment.center,
                        child=Column(
                            mainAxisAlignment=MainAxisAlignment.center,
                            children=[
                                Text(
                                    "Horizontal",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                SizedBox(height=4),
                                Text(
                                    self.horizontal_status,
                                    style=TextStyle(color=Colors.white, fontSize=12),
                                ),
                            ],
                        ),
                    ),
                ),
            ),
        )

        return Row(
            children=[
                left_box,
                SizedBox(width=12),
                right_box,
            ],
        )


class _PanDownCancelDemo(StatefulWidget):
    def createState(self):
        return _PanDownCancelDemoState()


class _PanDownCancelDemoState(State[_PanDownCancelDemo]):

    def initState(self):
        self.last_event = "Touch down on the box"

    def _on_pan_down(self, details):
        def update():
            self.last_event = (
                f"onPanDown ({details.globalPosition.dx:.0f}, "
                f"{details.globalPosition.dy:.0f})"
            )

        self.setState(update)

    def _on_pan_start(self, details):
        def update():
            self.last_event = (
                f"onPanStart ({details.globalPosition.dx:.0f}, "
                f"{details.globalPosition.dy:.0f})"
            )

        self.setState(update)

    def _on_pan_cancel(self):
        def update():
            self.last_event = "onPanCancel (drag did not materialize)"

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF4527A0) if is_dark else Color(0xFF7E57C2)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onPanDown=self._on_pan_down,
                    onPanStart=self._on_pan_start,
                    onPanCancel=self._on_pan_cancel,
                    child=Container(
                        width=180.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Touch Here",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    self.last_event,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _ScaleCallbacksDemo(StatefulWidget):
    def createState(self):
        return _ScaleCallbacksDemoState()


class _ScaleCallbacksDemoState(State[_ScaleCallbacksDemo]):

    def initState(self):
        self.scale_value = 1.0
        self.rotation_value = 0.0
        self.status = "Pinch or scroll to scale"

    def _on_scale_start(self, details):
        def update():
            self.status = (
                f"Scale started at ({details.focalPoint.dx:.0f}, "
                f"{details.focalPoint.dy:.0f})"
            )

        self.setState(update)

    def _on_scale_update(self, details):
        def update():
            self.scale_value = details.scale
            self.rotation_value = details.rotation
            self.status = (
                f"Scale: {self.scale_value:.2f} | "
                f"Rotation: {self.rotation_value:.3f} rad"
            )

        self.setState(update)

    def _on_scale_end(self, details):
        def update():
            self.status = (
                f"Scale ended | Final: {self.scale_value:.2f} | "
                f"Rot: {self.rotation_value:.3f}"
            )

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF37474F) if is_dark else Color(0xFF78909C)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onScaleStart=self._on_scale_start,
                    onScaleUpdate=self._on_scale_update,
                    onScaleEnd=self._on_scale_end,
                    child=Container(
                        width=200.0,
                        height=120.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Column(
                                mainAxisAlignment=MainAxisAlignment.center,
                                children=[
                                    Text(
                                        "Pinch / Scroll",
                                        style=TextStyle(
                                            color=Colors.white,
                                            fontWeight=FontWeight.bold,
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Text(
                                        f"Scale: {self.scale_value:.2f}",
                                        style=TextStyle(
                                            color=Colors.white, fontSize=13
                                        ),
                                    ),
                                    Text(
                                        f"Rotation: {self.rotation_value:.3f}",
                                        style=TextStyle(
                                            color=Colors.white, fontSize=13
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    self.status,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _DoubleTapLongPressDemo(StatefulWidget):
    def createState(self):
        return _DoubleTapLongPressDemoState()


class _DoubleTapLongPressDemoState(State[_DoubleTapLongPressDemo]):

    def initState(self):
        self.events = []

    def _append_event(self, text):
        def update():
            self.events.append(text)
            if len(self.events) > 6:
                self.events = self.events[-6:]

        self.setState(update)

    def _on_double_tap(self):
        self._append_event("onDoubleTap")

    def _on_long_press(self):
        self._append_event("onLongPress")

    def _on_long_press_start(self, details):
        self._append_event(
            f"onLongPressStart ({details.globalPosition.dx:.0f}, "
            f"{details.globalPosition.dy:.0f})"
        )

    def _on_long_press_move_update(self, details):
        self._append_event(
            f"onLongPressMoveUpdate offset=({details.offsetFromOrigin.dx:.0f}, "
            f"{details.offsetFromOrigin.dy:.0f})"
        )

    def _on_long_press_end(self, details):
        self._append_event(
            f"onLongPressEnd ({details.globalPosition.dx:.0f}, "
            f"{details.globalPosition.dy:.0f})"
        )

    def _on_long_press_up(self):
        self._append_event("onLongPressUp")

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFFC62828) if is_dark else Color(0xFFEF5350)

        event_widgets = []
        for e in self.events:
            event_widgets.append(
                Text(
                    e,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                )
            )
        if not event_widgets:
            event_widgets.append(
                Text(
                    "Double-tap or long-press the box",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onDoubleTap=self._on_double_tap,
                    onLongPress=self._on_long_press,
                    onLongPressStart=self._on_long_press_start,
                    onLongPressMoveUpdate=self._on_long_press_move_update,
                    onLongPressEnd=self._on_long_press_end,
                    onLongPressUp=self._on_long_press_up,
                    child=Container(
                        width=180.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Double Tap / Long Press",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                    fontSize=13,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=event_widgets,
                ),
            ],
        )


class _ExcludeSemanticsDemo(StatefulWidget):
    def createState(self):
        return _ExcludeSemanticsDemoState()


class _ExcludeSemanticsDemoState(State[_ExcludeSemanticsDemo]):

    def initState(self):
        self.default_count = 0
        self.excluded_count = 0

    def _on_tap_default(self):
        def update():
            self.default_count += 1

        self.setState(update)

    def _on_tap_excluded(self):
        def update():
            self.excluded_count += 1

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        color_a = Color(0xFF0D47A1) if is_dark else Color(0xFF42A5F5)
        color_b = Color(0xFF1B5E20) if is_dark else Color(0xFF66BB6A)

        left = Expanded(
            child=Column(
                children=[
                    GestureDetector(
                        onTap=self._on_tap_default,
                        excludeFromSemantics=False,
                        child=Container(
                            height=80.0,
                            decoration=BoxDecoration(
                                color=color_a,
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Align(
                                alignment=Alignment.center,
                                child=Text(
                                    "Default",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                            ),
                        ),
                    ),
                    SizedBox(height=8),
                    Text(
                        f"Taps: {self.default_count}",
                        style=TextStyle(fontSize=13),
                    ),
                    Text(
                        "excludeFromSemantics=False",
                        style=TextStyle(fontSize=11, color=Colors.grey),
                    ),
                ],
            ),
        )

        right = Expanded(
            child=Column(
                children=[
                    GestureDetector(
                        onTap=self._on_tap_excluded,
                        excludeFromSemantics=True,
                        child=Container(
                            height=80.0,
                            decoration=BoxDecoration(
                                color=color_b,
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Align(
                                alignment=Alignment.center,
                                child=Text(
                                    "Excluded",
                                    style=TextStyle(
                                        color=Colors.white,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                            ),
                        ),
                    ),
                    SizedBox(height=8),
                    Text(
                        f"Taps: {self.excluded_count}",
                        style=TextStyle(fontSize=13),
                    ),
                    Text(
                        "excludeFromSemantics=True",
                        style=TextStyle(fontSize=11, color=Colors.grey),
                    ),
                ],
            ),
        )

        return Row(
            children=[
                left,
                SizedBox(width=12),
                right,
            ],
        )


class _DraggableAffinityDemo(StatefulWidget):
    def createState(self):
        return _DraggableAffinityDemoState()


class _DraggableAffinityDemoState(State[_DraggableAffinityDemo]):

    def initState(self):
        self.h_status = "Drag horizontally"
        self.v_status = "Drag vertically"

    def _on_h_drag_end(self, details):
        def update():
            self.h_status = f"H dropped: wasAccepted={details.wasAccepted}"

        self.setState(update)

    def _on_v_drag_end(self, details):
        def update():
            self.v_status = f"V dropped: wasAccepted={details.wasAccepted}"

        self.setState(update)

    def build(self, context):
        h_draggable = Draggable(
            data="horizontal",
            affinity=Axis.horizontal,
            onDragEnd=self._on_h_drag_end,
            feedback=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.orange.withValues(alpha=0.8),
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "H drag",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(8),
                ),
            ),
            child=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.orange,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "H affinity",
                        style=TextStyle(
                            color=Colors.white,
                            fontWeight=FontWeight.bold,
                            fontSize=12,
                        ),
                    ),
                ),
            ),
        )

        v_draggable = Draggable(
            data="vertical",
            affinity=Axis.vertical,
            onDragEnd=self._on_v_drag_end,
            feedback=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.green.withValues(alpha=0.8),
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "V drag",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(8),
                ),
            ),
            child=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.green,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "V affinity",
                        style=TextStyle(
                            color=Colors.white,
                            fontWeight=FontWeight.bold,
                            fontSize=12,
                        ),
                    ),
                ),
            ),
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        h_draggable,
                        SizedBox(width=16),
                        v_draggable,
                    ],
                ),
                SizedBox(height=12),
                Text(
                    self.h_status,
                    style=TextStyle(fontSize=13, color=Colors.orange),
                ),
                Text(
                    self.v_status,
                    style=TextStyle(fontSize=13, color=Colors.green),
                ),
            ],
        )


class _DraggableIgnoringDemo(StatefulWidget):
    def createState(self):
        return _DraggableIgnoringDemoState()


class _DraggableIgnoringDemoState(State[_DraggableIgnoringDemo]):

    def initState(self):
        self.default_status = "Drag default"
        self.ignoring_status = "Drag ignoring"

    def _on_default_end(self, details):
        def update():
            self.default_status = f"Default dropped (accepted={details.wasAccepted})"

        self.setState(update)

    def _on_ignoring_end(self, details):
        def update():
            self.ignoring_status = f"Ignoring dropped (accepted={details.wasAccepted})"

        self.setState(update)

    def build(self, context):
        default_drag = Draggable(
            data="default",
            onDragEnd=self._on_default_end,
            ignoringFeedbackSemantics=False,
            ignoringFeedbackPointer=False,
            feedback=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.blue.withValues(alpha=0.8),
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Default",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(8),
                ),
            ),
            child=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Column(
                        mainAxisAlignment=MainAxisAlignment.center,
                        children=[
                            Text(
                                "Default",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                    fontSize=12,
                                ),
                            ),
                            Text(
                                "pointer=False",
                                style=TextStyle(color=Colors.white, fontSize=10),
                            ),
                        ],
                    ),
                ),
            ),
        )

        ignoring_drag = Draggable(
            data="ignoring",
            onDragEnd=self._on_ignoring_end,
            ignoringFeedbackSemantics=True,
            ignoringFeedbackPointer=True,
            feedback=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.green.withValues(alpha=0.8),
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Ignoring",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(8),
                ),
            ),
            child=Container(
                width=100.0,
                height=60.0,
                decoration=BoxDecoration(
                    color=Colors.green,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Column(
                        mainAxisAlignment=MainAxisAlignment.center,
                        children=[
                            Text(
                                "Ignoring",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                    fontSize=12,
                                ),
                            ),
                            Text(
                                "pointer=True",
                                style=TextStyle(color=Colors.white, fontSize=10),
                            ),
                        ],
                    ),
                ),
            ),
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        default_drag,
                        SizedBox(width=16),
                        ignoring_drag,
                    ],
                ),
                SizedBox(height=12),
                Text(
                    self.default_status,
                    style=TextStyle(fontSize=13, color=Colors.blue),
                ),
                Text(
                    self.ignoring_status,
                    style=TextStyle(fontSize=13, color=Colors.green),
                ),
            ],
        )


class _DragTargetHitTestDemo(StatefulWidget):
    def createState(self):
        return _DragTargetHitTestDemoState()


class _DragTargetHitTestDemoState(State[_DragTargetHitTestDemo]):

    def initState(self):
        self.translucent_hovering = False
        self.opaque_hovering = False
        self.status = "Drag the chip over the targets"

    def _on_will_accept_translucent(self, details):
        def update():
            self.translucent_hovering = True
            self.status = "Hovering over translucent target"

        self.setState(update)
        return True

    def _on_leave_translucent(self, data):
        def update():
            self.translucent_hovering = False

        self.setState(update)

    def _on_will_accept_opaque(self, details):
        def update():
            self.opaque_hovering = True
            self.status = "Hovering over opaque target"

        self.setState(update)
        return True

    def _on_leave_opaque(self, data):
        def update():
            self.opaque_hovering = False

        self.setState(update)

    def _on_accept(self, details):
        def update():
            self.translucent_hovering = False
            self.opaque_hovering = False
            self.status = f"Accepted: {details.data}"

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark

        draggable_chip = Draggable(
            data="test",
            feedback=Container(
                width=60.0,
                height=40.0,
                decoration=BoxDecoration(
                    color=Colors.blue.withValues(alpha=0.8),
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Drag",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
            ),
            childWhenDragging=Container(
                width=60.0,
                height=40.0,
                decoration=BoxDecoration(
                    color=Color(0xFFBDBDBD),
                    borderRadius=BorderRadius.circular(6),
                ),
            ),
            child=Container(
                width=60.0,
                height=40.0,
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(6),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Drag",
                        style=TextStyle(
                            color=Colors.white,
                            fontSize=12,
                            fontWeight=FontWeight.bold,
                        ),
                    ),
                ),
            ),
        )

        def _build_translucent(ctx, candidate_data, rejected_data):
            is_hov = len(candidate_data) > 0 and candidate_data[0] is not None
            bg = (
                (Color(0xFF1B5E20) if is_hov else Color(0xFF2C2C2C))
                if is_dark
                else (Color(0xFFE8F5E9) if is_hov else Color(0xFFF5F5F5))
            )
            return Container(
                width=200.0,
                height=80.0,
                decoration=BoxDecoration(
                    color=bg,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Translucent",
                        style=TextStyle(fontSize=13, color=Colors.grey),
                    ),
                ),
            )

        def _build_opaque(ctx, candidate_data, rejected_data):
            is_hov = len(candidate_data) > 0 and candidate_data[0] is not None
            bg = (
                (Color(0xFF0D47A1) if is_hov else Color(0xFF2C2C2C))
                if is_dark
                else (Color(0xFFE3F2FD) if is_hov else Color(0xFFF5F5F5))
            )
            return Container(
                width=200.0,
                height=80.0,
                decoration=BoxDecoration(
                    color=bg,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        "Opaque",
                        style=TextStyle(fontSize=13, color=Colors.grey),
                    ),
                ),
            )

        translucent_target = DragTarget(
            builder=_build_translucent,
            onWillAcceptWithDetails=self._on_will_accept_translucent,
            onLeave=self._on_leave_translucent,
            onAcceptWithDetails=self._on_accept,
            hitTestBehavior=HitTestBehavior.translucent,
        )

        opaque_target = DragTarget(
            builder=_build_opaque,
            onWillAcceptWithDetails=self._on_will_accept_opaque,
            onLeave=self._on_leave_opaque,
            onAcceptWithDetails=self._on_accept,
            hitTestBehavior=HitTestBehavior.opaque,
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                draggable_chip,
                SizedBox(height=12),
                Container(
                    height=130.0,
                    child=Stack(
                        children=[
                            Positioned(
                                left=0.0,
                                top=0.0,
                                child=translucent_target,
                            ),
                            Positioned(
                                left=60.0,
                                top=40.0,
                                child=opaque_target,
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                Text(
                    self.status,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _InkWellDemo(StatefulWidget):
    def createState(self):
        return _InkWellDemoState()


class _InkWellDemoState(State[_InkWellDemo]):
    def initState(self):
        self.inkwell_count = 0

    def build(self, context):
        return InkWell(
            onTap=lambda: self.setState(
                lambda: setattr(self, "inkwell_count", self.inkwell_count + 1)
            ),
            child=Container(
                padding=EdgeInsets.symmetric(horizontal=16, vertical=12),
                child=Row(
                    children=[
                        Icon(Icons.touch_app, color=Colors.blue),
                        SizedBox(width=8),
                        Text(
                            f"InkWell tapped {self.inkwell_count} times",
                            style=TextStyle(fontSize=14),
                        ),
                    ],
                ),
            ),
        )


class _InkWellDoubleTapDemo(StatefulWidget):
    def createState(self):
        return _InkWellDoubleTapDemoState()


class _InkWellDoubleTapDemoState(State[_InkWellDoubleTapDemo]):
    def initState(self):
        self.events = []

    def _log(self, event_name):
        self.events = (self.events + [event_name])[-5:]
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                InkWell(
                    onDoubleTap=lambda: self._log("double tap"),
                    onLongPress=lambda: self._log("long press"),
                    onLongPressUp=lambda: self._log("long press up"),
                    child=Container(
                        padding=EdgeInsets.all(16),
                        decoration=BoxDecoration(
                            color=Color(0xFFE3F2FD),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text("Double tap or long press me"),
                    ),
                ),
                SizedBox(height=8),
                *[
                    Text(
                        ev,
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    )
                    for ev in self.events
                ],
                *(
                    [
                        Text(
                            "No events yet",
                            style=TextStyle(fontSize=12, color=Colors.grey),
                        )
                    ]
                    if not self.events
                    else []
                ),
            ],
        )


class _InkWellSecondaryTapDemo(StatefulWidget):
    def createState(self):
        return _InkWellSecondaryTapDemoState()


class _InkWellSecondaryTapDemoState(State[_InkWellSecondaryTapDemo]):
    def initState(self):
        self.events = []

    def _log(self, event_name):
        self.events = (self.events + [event_name])[-5:]
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                InkWell(
                    onSecondaryTap=lambda: self._log("onSecondaryTap"),
                    onSecondaryTapDown=lambda d: self._log("onSecondaryTapDown"),
                    onSecondaryTapUp=lambda d: self._log("onSecondaryTapUp"),
                    child=Container(
                        padding=EdgeInsets.all(16),
                        decoration=BoxDecoration(
                            color=Color(0xFFFCE4EC),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text("Right-click me"),
                    ),
                ),
                SizedBox(height=8),
                *[
                    Text(
                        ev,
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    )
                    for ev in self.events
                ],
                *(
                    [
                        Text(
                            "No events yet",
                            style=TextStyle(fontSize=12, color=Colors.grey),
                        )
                    ]
                    if not self.events
                    else []
                ),
            ],
        )


class _InkWellStatesDemo(StatefulWidget):
    def createState(self):
        return _InkWellStatesDemoState()


class _InkWellStatesDemoState(State[_InkWellStatesDemo]):
    def initState(self):
        self.state_log = []

    def _on_hover(self, hovering):
        if hovering:
            self.state_log = (self.state_log + ["hovered"])[-5:]
        else:
            self.state_log = (self.state_log + ["unhovered"])[-5:]
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                InkWell(
                    onTap=lambda: self.setState(
                        lambda: setattr(
                            self,
                            "state_log",
                            (self.state_log + ["pressed"])[-5:],
                        )
                    ),
                    onHover=self._on_hover,
                    child=Container(
                        padding=EdgeInsets.all(16),
                        decoration=BoxDecoration(
                            color=Color(0xFFE8F5E9),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text("Hover and tap to see states"),
                    ),
                ),
                SizedBox(height=8),
                *[
                    Text(
                        s,
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    )
                    for s in self.state_log
                ],
                *(
                    [
                        Text(
                            "No states yet",
                            style=TextStyle(fontSize=12, color=Colors.grey),
                        )
                    ]
                    if not self.state_log
                    else []
                ),
            ],
        )


class _MouseRegionHoverDemo(StatefulWidget):
    def createState(self):
        return _MouseRegionHoverDemoState()


class _MouseRegionHoverDemoState(State[_MouseRegionHoverDemo]):
    def initState(self):
        self.hover_x = 0.0
        self.hover_y = 0.0
        self.is_hovering = False

    def _on_hover(self, event):
        self.hover_x = event.localPosition.dx
        self.hover_y = event.localPosition.dy
        self.is_hovering = True
        self.setState(lambda: None)

    def _on_exit(self, event):
        self.is_hovering = False
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                MouseRegion(
                    onHover=self._on_hover,
                    onExit=self._on_exit,
                    child=Container(
                        width=300.0,
                        height=120.0,
                        decoration=BoxDecoration(
                            color=Colors.blue.withValues(alpha=0.1),
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=Center(
                            child=Text(
                                (
                                    f"x={self.hover_x:.0f}, y={self.hover_y:.0f}"
                                    if self.is_hovering
                                    else "Hover over me"
                                ),
                                style=TextStyle(
                                    fontSize=16,
                                    fontFamily=CODE_FONT_FAMILY,
                                    color=(
                                        Colors.blue if self.is_hovering else Colors.grey
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "Move the mouse over the box to see live coordinates.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _TapMoveDemo(StatefulWidget):
    def createState(self):
        return _TapMoveDemoState()


class _TapMoveDemoState(State[_TapMoveDemo]):

    def initState(self):
        self.last_event = "Press and slide on the box"
        self.move_count = 0

    def _on_tap_down(self, details):
        def update():
            self.last_event = (
                f"onTapDown ({details.globalPosition.dx:.0f}, "
                f"{details.globalPosition.dy:.0f})"
            )
            self.move_count = 0

        self.setState(update)

    def _on_tap_move(self, details):
        def update():
            self.move_count += 1
            kind = details.kind._flut_value if details.kind else "?"
            self.last_event = (
                f"onTapMove #{self.move_count} kind={kind} "
                f"delta=({details.delta.dx:+.1f}, {details.delta.dy:+.1f})"
            )

        self.setState(update)

    def _on_tap_up(self, details):
        def update():
            self.last_event = f"onTapUp after {self.move_count} move events"

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF4527A0) if is_dark else Color(0xFF7E57C2)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onTapDown=self._on_tap_down,
                    onTapMove=self._on_tap_move,
                    onTapUp=self._on_tap_up,
                    child=Container(
                        width=220.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Press, slide, release",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    self.last_event,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _OnSecondaryTapDemo(StatefulWidget):
    def createState(self):
        return _OnSecondaryTapDemoState()


class _OnSecondaryTapDemoState(State[_OnSecondaryTapDemo]):

    def initState(self):
        self.count = 0

    def _on_secondary_tap(self):
        def update():
            self.count += 1

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF4E342E) if is_dark else Color(0xFF8D6E63)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onSecondaryTap=self._on_secondary_tap,
                    child=Container(
                        width=180.0,
                        height=80.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Right-click me",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    f"onSecondaryTap fired {self.count} time(s)",
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _LongPressDownDemo(StatefulWidget):
    def createState(self):
        return _LongPressDownDemoState()


class _LongPressDownDemoState(State[_LongPressDownDemo]):

    def initState(self):
        self.events = []

    def _push(self, text):
        def update():
            self.events.append(text)
            if len(self.events) > 6:
                self.events = self.events[-6:]

        self.setState(update)

    def _on_long_press_down(self, details):
        kind = details.kind._flut_value if details.kind else "?"
        self._push(
            f"onLongPressDown kind={kind} "
            f"({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
        )

    def _on_long_press_cancel(self):
        self._push("onLongPressCancel")

    def _on_long_press_start(self, details):
        self._push(
            f"onLongPressStart ({details.globalPosition.dx:.0f}, "
            f"{details.globalPosition.dy:.0f})"
        )

    def _on_long_press_end(self, details):
        self._push(
            f"onLongPressEnd ({details.globalPosition.dx:.0f}, "
            f"{details.globalPosition.dy:.0f})"
        )

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFFAD1457) if is_dark else Color(0xFFEC407A)

        event_widgets = []
        for e in self.events:
            event_widgets.append(
                Text(
                    e,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                )
            )
        if not event_widgets:
            event_widgets.append(
                Text(
                    "Press and hold (or press then release quickly to cancel)",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                GestureDetector(
                    onLongPressDown=self._on_long_press_down,
                    onLongPressCancel=self._on_long_press_cancel,
                    onLongPressStart=self._on_long_press_start,
                    onLongPressEnd=self._on_long_press_end,
                    child=Container(
                        width=220.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Press & hold",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=event_widgets,
                ),
            ],
        )


class _SecondaryTertiaryLongPressDemo(StatefulWidget):
    def createState(self):
        return _SecondaryTertiaryLongPressDemoState()


class _SecondaryTertiaryLongPressDemoState(State[_SecondaryTertiaryLongPressDemo]):

    def initState(self):
        self.secondary_count = 0
        self.tertiary_count = 0
        self.last = ""

    def _on_secondary_long_press_down(self, details):
        def update():
            self.last = (
                f"onSecondaryLongPressDown "
                f"({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )

        self.setState(update)

    def _on_secondary_long_press_start(self, details):
        def update():
            self.secondary_count += 1
            self.last = f"onSecondaryLongPressStart #{self.secondary_count}"

        self.setState(update)

    def _on_secondary_long_press_end(self, details):
        def update():
            self.last = "onSecondaryLongPressEnd"

        self.setState(update)

    def _on_secondary_long_press_cancel(self):
        def update():
            self.last = "onSecondaryLongPressCancel"

        self.setState(update)

    def _on_tertiary_long_press_down(self, details):
        def update():
            self.last = (
                f"onTertiaryLongPressDown "
                f"({details.globalPosition.dx:.0f}, {details.globalPosition.dy:.0f})"
            )

        self.setState(update)

    def _on_tertiary_long_press_start(self, details):
        def update():
            self.tertiary_count += 1
            self.last = f"onTertiaryLongPressStart #{self.tertiary_count}"

        self.setState(update)

    def _on_tertiary_long_press_end(self, details):
        def update():
            self.last = "onTertiaryLongPressEnd"

        self.setState(update)

    def _on_tertiary_long_press_cancel(self):
        def update():
            self.last = "onTertiaryLongPressCancel"

        self.setState(update)

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        secondary_color = Color(0xFF1565C0) if is_dark else Color(0xFF42A5F5)
        tertiary_color = Color(0xFF2E7D32) if is_dark else Color(0xFF66BB6A)

        secondary_box = GestureDetector(
            onSecondaryLongPressDown=self._on_secondary_long_press_down,
            onSecondaryLongPressStart=self._on_secondary_long_press_start,
            onSecondaryLongPressEnd=self._on_secondary_long_press_end,
            onSecondaryLongPressCancel=self._on_secondary_long_press_cancel,
            child=Container(
                width=160.0,
                height=80.0,
                decoration=BoxDecoration(
                    color=secondary_color,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        f"Secondary hold ({self.secondary_count})",
                        style=TextStyle(
                            color=Colors.white,
                            fontWeight=FontWeight.bold,
                            fontSize=12,
                        ),
                    ),
                ),
            ),
        )

        tertiary_box = GestureDetector(
            onTertiaryLongPressDown=self._on_tertiary_long_press_down,
            onTertiaryLongPressStart=self._on_tertiary_long_press_start,
            onTertiaryLongPressEnd=self._on_tertiary_long_press_end,
            onTertiaryLongPressCancel=self._on_tertiary_long_press_cancel,
            child=Container(
                width=160.0,
                height=80.0,
                decoration=BoxDecoration(
                    color=tertiary_color,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Align(
                    alignment=Alignment.center,
                    child=Text(
                        f"Tertiary hold ({self.tertiary_count})",
                        style=TextStyle(
                            color=Colors.white,
                            fontWeight=FontWeight.bold,
                            fontSize=12,
                        ),
                    ),
                ),
            ),
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        secondary_box,
                        SizedBox(width=12),
                        tertiary_box,
                    ],
                ),
                SizedBox(height=12),
                Text(
                    self.last or "Right-click-and-hold or middle-click-and-hold a box.",
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class _RawGestureDetectorDemo(StatefulWidget):
    def createState(self):
        return _RawGestureDetectorDemoState()


class _RawGestureDetectorDemoState(State[_RawGestureDetectorDemo]):
    def initState(self):
        self.tap_count = 0
        self.long_press_count = 0
        self.tap_init_count = 0
        self.long_press_init_count = 0
        self.last = "Tap or long-press the box"

    def _on_tap(self):
        def update():
            self.tap_count += 1
            self.last = f"onTap (#{self.tap_count})"

        self.setState(update)

    def _on_long_press(self):
        def update():
            self.long_press_count += 1
            self.last = f"onLongPress (#{self.long_press_count})"

        self.setState(update)

    def _build_tap_recognizer(self):
        return TapGestureRecognizer()

    def _init_tap_recognizer(self, instance):
        instance.onTap = self._on_tap
        self.tap_init_count += 1

    def _build_long_press_recognizer(self):
        return LongPressGestureRecognizer()

    def _init_long_press_recognizer(self, instance):
        instance.onLongPress = self._on_long_press
        self.long_press_init_count += 1

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        is_dark = scheme.brightness == Brightness.dark
        box_color = Color(0xFF00838F) if is_dark else Color(0xFF26C6DA)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                RawGestureDetector(
                    behavior=HitTestBehavior.opaque,
                    gestures={
                        TapGestureRecognizer: GestureRecognizerFactoryWithHandlers(
                            self._build_tap_recognizer,
                            self._init_tap_recognizer,
                        ),
                        LongPressGestureRecognizer: GestureRecognizerFactoryWithHandlers(
                            self._build_long_press_recognizer,
                            self._init_long_press_recognizer,
                        ),
                    },
                    child=Container(
                        width=220.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=box_color,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Align(
                            alignment=Alignment.center,
                            child=Text(
                                "Raw recognizers",
                                style=TextStyle(
                                    color=Colors.white,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    self.last,
                    style=TextStyle(
                        fontSize=13,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
                SizedBox(height=4),
                Text(
                    f"initializer calls — tap: {self.tap_init_count}, "
                    f"long-press: {self.long_press_init_count}",
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=Colors.grey,
                    ),
                ),
            ],
        )


class GesturePage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Drag & Gesture",
            description=(
                "Shows how pointer input becomes taps, pans, drags, and drop "
                "targets, with visible feedback for movement, velocity, and "
                "transferred data."
            ),
            children=[
                SplitViewTile(
                    title="Drag & Velocity",
                    description=(
                        "Uses GestureDetector onPanStart, onPanUpdate, and onPanEnd "
                        "to track a draggable box. Reports real-time position, drag "
                        "start coordinates, and release velocity with speed."
                    ),
                    instruction=(
                        "Drag the blue box around the canvas. Position updates in "
                        "real time. Release to see the velocity and speed of your "
                        "gesture. Click Reset Position to return the box to its origin."
                    ),
                    visible=_DragVelocityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onPanStart=on_pan_start,\n"
                            "    onPanUpdate=on_pan_update,\n"
                            "    onPanEnd=on_pan_end,\n"
                            "    child=Container(\n"
                            "        width=80.0,\n"
                            "        height=80.0,\n"
                            "        decoration=BoxDecoration(\n"
                            "            color=Colors.blue,\n"
                            "            borderRadius=BorderRadius.circular(12),\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Velocity clampMagnitude",
                    description=(
                        "Velocity.clampMagnitude clamps the speed to a range while "
                        "preserving direction. Also demonstrates +, -, and unary- operators."
                    ),
                    instruction=(
                        "Swipe inside the grey box and release. The raw velocity, "
                        "clamped velocity (100..500 px/s), and operator results are shown."
                    ),
                    visible=_ClampMagnitudeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "vel = details.velocity\n"
                            "clamped = vel.clampMagnitude(100.0, 500.0)\n"
                            "negated = -vel\n"
                            "combined = vel + Velocity(pixelsPerSecond=Offset(100, 0))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Draggable / DragTarget",
                    description=(
                        "Draggable widgets carry typed data that a DragTarget can accept. "
                        "Includes feedback and childWhenDragging visuals, plus "
                        "onAcceptWithDetails, onWillAcceptWithDetails, and onLeave callbacks."
                    ),
                    instruction=(
                        "Drag the fruit chips into the drop zone. The target highlights "
                        "when a draggable hovers over it and shows accepted items inside. "
                        "Click Reset to restore all chips."
                    ),
                    visible=_DragAndDropDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Draggable(\n"
                            "    data='Apple',\n"
                            "    feedback=Container(\n"
                            "        child=Text('Apple'),\n"
                            "    ),\n"
                            "    childWhenDragging=Container(\n"
                            "        child=Text('Apple'),\n"
                            "    ),\n"
                            "    child=Container(\n"
                            "        child=Text('Apple'),\n"
                            "    ),\n"
                            ")\n\n"
                            "DragTarget(\n"
                            "    builder=build_target,\n"
                            "    onAcceptWithDetails=on_accept,\n"
                            "    onWillAcceptWithDetails=on_will_accept,\n"
                            "    onLeave=on_leave,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DraggableDetails",
                    description=(
                        "Draggable.onDragEnd receives DraggableDetails with "
                        "wasAccepted (whether a DragTarget accepted it), "
                        "velocity.pixelsPerSecond, and offset of the drag end position."
                    ),
                    instruction=(
                        "Drag the blue circle freely or onto the drop target, then "
                        "release. The details panel shows wasAccepted, velocity, and "
                        "offset. Try both accepted and rejected drops."
                    ),
                    visible=_DraggableDetailsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Draggable(\n"
                            "    data='circle',\n"
                            "    onDragEnd=on_drag_end,\n"
                            "    feedback=circle_widget,\n"
                            "    child=circle_widget,\n"
                            ")\n\n"
                            "def on_drag_end(details):\n"
                            "    details.wasAccepted\n"
                            "    details.velocity.pixelsPerSecond\n"
                            "    details.offset"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector onTapDown/Up/Cancel",
                    description=(
                        "GestureDetector with onTapDown, onTapUp, and onTapCancel "
                        "callbacks. onTapDown and onTapUp receive details with the "
                        "global position of the tap event. onTapCancel fires when "
                        "a tap is aborted."
                    ),
                    instruction=(
                        "Tap the colored box to see the full tap lifecycle. Each "
                        "tap triggers onTapDown then onTapUp with coordinates. The "
                        "last 3 events are displayed below the box."
                    ),
                    visible=_TapLifecycleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onTapDown=on_tap_down,\n"
                            "    onTapUp=on_tap_up,\n"
                            "    onTapCancel=on_tap_cancel,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_tap_down(details):\n"
                            "    pos = details.globalPosition\n"
                            "    print(f'Down at ({pos.dx}, {pos.dy})')\n\n"
                            "def on_tap_up(details):\n"
                            "    pos = details.globalPosition\n"
                            "    print(f'Up at ({pos.dx}, {pos.dy})')\n\n"
                            "def on_tap_cancel():\n"
                            "    print('Tap cancelled')"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector secondary taps",
                    description=(
                        "GestureDetector with onSecondaryTapDown, onSecondaryTapUp, "
                        "and onSecondaryTapCancel. These callbacks respond to "
                        "right-click (secondary button) events with position details."
                    ),
                    instruction=(
                        "Right-click the purple box to trigger secondary tap events. "
                        "onSecondaryTapDown and onSecondaryTapUp log the global "
                        "position. The event log shows the last 5 events."
                    ),
                    visible=_SecondaryTapDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onSecondaryTapDown=on_secondary_down,\n"
                            "    onSecondaryTapUp=on_secondary_up,\n"
                            "    onSecondaryTapCancel=on_secondary_cancel,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_secondary_down(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_secondary_up(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_secondary_cancel():\n"
                            "    pass"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector tertiary taps",
                    description=(
                        "GestureDetector with onTertiaryTapDown, onTertiaryTapUp, "
                        "and onTertiaryTapCancel. These callbacks respond to "
                        "middle-click (tertiary button) events."
                    ),
                    instruction=(
                        "Middle-click the teal box to trigger tertiary tap events. "
                        "Each event is logged with its global position. The last "
                        "5 events are displayed."
                    ),
                    visible=_TertiaryTapDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onTertiaryTapDown=on_tertiary_down,\n"
                            "    onTertiaryTapUp=on_tertiary_up,\n"
                            "    onTertiaryTapCancel=on_tertiary_cancel,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_tertiary_down(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_tertiary_up(details):\n"
                            "    details.globalPosition"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector onTapMove",
                    description=(
                        "onTapMove fires while the pointer slides between onTapDown "
                        "and onTapUp. The TapMoveDetails object exposes kind, "
                        "globalPosition, localPosition, and a per-step delta."
                    ),
                    instruction=(
                        "Press inside the purple box and slide the pointer without "
                        "releasing. Each move tick is logged with its kind and delta."
                    ),
                    visible=_TapMoveDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onTapDown=on_tap_down,\n"
                            "    onTapMove=on_tap_move,\n"
                            "    onTapUp=on_tap_up,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_tap_move(details: TapMoveDetails):\n"
                            "    details.kind\n"
                            "    details.globalPosition\n"
                            "    details.delta"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector onSecondaryTap",
                    description=(
                        "onSecondaryTap is the bare 'right-click happened' callback, "
                        "fired when a secondary-button tap completes (no details "
                        "object). Use it when you only care that a right-click "
                        "occurred, independent of position tracking."
                    ),
                    instruction=(
                        "Right-click the brown box. The counter increments once per "
                        "completed secondary tap."
                    ),
                    visible=_OnSecondaryTapDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onSecondaryTap=lambda: ...,\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector long-press lifecycle (down/cancel)",
                    description=(
                        "onLongPressDown fires the moment a long-press contact lands "
                        "(LongPressDownDetails carries kind, globalPosition, "
                        "localPosition). onLongPressCancel fires if the gesture is "
                        "abandoned before the long-press timer triggers. "
                        "onLongPressStart / onLongPressEnd bracket the recognized "
                        "long-press."
                    ),
                    instruction=(
                        "Press and hold the pink box to see Down → Start → End. "
                        "Press and quickly release (or move outside) to see "
                        "Down → Cancel."
                    ),
                    visible=_LongPressDownDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onLongPressDown=on_lp_down,\n"
                            "    onLongPressCancel=on_lp_cancel,\n"
                            "    onLongPressStart=on_lp_start,\n"
                            "    onLongPressEnd=on_lp_end,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_lp_down(details: LongPressDownDetails):\n"
                            "    details.kind\n"
                            "    details.globalPosition\n\n"
                            "def on_lp_cancel():\n"
                            "    pass"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Secondary & tertiary long press",
                    description=(
                        "GestureDetector exposes the full long-press lifecycle "
                        "(Down / Cancel / Start / End) for the secondary and "
                        "tertiary mouse buttons too. Each variant fires "
                        "independently from the primary callbacks."
                    ),
                    instruction=(
                        "Right-click and hold the blue box for secondary callbacks. "
                        "Middle-click and hold the green box for tertiary callbacks. "
                        "The status line below shows the most recent event."
                    ),
                    visible=_SecondaryTertiaryLongPressDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onSecondaryLongPressDown=on_sec_down,\n"
                            "    onSecondaryLongPressStart=on_sec_start,\n"
                            "    onSecondaryLongPressEnd=on_sec_end,\n"
                            "    onSecondaryLongPressCancel=on_sec_cancel,\n"
                            "    onTertiaryLongPressDown=on_ter_down,\n"
                            "    onTertiaryLongPressStart=on_ter_start,\n"
                            "    onTertiaryLongPressEnd=on_ter_end,\n"
                            "    onTertiaryLongPressCancel=on_ter_cancel,\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="RawGestureDetector + recognizers",
                    description=(
                        "RawGestureDetector exposes Flutter's lower-level "
                        "Map<Type, GestureRecognizerFactory> API. Each entry "
                        "is a GestureRecognizerFactoryWithHandlers carrying "
                        "two callbacks: a constructor that creates the bare "
                        "recognizer, and an initializer that wires its "
                        "callbacks. Flutter invokes the initializer on every "
                        "rebuild so callback identities can refresh without "
                        "rebuilding the recognizer."
                    ),
                    instruction=(
                        "Tap or long-press the cyan box. The top line shows "
                        "the latest event; the bottom line shows how many "
                        "times each initializer has been invoked."
                    ),
                    visible=_RawGestureDetectorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "RawGestureDetector(\n"
                            "    behavior=HitTestBehavior.opaque,\n"
                            "    gestures={\n"
                            "        TapGestureRecognizer:\n"
                            "            GestureRecognizerFactoryWithHandlers(\n"
                            "                lambda: TapGestureRecognizer(),\n"
                            "                lambda r: setattr(r, 'onTap', on_tap),\n"
                            "            ),\n"
                            "        LongPressGestureRecognizer:\n"
                            "            GestureRecognizerFactoryWithHandlers(\n"
                            "                lambda: LongPressGestureRecognizer(),\n"
                            "                lambda r: setattr(r, 'onLongPress', on_long_press),\n"
                            "            ),\n"
                            "    },\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Vertical & horizontal drag",
                    description=(
                        "Two GestureDetectors side by side: the left box handles "
                        "onVerticalDragStart/Update/End only, the right handles "
                        "onHorizontalDragStart/Update/End only. Each tracks "
                        "cumulative drag delta on its locked axis."
                    ),
                    instruction=(
                        "Drag inside the green box to see vertical delta accumulate. "
                        "Drag inside the orange box to see horizontal delta. Each "
                        "box only responds to its designated axis."
                    ),
                    visible=_AxisDragDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onVerticalDragStart=on_v_start,\n"
                            "    onVerticalDragUpdate=on_v_update,\n"
                            "    onVerticalDragEnd=on_v_end,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "GestureDetector(\n"
                            "    onHorizontalDragStart=on_h_start,\n"
                            "    onHorizontalDragUpdate=on_h_update,\n"
                            "    onHorizontalDragEnd=on_h_end,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_v_update(details):\n"
                            "    delta_y += details.delta.dy\n\n"
                            "def on_h_update(details):\n"
                            "    delta_x += details.delta.dx"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="onPanDown & onPanCancel",
                    description=(
                        "GestureDetector with onPanDown, onPanStart, and onPanCancel. "
                        "onPanDown fires on initial contact with the global position. "
                        "onPanCancel fires if the gesture is abandoned before a drag "
                        "starts. onPanStart confirms the drag began."
                    ),
                    instruction=(
                        "Touch down on the box to see onPanDown with coordinates. "
                        "If you lift without dragging, onPanCancel fires. If you "
                        "start dragging, onPanStart fires instead."
                    ),
                    visible=_PanDownCancelDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onPanDown=on_pan_down,\n"
                            "    onPanStart=on_pan_start,\n"
                            "    onPanCancel=on_pan_cancel,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_pan_down(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_pan_start(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_pan_cancel():\n"
                            "    print('Pan cancelled')"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="GestureDetector scale callbacks",
                    description=(
                        "GestureDetector with onScaleStart, onScaleUpdate, and "
                        "onScaleEnd. onScaleUpdate provides live scale factor and "
                        "rotation in radians. The focal point is reported on start."
                    ),
                    instruction=(
                        "Use a pinch gesture or scroll wheel on the box to trigger "
                        "scale updates. The current scale factor and rotation values "
                        "update live inside the box and in the status text below."
                    ),
                    visible=_ScaleCallbacksDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onScaleStart=on_scale_start,\n"
                            "    onScaleUpdate=on_scale_update,\n"
                            "    onScaleEnd=on_scale_end,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_scale_start(details):\n"
                            "    details.focalPoint\n\n"
                            "def on_scale_update(details):\n"
                            "    details.scale\n"
                            "    details.rotation\n\n"
                            "def on_scale_end(details):\n"
                            "    pass"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="onDoubleTap & onLongPress lifecycle",
                    description=(
                        "GestureDetector with onDoubleTap, onLongPress, "
                        "onLongPressStart (with position), onLongPressMoveUpdate "
                        "(with offset from origin), onLongPressEnd (with position), "
                        "and onLongPressUp. Shows the full lifecycle of these gestures."
                    ),
                    instruction=(
                        "Double-tap the red box to trigger onDoubleTap. Long-press "
                        "and hold to see onLongPress, onLongPressStart, then move "
                        "to see onLongPressMoveUpdate, and release to see "
                        "onLongPressEnd and onLongPressUp."
                    ),
                    visible=_DoubleTapLongPressDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onDoubleTap=on_double_tap,\n"
                            "    onLongPress=on_long_press,\n"
                            "    onLongPressStart=on_lp_start,\n"
                            "    onLongPressMoveUpdate=on_lp_move,\n"
                            "    onLongPressEnd=on_lp_end,\n"
                            "    onLongPressUp=on_lp_up,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "def on_lp_start(details):\n"
                            "    details.globalPosition\n\n"
                            "def on_lp_move(details):\n"
                            "    details.offsetFromOrigin\n\n"
                            "def on_lp_end(details):\n"
                            "    details.globalPosition"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="IconButton onLongPress",
                    description="IconButton supports both onPressed and onLongPress callbacks for different interaction types.",
                    instruction="Tap the button to see 'Tapped!' or long-press it to see 'Long-pressed!' in the label below.",
                    visible=_IconButtonLongPressDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "IconButton(\n"
                            "    icon=Icon(Icons.touch_app),\n"
                            "    onPressed=lambda: print('tap'),\n"
                            "    onLongPress=lambda: print('long'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="excludeFromSemantics",
                    description=(
                        "Two GestureDetectors side by side: one with "
                        "excludeFromSemantics=False (default) and one with "
                        "excludeFromSemantics=True. Both have onTap and count "
                        "taps. The semantic difference affects accessibility "
                        "tree visibility."
                    ),
                    instruction=(
                        "Tap both boxes to increment their tap counters. Both "
                        "respond identically to taps. The difference is that the "
                        "right box with excludeFromSemantics=True is not visible "
                        "to the accessibility/semantics tree."
                    ),
                    visible=_ExcludeSemanticsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "GestureDetector(\n"
                            "    onTap=on_tap,\n"
                            "    excludeFromSemantics=False,\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "GestureDetector(\n"
                            "    onTap=on_tap,\n"
                            "    excludeFromSemantics=True,\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Draggable affinity",
                    description=(
                        "Two Draggables with different affinity values. "
                        "affinity=Axis.horizontal makes the drag recognizer prefer "
                        "horizontal movement to start the drag. affinity=Axis.vertical "
                        "prefers vertical movement. This controls which axis must be "
                        "detected first to initiate the drag."
                    ),
                    instruction=(
                        "Drag the orange box horizontally to start its drag "
                        "(horizontal affinity). Drag the green box vertically to "
                        "start its drag (vertical affinity). Release to see the "
                        "wasAccepted status."
                    ),
                    visible=_DraggableAffinityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Draggable(\n"
                            "    data='horizontal',\n"
                            "    affinity=Axis.horizontal,\n"
                            "    onDragEnd=on_drag_end,\n"
                            "    feedback=Container(...),\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "Draggable(\n"
                            "    data='vertical',\n"
                            "    affinity=Axis.vertical,\n"
                            "    onDragEnd=on_drag_end,\n"
                            "    feedback=Container(...),\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ignoringFeedbackSemantics & Pointer",
                    description=(
                        "Comparison of two Draggables: one with default settings "
                        "(ignoringFeedbackSemantics=False, ignoringFeedbackPointer=False) "
                        "and one with both set to True. When True, the feedback widget "
                        "does not participate in semantics and does not intercept "
                        "pointer events during the drag."
                    ),
                    instruction=(
                        "Drag both boxes and observe the behavior. The default "
                        "Draggable feedback intercepts pointer events. The ignoring "
                        "Draggable feedback passes pointer events through. Release "
                        "to see the wasAccepted status for each."
                    ),
                    visible=_DraggableIgnoringDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Draggable(\n"
                            "    data='default',\n"
                            "    ignoringFeedbackSemantics=False,\n"
                            "    ignoringFeedbackPointer=False,\n"
                            "    feedback=Container(...),\n"
                            "    child=Container(...),\n"
                            ")\n\n"
                            "Draggable(\n"
                            "    data='ignoring',\n"
                            "    ignoringFeedbackSemantics=True,\n"
                            "    ignoringFeedbackPointer=True,\n"
                            "    feedback=Container(...),\n"
                            "    child=Container(...),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DragTarget hitTestBehavior",
                    description=(
                        "Two DragTargets stacked in a Stack with different "
                        "hitTestBehavior values. HitTestBehavior.translucent allows "
                        "hit test events to pass through to widgets behind it. "
                        "HitTestBehavior.opaque absorbs all hit test events, blocking "
                        "widgets behind it from receiving them."
                    ),
                    instruction=(
                        "Drag the chip over the overlapping area of the two targets. "
                        "The translucent target (bottom) and opaque target (top, offset) "
                        "change color when a draggable hovers. Drop onto either target "
                        "to accept."
                    ),
                    visible=_DragTargetHitTestDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DragTarget(\n"
                            "    builder=build_translucent,\n"
                            "    onAcceptWithDetails=on_accept,\n"
                            "    hitTestBehavior=HitTestBehavior.translucent,\n"
                            ")\n\n"
                            "DragTarget(\n"
                            "    builder=build_opaque,\n"
                            "    onAcceptWithDetails=on_accept,\n"
                            "    hitTestBehavior=HitTestBehavior.opaque,\n"
                            ")\n\n"
                            "Stack(\n"
                            "    children=[\n"
                            "        Positioned(child=translucent_target),\n"
                            "        Positioned(child=opaque_target),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell",
                    description=(
                        "A rectangular area that responds to touch with a Material ripple effect. "
                        "Unlike GestureDetector, InkWell provides visual feedback on tap."
                    ),
                    instruction="Tap the area to see the ripple effect and increment the counter.",
                    visible=_InkWellDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onTap=on_tap,\n"
                            "    child=Container(\n"
                            "        child=Text('Tap me'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MouseRegion",
                    description=(
                        "Tracks mouse enter, exit, and hover events. Use the cursor property "
                        "with SystemMouseCursors to change the pointer appearance."
                    ),
                    instruction="Move your mouse over each box to see different cursor styles.",
                    visible=Row(
                        children=[
                            MouseRegion(
                                cursor=SystemMouseCursors.click,
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFE3F2FD),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("click", style=TextStyle(fontSize=13)),
                                ),
                            ),
                            SizedBox(width=8),
                            MouseRegion(
                                cursor=SystemMouseCursors.text,
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFFCE4EC),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("text", style=TextStyle(fontSize=13)),
                                ),
                            ),
                            SizedBox(width=8),
                            MouseRegion(
                                cursor=SystemMouseCursors.grab,
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFE8F5E9),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("grab", style=TextStyle(fontSize=13)),
                                ),
                            ),
                            SizedBox(width=8),
                            MouseRegion(
                                cursor=MouseCursor.defer,
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFF3E5F5),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text("defer", style=TextStyle(fontSize=13)),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "MouseRegion(\n"
                            "    cursor=SystemMouseCursors.click,\n"
                            "    child=Container(child=Text('click')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MouseRegion onHover",
                    description=(
                        "MouseRegion onHover callback fires continuously as the mouse "
                        "moves over the widget, providing the pointer position."
                    ),
                    instruction="Hover over the box to see live pointer coordinates update in real time.",
                    visible=_MouseRegionHoverDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets import MouseRegion\n\n"
                            "MouseRegion(\n"
                            "    onHover=lambda event: print(\n"
                            "        event.localPosition.dx,\n"
                            "        event.localPosition.dy,\n"
                            "    ),\n"
                            "    child=Container(width=300, height=120),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell onDoubleTap & onLongPress",
                    description=(
                        "InkWell that logs double tap, long press, and long press up events "
                        "in a text area below."
                    ),
                    instruction="Double-tap or long-press the area to see events logged.",
                    visible=_InkWellDoubleTapDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onDoubleTap=on_double_tap,\n"
                            "    onLongPress=on_long_press,\n"
                            "    onLongPressUp=on_long_press_up,\n"
                            "    child=Container(child=Text('Tap me')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell secondary taps",
                    description=(
                        "InkWell logging onSecondaryTap, onSecondaryTapDown, and "
                        "onSecondaryTapUp events."
                    ),
                    instruction="Right-click the area to trigger secondary tap events.",
                    visible=_InkWellSecondaryTapDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onSecondaryTap=on_secondary_tap,\n"
                            "    onSecondaryTapDown=on_down,\n"
                            "    onSecondaryTapUp=on_up,\n"
                            "    child=Container(child=Text('Right-click')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell colors & overlayColor",
                    description=(
                        "InkWell with focusColor=green, hoverColor=amber, highlightColor=red, "
                        "splashColor=purple, overlayColor=blue."
                    ),
                    instruction="Hover and tap the area to see colorful effects.",
                    visible=InkWell(
                        onTap=lambda: None,
                        focusColor=Colors.green,
                        hoverColor=Colors.amber,
                        highlightColor=Colors.red,
                        splashColor=Colors.purple,
                        overlayColor=WidgetStatePropertyAll(Color(0x330000FF)),
                        child=Container(
                            padding=EdgeInsets.all(16),
                            decoration=BoxDecoration(
                                color=Color(0xFFF5F5F5),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text("Colorful InkWell"),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onTap=on_tap,\n"
                            "    focusColor=Colors.green,\n"
                            "    hoverColor=Colors.amber,\n"
                            "    highlightColor=Colors.red,\n"
                            "    splashColor=Colors.purple,\n"
                            "    overlayColor=WidgetStatePropertyAll(\n"
                            "        Color(0x330000FF),\n"
                            "    ),\n"
                            "    child=Container(child=Text('Tap me')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell splashFactory & radius",
                    description=(
                        "InkWell with InkSplash.splashFactory(), radius=50, and "
                        "borderRadius=20 for a large centered splash effect."
                    ),
                    instruction="Tap the area to see the large splash with rounded border.",
                    visible=InkWell(
                        onTap=lambda: None,
                        splashFactory=InkSplash.splashFactory(),
                        radius=50,
                        borderRadius=BorderRadius.circular(20),
                        child=Container(
                            padding=EdgeInsets.symmetric(horizontal=32, vertical=24),
                            decoration=BoxDecoration(
                                color=Color(0xFFE3F2FD),
                                borderRadius=BorderRadius.circular(20),
                            ),
                            child=Text("Large splash"),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onTap=on_tap,\n"
                            "    splashFactory=InkSplash.splashFactory(),\n"
                            "    radius=50,\n"
                            "    borderRadius=BorderRadius.circular(20),\n"
                            "    child=Container(child=Text('Tap me')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell focusNode & statesController",
                    description=(
                        "InkWell with onHover logging state changes (hovered, pressed). "
                        "The current states are displayed below."
                    ),
                    instruction="Hover and tap the area to see state changes logged.",
                    visible=_InkWellStatesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onTap=on_tap,\n"
                            "    onHover=on_hover,\n"
                            "    child=Container(\n"
                            "        child=Text('Hover and tap'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="InkWell enableFeedback & hoverDuration",
                    description=(
                        "InkWell with enableFeedback=False, excludeFromSemantics=True, "
                        "and hoverDuration=Duration(seconds=1) for slow hover effect."
                    ),
                    instruction="Hover slowly over the area to observe the delayed effect.",
                    visible=InkWell(
                        onTap=lambda: None,
                        enableFeedback=False,
                        excludeFromSemantics=True,
                        hoverDuration=Duration(seconds=1),
                        hoverColor=Color(0x33FF9800),
                        child=Container(
                            padding=EdgeInsets.all(16),
                            decoration=BoxDecoration(
                                color=Color(0xFFF5F5F5),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text("Slow hover, no feedback"),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InkWell(\n"
                            "    onTap=on_tap,\n"
                            "    enableFeedback=False,\n"
                            "    excludeFromSemantics=True,\n"
                            "    hoverDuration=Duration(seconds=1),\n"
                            "    child=Container(\n"
                            "        child=Text('Slow hover'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
