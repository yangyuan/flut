import math

from flut.dart import Color, Duration, Matrix4
from flut.dart.ui import Clip
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Center,
    Column,
    Row,
    SizedBox,
    Container,
    AnimatedContainer,
    AnimatedOpacity,
    ListenableBuilder,
    Visibility,
    Expanded,
    Icon,
)
from flut.flutter.rendering import BoxConstraints, CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Theme,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Alignment,
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    LinearGradient,
)
from flut.flutter.animation import (
    AnimationController,
    AnimationBehavior,
    AnimationStyle,
    Curves,
)
from flut.flutter.widgets import (
    SingleTickerProviderStateMixin,
    TickerProviderStateMixin,
)

from widgets import CatalogPage, SplitViewTile, CodeArea


class _AnimatedContainerDemo(StatefulWidget):
    def createState(self):
        return _AnimatedContainerDemoState()


class _AnimatedContainerDemoState(State[_AnimatedContainerDemo]):
    def initState(self):
        self.expanded = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Size"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "expanded", not self.expanded)
                    ),
                ),
                SizedBox(height=12),
                AnimatedContainer(
                    duration=Duration(milliseconds=400),
                    width=300.0 if self.expanded else 150.0,
                    height=100.0 if self.expanded else 50.0,
                    color=Colors.deepPurple if self.expanded else Colors.blue,
                    child=Center(
                        child=Text(
                            "Expanded" if self.expanded else "Small",
                            style=TextStyle(color=Colors.white),
                        ),
                    ),
                ),
            ],
        )


class _AnimatedOpacityDemo(StatefulWidget):
    def createState(self):
        return _AnimatedOpacityDemoState()


class _AnimatedOpacityDemoState(State[_AnimatedOpacityDemo]):
    def initState(self):
        self.visible = True

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Opacity"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "visible", not self.visible)
                    ),
                ),
                SizedBox(height=12),
                AnimatedOpacity(
                    opacity=1.0 if self.visible else 0.2,
                    duration=Duration(milliseconds=500),
                    child=Container(
                        width=200.0,
                        height=80.0,
                        color=Colors.teal,
                        child=Center(
                            child=Text(
                                "Fade me",
                                style=TextStyle(color=Colors.white, fontSize=16),
                            ),
                        ),
                    ),
                ),
            ],
        )


class _AnimatedOpacityOnEndDemo(StatefulWidget):
    def createState(self):
        return _AnimatedOpacityOnEndDemoState()


class _AnimatedOpacityOnEndDemoState(State[_AnimatedOpacityOnEndDemo]):
    def initState(self):
        self.fading = True
        self.fade_done_count = 0

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Fade Toggle"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(self, "fading", not self.fading)
                            ),
                        ),
                        SizedBox(width=12),
                        Text(f"onEnd fired {self.fade_done_count} times"),
                    ],
                ),
                SizedBox(height=12),
                AnimatedOpacity(
                    opacity=1.0 if self.fading else 0.0,
                    duration=Duration(milliseconds=600),
                    onEnd=lambda: self.setState(
                        lambda: setattr(
                            self, "fade_done_count", self.fade_done_count + 1
                        )
                    ),
                    child=Container(
                        width=200.0,
                        height=60.0,
                        color=Colors.indigo,
                        child=Center(
                            child=Text(
                                "Watch the counter",
                                style=TextStyle(color=Colors.white),
                            ),
                        ),
                    ),
                ),
            ],
        )


class _AnimationControllerDemo(StatefulWidget):
    def createState(self):
        return _AnimationControllerDemoState()


class _AnimationControllerDemoState(
    State[_AnimationControllerDemo], SingleTickerProviderStateMixin
):
    def initState(self):
        self.anim = AnimationController(
            duration=Duration(seconds=2),
            vsync=self,
            lowerBound=0.0,
            upperBound=1.0,
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Forward"),
                            onPressed=lambda: self.anim.forward(),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reverse"),
                            onPressed=lambda: self.anim.reverse(),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Repeat"),
                            onPressed=lambda: self.anim.repeat(reverse=True),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Stop"),
                            onPressed=lambda: self.anim.stop(),
                        ),
                    ],
                ),
                SizedBox(height=12),
                ListenableBuilder(
                    listenable=self.anim,
                    builder=lambda ctx, child: Container(
                        width=50.0 + self.anim.value * 250.0,
                        height=40.0,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(8),
                            gradient=LinearGradient(
                                colors=[Colors.blue, Colors.purple],
                            ),
                        ),
                        child=Center(
                            child=Text(
                                f"{self.anim.value:.2f}",
                                style=TextStyle(color=Colors.white, fontSize=12),
                            ),
                        ),
                    ),
                ),
            ],
        )


def _duration_bar(label, duration, expanded):
    return Row(
        children=[
            SizedBox(
                width=130.0,
                child=Text(label, style=TextStyle(fontSize=12)),
            ),
            Expanded(
                child=AnimatedContainer(
                    duration=duration,
                    width=280.0 if expanded else 40.0,
                    height=32.0,
                    decoration=BoxDecoration(
                        color=Colors.blue if expanded else Colors.grey,
                        borderRadius=BorderRadius.circular(6),
                    ),
                    child=Center(
                        child=Text(
                            f"{duration.inMilliseconds}ms",
                            style=TextStyle(color=Colors.white, fontSize=11),
                        ),
                    ),
                ),
            ),
        ],
    )


class _DurationDemo(StatefulWidget):
    def createState(self):
        return _DurationDemoState()


class _DurationDemoState(State[_DurationDemo]):
    def initState(self):
        self.expanded = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Animate All"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "expanded", not self.expanded)
                    ),
                ),
                SizedBox(height=12),
                _duration_bar(
                    "200ms (fast)", Duration(milliseconds=200), self.expanded
                ),
                SizedBox(height=6),
                _duration_bar("500ms", Duration(milliseconds=500), self.expanded),
                SizedBox(height=6),
                _duration_bar("1 second", Duration(seconds=1), self.expanded),
                SizedBox(height=6),
                _duration_bar("2 seconds (slow)", Duration(seconds=2), self.expanded),
                SizedBox(height=6),
                _duration_bar(
                    "1s + 500ms",
                    Duration(seconds=1) + Duration(milliseconds=500),
                    self.expanded,
                ),
                SizedBox(height=6),
                _duration_bar(
                    "500ms * 3", Duration(milliseconds=500) * 3, self.expanded
                ),
            ],
        )


class _AnimationBehaviorDemo(StatefulWidget):
    def createState(self):
        return _AnimationBehaviorDemoState()


class _AnimationBehaviorDemoState(
    State[_AnimationBehaviorDemo], TickerProviderStateMixin
):
    def initState(self):
        self.reduced_motion = False
        self.anim_normal = AnimationController(
            duration=Duration(seconds=2),
            vsync=self,
        )
        self.anim_preserve = AnimationController(
            duration=Duration(seconds=2),
            vsync=self,
        )

    def build(self, context):
        if self.reduced_motion:
            self.anim_normal.duration = Duration(seconds=10)
        else:
            self.anim_normal.duration = Duration(seconds=2)
        self.anim_preserve.duration = Duration(seconds=2)

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Toggle Reduced Motion"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "reduced_motion", not self.reduced_motion
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"Reduced motion: {'ON' if self.reduced_motion else 'OFF'}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Forward"),
                            onPressed=lambda: (
                                self.anim_normal.forward(),
                                self.anim_preserve.forward(),
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reverse"),
                            onPressed=lambda: (
                                self.anim_normal.reverse(),
                                self.anim_preserve.reverse(),
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Stop"),
                            onPressed=lambda: (
                                self.anim_normal.stop(),
                                self.anim_preserve.stop(),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Text(
                    f"AnimationBehavior.normal ({self.anim_normal.duration}):",
                    style=TextStyle(fontSize=12),
                ),
                SizedBox(height=4),
                ListenableBuilder(
                    listenable=self.anim_normal,
                    builder=lambda ctx, child: Container(
                        width=50.0 + self.anim_normal.value * 250.0,
                        height=30.0,
                        decoration=BoxDecoration(
                            color=Colors.blue,
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Center(
                            child=Text(
                                f"{self.anim_normal.value:.2f}",
                                style=TextStyle(color=Colors.white, fontSize=11),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    f"AnimationBehavior.preserve ({self.anim_preserve.duration}):",
                    style=TextStyle(fontSize=12),
                ),
                SizedBox(height=4),
                ListenableBuilder(
                    listenable=self.anim_preserve,
                    builder=lambda ctx, child: Container(
                        width=50.0 + self.anim_preserve.value * 250.0,
                        height=30.0,
                        decoration=BoxDecoration(
                            color=Colors.deepPurple,
                            borderRadius=BorderRadius.circular(6),
                        ),
                        child=Center(
                            child=Text(
                                f"{self.anim_preserve.value:.2f}",
                                style=TextStyle(color=Colors.white, fontSize=11),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    "When reduced motion is ON, .normal slows down "
                    "(respects accessibility).\n"
                    ".preserve keeps original speed (ignores accessibility).",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _AnimationStyleDemo(StatefulWidget):
    def createState(self):
        return _AnimationStyleDemoState()


class _AnimationStyleDemoState(State[_AnimationStyleDemo]):
    def initState(self):
        self.style_index = 0
        self.toggled = False

    def build(self, context):
        style_names = ["Fast (100ms, linear)", "Slow (2s, easeInOut)", "No animation"]
        durations = [
            Duration(milliseconds=100),
            Duration(seconds=2),
            Duration.zero,
        ]
        curves = [Curves.linear, Curves.easeInOut, Curves.linear]

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Cycle Style"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "style_index",
                                    (self.style_index + 1) % 3,
                                )
                            ),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Toggle State"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(self, "toggled", not self.toggled)
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"Style: {style_names[self.style_index]}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
                SizedBox(height=12),
                AnimatedContainer(
                    duration=durations[self.style_index],
                    curve=curves[self.style_index],
                    width=280.0 if self.toggled else 150.0,
                    height=80.0 if self.toggled else 50.0,
                    color=Colors.deepPurple if self.toggled else Colors.teal,
                    child=Center(
                        child=Text(
                            "Toggled" if self.toggled else "Default",
                            style=TextStyle(color=Colors.white),
                        ),
                    ),
                ),
            ],
        )


class _ForegroundDecorationDemo(StatefulWidget):
    def createState(self):
        return _ForegroundDecorationDemoState()


class _ForegroundDecorationDemoState(State[_ForegroundDecorationDemo]):
    def initState(self):
        self.show_overlay = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Foreground Overlay"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show_overlay", not self.show_overlay)
                    ),
                ),
                SizedBox(height=12),
                AnimatedContainer(
                    duration=Duration(milliseconds=400),
                    width=200.0,
                    height=100.0,
                    decoration=BoxDecoration(
                        color=Colors.blue,
                        borderRadius=BorderRadius.circular(12),
                    ),
                    foregroundDecoration=(
                        BoxDecoration(
                            color=Color(0x80FF0000),
                            borderRadius=BorderRadius.circular(12),
                        )
                        if self.show_overlay
                        else None
                    ),
                    child=Center(
                        child=Text(
                            "Overlay ON" if self.show_overlay else "Overlay OFF",
                            style=TextStyle(color=Colors.white, fontSize=14),
                        ),
                    ),
                ),
            ],
        )


class _ConstraintsDemo(StatefulWidget):
    def createState(self):
        return _ConstraintsDemoState()


class _ConstraintsDemoState(State[_ConstraintsDemo]):
    def initState(self):
        self.large = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Constraints"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "large", not self.large)
                    ),
                ),
                SizedBox(height=12),
                AnimatedContainer(
                    duration=Duration(milliseconds=500),
                    constraints=(
                        BoxConstraints(maxWidth=400, maxHeight=200)
                        if self.large
                        else BoxConstraints(maxWidth=200, maxHeight=100)
                    ),
                    decoration=BoxDecoration(
                        color=Colors.teal,
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=Center(
                        child=Text(
                            "400x200" if self.large else "200x100",
                            style=TextStyle(color=Colors.white, fontSize=14),
                        ),
                    ),
                ),
            ],
        )


class _TransformAlignmentDemo(StatefulWidget):
    def createState(self):
        return _TransformAlignmentDemoState()


class _TransformAlignmentDemoState(State[_TransformAlignmentDemo]):
    def initState(self):
        self.rotated = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Toggle Rotation"),
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "rotated", not self.rotated)
                    ),
                ),
                SizedBox(height=24),
                Center(
                    child=AnimatedContainer(
                        duration=Duration(milliseconds=600),
                        width=150.0,
                        height=80.0,
                        transform=(
                            Matrix4.rotationZ(math.pi / 6)
                            if self.rotated
                            else Matrix4.identity()
                        ),
                        transformAlignment=Alignment.center,
                        decoration=BoxDecoration(
                            color=Colors.deepPurple,
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Center(
                            child=Text(
                                "Rotated" if self.rotated else "Normal",
                                style=TextStyle(color=Colors.white, fontSize=14),
                            ),
                        ),
                    ),
                ),
            ],
        )


class _AnimControllerDebugLabelDemo(StatefulWidget):
    def createState(self):
        return _AnimControllerDebugLabelDemoState()


class _AnimControllerDebugLabelDemoState(
    State[_AnimControllerDebugLabelDemo], SingleTickerProviderStateMixin
):
    def initState(self):
        self.anim = AnimationController(
            duration=Duration(seconds=2),
            vsync=self,
            debugLabel="fade-controller",
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Forward"),
                            onPressed=lambda: self.anim.forward(),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reverse"),
                            onPressed=lambda: self.anim.reverse(),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Repeat"),
                            onPressed=lambda: self.anim.repeat(reverse=True),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Stop"),
                            onPressed=lambda: self.anim.stop(),
                        ),
                    ],
                ),
                SizedBox(height=12),
                ListenableBuilder(
                    listenable=self.anim,
                    builder=lambda ctx, child: Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Text(
                                f"debugLabel: fade-controller",
                                style=TextStyle(
                                    fontSize=13, fontWeight=FontWeight.bold
                                ),
                            ),
                            SizedBox(height=6),
                            Row(
                                children=[
                                    Container(
                                        width=50.0 + self.anim.value * 200.0,
                                        height=30.0,
                                        decoration=BoxDecoration(
                                            color=Colors.indigo,
                                            borderRadius=BorderRadius.circular(6),
                                        ),
                                    ),
                                    SizedBox(width=8),
                                    Text(
                                        f"value: {self.anim.value:.3f}",
                                        style=TextStyle(fontSize=12),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        )


class AnimationPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Animations & Visual Effects",
            description=(
                "Shows how widgets change over time with implicit transitions, "
                "explicit controllers, transforms, visibility changes, and "
                "decorative effects you can compare on screen."
            ),
            children=[
                SplitViewTile(
                    title="AnimatedContainer",
                    description="Implicitly animates changes to width, height, and color over a given duration.",
                    instruction="Press Toggle Size to animate between small/blue and expanded/purple states.",
                    visible=_AnimatedContainerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=400),\n"
                            "    width=300.0 if expanded else 150.0,\n"
                            "    height=100.0 if expanded else 50.0,\n"
                            "    color=Colors.deepPurple if expanded else Colors.blue,\n"
                            "    child=Center(child=Text('...')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedOpacity",
                    description="Smoothly transitions a widget's opacity between two values.",
                    instruction="Press Toggle Opacity to fade the box between full and 20% opacity.",
                    visible=_AnimatedOpacityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AnimatedOpacity(\n"
                            "    opacity=1.0 if visible else 0.2,\n"
                            "    duration=Duration(milliseconds=500),\n"
                            "    child=Container(\n"
                            "        width=200.0, height=80.0,\n"
                            "        color=Colors.teal,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedOpacity with onEnd",
                    description="The onEnd callback fires each time the animation completes, useful for chaining logic.",
                    instruction="Press Fade Toggle and watch the counter increment each time the fade animation finishes.",
                    visible=_AnimatedOpacityOnEndDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AnimatedOpacity(\n"
                            "    opacity=1.0 if fading else 0.0,\n"
                            "    duration=Duration(milliseconds=600),\n"
                            "    onEnd=lambda: increment_counter(),\n"
                            "    child=Container(width=200.0, height=60.0),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimationController",
                    description=(
                        "Explicit animation via AnimationController + ListenableBuilder. "
                        "The controller runs in Dart; the builder rebuilds on each frame."
                    ),
                    instruction="Use Forward, Reverse, Repeat, and Stop to control the animation. The bar width and value label update in real time.",
                    visible=_AnimationControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "anim = AnimationController(\n"
                            "    duration=Duration(seconds=2),\n"
                            "    vsync=self,\n"
                            "    lowerBound=0.0,\n"
                            "    upperBound=1.0,\n"
                            ")\n"
                            "\n"
                            "ListenableBuilder(\n"
                            "    listenable=anim,\n"
                            "    builder=lambda ctx, child: Container(\n"
                            "        width=50.0 + anim.value * 250.0,\n"
                            "        height=40.0,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Duration",
                    description=(
                        "Duration controls how long animations take. Different constructors "
                        "and arithmetic let you express precise timings."
                    ),
                    instruction="Press Animate All — all bars animate simultaneously but each uses a different Duration, so you can see and feel the speed difference.",
                    visible=_DurationDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "# Each bar uses a different Duration\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=200),  # fast\n"
                            "    ...\n"
                            ")\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(seconds=2),          # slow\n"
                            "    ...\n"
                            ")\n\n"
                            "# Arithmetic builds durations\n"
                            "Duration(seconds=1) + Duration(milliseconds=500)\n"
                            "Duration(milliseconds=500) * 3\n"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimationBehavior",
                    description=(
                        "AnimationBehavior.normal respects accessibility reduce-motion settings "
                        "by slowing or disabling animations. AnimationBehavior.preserve ignores "
                        "those settings and always animates at the configured speed."
                    ),
                    instruction="Toggle Reduced Motion, then press Forward. The .normal bar slows to 10s while .preserve stays at 2s.",
                    visible=_AnimationBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.animation import AnimationBehavior\n\n"
                            "AnimationController(\n"
                            "    duration=Duration(seconds=2),\n"
                            "    vsync=self,\n"
                            "    animationBehavior=AnimationBehavior.normal,\n"
                            ")\n\n"
                            "AnimationController(\n"
                            "    duration=Duration(seconds=2),\n"
                            "    vsync=self,\n"
                            "    animationBehavior=AnimationBehavior.preserve,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimationStyle",
                    description=(
                        "AnimationStyle bundles curve and duration into a reusable preset. "
                        "AnimationStyle.noAnimation disables transitions instantly. "
                        "Custom styles control speed and easing."
                    ),
                    instruction="Cycle Style to switch between fast/slow/noAnimation, then press Toggle State to see the container animate.",
                    visible=_AnimationStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.animation import AnimationStyle, Curves\n\n"
                            "fast_style = AnimationStyle(\n"
                            "    duration=Duration(milliseconds=100),\n"
                            "    curve=Curves.linear,\n"
                            ")\n\n"
                            "slow_style = AnimationStyle(\n"
                            "    duration=Duration(seconds=2),\n"
                            "    curve=Curves.easeInOut,\n"
                            ")\n\n"
                            "no_anim = AnimationStyle.noAnimation"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedContainer foregroundDecoration",
                    description="Animates a foregroundDecoration on top of the container. A semi-transparent red BoxDecoration overlay appears and disappears smoothly.",
                    instruction="Press Toggle Foreground Overlay to animate a red semi-transparent overlay on/off the blue container.",
                    visible=_ForegroundDecorationDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=400),\n"
                            "    width=200.0, height=100.0,\n"
                            "    decoration=BoxDecoration(\n"
                            "        color=Colors.blue,\n"
                            "        borderRadius=BorderRadius.circular(12),\n"
                            "    ),\n"
                            "    foregroundDecoration=BoxDecoration(\n"
                            "        color=Color(0x80FF0000),\n"
                            "        borderRadius=BorderRadius.circular(12),\n"
                            "    ) if show_overlay else None,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedContainer constraints",
                    description="Animates between two BoxConstraints, smoothly resizing the container between small and large maximum dimensions.",
                    instruction="Press Toggle Constraints to animate between maxWidth=200/maxHeight=100 and maxWidth=400/maxHeight=200.",
                    visible=_ConstraintsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.rendering import BoxConstraints\n\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=500),\n"
                            "    constraints=BoxConstraints(\n"
                            "        maxWidth=400, maxHeight=200,\n"
                            "    ) if large else BoxConstraints(\n"
                            "        maxWidth=200, maxHeight=100,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedContainer transform & transformAlignment",
                    description="Animates a Matrix4 rotation transform with transformAlignment set to center, so the container rotates smoothly around its center point.",
                    instruction="Press Toggle Rotation to animate the container rotating 30 degrees (pi/6 radians) around its center.",
                    visible=_TransformAlignmentDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "import math\n"
                            "from flut.dart import Matrix4\n\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=600),\n"
                            "    transform=Matrix4.rotationZ(math.pi / 6)\n"
                            "        if rotated else Matrix4.identity(),\n"
                            "    transformAlignment=Alignment.center,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimatedContainer clipBehavior",
                    description="clipBehavior controls whether child content that overflows the container bounds is visible or clipped. Clip.none allows overflow; Clip.hardEdge clips it.",
                    instruction="Compare the two containers: the left one with Clip.none shows the overflowing child, the right one with Clip.hardEdge clips it.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Text(
                                        "Clip.none",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    AnimatedContainer(
                                        duration=Duration(milliseconds=300),
                                        width=100.0,
                                        height=60.0,
                                        clipBehavior=Clip.none,
                                        decoration=BoxDecoration(
                                            color=Colors.blue,
                                            borderRadius=BorderRadius.circular(8),
                                        ),
                                        child=Container(
                                            width=160.0,
                                            height=40.0,
                                            color=Colors.orange,
                                            child=Center(
                                                child=Text(
                                                    "Overflows!",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=11
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            SizedBox(width=80),
                            Column(
                                children=[
                                    Text(
                                        "Clip.hardEdge",
                                        style=TextStyle(
                                            fontSize=13, fontWeight=FontWeight.bold
                                        ),
                                    ),
                                    SizedBox(height=8),
                                    AnimatedContainer(
                                        duration=Duration(milliseconds=300),
                                        width=100.0,
                                        height=60.0,
                                        clipBehavior=Clip.hardEdge,
                                        decoration=BoxDecoration(
                                            color=Colors.blue,
                                            borderRadius=BorderRadius.circular(8),
                                        ),
                                        child=Container(
                                            width=160.0,
                                            height=40.0,
                                            color=Colors.orange,
                                            child=Center(
                                                child=Text(
                                                    "Clipped!",
                                                    style=TextStyle(
                                                        color=Colors.white, fontSize=11
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
                            "from flut.dart.ui import Clip\n\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=300),\n"
                            "    width=100.0, height=60.0,\n"
                            "    clipBehavior=Clip.none,\n"
                            "    child=Container(width=160.0, height=40.0),\n"
                            ")\n\n"
                            "AnimatedContainer(\n"
                            "    duration=Duration(milliseconds=300),\n"
                            "    width=100.0, height=60.0,\n"
                            "    clipBehavior=Clip.hardEdge,\n"
                            "    child=Container(width=160.0, height=40.0),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimationController debugLabel",
                    description="debugLabel assigns a name to an AnimationController for identification. The label is shown alongside the live animation value.",
                    instruction="Press Forward, Reverse, Repeat, or Stop to control the animation. The debugLabel and current value are displayed in real time.",
                    visible=_AnimControllerDebugLabelDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "anim = AnimationController(\n"
                            "    duration=Duration(seconds=2),\n"
                            "    vsync=self,\n"
                            "    debugLabel='fade-controller',\n"
                            ")\n\n"
                            "ListenableBuilder(\n"
                            "    listenable=anim,\n"
                            "    builder=lambda ctx, child: Text(\n"
                            "        f'debugLabel: {anim.debugLabel}\\n'\n"
                            "        f'value: {anim.value:.3f}',\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
