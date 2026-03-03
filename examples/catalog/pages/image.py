import base64

from flut.dart import FilterQuality
from flut.dart.typed_data import Uint8List
from flut.dart.ui import Color
from flut.flutter.material import (
    ButtonStyle,
    Colors,
    ElevatedButton,
    InputDecoration,
    TextField,
    Theme,
)
from flut.flutter.painting import (
    Border,
    BorderRadius,
    BoxDecoration,
    BoxFit,
    EdgeInsets,
    ImageRepeat,
    TextStyle,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisAlignment
from flut.flutter.widgets import (
    Center,
    Column,
    Container,
    Image,
    Padding,
    Row,
    SizedBox,
    State,
    StatefulWidget,
    StatelessWidget,
    Text,
    TextEditingController,
    WidgetStatePropertyAll,
    Wrap,
)
from widgets import CatalogPage, CodeArea, SplitViewTile


class _ImageRepeatDemo(StatefulWidget):
    def createState(self):
        return _ImageRepeatDemoState()


class _ImageRepeatDemoState(State["_ImageRepeatDemo"]):
    def initState(self):
        self.repeat_idx = 0

    def build(self, context):
        repeats = [
            ("repeat", ImageRepeat.repeat),
            ("repeatX", ImageRepeat.repeatX),
            ("repeatY", ImageRepeat.repeatY),
            ("noRepeat", ImageRepeat.noRepeat),
        ]
        name, repeat_val = repeats[self.repeat_idx]
        buttons = []
        for i, (lbl, _) in enumerate(repeats):
            is_sel = i == self.repeat_idx
            buttons.append(
                ElevatedButton(
                    child=Text(
                        lbl,
                        style=TextStyle(
                            fontSize=11, color=Colors.white if is_sel else Colors.black
                        ),
                    ),
                    style=ButtonStyle(
                        backgroundColor=WidgetStatePropertyAll(
                            Colors.blue if is_sel else Color(0xFFE0E0E0)
                        )
                    ),
                    onPressed=lambda idx=i: self.setState(
                        lambda: setattr(self, "repeat_idx", idx)
                    ),
                ),
            )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(spacing=8, runSpacing=4, children=buttons),
                SizedBox(height=8),
                Container(
                    width=200.0,
                    height=200.0,
                    decoration=BoxDecoration(
                        border=Border.all(color=Colors.grey, width=1.0)
                    ),
                    child=Image.network(
                        FLUTTER_LOGO_URL,
                        repeat=repeat_val,
                        width=200.0,
                        height=200.0,
                        cacheWidth=40,
                    ),
                ),
                SizedBox(height=4),
                Text(f"ImageRepeat.{name}", style=TextStyle(fontSize=12)),
            ],
        )


class _FilterQualityDemo(StatelessWidget):
    def build(self, context):
        qualities = [
            ("none", FilterQuality.none),
            ("low", FilterQuality.low),
            ("medium", FilterQuality.medium),
            ("high", FilterQuality.high),
        ]
        children = []
        for i, (name, fq) in enumerate(qualities):
            if i > 0:
                children.append(SizedBox(width=12))
            children.append(
                Column(
                    children=[
                        Container(
                            width=80.0,
                            height=80.0,
                            decoration=BoxDecoration(
                                border=Border.all(color=Colors.grey, width=1.0)
                            ),
                            child=Image.network(
                                FLUTTER_LOGO_URL,
                                width=80.0,
                                height=80.0,
                                fit=BoxFit.fill,
                                filterQuality=fq,
                                cacheWidth=20,
                            ),
                        ),
                        SizedBox(height=4),
                        Text(name, style=TextStyle(fontSize=11)),
                    ],
                ),
            )
        return Row(crossAxisAlignment=CrossAxisAlignment.start, children=children)


FLUTTER_LOGO_URL = (
    "https://storage.googleapis.com/cms-storage-bucket/c823e53b3a1a7b0d36a9.png"
)


class _NetworkImageDemo(StatelessWidget):
    def build(self, context):
        scheme = Theme.of(context).colorScheme
        return Container(
            decoration=BoxDecoration(
                color=Color(0xFFF5F5F5),
                borderRadius=BorderRadius.circular(12),
            ),
            child=Padding(
                padding=EdgeInsets.all(16),
                child=Center(
                    child=Image.network(
                        FLUTTER_LOGO_URL,
                        width=300,
                        fit=BoxFit.contain,
                    ),
                ),
            ),
        )


class _FittedImagesDemo(StatelessWidget):
    def build(self, context):
        scheme = Theme.of(context).colorScheme
        bg = Color(0xFFF5F5F5)
        label_color = Colors.grey

        def fitted_column(label, fit):
            return Column(
                children=[
                    Text(label, style=TextStyle(fontSize=12, color=label_color)),
                    SizedBox(height=4),
                    Container(
                        width=120,
                        height=120,
                        decoration=BoxDecoration(
                            borderRadius=BorderRadius.circular(8),
                            color=bg,
                        ),
                        child=Image.network(
                            FLUTTER_LOGO_URL,
                            width=120,
                            height=120,
                            fit=fit,
                        ),
                    ),
                ],
            )

        return Row(
            mainAxisAlignment=MainAxisAlignment.spaceEvenly,
            children=[
                fitted_column("BoxFit.cover", BoxFit.cover),
                fitted_column("BoxFit.contain", BoxFit.contain),
                fitted_column("BoxFit.fill", BoxFit.fill),
            ],
        )


class _Base64ImageDemo(StatefulWidget):
    def createState(self):
        return _Base64ImageDemoState()


class _Base64ImageDemoState(State[_Base64ImageDemo]):
    def initState(self):
        self.base64_controller = TextEditingController()
        self.image_bytes = None
        self.error_text = None

    def _render_image(self):
        text = self.base64_controller.text.strip()
        if not text:
            self.setState(
                lambda: setattr(self, "error_text", "Please enter a base64 string.")
            )
            return
        try:
            decoded = base64.b64decode(text)
            self.setState(
                lambda: (
                    setattr(self, "image_bytes", Uint8List(decoded)),
                    setattr(self, "error_text", None),
                )
            )
        except Exception:
            self.setState(
                lambda: (
                    setattr(self, "image_bytes", None),
                    setattr(self, "error_text", "Invalid base64 string."),
                )
            )

    def build(self, context):
        scheme = Theme.of(context).colorScheme
        children = [
            Container(
                width=500.0,
                child=TextField(
                    controller=self.base64_controller,
                    decoration=InputDecoration(
                        hintText="Paste base64 string here...",
                    ),
                    maxLines=6,
                    minLines=3,
                ),
            ),
            SizedBox(height=12),
            ElevatedButton(
                child=Text("Render Image"),
                onPressed=lambda: self._render_image(),
            ),
        ]
        if self.error_text is not None:
            children.append(SizedBox(height=8))
            children.append(
                Text(
                    self.error_text,
                    style=TextStyle(fontSize=13, color=scheme.error),
                )
            )
        if self.image_bytes is not None:
            children.append(SizedBox(height=12))
            children.append(
                Container(
                    decoration=BoxDecoration(
                        color=Color(0xFFF5F5F5),
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=Padding(
                        padding=EdgeInsets.all(16),
                        child=Center(
                            child=Image.memory(
                                self.image_bytes,
                                width=300,
                                fit=BoxFit.contain,
                            ),
                        ),
                    ),
                )
            )
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=children,
        )


class AssetPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Image",
            description=(
                "Covers image loading and presentation from different sources, "
                "with sizing, fitting, repetition, and quality settings that "
                "visibly change the result."
            ),
            children=[
                SplitViewTile(
                    title="Network Image",
                    description="Loads and displays an image from a URL using Image.network. The image is fetched asynchronously and rendered once available.",
                    instruction="The Flutter logo is loaded from a remote URL. Observe it renders with contained sizing within its container.",
                    visible=_NetworkImageDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Image.network(\n"
                            "    'https://example.com/image.png',\n"
                            "    width=300,\n"
                            "    fit=BoxFit.contain,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Sized & Fitted Images",
                    description=(
                        "BoxFit controls how an image is inscribed into a fixed-size box. "
                        "cover clips to fill the box, contain fits within bounds preserving "
                        "aspect ratio, and fill stretches to fill ignoring aspect ratio."
                    ),
                    instruction="Compare the three images side by side to see how each BoxFit mode renders the same source image differently within a 120\u00d7120 container.",
                    visible=_FittedImagesDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Image.network(\n"
                            "    url,\n"
                            "    width=120,\n"
                            "    height=120,\n"
                            "    fit=BoxFit.cover,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Image from Base64",
                    description="Decodes a base64-encoded string into raw bytes and displays the result using Image.memory. Useful for rendering embedded or dynamically generated images.",
                    instruction="Paste a valid base64-encoded image string into the text field and click Render Image. An error message appears for empty or invalid input.",
                    visible=_Base64ImageDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "decoded = base64.b64decode(text)\n"
                            "image_bytes = Uint8List(decoded)\n\n"
                            "Image.memory(\n"
                            "    image_bytes,\n"
                            "    width=300,\n"
                            "    fit=BoxFit.contain,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="ImageRepeat",
                    description="Controls how an image tiles within a fixed-size container. Repeat fills both axes, repeatX/repeatY fills one axis, noRepeat shows a single copy.",
                    instruction="Toggle between repeat modes to see the Flutter logo tile across the container.",
                    visible=_ImageRepeatDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Image.network(\n"
                            "    url,\n"
                            "    repeat=ImageRepeat.repeat,\n"
                            "    width=200.0,\n"
                            "    height=200.0,\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="FilterQuality",
                    description="A small image scaled up with four FilterQuality settings. Lower quality uses nearest-neighbor (pixelated), higher uses smoother interpolation.",
                    instruction="Compare the four scaled images side by side for quality differences.",
                    visible=_FilterQualityDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "Image.network(\n"
                            "    url,\n"
                            "    width=80.0,\n"
                            "    height=80.0,\n"
                            "    fit=BoxFit.fill,\n"
                            "    filterQuality=FilterQuality.none,\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
