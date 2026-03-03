from flut.dart import Color
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    GlobalKey,
    Form,
    AutovalidateMode,
    Expanded,
    Center,
    Icon,
    TextEditingController,
    FocusNode,
    CallbackShortcuts,
    SingleActivator,
    WidgetStatePropertyAll,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    TextFormField,
    InputDecoration,
    TextField,
    FloatingLabelBehavior,
    Icons,
    DropdownMenu,
    DropdownMenuEntry,
    MenuStyle,
)
from flut.dart.ui import FontWeight, TextDirection, Offset
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BoxDecoration,
    BorderRadius,
)
from flut.flutter.services.keyboard_key import LogicalKeyboardKey
from flut.flutter.services import SystemMouseCursors
from flut.flutter.services.text_input import TextInputType
from utils import CODE_FONT_FAMILY
from widgets import CatalogPage, SplitViewTile, CodeArea


class _FormDemo(StatefulWidget):
    def createState(self):
        return _FormDemoState()


class _FormDemoState(State[_FormDemo]):

    def initState(self):
        self.form_key = GlobalKey(debugLabel="demo-form")
        self.saved_values = {}
        self.status = ""

    def _validate_name(self, value):
        if not value or len(value.strip()) == 0:
            return "Name is required"
        if len(value) < 2:
            return "Name must be at least 2 characters"
        return None

    def _validate_email(self, value):
        if not value or len(value.strip()) == 0:
            return "Email is required"
        if "@" not in value:
            return "Enter a valid email"
        return None

    def _validate_age(self, value):
        if not value or len(value.strip()) == 0:
            return None
        try:
            age = int(value)
            if age < 0 or age > 150:
                return "Enter a valid age"
        except ValueError:
            return "Must be a number"
        return None

    def _on_submit(self):
        form_state = self.form_key.currentState
        if form_state is None:
            return
        is_valid = form_state.validate()
        if is_valid:
            form_state.save()

            def update():
                self.status = f"Form valid! Saved: {self.saved_values}"

            self.setState(update)
        else:

            def update():
                self.status = "Form has errors"

            self.setState(update)

    def _on_reset(self):
        form_state = self.form_key.currentState
        if form_state is None:
            return
        form_state.reset()

        def update():
            self.saved_values = {}
            self.status = "Form reset"

        self.setState(update)

    def build(self, context):
        status_widgets = []
        if self.status:
            status_widgets.append(
                Text(
                    self.status,
                    style=TextStyle(
                        fontSize=14,
                        color=(
                            Colors.green
                            if "valid" in self.status.lower()
                            else Colors.grey
                        ),
                    ),
                )
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Form(
                    key=self.form_key,
                    autovalidateMode=AutovalidateMode.onUserInteraction,
                    child=Column(
                        crossAxisAlignment=CrossAxisAlignment.start,
                        children=[
                            TextFormField(
                                decoration=InputDecoration(hintText="Name"),
                                validator=self._validate_name,
                                onSaved=lambda v: self.saved_values.update({"name": v}),
                            ),
                            SizedBox(height=12),
                            TextFormField(
                                decoration=InputDecoration(hintText="Email"),
                                validator=self._validate_email,
                                onSaved=lambda v: self.saved_values.update(
                                    {"email": v}
                                ),
                            ),
                            SizedBox(height=12),
                            TextFormField(
                                decoration=InputDecoration(hintText="Age (optional)"),
                                validator=self._validate_age,
                                onSaved=lambda v: self.saved_values.update({"age": v}),
                            ),
                        ],
                    ),
                ),
                SizedBox(height=16),
                Row(
                    children=[
                        ElevatedButton(
                            onPressed=self._on_submit,
                            child=Text("Validate & Save"),
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            onPressed=self._on_reset,
                            child=Text("Reset"),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=status_widgets,
                ),
            ],
        )


class _FormFieldStateDemo(StatefulWidget):
    def createState(self):
        return _FormFieldStateDemoState()


class _FormFieldStateDemoState(State[_FormFieldStateDemo]):

    def initState(self):
        self.field_key_1 = GlobalKey(debugLabel="field-1")
        self.field_key_2 = GlobalKey(debugLabel="field-2")
        self.status = ""

    def _validate_not_empty(self, value):
        if not value or len(value.strip()) == 0:
            return "This field cannot be empty"
        return None

    def _validate_min_length(self, value):
        if not value or len(value.strip()) == 0:
            return "This field cannot be empty"
        if len(value) < 4:
            return "Must be at least 4 characters"
        return None

    def _validate_field_1(self):
        state = self.field_key_1.currentState
        if state is not None:
            result = state.validate()

            def update():
                self.status = f"Field 1 validate() -> {result}"

            self.setState(update)

    def _validate_field_2(self):
        state = self.field_key_2.currentState
        if state is not None:
            result = state.validate()

            def update():
                self.status = f"Field 2 validate() -> {result}"

            self.setState(update)

    def _reset_field_1(self):
        state = self.field_key_1.currentState
        if state is not None:
            state.reset()

            def update():
                self.status = "Field 1 reset"

            self.setState(update)

    def _reset_field_2(self):
        state = self.field_key_2.currentState
        if state is not None:
            state.reset()

            def update():
                self.status = "Field 2 reset"

            self.setState(update)

    def build(self, context):
        status_widget = Text(
            (
                self.status
                if self.status
                else "Use buttons to validate or reset individual fields."
            ),
            style=TextStyle(
                fontSize=13,
                fontFamily=CODE_FONT_FAMILY,
                color=(
                    Colors.blue
                    if "True" in self.status
                    else Colors.orange if self.status else Colors.grey
                ),
            ),
        )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                TextFormField(
                    key=self.field_key_1,
                    decoration=InputDecoration(hintText="Field 1 (required)"),
                    validator=self._validate_not_empty,
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Validate Field 1"),
                            onPressed=self._validate_field_1,
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reset Field 1"),
                            onPressed=self._reset_field_1,
                        ),
                    ],
                ),
                SizedBox(height=16),
                TextFormField(
                    key=self.field_key_2,
                    decoration=InputDecoration(hintText="Field 2 (min 4 chars)"),
                    validator=self._validate_min_length,
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Validate Field 2"),
                            onPressed=self._validate_field_2,
                        ),
                        SizedBox(width=8),
                        ElevatedButton(
                            child=Text("Reset Field 2"),
                            onPressed=self._reset_field_2,
                        ),
                    ],
                ),
                SizedBox(height=12),
                status_widget,
            ],
        )


class _AutovalidateModeComparisonDemo(StatefulWidget):
    def createState(self):
        return _AutovalidateModeComparisonDemoState()


class _AutovalidateModeComparisonDemoState(State[_AutovalidateModeComparisonDemo]):

    def initState(self):
        self.interaction_log = []

    def _validator(self, value):
        if not value or len(value.strip()) == 0:
            return "Required"
        if len(value) < 3:
            return "Min 3 characters"
        return None

    def _on_changed_disabled(self, value):
        self.interaction_log = self.interaction_log + [f'disabled field: "{value}"']
        self.setState(lambda: None)

    def _on_changed_always(self, value):
        self.interaction_log = self.interaction_log + [f'always field: "{value}"']
        self.setState(lambda: None)

    def _on_changed_interact(self, value):
        self.interaction_log = self.interaction_log + [
            f'onUserInteraction field: "{value}"'
        ]
        self.setState(lambda: None)

    def build(self, context):
        log_widgets = []
        for entry in self.interaction_log[-6:]:
            color = Colors.grey
            if "disabled" in entry:
                color = Colors.blue
            elif "always" in entry:
                color = Colors.orange
            elif "onUserInteraction" in entry:
                color = Colors.green
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=11,
                        fontFamily=CODE_FONT_FAMILY,
                        color=color,
                    ),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        Expanded(
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=[
                                    Text(
                                        "disabled",
                                        style=TextStyle(
                                            fontSize=12,
                                            fontWeight=FontWeight.bold,
                                            color=Colors.blue,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    TextFormField(
                                        decoration=InputDecoration(
                                            hintText="Type here"
                                        ),
                                        validator=self._validator,
                                        autovalidateMode=AutovalidateMode.disabled,
                                        onChanged=self._on_changed_disabled,
                                    ),
                                ],
                            ),
                        ),
                        SizedBox(width=12),
                        Expanded(
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=[
                                    Text(
                                        "always",
                                        style=TextStyle(
                                            fontSize=12,
                                            fontWeight=FontWeight.bold,
                                            color=Colors.orange,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    TextFormField(
                                        decoration=InputDecoration(
                                            hintText="Type here"
                                        ),
                                        validator=self._validator,
                                        autovalidateMode=AutovalidateMode.always,
                                        onChanged=self._on_changed_always,
                                    ),
                                ],
                            ),
                        ),
                        SizedBox(width=12),
                        Expanded(
                            child=Column(
                                crossAxisAlignment=CrossAxisAlignment.start,
                                children=[
                                    Text(
                                        "onUserInteraction",
                                        style=TextStyle(
                                            fontSize=12,
                                            fontWeight=FontWeight.bold,
                                            color=Colors.green,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    TextFormField(
                                        decoration=InputDecoration(
                                            hintText="Type here"
                                        ),
                                        validator=self._validator,
                                        autovalidateMode=AutovalidateMode.onUserInteraction,
                                        onChanged=self._on_changed_interact,
                                    ),
                                ],
                            ),
                        ),
                    ],
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
                        children=(
                            log_widgets
                            if log_widgets
                            else [
                                Text(
                                    "Type in each field to compare validation behavior.",
                                    style=TextStyle(fontSize=11, color=Colors.grey),
                                )
                            ]
                        ),
                    ),
                ),
            ],
        )


class _TextFieldSubmitDemo(StatefulWidget):
    def createState(self):
        return _TextFieldSubmitDemoState()


class _TextFieldSubmitDemoState(State[_TextFieldSubmitDemo]):
    def initState(self):
        self.controller = TextEditingController(text="")
        self.submitted_text = ""

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=400.0,
                    child=TextField(
                        controller=self.controller,
                        decoration=InputDecoration(hintText="Type something..."),
                        onSubmitted=lambda val: self.setState(
                            lambda: setattr(self, "submitted_text", val)
                        ),
                    ),
                ),
                SizedBox(height=12),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Submit"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self, "submitted_text", self.controller.text
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Text("Clear"),
                            onPressed=lambda: (
                                self.controller.clear(),
                                self.setState(
                                    lambda: setattr(self, "submitted_text", "")
                                ),
                            ),
                        ),
                    ],
                ),
                SizedBox(height=16),
                Text(
                    (
                        f'Submitted: "{self.submitted_text}"'
                        if self.submitted_text
                        else "Nothing submitted yet."
                    ),
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _TextInputActionDemo(StatefulWidget):
    def createState(self):
        return _TextInputActionDemoState()


class _TextInputActionDemoState(State[_TextInputActionDemo]):

    def initState(self):
        self.focus_node_1 = FocusNode()
        self.focus_node_2 = FocusNode()
        self.focus_node_3 = FocusNode()
        self.action_log = []

    def _on_done(self, value):
        self.action_log = self.action_log + [f'done: "{value}"']
        self.focus_node_1.unfocus()
        self.setState(lambda: None)

    def _on_next(self, value):
        self.action_log = self.action_log + [f'next: "{value}" -> moved focus']
        self.focus_node_3.requestFocus()
        self.setState(lambda: None)

    def _on_search(self, value):
        self.action_log = self.action_log + [f'search: "{value}"']
        self.setState(lambda: None)

    def build(self, context):
        log_widgets = []
        for entry in self.action_log[-6:]:
            color = Colors.blue
            if entry.startswith("next"):
                color = Colors.green
            elif entry.startswith("search"):
                color = Colors.orange
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=color,
                    ),
                ),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "Press Enter in each field to see its action.",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            )

        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=400.0,
                    child=TextField(
                        focusNode=self.focus_node_1,
                        decoration=InputDecoration(
                            labelText="Action: done",
                            hintText="Submit dismisses focus",
                        ),
                        onSubmitted=self._on_done,
                    ),
                ),
                SizedBox(height=12),
                Container(
                    width=400.0,
                    child=TextField(
                        focusNode=self.focus_node_2,
                        decoration=InputDecoration(
                            labelText="Action: next",
                            hintText="Submit moves to search field",
                        ),
                        onSubmitted=self._on_next,
                    ),
                ),
                SizedBox(height=12),
                Container(
                    width=400.0,
                    child=TextField(
                        focusNode=self.focus_node_3,
                        decoration=InputDecoration(
                            labelText="Action: search",
                            hintText="Submit triggers search log",
                        ),
                        onSubmitted=self._on_search,
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
                        children=log_widgets,
                    ),
                ),
            ],
        )


class _ShortcutModifiersDemo(StatefulWidget):
    def createState(self):
        return _ShortcutModifiersDemoState()


class _ShortcutModifiersDemoState(State[_ShortcutModifiersDemo]):

    def initState(self):
        self.fired_log = []

    def _on_ctrl_a(self):
        self.fired_log = self.fired_log + ["Ctrl+A fired"]
        self.setState(lambda: None)

    def _on_shift_a(self):
        self.fired_log = self.fired_log + ["Shift+A fired"]
        self.setState(lambda: None)

    def _on_ctrl_shift_s(self):
        self.fired_log = self.fired_log + ["Ctrl+Shift+S fired"]
        self.setState(lambda: None)

    def build(self, context):
        ctrl_a = SingleActivator(LogicalKeyboardKey.keyA, control=True)
        shift_a = SingleActivator(LogicalKeyboardKey.keyA, shift=True)
        ctrl_shift_s = SingleActivator(
            LogicalKeyboardKey.keyS, control=True, shift=True
        )

        log_widgets = []
        for entry in self.fired_log[-8:]:
            color = Colors.blue
            if "Shift+A" in entry:
                color = Colors.green
            elif "Ctrl+Shift" in entry:
                color = Colors.purple
            log_widgets.append(
                Text(
                    entry,
                    style=TextStyle(
                        fontSize=12,
                        fontFamily=CODE_FONT_FAMILY,
                        color=color,
                    ),
                ),
            )
        if not log_widgets:
            log_widgets.append(
                Text(
                    "Press Ctrl+A, Shift+A, or Ctrl+Shift+S",
                    style=TextStyle(fontSize=12, color=Colors.grey),
                ),
            )

        return CallbackShortcuts(
            bindings={
                ctrl_a: self._on_ctrl_a,
                shift_a: self._on_shift_a,
                ctrl_shift_s: self._on_ctrl_shift_s,
            },
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        "Keyboard Shortcuts with SingleActivator",
                        style=TextStyle(fontSize=14, fontWeight=FontWeight.bold),
                    ),
                    SizedBox(height=8),
                    Row(
                        children=[
                            Container(
                                padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                                decoration=BoxDecoration(
                                    color=Colors.blue,
                                    borderRadius=BorderRadius.circular(4),
                                ),
                                child=Text(
                                    "Ctrl+A",
                                    style=TextStyle(color=Colors.white, fontSize=12),
                                ),
                            ),
                            SizedBox(width=8),
                            Container(
                                padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                                decoration=BoxDecoration(
                                    color=Colors.green,
                                    borderRadius=BorderRadius.circular(4),
                                ),
                                child=Text(
                                    "Shift+A",
                                    style=TextStyle(color=Colors.white, fontSize=12),
                                ),
                            ),
                            SizedBox(width=8),
                            Container(
                                padding=EdgeInsets.symmetric(horizontal=8, vertical=4),
                                decoration=BoxDecoration(
                                    color=Colors.purple,
                                    borderRadius=BorderRadius.circular(4),
                                ),
                                child=Text(
                                    "Ctrl+Shift+S",
                                    style=TextStyle(color=Colors.white, fontSize=12),
                                ),
                            ),
                        ],
                    ),
                    SizedBox(height=12),
                    Container(
                        width=400.0,
                        child=TextField(
                            decoration=InputDecoration(
                                hintText="Click here and press shortcut keys...",
                            ),
                            readOnly=True,
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
                            children=log_widgets,
                        ),
                    ),
                ],
            ),
        )


class _TextDirectionExpandsDemo(StatefulWidget):
    def createState(self):
        return _TextDirectionExpandsDemoState()


class _TextDirectionExpandsDemoState(State[_TextDirectionExpandsDemo]):
    def initState(self):
        self.rtl_controller = TextEditingController(text="")
        self.expands_controller = TextEditingController(text="")

    def build(self, context):
        return Row(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=250.0,
                    child=TextField(
                        controller=self.rtl_controller,
                        textDirection=TextDirection.rtl,
                        decoration=InputDecoration(
                            labelText="RTL Field",
                            hintText="Text starts from right...",
                        ),
                    ),
                ),
                SizedBox(width=16),
                Container(
                    width=250.0,
                    height=150.0,
                    child=TextField(
                        controller=self.expands_controller,
                        expands=True,
                        maxLines=None,
                        decoration=InputDecoration(
                            labelText="Expands Field",
                            hintText="This field fills available height...",
                        ),
                    ),
                ),
            ],
        )


class _OnEditingCompleteDemo(StatefulWidget):
    def createState(self):
        return _OnEditingCompleteDemoState()


class _OnEditingCompleteDemoState(State[_OnEditingCompleteDemo]):
    def initState(self):
        self.controller = TextEditingController(text="")
        self.completion_count = 0

    def _on_editing_complete(self):
        current = self.controller.text
        if not current.startswith("\u2713 "):
            self.controller.text = "\u2713 " + current
        self.completion_count = self.completion_count + 1
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=400.0,
                    child=TextField(
                        controller=self.controller,
                        decoration=InputDecoration(
                            labelText="Type then press Enter",
                            hintText="onEditingComplete demo...",
                        ),
                        onEditingComplete=self._on_editing_complete,
                    ),
                ),
                SizedBox(height=12),
                Text(
                    f"Completions: {self.completion_count}",
                    style=TextStyle(fontSize=14, fontWeight=FontWeight.bold),
                ),
            ],
        )


class _OnTapMouseCursorDemo(StatefulWidget):
    def createState(self):
        return _OnTapMouseCursorDemoState()


class _OnTapMouseCursorDemoState(State[_OnTapMouseCursorDemo]):
    def initState(self):
        self.tap_count = 0

    def _on_tap(self):
        self.tap_count = self.tap_count + 1
        self.setState(lambda: None)

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Container(
                    width=400.0,
                    child=TextField(
                        decoration=InputDecoration(
                            labelText="Click me",
                            hintText="Hover to see cell cursor...",
                        ),
                        onTap=self._on_tap,
                        mouseCursor=SystemMouseCursors.cell,
                    ),
                ),
                SizedBox(height=12),
                Text(
                    f"Tap count: {self.tap_count}",
                    style=TextStyle(fontSize=14, fontWeight=FontWeight.bold),
                ),
            ],
        )


class _DropdownTrailingIconDemo(StatefulWidget):
    def createState(self):
        return _DropdownTrailingIconDemoState()


class _DropdownTrailingIconDemoState(State[_DropdownTrailingIconDemo]):
    def initState(self):
        self.selected_1 = ""
        self.selected_2 = ""

    def build(self, context):
        entries = [
            DropdownMenuEntry(value="Apple", label="Apple"),
            DropdownMenuEntry(value="Banana", label="Banana"),
            DropdownMenuEntry(value="Cherry", label="Cherry"),
        ]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "showTrailingIcon=False (no arrow):", style=TextStyle(fontSize=13)
                ),
                SizedBox(height=4),
                DropdownMenu(
                    width=250.0,
                    hintText="No trailing icon",
                    showTrailingIcon=False,
                    dropdownMenuEntries=entries,
                    onSelected=lambda val: self.setState(
                        lambda: setattr(self, "selected_1", val or "")
                    ),
                ),
                SizedBox(height=8),
                Text(f"Selected: {self.selected_1}", style=TextStyle(fontSize=12)),
                SizedBox(height=16),
                Text(
                    "selectedTrailingIcon=Icon(Icons.check_circle):",
                    style=TextStyle(fontSize=13),
                ),
                SizedBox(height=4),
                DropdownMenu(
                    width=250.0,
                    hintText="Custom selected icon",
                    selectedTrailingIcon=Icon(Icons.check_circle),
                    dropdownMenuEntries=entries,
                    onSelected=lambda val: self.setState(
                        lambda: setattr(self, "selected_2", val or "")
                    ),
                ),
                SizedBox(height=8),
                Text(f"Selected: {self.selected_2}", style=TextStyle(fontSize=12)),
            ],
        )


class _DropdownMenuStyleDemo(StatefulWidget):
    def createState(self):
        return _DropdownMenuStyleDemoState()


class _DropdownMenuStyleDemoState(State[_DropdownMenuStyleDemo]):
    def initState(self):
        self.selected = ""

    def build(self, context):
        entries = [
            DropdownMenuEntry(value="1", label="One"),
            DropdownMenuEntry(value="2", label="Two"),
            DropdownMenuEntry(value="3", label="Three"),
            DropdownMenuEntry(value="100", label="Hundred"),
        ]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                DropdownMenu(
                    width=280.0,
                    hintText="Number input",
                    keyboardType=TextInputType.number,
                    menuStyle=MenuStyle(
                        backgroundColor=WidgetStatePropertyAll(Color(0xFFE1F5FE)),
                    ),
                    dropdownMenuEntries=entries,
                    onSelected=lambda val: self.setState(
                        lambda: setattr(self, "selected", val or "")
                    ),
                ),
                SizedBox(height=8),
                Text(f"Selected: {self.selected}", style=TextStyle(fontSize=12)),
            ],
        )


class _DropdownSelectOnlyDemo(StatefulWidget):
    def createState(self):
        return _DropdownSelectOnlyDemoState()


class _DropdownSelectOnlyDemoState(State[_DropdownSelectOnlyDemo]):
    def initState(self):
        self.selected_1 = ""
        self.selected_2 = ""

    def build(self, context):
        entries = [
            DropdownMenuEntry(value="Red", label="Red"),
            DropdownMenuEntry(value="Green", label="Green"),
            DropdownMenuEntry(value="Blue", label="Blue"),
        ]
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Text(
                    "selectOnly=True (pick only, no typing):",
                    style=TextStyle(fontSize=13),
                ),
                SizedBox(height=4),
                DropdownMenu(
                    width=250.0,
                    hintText="Select only",
                    selectOnly=True,
                    dropdownMenuEntries=entries,
                    onSelected=lambda val: self.setState(
                        lambda: setattr(self, "selected_1", val or "")
                    ),
                ),
                SizedBox(height=8),
                Text(f"Selected: {self.selected_1}", style=TextStyle(fontSize=12)),
                SizedBox(height=16),
                Text("alignmentOffset=Offset(0, -50):", style=TextStyle(fontSize=13)),
                SizedBox(height=4),
                DropdownMenu(
                    width=250.0,
                    hintText="Shifted menu",
                    alignmentOffset=Offset(0, -50),
                    dropdownMenuEntries=entries,
                    onSelected=lambda val: self.setState(
                        lambda: setattr(self, "selected_2", val or "")
                    ),
                ),
                SizedBox(height=8),
                Text(f"Selected: {self.selected_2}", style=TextStyle(fontSize=12)),
            ],
        )


class FormPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Form",
            description=(
                "Demonstrates collecting and validating user input, managing field "
                "state, and coordinating save, reset, submission, and "
                "controller-driven updates."
            ),
            children=[
                SplitViewTile(
                    title="Form & TextFormField",
                    description=(
                        "A Form widget with three TextFormField inputs demonstrating "
                        "inline validation (onUserInteraction), onSaved callbacks, and "
                        "programmatic validate/save/reset via GlobalKey."
                    ),
                    instruction=(
                        "Fill in the Name and Email fields (required) and optionally Age. "
                        "Click 'Validate & Save' to trigger validation and see saved values. "
                        "Click 'Reset' to clear all fields and status."
                    ),
                    visible=_FormDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "form_key = GlobalKey()\n\n"
                            "Form(\n"
                            "    key=form_key,\n"
                            "    autovalidateMode=AutovalidateMode.onUserInteraction,\n"
                            "    child=Column(children=[\n"
                            "        TextFormField(\n"
                            "            decoration=InputDecoration(hintText='Name'),\n"
                            "            validator=validate_name,\n"
                            "            onSaved=lambda v: saved.update({'name': v}),\n"
                            "        ),\n"
                            "    ]),\n"
                            ")\n\n"
                            "form_state = form_key.currentState\n"
                            "if form_state.validate():\n"
                            "    form_state.save()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FormFieldState",
                    description=(
                        "GlobalKey on individual TextFormFields gives access to "
                        "FormFieldState. Call validate() or reset() on a single field "
                        "independently of the entire form."
                    ),
                    instruction=(
                        "Leave fields empty and click Validate to see per-field errors. "
                        "Click Reset to clear the error on that specific field only. "
                        "Each field is controlled independently via its own GlobalKey."
                    ),
                    visible=_FormFieldStateDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "field_key = GlobalKey()\n"
                            "\n"
                            "TextFormField(\n"
                            "    key=field_key,\n"
                            "    validator=validate_not_empty,\n"
                            ")\n"
                            "\n"
                            "state = field_key.currentState\n"
                            "state.validate()\n"
                            "state.reset()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="AutovalidateMode Comparison",
                    description=(
                        "Three TextFormFields side by side with different "
                        "AutovalidateMode values: disabled (no auto-validation), "
                        "always (validates immediately), and onUserInteraction "
                        "(validates after the user types)."
                    ),
                    instruction=(
                        "Type in each field with the same short input. The 'always' field "
                        "shows errors immediately on render. The 'onUserInteraction' field "
                        "shows errors only after you type. The 'disabled' field never "
                        "auto-validates."
                    ),
                    visible=_AutovalidateModeComparisonDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "TextFormField(\n"
                            "    validator=validate,\n"
                            "    autovalidateMode=AutovalidateMode.disabled,\n"
                            ")\n"
                            "\n"
                            "TextFormField(\n"
                            "    validator=validate,\n"
                            "    autovalidateMode=AutovalidateMode.always,\n"
                            ")\n"
                            "\n"
                            "TextFormField(\n"
                            "    validator=validate,\n"
                            "    autovalidateMode=AutovalidateMode.onUserInteraction,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
