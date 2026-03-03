from flut.dart import Brightness, Color
from flut.flutter.widgets import (
    StatelessWidget,
    StatefulWidget,
    State,
    Column,
    Row,
    Container,
    ConstrainedBox,
    Expanded,
    SizedBox,
    Text,
    LayoutBuilder,
    Wrap,
    Icon,
    MouseRegion,
    Opacity,
)
from flut.flutter.rendering import (
    BoxConstraints,
    CrossAxisAlignment,
    WrapCrossAlignment,
    MainAxisSize,
)
from flut.flutter.material import Colors, Theme, Icons, IconButton
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    Border,
    BorderRadius,
    BorderSide,
    BoxDecoration,
    EdgeInsets,
    TextStyle,
    Axis,
)
from flut.flutter.services import Clipboard, ClipboardData


class _TileHeader(StatefulWidget):
    def __init__(self, *, title=None, description=None, key=None):
        super().__init__(key=key)
        self.title = title
        self.description = description

    def createState(self):
        return _TileHeaderState()


class _TileHeaderState(State["_TileHeader"]):
    def initState(self):
        self.is_hovering = False

    def _on_enter(self, event):
        self.setState(lambda: setattr(self, "is_hovering", True))

    def _on_exit(self, event):
        self.setState(lambda: setattr(self, "is_hovering", False))

    def _copy_title(self):
        if self.widget.title:
            Clipboard.setData(ClipboardData(text=self.widget.title))

    def build(self, context):
        children = []
        if self.widget.title:
            title_row_children = [
                Text(
                    self.widget.title,
                    style=TextStyle(fontSize=16, fontWeight=FontWeight.bold),
                ),
                SizedBox(width=4),
                Opacity(
                    opacity=1.0 if self.is_hovering else 0.0,
                    child=IconButton(
                        icon=Icon(Icons.content_copy, size=14.0),
                        onPressed=self._copy_title,
                        splashRadius=14.0,
                        constraints=BoxConstraints(minWidth=28.0, minHeight=28.0),
                        padding=EdgeInsets.all(4),
                    ),
                ),
            ]
            children.append(
                MouseRegion(
                    onEnter=self._on_enter,
                    onExit=self._on_exit,
                    child=Row(
                        mainAxisSize=MainAxisSize.min,
                        children=title_row_children,
                    ),
                ),
            )
        if self.widget.description:
            children.extend(
                [
                    SizedBox(height=4),
                    Text(
                        self.widget.description,
                        style=TextStyle(fontSize=13, color=Colors.grey),
                    ),
                ]
            )
        children.append(SizedBox(height=12))
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=children,
        )


class _TileSectionDivider(StatelessWidget):
    def __init__(self, *, key=None):
        super().__init__(key=key)

    def build(self, context):
        return SizedBox(height=16)


class CatalogTile(StatelessWidget):
    def __init__(self, *, title=None, description=None, key=None):
        super().__init__(key=key)
        self.title = title
        self.description = description


class CinemaTile(CatalogTile):
    def __init__(self, *, title=None, description=None, child, key=None):
        super().__init__(title=title, description=description, key=key)
        self.child = child

    def build(self, context):
        children = []
        if self.title or self.description:
            children.append(_TileHeader(title=self.title, description=self.description))
        children.append(Expanded(child=self.child))
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=children,
        )


class WideViewTile(CatalogTile):
    def __init__(
        self,
        *,
        title=None,
        description=None,
        visible=None,
        instruction=None,
        code=None,
        log=None,
        key=None,
    ):
        super().__init__(title=title, description=description, key=key)
        self.visible = visible
        self.instruction = instruction
        self.code = code
        self.log = log

    def build(self, context):
        children = []
        if self.title:
            children.append(_TileHeader(title=self.title, description=self.description))
        if self.visible is not None:
            children.append(self.visible)
            children.append(_TileSectionDivider())
        if self.instruction is not None:
            children.append(
                Text(
                    self.instruction,
                    style=TextStyle(fontSize=13, color=Colors.blueGrey),
                )
            )
            children.append(_TileSectionDivider())
        if self.log is not None:
            children.append(self.log)
            children.append(_TileSectionDivider())
        if self.code is not None:
            children.append(self.code)

        return Container(
            width=800.0,
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=children,
            ),
        )


class SplitViewTile(CatalogTile):
    def __init__(
        self,
        *,
        title,
        description=None,
        visible=None,
        instruction=None,
        code=None,
        log=None,
        key=None,
    ):
        super().__init__(title=title, description=description, key=key)
        self.visible = visible
        self.instruction = instruction
        self.code = code
        self.log = log

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark
        divider_color = Color(0xFF333333) if is_dark else Color(0xFFE0E0E0)

        left_children = []
        if self.visible is not None:
            left_children.append(self.visible)
        if self.code is not None:
            if left_children:
                left_children.append(_TileSectionDivider())
            left_children.append(self.code)
        if not left_children:
            left_children.append(SizedBox(height=0))

        left = Container(
            width=400.0,
            padding=EdgeInsets.only(right=20),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=left_children,
            ),
        )

        right_children = []
        if self.instruction is not None:
            right_children.append(
                Text(
                    self.instruction,
                    style=TextStyle(fontSize=13, color=Colors.blueGrey),
                )
            )
        if self.log is not None:
            if right_children:
                right_children.append(_TileSectionDivider())
            right_children.append(self.log)
        if not right_children:
            right_children.append(SizedBox(height=0))

        right = Container(
            padding=EdgeInsets.only(left=20),
            decoration=BoxDecoration(
                border=Border(
                    left=BorderSide(color=divider_color, width=1),
                ),
            ),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=right_children,
            ),
        )

        return Container(
            constraints=BoxConstraints(maxWidth=800.0),
            child=Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[
                    _TileHeader(title=self.title, description=self.description),
                    LayoutBuilder(
                        builder=lambda context, constraints: Wrap(
                            crossAxisAlignment=WrapCrossAlignment.start,
                            children=[
                                left,
                                Container(
                                    width=max(200.0, constraints.maxWidth - 400.0),
                                    child=right,
                                ),
                            ],
                        )
                    ),
                ],
            ),
        )
