import ast
import asyncio
import inspect
import os
import sys
import textwrap
from functools import lru_cache

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from flut import run_app_async
from flut.dart import Color
from flut.flutter.foundation import ValueKey, ValueNotifier
from flut.flutter.widgets import (
    StatefulWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Expanded,
    GestureDetector,
    Padding,
    Icon,
    SingleChildScrollView,
    WidgetState,
    WidgetStateColor,
    PlatformMenuBar,
    PlatformMenu,
    PlatformMenuItem,
    PlatformMenuItemGroup,
    PlatformProvidedMenuItem,
    PlatformProvidedMenuItemType,
    SingleActivator,
    TextEditingController,
)
from flut.flutter.rendering import CrossAxisAlignment, BoxConstraints
from flut.flutter.material import (
    MaterialApp,
    Scaffold,
    AppBar,
    Colors,
    ThemeData,
    ColorScheme,
    Icons,
    InkRipple,
    Switch,
    TextField,
    InputDecoration,
)
from flut.dart import Brightness
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    Border,
    BorderSide,
    BorderRadius,
)
from flut.flutter.services.keyboard_key import LogicalKeyboardKey
from widgets import CatalogPage
from widgets.catalog_page import TileFilter
from pages import (
    PythonPage,
    ButtonPage,
    AnimationPage,
    GesturePage,
    AsyncPage,
    ListViewPage,
    TypographyPage,
    CanvasPage,
    NavigationPage,
    ChatboxPage,
    WidgetPage,
    FormPage,
    LayoutPage,
    AssetPage,
    ReproPage,
    FocusPage,
    StressPage,
    ShortcutsPage,
    DialogPage,
    MenuPage,
    SliderPage,
    SelectionPage,
    IconPage,
    ThemePage,
    ListenablePage,
)

PAGES = [
    ("Python", Icons.highlight, PythonPage),
    ("Chatbox", Icons.chat, ChatboxPage),
    ("Layout", Icons.dashboard, LayoutPage),
    ("Widget", Icons.widgets, WidgetPage),
    ("Form", Icons.assignment, FormPage),
    ("Theme", Icons.palette, ThemePage),
    ("Typography", Icons.text_format, TypographyPage),
    ("Button", Icons.smart_button, ButtonPage),
    ("ListView", Icons.list, ListViewPage),
    ("Selection", Icons.check_circle, SelectionPage),
    ("Slider", Icons.tune, SliderPage),
    ("Icon", Icons.emoji_symbols, IconPage),
    ("Menu", Icons.menu, MenuPage),
    ("Dialog", Icons.open_in_new, DialogPage),
    ("Navigation", Icons.navigation, NavigationPage),
    ("Gesture", Icons.open_with, GesturePage),
    ("Animation", Icons.animation, AnimationPage),
    ("Listenable", Icons.notifications_active, ListenablePage),
    ("Canvas", Icons.brush, CanvasPage),
    ("Asset", Icons.image, AssetPage),
    ("Focus", Icons.keyboard, FocusPage),
    ("Shortcut", Icons.keyboard_alt, ShortcutsPage),
    ("Async", Icons.schedule, AsyncPage),
    ("Stress", Icons.stream, StressPage),
    ("Issue Repro", Icons.bug_report, ReproPage),
]


_catalog_engine_probe = None


def _extract_tile_title(node):
    if not isinstance(node, ast.Call):
        return None

    for keyword in node.keywords:
        if keyword.arg != "title":
            continue
        try:
            value = ast.literal_eval(keyword.value)
        except Exception:
            return None
        return value if isinstance(value, str) else None

    return None


@lru_cache(maxsize=None)
def _page_tile_titles(page_cls):
    if issubclass(page_cls, StatefulWidget):
        build_fn = page_cls().createState().build
    else:
        build_fn = page_cls.build

    try:
        source = textwrap.dedent(inspect.getsource(build_fn))
    except (OSError, TypeError):
        return ()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ()

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "CatalogPage":
            continue

        for keyword in node.keywords:
            if keyword.arg != "children":
                continue
            if not isinstance(keyword.value, (ast.List, ast.Tuple)):
                return ()
            return tuple(_extract_tile_title(child) for child in keyword.value.elts)

    return ()


def _page_filter_match_count(page_cls, filter_text):
    needle = filter_text.strip().lower()
    if not needle:
        return None

    return sum(
        1 for title in _page_tile_titles(page_cls) if title and needle in title.lower()
    )


class CatalogApp(StatefulWidget):
    def createState(self):
        return CatalogAppState()


class CatalogAppState(State[CatalogApp]):

    def initState(self):
        try:
            _catalog_engine_probe.value = _catalog_engine_probe.value + 1
            assert (
                _catalog_engine_probe.value == 2
            ), f"probe value {_catalog_engine_probe.value!r} != 2"
        except Exception as e:
            print(f"[catalog] error: initState ran before on_initialized: {e!r}")

        self.selected_index = 0
        self.is_dark = False
        self.filter_text = ""
        self.filter_controller = TextEditingController(text="")

    def _select(self, index):
        self.setState(lambda: setattr(self, "selected_index", index))

    def _toggle_brightness(self, value):
        self.setState(lambda: setattr(self, "is_dark", value))

    def _on_filter_changed(self, value):
        TileFilter.text = value
        self.setState(lambda: setattr(self, "filter_text", value))

    def build(self, context):
        nav_items = []
        filter_active = bool(self.filter_text.strip())
        badge_background = Color(0xFF4A4A4A) if self.is_dark else Color(0xFFE0E0E0)
        badge_foreground = Color(0xFFF5F5F5) if self.is_dark else Color(0xFF616161)
        for i, (label, icon, page_cls) in enumerate(PAGES):
            is_selected = i == self.selected_index
            match_count = _page_filter_match_count(page_cls, self.filter_text)
            row_children = [
                Icon(
                    icon,
                    color=Colors.blue if is_selected else Colors.grey,
                ),
                SizedBox(width=12),
                Expanded(
                    child=Text(
                        label,
                        style=TextStyle(
                            fontSize=14,
                            fontWeight=(
                                FontWeight.bold if is_selected else FontWeight.normal
                            ),
                            color=Colors.blue if is_selected else None,
                        ),
                    ),
                ),
            ]
            if filter_active:
                row_children.append(
                    Container(
                        padding=EdgeInsets.symmetric(
                            horizontal=10,
                            vertical=3,
                        ),
                        decoration=BoxDecoration(
                            color=badge_background,
                            borderRadius=BorderRadius.circular(999),
                        ),
                        child=Text(
                            str(match_count),
                            style=TextStyle(
                                fontSize=12,
                                fontWeight=FontWeight.bold,
                                color=badge_foreground,
                            ),
                        ),
                    )
                )
            nav_items.append(
                GestureDetector(
                    onTap=lambda idx=i: self._select(idx),
                    child=Container(
                        padding=EdgeInsets.symmetric(horizontal=16, vertical=12),
                        color=Color(0x1A2196F3) if is_selected else Colors.transparent,
                        child=Row(
                            children=row_children,
                        ),
                    ),
                )
            )

        _, _, page_cls = PAGES[self.selected_index]
        page = page_cls(key=ValueKey(f"page_{self.selected_index}"))

        brightness = Brightness.dark if self.is_dark else Brightness.light

        return PlatformMenuBar(
            menus=[
                PlatformMenu(
                    label="File",
                    menus=[
                        PlatformMenuItem(
                            label="New",
                            shortcut=SingleActivator(
                                LogicalKeyboardKey.keyN, control=True
                            ),
                        ),
                        PlatformMenuItem(
                            label="Open",
                            shortcut=SingleActivator(
                                LogicalKeyboardKey.keyO, control=True
                            ),
                        ),
                        PlatformMenuItemGroup(
                            members=[
                                PlatformMenuItem(
                                    label="Quit",
                                    onSelected=lambda: print("Quit selected"),
                                    shortcut=SingleActivator(
                                        LogicalKeyboardKey.keyQ, control=True
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                PlatformMenu(
                    label="View",
                    menus=[
                        PlatformMenuItem(
                            label="Toggle Dark Mode",
                            onSelected=lambda: self._toggle_brightness(
                                not self.is_dark
                            ),
                        ),
                    ],
                ),
            ],
            child=MaterialApp(
                title="Flut Catalog",
                theme=ThemeData(
                    colorScheme=ColorScheme.fromSeed(
                        seedColor=Colors.blue, brightness=brightness
                    ),
                    splashFactory=InkRipple.splashFactory(),
                    useMaterial3=True,
                ),
                home=Scaffold(
                    appBar=AppBar(
                        title=Text("Flut Catalog"),
                        actions=[
                            Row(
                                children=[
                                    Container(
                                        width=200.0,
                                        height=32.0,
                                        child=TextField(
                                            controller=self.filter_controller,
                                            onChanged=self._on_filter_changed,
                                            decoration=InputDecoration(
                                                hintText="Filter tiles...",
                                                prefixIcon=Icon(
                                                    Icons.search, size=18.0
                                                ),
                                                prefixIconConstraints=BoxConstraints(
                                                    minWidth=32.0, minHeight=0.0
                                                ),
                                                contentPadding=EdgeInsets.symmetric(
                                                    horizontal=8, vertical=8
                                                ),
                                                isCollapsed=True,
                                                isDense=True,
                                                border=None,
                                            ),
                                            style=TextStyle(fontSize=14),
                                        ),
                                    ),
                                    SizedBox(width=12),
                                    Icon(
                                        Icons.light_mode,
                                        color=(
                                            Colors.orange
                                            if not self.is_dark
                                            else Colors.grey
                                        ),
                                    ),
                                    Switch(
                                        value=self.is_dark,
                                        onChanged=self._toggle_brightness,
                                    ),
                                    Icon(
                                        Icons.dark_mode,
                                        color=(
                                            Colors.indigo
                                            if self.is_dark
                                            else Colors.grey
                                        ),
                                    ),
                                    SizedBox(width=8),
                                ],
                            ),
                        ],
                    ),
                    body=Row(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            Container(
                                width=220.0,
                                decoration=BoxDecoration(
                                    border=Border(
                                        right=BorderSide(color=Color(0xFFE0E0E0)),
                                    ),
                                ),
                                child=Column(
                                    crossAxisAlignment=CrossAxisAlignment.stretch,
                                    children=[
                                        Padding(
                                            padding=EdgeInsets.all(16),
                                            child=Text(
                                                "Demos",
                                                style=TextStyle(
                                                    fontSize=12,
                                                    fontWeight=FontWeight.bold,
                                                    color=Colors.grey,
                                                ),
                                            ),
                                        ),
                                        Expanded(
                                            child=SingleChildScrollView(
                                                child=Column(
                                                    crossAxisAlignment=CrossAxisAlignment.stretch,
                                                    children=nav_items,
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            Expanded(child=page),
                        ],
                    ),
                ),
            ),
        )


async def _on_catalog_initialized():
    global _catalog_engine_probe
    print("Catalog event: on_initialized")
    try:
        _catalog_engine_probe = ValueNotifier(0)
        _catalog_engine_probe.value = _catalog_engine_probe.value + 1
        assert (
            _catalog_engine_probe.value == 1
        ), f"probe value {_catalog_engine_probe.value!r} != 1"
    except Exception as e:
        print(f"[catalog] error: engine not ready in on_initialized: {e!r}")


async def _on_catalog_close():
    print("Catalog event: on_close")
    try:
        _catalog_engine_probe.value = _catalog_engine_probe.value + 1
        assert (
            _catalog_engine_probe.value == 3
        ), f"probe value {_catalog_engine_probe.value!r} != 3"
    except Exception as e:
        print(f"[catalog] error: engine not alive in on_close: {e!r}")


async def main():
    await run_app_async(
        CatalogApp(),
        width=1000,
        height=700,
        title="Flut Catalog",
        on_initialized=_on_catalog_initialized,
        on_close=_on_catalog_close,
    )


asyncio.run(main())
