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
    Icon,
    SingleActivator,
    Padding,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import CrossAxisAlignment, BoxConstraints
from flut.flutter.material import (
    Colors,
    Icons,
    MenuBar,
    MenuAnchor,
    MenuItemButton,
    SubmenuButton,
    MenuAcceleratorLabel,
    ElevatedButton,
    Theme,
    PopupMenuItem,
    PopupMenuButton,
    PopupMenuDivider,
    PopupMenuPosition,
    DropdownMenu,
    DropdownMenuEntry,
    DropdownMenuCloseBehavior,
    DropdownButton,
    DropdownMenuItem,
    showMenu,
)
from flut.flutter.rendering.stack import RelativeRect
from flut.flutter.widgets.raw_menu_anchor import MenuController
from flut.flutter.services.keyboard_key import LogicalKeyboardKey
from flut.flutter.painting import (
    BorderRadius,
    BoxDecoration,
    EdgeInsets,
    RoundedRectangleBorder,
    TextStyle,
)
from flut.dart import Color
from flut.dart.ui import Clip, FontStyle, FontWeight, Offset
from flut.flutter.services import SystemMouseCursors
from flut.flutter.animation import AnimationStyle
from utils import CODE_FONT_FAMILY
from widgets import CatalogPage, SplitViewTile, CodeArea


class _MenuBarDemo(StatefulWidget):
    def createState(self):
        return _MenuBarDemoState()


class _MenuBarDemoState(State[_MenuBarDemo]):
    def initState(self):
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-6:]
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                MenuBar(
                    children=[
                        SubmenuButton(
                            menuChildren=[
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("New"),
                                    leadingIcon=Icon(Icons.add),
                                    child=MenuAcceleratorLabel("&New"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Open"),
                                    leadingIcon=Icon(Icons.folder_open),
                                    child=MenuAcceleratorLabel("&Open"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Save"),
                                    leadingIcon=Icon(Icons.save),
                                    shortcut=SingleActivator(
                                        LogicalKeyboardKey.keyS, control=True
                                    ),
                                    child=MenuAcceleratorLabel("&Save"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Close"),
                                    child=MenuAcceleratorLabel("&Close"),
                                ),
                            ],
                            child=MenuAcceleratorLabel("&File"),
                        ),
                        SubmenuButton(
                            menuChildren=[
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Cut"),
                                    leadingIcon=Icon(Icons.content_cut),
                                    shortcut=SingleActivator(
                                        LogicalKeyboardKey.keyX, control=True
                                    ),
                                    child=MenuAcceleratorLabel("Cu&t"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Copy"),
                                    leadingIcon=Icon(Icons.content_copy),
                                    shortcut=SingleActivator(
                                        LogicalKeyboardKey.keyC, control=True
                                    ),
                                    child=MenuAcceleratorLabel("&Copy"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Paste"),
                                    leadingIcon=Icon(Icons.content_paste),
                                    shortcut=SingleActivator(
                                        LogicalKeyboardKey.keyV, control=True
                                    ),
                                    child=MenuAcceleratorLabel("&Paste"),
                                ),
                            ],
                            child=MenuAcceleratorLabel("&Edit"),
                        ),
                        SubmenuButton(
                            menuChildren=[
                                SubmenuButton(
                                    menuChildren=[
                                        MenuItemButton(
                                            onPressed=lambda: self._add_log("Zoom In"),
                                            child=Text("Zoom In"),
                                            shortcut=SingleActivator(
                                                LogicalKeyboardKey.equal, control=True
                                            ),
                                        ),
                                        MenuItemButton(
                                            onPressed=lambda: self._add_log("Zoom Out"),
                                            child=Text("Zoom Out"),
                                            shortcut=SingleActivator(
                                                LogicalKeyboardKey.minus, control=True
                                            ),
                                        ),
                                    ],
                                    child=Text("Zoom"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Full Screen"),
                                    child=Text("Full Screen"),
                                ),
                            ],
                            child=MenuAcceleratorLabel("&View"),
                        ),
                    ],
                ),
                SizedBox(height=16),
                Text("Action Log:", style=TextStyle(fontWeight=FontWeight.bold)),
                SizedBox(height=4),
                *[Text(line, style=TextStyle(fontSize=13)) for line in self.log_lines],
            ],
        )


class _MenuAnchorDemo(StatefulWidget):
    def createState(self):
        return _MenuAnchorDemoState()


class _MenuAnchorDemoState(State[_MenuAnchorDemo]):
    def initState(self):
        self.selected = "None"
        self.controller = MenuController()

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                MenuAnchor(
                    controller=self.controller,
                    menuChildren=[
                        MenuItemButton(
                            onPressed=lambda: self._select("Option A"),
                            child=Text("Option A"),
                        ),
                        MenuItemButton(
                            onPressed=lambda: self._select("Option B"),
                            child=Text("Option B"),
                        ),
                        MenuItemButton(
                            onPressed=lambda: self._select("Option C"),
                            child=Text("Option C"),
                        ),
                    ],
                    child=ElevatedButton(
                        onPressed=lambda: self.controller.open(),
                        child=Text("Open Menu"),
                    ),
                ),
                SizedBox(height=12),
                Text(f"Selected: {self.selected}"),
            ],
        )

    def _select(self, value):
        self.selected = value
        self.setState(lambda: None)


class _DisabledMenuItemDemo(StatefulWidget):
    def createState(self):
        return _DisabledMenuItemDemoState()


class _DisabledMenuItemDemoState(State[_DisabledMenuItemDemo]):
    def initState(self):
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-4:]
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                MenuBar(
                    children=[
                        SubmenuButton(
                            menuChildren=[
                                MenuItemButton(
                                    onPressed=lambda: self._add_log(
                                        "Enabled item clicked"
                                    ),
                                    leadingIcon=Icon(Icons.check),
                                    child=Text("Enabled Item"),
                                ),
                                MenuItemButton(
                                    onPressed=None,
                                    leadingIcon=Icon(Icons.block),
                                    child=Text("Disabled Item"),
                                ),
                                MenuItemButton(
                                    onPressed=lambda: self._add_log("Another enabled"),
                                    child=Text("Another Enabled"),
                                ),
                            ],
                            child=Text("Actions"),
                        ),
                    ],
                ),
                SizedBox(height=8),
                *[Text(line, style=TextStyle(fontSize=13)) for line in self.log_lines],
            ],
        )


class _PopupMenuDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuDemoState()


class _PopupMenuDemoState(State[_PopupMenuDemo]):
    def initState(self):
        self.popup_selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda context: [
                        PopupMenuItem(value="copy", child=Text("Copy")),
                        PopupMenuItem(value="paste", child=Text("Paste")),
                        PopupMenuItem(value="delete", child=Text("Delete")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "popup_selection", v)
                    ),
                    tooltip="Show menu",
                    icon=Icon(Icons.more_vert),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.popup_selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuDividerDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuDividerDemoState()


class _PopupMenuDividerDemoState(State[_PopupMenuDividerDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda context: [
                        PopupMenuItem(value="cut", child=Text("Cut")),
                        PopupMenuItem(value="copy", child=Text("Copy")),
                        PopupMenuItem(value="paste", child=Text("Paste")),
                        PopupMenuDivider(),
                        PopupMenuItem(value="delete", child=Text("Delete")),
                        PopupMenuDivider(
                            height=24,
                            thickness=2,
                            indent=16,
                            endIndent=16,
                            color=Colors.red,
                        ),
                        PopupMenuItem(value="report", child=Text("Report")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    tooltip="Show menu with dividers",
                    icon=Icon(Icons.more_vert),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuPositionDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuPositionDemoState()


class _PopupMenuPositionDemoState(State[_PopupMenuPositionDemo]):
    def initState(self):
        self.over_selection = "None"
        self.under_selection = "None"

    def build(self, context):
        items = lambda ctx: [
            PopupMenuItem(value="cut", child=Text("Cut")),
            PopupMenuItem(value="copy", child=Text("Copy")),
            PopupMenuItem(value="paste", child=Text("Paste")),
        ]
        return Row(
            children=[
                Column(
                    children=[
                        Text(
                            "over",
                            style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                        ),
                        PopupMenuButton(
                            itemBuilder=items,
                            position=PopupMenuPosition.over,
                            onSelected=lambda v: self.setState(
                                lambda: setattr(self, "over_selection", v)
                            ),
                            child=Container(
                                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                                decoration=BoxDecoration(
                                    color=Color(0xFFE3F2FD),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Text("Open Menu"),
                            ),
                        ),
                        SizedBox(height=4),
                        Text(
                            f"Selected: {self.over_selection}",
                            style=TextStyle(fontSize=11, color=Colors.grey),
                        ),
                    ],
                ),
                SizedBox(width=32),
                Column(
                    children=[
                        Text(
                            "under",
                            style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                        ),
                        PopupMenuButton(
                            itemBuilder=items,
                            position=PopupMenuPosition.under,
                            onSelected=lambda v: self.setState(
                                lambda: setattr(self, "under_selection", v)
                            ),
                            child=Container(
                                padding=EdgeInsets.symmetric(horizontal=16, vertical=8),
                                decoration=BoxDecoration(
                                    color=Color(0xFFFCE4EC),
                                    borderRadius=BorderRadius.circular(8),
                                ),
                                child=Text("Open Menu"),
                            ),
                        ),
                        SizedBox(height=4),
                        Text(
                            f"Selected: {self.under_selection}",
                            style=TextStyle(fontSize=11, color=Colors.grey),
                        ),
                    ],
                ),
            ],
        )


class _MenuControllerDemo(StatefulWidget):
    def createState(self):
        return _MenuControllerDemoState()


class _MenuControllerDemoState(State[_MenuControllerDemo]):
    def initState(self):
        self.menu_controller = MenuController()
        self.selected = "Red"

    def _open_menu(self):
        self.menu_controller.open()
        self.setState(lambda: None)

    def _close_menu(self):
        self.menu_controller.close()
        self.setState(lambda: None)

    def _on_selected(self, value):
        self.selected = value
        self.setState(lambda: None)

    def build(self, context):
        is_open = self.menu_controller.isOpen
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._open_menu,
                            child=Text("open()"),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._close_menu,
                            child=Text("close()"),
                        ),
                        SizedBox(width=12),
                        Container(
                            padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                            decoration=BoxDecoration(
                                color=(
                                    Color(0xFFE8F5E9) if is_open else Color(0xFFFCE4EC)
                                ),
                                borderRadius=BorderRadius.circular(4),
                            ),
                            child=Text(
                                f"isOpen: {is_open}",
                                style=TextStyle(
                                    fontSize=12, fontFamily=CODE_FONT_FAMILY
                                ),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                DropdownMenu(
                    menuController=self.menu_controller,
                    initialSelection=self.selected,
                    onSelected=self._on_selected,
                    label=Text("Color"),
                    dropdownMenuEntries=[
                        DropdownMenuEntry(value="Red", label="Red"),
                        DropdownMenuEntry(value="Green", label="Green"),
                        DropdownMenuEntry(value="Blue", label="Blue"),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {self.selected}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _PopupMenuStyleDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuStyleDemoState()


class _PopupMenuStyleDemoState(State[_PopupMenuStyleDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(
                            value="italic",
                            child=Text("Italic item"),
                            labelTextStyle=WidgetStatePropertyAll(
                                TextStyle(fontStyle=FontStyle.italic),
                            ),
                            mouseCursor=SystemMouseCursors.cell,
                        ),
                        PopupMenuItem(
                            value="bold",
                            child=Text("Bold item"),
                            labelTextStyle=WidgetStatePropertyAll(
                                TextStyle(fontWeight=FontWeight.bold),
                            ),
                            mouseCursor=SystemMouseCursors.cell,
                        ),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    icon=Icon(Icons.style),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuShadowDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuShadowDemoState()


class _PopupMenuShadowDemoState(State[_PopupMenuShadowDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(value="a", child=Text("Option A")),
                        PopupMenuItem(value="b", child=Text("Option B")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    shadowColor=Colors.red,
                    surfaceTintColor=Colors.amber,
                    icon=Icon(Icons.more_horiz),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuRoundedDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuRoundedDemoState()


class _PopupMenuRoundedDemoState(State[_PopupMenuRoundedDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(value="x", child=Text("Choice X")),
                        PopupMenuItem(value="y", child=Text("Choice Y")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    borderRadius=BorderRadius.circular(16),
                    shape=RoundedRectangleBorder(
                        borderRadius=BorderRadius.circular(16),
                    ),
                    icon=Icon(Icons.rounded_corner),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuPaddingDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuPaddingDemoState()


class _PopupMenuPaddingDemoState(State[_PopupMenuPaddingDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(value="one", child=Text("Item One")),
                        PopupMenuItem(value="two", child=Text("Item Two")),
                        PopupMenuItem(value="three", child=Text("Item Three")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    menuPadding=EdgeInsets.all(16),
                    constraints=BoxConstraints(minWidth=250),
                    offset=Offset(0, 40),
                    icon=Icon(Icons.menu),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuClipDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuClipDemoState()


class _PopupMenuClipDemoState(State[_PopupMenuClipDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(value="clip1", child=Text("Clipped A")),
                        PopupMenuItem(value="clip2", child=Text("Clipped B")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    clipBehavior=Clip.antiAlias,
                    enableFeedback=False,
                    icon=Icon(Icons.content_cut),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuNoAnimDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuNoAnimDemoState()


class _PopupMenuNoAnimDemoState(State[_PopupMenuNoAnimDemo]):
    def initState(self):
        self.selection = "None"

    def build(self, context):
        return Row(
            children=[
                PopupMenuButton(
                    itemBuilder=lambda ctx: [
                        PopupMenuItem(value="instant1", child=Text("Instant A")),
                        PopupMenuItem(value="instant2", child=Text("Instant B")),
                    ],
                    onSelected=lambda v: self.setState(
                        lambda: setattr(self, "selection", v)
                    ),
                    popUpAnimationStyle=AnimationStyle.noAnimation,
                    icon=Icon(Icons.flash_on),
                ),
                SizedBox(width=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13),
                ),
            ],
        )


class _PopupMenuVariantsDemo(StatefulWidget):
    def createState(self):
        return _PopupMenuVariantsDemoState()


class _PopupMenuVariantsDemoState(State[_PopupMenuVariantsDemo]):
    def initState(self):
        self.variant = "basic"
        self.selection = "None"

    def _select_variant(self, variant):
        self.variant = variant
        self.setState(lambda: None)

    def _build_items(self):
        if self.variant == "style":
            return [
                PopupMenuItem(
                    value="italic",
                    child=Text("Italic item"),
                    labelTextStyle=WidgetStatePropertyAll(
                        TextStyle(fontStyle=FontStyle.italic),
                    ),
                    mouseCursor=SystemMouseCursors.cell,
                ),
                PopupMenuItem(
                    value="bold",
                    child=Text("Bold item"),
                    labelTextStyle=WidgetStatePropertyAll(
                        TextStyle(fontWeight=FontWeight.bold),
                    ),
                    mouseCursor=SystemMouseCursors.cell,
                ),
            ]
        if self.variant == "shadow":
            return [
                PopupMenuItem(value="a", child=Text("Option A")),
                PopupMenuItem(value="b", child=Text("Option B")),
            ]
        if self.variant == "rounded":
            return [
                PopupMenuItem(value="x", child=Text("Choice X")),
                PopupMenuItem(value="y", child=Text("Choice Y")),
            ]
        if self.variant == "layout":
            return [
                PopupMenuItem(value="one", child=Text("Item One")),
                PopupMenuItem(value="two", child=Text("Item Two")),
                PopupMenuItem(value="three", child=Text("Item Three")),
            ]
        if self.variant == "clip":
            return [
                PopupMenuItem(value="clip1", child=Text("Clipped A")),
                PopupMenuItem(value="clip2", child=Text("Clipped B")),
            ]
        if self.variant == "animation":
            return [
                PopupMenuItem(value="instant1", child=Text("Instant A")),
                PopupMenuItem(value="instant2", child=Text("Instant B")),
            ]
        return [
            PopupMenuItem(value="copy", child=Text("Copy")),
            PopupMenuItem(value="paste", child=Text("Paste")),
            PopupMenuItem(value="delete", child=Text("Delete")),
        ]

    def _build_button(self, icon_map):
        kwargs = {
            "itemBuilder": lambda ctx: self._build_items(),
            "onSelected": lambda v: self.setState(
                lambda: setattr(self, "selection", v)
            ),
            "tooltip": "Show menu",
            "icon": Icon(icon_map[self.variant]),
            "enableFeedback": False if self.variant == "clip" else True,
        }

        if self.variant == "shadow":
            kwargs["shadowColor"] = Colors.red
            kwargs["surfaceTintColor"] = Colors.amber
        elif self.variant == "rounded":
            kwargs["borderRadius"] = BorderRadius.circular(16)
            kwargs["shape"] = RoundedRectangleBorder(
                borderRadius=BorderRadius.circular(16),
            )
        elif self.variant == "layout":
            kwargs["menuPadding"] = EdgeInsets.all(16)
            kwargs["constraints"] = BoxConstraints(minWidth=250)
            kwargs["offset"] = Offset(0, 40)
        elif self.variant == "clip":
            kwargs["clipBehavior"] = Clip.antiAlias
        elif self.variant == "animation":
            kwargs["popUpAnimationStyle"] = AnimationStyle.noAnimation

        return PopupMenuButton(**kwargs)

    def build(self, context):
        options = [
            ("basic", "Basic"),
            ("style", "Item Style"),
            ("shadow", "Shadow"),
            ("rounded", "Rounded"),
            ("layout", "Layout"),
            ("clip", "Clip"),
            ("animation", "Animation"),
        ]
        icon_map = {
            "basic": Icons.more_vert,
            "style": Icons.style,
            "shadow": Icons.more_horiz,
            "rounded": Icons.rounded_corner,
            "layout": Icons.menu,
            "clip": Icons.content_cut,
            "animation": Icons.flash_on,
        }
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        (
                            ElevatedButton(
                                onPressed=lambda key=key: self._select_variant(key),
                                child=Text(label),
                            )
                            if self.variant == key
                            else MenuItemButton(
                                onPressed=lambda key=key: self._select_variant(key),
                                child=Text(label),
                            )
                        )
                        for key, label in options
                    ],
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        self._build_button(icon_map),
                        SizedBox(width=12),
                        Text(
                            f"Selected: {self.selection}",
                            style=TextStyle(fontSize=13),
                        ),
                    ],
                ),
            ],
        )


class _DropdownMenuDemo(StatefulWidget):
    def createState(self):
        return _DropdownMenuDemoState()


class _DropdownMenuDemoState(State[_DropdownMenuDemo]):
    def initState(self):
        self.selected_color = "Red"
        self.selected_size = "Medium"

    def _on_color_selected(self, value):
        self.selected_color = value
        self.setState(lambda: None)

    def _on_size_selected(self, value):
        self.selected_size = value
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        DropdownMenu(
                            initialSelection=self.selected_color,
                            onSelected=self._on_color_selected,
                            label=Text("Color"),
                            leadingIcon=Icon(Icons.palette),
                            dropdownMenuEntries=[
                                DropdownMenuEntry(
                                    value="Red",
                                    label="Red",
                                    leadingIcon=Icon(Icons.circle, color=Colors.red),
                                ),
                                DropdownMenuEntry(
                                    value="Green",
                                    label="Green",
                                    leadingIcon=Icon(Icons.circle, color=Colors.green),
                                ),
                                DropdownMenuEntry(
                                    value="Blue",
                                    label="Blue",
                                    leadingIcon=Icon(Icons.circle, color=Colors.blue),
                                ),
                                DropdownMenuEntry(
                                    value="Orange",
                                    label="Orange",
                                    leadingIcon=Icon(Icons.circle, color=Colors.orange),
                                ),
                                DropdownMenuEntry(
                                    value="Purple",
                                    label="Purple",
                                    leadingIcon=Icon(Icons.circle, color=Colors.purple),
                                ),
                            ],
                        ),
                        SizedBox(width=16),
                        DropdownMenu(
                            initialSelection=self.selected_size,
                            onSelected=self._on_size_selected,
                            label=Text("Size"),
                            width=200.0,
                            dropdownMenuEntries=[
                                DropdownMenuEntry(value="Small", label="Small"),
                                DropdownMenuEntry(value="Medium", label="Medium"),
                                DropdownMenuEntry(value="Large", label="Large"),
                                DropdownMenuEntry(
                                    value="Extra Large", label="Extra Large"
                                ),
                            ],
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"Selected: color={self.selected_color}, size={self.selected_size}",
                    style=TextStyle(color=Colors.grey),
                ),
            ],
        )


class _DropdownButtonDemo(StatefulWidget):
    def createState(self):
        return _DropdownButtonDemoState()


class _DropdownButtonDemoState(State[_DropdownButtonDemo]):
    def initState(self):
        self.dropdown_button_value = "Apple"

    def _on_fruit_changed(self, value):
        self.dropdown_button_value = value
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    padding=EdgeInsets.symmetric(horizontal=12),
                    decoration=BoxDecoration(
                        borderRadius=BorderRadius.circular(8),
                    ),
                    child=DropdownButton(
                        value=self.dropdown_button_value,
                        onChanged=self._on_fruit_changed,
                        items=[
                            DropdownMenuItem(value="Apple", child=Text("Apple")),
                            DropdownMenuItem(value="Banana", child=Text("Banana")),
                            DropdownMenuItem(value="Cherry", child=Text("Cherry")),
                            DropdownMenuItem(value="Date", child=Text("Date")),
                            DropdownMenuItem(
                                value="Elderberry", child=Text("Elderberry")
                            ),
                        ],
                        isExpanded=True,
                        icon=Icon(Icons.arrow_drop_down),
                    ),
                ),
                SizedBox(height=8),
                Text(
                    f"Selected fruit: {self.dropdown_button_value}",
                    style=TextStyle(color=Colors.grey),
                ),
            ],
        )


class _DropdownMenuCloseBehaviorDemo(StatefulWidget):
    def createState(self):
        return _DropdownMenuCloseBehaviorDemoState()


class _DropdownMenuCloseBehaviorDemoState(State[_DropdownMenuCloseBehaviorDemo]):
    def initState(self):
        self.all_value = "Red"
        self.self_value = "Red"
        self.none_value = "Red"

    def build(self, context):
        entries = [
            DropdownMenuEntry(value="Red", label="Red"),
            DropdownMenuEntry(value="Green", label="Green"),
            DropdownMenuEntry(value="Blue", label="Blue"),
        ]
        return Row(
            children=[
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            "all",
                            style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=4),
                        DropdownMenu(
                            initialSelection=self.all_value,
                            onSelected=lambda v: self.setState(
                                lambda: setattr(self, "all_value", v)
                            ),
                            closeBehavior=DropdownMenuCloseBehavior.all,
                            dropdownMenuEntries=entries,
                            width=130.0,
                        ),
                    ],
                ),
                SizedBox(width=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            "self",
                            style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=4),
                        DropdownMenu(
                            initialSelection=self.self_value,
                            onSelected=lambda v: self.setState(
                                lambda: setattr(self, "self_value", v)
                            ),
                            closeBehavior=getattr(DropdownMenuCloseBehavior, "self"),
                            dropdownMenuEntries=entries,
                            width=130.0,
                        ),
                    ],
                ),
                SizedBox(width=12),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        Text(
                            "none",
                            style=TextStyle(fontSize=12, fontWeight=FontWeight.bold),
                        ),
                        SizedBox(height=4),
                        DropdownMenu(
                            initialSelection=self.none_value,
                            onSelected=lambda v: self.setState(
                                lambda: setattr(self, "none_value", v)
                            ),
                            closeBehavior=DropdownMenuCloseBehavior.none,
                            dropdownMenuEntries=entries,
                            width=130.0,
                        ),
                    ],
                ),
            ],
        )


class _DropdownSelectedItemBuilderDemo(StatefulWidget):
    def createState(self):
        return _DropdownSelectedItemBuilderDemoState()


class _DropdownSelectedItemBuilderDemoState(State[_DropdownSelectedItemBuilderDemo]):
    def initState(self):
        self.value = "Strawberry"
        self.fruits = ["Strawberry", "Blueberry", "Watermelon", "Pineapple"]

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                DropdownButton(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    items=[
                        DropdownMenuItem(value=f, child=Text(f)) for f in self.fruits
                    ],
                    selectedItemBuilder=lambda ctx: [
                        Text(f[:3] + "...") for f in self.fruits
                    ],
                    isExpanded=True,
                ),
                SizedBox(height=4),
                Text(
                    f"Full: {self.value}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _DropdownItemHeightDemo(StatefulWidget):
    def createState(self):
        return _DropdownItemHeightDemoState()


class _DropdownItemHeightDemoState(State[_DropdownItemHeightDemo]):
    def initState(self):
        self.value = "Alpha"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                DropdownButton(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    items=[
                        DropdownMenuItem(value="Alpha", child=Text("Alpha")),
                        DropdownMenuItem(value="Beta", child=Text("Beta")),
                        DropdownMenuItem(value="Gamma", child=Text("Gamma")),
                    ],
                    itemHeight=60,
                    mouseCursor=SystemMouseCursors.cell,
                    dropdownMenuItemMouseCursor=SystemMouseCursors.click,
                    isExpanded=True,
                ),
                SizedBox(height=4),
                Text(
                    f"Selected: {self.value}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class _DropdownBarrierDemo(StatefulWidget):
    def createState(self):
        return _DropdownBarrierDemoState()


class _DropdownBarrierDemoState(State[_DropdownBarrierDemo]):
    def initState(self):
        self.value = "One"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                DropdownButton(
                    value=self.value,
                    onChanged=lambda v: self.setState(
                        lambda: setattr(self, "value", v)
                    ),
                    items=[
                        DropdownMenuItem(value="One", child=Text("One")),
                        DropdownMenuItem(value="Two", child=Text("Two")),
                        DropdownMenuItem(value="Three", child=Text("Three")),
                    ],
                    barrierDismissible=False,
                    isExpanded=True,
                ),
                SizedBox(height=4),
                Text(
                    "barrierDismissible=False: must select an item",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            ],
        )


class _ShowMenuDemo(StatefulWidget):
    def createState(self):
        return _ShowMenuDemoState()


class _ShowMenuDemoState(State[_ShowMenuDemo]):
    def initState(self):
        self.selection = "None"

    def _select(self, value):
        self.selection = value
        self.setState(lambda: None)

    def _open_menu(self, context):
        showMenu(
            context=context,
            position=RelativeRect.fromLTRB(120.0, 120.0, 0.0, 0.0),
            items=[
                PopupMenuItem(
                    value="cut",
                    onTap=lambda: self._select("cut"),
                    child=Text("Cut"),
                ),
                PopupMenuItem(
                    value="copy",
                    onTap=lambda: self._select("copy"),
                    child=Text("Copy"),
                ),
                PopupMenuItem(
                    value="paste",
                    onTap=lambda: self._select("paste"),
                    child=Text("Paste"),
                ),
            ],
            elevation=8.0,
            clipBehavior=Clip.antiAlias,
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=lambda: self._open_menu(context),
                    child=Text(
                        "showMenu(...) at RelativeRect.fromLTRB(120, 120, 0, 0)"
                    ),
                ),
                SizedBox(height=12),
                Text(
                    f"Selected: {self.selection}",
                    style=TextStyle(fontSize=13, color=Colors.grey),
                ),
            ],
        )


class MenuPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Menus",
            description=(
                "Shows desktop-style command menus, nested actions, and shortcut "
                "hints, with clear feedback for anchored popups and open state."
            ),
            children=[
                SplitViewTile(
                    title="MenuBar",
                    description="A horizontal menu bar with cascading submenus. Supports accelerator labels and keyboard shortcuts.",
                    instruction="Click a top-level menu to open it. Hover over items to navigate. Try pressing Alt to see accelerator underlines.",
                    visible=_MenuBarDemo(),
                    code=CodeArea(
                        code="MenuBar(\n"
                        "    children=[\n"
                        "        SubmenuButton(\n"
                        "            menuChildren=[\n"
                        "                MenuItemButton(\n"
                        "                    onPressed=on_new,\n"
                        "                    leadingIcon=Icon(Icons.add),\n"
                        "                    shortcut=SingleActivator(\n"
                        "                        LogicalKeyboardKey.keyN,\n"
                        "                        control=True,\n"
                        "                    ),\n"
                        '                    child=MenuAcceleratorLabel("&New"),\n'
                        "                ),\n"
                        "            ],\n"
                        '            child=MenuAcceleratorLabel("&File"),\n'
                        "        ),\n"
                        "    ],\n"
                        ")",
                    ),
                ),
                SplitViewTile(
                    title="MenuAnchor",
                    description="Attach a menu to any widget. Opens on demand via MenuController.",
                    instruction="Click 'Open Menu' to show the context menu. Select an option to see the selected value update.",
                    visible=_MenuAnchorDemo(),
                    code=CodeArea(
                        code="controller = MenuController()\n"
                        "\n"
                        "MenuAnchor(\n"
                        "    controller=controller,\n"
                        "    menuChildren=[\n"
                        "        MenuItemButton(\n"
                        "            onPressed=on_select,\n"
                        '            child=Text("Option A"),\n'
                        "        ),\n"
                        "    ],\n"
                        "    child=ElevatedButton(\n"
                        "        onPressed=lambda: controller.open(),\n"
                        '        child=Text("Open Menu"),\n'
                        "    ),\n"
                        ")",
                    ),
                ),
                SplitViewTile(
                    title="Disabled MenuItemButton",
                    description="MenuItemButton with onPressed=None is disabled and grayed out.",
                    instruction="Open the menu. The 'Disabled Item' should appear grayed out and not respond to clicks.",
                    visible=_DisabledMenuItemDemo(),
                    code=CodeArea(
                        code="MenuItemButton(\n"
                        "    onPressed=None,\n"
                        '    child=Text("Disabled Item"),\n'
                        ")",
                    ),
                ),
                SplitViewTile(
                    title="PopupMenuButton variants",
                    description=(
                        "Combines the main PopupMenuButton property groups in one tile: the base action menu, "
                        "styled items, surface styling, rounded corners, layout sizing, clipping, and animation."
                    ),
                    instruction="Choose a preset, open the popup menu, then compare how the selected properties affect the menu and item presentation.",
                    visible=_PopupMenuVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "preset = 'rounded'\n\n"
                            "PopupMenuButton(\n"
                            "    itemBuilder=build_items,\n"
                            "    onSelected=on_selected,\n"
                            "    shadowColor=Colors.red if preset == 'shadow' else None,\n"
                            "    borderRadius=BorderRadius.circular(16)\n"
                            "        if preset == 'rounded' else None,\n"
                            "    menuPadding=EdgeInsets.all(16)\n"
                            "        if preset == 'layout' else None,\n"
                            "    clipBehavior=Clip.antiAlias if preset == 'clip' else None,\n"
                            "    popUpAnimationStyle=AnimationStyle.noAnimation\n"
                            "        if preset == 'animation' else None,\n"
                            "    icon=Icon(Icons.more_vert),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="PopupMenuDivider",
                    description=(
                        "PopupMenuDivider is a horizontal divider used between PopupMenuItem "
                        "entries. It supports height, thickness, indent, endIndent, radius, and color."
                    ),
                    instruction="Open the menu to see a default divider and a customized red divider grouping items.",
                    visible=_PopupMenuDividerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "PopupMenuButton(\n"
                            "    itemBuilder=lambda ctx: [\n"
                            "        PopupMenuItem(value='cut', child=Text('Cut')),\n"
                            "        PopupMenuItem(value='copy', child=Text('Copy')),\n"
                            "        PopupMenuItem(value='paste', child=Text('Paste')),\n"
                            "        PopupMenuDivider(),\n"
                            "        PopupMenuItem(value='delete', child=Text('Delete')),\n"
                            "        PopupMenuDivider(\n"
                            "            height=24,\n"
                            "            thickness=2,\n"
                            "            indent=16,\n"
                            "            endIndent=16,\n"
                            "            color=Colors.red,\n"
                            "        ),\n"
                            "        PopupMenuItem(value='report', child=Text('Report')),\n"
                            "    ],\n"
                            "    icon=Icon(Icons.more_vert),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="PopupMenuPosition",
                    description=(
                        "PopupMenuPosition controls whether the popup menu appears "
                        "over or under the anchor button."
                    ),
                    instruction="Click each button to see the menu appear at different positions.",
                    visible=_PopupMenuPositionDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "PopupMenuButton(\n"
                            "    itemBuilder=lambda ctx: [\n"
                            "        PopupMenuItem(value='cut', child=Text('Cut')),\n"
                            "        PopupMenuItem(value='copy', child=Text('Copy')),\n"
                            "    ],\n"
                            "    position=PopupMenuPosition.over,\n"
                            "    child=Text('Open Menu'),\n"
                            ")\n\n"
                            "PopupMenuButton(\n"
                            "    itemBuilder=items,\n"
                            "    position=PopupMenuPosition.under,\n"
                            "    child=Text('Open Menu'),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="MenuController",
                    description=(
                        "MenuController provides programmatic control over a DropdownMenu. "
                        "Call open() and close() to toggle the menu, and read isOpen to check its state."
                    ),
                    instruction="Use the open/close buttons to programmatically control the dropdown menu.",
                    visible=_MenuControllerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "ctrl = MenuController()\n\n"
                            "DropdownMenu(\n"
                            "    menuController=ctrl,\n"
                            "    initialSelection='Red',\n"
                            "    onSelected=on_selected,\n"
                            "    dropdownMenuEntries=[...],\n"
                            ")\n\n"
                            "ctrl.open()\n"
                            "ctrl.close()\n"
                            "ctrl.isOpen"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownMenu (Material 3)",
                    description=(
                        "Material 3 dropdown with filtering, leading icons, and label. "
                        "Uses DropdownMenuEntry items instead of DropdownMenuItem."
                    ),
                    instruction="Select a color and a size from the dropdown menus.",
                    visible=_DropdownMenuDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownMenu(\n"
                            "    initialSelection='Red',\n"
                            "    onSelected=on_color_selected,\n"
                            "    label=Text('Color'),\n"
                            "    dropdownMenuEntries=[\n"
                            "        DropdownMenuEntry(value='Red', label='Red'),\n"
                            "        DropdownMenuEntry(value='Blue', label='Blue'),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownButton (Classic)",
                    description=(
                        "The classic Material dropdown. Uses DropdownMenuItem children and "
                        "reports the selected value via onChanged. Set isExpanded=True to fill available width."
                    ),
                    instruction="Select a fruit from the dropdown.",
                    visible=_DropdownButtonDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownButton(\n"
                            "    value=selected_fruit,\n"
                            "    onChanged=on_fruit_changed,\n"
                            "    items=[\n"
                            "        DropdownMenuItem(value='Apple', child=Text('Apple')),\n"
                            "        DropdownMenuItem(value='Banana', child=Text('Banana')),\n"
                            "    ],\n"
                            "    isExpanded=True,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownMenuCloseBehavior",
                    description=(
                        "DropdownMenuCloseBehavior controls how the menu closes: "
                        "all (close entire menu tree), self (close only this menu), "
                        "or none (stay open on selection)."
                    ),
                    instruction="Open each dropdown and select an item to observe the close behavior.",
                    visible=_DropdownMenuCloseBehaviorDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownMenu(\n"
                            "    initialSelection='Red',\n"
                            "    onSelected=on_selected,\n"
                            "    closeBehavior=DropdownMenuCloseBehavior.all,\n"
                            "    dropdownMenuEntries=[...],\n"
                            ")\n\n"
                            "DropdownMenu(\n"
                            "    closeBehavior=DropdownMenuCloseBehavior.none,\n"
                            "    dropdownMenuEntries=[...],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownButton selectedItemBuilder",
                    description=(
                        "DropdownButton with selectedItemBuilder showing abbreviated text "
                        "(first 3 chars + '...') for the selected item."
                    ),
                    instruction="Open the dropdown to see full names; the button shows abbreviated text.",
                    visible=_DropdownSelectedItemBuilderDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownButton(\n"
                            "    value=selected,\n"
                            "    onChanged=on_changed,\n"
                            "    items=[...],\n"
                            "    selectedItemBuilder=lambda ctx: [\n"
                            "        Text(f[:3] + '...') for f in fruits\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownButton itemHeight & mouseCursor",
                    description=(
                        "DropdownButton with itemHeight=60 for tall items, "
                        "mouseCursor=cell, dropdownMenuItemMouseCursor=click."
                    ),
                    instruction="Open the dropdown to see the tall items and custom cursors.",
                    visible=_DropdownItemHeightDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownButton(\n"
                            "    value=selected,\n"
                            "    onChanged=on_changed,\n"
                            "    items=[...],\n"
                            "    itemHeight=60,\n"
                            "    mouseCursor=SystemMouseCursors.cell,\n"
                            "    dropdownMenuItemMouseCursor=\n"
                            "        SystemMouseCursors.click,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="DropdownButton barrierDismissible",
                    description=(
                        "DropdownButton with barrierDismissible=False. Clicking outside "
                        "the dropdown does not close it; you must select an item."
                    ),
                    instruction="Open the dropdown and try clicking outside \u2014 it won't close.",
                    visible=_DropdownBarrierDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "DropdownButton(\n"
                            "    value=selected,\n"
                            "    onChanged=on_changed,\n"
                            "    items=[...],\n"
                            "    barrierDismissible=False,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="showMenu & RelativeRect",
                    description=(
                        "showMenu(...) is a top-level function that displays a popup menu "
                        "anchored at a RelativeRect position relative to the Navigator. "
                        "RelativeRect.fromLTRB describes the inset of a rectangle from "
                        "the four edges of its container."
                    ),
                    instruction="Click the button to call showMenu at a fixed RelativeRect position.",
                    visible=_ShowMenuDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "showMenu(\n"
                            "    context=context,\n"
                            "    position=RelativeRect.fromLTRB(\n"
                            "        120.0, 120.0, 0.0, 0.0,\n"
                            "    ),\n"
                            "    items=[\n"
                            "        PopupMenuItem(\n"
                            "            value='cut',\n"
                            "            onTap=lambda: select('cut'),\n"
                            "            child=Text('Cut'),\n"
                            "        ),\n"
                            "    ],\n"
                            "    elevation=8.0,\n"
                            "    clipBehavior=Clip.antiAlias,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
