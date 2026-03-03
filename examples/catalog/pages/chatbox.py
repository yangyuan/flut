import asyncio
import base64
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from flut.dart import Brightness, Color
from flut.dart.typed_data import Uint8List
from flut.flutter.widgets import (
    StatefulWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Expanded,
    Flexible,
    FocusNode,
    GestureDetector,
    ClipRRect,
    Icon,
    Image,
    ListView,
    Positioned,
    Stack,
    Visibility,
    TextEditingController,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    MainAxisAlignment,
)
from flut.flutter.material import (
    CircularProgressIndicator,
    Colors,
    IconButton,
    Icons,
    InputBorder,
    InputDecoration,
    SelectableText,
    TextField,
    Theme,
)
from flut.flutter.foundation import ValueKey
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Alignment,
    Border,
    BorderRadius,
    BorderSide,
    BoxDecoration,
    EdgeInsets,
    TextStyle,
)
from flut.flutter.services import (
    KeyEvent,
    KeyDownEvent,
    LogicalKeyboardKey,
    HardwareKeyboard,
)
from flut.flutter.widgets import KeyEventResult

from widgets import CatalogPage, CinemaTile

CHAT_FONT_SIZE = 14

SAMPLE_REPLIES = [
    "That's an interesting point! Flutter's widget composition model makes it really powerful.",
    "I'd recommend using StatefulWidget when you need to manage local state that changes over time.",
    "The key insight is that widgets are just descriptions — the framework handles all the rendering.",
    "Great question! EdgeInsets.symmetric is handy when you want equal horizontal/vertical padding.",
    "You can use a ListView with reverse:true to auto-scroll to the bottom, just like this chat!",
]

IMAGE_EXTENSIONS = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}

TEXT_EXTENSIONS = {
    ".txt": "text/plain",
    ".md": "text/markdown",
}

SUPPORTED_EXTENSIONS = {**IMAGE_EXTENSIONS, **TEXT_EXTENSIONS}

_ALL_PATTERNS = " ".join(f"*{ext}" for ext in SUPPORTED_EXTENSIONS)
_FILETYPES_FILTER = [
    ("All supported files", _ALL_PATTERNS),
    ("Images", " ".join(f"*{ext}" for ext in IMAGE_EXTENSIONS)),
    ("Text files", " ".join(f"*{ext}" for ext in TEXT_EXTENSIONS)),
]


@dataclass
class Attachment:
    filename: str
    mime_type: str
    raw_bytes: bytes
    text_content: Optional[str] = None

    @property
    def is_image(self) -> bool:
        return self.mime_type.startswith("image/")


async def pick_files() -> List[Attachment]:
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    paths = filedialog.askopenfilenames(filetypes=_FILETYPES_FILTER)
    root.destroy()

    if not paths:
        return []

    results: List[Attachment] = []
    for path in paths:
        fp = Path(path)
        ext = fp.suffix.lower()
        mime = SUPPORTED_EXTENSIONS.get(ext)
        if not mime:
            continue
        raw = fp.read_bytes()
        text = (
            None if mime.startswith("image/") else raw.decode("utf-8", errors="replace")
        )
        results.append(
            Attachment(
                filename=fp.name, mime_type=mime, raw_bytes=raw, text_content=text
            )
        )
    return results


def _build_attachment_indicator(att: Attachment, on_remove, is_dark: bool):
    if att.is_image:
        leading = ClipRRect(
            borderRadius=BorderRadius.circular(4),
            child=Image.memory(
                Uint8List(att.raw_bytes),
                width=24,
                height=24,
                gaplessPlayback=True,
                excludeFromSemantics=True,
            ),
        )
    else:
        leading = Icon(Icons.description, color=Colors.blue)

    return Container(
        child=Row(
            children=[
                leading,
                SizedBox(width=8),
                Expanded(
                    child=Text(
                        att.filename,
                        style=TextStyle(
                            fontSize=12,
                            color=Color(0xFFBDBDBD) if is_dark else Color(0xFF424242),
                        ),
                    ),
                ),
                GestureDetector(
                    onTap=on_remove,
                    child=Icon(Icons.close, color=Colors.grey),
                ),
            ],
            crossAxisAlignment=CrossAxisAlignment.center,
        ),
        padding=EdgeInsets.only(left=8, top=6, right=12, bottom=6),
        decoration=BoxDecoration(
            color=Color(0xFF2D3748) if is_dark else Color(0xFFE3F2FD),
            borderRadius=BorderRadius.circular(12),
        ),
    )


def _build_bubble_image(raw_bytes: bytes, filename: str, cache_key: str, is_dark: bool):
    return Column(
        children=[
            Container(
                child=ClipRRect(
                    borderRadius=BorderRadius.circular(4),
                    child=Image.memory(
                        Uint8List(raw_bytes),
                        width=60,
                        height=60,
                        gaplessPlayback=True,
                        excludeFromSemantics=True,
                        key=ValueKey(cache_key),
                    ),
                ),
                width=72,
                height=72,
                alignment=Alignment.center,
                decoration=BoxDecoration(
                    color=Color(0xFF2D2D2D) if is_dark else Color(0xFFF5F5F5),
                    borderRadius=BorderRadius.circular(6),
                    border=Border.all(
                        width=1,
                        color=Color(0xFF404040) if is_dark else Color(0xFFE0E0E0),
                    ),
                ),
            ),
            Container(
                child=Text(
                    filename,
                    style=TextStyle(
                        fontSize=10,
                        color=Color(0xFFBDBDBD) if is_dark else Color(0xFF757575),
                    ),
                ),
                width=72,
                margin=EdgeInsets.only(bottom=6),
            ),
        ]
    )


def _build_bubble_text_file(filename: str, is_dark: bool):
    return Column(
        children=[
            Container(
                child=Icon(
                    Icons.description,
                    color=Color(0xFF42A5F5) if is_dark else Color(0xFF1565C0),
                    size=32,
                ),
                width=72,
                height=72,
                alignment=Alignment.center,
                decoration=BoxDecoration(
                    color=Color(0xFF2D2D2D) if is_dark else Color(0xFFF5F5F5),
                    borderRadius=BorderRadius.circular(6),
                    border=Border.all(
                        width=1,
                        color=Color(0xFF404040) if is_dark else Color(0xFFE0E0E0),
                    ),
                ),
            ),
            Container(
                child=Text(
                    filename,
                    style=TextStyle(
                        fontSize=10,
                        color=Color(0xFFBDBDBD) if is_dark else Color(0xFF757575),
                    ),
                ),
                width=72,
                margin=EdgeInsets.only(bottom=6),
            ),
        ]
    )


class ChatboxPage(StatefulWidget):
    def createState(self):
        return ChatboxPageState()


class ChatboxPageState(State[ChatboxPage]):

    def initState(self):
        self.input_controller = TextEditingController()
        self.input_focus_node = FocusNode(onKeyEvent=self._on_key_event)
        self.messages = [
            {
                "text": "Welcome to the Flut Chatbox demo! Type a message to try it out.",
                "is_user": False,
                "time": "now",
                "attachments": [],
            },
        ]
        self.is_thinking = False
        self.pending_attachments: List[Attachment] = []
        self._reply_index = 0

    def _on_key_event(self, event: KeyEvent):
        if not isinstance(event, KeyDownEvent):
            return KeyEventResult.ignored
        if (
            event.logicalKey == LogicalKeyboardKey.enter
            and not HardwareKeyboard.instance.isShiftPressed
        ):
            self._on_send()
            return KeyEventResult.handled
        return KeyEventResult.ignored

    def _on_send(self):
        text = self.input_controller.text
        if not text.strip() and not self.pending_attachments:
            return

        user_text = text.strip()
        timestamp = datetime.now().strftime("%H:%M:%S")

        self.input_controller.clear()
        self.messages.append(
            {
                "text": user_text,
                "is_user": True,
                "time": timestamp,
                "attachments": list(self.pending_attachments),
            }
        )
        self.pending_attachments.clear()
        self.is_thinking = True
        self.setState(lambda: None)

        asyncio.create_task(self._fake_reply())

    async def _fake_reply(self):
        await asyncio.sleep(0.8)
        reply = SAMPLE_REPLIES[self._reply_index % len(SAMPLE_REPLIES)]
        self._reply_index += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.messages.append(
            {
                "text": reply,
                "is_user": False,
                "time": timestamp,
                "attachments": [],
            }
        )
        self.is_thinking = False
        self.setState(lambda: None)

    def _on_attach(self):
        asyncio.create_task(self._do_attach())

    async def _do_attach(self):
        files = await pick_files()
        if files:
            self.pending_attachments.extend(files)
            self.setState(lambda: None)

    def _on_remove_attachment(self, index: int):
        if 0 <= index < len(self.pending_attachments):
            self.pending_attachments.pop(index)
            self.setState(lambda: None)

    def _on_reset(self):
        self.messages.clear()
        self.messages.append(
            {
                "text": "Chat cleared. Start a new conversation!",
                "is_user": False,
                "time": datetime.now().strftime("%H:%M:%S"),
                "attachments": [],
            }
        )
        self.pending_attachments.clear()
        self.is_thinking = False
        self._reply_index = 0
        self.setState(lambda: None)

    def _build_bubble(self, msg, index, is_dark):
        is_user = msg["is_user"]
        if is_dark:
            if is_user:
                bgcolor = Color(0xFF1E3A5F)
                border_color = Color(0xFF2C5282)
            else:
                bgcolor = Color(0xFF2D2D2D)
                border_color = Color(0xFF404040)
        else:
            if is_user:
                bgcolor = Color(0xFFE3F2FD)
                border_color = Color(0xFF90CAF9)
            else:
                bgcolor = Color(0xFFF5F5F5)
                border_color = Color(0xFFE0E0E0)

        align = MainAxisAlignment.end if is_user else MainAxisAlignment.start
        cross = CrossAxisAlignment.end if is_user else CrossAxisAlignment.start
        label = "You" if is_user else "Assistant"

        bubble_children = []
        for ai, att in enumerate(msg.get("attachments", [])):
            if att.is_image:
                bubble_children.append(
                    _build_bubble_image(
                        att.raw_bytes, att.filename, f"img_{index}_{ai}", is_dark
                    )
                )
            else:
                bubble_children.append(_build_bubble_text_file(att.filename, is_dark))
        if msg["text"]:
            bubble_children.append(
                SelectableText(msg["text"], style=TextStyle(fontSize=CHAT_FONT_SIZE))
            )

        content_widget = Column(children=bubble_children, crossAxisAlignment=cross)

        return Container(
            key=ValueKey(f"msg_{index}"),
            padding=EdgeInsets.only(left=12, right=14, bottom=8),
            child=Column(
                crossAxisAlignment=cross,
                children=[
                    Row(
                        mainAxisAlignment=align,
                        children=[
                            Text(
                                f"{label} · {msg['time']}",
                                style=TextStyle(fontSize=11, color=Colors.grey),
                            ),
                        ],
                    ),
                    SizedBox(height=2),
                    Row(
                        mainAxisAlignment=align,
                        children=[
                            Flexible(
                                child=Container(
                                    padding=EdgeInsets.only(
                                        left=14, top=8, right=14, bottom=8
                                    ),
                                    decoration=BoxDecoration(
                                        color=bgcolor,
                                        borderRadius=BorderRadius.circular(10),
                                        border=Border.all(width=1, color=border_color),
                                    ),
                                    child=content_widget,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark

        bubbles = [
            self._build_bubble(msg, i, is_dark) for i, msg in enumerate(self.messages)
        ]

        chat_list = ListView(
            children=list(reversed(bubbles)),
            padding=EdgeInsets.only(top=10, bottom=50 if self.is_thinking else 5),
            reverse=True,
            primary=False,
        )

        thinking_indicator = Visibility(
            visible=self.is_thinking,
            child=Container(
                padding=EdgeInsets.only(left=14, top=8, right=14, bottom=8),
                decoration=BoxDecoration(
                    color=Color(0xFF6B7280),
                    borderRadius=BorderRadius.circular(12),
                ),
                child=Row(
                    children=[
                        SizedBox(
                            width=12,
                            height=12,
                            child=CircularProgressIndicator(
                                strokeWidth=2, color=Colors.white
                            ),
                        ),
                        SizedBox(width=8),
                        Text(
                            "Thinking...",
                            style=TextStyle(fontSize=13, color=Colors.white),
                        ),
                    ]
                ),
            ),
        )

        reset_button = Container(
            child=IconButton(
                icon=Icon(Icons.refresh, color=Colors.white),
                onPressed=self._on_reset,
                iconSize=20,
            ),
            decoration=BoxDecoration(
                color=Colors.green,
                borderRadius=BorderRadius.circular(24),
            ),
        )

        chat_area = Stack(
            children=[
                Positioned(left=0, top=0, right=0, bottom=0, child=chat_list),
                Positioned(left=10, top=10, child=reset_button),
                Positioned(left=12, right=12, bottom=10, child=thinking_indicator),
            ]
        )

        if self.is_thinking:
            action_button = Container(
                child=IconButton(
                    icon=Icon(Icons.stop, color=Colors.white),
                    onPressed=self._on_stop,
                    iconSize=20,
                ),
                margin=EdgeInsets.only(bottom=4),
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(24),
                ),
            )
        else:
            action_button = Container(
                margin=EdgeInsets.only(bottom=4),
                decoration=BoxDecoration(
                    color=Colors.blue,
                    borderRadius=BorderRadius.circular(24),
                ),
                child=IconButton(
                    icon=Icon(Icons.arrow_upward, color=Colors.white),
                    onPressed=self._on_send,
                    iconSize=20,
                ),
            )

        attach_button = Container(
            child=IconButton(
                icon=Icon(Icons.attach_file, color=Colors.grey),
                onPressed=self._on_attach,
                iconSize=20,
            ),
            margin=EdgeInsets.only(bottom=4),
        )

        if is_dark:
            input_bg = Color(0xFF2D2D2D)
            input_border_color = Color(0xFF505050)
        else:
            input_bg = Colors.white
            input_border_color = Color(0xFFD9D9E3)

        input_container = Container(
            child=Row(
                children=[
                    attach_button,
                    Expanded(
                        child=TextField(
                            controller=self.input_controller,
                            focusNode=self.input_focus_node,
                            decoration=InputDecoration(
                                hintText="Type a message...",
                                border=InputBorder.none,
                            ),
                            style=TextStyle(fontSize=CHAT_FONT_SIZE),
                            maxLines=3,
                            minLines=1,
                        ),
                    ),
                    action_button,
                ],
                crossAxisAlignment=CrossAxisAlignment.end,
            ),
            decoration=BoxDecoration(
                color=input_bg,
                borderRadius=BorderRadius.circular(24),
                border=Border.all(width=1, color=input_border_color),
            ),
            padding=EdgeInsets.only(left=5, top=0, right=5, bottom=0),
        )

        input_children = []
        for i, att in enumerate(self.pending_attachments):
            idx = i
            indicator = _build_attachment_indicator(
                att,
                lambda idx=idx: self._on_remove_attachment(idx),
                is_dark=is_dark,
            )
            input_children.append(indicator)
            input_children.append(SizedBox(height=4))
        input_children.append(input_container)

        input_bar = Container(
            child=Column(children=input_children),
            padding=EdgeInsets.only(left=15, top=5, right=12, bottom=10),
        )

        chat_content = Container(
            decoration=BoxDecoration(
                borderRadius=BorderRadius.circular(12),
                border=Border.all(
                    width=1,
                    color=Color(0xFF333333) if is_dark else Color(0xFFE0E0E0),
                ),
            ),
            child=Column(
                children=[
                    Expanded(child=chat_area),
                    input_bar,
                ],
            ),
        )

        return CatalogPage(
            title="Chatbox",
            description=(
                "Presents a realistic chat surface with message composition, file "
                "attachments, keyboard behavior, auto-scrolling, and transient "
                "typing feedback."
            ),
            children=[
                CinemaTile(
                    child=chat_content,
                ),
            ],
        )

    def _on_stop(self):
        self.is_thinking = False
        self.setState(lambda: None)
