from flut.dart import Color
from flut.dart.ui import Clip
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Center,
    Column,
    Row,
    Wrap,
    SizedBox,
    Container,
    Icon,
    Padding,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    MainAxisSize,
    BoxConstraints,
    MainAxisAlignment,
)
from flut.flutter.material import (
    AlertDialog,
    Colors,
    Dialog,
    ElevatedButton,
    Icons,
    SimpleDialog,
    SimpleDialogOption,
    TextButton,
    showDialog,
)
from flut.flutter.widgets.navigator import Navigator
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
    RoundedRectangleBorder,
    Alignment,
    VerticalDirection,
)

from widgets import CatalogPage, SplitViewTile, CodeArea


class _AlertDialogDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogDemoState()


class _AlertDialogDemoState(State[_AlertDialogDemo]):
    def initState(self):
        self.result_text = "No dialog shown yet"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Show AlertDialog"),
                    onPressed=lambda: showDialog(
                        context=context,
                        builder=lambda ctx: AlertDialog(
                            title=Text("Discard draft?"),
                            content=Text(
                                "Are you sure you want to discard your draft? "
                                "This action cannot be undone."
                            ),
                            actions=[
                                TextButton(
                                    child=Text("Cancel"),
                                    onPressed=lambda: Navigator.pop(ctx),
                                ),
                                TextButton(
                                    child=Text("Discard"),
                                    onPressed=lambda: (
                                        Navigator.pop(ctx),
                                        self.setState(
                                            lambda: setattr(
                                                self,
                                                "result_text",
                                                "User chose: Discard",
                                            )
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(self.result_text, style=TextStyle(fontSize=13)),
            ],
        )


class _SimpleDialogDemo(StatefulWidget):
    def createState(self):
        return _SimpleDialogDemoState()


class _SimpleDialogDemoState(State[_SimpleDialogDemo]):
    def initState(self):
        self.selected = "None selected"

    def _show_simple(self, context):
        def on_option(value):
            Navigator.pop(context)
            self.setState(lambda: setattr(self, "selected", f"Selected: {value}"))

        showDialog(
            context=context,
            builder=lambda ctx: SimpleDialog(
                title=Text("Choose a department"),
                children=[
                    SimpleDialogOption(
                        onPressed=lambda: on_option("Treasury"),
                        child=Text("Treasury department"),
                    ),
                    SimpleDialogOption(
                        onPressed=lambda: on_option("State"),
                        child=Text("State department"),
                    ),
                    SimpleDialogOption(
                        onPressed=lambda: on_option("Defense"),
                        child=Text("Defense department"),
                    ),
                ],
            ),
        )

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Show SimpleDialog"),
                    onPressed=lambda: self._show_simple(context),
                ),
                SizedBox(height=12),
                Text(self.selected, style=TextStyle(fontSize=13)),
            ],
        )


class _DialogWidgetDemo(StatefulWidget):
    def createState(self):
        return _DialogWidgetDemoState()


class _DialogWidgetDemoState(State[_DialogWidgetDemo]):
    def initState(self):
        self.shown = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Show Custom Dialog"),
                    onPressed=lambda: showDialog(
                        context=context,
                        builder=lambda ctx: Dialog(
                            shape=RoundedRectangleBorder(
                                borderRadius=BorderRadius.circular(16),
                            ),
                            child=Container(
                                padding=EdgeInsets.all(24),
                                child=Column(
                                    mainAxisSize=MainAxisSize.min,
                                    children=[
                                        Icon(
                                            Icons.check_circle,
                                            color=Colors.green,
                                            size=48.0,
                                        ),
                                        SizedBox(height=16),
                                        Text(
                                            "Success!",
                                            style=TextStyle(
                                                fontSize=20,
                                            ),
                                        ),
                                        SizedBox(height=8),
                                        Text(
                                            "Your operation completed successfully.",
                                            style=TextStyle(
                                                fontSize=14,
                                                color=Colors.grey,
                                            ),
                                        ),
                                        SizedBox(height=24),
                                        ElevatedButton(
                                            child=Text("OK"),
                                            onPressed=lambda: Navigator.pop(ctx),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(
                    "Dialog gives full control over layout",
                    style=TextStyle(fontSize=11, color=Colors.grey),
                ),
            ],
        )


class _BarrierDismissDemo(StatefulWidget):
    def createState(self):
        return _BarrierDismissDemoState()


class _BarrierDismissDemoState(State[_BarrierDismissDemo]):
    def initState(self):
        self.log = "Tap the button"

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Non-dismissible Dialog"),
                    onPressed=lambda: showDialog(
                        context=context,
                        barrierDismissible=False,
                        builder=lambda ctx: AlertDialog(
                            title=Text("Terms & Conditions"),
                            content=Text(
                                "You must accept the terms to continue. "
                                "Tapping outside will NOT close this dialog."
                            ),
                            actions=[
                                TextButton(
                                    child=Text("Accept"),
                                    onPressed=lambda: (
                                        Navigator.pop(ctx),
                                        self.setState(
                                            lambda: setattr(
                                                self,
                                                "log",
                                                "Terms accepted",
                                            )
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
                SizedBox(height=12),
                Text(self.log, style=TextStyle(fontSize=13)),
            ],
        )


class _AlertDialogIconDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogIconDemoState()


class _AlertDialogIconDemoState(State[_AlertDialogIconDemo]):
    def initState(self):
        pass

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Text("Show Alert with Icon"),
                    onPressed=lambda: showDialog(
                        context=context,
                        builder=lambda ctx: AlertDialog(
                            icon=Icon(
                                Icons.warning_amber, color=Colors.orange, size=36.0
                            ),
                            title=Text("Warning"),
                            content=Text(
                                "This action may have unintended consequences. "
                                "Proceed with caution."
                            ),
                            actions=[
                                TextButton(
                                    child=Text("Cancel"),
                                    onPressed=lambda: Navigator.pop(ctx),
                                ),
                                TextButton(
                                    child=Text("Proceed"),
                                    onPressed=lambda: Navigator.pop(ctx),
                                ),
                            ],
                        ),
                    ),
                ),
            ],
        )


class _AlertDialogInlineDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogInlineDemoState()


class _AlertDialogInlineDemoState(State[_AlertDialogInlineDemo]):
    def initState(self):
        self.show_dialog = False

    def _toggle(self):
        self.show_dialog = not self.show_dialog
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=self._toggle,
                    child=Text("Hide Dialog" if self.show_dialog else "Show Dialog"),
                ),
                *(
                    [
                        Padding(
                            padding=EdgeInsets.only(top=8),
                            child=AlertDialog(
                                title=Text("Alert!"),
                                content=Text("This is an AlertDialog rendered inline."),
                                actions=[
                                    ElevatedButton(
                                        onPressed=self._toggle,
                                        child=Text("OK"),
                                    ),
                                ],
                            ),
                        ),
                    ]
                    if self.show_dialog
                    else []
                ),
            ],
        )


class _AlertDialogSpacingDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogSpacingDemoState()


class _AlertDialogSpacingDemoState(State[_AlertDialogSpacingDemo]):
    def initState(self):
        self.show = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show", not self.show)
                    ),
                    child=Text("Toggle Dialog"),
                ),
                *(
                    [
                        Padding(
                            padding=EdgeInsets.only(top=8),
                            child=AlertDialog(
                                icon=Icon(Icons.info, color=Colors.blue),
                                iconPadding=EdgeInsets.only(top=24),
                                title=Text("Spacing Demo"),
                                content=Text("Custom iconPadding and buttonPadding."),
                                buttonPadding=EdgeInsets.symmetric(horizontal=24),
                                actions=[
                                    TextButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("Cancel"),
                                    ),
                                    ElevatedButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("OK"),
                                    ),
                                ],
                            ),
                        ),
                    ]
                    if self.show
                    else []
                ),
            ],
        )


class _AlertDialogActionsAlignDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogActionsAlignDemoState()


class _AlertDialogActionsAlignDemoState(State[_AlertDialogActionsAlignDemo]):
    def initState(self):
        self.show = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show", not self.show)
                    ),
                    child=Text("Toggle Dialog"),
                ),
                *(
                    [
                        Padding(
                            padding=EdgeInsets.only(top=8),
                            child=AlertDialog(
                                title=Text("Actions Alignment"),
                                content=Text("Actions centered, overflow upward."),
                                actionsAlignment=MainAxisAlignment.center,
                                actionsOverflowDirection=VerticalDirection.up,
                                actions=[
                                    TextButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("Discard"),
                                    ),
                                    TextButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("Cancel"),
                                    ),
                                    ElevatedButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("Save"),
                                    ),
                                ],
                            ),
                        ),
                    ]
                    if self.show
                    else []
                ),
            ],
        )


class _AlertDialogShapeDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogShapeDemoState()


class _AlertDialogShapeDemoState(State[_AlertDialogShapeDemo]):
    def initState(self):
        self.show = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show", not self.show)
                    ),
                    child=Text("Toggle Dialog"),
                ),
                *(
                    [
                        Padding(
                            padding=EdgeInsets.only(top=8),
                            child=AlertDialog(
                                title=Text("Rounded Dialog"),
                                content=Text(
                                    "shape with borderRadius=24, blue shadow."
                                ),
                                shape=RoundedRectangleBorder(
                                    borderRadius=BorderRadius.circular(24),
                                ),
                                shadowColor=Colors.blue,
                                clipBehavior=Clip.antiAlias,
                                actions=[
                                    ElevatedButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("OK"),
                                    ),
                                ],
                            ),
                        ),
                    ]
                    if self.show
                    else []
                ),
            ],
        )


class _AlertDialogScrollableDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogScrollableDemoState()


class _AlertDialogScrollableDemoState(State[_AlertDialogScrollableDemo]):
    def initState(self):
        self.show = False

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    onPressed=lambda: self.setState(
                        lambda: setattr(self, "show", not self.show)
                    ),
                    child=Text("Toggle Dialog"),
                ),
                *(
                    [
                        Padding(
                            padding=EdgeInsets.only(top=8),
                            child=AlertDialog(
                                title=Text("Narrow Scrollable"),
                                content=Column(
                                    children=[
                                        Text("Line " + str(i)) for i in range(1, 16)
                                    ],
                                ),
                                insetPadding=EdgeInsets.all(10),
                                alignment=Alignment.bottomCenter,
                                constraints=BoxConstraints(maxWidth=300),
                                scrollable=True,
                                actions=[
                                    ElevatedButton(
                                        onPressed=lambda: self.setState(
                                            lambda: setattr(self, "show", False)
                                        ),
                                        child=Text("Close"),
                                    ),
                                ],
                            ),
                        ),
                    ]
                    if self.show
                    else []
                ),
            ],
        )


class _AlertDialogVariantsDemo(StatefulWidget):
    def createState(self):
        return _AlertDialogVariantsDemoState()


class _AlertDialogVariantsDemoState(State[_AlertDialogVariantsDemo]):
    def initState(self):
        self.variant = "basic"
        self.result_text = "Choose a preset, then open the dialog."

    def _select_variant(self, variant):
        self.variant = variant
        self.setState(lambda: None)

    def _close_with(self, dialog_context, label):
        Navigator.pop(dialog_context)
        self.setState(lambda: setattr(self, "result_text", f"{self.variant}: {label}"))

    def _build_dialog(self, dialog_context):
        if self.variant == "icon":
            return AlertDialog(
                icon=Icon(Icons.warning_amber, color=Colors.orange, size=36.0),
                title=Text("Warning"),
                content=Text(
                    "This action may have unintended consequences. Proceed with caution."
                ),
                actions=[
                    TextButton(
                        child=Text("Cancel"),
                        onPressed=lambda: self._close_with(dialog_context, "Cancel"),
                    ),
                    TextButton(
                        child=Text("Proceed"),
                        onPressed=lambda: self._close_with(dialog_context, "Proceed"),
                    ),
                ],
            )
        if self.variant == "spacing":
            return AlertDialog(
                icon=Icon(Icons.info, color=Colors.blue),
                iconPadding=EdgeInsets.only(top=24),
                title=Text("Spacing Demo"),
                content=Text("Custom iconPadding and buttonPadding."),
                buttonPadding=EdgeInsets.symmetric(horizontal=24),
                actions=[
                    TextButton(
                        child=Text("Cancel"),
                        onPressed=lambda: self._close_with(dialog_context, "Cancel"),
                    ),
                    ElevatedButton(
                        child=Text("OK"),
                        onPressed=lambda: self._close_with(dialog_context, "OK"),
                    ),
                ],
            )
        if self.variant == "actions":
            return AlertDialog(
                title=Text("Actions Alignment"),
                content=Text("Actions centered, overflow upward."),
                actionsAlignment=MainAxisAlignment.center,
                actionsOverflowDirection=VerticalDirection.up,
                actions=[
                    TextButton(
                        child=Text("Discard"),
                        onPressed=lambda: self._close_with(dialog_context, "Discard"),
                    ),
                    TextButton(
                        child=Text("Cancel"),
                        onPressed=lambda: self._close_with(dialog_context, "Cancel"),
                    ),
                    ElevatedButton(
                        child=Text("Save"),
                        onPressed=lambda: self._close_with(dialog_context, "Save"),
                    ),
                ],
            )
        if self.variant == "shape":
            return AlertDialog(
                title=Text("Rounded Dialog"),
                content=Text("shape with borderRadius=24, blue shadow."),
                shape=RoundedRectangleBorder(
                    borderRadius=BorderRadius.circular(24),
                ),
                shadowColor=Colors.blue,
                clipBehavior=Clip.antiAlias,
                actions=[
                    ElevatedButton(
                        child=Text("OK"),
                        onPressed=lambda: self._close_with(dialog_context, "OK"),
                    ),
                ],
            )
        return AlertDialog(
            title=Text("Discard draft?"),
            content=Text(
                "Are you sure you want to discard your draft? This action cannot be undone."
            ),
            actions=[
                TextButton(
                    child=Text("Cancel"),
                    onPressed=lambda: self._close_with(dialog_context, "Cancel"),
                ),
                TextButton(
                    child=Text("Discard"),
                    onPressed=lambda: self._close_with(dialog_context, "Discard"),
                ),
            ],
        )

    def _show_dialog(self, context):
        showDialog(
            context=context,
            builder=lambda dialog_context: self._build_dialog(dialog_context),
        )

    def build(self, context):
        options = [
            ("basic", "Basic"),
            ("icon", "Icon"),
            ("spacing", "Spacing"),
            ("actions", "Actions"),
            ("shape", "Shape"),
        ]
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
                            else TextButton(
                                onPressed=lambda key=key: self._select_variant(key),
                                child=Text(label),
                            )
                        )
                        for key, label in options
                    ],
                ),
                SizedBox(height=12),
                ElevatedButton(
                    child=Text("Show AlertDialog"),
                    onPressed=lambda: self._show_dialog(context),
                ),
                SizedBox(height=12),
                Text(self.result_text, style=TextStyle(fontSize=13)),
            ],
        )


class DialogPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Dialogs",
            description=(
                "Covers modal surfaces for confirmation, picking, and custom "
                "flows, including how values are returned to the page when a "
                "dialog closes."
            ),
            children=[
                SplitViewTile(
                    title="AlertDialog variants",
                    description=(
                        "Combines the most common AlertDialog presets in one tile: the basic confirmation layout, "
                        "an icon header, spacing adjustments, centered actions, and rounded shape styling."
                    ),
                    instruction="Choose a preset, open the dialog, then compare how the selected AlertDialog properties change the result.",
                    visible=_AlertDialogVariantsDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "preset = 'shape'\n\n"
                            "showDialog(\n"
                            "    context=context,\n"
                            "    builder=lambda ctx: AlertDialog(\n"
                            "        icon=Icon(Icons.warning_amber)\n"
                            "            if preset == 'icon' else None,\n"
                            "        iconPadding=EdgeInsets.only(top=24)\n"
                            "            if preset == 'spacing' else None,\n"
                            "        buttonPadding=EdgeInsets.symmetric(horizontal=24)\n"
                            "            if preset == 'spacing' else None,\n"
                            "        actionsAlignment=MainAxisAlignment.center\n"
                            "            if preset == 'actions' else None,\n"
                            "        shape=RoundedRectangleBorder(\n"
                            "            borderRadius=BorderRadius.circular(24)\n"
                            "        ) if preset == 'shape' else None,\n"
                            "        title=Text('Discard draft?'),\n"
                            "        actions=[...],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="SimpleDialog",
                    description="A dialog that offers the user a choice between several options, displayed as a list of SimpleDialogOption widgets.",
                    instruction="Press the button to show a SimpleDialog with three department options. Tap one to select it.",
                    visible=_SimpleDialogDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "showDialog(\n"
                            "    context=context,\n"
                            "    builder=lambda ctx: SimpleDialog(\n"
                            "        title=Text('Choose a department'),\n"
                            "        children=[\n"
                            "            SimpleDialogOption(\n"
                            "                onPressed=lambda: on_select('Treasury'),\n"
                            "                child=Text('Treasury department'),\n"
                            "            ),\n"
                            "            SimpleDialogOption(\n"
                            "                onPressed=lambda: on_select('State'),\n"
                            "                child=Text('State department'),\n"
                            "            ),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Dialog — custom layout",
                    description="The base Dialog widget provides full control over dialog layout. Use it when AlertDialog or SimpleDialog don't fit your needs.",
                    instruction="Press the button to show a custom Dialog with an icon, text, and a close button.",
                    visible=_DialogWidgetDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "showDialog(\n"
                            "    context=context,\n"
                            "    builder=lambda ctx: Dialog(\n"
                            "        shape=RoundedRectangleBorder(\n"
                            "            borderRadius=BorderRadius.circular(16),\n"
                            "        ),\n"
                            "        child=Container(\n"
                            "            padding=EdgeInsets.all(24),\n"
                            "            child=Column(\n"
                            "                children=[Icon(Icons.check_circle), ...],\n"
                            "            ),\n"
                            "        ),\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="barrierDismissible=False",
                    description="When barrierDismissible is False, the user cannot close the dialog by tapping outside. They must use the provided action buttons.",
                    instruction="Press the button. Try tapping outside the dialog — it won't close. You must press Accept.",
                    visible=_BarrierDismissDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "showDialog(\n"
                            "    context=context,\n"
                            "    barrierDismissible=False,\n"
                            "    builder=lambda ctx: AlertDialog(\n"
                            "        title=Text('Terms & Conditions'),\n"
                            "        content=Text('You must accept.'),\n"
                            "        actions=[\n"
                            "            TextButton(\n"
                            "                child=Text('Accept'),\n"
                            "                onPressed=lambda: Navigator.pop(ctx),\n"
                            "            ),\n"
                            "        ],\n"
                            "    ),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AlertDialog (inline)",
                    description=(
                        "AlertDialog rendered directly in the widget tree instead of as a modal overlay. "
                        "Useful for embedding confirmations or alerts within a page layout."
                    ),
                    instruction="Click the button to toggle the inline dialog on and off.",
                    visible=_AlertDialogInlineDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AlertDialog(\n"
                            "    title=Text('Alert!'),\n"
                            "    content=Text('Rendered inline.'),\n"
                            "    actions=[\n"
                            "        ElevatedButton(\n"
                            "            onPressed=dismiss,\n"
                            "            child=Text('OK'),\n"
                            "        ),\n"
                            "    ],\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AlertDialog insetPadding & constraints & scrollable",
                    description=(
                        "AlertDialog with narrow insetPadding, bottomCenter alignment, "
                        "maxWidth=300 constraint, and scrollable=True."
                    ),
                    instruction="Click the button to see a narrow scrollable dialog at the bottom.",
                    visible=_AlertDialogScrollableDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "AlertDialog(\n"
                            "    insetPadding=EdgeInsets.all(10),\n"
                            "    alignment=Alignment.bottomCenter,\n"
                            "    constraints=BoxConstraints(maxWidth=300),\n"
                            "    scrollable=True,\n"
                            "    title=Text('Narrow Scrollable'),\n"
                            "    content=Column(children=[...]),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
