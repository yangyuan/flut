from flut.dart import Color
from flut.dart.ui import FontWeight
from flut.flutter.widgets import (
    StatelessWidget,
    Text,
    Row,
    SizedBox,
    Container,
    ListView,
)
from flut.flutter.material import Tooltip, Colors
from flut.flutter.painting import (
    BoxDecoration,
    BorderRadius,
    Border,
    Alignment,
    EdgeInsets,
    TextStyle,
)


class ReproPage(StatelessWidget):
    def build(self, context):
        return ListView(
            padding=EdgeInsets.all(24),
            children=[
                Text(
                    "Repro",
                    style=TextStyle(fontSize=22, fontWeight=FontWeight.bold),
                ),
                SizedBox(height=4),
                Text(
                    "This page is used to repro known Flutter or flut issues.",
                    style=TextStyle(fontSize=14, color=Colors.grey),
                ),
                SizedBox(height=20),
                Row(
                    children=[
                        Tooltip(
                            message="Tooltip A",
                            child=Container(
                                width=100,
                                height=100,
                                alignment=Alignment.center,
                                child=Text("A"),
                                decoration=BoxDecoration(
                                    color=Color(0xFFE3F2FD),
                                    borderRadius=BorderRadius.circular(8),
                                    border=Border.all(width=1, color=Color(0xFF90CAF9)),
                                ),
                            ),
                        ),
                        SizedBox(width=16),
                        Tooltip(
                            message="Tooltip B",
                            child=Container(
                                width=100,
                                height=100,
                                alignment=Alignment.center,
                                child=Text("B"),
                                decoration=BoxDecoration(
                                    color=Color(0xFFF5F5F5),
                                    borderRadius=BorderRadius.circular(8),
                                    border=Border.all(width=1, color=Color(0xFFE0E0E0)),
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        )
