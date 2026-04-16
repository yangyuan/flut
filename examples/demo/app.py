import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from flut import run_app
from flut.flutter.widgets import StatelessWidget, StatefulWidget, State, Text, Center, Column, Icon
from flut.flutter.material import MaterialApp, Scaffold, AppBar, FloatingActionButton, Icons, ThemeData, ColorScheme, Colors, Theme
from flut.flutter.rendering import MainAxisAlignment


class MyApp(StatelessWidget):
    def build(self, context):
        return MaterialApp(
            title="Flut Demo",
            theme=ThemeData(
                colorScheme=ColorScheme.fromSeed(seedColor=Colors.deepPurple),
            ),
            home=MyHomePage(title="Flut Demo Home Page"),
        )


class MyHomePage(StatefulWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title

    def createState(self):
        return _MyHomePageState()


class _MyHomePageState(State[MyHomePage]):
    def initState(self):
        self._counter = 0

    def _incrementCounter(self):
        def _update():
            self._counter += 1

        self.setState(_update)

    def build(self, context):
        return Scaffold(
            appBar=AppBar(
                title=Text(self.widget.title),
                backgroundColor=Theme.of(context).colorScheme.inversePrimary,
            ),
            body=Center(
                child=Column(
                    mainAxisAlignment=MainAxisAlignment.center,
                    children=[
                        Text("You have pushed the button this many times:"),
                        Text(
                            f"{self._counter}",
                            style=Theme.of(context).textTheme.headlineMedium,
                        ),
                    ],
                ),
            ),
            floatingActionButton=FloatingActionButton(
                onPressed=self._incrementCounter,
                tooltip="Increment",
                child=Icon(Icons.add),
            ),
        )


if __name__ == "__main__":
    run_app(MyApp())