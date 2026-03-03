from flut.dart import Brightness
from flut.flutter.widgets import (
    StatelessWidget,
    Column,
    Expanded,
    Padding,
    SizedBox,
    SingleChildScrollView,
    Text,
)
from flut.flutter.rendering import CrossAxisAlignment
from flut.flutter.material import Colors, Theme
from flut.flutter.painting import EdgeInsets, TextStyle
from flut.dart.ui import FontWeight

from .tiles import CatalogTile, CinemaTile


class TileFilter:
    text = ""


class CatalogPage(StatelessWidget):
    def __init__(
        self,
        *,
        title,
        description="",
        scrollable=True,
        children=None,
        key=None,
    ):
        super().__init__(key=key)
        self.title = title
        self.description = description
        self.scrollable = scrollable
        self.children = children or []

    def build(self, context):
        theme = Theme.of(context)
        is_dark = theme.brightness == Brightness.dark

        filter_text = TileFilter.text
        if filter_text:
            ft_lower = filter_text.lower()
            tiles = [
                t for t in self.children if t.title and ft_lower in t.title.lower()
            ]
        else:
            tiles = self.children

        header_children = [
            Text(
                self.title,
                style=TextStyle(fontSize=22, fontWeight=FontWeight.bold),
            ),
        ]
        if self.description:
            header_children.extend(
                [
                    SizedBox(height=4),
                    Text(
                        self.description,
                        style=TextStyle(
                            fontSize=14,
                            color=Colors.grey,
                        ),
                    ),
                ]
            )
        header_children.append(SizedBox(height=20))

        has_fullpage = len(tiles) == 1 and isinstance(tiles[0], CinemaTile)

        if has_fullpage:
            return Padding(
                padding=EdgeInsets.all(24),
                child=Column(
                    crossAxisAlignment=CrossAxisAlignment.start,
                    children=[
                        *header_children,
                        Expanded(child=tiles[0]),
                    ],
                ),
            )
        else:
            spaced_tiles = []
            for i, tile in enumerate(tiles):
                if i > 0:
                    spaced_tiles.append(SizedBox(height=32))
                spaced_tiles.append(tile)
            content = Column(
                crossAxisAlignment=CrossAxisAlignment.start,
                children=[*header_children, *spaced_tiles],
            )
            if self.scrollable:
                return SingleChildScrollView(
                    padding=EdgeInsets.all(24),
                    child=content,
                )
            else:
                return Padding(
                    padding=EdgeInsets.all(24),
                    child=content,
                )
