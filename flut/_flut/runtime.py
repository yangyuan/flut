from typing import Optional


def flut_unpack(data) -> Optional[object]:
    if not isinstance(data, dict):
        return None

    flut_type = data.get("_flut_type")
    if not flut_type:
        return None

    oid = data.get("_flut_oid")
    if oid is not None:
        from flut._flut.engine import FlutRealtimeObject

        existing = FlutRealtimeObject._lookup_oid(oid)
        if existing is not None:
            return existing

    match flut_type:
        case "Color":
            from flut.dart.ui import Color

            return Color._flut_unpack(data)
        case "Canvas":
            from flut.dart.ui import Canvas

            return Canvas._flut_unpack(data)
        case "BuildContext":
            from flut.flutter.widgets.framework import BuildContext

            return BuildContext._flut_unpack(data)
        case "GlobalKey":
            from flut.flutter.widgets.framework import GlobalKey

            return GlobalKey._flut_unpack(data)
        case "FormState":
            from flut.flutter.widgets.form import FormState

            return FormState._flut_unpack(data)
        case "OverlayState":
            from flut.flutter.widgets.overlay import OverlayState

            return OverlayState._flut_unpack(data)
        case "ValueNotifier":
            from flut.flutter.foundation.change_notifier import ValueNotifier

            return ValueNotifier._flut_unpack(data)
        case "RenderBox":
            from flut.flutter.rendering.box import RenderBox

            return RenderBox._flut_unpack(data)
        case "Size":
            from flut.dart.ui import _Size

            return _Size._flut_unpack(data)
        case "Offset":
            from flut.dart.ui import _Offset

            return _Offset._flut_unpack(data)
        case "Rect":
            from flut.dart.ui import Rect

            return Rect._flut_unpack(data)
        case "DragStartDetails":
            from flut.flutter.gestures.drag_details import DragStartDetails

            return DragStartDetails._flut_unpack(data)
        case "DragUpdateDetails":
            from flut.flutter.gestures.drag_details import DragUpdateDetails

            return DragUpdateDetails._flut_unpack(data)
        case "DragEndDetails":
            from flut.flutter.gestures.drag_details import DragEndDetails

            return DragEndDetails._flut_unpack(data)
        case "DragDownDetails":
            from flut.flutter.gestures.drag_details import DragDownDetails

            return DragDownDetails._flut_unpack(data)
        case "LongPressStartDetails":
            from flut.flutter.gestures.long_press import LongPressStartDetails

            return LongPressStartDetails._flut_unpack(data)
        case "LongPressMoveUpdateDetails":
            from flut.flutter.gestures.long_press import LongPressMoveUpdateDetails

            return LongPressMoveUpdateDetails._flut_unpack(data)
        case "LongPressEndDetails":
            from flut.flutter.gestures.long_press import LongPressEndDetails

            return LongPressEndDetails._flut_unpack(data)
        case "TapDownDetails":
            from flut.flutter.gestures.tap import TapDownDetails

            return TapDownDetails._flut_unpack(data)
        case "TapUpDetails":
            from flut.flutter.gestures.tap import TapUpDetails

            return TapUpDetails._flut_unpack(data)
        case "ScaleStartDetails":
            from flut.flutter.gestures.scale import ScaleStartDetails

            return ScaleStartDetails._flut_unpack(data)
        case "ScaleUpdateDetails":
            from flut.flutter.gestures.scale import ScaleUpdateDetails

            return ScaleUpdateDetails._flut_unpack(data)
        case "ScaleEndDetails":
            from flut.flutter.gestures.scale import ScaleEndDetails

            return ScaleEndDetails._flut_unpack(data)
        case "DraggableDetails":
            from flut.flutter.widgets.drag_target import DraggableDetails

            return DraggableDetails._flut_unpack(data)
        case "DragTargetDetails":
            from flut.flutter.widgets.drag_target import DragTargetDetails

            return DragTargetDetails._flut_unpack(data)
        case "PointerEvent":
            from flut.flutter.gestures.events import PointerEvent

            return PointerEvent._flut_unpack(data)
        case "PointerEnterEvent":
            from flut.flutter.gestures.events import PointerEnterEvent

            return PointerEnterEvent._flut_unpack(data)
        case "PointerExitEvent":
            from flut.flutter.gestures.events import PointerExitEvent

            return PointerExitEvent._flut_unpack(data)
        case "Velocity":
            from flut.flutter.gestures.velocity_tracker import Velocity

            return Velocity._flut_unpack(data)
        case "DropdownMenuEntry":
            from flut.flutter.material.dropdown_menu import DropdownMenuEntry

            return DropdownMenuEntry._flut_unpack(data)
        case "ScrollMetrics":
            from flut.flutter.widgets.scroll_metrics import ScrollMetrics

            return ScrollMetrics._flut_unpack(data)
        case "ScrollNotification":
            from flut.flutter.widgets.scroll_notification import ScrollNotification

            return ScrollNotification._flut_unpack(data)
        case "ScrollStartNotification":
            from flut.flutter.widgets.scroll_notification import ScrollStartNotification

            return ScrollStartNotification._flut_unpack(data)
        case "ScrollUpdateNotification":
            from flut.flutter.widgets.scroll_notification import (
                ScrollUpdateNotification,
            )

            return ScrollUpdateNotification._flut_unpack(data)
        case "ScrollEndNotification":
            from flut.flutter.widgets.scroll_notification import ScrollEndNotification

            return ScrollEndNotification._flut_unpack(data)
        case "OverscrollNotification":
            from flut.flutter.widgets.scroll_notification import OverscrollNotification

            return OverscrollNotification._flut_unpack(data)
        case "AxisDirection":
            from flut.flutter.painting.basic_types import AxisDirection

            return AxisDirection._flut_unpack(data)
        case "KeyDownEvent":
            from flut.flutter.services.hardware_keyboard import KeyDownEvent

            return KeyDownEvent._flut_unpack(data)
        case "KeyUpEvent":
            from flut.flutter.services.hardware_keyboard import KeyUpEvent

            return KeyUpEvent._flut_unpack(data)
        case "KeyRepeatEvent":
            from flut.flutter.services.hardware_keyboard import KeyRepeatEvent

            return KeyRepeatEvent._flut_unpack(data)
        case "KeyEvent":
            from flut.flutter.services.hardware_keyboard import KeyEvent

            return KeyEvent._flut_unpack(data)
        case "ClipboardData":
            from flut.flutter.services.clipboard import ClipboardData

            return ClipboardData._flut_unpack(data)
        case "LogicalKeyboardKey":
            from flut.flutter.services.keyboard_key import _LogicalKeyboardKey

            return _LogicalKeyboardKey._flut_unpack(data)
        case "PhysicalKeyboardKey":
            from flut.flutter.services.keyboard_key import _PhysicalKeyboardKey

            return _PhysicalKeyboardKey._flut_unpack(data)
        case "Duration":
            from flut.dart.core import _Duration

            return _Duration._flut_unpack(data)
        case "EdgeInsets":
            from flut.flutter.painting.edge_insets import EdgeInsets

            return EdgeInsets._flut_unpack(data)
        case "ColorScheme":
            from flut.flutter.material.color_scheme import ColorScheme

            return ColorScheme._flut_unpack(data)
        case "Brightness":
            from flut.dart.ui import Brightness

            return Brightness._flut_unpack(data)
        case "Clip":
            from flut.dart.ui import Clip

            return Clip._flut_unpack(data)
        case "ColorSpace":
            from flut.dart.ui import ColorSpace

            return ColorSpace._flut_unpack(data)
        case "PointerDeviceKind":
            from flut.dart.ui import PointerDeviceKind

            return PointerDeviceKind._flut_unpack(data)
        case "Matrix4":
            from flut.dart._dart import Matrix4

            return Matrix4._flut_unpack(data)
        case "ThemeData":
            from flut.flutter.material.theme_data import ThemeData

            return ThemeData._flut_unpack(data)
        case "TextTheme":
            from flut.flutter.material.text_theme import TextTheme

            return TextTheme._flut_unpack(data)
        case "TextStyle":
            from flut.flutter.painting.text_style import TextStyle

            return TextStyle._flut_unpack(data)
        case "FontWeight":
            from flut.dart.ui import _FontWeight

            return _FontWeight._flut_unpack(data)
        case "MediaQueryData":
            from flut.flutter.widgets.media_query import MediaQueryData

            return MediaQueryData._flut_unpack(data)
        case "NavigationMode":
            from flut.flutter.widgets.media_query import NavigationMode

            return NavigationMode._flut_unpack(data)
        case "DeviceGestureSettings":
            from flut.flutter.gestures.gesture_settings import DeviceGestureSettings

            return DeviceGestureSettings._flut_unpack(data)
        case "TextScaler":
            from flut.flutter.painting.text_scaler import _TextScaler

            return _TextScaler._flut_unpack(data)
        case "HardwareKeyboard":
            from flut.flutter.services.hardware_keyboard import HardwareKeyboard

            return HardwareKeyboard._flut_unpack(data)
        case "SchedulerBinding":
            from flut.flutter.scheduler.binding import SchedulerBinding

            return SchedulerBinding._flut_unpack(data)
        case "RouteSettings":
            from flut.flutter.widgets.navigator import RouteSettings

            return RouteSettings._flut_unpack(data)
        case "ModalRoute":
            from flut.flutter.widgets.routes import ModalRoute

            return ModalRoute._flut_unpack(data)
        case "PageRoute":
            from flut.flutter.widgets.pages import PageRoute

            return PageRoute._flut_unpack(data)
        case "MaterialPageRoute":
            from flut.flutter.material.page import MaterialPageRoute

            return MaterialPageRoute._flut_unpack(data)
        case "ValueKey":
            from flut.flutter.foundation.key import ValueKey

            return ValueKey._flut_unpack(data)
        case "UniqueKey":
            from flut.flutter.foundation.key import UniqueKey

            return UniqueKey._flut_unpack(data)
        case "WidgetState":
            from flut.flutter.widgets.widget_state import _WidgetState

            return _WidgetState._flut_unpack(data)
        case "WidgetStateColor":
            from flut.flutter.widgets.widget_state import WidgetStateColor

            return WidgetStateColor._flut_unpack(data)
        case "ScrollPosition":
            from flut.flutter.widgets.scroll_position import ScrollPosition

            return ScrollPosition._flut_unpack(data)
        case "TextEditingController":
            from flut.flutter.widgets.editable_text import TextEditingController

            return TextEditingController._flut_unpack(data)
        case "ScrollController":
            from flut.flutter.widgets.scroll_controller import ScrollController

            return ScrollController._flut_unpack(data)
        case "ExpansibleController":
            from flut.flutter.widgets.expansible import ExpansibleController

            return ExpansibleController._flut_unpack(data)
        case "FocusNode":
            from flut.flutter.widgets.focus_manager import FocusNode

            return FocusNode._flut_unpack(data)
        case "FocusScopeNode":
            from flut.flutter.widgets.focus_manager import FocusScopeNode

            return FocusScopeNode._flut_unpack(data)
        case "TabController":
            from flut.flutter.material.tab_controller import TabController

            return TabController._flut_unpack(data)
        case "MenuController":
            from flut.flutter.widgets.raw_menu_anchor import MenuController

            return MenuController._flut_unpack(data)
        case "RenderObject":
            from flut.flutter.rendering.object import RenderObject

            return RenderObject._flut_unpack(data)
        case "FormFieldState":
            from flut.flutter.widgets.form import FormFieldState

            return FormFieldState._flut_unpack(data)
        case "TransformationController":
            from flut.flutter.widgets.interactive_viewer import (
                TransformationController,
            )

            return TransformationController._flut_unpack(data)
        case "Alignment":
            from flut.flutter.painting.alignment import _Alignment

            return _Alignment._flut_unpack(data)
        case "AlignmentDirectional":
            from flut.flutter.painting.alignment import _AlignmentDirectional

            return _AlignmentDirectional._flut_unpack(data)
        case "BorderRadius":
            from flut.flutter.painting.border_radius import BorderRadius

            return BorderRadius._flut_unpack(data)
        case "BorderSide":
            from flut.flutter.painting.borders import _BorderSide

            return _BorderSide._flut_unpack(data)
        case "Border":
            from flut.flutter.painting.box_border import Border

            return Border._flut_unpack(data)
        case "BoxDecoration":
            from flut.flutter.painting.box_decoration import BoxDecoration

            return BoxDecoration._flut_unpack(data)
        case "TextSpan":
            from flut.flutter.painting.text_span import TextSpan

            return TextSpan._flut_unpack(data)
        case "WidgetSpan":
            from flut.flutter.widgets.widget_span import WidgetSpan

            return WidgetSpan._flut_unpack(data)
        case "IconData":
            from flut.flutter.widgets.icon_data import IconData

            return IconData._flut_unpack(data)
        case "InputDecoration":
            from flut.flutter.material.input_decorator import InputDecoration

            return InputDecoration._flut_unpack(data)
        case "InputBorder":
            from flut.flutter.material.input_border import InputBorder

            return InputBorder._flut_unpack(data)
        case "Curve":
            from flut.flutter.animation.curves import Curve

            return Curve._flut_unpack(data)
        case "AnimationStatus":
            from flut.flutter.animation.animation import AnimationStatus

            return AnimationStatus._flut_unpack(data)
        case "AnimationStyle":
            from flut.flutter.animation.animation_style import _AnimationStyle

            return _AnimationStyle._flut_unpack(data)
        case "BoxShadow":
            from flut.flutter.painting.box_shadow import BoxShadow

            return BoxShadow._flut_unpack(data)
        case "TileMode":
            from flut.dart.ui import TileMode

            return TileMode._flut_unpack(data)
        case "BlurStyle":
            from flut.dart.ui import BlurStyle

            return BlurStyle._flut_unpack(data)
        case "PaintingStyle":
            from flut.dart.ui import PaintingStyle

            return PaintingStyle._flut_unpack(data)
        case "StrokeCap":
            from flut.dart.ui import StrokeCap

            return StrokeCap._flut_unpack(data)
        case "StrokeJoin":
            from flut.dart.ui import StrokeJoin

            return StrokeJoin._flut_unpack(data)
        case "BlendMode":
            from flut.dart.ui import BlendMode

            return BlendMode._flut_unpack(data)
        case "FilterQuality":
            from flut.dart.ui import FilterQuality

            return FilterQuality._flut_unpack(data)
        case "MaskFilter":
            from flut.dart.ui import MaskFilter

            return MaskFilter._flut_unpack(data)
        case "ColorFilter":
            from flut.dart.ui import ColorFilter

            return ColorFilter._flut_unpack(data)
        case "ImageFilter":
            from flut.dart.ui import ImageFilter

            return ImageFilter._flut_unpack(data)
        case "Gradient":
            from flut.dart.ui import Gradient

            return Gradient._flut_unpack(data)
        case "LinearGradient":
            from flut.flutter.painting.gradient import LinearGradient

            return LinearGradient._flut_unpack(data)
        case "RadialGradient":
            from flut.flutter.painting.gradient import RadialGradient

            return RadialGradient._flut_unpack(data)
        case "SweepGradient":
            from flut.flutter.painting.gradient import SweepGradient

            return SweepGradient._flut_unpack(data)
        case "GradientRotation":
            from flut.flutter.painting.gradient import GradientRotation

            return GradientRotation._flut_unpack(data)
        case "AnimationController":
            from flut.flutter.animation.animation_controller import (
                AnimationController,
            )

            return AnimationController._flut_unpack(data)
        case "Paint":
            from flut.dart.ui import Paint

            return Paint._flut_unpack(data)
        case "BoxConstraints":
            from flut.flutter.rendering.box import BoxConstraints

            return BoxConstraints._flut_unpack(data)
        case "SingleActivator":
            from flut.flutter.widgets.shortcuts import SingleActivator

            return SingleActivator._flut_unpack(data)
        case "CharacterActivator":
            from flut.flutter.widgets.shortcuts import CharacterActivator

            return CharacterActivator._flut_unpack(data)
        case "Set":
            values = data.get("values", [])
            return set(
                flut_unpack(item) if isinstance(item, dict) else item for item in values
            )
        case "Uint8List":
            from flut.dart.typed_data import Uint8List

            return Uint8List._flut_unpack(data)
        case "Future":
            from flut._flut.engine import Future

            return Future._flut_unpack(data)
        case "TextBaseline":
            from flut.dart.ui import TextBaseline

            return TextBaseline._flut_unpack(data)
        case "FontStyle":
            from flut.dart.ui import FontStyle

            return FontStyle._flut_unpack(data)
        case "TextDecorationStyle":
            from flut.dart.ui import TextDecorationStyle

            return TextDecorationStyle._flut_unpack(data)
        case "TextLeadingDistribution":
            from flut.dart.ui import TextLeadingDistribution

            return TextLeadingDistribution._flut_unpack(data)
        case "TextWidthBasis":
            from flut.flutter.painting.text_painter import TextWidthBasis

            return TextWidthBasis._flut_unpack(data)
        case "BoxShape":
            from flut.flutter.painting.box_border import BoxShape

            return BoxShape._flut_unpack(data)
        case "FloatingLabelBehavior":
            from flut.flutter.material.input_decorator import FloatingLabelBehavior

            return FloatingLabelBehavior._flut_unpack(data)
        case "DragStartBehavior":
            from flut.flutter.gestures.recognizer import DragStartBehavior

            return DragStartBehavior._flut_unpack(data)
        case "MaterialTapTargetSize":
            from flut.flutter.material.theme_data import (
                MaterialTapTargetSize,
            )

            return MaterialTapTargetSize._flut_unpack(data)
        case "TargetPlatform":
            from flut.flutter.foundation.platform import TargetPlatform

            return TargetPlatform._flut_unpack(data)
        case "ImageRepeat":
            from flut.flutter.painting.decoration_image import ImageRepeat

            return ImageRepeat._flut_unpack(data)
        case "AutovalidateMode":
            from flut.flutter.widgets.form import AutovalidateMode

            return AutovalidateMode._flut_unpack(data)
        case "TraversalDirection":
            from flut.flutter.widgets.focus_traversal import TraversalDirection

            return TraversalDirection._flut_unpack(data)
        case "ThemeMode":
            from flut.flutter.material.app import ThemeMode

            return ThemeMode._flut_unpack(data)
        case "HitTestBehavior":
            from flut.flutter.rendering.proxy_box import HitTestBehavior

            return HitTestBehavior._flut_unpack(data)
        case "TraversalEdgeBehavior":
            from flut.flutter.widgets.focus_traversal import TraversalEdgeBehavior

            return TraversalEdgeBehavior._flut_unpack(data)
        case "AnimationBehavior":
            from flut.flutter.animation.animation_controller import AnimationBehavior

            return AnimationBehavior._flut_unpack(data)
        case "LockState":
            from flut.flutter.widgets.shortcuts import LockState

            return LockState._flut_unpack(data)
        case "PanAxis":
            from flut.flutter.widgets.interactive_viewer import PanAxis

            return PanAxis._flut_unpack(data)
        case "ScrollViewKeyboardDismissBehavior":
            from flut.flutter.widgets.scroll_view import (
                ScrollViewKeyboardDismissBehavior,
            )

            return ScrollViewKeyboardDismissBehavior._flut_unpack(data)
        case "VerticalDirection":
            from flut.flutter.painting.basic_types import VerticalDirection

            return VerticalDirection._flut_unpack(data)
        case "TextInputAction":
            from flut.flutter.services.text_input import TextInputAction

            return TextInputAction._flut_unpack(data)
        case "RoundedRectangleBorder":
            from flut.flutter.painting.rounded_rectangle_border import (
                RoundedRectangleBorder,
            )

            return RoundedRectangleBorder._flut_unpack(data)
        case "CircleBorder":
            from flut.flutter.painting.circle_border import CircleBorder

            return CircleBorder._flut_unpack(data)
        case "StadiumBorder":
            from flut.flutter.painting.stadium_border import StadiumBorder

            return StadiumBorder._flut_unpack(data)
        case "BeveledRectangleBorder":
            from flut.flutter.painting.beveled_rectangle_border import (
                BeveledRectangleBorder,
            )

            return BeveledRectangleBorder._flut_unpack(data)
        case "ContinuousRectangleBorder":
            from flut.flutter.painting.continuous_rectangle_border import (
                ContinuousRectangleBorder,
            )

            return ContinuousRectangleBorder._flut_unpack(data)
        case "ScrollPhysics":
            from flut.flutter.widgets.scroll_physics import ScrollPhysics

            return ScrollPhysics._flut_unpack(data)
        case "BouncingScrollPhysics":
            from flut.flutter.widgets.scroll_physics import BouncingScrollPhysics

            return BouncingScrollPhysics._flut_unpack(data)
        case "ClampingScrollPhysics":
            from flut.flutter.widgets.scroll_physics import ClampingScrollPhysics

            return ClampingScrollPhysics._flut_unpack(data)
        case "NeverScrollableScrollPhysics":
            from flut.flutter.widgets.scroll_physics import NeverScrollableScrollPhysics

            return NeverScrollableScrollPhysics._flut_unpack(data)
        case "AlwaysScrollableScrollPhysics":
            from flut.flutter.widgets.scroll_physics import (
                AlwaysScrollableScrollPhysics,
            )

            return AlwaysScrollableScrollPhysics._flut_unpack(data)
        case "ScrollDecelerationRate":
            from flut.flutter.widgets.scroll_physics import ScrollDecelerationRate

            return ScrollDecelerationRate._flut_unpack(data)
        case "VisualDensity":
            from flut.flutter.material.theme_data import _VisualDensity

            return _VisualDensity._flut_unpack(data)
        case "TextInputType":
            from flut.flutter.services.text_input import _TextInputType

            return _TextInputType._flut_unpack(data)
        case "ScrollBehavior":
            from flut.flutter.widgets.scroll_configuration import ScrollBehavior

            return ScrollBehavior._flut_unpack(data)
        case "IconThemeData":
            from flut.flutter.widgets.icon_theme_data import IconThemeData

            return IconThemeData._flut_unpack(data)
        case "ChipAnimationStyle":
            from flut.flutter.material.chip import (
                ChipAnimationStyle,
            )

            return ChipAnimationStyle._flut_unpack(data)
        case "Shadow":
            from flut.dart.ui import Shadow

            return Shadow._flut_unpack(data)
        case "TextOverflow":
            from flut.flutter.painting.text_painter import TextOverflow

            return TextOverflow._flut_unpack(data)
        case "TextAlign":
            from flut.dart.ui import TextAlign

            return TextAlign._flut_unpack(data)
        case "Axis":
            from flut.flutter.painting.basic_types import Axis

            return Axis._flut_unpack(data)
        case "MainAxisAlignment":
            from flut.flutter.rendering.flex import MainAxisAlignment

            return MainAxisAlignment._flut_unpack(data)
        case "MainAxisSize":
            from flut.flutter.rendering.flex import MainAxisSize

            return MainAxisSize._flut_unpack(data)
        case "CrossAxisAlignment":
            from flut.flutter.rendering.flex import CrossAxisAlignment

            return CrossAxisAlignment._flut_unpack(data)
        case "FlexFit":
            from flut.flutter.rendering.flex import FlexFit

            return FlexFit._flut_unpack(data)
        case "StackFit":
            from flut.flutter.rendering.stack import StackFit

            return StackFit._flut_unpack(data)
        case "BoxFit":
            from flut.flutter.painting.box_fit import BoxFit

            return BoxFit._flut_unpack(data)
        case "BorderStyle":
            from flut.flutter.painting.borders import BorderStyle

            return BorderStyle._flut_unpack(data)
        case "PlaceholderAlignment":
            from flut.dart.ui import PlaceholderAlignment

            return PlaceholderAlignment._flut_unpack(data)
        case "Orientation":
            from flut.flutter.widgets.media_query import Orientation

            return Orientation._flut_unpack(data)
        case "MenuStyle":
            from flut.flutter.material.menu_style import MenuStyle

            return MenuStyle._flut_unpack(data)
        case "NavigationDestinationLabelBehavior":
            from flut.flutter.material.navigation_bar import (
                NavigationDestinationLabelBehavior,
            )

            return NavigationDestinationLabelBehavior._flut_unpack(data)
        case "PopupMenuPosition":
            from flut.flutter.material.popup_menu_theme import PopupMenuPosition

            return PopupMenuPosition._flut_unpack(data)
        case "ListTileControlAffinity":
            from flut.flutter.material.list_tile import ListTileControlAffinity

            return ListTileControlAffinity._flut_unpack(data)
        case "SliderInteraction":
            from flut.flutter.material.slider import SliderInteraction

            return SliderInteraction._flut_unpack(data)
        case "ShowValueIndicator":
            from flut.flutter.material.slider_theme import ShowValueIndicator

            return ShowValueIndicator._flut_unpack(data)
        case "OverflowBarAlignment":
            from flut.flutter.widgets.overflow_bar import OverflowBarAlignment

            return OverflowBarAlignment._flut_unpack(data)
        case "SliverPaintOrder":
            from flut.flutter.rendering.viewport import SliverPaintOrder

            return SliverPaintOrder._flut_unpack(data)
        case "DropdownMenuCloseBehavior":
            from flut.flutter.material.dropdown_menu import DropdownMenuCloseBehavior

            return DropdownMenuCloseBehavior._flut_unpack(data)
        case "TextDirection":
            from flut.dart.ui import TextDirection

            return TextDirection._flut_unpack(data)
        case "WrapAlignment":
            from flut.flutter.rendering.wrap import WrapAlignment

            return WrapAlignment._flut_unpack(data)
        case "WrapCrossAlignment":
            from flut.flutter.rendering.wrap import WrapCrossAlignment

            return WrapCrossAlignment._flut_unpack(data)
        case "KeyEventResult":
            from flut.flutter.widgets.focus_manager import KeyEventResult

            return KeyEventResult._flut_unpack(data)
        case "ButtonStyle":
            from flut.flutter.material.button_style import ButtonStyle

            return ButtonStyle._flut_unpack(data)
        case "NumericFocusOrder":
            from flut.flutter.widgets.focus_traversal import NumericFocusOrder

            return NumericFocusOrder._flut_unpack(data)
        case "OverlayEntry":
            from flut.flutter.widgets.overlay import OverlayEntry

            return OverlayEntry._flut_unpack(data)
        case "WidgetStatesController":
            from flut.flutter.widgets.widget_state import WidgetStatesController

            return WidgetStatesController._flut_unpack(data)
        case "Double":
            v = data.get("value")
            if v == "inf":
                return float("inf")
            if v == "-inf":
                return float("-inf")
            if v == "nan":
                return float("nan")
            return float(v)
        case "PlatformProvidedMenuItemType":
            from flut.flutter.widgets.platform_menu_bar import (
                PlatformProvidedMenuItemType,
            )

            return PlatformProvidedMenuItemType._flut_unpack(data)
        case "MaterialType":
            from flut.flutter.material.material import MaterialType

            return MaterialType._flut_unpack(data)
        case _:
            raise RuntimeError(f"Unknown _flut_type: {flut_type}")


def _flut_unpack_optional_field(data: dict, field: str) -> Optional[object]:
    value = data.get(field)
    if value is None:
        return None
    if isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, dict):
        return flut_unpack(value)
    if isinstance(value, list):
        return [flut_unpack(item) if isinstance(item, dict) else item for item in value]
    return value


def _flut_unpack_required_field(data: dict, field: str) -> object:
    value = _flut_unpack_optional_field(data, field)
    if value is None:
        flut_type = data.get("_flut_type", "")
        raise ValueError(f"Missing required field '{field}' in {flut_type}")
    return value
