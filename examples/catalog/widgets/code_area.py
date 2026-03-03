import re

from utils import CODE_FONT_FAMILY
from flut.dart import Brightness, Color
from flut.flutter.widgets import (
    StatelessWidget,
    Column,
    Container,
    SizedBox,
    Text,
    TextEditingController,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    InputBorder,
    InputDecoration,
    SelectableText,
    TextField,
    Theme,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Border,
    BorderRadius,
    BoxDecoration,
    EdgeInsets,
    TextSpan,
    TextStyle,
)

_DARK_COLORS = {
    "keyword_decl": Color(0xFF569CD6),
    "keyword": Color(0xFFC586C0),
    "builtin_func": Color(0xFFDCDCAA),
    "builtin_type": Color(0xFF4EC9B0),
    "string": Color(0xFFCE9178),
    "number": Color(0xFFB5CEA8),
    "comment": Color(0xFF6A9955),
    "class_name": Color(0xFF4EC9B0),
    "func_name": Color(0xFFDCDCAA),
    "bracket": Color(0xFFFFD700),
    "text": Color(0xFFD4D4D4),
    "background": Color(0xFF1E1E1E),
    "border": Color(0xFF333333),
}

_LIGHT_COLORS = {
    "keyword_decl": Color(0xFF0000FF),
    "keyword": Color(0xFFAF00DB),
    "builtin_func": Color(0xFF795E26),
    "builtin_type": Color(0xFF267F99),
    "string": Color(0xFFA31515),
    "number": Color(0xFF098658),
    "comment": Color(0xFF008000),
    "class_name": Color(0xFF267F99),
    "func_name": Color(0xFF795E26),
    "bracket": Color(0xFFAF6E04),
    "text": Color(0xFF1E1E1E),
    "background": Color(0xFFF8F8F8),
    "border": Color(0xFFE0E0E0),
}


def get_code_colors(is_dark: bool) -> dict:
    return _DARK_COLORS if is_dark else _LIGHT_COLORS


PYTHON_KEYWORDS_DECL = {
    "class",
    "def",
    "nonlocal",
    "global",
    "True",
    "False",
    "None",
}

PYTHON_KEYWORDS = {
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "continue",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
}

_BRACKETS = set("()[]{}")

BUILTIN_FUNCTIONS = {
    "print",
    "len",
    "range",
    "enumerate",
    "zip",
    "map",
    "filter",
    "sorted",
    "reversed",
    "isinstance",
}

BUILTIN_TYPES = {
    "super",
    "self",
    "int",
    "str",
    "float",
    "list",
    "dict",
    "set",
    "tuple",
    "bool",
    "type",
}

_TOKEN_PATTERN = re.compile(
    r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')'  # strings
    r"|(\d+(?:\.\d+)?)"  # numbers
    r"|(@[A-Za-z_][\w.]*)"  # decorators
    r"|(\b[A-Za-z_]\w*\b)"  # identifiers
    r"|(#[^\n]*)"  # comments
    r"|(\S)"  # other chars
)


def highlight_python(text: str, *, is_dark: bool = True) -> TextSpan:
    colors = get_code_colors(is_dark)
    children = []
    last_end = 0
    expect_class_name = False
    expect_func_name = False

    for m in _TOKEN_PATTERN.finditer(text):
        if m.start() > last_end:
            children.append(TextSpan(text=text[last_end : m.start()]))

        string_tok, number_tok, decorator_tok, ident_tok, comment_tok, other_tok = (
            m.groups()
        )

        if decorator_tok:
            children.append(
                TextSpan(
                    text=decorator_tok,
                    style=TextStyle(color=colors["keyword"]),
                )
            )
        elif comment_tok:
            children.append(
                TextSpan(
                    text=comment_tok,
                    style=TextStyle(color=colors["comment"]),
                )
            )
        elif string_tok:
            children.append(
                TextSpan(
                    text=string_tok,
                    style=TextStyle(color=colors["string"]),
                )
            )
        elif number_tok:
            children.append(
                TextSpan(
                    text=number_tok,
                    style=TextStyle(color=colors["number"]),
                )
            )
        elif ident_tok:
            if expect_class_name:
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["class_name"]),
                    )
                )
                expect_class_name = False
            elif expect_func_name:
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["func_name"]),
                    )
                )
                expect_func_name = False
            elif ident_tok in PYTHON_KEYWORDS_DECL:
                if ident_tok == "class":
                    expect_class_name = True
                elif ident_tok == "def":
                    expect_func_name = True
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["keyword_decl"]),
                    )
                )
            elif ident_tok in PYTHON_KEYWORDS:
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["keyword"]),
                    )
                )
            elif ident_tok in BUILTIN_FUNCTIONS:
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["builtin_func"]),
                    )
                )
            elif ident_tok in BUILTIN_TYPES:
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["builtin_type"]),
                    )
                )
            elif ident_tok[0].isupper() and not ident_tok.isupper():
                children.append(
                    TextSpan(
                        text=ident_tok,
                        style=TextStyle(color=colors["class_name"]),
                    )
                )
            else:
                children.append(TextSpan(text=ident_tok))
        else:
            if other_tok in _BRACKETS:
                children.append(
                    TextSpan(
                        text=other_tok,
                        style=TextStyle(color=colors["bracket"]),
                    )
                )
            else:
                children.append(TextSpan(text=other_tok))

        last_end = m.end()

    if last_end < len(text):
        children.append(TextSpan(text=text[last_end:]))

    if not children:
        children.append(TextSpan(text=""))

    return TextSpan(children=children)


class _HighlightController(TextEditingController):
    def __init__(self, *, text, is_dark=True):
        self._is_dark = is_dark
        super().__init__(text=text)

    def buildTextSpan(self, *, context, style, withComposing):
        span = highlight_python(self.text, is_dark=self._is_dark)
        return TextSpan(style=style, children=[span])


class CodeArea(StatelessWidget):
    def __init__(self, *, code, title=None, language="python", key=None):
        super().__init__(key=key)
        self.code = code
        self.title = title
        self.language = language

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark
        colors = get_code_colors(is_dark)
        base_style = TextStyle(
            fontFamily=CODE_FONT_FAMILY,
            fontSize=13,
            color=colors["text"],
            height=1.5,
        )

        if self.language == "python":
            controller = _HighlightController(
                text=self.code,
                is_dark=is_dark,
            )
            code_widget = TextField(
                controller=controller,
                readOnly=True,
                maxLines=None,
                style=base_style,
                decoration=InputDecoration(border=InputBorder.none),
            )
        else:
            code_widget = SelectableText(
                self.code,
                style=base_style,
            )

        code_container = Container(
            width=800.0,
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=colors["background"],
                borderRadius=BorderRadius.circular(6),
                border=Border.all(color=colors["border"]),
            ),
            child=code_widget,
        )

        if self.title:
            return Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    Text(
                        self.title,
                        style=TextStyle(
                            fontSize=14,
                            fontWeight=FontWeight.bold,
                        ),
                    ),
                    SizedBox(height=8),
                    code_container,
                ],
            )

        return code_container
