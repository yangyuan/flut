from flut.dart import Color, Brightness, Duration
from flut.dart.ui import Clip
from flut.flutter.animation import AnimationStyle
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Padding,
    SingleChildScrollView,
    Center,
    Expanded,
    Icon,
    Navigator,
    RouteSettings,
    ModalRoute,
    PageRoute,
    Stack,
    Positioned,
    SingleTickerProviderStateMixin,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.material import (
    Colors,
    ColorScheme,
    ElevatedButton,
    ExpansionTile,
    MaterialApp,
    Scaffold,
    AppBar,
    Icons,
    MaterialPageRoute,
    NavigationBar,
    NavigationDestination,
    NavigationDestinationLabelBehavior,
    Switch,
    TabController,
    DefaultTabController,
    TabBar,
    TabBarView,
    Tab,
    Theme,
    ThemeData,
    ThemeMode,
    Drawer,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    RoundedRectangleBorder,
)
from flut.flutter.widgets.scroll_physics import BouncingScrollPhysics

from utils import CODE_FONT_FAMILY
from widgets import CatalogPage, SplitViewTile, CodeArea


def _info_row(label, value):
    return Padding(
        padding=EdgeInsets.symmetric(vertical=2),
        child=Row(
            children=[
                Text(
                    f"{label}: ",
                    style=TextStyle(
                        fontSize=13,
                        fontWeight=FontWeight.bold,
                        color=Color(0xFF555555),
                    ),
                ),
                Text(
                    value,
                    style=TextStyle(fontSize=13, color=Colors.blue),
                ),
            ],
        ),
    )


class _DetailPage(StatefulWidget):
    def __init__(self, *, key=None, title="Detail", message="Hello from navigation!"):
        super().__init__(key=key)
        self.title = title
        self.message = message

    def createState(self):
        return _DetailPageState()


class _DetailPageState(State[_DetailPage]):

    def initState(self):
        self.pop_count = 0

    def build(self, context):
        route = ModalRoute.of(context)

        route_info_items = []
        if route is not None:
            route_info_items.append(
                _info_row("isCurrent", str(route.isCurrent)),
            )
            route_info_items.append(
                _info_row("isActive", str(route.isActive)),
            )
            route_info_items.append(
                _info_row("canPop", str(route.canPop)),
            )
            settings = route.settings
            if settings is not None:
                route_info_items.append(
                    _info_row("settings.name", str(settings.name)),
                )

            route_info_items.append(SizedBox(height=12))
            route_info_items.append(
                Text(
                    "isinstance checks (Python inheritance)",
                    style=TextStyle(
                        fontSize=14,
                        fontWeight=FontWeight.bold,
                        color=Colors.deepPurple,
                    ),
                ),
            )
            route_info_items.append(SizedBox(height=4))
            route_info_items.append(
                _info_row(
                    "isinstance(route, ModalRoute)", str(isinstance(route, ModalRoute))
                ),
            )
            route_info_items.append(
                _info_row(
                    "isinstance(route, PageRoute)", str(isinstance(route, PageRoute))
                ),
            )
            route_info_items.append(
                _info_row(
                    "isinstance(route, MaterialPageRoute)",
                    str(isinstance(route, MaterialPageRoute)),
                ),
            )
            route_info_items.append(
                _info_row("type(route).__name__", type(route).__name__),
            )
            route_info_items.append(
                _info_row(
                    "type(route).__mro__",
                    " → ".join(c.__name__ for c in type(route).__mro__[:5]),
                ),
            )
        else:
            route_info_items.append(
                Text("ModalRoute.of(context) returned None"),
            )

        return Scaffold(
            appBar=AppBar(
                title=Text(self.widget.title),
            ),
            body=SingleChildScrollView(
                padding=EdgeInsets.all(24),
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Container(
                            padding=EdgeInsets.all(16),
                            decoration=BoxDecoration(
                                color=Color(0xFFE8F5E9),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Row(
                                children=[
                                    Icon(Icons.check_circle, color=Colors.green),
                                    SizedBox(width=12),
                                    Text(
                                        self.widget.message,
                                        style=TextStyle(fontSize=16),
                                    ),
                                ],
                            ),
                        ),
                        SizedBox(height=24),
                        Text(
                            "Route Information",
                            style=TextStyle(fontSize=16, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=8),
                        Container(
                            padding=EdgeInsets.all(12),
                            decoration=BoxDecoration(
                                color=Color(0xFFF5F5F5),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=route_info_items,
                            ),
                        ),
                        SizedBox(height=24),
                        Row(
                            children=[
                                ElevatedButton(
                                    child=Text("Go Back"),
                                    onPressed=lambda: Navigator.pop(context),
                                ),
                                SizedBox(width=12),
                                ElevatedButton(
                                    child=Text("Push Another"),
                                    onPressed=lambda: Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                            builder=lambda ctx: (
                                                _DetailPage(
                                                    title="Nested Detail",
                                                    message="Pushed from detail page!",
                                                )
                                                .createState()
                                                ._build_standalone(ctx)
                                                if False
                                                else _NestedPage()
                                            ),
                                            settings=RouteSettings(name="/nested"),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )


class _NestedPage(StatefulWidget):
    def createState(self):
        return _NestedPageState()


class _NestedPageState(State[_NestedPage]):

    def build(self, context):
        route = ModalRoute.of(context)

        inherit_items = []
        if route is not None:
            inherit_items.append(
                _info_row(
                    "isinstance(route, ModalRoute)", str(isinstance(route, ModalRoute))
                ),
            )
            inherit_items.append(
                _info_row(
                    "isinstance(route, PageRoute)", str(isinstance(route, PageRoute))
                ),
            )
            inherit_items.append(
                _info_row(
                    "isinstance(route, MaterialPageRoute)",
                    str(isinstance(route, MaterialPageRoute)),
                ),
            )

        can_pop = Navigator.canPop(context)

        return Scaffold(
            appBar=AppBar(title=Text("Nested Page")),
            body=SingleChildScrollView(
                padding=EdgeInsets.all(24),
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Container(
                            padding=EdgeInsets.all(16),
                            decoration=BoxDecoration(
                                color=Color(0xFFFFF3E0),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Row(
                                children=[
                                    Icon(Icons.layers, color=Colors.orange),
                                    SizedBox(width=12),
                                    Text(
                                        "This is a nested navigation page",
                                        style=TextStyle(fontSize=16),
                                    ),
                                ],
                            ),
                        ),
                        SizedBox(height=24),
                        Text(
                            "Inheritance Hierarchy",
                            style=TextStyle(fontSize=16, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=8),
                        Container(
                            padding=EdgeInsets.all(12),
                            decoration=BoxDecoration(
                                color=Color(0xFFF3E5F5),
                                borderRadius=BorderRadius.circular(8),
                            ),
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=inherit_items,
                            ),
                        ),
                        SizedBox(height=16),
                        _info_row("Navigator.canPop(context)", str(can_pop)),
                        SizedBox(height=24),
                        ElevatedButton(
                            child=Text("Pop Back"),
                            onPressed=lambda: Navigator.pop(context),
                        ),
                    ],
                ),
            ),
        )


class _BasicNavigationDemo(StatefulWidget):
    def createState(self):
        return _BasicNavigationDemoState()


class _BasicNavigationDemoState(State[_BasicNavigationDemo]):

    def initState(self):
        self.push_count = 0

    def _push_detail(self, context):
        Navigator.push(
            context,
            MaterialPageRoute(
                builder=lambda ctx: _DetailPage(
                    title="Detail Page",
                    message="Pushed via Navigator.push!",
                ),
            ),
        )

    def _push_with_settings(self, context):
        self.push_count += 1
        Navigator.push(
            context,
            MaterialPageRoute(
                builder=lambda ctx: _DetailPage(
                    title="Page with Settings",
                    message=f"Push #{self.push_count} with RouteSettings",
                ),
                settings=RouteSettings(name=f"/detail/{self.push_count}"),
            ),
        )

    def build(self, context):
        return Row(
            children=[
                ElevatedButton(
                    child=Text("Push Detail Page"),
                    onPressed=lambda: self._push_detail(context),
                ),
                SizedBox(width=12),
                ElevatedButton(
                    child=Text("Push with Settings"),
                    onPressed=lambda: self._push_with_settings(context),
                ),
            ],
        )


class _NavigationBarDemo(StatefulWidget):
    def createState(self):
        return _NavigationBarDemoState()


class _NavigationBarDemoState(State[_NavigationBarDemo]):

    def initState(self):
        self.nav_index = 0

    def _on_nav_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_nav_changed,
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected tab: {['Home', 'Search', 'Profile'][self.nav_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _FullscreenDialogDemo(StatelessWidget):

    def build(self, context):
        return ElevatedButton(
            child=Text("Push Fullscreen Dialog"),
            onPressed=lambda: Navigator.push(
                context,
                MaterialPageRoute(
                    builder=lambda ctx: _DetailPage(
                        title="Fullscreen Dialog",
                        message="This was pushed as fullscreenDialog=True",
                    ),
                    fullscreenDialog=True,
                    settings=RouteSettings(name="/fullscreen"),
                ),
            ),
        )


class _PushReplacementDemo(StatelessWidget):

    def build(self, context):
        return ElevatedButton(
            child=Text("Push Replacement"),
            onPressed=lambda: Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                    builder=lambda ctx: _DetailPage(
                        title="Replacement Page",
                        message="This replaced the previous route (can't go back).",
                    ),
                    settings=RouteSettings(name="/replacement"),
                ),
            ),
        )


class _TabControllerDemo(StatefulWidget):
    def createState(self):
        return _TabControllerDemoState()


class _TabControllerDemoState(
    State[_TabControllerDemo], SingleTickerProviderStateMixin
):
    def initState(self):
        self.controller = TabController(length=3, vsync=self)

    def _go_to(self, index):
        self.controller.animateTo(index)
        self.setState(lambda: None)

    def build(self, context):
        tab_names = ["Home", "Search", "Profile"]
        return Container(
            height=350.0,
            child=Column(
                children=[
                    Row(
                        mainAxisAlignment=MainAxisAlignment.center,
                        children=[
                            ElevatedButton(
                                child=Text("Go to 0"),
                                onPressed=lambda: self._go_to(0),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                child=Text("Go to 1"),
                                onPressed=lambda: self._go_to(1),
                            ),
                            SizedBox(width=8),
                            ElevatedButton(
                                child=Text("Go to 2"),
                                onPressed=lambda: self._go_to(2),
                            ),
                        ],
                    ),
                    SizedBox(height=8),
                    Text(
                        f"index: {self.controller.index}  |  indexIsChanging: {self.controller.indexIsChanging}",
                        style=TextStyle(fontSize=13, color=Colors.grey),
                    ),
                    SizedBox(height=8),
                    Expanded(
                        child=Scaffold(
                            appBar=AppBar(
                                title=Text("Programmatic Tabs"),
                                bottom=TabBar(
                                    controller=self.controller,
                                    tabs=[
                                        Tab(text="Home", icon=Icon(Icons.home)),
                                        Tab(text="Search", icon=Icon(Icons.search)),
                                        Tab(text="Profile", icon=Icon(Icons.person)),
                                    ],
                                ),
                            ),
                            body=TabBarView(
                                controller=self.controller,
                                children=[
                                    Center(
                                        child=Text(
                                            "Home Content",
                                            style=TextStyle(fontSize=18),
                                        )
                                    ),
                                    Center(
                                        child=Text(
                                            "Search Content",
                                            style=TextStyle(fontSize=18),
                                        )
                                    ),
                                    Center(
                                        child=Text(
                                            "Profile Content",
                                            style=TextStyle(fontSize=18),
                                        )
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
            ),
        )


class _LabelBehaviorDemo(StatefulWidget):
    def createState(self):
        return _LabelBehaviorDemoState()


class _LabelBehaviorDemoState(State[_LabelBehaviorDemo]):
    def initState(self):
        self.nav_index = 0
        self.behavior_index = 0

    def _cycle_behavior(self):
        self.behavior_index = (self.behavior_index + 1) % 3
        self.setState(lambda: None)

    def _on_nav_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        behaviors = [
            NavigationDestinationLabelBehavior.alwaysShow,
            NavigationDestinationLabelBehavior.alwaysHide,
            NavigationDestinationLabelBehavior.onlyShowSelected,
        ]
        behavior_names = ["alwaysShow", "alwaysHide", "onlyShowSelected"]
        current = behaviors[self.behavior_index]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text(f"labelBehavior: {behavior_names[self.behavior_index]}"),
                    onPressed=self._cycle_behavior,
                ),
                SizedBox(height=12),
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_nav_changed,
                    labelBehavior=current,
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {['Home', 'Search', 'Profile'][self.nav_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _AnimationStyleDemo(StatefulWidget):
    def createState(self):
        return _AnimationStyleDemoState()


class _AnimationStyleDemoState(State[_AnimationStyleDemo]):
    def build(self, context):
        tile_children = [
            Padding(
                padding=EdgeInsets.all(12),
                child=Text("Expanded content area"),
            ),
        ]
        return Row(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Expanded(
                    child=Column(
                        children=[
                            Text(
                                "Default Animation",
                                style=TextStyle(
                                    fontSize=13,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                            ExpansionTile(
                                title=Text("Tap me"),
                                children=tile_children,
                            ),
                        ],
                    ),
                ),
                SizedBox(width=16),
                Expanded(
                    child=Column(
                        children=[
                            Text(
                                "No Animation",
                                style=TextStyle(
                                    fontSize=13,
                                    fontWeight=FontWeight.bold,
                                ),
                            ),
                            ExpansionTile(
                                title=Text("Tap me"),
                                expansionAnimationStyle=AnimationStyle.noAnimation,
                                children=tile_children,
                            ),
                        ],
                    ),
                ),
            ],
        )


class _BrightnessDemo(StatelessWidget):
    def build(self, context):
        theme_data = Theme.of(context)
        scheme = theme_data.colorScheme
        brightness = scheme.brightness
        is_dark = brightness == Brightness.dark
        label = "dark" if is_dark else "light"
        return Container(
            padding=EdgeInsets.all(16),
            decoration=BoxDecoration(
                color=scheme.surface,
                borderRadius=BorderRadius.circular(8),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        f"ColorScheme.brightness = Brightness.{label}",
                        style=TextStyle(
                            fontSize=14,
                            fontWeight=FontWeight.bold,
                            color=scheme.onSurface,
                        ),
                    ),
                    SizedBox(height=8),
                    Row(
                        children=[
                            _color_chip("primary", scheme.primary),
                            SizedBox(width=8),
                            _color_chip("secondary", scheme.secondary),
                            SizedBox(width=8),
                            _color_chip("surface", scheme.surface),
                            SizedBox(width=8),
                            _color_chip("error", scheme.error),
                        ],
                    ),
                ],
            ),
        )


def _color_chip(label, color):
    return Column(
        children=[
            Container(
                width=48.0,
                height=48.0,
                decoration=BoxDecoration(
                    color=color,
                    borderRadius=BorderRadius.circular(8),
                ),
            ),
            SizedBox(height=4),
            Text(label, style=TextStyle(fontSize=11, color=Colors.grey)),
        ],
    )


class _ThemeModeDemo(StatefulWidget):
    def createState(self):
        return _ThemeModeDemoState()


class _ThemeModeDemoState(State[_ThemeModeDemo]):
    def initState(self):
        self.mode_index = 0

    def _set_mode(self, index):
        self.mode_index = index
        self.setState(lambda: None)

    def build(self, context):
        modes = [ThemeMode.system, ThemeMode.light, ThemeMode.dark]
        mode_names = ["system", "light", "dark"]
        current_mode = modes[self.mode_index]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("System"),
                            onPressed=lambda: self._set_mode(0),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Light"),
                            onPressed=lambda: self._set_mode(1),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Dark"),
                            onPressed=lambda: self._set_mode(2),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"ThemeMode: {mode_names[self.mode_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
                SizedBox(height=12),
                Container(
                    height=200.0,
                    child=MaterialApp(
                        title="Theme Preview",
                        theme=ThemeData(
                            colorScheme=ColorScheme.fromSeed(
                                seedColor=Colors.blue,
                            ),
                        ),
                        darkTheme=ThemeData(
                            colorScheme=ColorScheme.fromSeed(
                                seedColor=Colors.blue,
                                brightness=Brightness.dark,
                            ),
                        ),
                        themeMode=current_mode,
                        home=Scaffold(
                            appBar=AppBar(title=Text("Preview")),
                            body=Center(
                                child=Text(
                                    f"Theme: {mode_names[self.mode_index]}",
                                    style=TextStyle(fontSize=16),
                                ),
                            ),
                        ),
                    ),
                ),
            ],
        )


class _DrawerShapeDemo(StatefulWidget):
    def createState(self):
        return _DrawerShapeDemoState()


class _DrawerShapeDemoState(State[_DrawerShapeDemo]):
    def build(self, context):
        return Container(
            height=300.0,
            child=Scaffold(
                appBar=AppBar(title=Text("Drawer Demo")),
                drawer=Drawer(
                    shadowColor=Colors.purple,
                    shape=RoundedRectangleBorder(
                        borderRadius=BorderRadius.circular(24),
                    ),
                    surfaceTintColor=Colors.green,
                    clipBehavior=Clip.antiAlias,
                    child=Padding(
                        padding=EdgeInsets.all(24),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                SizedBox(height=48),
                                Text(
                                    "Styled Drawer",
                                    style=TextStyle(
                                        fontSize=20,
                                        fontWeight=FontWeight.bold,
                                    ),
                                ),
                                SizedBox(height=12),
                                Text("shadowColor: purple"),
                                Text("shape: RoundedRectangleBorder(24)"),
                                Text("surfaceTintColor: green"),
                                Text("clipBehavior: antiAlias"),
                            ],
                        ),
                    ),
                ),
                body=Center(
                    child=Text("Tap the menu icon to open drawer"),
                ),
            ),
        )


class _NavBarAnimDurationDemo(StatefulWidget):
    def createState(self):
        return _NavBarAnimDurationDemoState()


class _NavBarAnimDurationDemoState(State[_NavBarAnimDurationDemo]):
    def initState(self):
        self.nav_index = 0

    def _on_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_changed,
                    animationDuration=Duration(seconds=2),
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {['Home', 'Search', 'Profile'][self.nav_index]} (2s animation)",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _NavBarShadowSurfaceDemo(StatefulWidget):
    def createState(self):
        return _NavBarShadowSurfaceDemoState()


class _NavBarShadowSurfaceDemoState(State[_NavBarShadowSurfaceDemo]):
    def initState(self):
        self.nav_index = 0

    def _on_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_changed,
                    shadowColor=Colors.red,
                    surfaceTintColor=Colors.amber,
                    elevation=8.0,
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {['Home', 'Search', 'Profile'][self.nav_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _NavBarIndicatorDemo(StatefulWidget):
    def createState(self):
        return _NavBarIndicatorDemoState()


class _NavBarIndicatorDemoState(State[_NavBarIndicatorDemo]):
    def initState(self):
        self.nav_index = 0

    def _on_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_changed,
                    indicatorShape=RoundedRectangleBorder(
                        borderRadius=BorderRadius.circular(4),
                    ),
                    overlayColor=WidgetStatePropertyAll(
                        Color(0x1AF44336),
                    ),
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {['Home', 'Search', 'Profile'][self.nav_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _NavBarLabelStyleDemo(StatefulWidget):
    def createState(self):
        return _NavBarLabelStyleDemoState()


class _NavBarLabelStyleDemoState(State[_NavBarLabelStyleDemo]):
    def initState(self):
        self.nav_index = 0

    def _on_changed(self, index):
        self.nav_index = index
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                NavigationBar(
                    selectedIndex=self.nav_index,
                    onDestinationSelected=self._on_changed,
                    labelTextStyle=WidgetStatePropertyAll(
                        TextStyle(
                            fontSize=16,
                            fontWeight=FontWeight.bold,
                            color=Colors.deepPurple,
                        ),
                    ),
                    labelPadding=EdgeInsets.only(top=8),
                    destinations=[
                        NavigationDestination(
                            icon=Icon(Icons.home),
                            label="Home",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.search),
                            label="Search",
                        ),
                        NavigationDestination(
                            icon=Icon(Icons.person),
                            label="Profile",
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {['Home', 'Search', 'Profile'][self.nav_index]}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _TabBarViewPhysicsDemo(StatefulWidget):
    def createState(self):
        return _TabBarViewPhysicsDemoState()


class _TabBarViewPhysicsDemoState(State[_TabBarViewPhysicsDemo]):
    def build(self, context):
        return Container(
            height=350.0,
            child=DefaultTabController(
                length=3,
                child=Scaffold(
                    appBar=AppBar(
                        title=Text("ViewportFraction Demo"),
                        bottom=TabBar(
                            tabs=[
                                Tab(text="Red"),
                                Tab(text="Green"),
                                Tab(text="Blue"),
                            ],
                        ),
                    ),
                    body=TabBarView(
                        viewportFraction=0.8,
                        physics=BouncingScrollPhysics(),
                        clipBehavior=Clip.none,
                        children=[
                            Container(
                                color=Color(0xFFFFCDD2),
                                child=Center(
                                    child=Text(
                                        "Red Tab",
                                        style=TextStyle(fontSize=24),
                                    ),
                                ),
                            ),
                            Container(
                                color=Color(0xFFC8E6C9),
                                child=Center(
                                    child=Text(
                                        "Green Tab",
                                        style=TextStyle(fontSize=24),
                                    ),
                                ),
                            ),
                            Container(
                                color=Color(0xFFBBDEFB),
                                child=Center(
                                    child=Text(
                                        "Blue Tab",
                                        style=TextStyle(fontSize=24),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        )


class _HighContrastThemeDemo(StatefulWidget):
    def createState(self):
        return _HighContrastThemeDemoState()


class _HighContrastThemeDemoState(State[_HighContrastThemeDemo]):

    def initState(self):
        self.high_contrast = False

    def _make_panel(
        self,
        surface,
        on_surface,
        primary,
        on_primary,
        secondary,
        on_secondary,
        error,
        on_error,
        label,
    ):
        return Expanded(
            child=Container(
                height=200,
                padding=EdgeInsets.all(12),
                decoration=BoxDecoration(
                    color=surface,
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            label,
                            style=TextStyle(
                                fontSize=14,
                                fontWeight=FontWeight.bold,
                                color=on_surface,
                            ),
                        ),
                        SizedBox(height=8),
                        Container(
                            width=80,
                            height=32,
                            decoration=BoxDecoration(
                                color=primary,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Center(
                                child=Text(
                                    "Primary",
                                    style=TextStyle(fontSize=12, color=on_primary),
                                ),
                            ),
                        ),
                        SizedBox(height=8),
                        Container(
                            width=80,
                            height=32,
                            decoration=BoxDecoration(
                                color=secondary,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Center(
                                child=Text(
                                    "Secondary",
                                    style=TextStyle(fontSize=12, color=on_secondary),
                                ),
                            ),
                        ),
                        SizedBox(height=8),
                        Container(
                            width=80,
                            height=32,
                            decoration=BoxDecoration(
                                color=error,
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Center(
                                child=Text(
                                    "Error",
                                    style=TextStyle(fontSize=12, color=on_error),
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        )

    def build(self, context):
        normal_panel = self._make_panel(
            surface=Color(0xFFFFFFFF),
            on_surface=Color(0xFF000000),
            primary=Color(0xFF6200EE),
            on_primary=Color(0xFFFFFFFF),
            secondary=Color(0xFF03DAC6),
            on_secondary=Color(0xFF000000),
            error=Color(0xFFB00020),
            on_error=Color(0xFFFFFFFF),
            label="Normal",
        )

        if self.high_contrast:
            right_panel = self._make_panel(
                surface=Color(0xFF000000),
                on_surface=Color(0xFFFFFFFF),
                primary=Color(0xFFFF0000),
                on_primary=Color(0xFFFFFFFF),
                secondary=Color(0xFF00FF00),
                on_secondary=Color(0xFF000000),
                error=Color(0xFFFFFF00),
                on_error=Color(0xFF000000),
                label="High Contrast",
            )
        else:
            right_panel = self._make_panel(
                surface=Color(0xFFFFFFFF),
                on_surface=Color(0xFF000000),
                primary=Color(0xFF6200EE),
                on_primary=Color(0xFFFFFFFF),
                secondary=Color(0xFF03DAC6),
                on_secondary=Color(0xFF000000),
                error=Color(0xFFB00020),
                on_error=Color(0xFFFFFFFF),
                label="Normal (copy)",
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Text(
                            "High Contrast",
                            style=TextStyle(fontSize=14, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(width=8),
                        Switch(
                            value=self.high_contrast,
                            onChanged=lambda v: self.setState(
                                lambda: setattr(self, "high_contrast", v)
                            ),
                        ),
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        normal_panel,
                        SizedBox(width=12),
                        right_panel,
                    ],
                ),
            ],
        )


class _DebugBannerDemo(StatelessWidget):
    def build(self, context):
        def make_app_mock(show_banner, label):
            content = Container(
                width=140,
                height=100,
                decoration=BoxDecoration(
                    color=Color(0xFFF5F5F5),
                    borderRadius=BorderRadius.circular(8),
                ),
                child=Center(
                    child=Text(
                        label,
                        style=TextStyle(fontSize=12, color=Colors.grey),
                    ),
                ),
            )
            if show_banner:
                return Stack(
                    children=[
                        content,
                        Positioned(
                            top=0,
                            right=0,
                            child=Container(
                                padding=EdgeInsets.symmetric(horizontal=6, vertical=2),
                                decoration=BoxDecoration(
                                    color=Color(0xFFA30000),
                                    borderRadius=BorderRadius(
                                        topRight=8,
                                        bottomLeft=8,
                                    ),
                                ),
                                child=Text(
                                    "DEBUG",
                                    style=TextStyle(
                                        fontSize=10,
                                        fontWeight=FontWeight.bold,
                                        color=Colors.white,
                                    ),
                                ),
                            ),
                        ),
                    ],
                )
            return content

        color_box = Container(
            width=40,
            height=40,
            decoration=BoxDecoration(
                color=Color(0xFF42A5F5),
                borderRadius=BorderRadius.circular(8),
            ),
            child=Center(
                child=Text(
                    "C",
                    style=TextStyle(
                        fontSize=16,
                        fontWeight=FontWeight.bold,
                        color=Colors.white,
                    ),
                ),
            ),
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Text(
                            "color (app switcher):",
                            style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(width=8),
                        color_box,
                        SizedBox(width=4),
                        Text(
                            "Color(0xFF42A5F5)",
                            style=TextStyle(
                                fontSize=11,
                                fontFamily=CODE_FONT_FAMILY,
                                color=Colors.grey,
                            ),
                        ),
                    ],
                ),
                SizedBox(height=16),
                Text(
                    "debugShowCheckedModeBanner",
                    style=TextStyle(fontSize=13, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        Column(
                            children=[
                                make_app_mock(True, "banner=True"),
                                SizedBox(height=4),
                                Text(
                                    "Default (True)",
                                    style=TextStyle(fontSize=11, color=Colors.grey),
                                ),
                            ],
                        ),
                        SizedBox(width=16),
                        Column(
                            children=[
                                make_app_mock(False, "banner=False"),
                                SizedBox(height=4),
                                Text(
                                    "Set to False",
                                    style=TextStyle(fontSize=11, color=Colors.grey),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )


class NavigationPage(StatelessWidget):

    def build(self, context):
        return CatalogPage(
            title="Navigation",
            description=(
                "Covers route-based navigation, moving between screens, and "
                "inspecting the active route stack as pages are pushed and popped."
            ),
            children=[
                SplitViewTile(
                    title="Basic Navigation",
                    description=(
                        "Push and pop pages using Navigator with MaterialPageRoute. "
                        "The detail page displays route information and isinstance checks "
                        "against the ModalRoute hierarchy."
                    ),
                    instruction=(
                        "Click 'Push Detail Page' to navigate to a detail page. "
                        "Click 'Push with Settings' to push with named RouteSettings "
                        "and an incrementing counter."
                    ),
                    visible=_BasicNavigationDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Navigator.push(\n"
                            "    context,\n"
                            "    MaterialPageRoute(\n"
                            "        builder=lambda ctx: DetailPage(),\n"
                            "        settings=RouteSettings(name='/detail'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationBar",
                    description=(
                        "Material 3 bottom navigation bar with destination items. "
                        "Each destination has an icon and label."
                    ),
                    instruction="Tap each destination to change the selected index.",
                    visible=_NavigationBarDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=nav_index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    destinations=[\n"
                            "        NavigationDestination(\n"
                            "            icon=Icon(Icons.home),\n"
                            "            label='Home',\n"
                            "        ),\n"
                            "        NavigationDestination(\n"
                            "            icon=Icon(Icons.search),\n"
                            "            label='Search',\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Drawer",
                    description=(
                        "Drawer provides a slide-out side panel for navigation, "
                        "typically attached via Scaffold(drawer=Drawer(...)). "
                        "Opened by the hamburger icon or Scaffold.of(context).openDrawer()."
                    ),
                    instruction=(
                        "Drawer is not shown inline. Use Scaffold's drawer parameter "
                        "and open it programmatically or via the AppBar menu icon."
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Scaffold(\n"
                            "    drawer=Drawer(\n"
                            "        child=ListView(children=[...]),\n"
                            "    ),\n"
                            "    body=Center(child=Text('Main content')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Fullscreen Dialog",
                    description=(
                        "A route pushed with fullscreenDialog=True displays a close button "
                        "instead of a back arrow in the AppBar."
                    ),
                    instruction="Click the button to push a fullscreen dialog route.",
                    visible=_FullscreenDialogDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Navigator.push(\n"
                            "    context,\n"
                            "    MaterialPageRoute(\n"
                            "        builder=lambda ctx: MyPage(),\n"
                            "        fullscreenDialog=True,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Push Replacement",
                    description=(
                        "Replaces the current route so the user cannot navigate back to it. "
                        "Useful for login-to-home transitions."
                    ),
                    instruction="Click the button to replace the current route with a new one.",
                    visible=_PushReplacementDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Navigator.pushReplacement(\n"
                            "    context,\n"
                            "    MaterialPageRoute(\n"
                            "        builder=lambda ctx: MyPage(),\n"
                            "        settings=RouteSettings(name='/replacement'),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Python Inheritance (isinstance)",
                    description=(
                        "Flut's route classes use true Python inheritance. "
                        "MaterialPageRoute extends PageRoute extends ModalRoute. "
                        "All isinstance checks work correctly. "
                        "MRO: MaterialPageRoute \u2192 PageRoute \u2192 ModalRoute "
                        "\u2192 FlutRealtimeObject \u2192 FlutObject."
                    ),
                    instruction=(
                        "Push a detail page from the Basic Navigation tile above "
                        "to see live isinstance checks on the route object."
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "route = ModalRoute.of(context)\n"
                            "isinstance(route, ModalRoute)\n"
                            "isinstance(route, PageRoute)\n"
                            "isinstance(route, MaterialPageRoute)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Navigator API",
                    description="Core Navigator static methods for imperative route management.",
                    instruction="Use these methods to push, pop, and query the navigation stack.",
                    code=CodeArea(
                        language="python",
                        code=(
                            "Navigator.push(context, MaterialPageRoute(\n"
                            "    builder=lambda ctx: MyPage(),\n"
                            "    settings=RouteSettings(name='/detail'),\n"
                            "))\n"
                            "\n"
                            "Navigator.pop(context)\n"
                            "Navigator.canPop(context)\n"
                            "Navigator.pushReplacement(context, route)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DefaultTabController + TabBar + TabBarView",
                    description=(
                        "Tab navigation with DefaultTabController. "
                        "The TickerProvider is internal to the Dart widget "
                        "\u2014 no Python mixin needed."
                    ),
                    instruction="Click each tab to switch between Home, Search, and Profile content areas.",
                    visible=Container(
                        height=350.0,
                        child=DefaultTabController(
                            length=3,
                            child=Scaffold(
                                appBar=AppBar(
                                    title=Text("Tabs"),
                                    bottom=TabBar(
                                        tabs=[
                                            Tab(text="Home", icon=Icon(Icons.home)),
                                            Tab(text="Search", icon=Icon(Icons.search)),
                                            Tab(
                                                text="Profile",
                                                icon=Icon(Icons.person),
                                            ),
                                        ],
                                    ),
                                ),
                                body=TabBarView(
                                    children=[
                                        Center(
                                            child=Text(
                                                "Home Tab",
                                                style=TextStyle(fontSize=18),
                                            )
                                        ),
                                        Center(
                                            child=Text(
                                                "Search Tab",
                                                style=TextStyle(fontSize=18),
                                            )
                                        ),
                                        Center(
                                            child=Text(
                                                "Profile Tab",
                                                style=TextStyle(fontSize=18),
                                            )
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DefaultTabController(\n"
                            "    length=3,\n"
                            "    child=Scaffold(\n"
                            "        appBar=AppBar(\n"
                            "            title=Text('Tabs'),\n"
                            "            bottom=TabBar(\n"
                            "                tabs=[\n"
                            "                    Tab(text='Home', icon=Icon(Icons.home)),\n"
                            "                    Tab(text='Search', icon=Icon(Icons.search)),\n"
                            "                ],\n"
                            "            ),\n"
                            "        ),\n"
                            "        body=TabBarView(\n"
                            "            children=[\n"
                            "                Center(child=Text('Home Tab')),\n"
                            "                Center(child=Text('Search Tab')),\n"
                            "            ],\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TabController (Programmatic)",
                    description=(
                        "Explicit TabController with vsync=self for programmatic "
                        "tab switching. The State class uses SingleTickerProviderStateMixin "
                        "to provide the required TickerProvider."
                    ),
                    instruction=(
                        "Click 'Go to 0', 'Go to 1', or 'Go to 2' to animate "
                        "to that tab. Watch the current index and indexIsChanging update."
                    ),
                    visible=_TabControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class MyTabState(\n"
                            "    State[MyTabWidget], SingleTickerProviderStateMixin\n"
                            "):\n"
                            "    def initState(self):\n"
                            "        self.controller = TabController(length=3, vsync=self)\n"
                            "\n"
                            "    def build(self, context):\n"
                            "        return Scaffold(\n"
                            "            appBar=AppBar(\n"
                            "                bottom=TabBar(\n"
                            "                    controller=self.controller,\n"
                            "                    tabs=[Tab(text='A'), Tab(text='B')],\n"
                            "                ),\n"
                            "            ),\n"
                            "            body=TabBarView(\n"
                            "                controller=self.controller,\n"
                            "                children=[Text('A'), Text('B')],\n"
                            "            ),\n"
                            "        )\n"
                            "\n"
                            "self.controller.animateTo(1)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Tab iconMargin",
                    description="iconMargin controls the spacing between a Tab's icon and its text label. Compare default spacing to custom iconMargin=EdgeInsets.only(bottom=16).",
                    instruction="Two tabs side by side inside a TabBar: the left tab uses default icon margin, the right tab uses a larger bottom margin of 16px.",
                    visible=DefaultTabController(
                        length=2,
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                TabBar(
                                    tabs=[
                                        Tab(
                                            text="Default",
                                            icon=Icon(Icons.star),
                                        ),
                                        Tab(
                                            text="bottom=16",
                                            icon=Icon(Icons.settings),
                                            iconMargin=EdgeInsets.only(bottom=16),
                                        ),
                                    ],
                                ),
                                SizedBox(height=8),
                                Text(
                                    "Left tab: default iconMargin\n"
                                    "Right tab: iconMargin=EdgeInsets.only(bottom=16)",
                                    style=TextStyle(fontSize=11, color=Colors.grey),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "from flut.flutter.material import (\n"
                            "    Tab, TabBar, DefaultTabController, Icons,\n"
                            ")\n\n"
                            "Tab(\n"
                            "    text='Default',\n"
                            "    icon=Icon(Icons.star),\n"
                            ")\n\n"
                            "Tab(\n"
                            "    text='bottom=16',\n"
                            "    icon=Icon(Icons.settings),\n"
                            "    iconMargin=EdgeInsets.only(bottom=16),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationDestinationLabelBehavior",
                    description=(
                        "Controls whether NavigationBar destination labels are shown. "
                        "alwaysShow keeps all labels visible, alwaysHide removes them, "
                        "and onlyShowSelected shows only the active label."
                    ),
                    instruction=(
                        "Click the toggle button to cycle through alwaysShow, "
                        "alwaysHide, and onlyShowSelected. Watch the labels appear and disappear."
                    ),
                    visible=_LabelBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    labelBehavior=NavigationDestinationLabelBehavior.alwaysHide,\n"
                            "    destinations=[\n"
                            "        NavigationDestination(\n"
                            "            icon=Icon(Icons.home),\n"
                            "            label='Home',\n"
                            "        ),\n"
                            "        NavigationDestination(\n"
                            "            icon=Icon(Icons.search),\n"
                            "            label='Search',\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AnimationStyle.noAnimation",
                    description=(
                        "AnimationStyle.noAnimation disables expand/collapse animation "
                        "on ExpansionTile. Compare side by side with default animation."
                    ),
                    instruction=(
                        "Tap both ExpansionTiles. The left uses default animated "
                        "expand; the right expands instantly with noAnimation."
                    ),
                    visible=_AnimationStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ExpansionTile(\n"
                            "    title=Text('Animated'),\n"
                            "    children=[Text('content')],\n"
                            ")\n"
                            "\n"
                            "ExpansionTile(\n"
                            "    title=Text('Instant'),\n"
                            "    expansionAnimationStyle=AnimationStyle.noAnimation,\n"
                            "    children=[Text('content')],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ColorScheme Brightness",
                    description=(
                        "Read the current theme's brightness from ColorScheme to adapt UI. "
                        "Shows the primary, secondary, surface, and error colors from the active color scheme."
                    ),
                    instruction="Observe the current theme brightness and its color scheme values. Switch between light and dark theme to see changes.",
                    visible=_BrightnessDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "scheme = Theme.of(context).colorScheme\n"
                            "is_dark = scheme.brightness == Brightness.dark\n\n"
                            "Container(\n"
                            "    color=scheme.surface,\n"
                            "    child=Text(\n"
                            "        f'Brightness: {scheme.brightness}',\n"
                            "        style=TextStyle(color=scheme.onSurface),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ThemeMode",
                    description=(
                        "ThemeMode controls whether a MaterialApp uses the light theme, "
                        "dark theme, or follows the system setting. "
                        "Requires both theme and darkTheme to be set."
                    ),
                    instruction=(
                        "Click System, Light, or Dark to switch the ThemeMode. "
                        "The preview area below changes its color scheme accordingly."
                    ),
                    visible=_ThemeModeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "MaterialApp(\n"
                            "    theme=ThemeData(\n"
                            "        colorScheme=ColorScheme.fromSeed(\n"
                            "            seedColor=Colors.blue,\n"
                            "        ),\n"
                            "    ),\n"
                            "    darkTheme=ThemeData(\n"
                            "        colorScheme=ColorScheme.fromSeed(\n"
                            "            seedColor=Colors.blue,\n"
                            "            brightness=Brightness.dark,\n"
                            "        ),\n"
                            "    ),\n"
                            "    themeMode=ThemeMode.dark,\n"
                            "    home=Scaffold(body=Text('Hello')),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MaterialApp highContrastTheme",
                    description=(
                        "MaterialApp accepts a highContrastTheme parameter for "
                        "accessibility. When the system reports high-contrast mode, "
                        "this ThemeData is used instead of the normal theme. Here we "
                        "simulate normal vs high-contrast ColorSchemes side by side."
                    ),
                    instruction=(
                        "Toggle the switch to activate high-contrast mode. The right "
                        "panel switches from a copy of the normal scheme to a high-contrast "
                        "scheme with black background, white text, and bright primary/error colors."
                    ),
                    visible=_HighContrastThemeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "MaterialApp(\n"
                            "    theme=ThemeData(\n"
                            "        colorScheme=ColorScheme(\n"
                            "            brightness=Brightness.light,\n"
                            "            primary=Color(0xFF6200EE),\n"
                            "            ...\n"
                            "        ),\n"
                            "    ),\n"
                            "    highContrastTheme=ThemeData(\n"
                            "        colorScheme=ColorScheme(\n"
                            "            brightness=Brightness.dark,\n"
                            "            primary=Color(0xFFFF0000),\n"
                            "            surface=Color(0xFF000000),\n"
                            "            onSurface=Color(0xFFFFFFFF),\n"
                            "            ...\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MaterialApp color & debugShowCheckedModeBanner",
                    description=(
                        "MaterialApp.color sets the application color shown in the OS "
                        "task switcher (Android). debugShowCheckedModeBanner controls "
                        "the 'DEBUG' ribbon in the top-right corner (True by default)."
                    ),
                    instruction=(
                        "Compare the two mock app panels: one shows the DEBUG ribbon "
                        "(default behavior), the other has it removed. The colored box "
                        "demonstrates the color parameter used for the OS switcher."
                    ),
                    visible=_DebugBannerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "MaterialApp(\n"
                            "    color=Color(0xFF42A5F5),\n"
                            "    debugShowCheckedModeBanner=False,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar automaticallyImplyLeading",
                    description=(
                        "automaticallyImplyLeading controls whether the AppBar "
                        "automatically inserts a leading widget (back arrow or "
                        "hamburger icon). Set to False to suppress it."
                    ),
                    instruction=(
                        "Compare the two AppBars: the left one has a hamburger "
                        "icon (automaticallyImplyLeading=True with a drawer), "
                        "the right one has no leading icon (False)."
                    ),
                    visible=Row(
                        children=[
                            Expanded(
                                child=Container(
                                    height=120.0,
                                    child=Scaffold(
                                        appBar=AppBar(
                                            title=Text("True"),
                                            automaticallyImplyLeading=True,
                                        ),
                                        drawer=Drawer(
                                            child=Text("Drawer"),
                                        ),
                                        body=Center(
                                            child=Text(
                                                "Has leading icon",
                                                style=TextStyle(fontSize=12),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            SizedBox(width=8),
                            Expanded(
                                child=Container(
                                    height=120.0,
                                    child=Scaffold(
                                        appBar=AppBar(
                                            title=Text("False"),
                                            automaticallyImplyLeading=False,
                                        ),
                                        drawer=Drawer(
                                            child=Text("Drawer"),
                                        ),
                                        body=Center(
                                            child=Text(
                                                "No leading icon",
                                                style=TextStyle(fontSize=12),
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
                            "AppBar(\n"
                            "    title=Text('My Page'),\n"
                            "    automaticallyImplyLeading=True,\n"
                            ")\n"
                            "\n"
                            "AppBar(\n"
                            "    title=Text('My Page'),\n"
                            "    automaticallyImplyLeading=False,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar shadowColor & foregroundColor",
                    description=(
                        "shadowColor sets the color of the AppBar shadow. "
                        "foregroundColor sets the color of AppBar text and icons."
                    ),
                    instruction=(
                        "Observe the amber-colored title text (foregroundColor) "
                        "and the red shadow beneath the AppBar (shadowColor)."
                    ),
                    visible=Container(
                        height=120.0,
                        child=Scaffold(
                            appBar=AppBar(
                                title=Text("Shadow & Foreground"),
                                shadowColor=Colors.red,
                                foregroundColor=Colors.amber,
                                elevation=8.0,
                            ),
                            body=Center(
                                child=Text("shadowColor=red, foregroundColor=amber"),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    title=Text('My Title'),\n"
                            "    shadowColor=Colors.red,\n"
                            "    foregroundColor=Colors.amber,\n"
                            "    elevation=8.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar titleSpacing & toolbarHeight",
                    description=(
                        "titleSpacing controls horizontal space around the title. "
                        "toolbarHeight sets the height of the toolbar area."
                    ),
                    instruction=(
                        "Compare the two AppBars: the top one has titleSpacing=0 "
                        "(title flush left), the bottom one has toolbarHeight=80 (tall bar)."
                    ),
                    visible=Column(
                        children=[
                            Container(
                                height=80.0,
                                child=Scaffold(
                                    appBar=AppBar(
                                        title=Text("titleSpacing=0"),
                                        titleSpacing=0.0,
                                    ),
                                    body=SizedBox(),
                                ),
                            ),
                            SizedBox(height=8),
                            Container(
                                height=120.0,
                                child=Scaffold(
                                    appBar=AppBar(
                                        title=Text("toolbarHeight=80"),
                                        toolbarHeight=80.0,
                                    ),
                                    body=SizedBox(),
                                ),
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    title=Text('Flush Left'),\n"
                            "    titleSpacing=0.0,\n"
                            ")\n"
                            "\n"
                            "AppBar(\n"
                            "    title=Text('Tall Bar'),\n"
                            "    toolbarHeight=80.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar toolbarOpacity & bottomOpacity",
                    description=(
                        "toolbarOpacity makes the toolbar area semi-transparent. "
                        "bottomOpacity makes the bottom widget (e.g. TabBar) semi-transparent."
                    ),
                    instruction=(
                        "Observe the faded toolbar (0.5 opacity) and the "
                        "very faint TabBar at the bottom (0.3 opacity)."
                    ),
                    visible=Container(
                        height=200.0,
                        child=DefaultTabController(
                            length=2,
                            child=Scaffold(
                                appBar=AppBar(
                                    title=Text("Opacity Demo"),
                                    toolbarOpacity=0.5,
                                    bottomOpacity=0.3,
                                    bottom=TabBar(
                                        tabs=[
                                            Tab(text="Tab 1"),
                                            Tab(text="Tab 2"),
                                        ],
                                    ),
                                ),
                                body=Center(
                                    child=Text(
                                        "toolbarOpacity=0.5, bottomOpacity=0.3",
                                        style=TextStyle(fontSize=13),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    title=Text('Faded'),\n"
                            "    toolbarOpacity=0.5,\n"
                            "    bottomOpacity=0.3,\n"
                            "    bottom=TabBar(\n"
                            "        tabs=[Tab(text='A'), Tab(text='B')],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar toolbarTextStyle & titleTextStyle",
                    description=(
                        "titleTextStyle sets the style for the AppBar title. "
                        "toolbarTextStyle sets the default text style for "
                        "toolbar children other than the title."
                    ),
                    instruction=(
                        "Observe the large, bold, deep-purple title text "
                        "styled via titleTextStyle, and the smaller grey "
                        "toolbar text via toolbarTextStyle."
                    ),
                    visible=Container(
                        height=120.0,
                        child=Scaffold(
                            appBar=AppBar(
                                title=Text("Custom Styled Title"),
                                titleTextStyle=TextStyle(
                                    fontSize=24,
                                    fontWeight=FontWeight.bold,
                                    color=Colors.deepPurple,
                                    letterSpacing=1.5,
                                ),
                                toolbarTextStyle=TextStyle(
                                    fontSize=12,
                                    color=Colors.grey,
                                ),
                            ),
                            body=Center(
                                child=Text("titleTextStyle + toolbarTextStyle"),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    title=Text('Styled'),\n"
                            "    titleTextStyle=TextStyle(\n"
                            "        fontSize=24,\n"
                            "        fontWeight=FontWeight.bold,\n"
                            "        color=Colors.deepPurple,\n"
                            "    ),\n"
                            "    toolbarTextStyle=TextStyle(\n"
                            "        fontSize=12,\n"
                            "        color=Colors.grey,\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AppBar forceMaterialTransparency & clipBehavior",
                    description=(
                        "forceMaterialTransparency=True removes the AppBar "
                        "background material, making it fully transparent. "
                        "clipBehavior controls how the AppBar clips its content."
                    ),
                    instruction=(
                        "Observe the transparent AppBar over the green background. "
                        "The title floats without any AppBar surface behind it."
                    ),
                    visible=Container(
                        height=140.0,
                        color=Color(0xFFA5D6A7),
                        child=Scaffold(
                            backgroundColor=Color(0xFFA5D6A7),
                            appBar=AppBar(
                                title=Text(
                                    "Transparent AppBar",
                                    style=TextStyle(color=Colors.black),
                                ),
                                forceMaterialTransparency=True,
                                clipBehavior=Clip.antiAlias,
                            ),
                            body=Center(
                                child=Text(
                                    "Green background shows through",
                                    style=TextStyle(fontSize=14),
                                ),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AppBar(\n"
                            "    title=Text('Transparent'),\n"
                            "    forceMaterialTransparency=True,\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Drawer shadowColor & shape",
                    description=(
                        "Drawer supports shadowColor, shape, surfaceTintColor, "
                        "and clipBehavior for visual customization. Use "
                        "RoundedRectangleBorder for rounded drawer edges."
                    ),
                    instruction=(
                        "Tap the hamburger menu icon in the AppBar to open the "
                        "drawer. Observe the purple shadow, rounded corners, "
                        "and green surface tint."
                    ),
                    visible=_DrawerShapeDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Drawer(\n"
                            "    shadowColor=Colors.purple,\n"
                            "    shape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(24),\n"
                            "    ),\n"
                            "    surfaceTintColor=Colors.green,\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            "    child=Text('Drawer content'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Drawer semanticLabel",
                    description=(
                        "semanticLabel provides an accessibility label for "
                        "screen readers. It does not affect visual appearance "
                        "but improves accessibility for assistive technologies."
                    ),
                    instruction=(
                        "This property is for accessibility. Screen readers "
                        "will announce the specified label when the drawer is opened."
                    ),
                    visible=Container(
                        padding=EdgeInsets.all(16),
                        decoration=BoxDecoration(
                            color=Color(0xFFF3E5F5),
                            borderRadius=BorderRadius.circular(8),
                        ),
                        child=Column(
                            crossAxisAlignment=CrossAxisAlignment.start,
                            children=[
                                Text(
                                    "Accessibility property",
                                    style=TextStyle(
                                        fontSize=14,
                                        fontWeight=FontWeight.bold,
                                        color=Colors.deepPurple,
                                    ),
                                ),
                                SizedBox(height=8),
                                Text(
                                    'semanticLabel="Main navigation drawer"',
                                    style=TextStyle(fontSize=13, color=Colors.grey),
                                ),
                                SizedBox(height=4),
                                Text(
                                    "Screen readers announce this label when the drawer opens.",
                                    style=TextStyle(fontSize=12),
                                ),
                            ],
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Drawer(\n"
                            "    semanticLabel='Main navigation drawer',\n"
                            "    child=ListView(\n"
                            "        children=[\n"
                            "            ListTile(title=Text('Home')),\n"
                            "            ListTile(title=Text('Settings')),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationBar animationDuration",
                    description=(
                        "animationDuration controls how long the indicator "
                        "animation takes when switching destinations. "
                        "Set to Duration(seconds=2) for a slow, visible transition."
                    ),
                    instruction=(
                        "Tap each destination and watch the indicator "
                        "animate slowly over 2 seconds to the new position."
                    ),
                    visible=_NavBarAnimDurationDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    animationDuration=Duration(seconds=2),\n"
                            "    destinations=[\n"
                            "        NavigationDestination(\n"
                            "            icon=Icon(Icons.home),\n"
                            "            label='Home',\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationBar shadowColor & surfaceTintColor",
                    description=(
                        "shadowColor sets the shadow color beneath the bar. "
                        "surfaceTintColor tints the NavigationBar surface. "
                        "Requires elevation to see the shadow."
                    ),
                    instruction=(
                        "Observe the amber-tinted surface and the red shadow "
                        "beneath the NavigationBar. Tap destinations to interact."
                    ),
                    visible=_NavBarShadowSurfaceDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    shadowColor=Colors.red,\n"
                            "    surfaceTintColor=Colors.amber,\n"
                            "    elevation=8.0,\n"
                            "    destinations=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationBar indicatorShape & overlayColor",
                    description=(
                        "indicatorShape replaces the default pill shape with a "
                        "custom shape (e.g. RoundedRectangleBorder for square). "
                        "overlayColor sets the splash/ripple color on tap."
                    ),
                    instruction=(
                        "Tap each destination. Notice the square-ish indicator "
                        "shape and the red ripple overlay on tap."
                    ),
                    visible=_NavBarIndicatorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    indicatorShape=RoundedRectangleBorder(\n"
                            "        borderRadius=BorderRadius.circular(4),\n"
                            "    ),\n"
                            "    overlayColor=WidgetStatePropertyAll(\n"
                            "        Color(0x1AF44336),\n"
                            "    ),\n"
                            "    destinations=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="NavigationBar labelTextStyle & labelPadding",
                    description=(
                        "labelTextStyle customizes the text style of destination "
                        "labels. labelPadding adds padding around each label. "
                        "Both accept WidgetStatePropertyAll for uniform styling."
                    ),
                    instruction=(
                        "Observe the bold, large, deep-purple labels with extra "
                        "top padding. Tap destinations to interact."
                    ),
                    visible=_NavBarLabelStyleDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "NavigationBar(\n"
                            "    selectedIndex=index,\n"
                            "    onDestinationSelected=on_changed,\n"
                            "    labelTextStyle=WidgetStatePropertyAll(\n"
                            "        TextStyle(\n"
                            "            fontSize=16,\n"
                            "            fontWeight=FontWeight.bold,\n"
                            "            color=Colors.deepPurple,\n"
                            "        ),\n"
                            "    ),\n"
                            "    labelPadding=EdgeInsets.only(top=8),\n"
                            "    destinations=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TabBarView physics & viewportFraction",
                    description=(
                        "viewportFraction < 1.0 lets adjacent tabs peek in from "
                        "the sides. physics=BouncingScrollPhysics adds iOS-style "
                        "bouncing. clipBehavior=Clip.none prevents clipping."
                    ),
                    instruction=(
                        "Swipe between tabs. Notice the adjacent tab edges are "
                        "visible (viewportFraction=0.8) and the bouncing overscroll."
                    ),
                    visible=_TabBarViewPhysicsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TabBarView(\n"
                            "    viewportFraction=0.8,\n"
                            "    physics=BouncingScrollPhysics(),\n"
                            "    clipBehavior=Clip.none,\n"
                            "    children=[\n"
                            "        Container(color=Colors.red, child=Text('A')),\n"
                            "        Container(color=Colors.green, child=Text('B')),\n"
                            "        Container(color=Colors.blue, child=Text('C')),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
