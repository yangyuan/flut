import asyncio
import sys

from flut.dart import Color
from flut.flutter.widgets import (
    StatefulWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    TextEditingController,
    Icon,
    Stack,
    Positioned,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import (
    Colors,
    TextField,
    InputBorder,
    InputDecoration,
    SelectableText,
    ElevatedButton,
    Icons,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    TextSpan,
    BoxDecoration,
    BorderRadius,
    Border,
)

from widgets import (
    CatalogPage,
    WideViewTile,
    CodeArea,
    CODE_FONT_FAMILY,
    highlight_python,
)


class HighlightedController(TextEditingController):
    def buildTextSpan(self, *, context, style, withComposing):
        return TextSpan(
            style=style,
            children=[highlight_python(self.text, is_dark=True)],
        )


class PythonPage(StatefulWidget):
    def createState(self):
        return PythonPageState()


class PythonPageState(State[PythonPage]):

    def initState(self):
        self.controller = HighlightedController(
            text='def hello(name):\n    print(f"Hello {name}!")\n\n# Call it\nhello("world")'
        )
        self.output = ""
        self.running = False

    async def _execute_code(self):
        if self.running:
            return
        code = self.controller.text
        self.running = True
        self.output = ""
        self.setState(lambda: None)

        try:
            proc = await asyncio.create_subprocess_exec(
                sys.executable,
                "-c",
                code,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=10)
            output = stdout.decode() if stdout else ""
            if stderr:
                output += stderr.decode()
            self.output = output if output else "(no output)"
        except asyncio.TimeoutError:
            self.output = "Error: execution timed out (10s)"
            try:
                proc.kill()
            except Exception:
                pass
        except Exception as e:
            self.output = f"Error: {e}"
        finally:
            self.running = False
            self.setState(lambda: None)

    def build(self, context):
        editor = Container(
            decoration=BoxDecoration(
                color=Color(0xFF1E1E1E),
                borderRadius=BorderRadius.circular(8),
                border=Border.all(color=Color(0xFF333333)),
            ),
            padding=EdgeInsets.all(12),
            child=Stack(
                children=[
                    TextField(
                        controller=self.controller,
                        maxLines=12,
                        style=TextStyle(
                            fontFamily=CODE_FONT_FAMILY,
                            fontSize=14,
                            color=Color(0xFFD4D4D4),
                            height=1.5,
                        ),
                        decoration=InputDecoration(
                            border=InputBorder.none,
                            hintText="Type some Python code...",
                        ),
                    ),
                    Positioned(
                        top=0,
                        right=0,
                        child=ElevatedButton(
                            onPressed=self._execute_code,
                            child=Row(
                                children=[
                                    Icon(Icons.play_arrow, size=18.0),
                                    SizedBox(width=6),
                                    Text("Running..." if self.running else "Execute"),
                                ],
                            ),
                        ),
                    ),
                ],
            ),
        )

        output_area = Container(
            width=800.0,
            padding=EdgeInsets.all(12),
            decoration=BoxDecoration(
                color=Color(0xFF1E1E1E),
                borderRadius=BorderRadius.circular(6),
                border=Border.all(color=Color(0xFF333333)),
            ),
            child=SelectableText(
                self.output if self.output else "Output will appear here...",
                style=TextStyle(
                    fontFamily=CODE_FONT_FAMILY,
                    fontSize=13,
                    color=(
                        Color(0xFF4EC9B0)
                        if self.output and not self.output.startswith("Error:")
                        else Colors.grey
                    ),
                ),
            ),
        )

        visible = Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                editor,
                SizedBox(height=12),
                output_area,
            ],
        )
        code_area = CodeArea(
            language="python",
            code=(
                "class HighlightedController(TextEditingController):\n"
                "    def buildTextSpan(self, *, context, style, withComposing):\n"
                "        return TextSpan(\n"
                "            style=style,\n"
                "            children=[highlight_python(self.text, is_dark=is_dark)],\n"
                "        )"
            ),
        )

        return CatalogPage(
            title="Python Playground",
            description=(
                "Provides an in-app Python playground where code can be edited, "
                "run, and inspected without leaving the catalog."
            ),
            children=[
                WideViewTile(
                    visible=visible,
                    code=code_area,
                ),
            ],
        )
