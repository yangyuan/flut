# Flut

<img src="https://raw.githubusercontent.com/yangyuan/flut/master/flut/assets/icon.svg" width="64" height="64" alt="flut">

Bring Flutter to Python

## Overview

Flut is a Python project that brings the real Flutter widget system into the Python ecosystem. It is designed to expose Flutter's API as honestly and closely as possible.

### Common Use Cases

Flut is a good fit when you are writing a Python application and need a modern desktop UI, when your project needs to stay in the Python ecosystem, or when you want Flutter's widget model without moving your codebase to Dart.

Typical examples include:
- A Python data, automation, or AI tool that needs a polished cross-platform desktop interface.
- Students, researchers, or developers who want to quickly build a desktop proof-of-concept UI while keeping models, inference code, or data pipelines in Python.
- An internal business application whose networking, domain logic, or integrations already live in Python.
- A Python enthusiast who wants a UI application that can be installed through the familiar `pip install app` workflow.

Because Flut follows Flutter's API closely, Flutter examples and AI-generated Flutter code can often be adapted to Flut with only straightforward Python syntax changes. The reverse is also true: if you later decide to migrate to Flutter and Dart, you can retain your entire UI structure and design work.

Please take a look at the [catalog app](https://github.com/yangyuan/flut/tree/master/examples/catalog).

![Flut Catalog](https://raw.githubusercontent.com/yangyuan/flut/master/examples/catalog/screenshot.png)

### True Flutter

Flutter code maps almost 1:1 from Dart to Python.

```dart
// Flutter (Dart)
Container(
  padding: EdgeInsets.all(16),
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(8),
  ),
  child: Text('Hello'),
)
```

```python
# Flut (Python)
Container(
  padding=EdgeInsets.all(16),
  decoration=BoxDecoration(
    color=Colors.blue,
    borderRadius=BorderRadius.circular(8),
  ),
  child=Text('Hello'),
)
```

Under the hood, the real Flutter widget system is used. Because Flut closely mirrors Flutter's API, coding agents can transfer their knowledge of Flutter patterns and generate Flut code naturally.

### State-of-the-Art asyncio Integration

Flut provides a true async integration, bridging asyncio with the Flutter UI thread in a design that exactly matches Flutter. Thread safety and event loop conflicts are handled internally.

### No Performance Surprises

The majority of projects using Flut will enjoy near identical performance to Flutter. FFI between Python and Dart does bring additional communication overhead, but the cost is fixed.

## Installation

```bash
pip install flut
```

Prebuilt wheels are available for Windows (x64), macOS (x64, arm64), and Linux (x64).

Building from source is also supported and requires the Flutter SDK.

## Usage

Create a file `app.py`:

```python
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

```

Run it:

```bash
python app.py
```

![Flut Demo](https://raw.githubusercontent.com/yangyuan/flut/master/examples/demo/screenshot.png)

For async support:

```python
import asyncio
from flut import run_app_async

# ... your app code ...

if __name__ == "__main__":
    asyncio.run(run_app_async(MyApp()))
```

For a more complete example, see the [catalog app](https://github.com/yangyuan/flut/tree/master/examples/catalog).


## Flutter Parity

Flut is a project that brings Flutter to Python. Some features are not applicable in this context: whether due to platform limitations, overlap with Python's own ecosystem, being tied to the Dart development workflow, or simply due to its challanging nature. The following are out of scope, listed from lowest to highest priority for future consideration:

- **Web Support**
- **Mobile Support**
- **Plugins**
- **Flutter DevTools**
- **Isolates**
- **Platform Channels**
- **Streams/StreamBuilder**
- **Non-State Mixins**

The following are implemented with compromises:
- **InheritedWidget** Uses `visitAncestorElements` + `dependOnInheritedElement` instead of type-based lookup, resulting in O(depth) lookup vs Flutter's O(1). Negligible for typical widget trees.
- **Shortcuts / Actions** O(depth) action lookup vs Flutter's O(1). Negligible for typical widget trees.
- **showDialog** wraps the builder in a StatelessWidget proxy so the dialog's widget tree is built through the standard Dart-initiated build path, enabling callbacks in dialog children to work correctly.

## Build
```
cd flut/.flutter
flutter build windows/macos/linux --no-tree-shake-icons
```

## License

MIT

## Disclaimer

Flut is an independent project and is not endorsed by, sponsored by, or affiliated with Google LLC. Flutter is a trademark of Google LLC.