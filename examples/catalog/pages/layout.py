import math

from utils import CODE_FONT_FAMILY
from flut.dart import (
    BlurStyle,
    Color,
    Duration,
    Radius,
    Rect,
    RRect,
    Size,
    TextAlign,
    TextBaseline,
    PlaceholderAlignment,
    ViewPadding,
)
from flut.dart.ui import Clip, TextDirection, FilterQuality, BlendMode, Offset
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
    Flexible,
    Opacity,
    Spacer,
    Wrap,
    Padding,
    Icon,
    MediaQuery,
    WidgetSpan,
    AspectRatio,
    FittedBox,
    ConstrainedBox,
    LayoutBuilder,
    Align,
    ClipRRect,
    Stack,
    Positioned,
    GestureDetector,
    ListView,
    CustomScrollView,
    SliverToBoxAdapter,
    ScrollViewKeyboardDismissBehavior,
    ScrollPhysics,
    MouseRegion,
    Transform,
    SingleChildScrollView,
    AnimatedContainer,
    InteractiveViewer,
    PanAxis,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    MainAxisAlignment,
    MainAxisSize,
    FlexFit,
    WrapAlignment,
    WrapCrossAlignment,
    BoxConstraints,
    HitTestBehavior,
)
from flut.flutter.material import (
    ButtonStyle,
    Colors,
    ElevatedButton,
    Icons,
    Tooltip,
    TextField,
    InputDecoration,
    Card,
    Divider,
    Material,
    MaterialType,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import TextOverflow
from flut.flutter.painting import (
    Alignment,
    BeveledRectangleBorder,
    Border,
    BorderSide,
    BorderStyle,
    ContinuousRectangleBorder,
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BoxShadow,
    BorderRadius,
    BorderRadiusDirectional,
    BorderRadiusGeometry,
    EdgeInsetsDirectional,
    EdgeInsetsGeometry,
    TextSpan,
    Axis,
    BoxFit,
    AxisDirection,
    VerticalDirection,
    GradientRotation,
    LinearGradient,
    RadialGradient,
    RoundedRectangleBorder,
    CircleBorder,
    StadiumBorder,
    SweepGradient,
)
from flut.flutter.animation import Curves
from flut.flutter.rendering.viewport import SliverPaintOrder
from flut.flutter.painting.box_border import BoxShape
from flut.flutter.widgets.overflow_bar import OverflowBarAlignment

from widgets import CatalogPage, SplitViewTile, CodeArea


def _info_card(title, subtitle, icon):
    return Card(
        elevation=2.0,
        margin=EdgeInsets.only(bottom=12),
        child=Padding(
            padding=EdgeInsets.all(16),
            child=Row(
                children=[
                    Icon(icon, color=Colors.blue),
                    SizedBox(width=16),
                    Expanded(
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Text(
                                    title,
                                    style=TextStyle(
                                        fontSize=16,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                SizedBox(height=4),
                                Text(
                                    subtitle,
                                    style=TextStyle(
                                        fontSize=13,
                                        color=Colors.grey,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    )


class _BlurStyleCard(StatelessWidget):
    def __init__(self, label, blur_style):
        super().__init__()
        self.label = label
        self.blur_style = blur_style

    def build(self, context):
        return Column(
            children=[
                Container(
                    width=80.0,
                    height=80.0,
                    decoration=BoxDecoration(
                        color=Colors.white,
                        borderRadius=BorderRadius.circular(8),
                        boxShadow=[
                            BoxShadow(
                                color=Color(0x80000000),
                                blurRadius=10.0,
                                spreadRadius=2.0,
                                blurStyle=self.blur_style,
                            ),
                        ],
                    ),
                ),
                SizedBox(height=8),
                Text(self.label, style=TextStyle(fontSize=11)),
            ],
        )


class _OpacityDemo(StatefulWidget):
    def createState(self):
        return _OpacityDemoState()


class _OpacityDemoState(State[_OpacityDemo]):
    def initState(self):
        self.opacity_value = 1.0

    def _toggle(self):
        self.opacity_value = 0.2 if self.opacity_value == 1.0 else 1.0
        self.setState(lambda: None)

    def build(self, context):
        return Row(
            children=[
                ElevatedButton(
                    child=Text("Toggle Opacity"),
                    onPressed=self._toggle,
                ),
                SizedBox(width=16),
                Opacity(
                    opacity=self.opacity_value,
                    child=Container(
                        padding=EdgeInsets.all(12),
                        decoration=BoxDecoration(
                            color=Colors.blue,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Text(
                            f"opacity={self.opacity_value}",
                            style=TextStyle(color=Colors.white),
                        ),
                    ),
                ),
            ],
        )


class _MainAxisSizeDemo(StatefulWidget):
    def createState(self):
        return _MainAxisSizeDemoState()


class _MainAxisSizeDemoState(State[_MainAxisSizeDemo]):
    def initState(self):
        self.use_min_size = False

    def _toggle(self):
        self.use_min_size = not self.use_min_size
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle MainAxisSize"),
                            onPressed=self._toggle,
                        ),
                        SizedBox(width=12),
                        Text(
                            f"MainAxisSize.{'min' if self.use_min_size else 'max'}",
                            style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    padding=EdgeInsets.all(8),
                    child=Row(
                        mainAxisSize=(
                            MainAxisSize.min if self.use_min_size else MainAxisSize.max
                        ),
                        children=[
                            Container(
                                width=60.0,
                                height=40.0,
                                color=Colors.blue,
                                child=Center(
                                    child=Text(
                                        "A", style=TextStyle(color=Colors.white)
                                    ),
                                ),
                            ),
                            SizedBox(width=8),
                            Container(
                                width=60.0,
                                height=40.0,
                                color=Colors.teal,
                                child=Center(
                                    child=Text(
                                        "B", style=TextStyle(color=Colors.white)
                                    ),
                                ),
                            ),
                            SizedBox(width=8),
                            Container(
                                width=60.0,
                                height=40.0,
                                color=Colors.deepPurple,
                                child=Center(
                                    child=Text(
                                        "C", style=TextStyle(color=Colors.white)
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )


class _VerticalDirectionDemo(StatefulWidget):
    def createState(self):
        return _VerticalDirectionDemoState()


class _VerticalDirectionDemoState(State[_VerticalDirectionDemo]):
    def initState(self):
        self.use_up = False

    def build(self, context):
        items = [
            Container(
                width=200.0,
                height=40.0,
                color=Colors.red,
                child=Center(
                    child=Text("1 - Red", style=TextStyle(color=Colors.white)),
                ),
            ),
            Container(
                width=200.0,
                height=40.0,
                color=Colors.green,
                child=Center(
                    child=Text("2 - Green", style=TextStyle(color=Colors.white)),
                ),
            ),
            Container(
                width=200.0,
                height=40.0,
                color=Colors.blue,
                child=Center(
                    child=Text("3 - Blue", style=TextStyle(color=Colors.white)),
                ),
            ),
        ]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Direction"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(self, "use_up", not self.use_up)
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"VerticalDirection.{'up' if self.use_up else 'down'}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    verticalDirection=(
                        VerticalDirection.up if self.use_up else VerticalDirection.down
                    ),
                    spacing=4,
                    children=items,
                ),
            ],
        )


class _MediaQueryDemo(StatelessWidget):
    def build(self, context):
        media = MediaQuery.of(context)
        return Container(
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Color(0xFFF5F5F5),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        f"Screen: {media.size.width:.0f} \u00d7 {media.size.height:.0f}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Pixel ratio: {media.devicePixelRatio:.1f}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Brightness: {media.platformBrightness}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Text scale: {media.textScaler.scale(1.0):.2f}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Padding: L={media.padding.left:.0f} T={media.padding.top:.0f} "
                        f"R={media.padding.right:.0f} B={media.padding.bottom:.0f}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"View insets: L={media.viewInsets.left:.0f} T={media.viewInsets.top:.0f} "
                        f"R={media.viewInsets.right:.0f} B={media.viewInsets.bottom:.0f}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Navigation: {media.navigationMode}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                    Text(
                        f"Gesture touchSlop: {media.gestureSettings.touchSlop}",
                        style=TextStyle(fontSize=13, fontFamily=CODE_FONT_FAMILY),
                    ),
                ],
            ),
        )


def _text_align_box(label, align):
    return Container(
        width=110.0,
        padding=EdgeInsets.all(8),
        decoration=BoxDecoration(
            color=Color(0xFFF5F5F5),
            borderRadius=BorderRadius.circular(8),
        ),
        child=Column(
            crossAxisAlignment=CrossAxisAlignment.stretch,
            children=[
                Text(
                    label,
                    style=TextStyle(
                        fontSize=11, color=Colors.grey, fontFamily=CODE_FONT_FAMILY
                    ),
                ),
                SizedBox(height=4),
                Text("Sample text", textAlign=align, style=TextStyle(fontSize=14)),
            ],
        ),
    )


def _padding_box(label, ei):
    return Column(
        children=[
            Container(
                decoration=BoxDecoration(
                    color=Color(0xFFBBDEFB),
                    borderRadius=BorderRadius.circular(6),
                ),
                padding=ei,
                child=Container(
                    width=60.0,
                    height=40.0,
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(4),
                    ),
                    child=Center(
                        child=Text(
                            "content",
                            style=TextStyle(color=Colors.white, fontSize=10),
                        ),
                    ),
                ),
            ),
            SizedBox(height=4),
            Text(label, style=TextStyle(fontSize=11)),
        ],
    )


def _br_card(label, br):
    return Column(
        children=[
            Container(
                width=120.0,
                height=80.0,
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=br,
                ),
                child=Center(
                    child=Text(
                        label,
                        style=TextStyle(color=Colors.white, fontSize=10),
                        textAlign=TextAlign.center,
                    ),
                ),
            ),
            SizedBox(height=4),
            Text(label, style=TextStyle(fontSize=11)),
        ],
    )


class _AxisDirectionDemo(StatefulWidget):
    def createState(self):
        return _AxisDirectionDemoState()


class _AxisDirectionDemoState(State[_AxisDirectionDemo]):
    def initState(self):
        self.direction_index = 0

    def build(self, context):
        directions = [
            ("AxisDirection.down", Axis.vertical, False),
            ("AxisDirection.up", Axis.vertical, True),
            ("AxisDirection.right", Axis.horizontal, False),
            ("AxisDirection.left", Axis.horizontal, True),
        ]
        current = directions[self.direction_index]
        colors = [Colors.red, Colors.green, Colors.blue, Colors.orange, Colors.purple]
        is_horizontal = current[1] == Axis.horizontal

        items = [
            SliverToBoxAdapter(
                child=Container(
                    width=80.0 if is_horizontal else None,
                    height=50.0,
                    color=colors[i],
                    child=Center(
                        child=Text(
                            f"Item {i + 1}",
                            style=TextStyle(color=Colors.white, fontSize=12),
                        ),
                    ),
                ),
            )
            for i in range(5)
        ]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Cycle Direction"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "direction_index",
                                    (self.direction_index + 1) % 4,
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(current[0], style=TextStyle(fontSize=13)),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    height=200.0 if not is_horizontal else 80.0,
                    width=350.0 if is_horizontal else None,
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=CustomScrollView(
                        scrollDirection=current[1],
                        reverse=current[2],
                        slivers=items,
                    ),
                ),
            ],
        )


class _SliverPaintOrderDemo(StatefulWidget):
    def createState(self):
        return _SliverPaintOrderDemoState()


class _SliverPaintOrderDemoState(State[_SliverPaintOrderDemo]):
    def initState(self):
        self.first_is_top = True

    def build(self, context):
        order = (
            SliverPaintOrder.firstIsTop
            if self.first_is_top
            else SliverPaintOrder.lastIsTop
        )
        order_label = "firstIsTop" if self.first_is_top else "lastIsTop"

        colors = [
            (Colors.red, "First (Red)"),
            (Colors.green, "Second (Green)"),
            (Colors.blue, "Third (Blue)"),
        ]

        children = [
            Positioned(
                left=i * 40.0,
                top=i * 20.0,
                child=Container(
                    width=120.0,
                    height=60.0,
                    decoration=BoxDecoration(
                        color=color,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Center(
                        child=Text(
                            label,
                            style=TextStyle(color=Colors.white, fontSize=11),
                        ),
                    ),
                ),
            )
            for i, (color, label) in enumerate(
                colors if self.first_is_top else reversed(list(enumerate(colors)))
            )
        ]

        stacked_children = []
        if self.first_is_top:
            for i, (color, label) in enumerate(colors):
                stacked_children.append(
                    Positioned(
                        left=i * 40.0,
                        top=i * 20.0,
                        child=Container(
                            width=120.0,
                            height=60.0,
                            decoration=BoxDecoration(
                                color=color,
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Center(
                                child=Text(
                                    label,
                                    style=TextStyle(color=Colors.white, fontSize=11),
                                ),
                            ),
                        ),
                    )
                )
        else:
            for i, (color, label) in enumerate(reversed(colors)):
                stacked_children.append(
                    Positioned(
                        left=(2 - i) * 40.0,
                        top=(2 - i) * 20.0,
                        child=Container(
                            width=120.0,
                            height=60.0,
                            decoration=BoxDecoration(
                                color=color,
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Center(
                                child=Text(
                                    label,
                                    style=TextStyle(color=Colors.white, fontSize=11),
                                ),
                            ),
                        ),
                    )
                )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Paint Order"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "first_is_top", not self.first_is_top
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"SliverPaintOrder.{order_label}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    width=280.0,
                    height=120.0,
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Stack(
                        clipBehavior=Clip.none,
                        children=stacked_children,
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "firstIsTop: first sliver paints on top (z-order).\n"
                    "lastIsTop: last sliver paints on top.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _ScrollViewKeyboardDismissDemo(StatefulWidget):
    def createState(self):
        return _ScrollViewKeyboardDismissDemoState()


class _ScrollViewKeyboardDismissDemoState(State[_ScrollViewKeyboardDismissDemo]):
    def initState(self):
        self.use_on_drag = False

    def build(self, context):
        behavior = (
            ScrollViewKeyboardDismissBehavior.onDrag
            if self.use_on_drag
            else ScrollViewKeyboardDismissBehavior.manual
        )
        label = "onDrag" if self.use_on_drag else "manual"

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Behavior"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "use_on_drag", not self.use_on_drag
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"ScrollViewKeyboardDismissBehavior.{label}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    width=300.0,
                    child=TextField(
                        decoration=InputDecoration(
                            hintText="Type here, then scroll below",
                        ),
                    ),
                ),
                SizedBox(height=8),
                Container(
                    height=150.0,
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=ListView(
                        shrinkWrap=True,
                        children=[
                            Container(
                                height=40.0,
                                color=Colors.blue.withValues(alpha=0.1 + i * 0.08),
                                child=Center(
                                    child=Text(
                                        f"List item {i + 1}",
                                        style=TextStyle(fontSize=13),
                                    ),
                                ),
                            )
                            for i in range(10)
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "manual: keyboard stays open while scrolling.\n"
                    "onDrag: keyboard dismisses when user scrolls.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _ScrollPhysicsDemo(StatefulWidget):
    def createState(self):
        return _ScrollPhysicsDemoState()


class _ScrollPhysicsDemoState(State[_ScrollPhysicsDemo]):
    def initState(self):
        self.physics_index = 0

    def build(self, context):
        physics_options = [
            ("BouncingScrollPhysics", Colors.blue),
            ("ClampingScrollPhysics", Colors.teal),
            ("NeverScrollableScrollPhysics", Colors.red),
        ]
        current = physics_options[self.physics_index]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Cycle Physics"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "physics_index",
                                    (self.physics_index + 1) % 3,
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(current[0], style=TextStyle(fontSize=13)),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    height=180.0,
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=ListView(
                        physics=ScrollPhysics(),
                        shrinkWrap=True,
                        children=[
                            Container(
                                height=45.0,
                                color=current[1].withValues(
                                    alpha=0.15 + (i % 3) * 0.15
                                ),
                                child=Center(
                                    child=Text(
                                        f"{current[0]} - Item {i + 1}",
                                        style=TextStyle(fontSize=12),
                                    ),
                                ),
                            )
                            for i in range(8)
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "Bouncing: iOS-style over-scroll bounce.\n"
                    "Clamping: Android-style hard stop at edges.\n"
                    "NeverScrollable: scroll is disabled entirely.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _HitTestBehaviorDemo(StatefulWidget):
    def createState(self):
        return _HitTestBehaviorDemoState()


class _HitTestBehaviorDemoState(State[_HitTestBehaviorDemo]):
    def initState(self):
        self.behavior_index = 0
        self.tap_log = "Tap the boxes to see events"

    def build(self, context):
        behaviors = [
            (HitTestBehavior.deferToChild, "deferToChild"),
            (HitTestBehavior.opaque, "opaque"),
            (HitTestBehavior.translucent, "translucent"),
        ]
        current = behaviors[self.behavior_index]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Cycle Behavior"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "behavior_index",
                                    (self.behavior_index + 1) % 3,
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"HitTestBehavior.{current[1]}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                GestureDetector(
                    behavior=current[0],
                    onTap=lambda: self.setState(
                        lambda: setattr(self, "tap_log", "OUTER tapped")
                    ),
                    child=Container(
                        width=250.0,
                        height=100.0,
                        decoration=BoxDecoration(
                            color=Colors.orange.withValues(alpha=0.3),
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=Center(
                            child=GestureDetector(
                                onTap=lambda: self.setState(
                                    lambda: setattr(self, "tap_log", "INNER tapped")
                                ),
                                child=Container(
                                    width=120.0,
                                    height=50.0,
                                    decoration=BoxDecoration(
                                        color=Colors.blue.withValues(alpha=0.5),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Center(
                                        child=Text(
                                            "Inner",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(self.tap_log, style=TextStyle(fontSize=13)),
                SizedBox(height=4),
                Text(
                    "deferToChild: only child area receives taps.\n"
                    "opaque: entire detector area receives taps.\n"
                    "translucent: taps pass through to detectors below.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _MouseRegionOpaqueDemo(StatefulWidget):
    def createState(self):
        return _MouseRegionOpaqueDemoState()


class _MouseRegionOpaqueDemoState(State[_MouseRegionOpaqueDemo]):
    def initState(self):
        self.top_log = "Top: -"
        self.bottom_log = "Bottom: -"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "opaque=False + translucent (both fire):",
                    style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                Container(
                    width=260.0,
                    height=80.0,
                    child=Stack(
                        children=[
                            MouseRegion(
                                opaque=False,
                                hitTestBehavior=HitTestBehavior.translucent,
                                onEnter=lambda e: self.setState(
                                    lambda: setattr(
                                        self, "bottom_log", "Bottom: entered"
                                    )
                                ),
                                child=Container(
                                    width=260.0,
                                    height=80.0,
                                    decoration=BoxDecoration(
                                        color=Colors.orange.withValues(alpha=0.2),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Center(
                                        child=Text(
                                            "Bottom region",
                                            style=TextStyle(fontSize=12),
                                        ),
                                    ),
                                ),
                            ),
                            Positioned(
                                left=40.0,
                                top=15.0,
                                child=MouseRegion(
                                    opaque=False,
                                    onEnter=lambda e: self.setState(
                                        lambda: setattr(self, "top_log", "Top: entered")
                                    ),
                                    child=Container(
                                        width=180.0,
                                        height=50.0,
                                        decoration=BoxDecoration(
                                            color=Colors.blue.withValues(alpha=0.3),
                                            borderRadius=BorderRadius.circular(8),
                                        ),
                                        child=Center(
                                            child=Text(
                                                "Top region (opaque=False)",
                                                style=TextStyle(
                                                    fontSize=11, color=Colors.white
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(self.top_log, style=TextStyle(fontSize=12)),
                Text(self.bottom_log, style=TextStyle(fontSize=12)),
                SizedBox(height=12),
                Text(
                    "opaque=True (only top fires):",
                    style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                Container(
                    width=260.0,
                    height=80.0,
                    child=Stack(
                        children=[
                            MouseRegion(
                                onEnter=lambda e: self.setState(
                                    lambda: setattr(
                                        self, "bottom_log", "Bottom: entered (opaque)"
                                    )
                                ),
                                child=Container(
                                    width=260.0,
                                    height=80.0,
                                    decoration=BoxDecoration(
                                        color=Colors.orange.withValues(alpha=0.2),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Center(
                                        child=Text(
                                            "Bottom region",
                                            style=TextStyle(fontSize=12),
                                        ),
                                    ),
                                ),
                            ),
                            Positioned(
                                left=40.0,
                                top=15.0,
                                child=MouseRegion(
                                    opaque=True,
                                    onEnter=lambda e: self.setState(
                                        lambda: setattr(
                                            self, "top_log", "Top: entered (opaque)"
                                        )
                                    ),
                                    child=Container(
                                        width=180.0,
                                        height=50.0,
                                        decoration=BoxDecoration(
                                            color=Colors.blue.withValues(alpha=0.3),
                                            borderRadius=BorderRadius.circular(8),
                                        ),
                                        child=Center(
                                            child=Text(
                                                "Top region (opaque=True)",
                                                style=TextStyle(
                                                    fontSize=11, color=Colors.white
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "With opaque=True the top region blocks the bottom from receiving events.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _AlignmentPickerDemo(StatefulWidget):
    def createState(self):
        return _AlignmentPickerDemoState()


class _AlignmentPickerDemoState(State["_AlignmentPickerDemo"]):

    def initState(self):
        self.alignment_idx = 4

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                _alignment_picker(
                    self.alignment_idx,
                    lambda idx: self.setState(
                        lambda: setattr(self, "alignment_idx", idx)
                    ),
                ),
                SizedBox(height=12),
                _alignment_demo(self.alignment_idx),
            ],
        )


class _AnimatedContainerDemo(StatefulWidget):
    def createState(self):
        return _AnimatedContainerDemoState()


class _AnimatedContainerDemoState(State["_AnimatedContainerDemo"]):

    def initState(self):
        self.anim_toggled = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Animation"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "anim_toggled", not self.anim_toggled)
                    ),
                ),
                SizedBox(height=8),
                AnimatedContainer(
                    duration=Duration(milliseconds=500),
                    curve=Curves.easeOut,
                    width=280.0 if self.anim_toggled else 140.0,
                    height=70.0,
                    padding=(
                        EdgeInsets.all(16) if self.anim_toggled else EdgeInsets.all(8)
                    ),
                    margin=EdgeInsets.only(left=40.0 if self.anim_toggled else 0.0),
                    alignment=(
                        Alignment.center if self.anim_toggled else Alignment.topLeft
                    ),
                    decoration=BoxDecoration(
                        color=(Colors.deepPurple if self.anim_toggled else Colors.teal),
                        borderRadius=BorderRadius.circular(
                            20 if self.anim_toggled else 4
                        ),
                    ),
                    child=Text(
                        "decoration + margin + curve",
                        style=TextStyle(color=Colors.white, fontSize=12),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "Curve comparison",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                _curve_row("linear", Curves.linear, self.anim_toggled),
                _curve_row("ease", Curves.ease, self.anim_toggled),
                _curve_row("easeIn", Curves.easeIn, self.anim_toggled),
                _curve_row("easeOut", Curves.easeOut, self.anim_toggled),
                _curve_row("decelerate", Curves.decelerate, self.anim_toggled),
            ],
        )


class _OutlinedBorderShapesDemo(StatefulWidget):
    def createState(self):
        return _OutlinedBorderShapesDemoState()


class _OutlinedBorderShapesDemoState(State["_OutlinedBorderShapesDemo"]):

    def initState(self):
        pass

    def build(self, context):
        shapes = [
            (
                "RoundedRectangle",
                RoundedRectangleBorder(borderRadius=BorderRadius.circular(12)),
            ),
            ("Circle", CircleBorder()),
            ("Stadium", StadiumBorder()),
            (
                "BeveledRectangle",
                BeveledRectangleBorder(borderRadius=BorderRadius.circular(12)),
            ),
            (
                "ContinuousRectangle",
                ContinuousRectangleBorder(borderRadius=BorderRadius.circular(16)),
            ),
        ]
        buttons = []
        for name, shape in shapes:
            buttons.append(
                ElevatedButton(
                    child=Text(name, style=TextStyle(fontSize=11)),
                    style=ButtonStyle(
                        shape=WidgetStatePropertyAll(shape),
                    ),
                    onPressed=lambda: None,
                ),
            )
        return Wrap(spacing=8, runSpacing=8, children=buttons)


class _PanAxisDemo(StatefulWidget):
    def createState(self):
        return _PanAxisDemoState()


class _PanAxisDemoState(State["_PanAxisDemo"]):

    def initState(self):
        self.axis_idx = 3

    def build(self, context):
        axes = [
            ("horizontal", PanAxis.horizontal),
            ("vertical", PanAxis.vertical),
            ("aligned", PanAxis.aligned),
            ("free", PanAxis.free),
        ]
        name, _ = axes[self.axis_idx]
        buttons = []
        for i, (lbl, _) in enumerate(axes):
            is_sel = i == self.axis_idx
            buttons.append(
                ElevatedButton(
                    child=Text(
                        lbl,
                        style=TextStyle(
                            fontSize=11,
                            color=Colors.white if is_sel else Colors.black,
                        ),
                    ),
                    style=ButtonStyle(
                        backgroundColor=WidgetStatePropertyAll(
                            Colors.blue if is_sel else Color(0xFFE0E0E0)
                        ),
                    ),
                    onPressed=lambda idx=i: self.setState(
                        lambda: setattr(self, "axis_idx", idx)
                    ),
                ),
            )
        grid_colors = [
            Colors.red,
            Colors.blue,
            Colors.green,
            Colors.orange,
            Colors.purple,
            Colors.teal,
        ]
        grid_children = []
        for row in range(4):
            for col in range(4):
                c = grid_colors[(row + col) % len(grid_colors)]
                grid_children.append(
                    Positioned(
                        left=col * 100.0,
                        top=row * 80.0,
                        child=Container(
                            width=95.0,
                            height=75.0,
                            color=c.withValues(alpha=0.3),
                            child=Center(
                                child=Text(
                                    f"({row},{col})",
                                    style=TextStyle(fontSize=11),
                                ),
                            ),
                        ),
                    ),
                )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(spacing=8, runSpacing=4, children=buttons),
                SizedBox(height=8),
                Text(
                    f"PanAxis.{name}",
                    style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                ),
                SizedBox(height=4),
                Container(
                    width=350.0,
                    height=200.0,
                    decoration=BoxDecoration(
                        border=Border.all(color=Colors.grey, width=1.0),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=InteractiveViewer(
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
            ],
        )


class _TransformControllerDemo(StatefulWidget):
    def createState(self):
        return _TransformControllerDemoState()


class _TransformControllerDemoState(State["_TransformControllerDemo"]):

    def initState(self):
        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0

    def _reset(self):
        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.setState(lambda: None)

    def _zoom2x(self):
        self.scale = 2.0
        self.setState(lambda: None)

    def _pan_offset(self):
        self.offset_x = 60.0
        self.offset_y = 30.0
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=4,
                    children=[
                        ElevatedButton(
                            child=Text(
                                "Reset (Identity)",
                                style=TextStyle(fontSize=11),
                            ),
                            onPressed=self._reset,
                        ),
                        ElevatedButton(
                            child=Text("Zoom 2x", style=TextStyle(fontSize=11)),
                            onPressed=self._zoom2x,
                        ),
                        ElevatedButton(
                            child=Text(
                                "Pan to (60, 30)",
                                style=TextStyle(fontSize=11),
                            ),
                            onPressed=self._pan_offset,
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    padding=EdgeInsets.all(8),
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(4),
                    ),
                    child=Text(
                        f"Transform: scale={self.scale}, translate=({self.offset_x}, {self.offset_y})",
                        style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
                    ),
                ),
                SizedBox(height=8),
                Container(
                    width=350.0,
                    height=180.0,
                    decoration=BoxDecoration(
                        border=Border.all(color=Colors.grey, width=1.0),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Stack(
                        children=[
                            Positioned(
                                left=self.offset_x,
                                top=self.offset_y,
                                child=Container(
                                    width=120.0 * self.scale,
                                    height=80.0 * self.scale,
                                    decoration=BoxDecoration(
                                        color=Colors.blue.withValues(alpha=0.2),
                                        border=Border.all(color=Colors.blue, width=2.0),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Center(
                                        child=Text(
                                            "Content",
                                            style=TextStyle(fontSize=14),
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )


_ALIGNMENTS = [
    Alignment.topLeft,
    Alignment.topCenter,
    Alignment.topRight,
    Alignment.centerLeft,
    Alignment.center,
    Alignment.centerRight,
    Alignment.bottomLeft,
    Alignment.bottomCenter,
    Alignment.bottomRight,
]

_ALIGNMENT_NAMES = [
    "topLeft",
    "topCenter",
    "topRight",
    "centerLeft",
    "center",
    "centerRight",
    "bottomLeft",
    "bottomCenter",
    "bottomRight",
]


def _alignment_picker(selected_idx, on_select):
    chips = []
    for i, name in enumerate(_ALIGNMENT_NAMES):
        is_selected = i == selected_idx
        chips.append(
            GestureDetector(
                onTap=lambda idx=i: on_select(idx),
                child=Container(
                    padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                    decoration=BoxDecoration(
                        color=Colors.blue if is_selected else Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(4),
                    ),
                    child=Text(
                        name,
                        style=TextStyle(
                            fontSize=11,
                            color=Colors.white if is_selected else Colors.black,
                        ),
                    ),
                ),
            )
        )
    return Wrap(spacing=6, runSpacing=6, children=chips)


def _alignment_demo(idx):
    return Container(
        width=260.0,
        height=160.0,
        decoration=BoxDecoration(
            color=Color(0xFFF5F5F5),
            borderRadius=BorderRadius.circular(8),
        ),
        alignment=_ALIGNMENTS[idx],
        child=Container(
            width=50.0,
            height=50.0,
            decoration=BoxDecoration(
                color=Colors.blue,
                borderRadius=BorderRadius.circular(8),
            ),
            child=Center(
                child=Text(
                    _ALIGNMENT_NAMES[idx],
                    style=TextStyle(color=Colors.white, fontSize=8),
                ),
            ),
        ),
    )


def _wrap_chip(label, color):
    return Container(
        width=50.0,
        height=28.0,
        color=color,
        child=Center(
            child=Text(label, style=TextStyle(color=Colors.white, fontSize=12)),
        ),
    )


def _curve_row(name, curve, toggled):
    return Padding(
        padding=EdgeInsets.only(bottom=4),
        child=Row(
            children=[
                Container(
                    width=72.0,
                    child=Text(name, style=TextStyle(fontSize=11)),
                ),
                AnimatedContainer(
                    duration=Duration(milliseconds=500),
                    curve=curve,
                    width=200.0 if toggled else 40.0,
                    height=20.0,
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(4),
                    ),
                ),
            ],
        ),
    )


class _OverflowBarAlignmentDemo(StatefulWidget):
    def createState(self):
        return _OverflowBarAlignmentDemoState()


class _OverflowBarAlignmentDemoState(State[_OverflowBarAlignmentDemo]):
    def initState(self):
        self.alignment_index = 0

    def build(self, context):
        alignments = [
            (OverflowBarAlignment.start, CrossAxisAlignment.start, "start"),
            (OverflowBarAlignment.end, CrossAxisAlignment.end, "end"),
            (OverflowBarAlignment.center, CrossAxisAlignment.center, "center"),
        ]
        current = alignments[self.alignment_index]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Alignment"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "alignment_index",
                                    (self.alignment_index + 1) % 3,
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"OverflowBarAlignment.{current[2]}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Container(
                    width=180.0,
                    padding=EdgeInsets.all(8),
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Column(
                        crossAxisAlignment=current[1],
                        spacing=4,
                        children=[
                            ElevatedButton(
                                child=Text("Action 1"),
                                onPressed=lambda: None,
                            ),
                            ElevatedButton(
                                child=Text("Action 2"),
                                onPressed=lambda: None,
                            ),
                            ElevatedButton(
                                child=Text("Long Action 3"),
                                onPressed=lambda: None,
                            ),
                        ],
                    ),
                ),
                SizedBox(height=4),
                Text(
                    "When buttons overflow horizontally, OverflowBar\n"
                    "stacks them vertically with this alignment.",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


def _contract_metric(label, value):
    return Padding(
        padding=EdgeInsets.only(bottom=4),
        child=Text(
            f"{label}: {value}",
            style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY),
        ),
    )


class LayoutPage(StatelessWidget):
    def build(self, context):
        tag_labels = [
            "Flutter",
            "Python",
            "Dart",
            "Widgets",
            "Layout",
            "Material",
            "Painting",
            "Rendering",
        ]
        wrap_tags = [
            Container(
                padding=EdgeInsets.symmetric(horizontal=12, vertical=6),
                decoration=BoxDecoration(
                    color=Colors.blue.withValues(alpha=0.1),
                    borderRadius=BorderRadius.circular(16),
                ),
                child=Text(label, style=TextStyle(fontSize=13, color=Colors.blue)),
            )
            for label in tag_labels
        ]
        contract_radius = Radius.elliptical(24, 16)
        contract_rrect = RRect.fromRectAndRadius(
            Rect.fromLTWH(0, 0, 200, 108),
            contract_radius,
        )
        contract_view_padding = ViewPadding(
            left=12,
            top=20,
            right=16,
            bottom=10,
        )
        contract_geometry = EdgeInsetsGeometry.fromViewPadding(
            contract_view_padding,
            1.0,
        ).add(EdgeInsetsDirectional.fromSTEB(24, 8, 12, 14))
        contract_resolved_ltr = contract_geometry.resolve(TextDirection.ltr)
        contract_resolved_rtl = contract_geometry.resolve(TextDirection.rtl)
        contract_inner_rrect = contract_resolved_ltr.deflateRRect(contract_rrect)

        return CatalogPage(
            title="Layout",
            description=(
                "Explores how constraints, alignment, spacing, clipping, overflow, "
                "and responsive builders shape composition across rows, columns, "
                "wraps, and boxed layouts."
            ),
            children=[
                SplitViewTile(
                    title="AspectRatio / FittedBox / ConstrainedBox",
                    description=(
                        "AspectRatio enforces a width-to-height ratio. "
                        "FittedBox scales its child to fit within given bounds. "
                        "ConstrainedBox applies min/max size constraints."
                    ),
                    instruction="Observe how each widget sizes its child differently within the same Row.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "AspectRatio 16:9",
                                            style=TextStyle(fontSize=12),
                                        ),
                                        Container(
                                            color=Color(0xFFE0E0E0),
                                            width=160.0,
                                            child=AspectRatio(
                                                aspectRatio=16 / 9,
                                                child=Container(
                                                    color=Colors.blue,
                                                    child=Center(
                                                        child=Text(
                                                            "16:9",
                                                            style=TextStyle(
                                                                color=Colors.white
                                                            ),
                                                        )
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=16),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text("FittedBox", style=TextStyle(fontSize=12)),
                                        Container(
                                            width=100.0,
                                            height=40.0,
                                            color=Color(0xFFE0E0E0),
                                            child=FittedBox(
                                                fit=BoxFit.contain,
                                                child=Text(
                                                    "Fitted!",
                                                    style=TextStyle(fontSize=40),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=16),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "ConstrainedBox",
                                            style=TextStyle(fontSize=12),
                                        ),
                                        ConstrainedBox(
                                            constraints=BoxConstraints(
                                                minWidth=80,
                                                maxWidth=120,
                                                minHeight=40,
                                                maxHeight=60,
                                            ),
                                            child=Container(
                                                color=Colors.orange,
                                                child=Center(
                                                    child=Text("Constrained"),
                                                ),
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
                            "AspectRatio(\n"
                            "    aspectRatio=16 / 9,\n"
                            "    child=Container(color=Colors.blue),\n"
                            ")\n"
                            "\n"
                            "FittedBox(\n"
                            "    fit=BoxFit.contain,\n"
                            "    child=Text('Fitted!', style=TextStyle(fontSize=40)),\n"
                            ")\n"
                            "\n"
                            "ConstrainedBox(\n"
                            "    constraints=BoxConstraints(\n"
                            "        minWidth=80, maxWidth=120,\n"
                            "        minHeight=40, maxHeight=60,\n"
                            "    ),\n"
                            "    child=Container(color=Colors.orange),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SizedBox Named Constructors",
                    description=(
                        "SizedBox.expand fills its parent, SizedBox.shrink collapses to zero, "
                        "SizedBox.square creates equal-dimension boxes, and SizedBox.fromSize "
                        "accepts a Size object."
                    ),
                    instruction="Each colored box uses a different SizedBox named constructor.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "SizedBox.expand (fills parent):",
                                style=TextStyle(fontSize=12),
                            ),
                            Container(
                                height=40.0,
                                color=Color(0xFFE0E0E0),
                                child=SizedBox.expand(
                                    child=Container(
                                        color=Colors.blue,
                                        child=Center(
                                            child=Text(
                                                "expand",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "SizedBox.square (dimension=50):",
                                style=TextStyle(fontSize=12),
                            ),
                            SizedBox.square(
                                dimension=50.0,
                                child=Container(
                                    color=Colors.green,
                                    child=Center(
                                        child=Text(
                                            "50",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "SizedBox.fromSize (Size(120, 40)):",
                                style=TextStyle(fontSize=12),
                            ),
                            SizedBox.fromSize(
                                size=Size(120, 40),
                                child=Container(
                                    color=Colors.orange,
                                    child=Center(
                                        child=Text(
                                            "120x40",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "SizedBox.shrink (zero size):",
                                style=TextStyle(fontSize=12),
                            ),
                            Container(
                                color=Color(0xFFE0E0E0),
                                padding=EdgeInsets.all(4),
                                child=Row(
                                    children=[
                                        Text("Before", style=TextStyle(fontSize=12)),
                                        SizedBox.shrink(),
                                        Text("After", style=TextStyle(fontSize=12)),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SizedBox.expand(\n"
                            "    child=Container(color=Colors.blue),\n"
                            ")\n"
                            "\n"
                            "SizedBox.square(\n"
                            "    dimension=50.0,\n"
                            "    child=Container(color=Colors.green),\n"
                            ")\n"
                            "\n"
                            "SizedBox.fromSize(\n"
                            "    size=Size(120, 40),\n"
                            "    child=Container(color=Colors.orange),\n"
                            ")\n"
                            "\n"
                            "SizedBox.shrink()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MediaQuery",
                    description=(
                        "Reads live screen metrics such as size, pixel ratio, padding, "
                        "and view insets from MediaQuery.of(context)."
                    ),
                    instruction="The panel shows real-time values from the current window. Resize the window to see them update.",
                    visible=_MediaQueryDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "media = MediaQuery.of(context)\n"
                            "Text(f'Screen: {media.size.width:.0f} x {media.size.height:.0f}')\n"
                            "Text(f'Pixel ratio: {media.devicePixelRatio:.1f}')\n"
                            "Text(f'Padding: {media.padding}')\n"
                            "Text(f'View insets: {media.viewInsets}')"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Edge Insets Geometry Contracts",
                    description=(
                        "Exercises Radius, RRect, ViewPadding, EdgeInsetsGeometry, "
                        "and EdgeInsetsDirectional with real geometry calculations."
                    ),
                    instruction=(
                        "The left panel shows the constructed contract values. The "
                        "right panel applies resolved directional padding to a live box."
                    ),
                    visible=Row(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        _contract_metric("Radius", contract_radius),
                                        _contract_metric("RRect", contract_rrect),
                                        _contract_metric(
                                            "ViewPadding",
                                            contract_view_padding,
                                        ),
                                        _contract_metric(
                                            "resolve(ltr)",
                                            contract_resolved_ltr,
                                        ),
                                        _contract_metric(
                                            "resolve(rtl)",
                                            contract_resolved_rtl,
                                        ),
                                        _contract_metric(
                                            "deflateRRect",
                                            contract_inner_rrect,
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=24),
                            Expanded(
                                child=Container(
                                    height=180.0,
                                    padding=EdgeInsets.all(16),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFF3F7F9),
                                        border=Border.all(
                                            color=Color(0xFFCAD6DC),
                                        ),
                                        borderRadius=BorderRadius.circular(18),
                                    ),
                                    child=Container(
                                        decoration=BoxDecoration(
                                            color=Colors.teal.withValues(alpha=0.10),
                                            borderRadius=BorderRadius.circular(14),
                                        ),
                                        child=Padding(
                                            padding=contract_resolved_rtl,
                                            child=Container(
                                                decoration=BoxDecoration(
                                                    color=Colors.teal,
                                                    borderRadius=BorderRadius.circular(
                                                        10
                                                    ),
                                                ),
                                                child=Center(
                                                    child=Text(
                                                        "resolved RTL padding",
                                                        textAlign=TextAlign.center,
                                                        style=TextStyle(
                                                            color=Colors.white,
                                                            fontSize=12,
                                                            fontWeight=FontWeight.bold,
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.dart import Radius, Rect, RRect, ViewPadding\n"
                            "from flut.dart.ui import TextDirection\n"
                            "from flut.flutter.painting import EdgeInsetsDirectional, EdgeInsetsGeometry\n\n"
                            "radius = Radius.elliptical(24, 16)\n"
                            "rrect = RRect.fromRectAndRadius(Rect.fromLTWH(0, 0, 200, 108), radius)\n"
                            "view_padding = ViewPadding(left=12, top=20, right=16, bottom=10)\n"
                            "geometry = EdgeInsetsGeometry.fromViewPadding(view_padding, 1.0).add(\n"
                            "    EdgeInsetsDirectional.fromSTEB(24, 8, 12, 14)\n"
                            ")\n"
                            "resolved = geometry.resolve(TextDirection.rtl)\n"
                            "inner = resolved.deflateRRect(rrect)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Wrap",
                    description=(
                        "Flows children into multiple runs when they exceed the available width. "
                        "Supports WrapAlignment, WrapCrossAlignment, and direction (Axis)."
                    ),
                    instruction="Resize the window to see tags flow onto multiple lines.",
                    visible=Wrap(
                        spacing=8,
                        runSpacing=8,
                        alignment=WrapAlignment.start,
                        crossAxisAlignment=WrapCrossAlignment.center,
                        direction=Axis.horizontal,
                        children=wrap_tags,
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Wrap(\n"
                            "    spacing=8,\n"
                            "    runSpacing=8,\n"
                            "    alignment=WrapAlignment.start,\n"
                            "    crossAxisAlignment=WrapCrossAlignment.center,\n"
                            "    direction=Axis.horizontal,\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Spacer",
                    description=(
                        "Flexible blank space that pushes siblings apart inside a Row or Column. "
                        "Spacer(flex=2) takes twice the space of Spacer()."
                    ),
                    instruction="Notice how 'Left', 'Center', and 'Right' are spaced unevenly because the second Spacer has flex=2.",
                    visible=Container(
                        height=40.0,
                        padding=EdgeInsets.symmetric(horizontal=12),
                        decoration=BoxDecoration(
                            color=Color(0xFFF5F5F5),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Row(
                            children=[
                                Text("Left", style=TextStyle(fontSize=14)),
                                Spacer(),
                                Text("Center", style=TextStyle(fontSize=14)),
                                Spacer(flex=2),
                                Text("Right", style=TextStyle(fontSize=14)),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Row(\n"
                            "    children=[\n"
                            "        Text('Left'),\n"
                            "        Spacer(),\n"
                            "        Text('Center'),\n"
                            "        Spacer(flex=2),\n"
                            "        Text('Right'),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Column & Row Spacing",
                    description=(
                        "The spacing parameter adds uniform gaps between children, "
                        "replacing manual SizedBox spacers. Works on both Column and Row."
                    ),
                    instruction="Compare the two columns: the left uses SizedBox for spacing, the right uses the spacing parameter.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "With SizedBox:",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=8),
                                        Container(
                                            height=32.0,
                                            color=Colors.blue,
                                            child=Center(
                                                child=Text(
                                                    "A",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
                                            ),
                                        ),
                                        SizedBox(height=8),
                                        Container(
                                            height=32.0,
                                            color=Colors.blue,
                                            child=Center(
                                                child=Text(
                                                    "B",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
                                            ),
                                        ),
                                        SizedBox(height=8),
                                        Container(
                                            height=32.0,
                                            color=Colors.blue,
                                            child=Center(
                                                child=Text(
                                                    "C",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=24),
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    spacing=8,
                                    children=[
                                        Text(
                                            "With spacing=8:",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        Container(
                                            height=32.0,
                                            color=Colors.teal,
                                            child=Center(
                                                child=Text(
                                                    "A",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
                                            ),
                                        ),
                                        Container(
                                            height=32.0,
                                            color=Colors.teal,
                                            child=Center(
                                                child=Text(
                                                    "B",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
                                            ),
                                        ),
                                        Container(
                                            height=32.0,
                                            color=Colors.teal,
                                            child=Center(
                                                child=Text(
                                                    "C",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                )
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
                            "# Before: manual SizedBox gaps\n"
                            "Column(children=[\n"
                            "    item_a,\n"
                            "    SizedBox(height=8),\n"
                            "    item_b,\n"
                            "    SizedBox(height=8),\n"
                            "    item_c,\n"
                            "])\n"
                            "\n"
                            "# After: spacing parameter\n"
                            "Column(spacing=8, children=[\n"
                            "    item_a,\n"
                            "    item_b,\n"
                            "    item_c,\n"
                            "])"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="VerticalDirection",
                    description=(
                        "VerticalDirection changes whether a Column lays its children "
                        "from top to bottom or bottom to top."
                    ),
                    instruction="Toggle the direction to see the same children reflow upward or downward.",
                    visible=_VerticalDirectionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Column(\n"
                            "    verticalDirection=VerticalDirection.up,\n"
                            "    children=[\n"
                            "        Container(color=Colors.red),\n"
                            "        Container(color=Colors.green),\n"
                            "        Container(color=Colors.blue),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Align widthFactor / heightFactor",
                    description=(
                        "widthFactor and heightFactor size the Align widget as a "
                        "multiple of its child's dimensions. Without them, Align "
                        "expands to fill available space."
                    ),
                    instruction="Compare the three boxes: default Align fills its parent, while widthFactor/heightFactor constrain it relative to the child.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "Align (no factor \u2014 fills parent):",
                                style=TextStyle(fontSize=12, color=Colors.grey),
                            ),
                            SizedBox(height=4),
                            Container(
                                height=50.0,
                                color=Color(0xFFE0E0E0),
                                child=Align(
                                    alignment=Alignment.centerLeft,
                                    child=Container(
                                        width=60.0,
                                        height=30.0,
                                        color=Colors.blue,
                                        child=Center(
                                            child=Text(
                                                "60",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "Align (widthFactor=2.0):",
                                style=TextStyle(fontSize=12, color=Colors.grey),
                            ),
                            SizedBox(height=4),
                            Container(
                                color=Color(0xFFE0E0E0),
                                child=Align(
                                    alignment=Alignment.center,
                                    widthFactor=2.0,
                                    child=Container(
                                        width=60.0,
                                        height=30.0,
                                        color=Colors.teal,
                                        child=Center(
                                            child=Text(
                                                "60",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=4),
                            Text(
                                "\u2191 Align width = 60 \u00d7 2.0 = 120",
                                style=TextStyle(fontSize=11, color=Colors.teal),
                            ),
                            SizedBox(height=12),
                            Text(
                                "Align (widthFactor=3.0, heightFactor=2.0):",
                                style=TextStyle(fontSize=12, color=Colors.grey),
                            ),
                            SizedBox(height=4),
                            Container(
                                color=Color(0xFFE0E0E0),
                                child=Align(
                                    alignment=Alignment.center,
                                    widthFactor=3.0,
                                    heightFactor=2.0,
                                    child=Container(
                                        width=60.0,
                                        height=30.0,
                                        color=Colors.orange,
                                        child=Center(
                                            child=Text(
                                                "60\u00d730",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(height=4),
                            Text(
                                "\u2191 Align = 180 \u00d7 60 (child \u00d7 factors)",
                                style=TextStyle(fontSize=11, color=Colors.orange),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Align(\n"
                            "    alignment=Alignment.center,\n"
                            "    widthFactor=2.0,\n"
                            "    child=Container(width=60, height=30),\n"
                            ")  # Align width = 60 * 2.0 = 120\n"
                            "\n"
                            "Align(\n"
                            "    alignment=Alignment.center,\n"
                            "    widthFactor=3.0,\n"
                            "    heightFactor=2.0,\n"
                            "    child=Container(width=60, height=30),\n"
                            ")  # Align = 180 x 60"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ClipRRect",
                    description=(
                        "Clips overflowing child content to a rounded rectangle. "
                        "Unlike BoxDecoration borderRadius which only rounds the "
                        "background, ClipRRect actually clips all child pixels."
                    ),
                    instruction=(
                        "Left: without ClipRRect the red overflow is visible outside the grey box. "
                        "Right: ClipRRect clips all child content to the rounded boundary."
                    ),
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "No ClipRRect (overflow visible):",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=120.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFE0E0E0),
                                                borderRadius=BorderRadius.circular(16),
                                            ),
                                            child=Stack(
                                                children=[
                                                    Positioned(
                                                        left=-20.0,
                                                        top=-20.0,
                                                        child=Container(
                                                            width=60.0,
                                                            height=60.0,
                                                            color=Colors.red,
                                                        ),
                                                    ),
                                                    Positioned(
                                                        right=-15.0,
                                                        bottom=-15.0,
                                                        child=Container(
                                                            width=50.0,
                                                            height=50.0,
                                                            color=Colors.blue,
                                                        ),
                                                    ),
                                                    Center(
                                                        child=Text(
                                                            "Overflow",
                                                            style=TextStyle(
                                                                fontSize=12
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=24),
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "With ClipRRect (overflow clipped):",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        ClipRRect(
                                            borderRadius=BorderRadius.circular(16),
                                            child=Container(
                                                width=120.0,
                                                height=80.0,
                                                color=Color(0xFFE0E0E0),
                                                child=Stack(
                                                    children=[
                                                        Positioned(
                                                            left=-20.0,
                                                            top=-20.0,
                                                            child=Container(
                                                                width=60.0,
                                                                height=60.0,
                                                                color=Colors.red,
                                                            ),
                                                        ),
                                                        Positioned(
                                                            right=-15.0,
                                                            bottom=-15.0,
                                                            child=Container(
                                                                width=50.0,
                                                                height=50.0,
                                                                color=Colors.blue,
                                                            ),
                                                        ),
                                                        Center(
                                                            child=Text(
                                                                "Clipped",
                                                                style=TextStyle(
                                                                    fontSize=12
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                ),
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
                            "# Without ClipRRect: child overflow is visible\n"
                            "Container(\n"
                            "    borderRadius=BorderRadius.circular(16),\n"
                            "    child=Stack(children=[\n"
                            "        Positioned(left=-20, top=-20,\n"
                            "            child=Container(width=60, height=60)),\n"
                            "    ]),\n"
                            ")\n"
                            "\n"
                            "# With ClipRRect: overflow is clipped\n"
                            "ClipRRect(\n"
                            "    borderRadius=BorderRadius.circular(16),\n"
                            "    child=Container(\n"
                            "        child=Stack(children=[\n"
                            "            Positioned(left=-20, top=-20,\n"
                            "                child=Container(width=60, height=60)),\n"
                            "        ]),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BorderRadiusGeometry",
                    description=(
                        "BorderRadiusGeometry is the abstract supertype of BorderRadius "
                        "(physical corners: topLeft/topRight/bottomLeft/bottomRight) and "
                        "BorderRadiusDirectional (logical corners: topStart/topEnd/"
                        "bottomStart/bottomEnd, resolved against TextDirection). Widgets "
                        "such as Container.borderRadius, ClipRRect.borderRadius and "
                        "RoundedRectangleBorder.borderRadius accept either subtype."
                    ),
                    instruction=(
                        "Left: BorderRadius.only with physical corners. "
                        "Right: BorderRadiusDirectional.only with logical corners "
                        "(start/end resolve against the ambient TextDirection - LTR here, "
                        "so start == left)."
                    ),
                    visible=Row(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "BorderRadius.only",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=140.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFF90CAF9),
                                                borderRadius=BorderRadius.only(
                                                    topLeft=Radius.circular(24),
                                                    bottomRight=Radius.circular(24),
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
                                            "BorderRadiusDirectional.only",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=140.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFA5D6A7),
                                                borderRadius=BorderRadiusDirectional.only(
                                                    topStart=Radius.circular(24),
                                                    bottomEnd=Radius.circular(24),
                                                ),
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
                            "# Physical corners.\n"
                            "BorderRadius.only(\n"
                            "    topLeft=Radius.circular(24),\n"
                            "    bottomRight=Radius.circular(24),\n"
                            ")\n"
                            "\n"
                            "# Logical corners (resolved against TextDirection).\n"
                            "BorderRadiusDirectional.only(\n"
                            "    topStart=Radius.circular(24),\n"
                            "    bottomEnd=Radius.circular(24),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Stack clipBehavior",
                    description=(
                        "Stack.clipBehavior controls whether children that overflow "
                        "the Stack bounds are clipped. Clip.hardEdge (default) clips "
                        "overflow. Clip.none lets overflow paint outside the boundary."
                    ),
                    instruction=(
                        "Left: Clip.none — the red and blue boxes extend past the grey "
                        "boundary. Right: Clip.hardEdge — identical layout but overflow "
                        "is cut off at the Stack edge."
                    ),
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "Clip.none:",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=120.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFE0E0E0),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=Stack(
                                                clipBehavior=Clip.none,
                                                children=[
                                                    Positioned(
                                                        left=-20.0,
                                                        top=-15.0,
                                                        child=Container(
                                                            width=50.0,
                                                            height=50.0,
                                                            color=Colors.red,
                                                        ),
                                                    ),
                                                    Positioned(
                                                        right=-20.0,
                                                        bottom=-15.0,
                                                        child=Container(
                                                            width=50.0,
                                                            height=50.0,
                                                            color=Colors.blue,
                                                        ),
                                                    ),
                                                    Center(
                                                        child=Text(
                                                            "Visible",
                                                            style=TextStyle(
                                                                fontSize=12
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=24),
                            Expanded(
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.start,
                                    children=[
                                        Text(
                                            "Clip.hardEdge:",
                                            style=TextStyle(
                                                fontSize=12, color=Colors.grey
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=120.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFE0E0E0),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=Stack(
                                                clipBehavior=Clip.hardEdge,
                                                children=[
                                                    Positioned(
                                                        left=-20.0,
                                                        top=-15.0,
                                                        child=Container(
                                                            width=50.0,
                                                            height=50.0,
                                                            color=Colors.red,
                                                        ),
                                                    ),
                                                    Positioned(
                                                        right=-20.0,
                                                        bottom=-15.0,
                                                        child=Container(
                                                            width=50.0,
                                                            height=50.0,
                                                            color=Colors.blue,
                                                        ),
                                                    ),
                                                    Center(
                                                        child=Text(
                                                            "Clipped",
                                                            style=TextStyle(
                                                                fontSize=12
                                                            ),
                                                        ),
                                                    ),
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
                            "from flut.dart.ui import Clip\n"
                            "\n"
                            "# Overflow paints outside Stack bounds\n"
                            "Stack(\n"
                            "    clipBehavior=Clip.none,\n"
                            "    children=[\n"
                            "        Positioned(left=-20, top=-15,\n"
                            "            child=Container(width=50, height=50)),\n"
                            "    ],\n"
                            ")\n"
                            "\n"
                            "# Overflow is clipped at Stack edge (default)\n"
                            "Stack(\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Opacity",
                    description="Fades a child widget by setting an opacity between 0.0 (invisible) and 1.0 (fully visible).",
                    instruction="Click 'Toggle Opacity' to switch between full and 20% opacity.",
                    visible=_OpacityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Opacity(\n"
                            "    opacity=opacity_value,\n"
                            "    child=Container(\n"
                            "        padding=EdgeInsets.all(12),\n"
                            "        decoration=BoxDecoration(\n"
                            "            color=Colors.blue,\n"
                            "            borderRadius=BorderRadius.circular(8),\n"
                            "        ),\n"
                            "        child=Text(f'opacity={opacity_value}'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MainAxisSize",
                    description=(
                        "MainAxisSize.min shrinks a Row/Column to fit its children. "
                        "MainAxisSize.max (default) stretches to fill available space."
                    ),
                    instruction="Click 'Toggle MainAxisSize' and observe the grey background shrink or expand around the colored boxes.",
                    visible=_MainAxisSizeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Row(\n"
                            "    mainAxisSize=MainAxisSize.min,\n"
                            "    children=[\n"
                            "        Container(width=60, height=40, color=Colors.blue),\n"
                            "        SizedBox(width=8),\n"
                            "        Container(width=60, height=40, color=Colors.teal),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TextAlign & TextOverflow",
                    description=(
                        "TextAlign controls horizontal alignment within the text's layout box. "
                        "TextOverflow.ellipsis truncates long text with '\u2026'."
                    ),
                    instruction="Compare left, center, and right alignment. The bottom box shows ellipsis on a long string.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Row(
                                children=[
                                    _text_align_box("TextAlign.left", TextAlign.left),
                                    SizedBox(width=8),
                                    _text_align_box(
                                        "TextAlign.center", TextAlign.center
                                    ),
                                    SizedBox(width=8),
                                    _text_align_box("TextAlign.right", TextAlign.right),
                                ],
                            ),
                            SizedBox(height=12),
                            Container(
                                width=220.0,
                                padding=EdgeInsets.all(8),
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Text(
                                    "This is a very long text that should be truncated with an ellipsis",
                                    maxLines=1,
                                    overflow=TextOverflow.ellipsis,
                                    style=TextStyle(fontSize=13),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text('Sample', textAlign=TextAlign.center)\n"
                            "\n"
                            "Text(\n"
                            "    'Very long text...',\n"
                            "    maxLines=1,\n"
                            "    overflow=TextOverflow.ellipsis,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="WidgetSpan",
                    description=(
                        "Embeds arbitrary widgets inline within Text.rich. "
                        "PlaceholderAlignment and TextBaseline control vertical positioning."
                    ),
                    instruction="See the star icon and 'tag' badge rendered inline alongside text spans.",
                    visible=Text.rich(
                        TextSpan(
                            children=[
                                TextSpan(
                                    text="Hello ",
                                    style=TextStyle(fontSize=16),
                                ),
                                WidgetSpan(
                                    alignment=PlaceholderAlignment.baseline,
                                    baseline=TextBaseline.alphabetic,
                                    child=Icon(
                                        Icons.star, color=Colors.amber, size=18.0
                                    ),
                                ),
                                TextSpan(
                                    text=" World ",
                                    style=TextStyle(fontSize=16),
                                ),
                                WidgetSpan(
                                    alignment=PlaceholderAlignment.middle,
                                    child=Container(
                                        padding=EdgeInsets.symmetric(
                                            horizontal=6, vertical=2
                                        ),
                                        decoration=BoxDecoration(
                                            color=Colors.blue,
                                            borderRadius=BorderRadius.circular(4),
                                        ),
                                        child=Text(
                                            "tag",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=11
                                            ),
                                        ),
                                    ),
                                ),
                                TextSpan(
                                    text=" inline!",
                                    style=TextStyle(fontSize=16),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Text.rich(\n"
                            "    TextSpan(children=[\n"
                            "        TextSpan(text='Hello '),\n"
                            "        WidgetSpan(\n"
                            "            alignment=PlaceholderAlignment.baseline,\n"
                            "            baseline=TextBaseline.alphabetic,\n"
                            "            child=Icon(Icons.star, size=18.0),\n"
                            "        ),\n"
                            "        TextSpan(text=' World '),\n"
                            "        WidgetSpan(\n"
                            "            alignment=PlaceholderAlignment.middle,\n"
                            "            child=Container(child=Text('tag')),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Tooltip",
                    description="Shows a text overlay on hover. Supports plain message, rich text via richMessage, waitDuration, and exitDuration.",
                    instruction="Hover over each box: plain tooltip, delayed tooltip, and rich styled tooltip.",
                    visible=Row(
                        children=[
                            Tooltip(
                                message="This is a tooltip!",
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Colors.blue.withValues(alpha=0.1),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Row(
                                        children=[
                                            Icon(
                                                Icons.info, color=Colors.blue, size=16.0
                                            ),
                                            SizedBox(width=6),
                                            Text(
                                                "Hover me", style=TextStyle(fontSize=13)
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                            SizedBox(width=12),
                            Tooltip(
                                message="Appears after 200ms",
                                waitDuration=Duration(milliseconds=200),
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFFCE4EC),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text(
                                        "With wait", style=TextStyle(fontSize=13)
                                    ),
                                ),
                            ),
                            SizedBox(width=12),
                            Tooltip(
                                richMessage=TextSpan(
                                    children=[
                                        TextSpan(
                                            text="Bold",
                                            style=TextStyle(fontWeight=FontWeight.bold),
                                        ),
                                        TextSpan(text=" and "),
                                        TextSpan(
                                            text="colored",
                                            style=TextStyle(color=Colors.amber),
                                        ),
                                    ],
                                ),
                                exitDuration=Duration(milliseconds=500),
                                child=Container(
                                    padding=EdgeInsets.all(12),
                                    decoration=BoxDecoration(
                                        color=Color(0xFFE8F5E9),
                                        borderRadius=BorderRadius.circular(8),
                                    ),
                                    child=Text(
                                        "Rich tip", style=TextStyle(fontSize=13)
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Tooltip(\n"
                            "    message='Simple tooltip',\n"
                            "    child=Text('Hover me'),\n"
                            ")\n"
                            "\n"
                            "Tooltip(\n"
                            "    richMessage=TextSpan(children=[\n"
                            "        TextSpan(text='Bold', style=TextStyle(\n"
                            "            fontWeight=FontWeight.bold)),\n"
                            "        TextSpan(text=' and '),\n"
                            "        TextSpan(text='colored', style=TextStyle(\n"
                            "            color=Colors.amber)),\n"
                            "    ]),\n"
                            "    exitDuration=Duration(milliseconds=500),\n"
                            "    child=Text('Rich tip'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="LayoutBuilder",
                    description=(
                        "Receives the parent's constraints during layout, enabling "
                        "responsive designs based on available width and height."
                    ),
                    instruction="The box shows the live maxWidth and maxHeight from the parent constraints.",
                    visible=LayoutBuilder(
                        builder=lambda ctx, constraints: Container(
                            padding=EdgeInsets.all(12),
                            decoration=BoxDecoration(
                                color=Color(0xFFE3F2FD),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Text(
                                f"maxWidth: {constraints.maxWidth:.0f}  maxHeight: {constraints.maxHeight:.0f}",
                                style=TextStyle(
                                    fontSize=13, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "LayoutBuilder(\n"
                            "    builder=lambda ctx, constraints: Container(\n"
                            "        child=Text(\n"
                            "            f'maxWidth: {constraints.maxWidth:.0f}'\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Container Constraints",
                    description=(
                        "Container constraints (minWidth, maxWidth, minHeight, maxHeight) "
                        "are enforced by the parent. Parent tight constraints (Expanded) "
                        "override child constraints, while loose constraints (Flexible) respect them."
                    ),
                    instruction=(
                        "Compare the three rows: unconstrained parent, Expanded (tight), "
                        "and Flexible (loose). Notice how minWidth=200 is honored or ignored."
                    ),
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "minWidth=200, maxWidth=400 (unconstrained parent):",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                constraints=BoxConstraints(minWidth=200, maxWidth=400),
                                padding=EdgeInsets.all(8),
                                color=Colors.teal.withValues(alpha=0.2),
                                child=Text(
                                    "I'm between 200\u2013400px wide",
                                    style=TextStyle(fontSize=13),
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "minWidth=200 inside Expanded (tight constraint wins):",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            SizedBox(height=4),
                            Row(
                                children=[
                                    Container(
                                        width=200.0,
                                        height=40.0,
                                        color=Colors.blue,
                                        child=Center(
                                            child=Text(
                                                "Fixed 200",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                    Expanded(
                                        child=Container(
                                            constraints=BoxConstraints(minWidth=200),
                                            height=40.0,
                                            color=Colors.orange,
                                            child=LayoutBuilder(
                                                builder=lambda ctx, c: Center(
                                                    child=Text(
                                                        f"minWidth=200, actual={c.maxWidth:.0f}",
                                                        style=TextStyle(fontSize=12),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(height=4),
                            Text(
                                "\u2191 Expanded forces tight constraints, so minWidth=200 is ignored "
                                "when remaining space < 200.",
                                style=TextStyle(fontSize=11, color=Colors.red),
                            ),
                            SizedBox(height=12),
                            Text(
                                "minWidth=200 inside Flexible (loose constraint respects min):",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                            SizedBox(height=4),
                            Row(
                                children=[
                                    Container(
                                        width=200.0,
                                        height=40.0,
                                        color=Colors.blue,
                                        child=Center(
                                            child=Text(
                                                "Fixed 200",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                    Flexible(
                                        child=Container(
                                            constraints=BoxConstraints(minWidth=200),
                                            height=40.0,
                                            color=Colors.green,
                                            child=LayoutBuilder(
                                                builder=lambda ctx, c: Center(
                                                    child=Text(
                                                        f"minWidth=200, actual={c.maxWidth:.0f}",
                                                        style=TextStyle(fontSize=12),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(height=4),
                            Text(
                                "\u2191 Flexible passes loose constraints (min=0, max=remaining). "
                                "Container enforces its own minWidth=200.",
                                style=TextStyle(fontSize=11, color=Colors.green),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    constraints=BoxConstraints(minWidth=200, maxWidth=400),\n"
                            "    child=Text('Between 200-400px'),\n"
                            ")\n"
                            "\n"
                            "Expanded(\n"
                            "    child=Container(\n"
                            "        constraints=BoxConstraints(minWidth=200),\n"
                            "        child=Text('Tight: minWidth ignored'),\n"
                            "    ),\n"
                            ")\n"
                            "\n"
                            "Flexible(\n"
                            "    child=Container(\n"
                            "        constraints=BoxConstraints(minWidth=200),\n"
                            "        child=Text('Loose: minWidth respected'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="EdgeInsets",
                    description=(
                        "EdgeInsets controls padding around content. "
                        "The light-blue area shows the padding space; the dark-blue box is the content."
                    ),
                    instruction="Compare how different constructors distribute padding. The visible gap between the light border and dark content reveals each EdgeInsets shape.",
                    visible=Wrap(
                        spacing=16.0,
                        runSpacing=16.0,
                        children=[
                            _padding_box("all(16)", EdgeInsets.all(16)),
                            _padding_box(
                                "symmetric(h=24, v=8)",
                                EdgeInsets.symmetric(horizontal=24, vertical=8),
                            ),
                            _padding_box("only(left=32)", EdgeInsets.only(left=32)),
                            _padding_box("(4, 20, 4, 20)", EdgeInsets(4, 20, 4, 20)),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "# Uniform padding on all sides\n"
                            "Container(\n"
                            "    padding=EdgeInsets.all(16),\n"
                            "    child=content,\n"
                            ")\n\n"
                            "# Different horizontal vs vertical\n"
                            "Container(\n"
                            "    padding=EdgeInsets.symmetric(\n"
                            "        horizontal=24, vertical=8,\n"
                            "    ),\n"
                            "    child=content,\n"
                            ")\n\n"
                            "# Padding on one side only\n"
                            "Container(\n"
                            "    padding=EdgeInsets.only(left=32),\n"
                            "    child=content,\n"
                            ")\n"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BorderRadius",
                    description=(
                        "BorderRadius shapes container corners. "
                        "Each box demonstrates a different constructor applied as a decoration."
                    ),
                    instruction="Compare corner rounding across constructors — from uniform circles to asymmetric horizontal/vertical splits.",
                    visible=Wrap(
                        spacing=16.0,
                        runSpacing=16.0,
                        children=[
                            _br_card("circular(12)", BorderRadius.circular(12)),
                            _br_card(
                                "all(Radius.circular(24))",
                                BorderRadius.all(Radius.circular(24)),
                            ),
                            _br_card(
                                "horizontal\nleft=20, right=4",
                                BorderRadius.horizontal(
                                    left=Radius.circular(20),
                                    right=Radius.circular(4),
                                ),
                            ),
                            _br_card(
                                "vertical\ntop=24, bottom=0",
                                BorderRadius.vertical(
                                    top=Radius.circular(24),
                                    bottom=Radius.circular(0),
                                ),
                            ),
                            _br_card(
                                "only\ntopLeft=30",
                                BorderRadius.only(topLeft=Radius.circular(30)),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    decoration=BoxDecoration(\n"
                            "        color=Colors.blue,\n"
                            "        borderRadius=BorderRadius.circular(12),\n"
                            "    ),\n"
                            ")\n\n"
                            "# Asymmetric corners\n"
                            "BorderRadius.horizontal(\n"
                            "    left=Radius.circular(20),\n"
                            "    right=Radius.circular(4),\n"
                            ")\n"
                            "BorderRadius.vertical(\n"
                            "    top=Radius.circular(24),\n"
                            "    bottom=Radius.circular(0),\n"
                            ")\n"
                            "BorderRadius.only(topLeft=Radius.circular(30))\n"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AxisDirection",
                    description=(
                        "AxisDirection controls which direction a scroll view scrolls. "
                        "Achieved via scrollDirection and reverse on CustomScrollView. "
                        "down=top-to-bottom, up=bottom-to-top, right=left-to-right, left=right-to-left."
                    ),
                    instruction="Press Cycle Direction to switch between down, up, right, and left scroll directions.",
                    visible=_AxisDirectionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.painting import AxisDirection, Axis\n\n"
                            "CustomScrollView(\n"
                            "    scrollDirection=Axis.vertical,\n"
                            "    reverse=False,\n"
                            "    slivers=[\n"
                            "        SliverToBoxAdapter(\n"
                            "            child=Container(height=50, color=Colors.red),\n"
                            "        ),\n"
                            "    ],\n"
                            ")\n\n"
                            "CustomScrollView(\n"
                            "    scrollDirection=Axis.horizontal,\n"
                            "    reverse=True,\n"
                            "    slivers=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SliverPaintOrder",
                    description=(
                        "SliverPaintOrder controls the z-order of overlapping slivers. "
                        "firstIsTop paints the first sliver on top. "
                        "lastIsTop paints the last sliver on top."
                    ),
                    instruction="Press Toggle Paint Order to switch between firstIsTop and lastIsTop. Observe which colored box appears on top.",
                    visible=_SliverPaintOrderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.rendering import SliverPaintOrder\n\n"
                            "CustomScrollView(\n"
                            "    paintOrder=SliverPaintOrder.firstIsTop,\n"
                            "    slivers=[\n"
                            "        SliverToBoxAdapter(child=red_box),\n"
                            "        SliverToBoxAdapter(child=green_box),\n"
                            "        SliverToBoxAdapter(child=blue_box),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ScrollViewKeyboardDismissBehavior",
                    description=(
                        "Controls whether the on-screen keyboard is dismissed when "
                        "the user begins scrolling a scroll view. manual keeps it open, "
                        "onDrag dismisses it."
                    ),
                    instruction="Type in the text field, then toggle behavior and scroll the list. With onDrag, scrolling would dismiss the keyboard.",
                    visible=_ScrollViewKeyboardDismissDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets import (\n"
                            "    ScrollViewKeyboardDismissBehavior, ListView,\n"
                            ")\n\n"
                            "ListView(\n"
                            "    keyboardDismissBehavior=\n"
                            "        ScrollViewKeyboardDismissBehavior.onDrag,\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ScrollPhysics",
                    description=(
                        "ScrollPhysics determines how a scroll view responds "
                        "to user input. The physics param is wired to ListView. "
                        "Concrete subclasses (Bouncing, Clamping, NeverScrollable) "
                        "are not yet available."
                    ),
                    instruction="The list uses ScrollPhysics() (default). Scroll to verify the param is wired. Concrete subclass labels shown for reference.",
                    visible=_ScrollPhysicsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets import ScrollPhysics\n\n"
                            "ListView(\n"
                            "    physics=BouncingScrollPhysics(),\n"
                            "    children=[...],\n"
                            ")\n\n"
                            "ListView(\n"
                            "    physics=NeverScrollableScrollPhysics(),\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="HitTestBehavior",
                    description=(
                        "HitTestBehavior controls how a GestureDetector responds to taps. "
                        "deferToChild only recognizes taps on the child widget. "
                        "opaque captures all taps in the detector area. "
                        "translucent allows taps to pass through to detectors behind."
                    ),
                    instruction="Cycle between behaviors and tap the inner (blue) or outer (orange) areas. Check the log to see which detector received the tap.",
                    visible=_HitTestBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.rendering import HitTestBehavior\n\n"
                            "GestureDetector(\n"
                            "    behavior=HitTestBehavior.opaque,\n"
                            "    onTap=lambda: print('outer'),\n"
                            "    child=GestureDetector(\n"
                            "        behavior=HitTestBehavior.deferToChild,\n"
                            "        onTap=lambda: print('inner'),\n"
                            "        child=Container(color=Colors.blue),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Wrap textDirection & clipBehavior",
                    description=(
                        "Wrap supports textDirection to control flow direction "
                        "and verticalDirection + clipBehavior for vertical layout control."
                    ),
                    instruction="Compare the two Wraps: one flows right-to-left via textDirection=rtl, the other flows bottom-to-top via verticalDirection=up with clipBehavior=hardEdge.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "textDirection=TextDirection.rtl",
                                style=TextStyle(
                                    fontSize=12, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                width=320.0,
                                padding=EdgeInsets.all(8),
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Wrap(
                                    spacing=8,
                                    runSpacing=8,
                                    textDirection=TextDirection.rtl,
                                    children=[
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            decoration=BoxDecoration(
                                                color=Colors.red.withValues(alpha=0.15),
                                                borderRadius=BorderRadius.circular(12),
                                            ),
                                            child=Text(
                                                "First", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            decoration=BoxDecoration(
                                                color=Colors.green.withValues(
                                                    alpha=0.15
                                                ),
                                                borderRadius=BorderRadius.circular(12),
                                            ),
                                            child=Text(
                                                "Second", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            decoration=BoxDecoration(
                                                color=Colors.blue.withValues(
                                                    alpha=0.15
                                                ),
                                                borderRadius=BorderRadius.circular(12),
                                            ),
                                            child=Text(
                                                "Third", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            decoration=BoxDecoration(
                                                color=Colors.orange.withValues(
                                                    alpha=0.15
                                                ),
                                                borderRadius=BorderRadius.circular(12),
                                            ),
                                            child=Text(
                                                "Fourth", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(height=12),
                            Text(
                                "verticalDirection=up + clipBehavior=hardEdge",
                                style=TextStyle(
                                    fontSize=12, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                width=320.0,
                                height=50.0,
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Wrap(
                                    spacing=8,
                                    runSpacing=8,
                                    verticalDirection=VerticalDirection.up,
                                    clipBehavior=Clip.hardEdge,
                                    children=[
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            color=Colors.purple.withValues(alpha=0.15),
                                            child=Text(
                                                "A", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            color=Colors.teal.withValues(alpha=0.15),
                                            child=Text(
                                                "B", style=TextStyle(fontSize=12)
                                            ),
                                        ),
                                        Container(
                                            padding=EdgeInsets.symmetric(
                                                horizontal=10, vertical=4
                                            ),
                                            color=Colors.pink.withValues(alpha=0.15),
                                            child=Text(
                                                "C", style=TextStyle(fontSize=12)
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
                            "from flut.dart.ui import TextDirection, Clip\n"
                            "from flut.flutter.painting import VerticalDirection\n\n"
                            "Wrap(\n"
                            "    textDirection=TextDirection.rtl,\n"
                            "    children=[...],\n"
                            ")\n\n"
                            "Wrap(\n"
                            "    verticalDirection=VerticalDirection.up,\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Transform",
                    description="Applies geometric transformations (rotate, scale, translate) to a child widget at paint time.",
                    instruction="Three boxes show rotate (0.3 rad), scale (1.5x), and translate (+20, +10) applied simultaneously.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Text(
                                        "rotate",
                                        style=TextStyle(
                                            fontSize=14, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Transform.rotate(
                                        angle=0.3,
                                        child=Container(
                                            width=80.0,
                                            height=80.0,
                                            color=Colors.blue,
                                            child=Center(
                                                child=Text(
                                                    "0.3 rad",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(width=48),
                            Column(
                                children=[
                                    Text(
                                        "scale",
                                        style=TextStyle(
                                            fontSize=14, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Transform.scale(
                                        scale=1.5,
                                        child=Container(
                                            width=60.0,
                                            height=60.0,
                                            color=Colors.deepPurple,
                                            child=Center(
                                                child=Text(
                                                    "1.5x",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(width=48),
                            Column(
                                children=[
                                    Text(
                                        "translate",
                                        style=TextStyle(
                                            fontSize=14, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Transform.translate(
                                        offset=Offset(20, 10),
                                        child=Container(
                                            width=80.0,
                                            height=80.0,
                                            color=Colors.teal,
                                            child=Center(
                                                child=Text(
                                                    "+20,+10",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=12
                                                    ),
                                                ),
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
                            "Transform.rotate(angle=0.3, child=box)\n"
                            "Transform.scale(scale=1.5, child=box)\n"
                            "Transform.translate(offset=Offset(20, 10), child=box)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Transform filterQuality",
                    description=(
                        "Transform.scale accepts filterQuality to control rendering quality. "
                        "FilterQuality.none produces pixelated results, FilterQuality.high produces smooth results."
                    ),
                    instruction="Compare the two scaled containers: the left uses FilterQuality.none (pixelated), the right uses FilterQuality.high (smooth).",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "FilterQuality.none",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Transform.scale(
                                            scale=3.0,
                                            filterQuality=FilterQuality.none,
                                            child=Container(
                                                width=20.0,
                                                height=20.0,
                                                decoration=BoxDecoration(
                                                    color=Colors.blue,
                                                    borderRadius=BorderRadius.circular(
                                                        2
                                                    ),
                                                ),
                                                child=Center(
                                                    child=Text(
                                                        "P",
                                                        style=TextStyle(
                                                            color=Colors.white,
                                                            fontSize=6,
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=80),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "FilterQuality.high",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Transform.scale(
                                            scale=3.0,
                                            filterQuality=FilterQuality.high,
                                            child=Container(
                                                width=20.0,
                                                height=20.0,
                                                decoration=BoxDecoration(
                                                    color=Colors.green,
                                                    borderRadius=BorderRadius.circular(
                                                        2
                                                    ),
                                                ),
                                                child=Center(
                                                    child=Text(
                                                        "S",
                                                        style=TextStyle(
                                                            color=Colors.white,
                                                            fontSize=6,
                                                        ),
                                                    ),
                                                ),
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
                            "from flut.dart.ui import FilterQuality\n\n"
                            "Transform.scale(\n"
                            "    scale=3.0,\n"
                            "    filterQuality=FilterQuality.none,\n"
                            "    child=Container(width=20, height=20, color=Colors.blue),\n"
                            ")\n\n"
                            "Transform.scale(\n"
                            "    scale=3.0,\n"
                            "    filterQuality=FilterQuality.high,\n"
                            "    child=Container(width=20, height=20, color=Colors.green),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Transform.flip",
                    description=(
                        "Transform.flip mirrors its child horizontally (flipX), "
                        "vertically (flipY), or both."
                    ),
                    instruction="Observe the mirrored text in each container: flipX reverses horizontally, flipY vertically, and both together.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "flipX=True", style=TextStyle(fontSize=11)
                                        ),
                                        SizedBox(height=4),
                                        Transform.flip(
                                            flipX=True,
                                            child=Container(
                                                padding=EdgeInsets.all(12),
                                                decoration=BoxDecoration(
                                                    color=Colors.blue.withValues(
                                                        alpha=0.15
                                                    ),
                                                    borderRadius=BorderRadius.circular(
                                                        8
                                                    ),
                                                ),
                                                child=Text(
                                                    "Hello",
                                                    style=TextStyle(
                                                        fontSize=18, color=Colors.blue
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=8),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "flipY=True", style=TextStyle(fontSize=11)
                                        ),
                                        SizedBox(height=4),
                                        Transform.flip(
                                            flipY=True,
                                            child=Container(
                                                padding=EdgeInsets.all(12),
                                                decoration=BoxDecoration(
                                                    color=Colors.green.withValues(
                                                        alpha=0.15
                                                    ),
                                                    borderRadius=BorderRadius.circular(
                                                        8
                                                    ),
                                                ),
                                                child=Text(
                                                    "Hello",
                                                    style=TextStyle(
                                                        fontSize=18, color=Colors.green
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=8),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text("both=True", style=TextStyle(fontSize=11)),
                                        SizedBox(height=4),
                                        Transform.flip(
                                            flipX=True,
                                            flipY=True,
                                            child=Container(
                                                padding=EdgeInsets.all(12),
                                                decoration=BoxDecoration(
                                                    color=Colors.orange.withValues(
                                                        alpha=0.15
                                                    ),
                                                    borderRadius=BorderRadius.circular(
                                                        8
                                                    ),
                                                ),
                                                child=Text(
                                                    "Hello",
                                                    style=TextStyle(
                                                        fontSize=18, color=Colors.orange
                                                    ),
                                                ),
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
                            "Transform.flip(\n"
                            "    flipX=True,\n"
                            "    child=Text('Hello'),\n"
                            ")\n\n"
                            "Transform.flip(\n"
                            "    flipY=True,\n"
                            "    child=Text('Hello'),\n"
                            ")\n\n"
                            "Transform.flip(\n"
                            "    flipX=True, flipY=True,\n"
                            "    child=Text('Hello'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="LinearGradient",
                    description="Paints a gradient that transitions linearly across the box decoration.",
                    instruction="A rounded container filled with a blue-to-purple-to-pink gradient.",
                    visible=Container(
                        width=300.0,
                        height=80.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(12),
                            gradient=LinearGradient(
                                colors=[Colors.blue, Colors.purple, Colors.pink],
                            ),
                        ),
                        child=Center(
                            child=Text(
                                "LinearGradient",
                                style=TextStyle(color=Colors.white, fontSize=16),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    decoration=BoxDecoration(\n"
                            "        borderRadius=BorderRadius.circular(12),\n"
                            "        gradient=LinearGradient(\n"
                            "            colors=[Colors.blue, Colors.purple, Colors.pink],\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="RadialGradient",
                    description="Paints a gradient that radiates outward from the center of the box.",
                    instruction="A circular container filled with a yellow-to-orange-to-red radial gradient.",
                    visible=Container(
                        width=150.0,
                        height=150.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(75),
                            gradient=RadialGradient(
                                colors=[Colors.yellow, Colors.orange, Colors.red],
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    decoration=BoxDecoration(\n"
                            "        borderRadius=BorderRadius.circular(75),\n"
                            "        gradient=RadialGradient(\n"
                            "            colors=[Colors.yellow, Colors.orange, Colors.red],\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BoxShadow",
                    description="Adds a drop shadow beneath a container via the boxShadow property of BoxDecoration.",
                    instruction="A white card with a soft shadow offset 4px downward. Best visible on a light background.",
                    visible=Container(
                        width=200.0,
                        height=80.0,
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                            boxShadow=[
                                BoxShadow(
                                    color=Color(0x40000000),
                                    blurRadius=12.0,
                                    offset=Offset(0, 4),
                                ),
                            ],
                        ),
                        child=Center(
                            child=Text("Shadow Card", style=TextStyle(fontSize=14)),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "BoxDecoration(\n"
                            "    color=Colors.white,\n"
                            "    borderRadius=BorderRadius.circular(12),\n"
                            "    boxShadow=[\n"
                            "        BoxShadow(\n"
                            "            color=Color(0x40000000),\n"
                            "            blurRadius=12.0,\n"
                            "            offset=Offset(0, 4),\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BoxShadow BlurStyle",
                    description="BlurStyle controls how the shadow blur is rendered. normal draws a standard Gaussian blur, solid fills the interior, outer draws only outside the shape, and inner draws only inside.",
                    instruction="Four containers each show a different BlurStyle applied to the same BoxShadow parameters. Compare how each style affects the shadow rendering.",
                    visible=Row(
                        children=[
                            _BlurStyleCard("normal", BlurStyle.normal),
                            SizedBox(width=12),
                            _BlurStyleCard("solid", BlurStyle.solid),
                            SizedBox(width=12),
                            _BlurStyleCard("outer", BlurStyle.outer),
                            SizedBox(width=12),
                            _BlurStyleCard("inner", BlurStyle.inner),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.dart import BlurStyle\n\n"
                            "BoxShadow(\n"
                            "    color=Color(0x80000000),\n"
                            "    blurRadius=10.0,\n"
                            "    spreadRadius=2.0,\n"
                            "    blurStyle=BlurStyle.outer,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="LinearGradient transform",
                    description="GradientRotation rotates a LinearGradient by a given angle in radians. Compare a straight gradient to one rotated by pi/4.",
                    instruction="Two containers side by side: left has a default LinearGradient, right has the same gradient rotated 45 degrees via GradientRotation(pi/4).",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Text(
                                        "No transform",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Container(
                                        width=140.0,
                                        height=100.0,
                                        decoration=BoxDecoration(
                                            borderRadius=BorderRadius.circular(10),
                                            gradient=LinearGradient(
                                                colors=[Colors.blue, Colors.green],
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(width=24),
                            Column(
                                children=[
                                    Text(
                                        "GradientRotation(pi/4)",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Container(
                                        width=140.0,
                                        height=100.0,
                                        decoration=BoxDecoration(
                                            borderRadius=BorderRadius.circular(10),
                                            gradient=LinearGradient(
                                                colors=[Colors.blue, Colors.green],
                                                transform=GradientRotation(math.pi / 4),
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
                            "import math\n"
                            "from flut.flutter.painting import GradientRotation\n\n"
                            "LinearGradient(\n"
                            "    colors=[Colors.blue, Colors.green],\n"
                            "    transform=GradientRotation(math.pi / 4),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="RadialGradient focal & focalRadius",
                    description="The focal point shifts the apparent center of the radial gradient. focalRadius controls the size of the focal highlight. Compare a default RadialGradient to one with focal=Alignment.topLeft and focalRadius=0.3.",
                    instruction="Two circles: left is a default radial gradient, right has its focal point shifted to the top-left corner with focalRadius=0.3.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Text(
                                        "Default",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Container(
                                        width=120.0,
                                        height=120.0,
                                        decoration=BoxDecoration(
                                            borderRadius=BorderRadius.circular(60),
                                            gradient=RadialGradient(
                                                colors=[
                                                    Colors.white,
                                                    Colors.blue,
                                                    Colors.indigo,
                                                ],
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(width=24),
                            Column(
                                children=[
                                    Text(
                                        "focal=topLeft, r=0.3",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    Container(
                                        width=120.0,
                                        height=120.0,
                                        decoration=BoxDecoration(
                                            borderRadius=BorderRadius.circular(60),
                                            gradient=RadialGradient(
                                                colors=[
                                                    Colors.white,
                                                    Colors.blue,
                                                    Colors.indigo,
                                                ],
                                                focal=Alignment.topLeft,
                                                focalRadius=0.3,
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
                            "from flut.flutter.painting import Alignment\n\n"
                            "RadialGradient(\n"
                            "    colors=[Colors.white, Colors.blue, Colors.indigo],\n"
                            "    focal=Alignment.topLeft,\n"
                            "    focalRadius=0.3,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="RadialGradient transform",
                    description="GradientRotation applied to a RadialGradient rotates the entire gradient pattern by the given angle.",
                    instruction="A circle with a RadialGradient rotated by pi/3 radians via GradientRotation, producing an angled radial pattern.",
                    visible=Container(
                        width=140.0,
                        height=140.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(70),
                            gradient=RadialGradient(
                                colors=[Colors.yellow, Colors.red, Colors.purple],
                                transform=GradientRotation(math.pi / 3),
                            ),
                        ),
                        child=Center(
                            child=Text(
                                "pi/3",
                                style=TextStyle(color=Colors.white, fontSize=14),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "import math\n"
                            "from flut.flutter.painting import GradientRotation\n\n"
                            "RadialGradient(\n"
                            "    colors=[Colors.yellow, Colors.red, Colors.purple],\n"
                            "    transform=GradientRotation(math.pi / 3),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SweepGradient transform",
                    description="GradientRotation applied to a SweepGradient rotates the sweep start angle, shifting where the color cycle begins.",
                    instruction="A circle with a SweepGradient rotated by pi/2 radians. The color sweep starts from a different angle than the default.",
                    visible=Container(
                        width=140.0,
                        height=140.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(70),
                            gradient=SweepGradient(
                                colors=[
                                    Colors.red,
                                    Colors.orange,
                                    Colors.yellow,
                                    Colors.green,
                                    Colors.blue,
                                    Colors.red,
                                ],
                                transform=GradientRotation(math.pi / 2),
                            ),
                        ),
                        child=Center(
                            child=Text(
                                "pi/2",
                                style=TextStyle(color=Colors.white, fontSize=14),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "import math\n"
                            "from flut.flutter.painting import (\n"
                            "    SweepGradient, GradientRotation,\n"
                            ")\n\n"
                            "SweepGradient(\n"
                            "    colors=[\n"
                            "        Colors.red, Colors.orange, Colors.yellow,\n"
                            "        Colors.green, Colors.blue, Colors.red,\n"
                            "    ],\n"
                            "    transform=GradientRotation(math.pi / 2),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FittedBox clipBehavior",
                    description=(
                        "FittedBox clipBehavior controls whether oversized content "
                        "is clipped or allowed to overflow."
                    ),
                    instruction="Compare: Clip.none allows overflow outside the box, Clip.hardEdge clips it.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Clip.none (overflow visible)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=80.0,
                                            height=40.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(4),
                                            ),
                                            child=FittedBox(
                                                fit=BoxFit.none,
                                                clipBehavior=Clip.none,
                                                child=Container(
                                                    width=160.0,
                                                    height=60.0,
                                                    color=Colors.red.withValues(
                                                        alpha=0.3
                                                    ),
                                                    child=Center(
                                                        child=Text(
                                                            "Oversized",
                                                            style=TextStyle(
                                                                fontSize=14
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=40),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Clip.hardEdge (clipped)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            width=80.0,
                                            height=40.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(4),
                                            ),
                                            child=FittedBox(
                                                fit=BoxFit.none,
                                                clipBehavior=Clip.hardEdge,
                                                child=Container(
                                                    width=160.0,
                                                    height=60.0,
                                                    color=Colors.blue.withValues(
                                                        alpha=0.3
                                                    ),
                                                    child=Center(
                                                        child=Text(
                                                            "Oversized",
                                                            style=TextStyle(
                                                                fontSize=14
                                                            ),
                                                        ),
                                                    ),
                                                ),
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
                            "FittedBox(\n"
                            "    fit=BoxFit.none,\n"
                            "    clipBehavior=Clip.none,\n"
                            "    child=Container(width=160, height=60),\n"
                            ")\n\n"
                            "FittedBox(\n"
                            "    fit=BoxFit.none,\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    child=Container(width=160, height=60),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MouseRegion opaque & hitTestBehavior",
                    description=(
                        "MouseRegion opaque controls whether the region blocks hit testing "
                        "to regions behind it. hitTestBehavior=translucent allows both "
                        "stacked regions to receive events."
                    ),
                    instruction="Hover over the stacked regions. With opaque=False + translucent, both top and bottom fire. With opaque=True, only the top fires.",
                    visible=_MouseRegionOpaqueDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets import MouseRegion, Stack\n"
                            "from flut.flutter.rendering import HitTestBehavior\n\n"
                            "Stack(children=[\n"
                            "    MouseRegion(\n"
                            "        opaque=False,\n"
                            "        hitTestBehavior=HitTestBehavior.translucent,\n"
                            "        onEnter=lambda e: print('bottom'),\n"
                            "        child=Container(...),\n"
                            "    ),\n"
                            "    MouseRegion(\n"
                            "        opaque=True,\n"
                            "        onEnter=lambda e: print('top'),\n"
                            "        child=Container(...),\n"
                            "    ),\n"
                            "])"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SingleChildScrollView reverse & primary",
                    description=(
                        "SingleChildScrollView with reverse=True scrolls content in the "
                        "inverted direction, starting from the bottom."
                    ),
                    instruction="Compare the two scroll views: the left is normal (top-first), the right is reverse (bottom-first).",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Normal (reverse=False)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=120.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=SingleChildScrollView(
                                                reverse=False,
                                                child=Column(
                                                    children=[
                                                        Container(
                                                            height=40.0,
                                                            color=Colors.blue.withValues(
                                                                alpha=0.1 + i * 0.1
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Item {i + 1}",
                                                                    style=TextStyle(
                                                                        fontSize=12
                                                                    ),
                                                                ),
                                                            ),
                                                        )
                                                        for i in range(6)
                                                    ],
                                                ),
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
                                            "Reverse (reverse=True)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=120.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=SingleChildScrollView(
                                                reverse=True,
                                                child=Column(
                                                    children=[
                                                        Container(
                                                            height=40.0,
                                                            color=Colors.green.withValues(
                                                                alpha=0.1 + i * 0.1
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Item {i + 1}",
                                                                    style=TextStyle(
                                                                        fontSize=12
                                                                    ),
                                                                ),
                                                            ),
                                                        )
                                                        for i in range(6)
                                                    ],
                                                ),
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
                            "from flut.flutter.widgets import SingleChildScrollView\n\n"
                            "SingleChildScrollView(\n"
                            "    reverse=False,\n"
                            "    child=Column(children=[...]),\n"
                            ")\n\n"
                            "SingleChildScrollView(\n"
                            "    reverse=True,\n"
                            "    child=Column(children=[...]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SingleChildScrollView clipBehavior",
                    description=(
                        "SingleChildScrollView clipBehavior controls whether overflowing "
                        "content is clipped. Clip.none makes overflow visible outside bounds."
                    ),
                    instruction="Compare the two scroll views: Clip.hardEdge clips content at bounds, Clip.none shows overflow.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Clip.hardEdge (default)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=SingleChildScrollView(
                                                clipBehavior=Clip.hardEdge,
                                                child=Column(
                                                    children=[
                                                        Container(
                                                            height=40.0,
                                                            color=Colors.blue.withValues(
                                                                alpha=0.15 + i * 0.12
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Row {i + 1}",
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
                                        ),
                                    ],
                                ),
                            ),
                            SizedBox(width=12),
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Clip.none (overflow visible)",
                                            style=TextStyle(fontSize=11),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=SingleChildScrollView(
                                                clipBehavior=Clip.none,
                                                child=Column(
                                                    children=[
                                                        Container(
                                                            height=40.0,
                                                            color=Colors.orange.withValues(
                                                                alpha=0.15 + i * 0.12
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Row {i + 1}",
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
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "SingleChildScrollView(\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    child=Column(children=[...]),\n"
                            ")\n\n"
                            "SingleChildScrollView(\n"
                            "    clipBehavior=Clip.none,\n"
                            "    child=Column(children=[...]),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomScrollView clipBehavior & hitTestBehavior",
                    description=(
                        "CustomScrollView clipBehavior controls clipping of overflowing slivers. "
                        "Clip.none vs Clip.hardEdge shown side by side."
                    ),
                    instruction="Compare the two scroll views: Clip.hardEdge clips at bounds, Clip.none allows overflow.",
                    visible=Row(
                        children=[
                            Expanded(
                                child=Column(
                                    children=[
                                        Text(
                                            "Clip.hardEdge",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=120.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=CustomScrollView(
                                                clipBehavior=Clip.hardEdge,
                                                slivers=[
                                                    SliverToBoxAdapter(
                                                        child=Container(
                                                            height=50.0,
                                                            color=Colors.blue.withValues(
                                                                alpha=0.15 + i * 0.12
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Sliver {i + 1}",
                                                                    style=TextStyle(
                                                                        fontSize=12
                                                                    ),
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
                                            "Clip.none",
                                            style=TextStyle(
                                                fontSize=11, fontFamily=CODE_FONT_FAMILY
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Container(
                                            height=120.0,
                                            decoration=BoxDecoration(
                                                color=Color(0xFFF5F5F5),
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                            child=CustomScrollView(
                                                clipBehavior=Clip.none,
                                                slivers=[
                                                    SliverToBoxAdapter(
                                                        child=Container(
                                                            height=50.0,
                                                            color=Colors.orange.withValues(
                                                                alpha=0.15 + i * 0.12
                                                            ),
                                                            child=Center(
                                                                child=Text(
                                                                    f"Sliver {i + 1}",
                                                                    style=TextStyle(
                                                                        fontSize=12
                                                                    ),
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
                            "CustomScrollView(\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    slivers=[...],\n"
                            ")\n\n"
                            "CustomScrollView(\n"
                            "    clipBehavior=Clip.none,\n"
                            "    slivers=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomScrollView semanticChildCount",
                    description=(
                        "CustomScrollView semanticChildCount provides an explicit count "
                        "of semantic children for accessibility. Shown here with "
                        "SliverToBoxAdapter items and a matching count label."
                    ),
                    instruction="The scroll view has semanticChildCount=5 matching the 5 numbered SliverToBoxAdapter items.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "semanticChildCount=5",
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
                                    semanticChildCount=5,
                                    slivers=[
                                        SliverToBoxAdapter(
                                            child=Container(
                                                height=50.0,
                                                color=[
                                                    Colors.red,
                                                    Colors.green,
                                                    Colors.blue,
                                                    Colors.orange,
                                                    Colors.purple,
                                                ][i].withValues(alpha=0.25),
                                                child=Center(
                                                    child=Text(
                                                        f"Semantic item {i + 1} of 5",
                                                        style=TextStyle(fontSize=13),
                                                    ),
                                                ),
                                            ),
                                        )
                                        for i in range(5)
                                    ],
                                ),
                            ),
                            SizedBox(height=4),
                            Text(
                                "semanticChildCount tells accessibility tools how many items exist.",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CustomScrollView(\n"
                            "    semanticChildCount=5,\n"
                            "    slivers=[\n"
                            "        SliverToBoxAdapter(\n"
                            "            child=Text('Item 1 of 5'),\n"
                            "        ),\n"
                            "        SliverToBoxAdapter(\n"
                            "            child=Text('Item 2 of 5'),\n"
                            "        ),\n"
                            "        ...\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Basic Card",
                    description="A Card provides a Material surface with elevation that casts a shadow. The elevation property controls shadow depth.",
                    instruction="Observe the shadow beneath each card at different elevation levels.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Card(
                                elevation=1.0,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Elevation 1.0"),
                                ),
                            ),
                            SizedBox(height=8),
                            Card(
                                elevation=4.0,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Elevation 4.0"),
                                ),
                            ),
                            SizedBox(height=8),
                            Card(
                                elevation=8.0,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Elevation 8.0"),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Card(\n"
                            "    elevation=4.0,\n"
                            "    child=Padding(\n"
                            "        padding=EdgeInsets.all(16),\n"
                            "        child=Text('Elevation 4.0'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Card with Icon and Text",
                    description=(
                        "A common Card pattern: a Row with an Icon on the left "
                        "and a Column of title and subtitle on the right, using Expanded to fill available space."
                    ),
                    instruction="Review the layout structure: icon, spacing, then vertically stacked title and subtitle.",
                    visible=Card(
                        elevation=2.0,
                        child=Padding(
                            padding=EdgeInsets.all(16),
                            child=Row(
                                children=[
                                    Icon(Icons.widgets, color=Colors.blue),
                                    SizedBox(width=16),
                                    Expanded(
                                        child=Column(
                                            crossAxisAlignment=CrossAxisAlignment.start,
                                            children=[
                                                Text(
                                                    "Flutter Widgets",
                                                    style=TextStyle(
                                                        fontSize=16,
                                                        fontWeight=FontWeight.bold,
                                                    ),
                                                ),
                                                SizedBox(height=4),
                                                Text(
                                                    "Build UIs with composable widgets",
                                                    style=TextStyle(
                                                        fontSize=13,
                                                        color=Colors.grey,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Card(\n"
                            "    elevation=2.0,\n"
                            "    child=Padding(\n"
                            "        padding=EdgeInsets.all(16),\n"
                            "        child=Row(\n"
                            "            children=[\n"
                            "                Icon(Icons.widgets, color=Colors.blue),\n"
                            "                SizedBox(width=16),\n"
                            "                Expanded(\n"
                            "                    child=Column(\n"
                            "                        crossAxisAlignment=CrossAxisAlignment.start,\n"
                            "                        children=[\n"
                            "                            Text('Title', style=TextStyle(\n"
                            "                                fontSize=16,\n"
                            "                                fontWeight=FontWeight.bold,\n"
                            "                            )),\n"
                            "                            SizedBox(height=4),\n"
                            "                            Text('Subtitle', style=TextStyle(\n"
                            "                                fontSize=13, color=Colors.grey,\n"
                            "                            )),\n"
                            "                        ],\n"
                            "                    ),\n"
                            "                ),\n"
                            "            ],\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Card Collection",
                    description="Multiple cards rendered in a vertical list, each with an icon, title, and subtitle. Margin controls spacing between cards.",
                    instruction="Scroll through the list of cards. Each represents a different feature with its own icon.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            _info_card(
                                "Flutter Widgets",
                                "Build UIs with composable widgets",
                                Icons.widgets,
                            ),
                            _info_card(
                                "Python Power",
                                "Use Python's rich ecosystem",
                                Icons.code,
                            ),
                            _info_card(
                                "Hot Reload",
                                "See changes instantly (coming soon)",
                                Icons.refresh,
                            ),
                            _info_card(
                                "Cross Platform",
                                "Run on Windows, macOS, Linux",
                                Icons.computer,
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "items = [\n"
                            "    ('Flutter Widgets', 'Composable widgets', Icons.widgets),\n"
                            "    ('Python Power', 'Rich ecosystem', Icons.code),\n"
                            "]\n\n"
                            "Column(\n"
                            "    children=[\n"
                            "        info_card(title, subtitle, icon)\n"
                            "        for title, subtitle, icon in items\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Card Variants",
                    description=(
                        "Card provides named constructors: Card.filled() uses a solid surface color, "
                        "Card.outlined() draws a border instead of elevation shadow."
                    ),
                    instruction="Compare the three card styles: default (elevated), filled (solid background), and outlined (bordered).",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Card(
                                elevation=4.0,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Default Card"),
                                ),
                            ),
                            SizedBox(height=8),
                            Card.filled(
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Card.filled()"),
                                ),
                            ),
                            SizedBox(height=8),
                            Card.outlined(
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("Card.outlined()"),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Card(\n"
                            "    elevation=4.0,\n"
                            "    child=Text('Default'),\n"
                            ")\n"
                            "\n"
                            "Card.filled(child=Text('Filled'))\n"
                            "\n"
                            "Card.outlined(child=Text('Outlined'))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Divider",
                    description=(
                        "Divider renders a thin horizontal line. "
                        "Use indent/endIndent to control inset from edges."
                    ),
                    instruction="See the dividers between items: default, indented, and with custom thickness and color.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text("Above default divider"),
                            Divider(),
                            Text("Above indented divider"),
                            Divider(indent=16.0, endIndent=16.0),
                            Text("Above thick colored divider"),
                            Divider(thickness=3.0, color=Colors.blue),
                            Text("Below"),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Divider()\n"
                            "\n"
                            "Divider(indent=16.0, endIndent=16.0)\n"
                            "\n"
                            "Divider(thickness=3.0, color=Colors.blue)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Material",
                    description=(
                        "Material is the foundational surface widget. Card wraps Material internally. "
                        "Use it directly when you need control over type, elevation, shape, and color."
                    ),
                    instruction="Compare the four Material surfaces: canvas (default), circle shape, transparency, and a custom rounded shape with shadow.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Material(
                                elevation=2.0,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("MaterialType.canvas (default)"),
                                ),
                            ),
                            SizedBox(height=12),
                            Material(
                                type=MaterialType.circle,
                                elevation=4.0,
                                color=Colors.blue,
                                child=SizedBox(
                                    width=80.0,
                                    height=80.0,
                                    child=Icon(Icons.star, color=Colors.white),
                                ),
                            ),
                            SizedBox(height=12),
                            Material(
                                type=MaterialType.transparency,
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text("MaterialType.transparency"),
                                ),
                            ),
                            SizedBox(height=12),
                            Material(
                                elevation=6.0,
                                color=Colors.green,
                                shadowColor=Colors.black,
                                shape=RoundedRectangleBorder(
                                    borderRadius=BorderRadius.circular(16),
                                ),
                                child=Padding(
                                    padding=EdgeInsets.all(16),
                                    child=Text(
                                        "Custom shape + elevation",
                                        style=TextStyle(color=Colors.white),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Material(\n"
                            "    elevation=2.0,\n"
                            "    child=Text('Canvas'),\n"
                            ")\n"
                            "\n"
                            "Material(\n"
                            "    type=MaterialType.circle,\n"
                            "    elevation=4.0,\n"
                            "    color=Colors.blue,\n"
                            "    child=SizedBox(width=80, height=80),\n"
                            ")\n"
                            "\n"
                            "Material(\n"
                            "    elevation=6.0,\n"
                            "    color=Colors.green,\n"
                            "    shape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(16),\n"
                            "    ),\n"
                            "    child=Text('Custom shape'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BoxDecoration backgroundBlendMode",
                    description="BoxDecoration.backgroundBlendMode controls how the decoration's color blends with the content behind it.",
                    instruction="Compare the three blue boxes over an orange background: normal covers it, multiply darkens, screen lightens.",
                    visible=Container(
                        padding=EdgeInsets.all(16),
                        decoration=BoxDecoration(
                            color=Colors.orange,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=Row(
                            children=[
                                Column(
                                    children=[
                                        Container(
                                            width=80.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Colors.blue,
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Text("Normal", style=TextStyle(fontSize=11)),
                                    ],
                                ),
                                SizedBox(width=16),
                                Column(
                                    children=[
                                        Container(
                                            width=80.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Colors.blue,
                                                backgroundBlendMode=BlendMode.multiply,
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Text("Multiply", style=TextStyle(fontSize=11)),
                                    ],
                                ),
                                SizedBox(width=16),
                                Column(
                                    children=[
                                        Container(
                                            width=80.0,
                                            height=80.0,
                                            decoration=BoxDecoration(
                                                color=Colors.blue,
                                                backgroundBlendMode=BlendMode.screen,
                                                borderRadius=BorderRadius.circular(8),
                                            ),
                                        ),
                                        SizedBox(height=4),
                                        Text("Screen", style=TextStyle(fontSize=11)),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "BoxDecoration(\n"
                            "    color=Colors.blue,\n"
                            "    backgroundBlendMode=BlendMode.multiply,\n"
                            "    borderRadius=BorderRadius.circular(8),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BoxShape",
                    description="BoxDecoration.shape controls whether the box is rendered as a rectangle or a circle.",
                    instruction="Compare the rectangular box on the left with the circular box on the right.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Container(
                                        width=80.0,
                                        height=80.0,
                                        decoration=BoxDecoration(
                                            color=Colors.blue,
                                            shape=BoxShape.rectangle,
                                            borderRadius=BorderRadius.circular(8),
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    Text("rectangle", style=TextStyle(fontSize=11)),
                                ],
                            ),
                            SizedBox(width=24),
                            Column(
                                children=[
                                    Container(
                                        width=80.0,
                                        height=80.0,
                                        decoration=BoxDecoration(
                                            color=Colors.green,
                                            shape=BoxShape.circle,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    Text("circle", style=TextStyle(fontSize=11)),
                                ],
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "BoxDecoration(\n"
                            "    color=Colors.blue,\n"
                            "    shape=BoxShape.rectangle,\n"
                            ")\n\n"
                            "BoxDecoration(\n"
                            "    color=Colors.green,\n"
                            "    shape=BoxShape.circle,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Alignment Constants",
                    description=(
                        "All nine Alignment constants visualized. The blue box moves inside "
                        "a fixed container based on the selected alignment."
                    ),
                    instruction="Click an alignment name to reposition the blue box.",
                    visible=_AlignmentPickerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Container(\n"
                            "    width=260.0,\n"
                            "    height=160.0,\n"
                            "    alignment=Alignment.center,\n"
                            "    child=Container(width=50.0, height=50.0, color=Colors.blue),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Container Margin & Asymmetric Border",
                    description=(
                        "Container.margin adds outer spacing, and Border() accepts per-side "
                        "BorderSide values. BorderRadius can target individual corners."
                    ),
                    instruction="Observe the asymmetric margins (gray = outer container) and per-side border colors.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Wrap(
                                spacing=16,
                                runSpacing=8,
                                children=[
                                    Container(
                                        color=Color(0xFFE0E0E0),
                                        child=Container(
                                            margin=EdgeInsets.only(
                                                left=20, top=8, right=40, bottom=16
                                            ),
                                            padding=EdgeInsets.all(12),
                                            decoration=BoxDecoration(
                                                color=Colors.white,
                                                border=Border(
                                                    top=BorderSide(
                                                        color=Colors.red, width=3.0
                                                    ),
                                                    right=BorderSide(
                                                        color=Colors.blue, width=2.0
                                                    ),
                                                    bottom=BorderSide(
                                                        color=Colors.green, width=3.0
                                                    ),
                                                    left=BorderSide(
                                                        color=Colors.orange, width=2.0
                                                    ),
                                                ),
                                            ),
                                            child=Text(
                                                "margin + per-side Border",
                                                style=TextStyle(fontSize=12),
                                            ),
                                        ),
                                    ),
                                    SizedBox(width=16),
                                    Container(
                                        width=100.0,
                                        height=80.0,
                                        decoration=BoxDecoration(
                                            color=Colors.deepPurple,
                                            borderRadius=BorderRadius.only(
                                                topLeft=Radius.circular(20),
                                                bottomRight=Radius.circular(20),
                                            ),
                                        ),
                                        child=Center(
                                            child=Text(
                                                "Diagonal\ncorners",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                    SizedBox(width=16),
                                    Container(
                                        width=80.0,
                                        height=80.0,
                                        decoration=BoxDecoration(
                                            color=Colors.teal,
                                            borderRadius=BorderRadius.all(
                                                Radius.circular(12)
                                            ),
                                        ),
                                        child=Center(
                                            child=Text(
                                                "BR.all(12)",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=11
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(height=8),
                            Row(
                                children=[
                                    Container(
                                        padding=EdgeInsets(10, 20, 30, 40),
                                        color=Color.fromRGBO(65, 105, 225, 0.85),
                                        child=Text(
                                            "EdgeInsets(10,20,30,40) + Color.fromRGBO",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
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
                            "Container(\n"
                            "    margin=EdgeInsets.only(left=20, top=8, right=40, bottom=16),\n"
                            "    decoration=BoxDecoration(\n"
                            "        border=Border(\n"
                            "            top=BorderSide(color=Colors.red, width=3.0),\n"
                            "            right=BorderSide(color=Colors.blue, width=2.0),\n"
                            "        ),\n"
                            "    ),\n"
                            ")\n"
                            "\n"
                            "BoxDecoration(\n"
                            "    borderRadius=BorderRadius(\n"
                            "        topLeft=Radius.circular(20),\n"
                            "        bottomRight=Radius.circular(20),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MainAxisAlignment Spacing",
                    description=(
                        "spaceBetween distributes children with equal space between them "
                        "(no space at edges). spaceAround adds half-space at edges."
                    ),
                    instruction="Compare the spacing of items in each row.",
                    visible=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                "spaceBetween",
                                style=TextStyle(
                                    fontSize=13, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                height=36.0,
                                padding=EdgeInsets.symmetric(horizontal=8),
                                color=Color(0xFFF5F5F5),
                                child=Row(
                                    mainAxisAlignment=MainAxisAlignment.spaceBetween,
                                    children=[
                                        Text("Left"),
                                        Text("Mid"),
                                        Text("Right"),
                                    ],
                                ),
                            ),
                            SizedBox(height=8),
                            Text(
                                "spaceAround",
                                style=TextStyle(
                                    fontSize=13, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=4),
                            Container(
                                height=36.0,
                                color=Color(0xFFE3F2FD),
                                child=Row(
                                    mainAxisAlignment=MainAxisAlignment.spaceAround,
                                    children=[Text("A"), Text("B"), Text("C")],
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Row(\n"
                            "    mainAxisAlignment=MainAxisAlignment.spaceBetween,\n"
                            "    children=[Text('Left'), Text('Mid'), Text('Right')],\n"
                            ")\n"
                            "\n"
                            "Row(\n"
                            "    mainAxisAlignment=MainAxisAlignment.spaceAround,\n"
                            "    children=[Text('A'), Text('B'), Text('C')],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CrossAxisAlignment.stretch",
                    description=(
                        "stretch forces children to fill the cross axis completely, "
                        "ignoring their intrinsic width."
                    ),
                    instruction="Both colored bars extend to the full width of the 300px container.",
                    visible=Container(
                        height=70.0,
                        width=300.0,
                        color=Color(0xFFF5F5F5),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.stretch,
                            children=[
                                Container(
                                    height=28.0,
                                    color=Colors.blue,
                                    child=Center(
                                        child=Text(
                                            "Stretched full width",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
                                            ),
                                        ),
                                    ),
                                ),
                                SizedBox(height=4),
                                Container(
                                    height=28.0,
                                    color=Colors.teal,
                                    child=Center(
                                        child=Text(
                                            "Also stretched",
                                            style=TextStyle(
                                                color=Colors.white, fontSize=12
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
                            "Column(\n"
                            "    crossAxisAlignment=CrossAxisAlignment.stretch,\n"
                            "    children=[\n"
                            "        Container(height=28.0, color=Colors.blue),\n"
                            "        Container(height=28.0, color=Colors.teal),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FlexFit: tight vs loose",
                    description=(
                        "Flexible with FlexFit.tight forces the child to fill all allocated space. "
                        "FlexFit.loose lets the child be smaller than its allocation."
                    ),
                    instruction="The tight child fills its flex share; the loose child shrinks to its content width.",
                    visible=Container(
                        height=40.0,
                        color=Color(0xFFF5F5F5),
                        child=Row(
                            children=[
                                Flexible(
                                    fit=FlexFit.tight,
                                    child=Container(
                                        color=Colors.blue,
                                        child=Padding(
                                            padding=EdgeInsets.all(8),
                                            child=Text(
                                                "tight (fills space)",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                SizedBox(width=4),
                                Flexible(
                                    fit=FlexFit.loose,
                                    child=Container(
                                        color=Colors.teal,
                                        child=Padding(
                                            padding=EdgeInsets.all(8),
                                            child=Text(
                                                "loose (shrinks)",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
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
                            "Row(children=[\n"
                            "    Flexible(\n"
                            "        fit=FlexFit.tight,\n"
                            "        child=Container(color=Colors.blue, child=Text('fills')),\n"
                            "    ),\n"
                            "    Flexible(\n"
                            "        fit=FlexFit.loose,\n"
                            "        child=Container(color=Colors.teal, child=Text('shrinks')),\n"
                            "    ),\n"
                            "])"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Expanded Flex Ratios",
                    description="Expanded divides remaining space proportionally by the flex factor.",
                    instruction="The first child gets 1/4 of the width, the second gets 3/4.",
                    visible=Container(
                        height=36.0,
                        child=Row(
                            children=[
                                Expanded(
                                    flex=1,
                                    child=Container(
                                        color=Colors.blue,
                                        child=Center(
                                            child=Text(
                                                "flex=1",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                SizedBox(width=4),
                                Expanded(
                                    flex=3,
                                    child=Container(
                                        color=Colors.deepPurple,
                                        child=Center(
                                            child=Text(
                                                "flex=3",
                                                style=TextStyle(
                                                    color=Colors.white, fontSize=12
                                                ),
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
                            "Row(children=[\n"
                            "    Expanded(flex=1, child=Container(color=Colors.blue)),\n"
                            "    Expanded(flex=3, child=Container(color=Colors.deepPurple)),\n"
                            "])"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Wrap (vertical direction)",
                    description=(
                        "Wrap with direction=Axis.vertical lays out children top-to-bottom, "
                        "creating a new column when the container height is exceeded."
                    ),
                    instruction="Five colored chips wrap vertically within a 100px-tall container.",
                    visible=Container(
                        height=100.0,
                        child=Wrap(
                            direction=Axis.vertical,
                            spacing=4,
                            runSpacing=8,
                            alignment=WrapAlignment.start,
                            children=[
                                _wrap_chip("1", Colors.red),
                                _wrap_chip("2", Colors.blue),
                                _wrap_chip("3", Colors.green),
                                _wrap_chip("4", Colors.orange),
                                _wrap_chip("5", Colors.purple),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Wrap(\n"
                            "    direction=Axis.vertical,\n"
                            "    spacing=4,\n"
                            "    runSpacing=8,\n"
                            "    children=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Positioned + Stack",
                    description=(
                        "Positioned places children at explicit edges within a Stack. "
                        "Setting opposing edges (left + right, or top + bottom) stretches the child."
                    ),
                    instruction="Four labels are pinned to each corner. The center box stretches between its edges.",
                    visible=Container(
                        width=350.0,
                        height=150.0,
                        decoration=BoxDecoration(
                            border=Border.all(color=Colors.grey, width=1.0),
                        ),
                        child=Stack(
                            children=[
                                Positioned(
                                    left=8,
                                    top=8,
                                    child=Text(
                                        "left+top",
                                        style=TextStyle(fontSize=11),
                                    ),
                                ),
                                Positioned(
                                    right=8,
                                    top=8,
                                    child=Text(
                                        "right+top",
                                        style=TextStyle(fontSize=11),
                                    ),
                                ),
                                Positioned(
                                    left=8,
                                    bottom=8,
                                    child=Text(
                                        "left+bottom",
                                        style=TextStyle(fontSize=11),
                                    ),
                                ),
                                Positioned(
                                    right=8,
                                    bottom=8,
                                    child=Text(
                                        "right+bottom",
                                        style=TextStyle(fontSize=11),
                                    ),
                                ),
                                Positioned(
                                    left=80,
                                    right=80,
                                    top=50,
                                    bottom=50,
                                    child=Container(
                                        color=Colors.blue.withValues(alpha=0.15),
                                        child=Center(
                                            child=Text(
                                                "stretched",
                                                style=TextStyle(fontSize=11),
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
                            "Stack(children=[\n"
                            "    Positioned(left=8, top=8, child=Text('corner')),\n"
                            "    Positioned(\n"
                            "        left=80, right=80, top=50, bottom=50,\n"
                            "        child=Container(color=Colors.blue),\n"
                            "    ),\n"
                            "])"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="OutlinedBorder Shapes",
                    description=(
                        "ElevatedButtons with different OutlinedBorder shapes via "
                        "ButtonStyle.shape. Each shape clips and decorates the button differently."
                    ),
                    instruction="Observe five buttons, each with a distinct border shape.",
                    visible=_OutlinedBorderShapesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ElevatedButton(\n"
                            "    child=Text('Stadium'),\n"
                            "    style=ButtonStyle(\n"
                            "        shape=WidgetStatePropertyAll(StadiumBorder()),\n"
                            "    ),\n"
                            "    onPressed=on_pressed,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedContainer & Curves",
                    description=(
                        "AnimatedContainer smoothly transitions width, height, padding, margin, "
                        "alignment, and decoration. Different Curves control the easing profile."
                    ),
                    instruction="Click Toggle Animation to see the container and curve bars animate.",
                    visible=_AnimatedContainerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=500),\n"
                            "    curve=Curves.easeOut,\n"
                            "    width=280.0 if toggled else 140.0,\n"
                            "    decoration=BoxDecoration(\n"
                            "        color=Colors.deepPurple if toggled else Colors.teal,\n"
                            "        borderRadius=BorderRadius.circular(20 if toggled else 4),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="PanAxis",
                    description=(
                        "PanAxis controls the allowed panning directions in an "
                        "InteractiveViewer: horizontal, vertical, aligned, or free."
                    ),
                    instruction="Shows the PanAxis enum values. Drag the grid freely — panAxis will constrain direction when wired to InteractiveViewer.",
                    visible=_PanAxisDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "InteractiveViewer(\n"
                            "    panAxis=PanAxis.horizontal,\n"
                            "    boundaryMargin=EdgeInsets.all(40),\n"
                            "    child=large_content,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TransformationController",
                    description=(
                        "Programmatic control of scale and translation, simulating what "
                        "TransformationController provides for InteractiveViewer."
                    ),
                    instruction=(
                        "Press buttons to reset, zoom 2x, or pan to an offset. "
                        "The current transform is displayed as text."
                    ),
                    visible=_TransformControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "controller = TransformationController()\n"
                            "InteractiveViewer(\n"
                            "    transformationController=controller,\n"
                            "    child=content,\n"
                            ")\n"
                            "\n"
                            "controller.value = Matrix4.identity()\n"
                            "controller.value = Matrix4.identity()..scale(2.0)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BorderStyle",
                    description=(
                        "BoxDecoration borders support BorderStyle.solid for visible borders "
                        "and BorderStyle.none to hide them while keeping the layout space."
                    ),
                    instruction="Compare the solid border on the left with the invisible (none) border on the right.",
                    visible=Row(
                        children=[
                            Container(
                                width=120.0,
                                height=60.0,
                                decoration=BoxDecoration(
                                    border=Border.all(
                                        color=Colors.blue,
                                        width=2.0,
                                        style=BorderStyle.solid,
                                    ),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Center(
                                    child=Text("solid", style=TextStyle(fontSize=13)),
                                ),
                            ),
                            SizedBox(width=12),
                            Container(
                                width=120.0,
                                height=60.0,
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    border=Border.all(style=BorderStyle.none),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Center(
                                    child=Text("none", style=TextStyle(fontSize=13)),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Border.all(\n"
                            "    color=Colors.blue,\n"
                            "    width=2.0,\n"
                            "    style=BorderStyle.solid,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="OverflowBarAlignment",
                    description=(
                        "OverflowBarAlignment controls how overflowed children align "
                        "when an OverflowBar switches from horizontal to vertical layout. "
                        "Values: start, end, center."
                    ),
                    instruction="Press Toggle Alignment to cycle between start, end, and center alignment of the stacked buttons.",
                    visible=_OverflowBarAlignmentDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.widgets import OverflowBar\n\n"
                            "OverflowBar(\n"
                            "    overflowAlignment=OverflowBarAlignment.center,\n"
                            "    spacing=8,\n"
                            "    overflowSpacing=4,\n"
                            "    children=[\n"
                            "        ElevatedButton(child=Text('Action 1')),\n"
                            "        ElevatedButton(child=Text('Action 2')),\n"
                            "        ElevatedButton(child=Text('Long Action 3')),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
