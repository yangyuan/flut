import 'dart:ui';

import 'package:flutter/gestures.dart'
    show
        DeviceGestureSettings,
        GestureRecognizer,
        LongPressDownDetails,
        LongPressGestureRecognizer,
        TapGestureRecognizer,
        TapMoveDetails;

import 'package:flut/dart/ui.dart';
import 'package:flut/dart/_dart.dart';
import 'package:flut/dart/core.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/native.dart';
import 'package:flut/flut/error.dart';
import 'package:flut/flut/widget.dart';
import 'package:flut/flutter/widgets/framework.dart';
import 'package:flut/flutter/widgets/focus_manager.dart';
import 'package:flut/flutter/widgets/focus_traversal.dart';
import 'package:flut/flutter/widgets/drag_target.dart';
import 'package:flut/flutter/foundation/key.dart';
import 'package:flut/flutter/rendering/box.dart';
import 'package:flut/flutter/rendering/custom_paint.dart';
import 'package:flut/flutter/widgets/form.dart';
import 'package:flut/flutter/material/app_bar.dart';
import 'package:flut/flutter/widgets/basic.dart';
import 'package:flut/flutter/widgets/spacer.dart';
import 'package:flut/flutter/widgets/container.dart';
import 'package:flut/flutter/widgets/editable_text.dart';
import 'package:flut/flutter/widgets/gesture_detector.dart';
import 'package:flut/flutter/widgets/icon.dart';
import 'package:flut/flutter/widgets/implicit_animations.dart';
import 'package:flut/flutter/widgets/scroll_controller.dart';
import 'package:flut/flutter/widgets/scroll_position.dart';
import 'package:flut/flutter/widgets/scroll_view.dart';
import 'package:flut/flutter/material/selectable_text.dart';
import 'package:flut/flutter/widgets/interactive_viewer.dart';
import 'package:flut/flutter/widgets/raw_menu_anchor.dart';
import 'package:flut/flutter/widgets/single_child_scroll_view.dart';
import 'package:flut/flutter/widgets/text.dart';
import 'package:flut/flutter/widgets/widget_span.dart';
import 'package:flut/flutter/widgets/visibility.dart';
import 'package:flut/flutter/material/app.dart';
import 'package:flut/flutter/material/card.dart';
import 'package:flut/flutter/material/divider.dart';
import 'package:flut/flutter/material/elevated_button.dart';
import 'package:flut/flutter/material/button_style.dart';
import 'package:flut/flutter/material/floating_action_button.dart';
import 'package:flut/flutter/material/icon_button.dart';
import 'package:flut/flutter/material/button_style_button.dart';
import 'package:flut/flutter/material/ink_well.dart';
import 'package:flut/flutter/material/progress_indicator.dart';
import 'package:flut/flutter/material/scaffold.dart';
import 'package:flut/flutter/material/scrollbar.dart';
import 'package:flut/flutter/widgets/scrollbar.dart';
import 'package:flut/flutter/material/text_field.dart';
import 'package:flut/flutter/material/theme_data.dart';
import 'package:flut/flutter/foundation/platform.dart';
import 'package:flut/flutter/material/text_theme.dart';
import 'package:flut/flutter/painting/alignment.dart';
import 'package:flut/flutter/painting/border_radius.dart';
import 'package:flut/flutter/painting/borders.dart';
import 'package:flut/flutter/painting/box_border.dart';
import 'package:flut/flutter/painting/box_decoration.dart';
import 'package:flut/flutter/painting/edge_insets.dart';
import 'package:flut/flutter/painting/basic_types.dart';
import 'package:flut/flutter/painting/text_painter.dart';
import 'package:flut/flutter/painting/text_span.dart';
import 'package:flut/flutter/painting/text_style.dart';
import 'package:flut/flutter/animation/curves.dart';
import 'package:flut/flutter/animation/animation_style.dart';
import 'package:flut/flutter/widgets/media_query.dart';
import 'package:flut/flutter/material/theme.dart';
import 'package:flut/flutter/material/color_scheme.dart';
import 'package:flut/flutter/widgets/icon_data.dart';
import 'package:flut/flutter/material/input_decorator.dart';
import 'package:flut/flutter/scheduler/binding.dart';
import 'package:flut/flutter/material/input_border.dart';
import 'package:flut/flutter/rendering/flex.dart';
import 'package:flut/flutter/rendering/stack.dart';
import 'package:flut/flutter/rendering/wrap.dart';
import 'package:flut/flutter/services/mouse_cursor.dart';
import 'package:flut/flutter/services/hardware_keyboard.dart';
import 'package:flut/flutter/services/keyboard_key.dart';
import 'package:flut/flutter/gestures/drag_details.dart';
import 'package:flut/flutter/gestures/velocity_tracker.dart';
import 'package:flut/flutter/gestures/long_press.dart';
import 'package:flut/flutter/services/clipboard.dart';
import 'package:flut/flutter/gestures/tap.dart';
import 'package:flut/flutter/gestures/scale.dart';
import 'package:flut/flutter/gestures/recognizer.dart';
import 'package:flut/flutter/material/text_button.dart';
import 'package:flut/flutter/material/outlined_button.dart';
import 'package:flut/flutter/material/list_tile.dart';
import 'package:flut/flutter/material/switch.dart';
import 'package:flut/flutter/material/checkbox.dart';
import 'package:flut/flutter/material/tooltip.dart';
import 'package:flut/flutter/material/circle_avatar.dart';
import 'package:flut/flutter/material/dropdown_menu.dart';
import 'package:flut/flutter/material/dropdown.dart';
import 'package:flut/flutter/widgets/routes.dart';
import 'package:flut/flutter/widgets/pages.dart';
import 'package:flut/flutter/widgets/navigator.dart';
import 'package:flut/flutter/material/page.dart';
import 'package:flut/flutter/widgets/widget_state.dart';
import 'package:flut/flutter/widgets/image.dart';
import 'package:flut/flutter/painting/box_fit.dart';
import 'package:flut/flutter/painting/decoration_image.dart';
import 'package:flut/dart/io.dart';
import 'package:flut/dart/typed_data.dart';
import 'package:flut/flutter/gestures/events.dart';
import 'package:flut/flutter/material/slider.dart';
import 'package:flut/flutter/material/slider_theme.dart';
import 'package:flut/flutter/material/dialog.dart';
import 'package:flut/flutter/material/drawer.dart';
import 'package:flut/flutter/material/navigation_bar.dart';
import 'package:flut/flutter/material/radio.dart';
import 'package:flut/flutter/material/chip.dart';
import 'package:flut/flutter/widgets/radio_group.dart';
import 'package:flut/flutter/material/popup_menu.dart';
import 'package:flut/flutter/material/popup_menu_theme.dart';
import 'package:flut/flutter/material/expansion_tile.dart';
import 'package:flut/flutter/material/text_form_field.dart';
import 'package:flut/flutter/widgets/expansible.dart';
import 'package:flut/flutter/widgets/notification_listener.dart';
import 'package:flut/flutter/widgets/scroll_notification.dart';
import 'package:flut/flutter/widgets/overlay.dart';
import 'package:flut/flutter/widgets/layout_builder.dart';
import 'package:flut/flutter/widgets/transitions.dart';
import 'package:flut/flutter/widgets/value_listenable_builder.dart';
import 'package:flut/flutter/foundation/change_notifier.dart';
import 'package:flut/flutter/painting/box_shadow.dart';
import 'package:flut/flutter/painting/gradient.dart';
import 'package:flut/flutter/animation/animation_controller.dart';
import 'package:flut/flutter/animation/animation.dart';
import 'package:flut/flutter/material/tab_controller.dart';
import 'package:flut/flutter/material/tabs.dart';
import 'package:flut/flutter/widgets/actions.dart';
import 'package:flut/flutter/widgets/shortcuts.dart';
import 'package:flut/flutter/gestures/gesture_settings.dart';
import 'package:flut/flutter/painting/text_scaler.dart';
import 'package:flut/flutter/rendering/object.dart';
import 'package:flut/flutter/painting/rounded_rectangle_border.dart';
import 'package:flut/flutter/painting/circle_border.dart';
import 'package:flut/flutter/rendering/selection.dart';
import 'package:flut/flutter/services/text_editing.dart';
import 'package:flut/flutter/widgets/magnifier.dart';
import 'package:flut/flutter/widgets/text_selection.dart';
import 'package:flut/flutter/widgets/selection_container.dart';
import 'package:flut/flutter/widgets/default_selection_style.dart';
import 'package:flut/flutter/widgets/selectable_region.dart';
import 'package:flut/flutter/widgets/text_selection_toolbar_anchors.dart';
import 'package:flut/flutter/material/adaptive_text_selection_toolbar.dart';
import 'package:flut/flutter/material/selection_area.dart';
import 'package:flut/flutter/material/text_selection_toolbar.dart';
import 'package:flut/flutter/material/text_selection_theme.dart';
import 'package:flut/flutter/painting/stadium_border.dart';
import 'package:flut/flutter/painting/beveled_rectangle_border.dart';
import 'package:flut/flutter/painting/continuous_rectangle_border.dart';
import 'package:flut/flutter/widgets/scroll_physics.dart';
import 'package:flut/flutter/widgets/scroll_configuration.dart';
import 'package:flut/flutter/widgets/icon_theme_data.dart';
import 'package:flut/flutter/material/menu_style.dart';
import 'package:flut/flutter/material/menu_anchor.dart';
import 'package:flut/flutter/material/material.dart';
import 'package:flut/flutter/widgets/overflow_bar.dart';
import 'package:flut/flutter/widgets/platform_menu_bar.dart';
import 'package:flut/flutter/rendering/viewport.dart';
import 'package:flut/flutter/rendering/proxy_box.dart';
import 'package:flut/flutter/services/text_input.dart';

class FlutCallableRef {
  final FlutRuntime runtime;
  final int cid;
  final String? callableType;

  FlutCallableRef(this.runtime, this.cid, this.callableType);

  T? invoke<T>({List<dynamic>? args}) {
    return runtime.callAction<T>(cid, args: args);
  }

  Map<String, dynamic> flutEncode() {
    final result = {'_flut_type': 'Callable', '_flut_cid': cid};
    if (callableType != null) result['_flut_callable_type'] = callableType!;
    return result;
  }

  static FlutCallableRef? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final cid = data['_flut_cid'] as int?;
    if (cid == null) return null;
    final callableType = data['_flut_callable_type'] as String?;
    return FlutCallableRef(runtime, cid, callableType);
  }
}

class FlutRuntime {
  final FlutNative flutNative;

  final Map<int, FlutRealtimeObject> objectRegistry = {};
  final Map<int, int> _hashToOid = {};
  final Map<String, Function> _staticRegistry = {};
  final Expando<int> _callableRegistry = Expando<int>();

  int _nextOid = 1;

  FlutRuntime(this.flutNative) {
    _registerStaticHandlers();
  }

  int generateOid() => _nextOid++;

  int createObject(Map<String, dynamic> data) {
    final oid = generateOid();
    data['_flut_oid'] = oid;

    final type = data['_flut_type'] as String?;
    if (type == null) {
      throw FlutRuntimeException('Missing _flut_type in createObject');
    }

    final result = _createRealtimeByType(type, data);
    objectRegistry[oid] = result;
    _hashToOid[identityHashCode(result.flutTarget)] = oid;

    return oid;
  }

  FlutRealtimeObject _createRealtimeByType(
    String type,
    Map<String, dynamic> data,
  ) {
    switch (type) {
      case 'Listenable':
        return FlutListenable.flutCreate(this, data);
      case 'ChangeNotifier':
        return FlutChangeNotifier.flutCreate(this, data);
      case 'TextEditingController':
        return FlutTextEditingController.flutCreate(this, data);
      case 'ScrollController':
        return FlutScrollController.flutCreate(this, data);
      case 'FocusNode':
        return FlutFocusNode.flutCreate(this, data);
      case 'FocusScopeNode':
        return FlutFocusScopeNode.flutCreate(this, data);
      case 'ColorScheme':
        return FlutColorScheme.flutCreate(this, data);
      case 'ThemeData':
        return FlutThemeData.flutCreate(this, data);
      case 'WidgetStateColor':
        return FlutWidgetStateColor.flutCreate(this, data);
      case 'WidgetStateProperty':
        return FlutWidgetStateProperty.flutCreate(this, data);
      case 'WidgetStatePropertyAll':
        return FlutWidgetStatePropertyAll.flutCreate(this, data);
      case 'PageRoute':
        return FlutPageRoute.flutCreate(this, data);
      case 'MaterialPageRoute':
        return FlutMaterialPageRoute.flutCreate(this, data);
      case 'UniqueKey':
        return FlutUniqueKey.flutCreate(this, data);
      case 'GlobalKey':
        return FlutGlobalKey.flutCreate(this, data);
      case 'ExpansibleController':
        return FlutExpansibleController.flutCreate(this, data);
      case 'OverlayEntry':
        return FlutOverlayEntry.flutCreate(this, data);
      case 'ValueNotifier':
        return FlutValueNotifier.flutCreate(this, data);
      case 'MagnifierController':
        return FlutMagnifierController.flutCreate(this, data);
      case 'AnimationController':
        return FlutAnimationController.flutCreate(this, data);
      case 'TabController':
        return FlutTabController.flutCreate(this, data);
      case 'MenuController':
        return FlutMenuController.flutCreate(this, data);
      case 'TransformationController':
        return FlutTransformationController.flutCreate(this, data);
      case 'ActionDispatcher':
        return FlutActionDispatcher.flutCreate(this, data);
      case 'WidgetStatesController':
        return FlutWidgetStatesController.flutCreate(this, data);
      case 'ButtonStyle':
        return FlutButtonStyle.flutCreate(this, data);
      case 'InteractiveInkFeatureFactory':
        return FlutInteractiveInkFeatureFactory.flutCreate(this, data);
      case 'TapGestureRecognizer':
        return FlutTapGestureRecognizer.flutCreate(this, data);
      case 'LongPressGestureRecognizer':
        return FlutLongPressGestureRecognizer.flutCreate(this, data);
      default:
        throw FlutRuntimeException('Unknown realtime object type: $type');
    }
  }

  Key? decodeKey(Map<String, dynamic> data) {
    final key = data['key'];
    if (key == null) return null;
    if (key is Map<String, dynamic>) {
      final oid = key['_flut_oid'] as int?;
      if (oid != null) {
        final existing = objectRegistry[oid];
        if (existing == null) {
          throw FlutRuntimeException(
            'Key with oid $oid not found in registry.',
          );
        }
        if (existing.flutTarget is Key) return existing.flutTarget as Key;
        throw FlutRuntimeException('Object with oid $oid is not a Key.');
      }
      final type = key['_flut_type'] as String?;
      switch (type) {
        case 'ValueKey':
          return FlutValueKey.flutDecode(this, key);
        default:
          return ValueKey(key);
      }
    }
    // TODO: Remove string fallback after a few versions
    return ValueKey(key);
  }

  void registerStatic(String name, Function handler) {
    _staticRegistry[name] = handler;
  }

  late final Finalizer<int> _callableFinalizer = Finalizer<int>((cid) {
    try {
      flutNative.invokeNativeAsync('release_callable', {'cid': cid});
    } catch (_) {}
  });

  void trackCallable(Function closure, int cid) {
    _callableRegistry[closure] = cid;
    _callableFinalizer.attach(closure, cid);
  }

  int? cidForCallable(Function closure) => _callableRegistry[closure];

  dynamic adaptCallableByType(FlutCallableRef callable) {
    if (callable.callableType == null) return callable;
    switch (callable.callableType) {
      case 'VoidCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureTapCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureTapCancelCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressCancelCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressUpCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'AllowedButtonsFilter':
        bool closure(int buttons) =>
            callable.invoke<bool>(args: [buttons]) ?? false;
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureTapMoveCallback':
        void closure(TapMoveDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureRecognizerFactoryConstructor':
        GestureRecognizer closure() =>
            callable.invoke<GestureRecognizer>(args: [])!;
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureRecognizerFactoryInitializer':
        void closure(GestureRecognizer instance) =>
            callable.invoke(args: [instance]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureDragStartCallback':
        void closure(DragStartDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureDragUpdateCallback':
        void closure(DragUpdateDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureDragEndCallback':
        void closure(DragEndDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureTapDownCallback':
        void closure(TapDownDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureTapUpCallback':
        void closure(TapUpDetails details) => callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressDownCallback':
        void closure(LongPressDownDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureScaleStartCallback':
        void closure(ScaleStartDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureScaleUpdateCallback':
        void closure(ScaleUpdateDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureScaleEndCallback':
        void closure(ScaleEndDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureDragDownCallback':
        void closure(DragDownDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureDragCancelCallback':
        void closure() => callable.invoke(args: []);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressStartCallback':
        void closure(LongPressStartDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressMoveUpdateCallback':
        void closure(LongPressMoveUpdateDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'GestureLongPressEndCallback':
        void closure(LongPressEndDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'ToolbarBuilder':
        Widget closure(BuildContext context, Widget child) =>
            callable.invoke<Widget>(args: [context, child]) ?? child;
        trackCallable(closure, callable.cid);
        return closure;
      case 'MagnifierBuilder':
        Widget? closure(
          BuildContext context,
          MagnifierController controller,
          ValueNotifier<MagnifierInfo> magnifierInfo,
        ) =>
            callable.invoke<Widget>(args: [context, controller, magnifierInfo]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'ValueChanged<String>':
        void closure(String value) => callable.invoke(args: [value]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'ValueChanged<bool>':
        void closure(bool value) => callable.invoke(args: [value]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'ValueChanged<bool?>':
        void closure(bool? value) => callable.invoke(args: [value]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'PointerEnterEventListener':
        void closure(PointerEnterEvent event) => callable.invoke(args: [event]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'PointerExitEventListener':
        void closure(PointerExitEvent event) => callable.invoke(args: [event]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'TapRegionCallback':
        void closure(PointerDownEvent event) => callable.invoke(args: [event]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'TapRegionUpCallback':
        void closure(PointerUpEvent event) => callable.invoke(args: [event]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'FocusOnKeyEventCallback':
        KeyEventResult closure(FocusNode node, KeyEvent event) =>
            callable.invoke<KeyEventResult>(args: [event])!;
        trackCallable(closure, callable.cid);
        return closure;
      case 'WidgetBuilder':
        Widget closure(BuildContext context) =>
            callable.invoke<Widget>(args: [context])!;
        trackCallable(closure, callable.cid);
        return closure;
      case 'RoutePredicate':
        bool closureRoutePredicate(Route<dynamic> route) =>
            callable.invoke<bool>(args: [route])!;
        trackCallable(closureRoutePredicate, callable.cid);
        return closureRoutePredicate;
      case 'NullableIndexedWidgetBuilder':
        Widget? closureIndexed(BuildContext context, int index) =>
            callable.invoke<Widget>(args: [context, index]);
        trackCallable(closureIndexed, callable.cid);
        return closureIndexed;
      case 'ValueChanged<dynamic?>':
        void closure(dynamic value) => callable.invoke(args: [value]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'ValueChanged<double>':
        void closureDouble(double value) => callable.invoke(args: [value]);
        trackCallable(closureDouble, callable.cid);
        return closureDouble;
      case 'ValueChanged<int>':
        void closureInt(int value) => callable.invoke(args: [value]);
        trackCallable(closureInt, callable.cid);
        return closureInt;
      case 'PopupMenuItemBuilder':
        List<PopupMenuEntry<dynamic>> closureBuilder(BuildContext context) {
          return callable.invoke<List<PopupMenuEntry<dynamic>>>(
            args: [context],
          )!;
        }
        trackCallable(closureBuilder, callable.cid);
        return closureBuilder;
      case 'DraggableCanceledCallback':
        void closureCanceled(Velocity velocity, Offset offset) =>
            callable.invoke(args: [velocity, offset]);
        trackCallable(closureCanceled, callable.cid);
        return closureCanceled;
      case 'DragEndCallback':
        void closureDragEnd(DraggableDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closureDragEnd, callable.cid);
        return closureDragEnd;
      case 'DragTargetBuilder':
        Widget closureDragTargetBuilder(
          BuildContext context,
          List<Object?> candidateData,
          List<dynamic> rejectedData,
        ) => callable.invoke<Widget>(
          args: [context, candidateData, rejectedData],
        )!;
        trackCallable(closureDragTargetBuilder, callable.cid);
        return closureDragTargetBuilder;
      case 'DragTargetWillAcceptWithDetails':
        bool closureWillAccept(DragTargetDetails details) =>
            callable.invoke<bool>(args: [details])!;
        trackCallable(closureWillAccept, callable.cid);
        return closureWillAccept;
      case 'DragTargetAcceptWithDetails':
        void closureAccept(DragTargetDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closureAccept, callable.cid);
        return closureAccept;
      case 'DragTargetLeave':
        void closureLeave(Object? data) => callable.invoke(args: [data]);
        trackCallable(closureLeave, callable.cid);
        return closureLeave;
      case 'DragTargetMove':
        void closureMove(DragTargetDetails details) =>
            callable.invoke(args: [details]);
        trackCallable(closureMove, callable.cid);
        return closureMove;
      case 'FormFieldValidator':
        String? closureValidator(String? value) =>
            callable.invoke<String?>(args: [value]);
        trackCallable(closureValidator, callable.cid);
        return closureValidator;
      case 'FormFieldSetter':
        void closureSetter(String? value) => callable.invoke(args: [value]);
        trackCallable(closureSetter, callable.cid);
        return closureSetter;
      case 'NotificationListenerCallback':
        bool closureNotification(Notification notification) =>
            callable.invoke<bool>(args: [notification])!;
        trackCallable(closureNotification, callable.cid);
        return closureNotification;
      case 'LayoutWidgetBuilder':
        Widget closureLayout(
          BuildContext context,
          BoxConstraints constraints,
        ) => callable.invoke<Widget>(args: [context, constraints])!;
        trackCallable(closureLayout, callable.cid);
        return closureLayout;
      case 'TransitionBuilder':
        Widget closureTransition(BuildContext context, Widget? child) =>
            callable.invoke<Widget>(args: [context])!;
        trackCallable(closureTransition, callable.cid);
        return closureTransition;
      case 'ValueWidgetBuilder':
        Widget closureValueBuilder(
          BuildContext context,
          dynamic value,
          Widget? child,
        ) => callable.invoke<Widget>(args: [context, value])!;
        trackCallable(closureValueBuilder, callable.cid);
        return closureValueBuilder;
      case 'ImageErrorListener':
        void closureImageError(Object exception, StackTrace? stackTrace) =>
            callable.invoke(args: [exception, stackTrace]);
        trackCallable(closureImageError, callable.cid);
        return closureImageError;
      case 'TooltipTriggeredCallback':
        void closureTooltipTriggered() => callable.invoke(args: []);
        trackCallable(closureTooltipTriggered, callable.cid);
        return closureTooltipTriggered;
      case 'SelectionChangedCallback':
        void closureSelectionChanged(
          TextSelection selection,
          SelectionChangedCause? cause,
        ) => callable.invoke(args: [selection, cause]);
        trackCallable(closureSelectionChanged, callable.cid);
        return closureSelectionChanged;
      case 'ValueChanged<SelectedContent?>':
        void closureSelectedContent(SelectedContent? value) =>
            callable.invoke(args: [value]);
        trackCallable(closureSelectedContent, callable.cid);
        return closureSelectedContent;
      case 'SelectableRegionContextMenuBuilder':
        Widget closureSelectableRegionContextMenu(
          BuildContext context,
          SelectableRegionState selectableRegionState,
        ) => callable.invoke<Widget>(args: [context, selectableRegionState])!;
        trackCallable(closureSelectableRegionContextMenu, callable.cid);
        return closureSelectableRegionContextMenu;
      case 'EditableTextContextMenuBuilder':
        Widget closureContextMenu(
          BuildContext context,
          EditableTextState editableTextState,
        ) => callable.invoke<Widget>(args: [context, editableTextState])!;
        trackCallable(closureContextMenu, callable.cid);
        return closureContextMenu;
      case 'PointerHoverEventListener':
        void closureHover(PointerHoverEvent event) =>
            callable.invoke(args: [event]);
        trackCallable(closureHover, callable.cid);
        return closureHover;
      case 'SemanticFormatterCallback':
        String closureFormatter(double value) =>
            callable.invoke<String>(args: [value])!;
        trackCallable(closureFormatter, callable.cid);
        return closureFormatter;
      case 'void Function(FocusNode)':
        void closure(FocusNode node) => callable.invoke(args: [node]);
        trackCallable(closure, callable.cid);
        return closure;
      case 'DropdownMenuDecorationBuilder':
        Widget closureDecorationBuilder(BuildContext context, Widget child) =>
            callable.invoke<Widget>(args: [context, child])!;
        trackCallable(closureDecorationBuilder, callable.cid);
        return closureDecorationBuilder;
      case 'FilterCallback':
        List<DropdownMenuEntry<dynamic>> closureFilter(
          List<DropdownMenuEntry<dynamic>> entries,
          String filter,
        ) => callable.invoke<List<DropdownMenuEntry<dynamic>>>(
          args: [entries, filter],
        )!;
        trackCallable(closureFilter, callable.cid);
        return closureFilter;
      case 'SearchCallback':
        int? closureSearch(
          List<DropdownMenuEntry<dynamic>> entries,
          String query,
        ) => callable.invoke<int?>(args: [entries, query]);
        trackCallable(closureSearch, callable.cid);
        return closureSearch;
      case 'DropdownButtonBuilder':
        List<Widget> closureDropdownBuilder(BuildContext context) =>
            callable.invoke<List<Widget>>(args: [context])!;
        trackCallable(closureDropdownBuilder, callable.cid);
        return closureDropdownBuilder;
      default:
        return callable;
    }
  }

  FlutCallableRef? decodeFlutCallable(dynamic value) {
    if (value is Map<String, dynamic> && value['_flut_type'] == 'Callable') {
      return FlutCallableRef.flutDecode(this, value);
    }
    return null;
  }

  void _registerStaticHandlers() {
    FlutTheme.registerStatics(this);
    FlutMediaQuery.registerStatics(this);
    FlutHardwareKeyboard.registerStatics(this);
    FlutSchedulerBinding.registerStatics(this);
    FlutModalRoute.registerStatics(this);
    FlutNavigator.registerStatics(this);
    FlutWidgetStateColor.registerStatics(this);
    FlutForm.registerStatics(this);
    FlutOverlay.registerStatics(this);
    FlutMagnifierController.registerStatics(this);
    FlutInheritedScope.registerStatics(this);
    FlutActions.registerStatics(this);
    FlutVisibility.registerStatics(this);
    FlutDivider.registerStatics(this);
    FlutTooltip.registerStatics(this);
    FlutElevatedButton.registerStatics(this);
    FlutIconButton.registerStatics(this);
    FlutOutlinedButton.registerStatics(this);
    FlutInteractiveInkFeatureFactory.registerStatics(this);
    FlutWidgetSpan.registerStatics(this);
    FlutExpansibleController.registerStatics(this);
    FlutClipboard.registerStatics(this);
    FlutShowDialog.registerStatics(this);
    FlutShowMenu.registerStatics(this);
    FlutSelectionContainer.registerStatics(this);
    FlutTextSelectionTheme.registerStatics(this);
  }

  void triggerAction(int actionId, {Map<String, dynamic>? payload}) {
    final data = <String, dynamic>{'id': actionId, ...?payload};
    flutNative.invokeNativeAsync('action', data);
  }

  dynamic unpackNullableRequiredCallback(
    Map<String, dynamic> data,
    String fieldName,
  ) {
    if (!data.containsKey(fieldName)) {
      final parentType = data['_flut_type'] as String? ?? '';
      throw FlutMissingRequiredParameterException(parentType, fieldName);
    }
    return unpackOptionalCallback(data, fieldName);
  }

  dynamic unpackRequiredCallback(Map<String, dynamic> data, String fieldName) {
    final result = unpackOptionalCallback(data, fieldName);
    if (result == null) {
      final parentType = data['_flut_type'] as String? ?? '';
      throw FlutMissingRequiredParameterException(parentType, fieldName);
    }
    return result;
  }

  dynamic unpackOptionalCallback(Map<String, dynamic> data, String fieldName) {
    final callableRef = unpackOptionalField<FlutCallableRef>(data, fieldName);
    if (callableRef == null) return null;
    return adaptCallableByType(callableRef);
  }

  String? unpackConstructor(Map<String, dynamic> data) {
    return data['_flut_init'] as String?;
  }

  Map<String, dynamic>? invokeAction(
    int actionId, {
    Map<String, dynamic>? payload,
  }) {
    final data = <String, dynamic>{'id': actionId, ...?payload};
    return flutNative.invokeNativeSync('action', data);
  }

  T? callAction<T>(
    int actionId, {
    List<dynamic>? args,
    Map<String, dynamic>? kwargs,
  }) {
    final payload = <String, dynamic>{};
    if (args != null && args.isNotEmpty) {
      payload['args'] = args.map((a) => encodeValue(a)).toList();
    }
    if (kwargs != null && kwargs.isNotEmpty) {
      payload['kwargs'] = kwargs.map((k, v) => MapEntry(k, encodeValue(v)));
    }
    final result = invokeAction(
      actionId,
      payload: payload.isEmpty ? null : payload,
    );
    final error = result?['_flut_error'];
    if (error != null) {
      throw FlutterError('Python callback error (action $actionId): $error');
    }
    final innerResult = result?['_flut_result'];
    if (innerResult == null) return null;
    if (innerResult is T) return innerResult;
    if (innerResult is Map<String, dynamic>) {
      return decodeObject<T>(innerResult);
    }
    if (innerResult is List) {
      return decodeList<T>(innerResult);
    }
    return null;
  }

  Map<String, dynamic> handleStaticCall(
    String name,
    List<dynamic> args,
    Map<String, dynamic>? kwargs,
  ) {
    final handler = _staticRegistry[name];
    if (handler == null) {
      return {'_flut_error': 'Unknown static function', 'name': name};
    }

    final resolvedArgs = args.map(resolveArg).toList();
    final resolvedKwargs = kwargs?.map((k, v) => MapEntry(k, resolveArg(v)));

    try {
      Map<Symbol, dynamic>? namedArgs;
      if (resolvedKwargs != null && resolvedKwargs.isNotEmpty) {
        namedArgs = resolvedKwargs.map((k, v) => MapEntry(Symbol(k), v));
      }
      final result = Function.apply(handler, [
        this,
        ...resolvedArgs,
      ], namedArgs);
      return {'_flut_value': encodeValue(result)};
    } catch (e) {
      return {'_flut_error': e.toString()};
    }
  }

  dynamic resolveArg(dynamic arg) {
    if (arg is Map<String, dynamic>) {
      if (arg.containsKey('_flut_oid')) {
        final oid = arg['_flut_oid'] as int;
        final obj = objectRegistry[oid];
        if (obj is FlutRealtimeObject) {
          return obj.flutTarget;
        }
        return obj;
      }
      if (arg.containsKey('_flut_type')) {
        return decodeObject(arg);
      }
    }
    return arg;
  }

  Widget? decodeWidget(dynamic data) {
    return decodeObject<Widget>(data);
  }

  Widget buildWidgetFromJson(Map<String, dynamic> data) {
    final widget = decodeWidget(data);
    if (widget == null) {
      throw FlutRuntimeException('Failed to decode widget');
    }
    return widget;
  }

  T? unpackOptionalField<T>(Map<String, dynamic> data, String fieldName) {
    final value = data[fieldName];
    if (value == null) return null;

    if (value is Map<String, dynamic> && value['_flut_type'] == 'Callable') {
      if (T == int) return value['_flut_cid'] as T;
      if (T == FlutCallableRef) {
        return FlutCallableRef.flutDecode(this, value) as T;
      }
    }

    if (T == double) {
      return FlutDouble.decode(value) as T;
    }
    if (T == int) return value as T;
    if (T == bool) return value as T;
    if (T == String) return value as T;

    if (value is List) {
      return decodeList<T>(value);
    }

    return decodeObject<T>(value);
  }

  T? decodeList<T>(List<dynamic> value) {
    if (T == List<Widget>) {
      return value.map((c) => decodeWidget(c)).nonNulls.toList() as T;
    }

    if (T == List<InlineSpan>) {
      return value.map((c) => decodeObject<InlineSpan>(c)).nonNulls.toList()
          as T;
    }

    if (T == List<DropdownMenuItem<dynamic>>) {
      return value
              .map((c) => decodeObject<DropdownMenuItem<dynamic>>(c))
              .nonNulls
              .toList()
          as T;
    }

    if (T == List<DropdownMenuEntry<dynamic>>) {
      return value
              .map((c) => decodeObject<DropdownMenuEntry<dynamic>>(c))
              .nonNulls
              .toList()
          as T;
    }

    if (T == List<PopupMenuEntry<dynamic>>) {
      return value
              .map((c) => decodeObject<PopupMenuEntry<dynamic>>(c))
              .nonNulls
              .toList()
          as T;
    }

    if (T == List<Shadow>) {
      return value.map((c) => decodeObject<Shadow>(c)).nonNulls.toList() as T;
    }

    if (T == List<PlatformMenuItem>) {
      return value
              .map((c) => decodeObject<PlatformMenuItem>(c))
              .nonNulls
              .toList()
          as T;
    }

    if (T == List<Listenable?>) {
      return value
              .map((c) => c == null ? null : decodeObject<Listenable>(c))
              .toList()
          as T;
    }

    if (T == Set<PointerDeviceKind>) {
      return value
              .map((c) => decodeObject<PointerDeviceKind>(c))
              .nonNulls
              .toSet()
          as T;
    }

    if (T == Map<Type, GestureRecognizerFactory>) {
      final result = <Type, GestureRecognizerFactory>{};
      for (final c in value) {
        final factory = decodeObject<GestureRecognizerFactory>(c);
        if (factory != null) {
          result[factory.constructor().runtimeType] = factory;
        }
      }
      return result as T;
    }

    return null;
  }

  T unpackRequiredField<T>(Map<String, dynamic> data, String fieldName) {
    if (!data.containsKey(fieldName)) {
      final parentType = data['_flut_type'] as String? ?? '';
      throw FlutMissingRequiredParameterException(parentType, fieldName);
    }
    return unpackOptionalField<T>(data, fieldName) as T;
  }

  T? unpackNullableRequiredField<T>(
    Map<String, dynamic> data,
    String fieldName,
  ) {
    if (!data.containsKey(fieldName)) {
      final parentType = data['_flut_type'] as String? ?? '';
      throw FlutMissingRequiredParameterException(parentType, fieldName);
    }
    return unpackOptionalField<T>(data, fieldName);
  }

  dynamic unpackDynamicOptionalField(
    Map<String, dynamic> data,
    String fieldName,
  ) {
    final value = data[fieldName];
    if (value == null) return null;
    if (value is num || value is String || value is bool) return value;
    if (value is Map<String, dynamic>) return decodeObject(value);
    if (value is List) return value;
    return value;
  }

  dynamic unpackDynamicRequiredField(
    Map<String, dynamic> data,
    String fieldName,
  ) {
    if (!data.containsKey(fieldName)) {
      final parentType = data['_flut_type'] as String? ?? '';
      throw FlutMissingRequiredParameterException(parentType, fieldName);
    }
    return unpackDynamicOptionalField(data, fieldName);
  }

  T? decodeObject<T>(dynamic data) {
    if (data == null) return null;

    if (T == Widget && data is Widget) {
      return data as T;
    }

    if (data is! Map<String, dynamic>) {
      throw FlutInvalidValueException(T.toString(), data);
    }

    final type = data['_flut_type'] as String?;
    if (type == null) {
      throw FlutRuntimeException('Missing _flut_type field');
    }

    final oid = data['_flut_oid'] as int?;
    if (oid != null) {
      final existing = objectRegistry[oid];
      if (existing == null) {
        throw FlutRuntimeException(
          'Realtime object $type with oid $oid not found in registry.',
        );
      }
      if (existing is T) return existing as T;
      if (existing.flutTarget is T) return existing.flutTarget as T;
      throw FlutInvalidValueException(T.toString(), existing);
    }

    final result = _decodeByType(type, data);

    if (result is! T) {
      throw FlutInvalidValueException(T.toString(), result);
    }

    return result;
  }

  R? unpackGenericField<R, V>(Map<String, dynamic> data, String fieldName) {
    final value = data[fieldName];
    if (value == null) return null;
    if (value is! Map<String, dynamic>) return null;
    final oid = value['_flut_oid'] as int?;
    if (oid != null) {
      final existing = objectRegistry[oid];
      if (existing == null) return null;
      if (existing is R) return existing as R;
      if (existing.flutTarget is R) return existing.flutTarget as R;
      final adapted = existing.adaptGeneric<V>();
      if (adapted is R) return adapted;
      return null;
    }
    return unpackOptionalField<R>(data, fieldName);
  }

  dynamic _decodeByType(String type, Map<String, dynamic> data) {
    switch (type) {
      case 'Intent':
        return FlutIntent.flutDecode(this, data);
      case 'EdgeInsetsGeometry':
        return FlutEdgeInsetsGeometry.flutDecode(this, data);
      case 'EdgeInsets':
        return FlutEdgeInsets.flutDecode(this, data);
      case 'EdgeInsetsDirectional':
        return FlutEdgeInsetsDirectional.flutDecode(this, data);
      case 'Alignment':
        return FlutAlignment.flutDecode(this, data);
      case 'AlignmentDirectional':
        return FlutAlignmentDirectional.flutDecode(this, data);
      case 'AlignmentGeometry':
        return FlutAlignmentGeometry.flutDecode(this, data);
      case 'BorderRadiusGeometry':
        return FlutBorderRadiusGeometry.flutDecode(this, data);
      case 'BorderRadius':
        return FlutBorderRadius.flutDecode(this, data);
      case 'BorderRadiusDirectional':
        return FlutBorderRadiusDirectional.flutDecode(this, data);
      case 'BorderStyle':
        return const FlutBorderStyle().flutDecode(data);
      case 'DynamicSchemeVariant':
        return const FlutDynamicSchemeVariant().flutDecode(data);
      case 'FontWeight':
        return FlutFontWeight.flutDecode(this, data);
      case 'TextDecoration':
        return FlutTextDecoration.flutDecode(this, data);
      case 'BorderSide':
        return FlutBorderSide.flutDecode(this, data);
      case 'Border':
        return FlutBorder.flutDecode(this, data);
      case 'BoxDecoration':
        return FlutBoxDecoration.flutDecode(this, data);
      case 'TextSpan':
        return FlutTextSpan.flutDecode(this, data);
      case 'WidgetSpan':
        return FlutWidgetSpan.flutDecode(this, data);
      case 'TextStyle':
        return FlutTextStyle.flutDecode(this, data);
      case 'TextOverflow':
        return const FlutTextOverflow().flutDecode(data);
      case 'TextAffinity':
        return const FlutTextAffinity().flutDecode(data);
      case 'SelectionChangedCause':
        return const FlutSelectionChangedCause().flutDecode(data);
      case 'TextSelection':
        return FlutTextSelection.flutDecode(this, data);
      case 'IconData':
        return FlutIconData.flutDecode(this, data);
      case 'TextTheme':
        return FlutTextTheme.flutDecode(this, data);
      case 'InputDecoration':
        return FlutInputDecoration.flutDecode(this, data);
      case 'InputBorder':
        return FlutInputBorder.flutDecode(this, data);
      case 'Duration':
        return FlutDuration.flutDecode(this, data);
      case 'Curve':
        return FlutCurve.flutDecode(this, data);
      case 'AnimationStyle':
        return FlutAnimationStyle.flutDecode(this, data);
      case 'LogicalKeyboardKey':
        return FlutLogicalKeyboardKey.flutDecode(this, data);
      case 'PhysicalKeyboardKey':
        return FlutPhysicalKeyboardKey.flutDecode(this, data);
      case 'Color':
        return FlutColor.flutDecode(this, data);
      case 'WidgetState':
        return const FlutWidgetState().flutDecode(data);
      case 'WidgetStatesConstraint':
        return FlutWidgetStatesConstraint.flutDecode(this, data);
      case 'MainAxisAlignment':
        return const FlutMainAxisAlignment().flutDecode(data);
      case 'MainAxisSize':
        return const FlutMainAxisSize().flutDecode(data);
      case 'CrossAxisAlignment':
        return const FlutCrossAxisAlignment().flutDecode(data);
      case 'MouseCursor':
        return FlutMouseCursor.flutDecode(this, data);
      case 'SystemMouseCursor':
        return FlutSystemMouseCursor.flutDecode(this, data);
      case 'KeyEventResult':
        return const FlutKeyEventResult().flutDecode(data);
      case 'PaintingStyle':
        return const FlutPaintingStyle().flutDecode(data);
      case 'StrokeCap':
        return const FlutStrokeCap().flutDecode(data);
      case 'StrokeJoin':
        return const FlutStrokeJoin().flutDecode(data);
      case 'BlendMode':
        return const FlutBlendMode().flutDecode(data);
      case 'FilterQuality':
        return const FlutFilterQuality().flutDecode(data);
      case 'BlurStyle':
        return const FlutBlurStyle().flutDecode(data);
      case 'TileMode':
        return const FlutTileMode().flutDecode(data);
      case 'MaskFilter':
        return FlutMaskFilter.flutDecode(this, data);
      case 'ColorFilter':
        return FlutColorFilter.flutDecode(this, data);
      case 'ImageFilter':
        return FlutImageFilter.flutDecode(this, data);
      case 'Gradient':
        return FlutGradient.flutDecode(this, data);
      case 'PlaceholderAlignment':
        return const FlutPlaceholderAlignment().flutDecode(data);
      case 'TextBaseline':
        return const FlutTextBaseline().flutDecode(data);
      case 'FlexFit':
        return const FlutFlexFit().flutDecode(data);
      case 'StackFit':
        return const FlutStackFit().flutDecode(data);
      case 'ScrollbarOrientation':
        return const FlutScrollbarOrientation().flutDecode(data);
      case 'Axis':
        return const FlutAxis().flutDecode(data);
      case 'TextAlign':
        return const FlutTextAlign().flutDecode(data);
      case 'Brightness':
        return const FlutBrightness().flutDecode(data);
      case 'TextDirection':
        return const FlutTextDirection().flutDecode(data);
      case 'Clip':
        return const FlutClip().flutDecode(data);
      case 'ColorSpace':
        return const FlutColorSpace().flutDecode(data);
      case 'PointerDeviceKind':
        return const FlutPointerDeviceKind().flutDecode(data);
      case 'BoxShape':
        return const FlutBoxShape().flutDecode(data);
      case 'FontStyle':
        return const FlutFontStyle().flutDecode(data);
      case 'TextDecorationStyle':
        return const FlutTextDecorationStyle().flutDecode(data);
      case 'TextLeadingDistribution':
        return const FlutTextLeadingDistribution().flutDecode(data);
      case 'TextWidthBasis':
        return const FlutTextWidthBasis().flutDecode(data);
      case 'FloatingLabelBehavior':
        return const FlutFloatingLabelBehavior().flutDecode(data);
      case 'DragStartBehavior':
        return const FlutDragStartBehavior().flutDecode(data);
      case 'NavigationMode':
        return const FlutNavigationMode().flutDecode(data);
      case 'Orientation':
        return const FlutOrientation().flutDecode(data);
      case 'DeviceGestureSettings':
        return FlutDeviceGestureSettings.flutDecode(this, data);
      case 'GestureRecognizerFactory':
        return FlutGestureRecognizerFactory.flutDecode(this, data);
      case 'GestureRecognizerFactoryWithHandlers':
        return FlutGestureRecognizerFactoryWithHandlers.flutDecode(this, data);
      case 'TapMoveDetails':
        return FlutTapMoveDetails.flutDecode(this, data);
      case 'LongPressDownDetails':
        return FlutLongPressDownDetails.flutDecode(this, data);
      case 'TextScaler':
        return FlutTextScaler.flutDecode(this, data);
      case 'TextMagnifierConfiguration':
        return FlutTextMagnifierConfiguration.flutDecode(this, data);
      case 'MagnifierInfo':
        return FlutMagnifierInfo.flutDecode(this, data);
      case 'SelectedContent':
        return FlutSelectedContent.flutDecode(this, data);
      case 'SelectedContentRange':
        return FlutSelectedContentRange.flutDecode(this, data);
      case 'SelectionResult':
        return const FlutSelectionResult().flutDecode(data);
      case 'SelectionEventType':
        return const FlutSelectionEventType().flutDecode(data);
      case 'TextGranularity':
        return const FlutTextGranularity().flutDecode(data);
      case 'SelectionExtendDirection':
        return const FlutSelectionExtendDirection().flutDecode(data);
      case 'SelectionStatus':
        return const FlutSelectionStatus().flutDecode(data);
      case 'TextSelectionHandleType':
        return const FlutTextSelectionHandleType().flutDecode(data);
      case 'SelectionPoint':
        return FlutSelectionPoint.flutDecode(this, data);
      case 'SelectionGeometry':
        return FlutSelectionGeometry.flutDecode(this, data);
      case 'SelectAllSelectionEvent':
        return FlutSelectAllSelectionEvent.flutDecode(this, data);
      case 'ClearSelectionEvent':
        return FlutClearSelectionEvent.flutDecode(this, data);
      case 'SelectWordSelectionEvent':
        return FlutSelectWordSelectionEvent.flutDecode(this, data);
      case 'SelectParagraphSelectionEvent':
        return FlutSelectParagraphSelectionEvent.flutDecode(this, data);
      case 'SelectionEdgeUpdateEvent':
        return FlutSelectionEdgeUpdateEvent.flutDecode(this, data);
      case 'GranularlyExtendSelectionEvent':
        return FlutGranularlyExtendSelectionEvent.flutDecode(this, data);
      case 'DirectionallyExtendSelectionEvent':
        return FlutDirectionallyExtendSelectionEvent.flutDecode(this, data);
      case 'TextSelectionToolbarAnchors':
        return FlutTextSelectionToolbarAnchors.flutDecode(this, data);
      case 'TextSelectionControls':
        return FlutTextSelectionControls.flutDecode(this, data);
      case 'TextSelectionHandleControls':
        return FlutTextSelectionHandleControls.flutDecode(this, data);
      case 'EmptyTextSelectionControls':
        return FlutEmptyTextSelectionControls.flutDecode(this, data);
      case 'SelectionRegistrar':
        return FlutSelectionRegistrar.flutDecode(this, data);
      case 'SelectionContainerDelegate':
        return FlutSelectionContainerDelegate.flutDecode(this, data);
      case 'MultiSelectableSelectionContainerDelegate':
        return FlutMultiSelectableSelectionContainerDelegate.flutDecode(
          this,
          data,
        );
      case 'StaticSelectionContainerDelegate':
        return FlutStaticSelectionContainerDelegate.flutDecode(this, data);
      case 'MaterialTapTargetSize':
        return const FlutMaterialTapTargetSize().flutDecode(data);
      case 'TargetPlatform':
        return const FlutTargetPlatform().flutDecode(data);
      case 'Matrix4':
        return FlutMatrix4.flutDecode(this, data);
      case 'Size':
        return FlutSize.flutDecode(this, data);
      case 'Radius':
        return FlutRadius.flutDecode(this, data);
      case 'Offset':
        return FlutOffset.flutDecode(this, data);
      case 'Rect':
        return FlutRect.flutDecode(this, data);
      case 'RelativeRect':
        return FlutRelativeRect.flutDecode(this, data);
      case 'RRect':
        return FlutRRect.flutDecode(this, data);
      case 'ViewPadding':
        return FlutViewPadding.flutDecode(this, data);
      case 'Paint':
        return FlutPaint.flutDecode(this, data);
      case 'Shadow':
        return FlutShadow.flutDecode(this, data);
      case 'CustomPainter':
        return FlutCustomPainter.flutDecode(this, data);
      case 'StatefulWidget':
        return FlutStatefulWidget(
          key: decodeKey(data),
          flutPid: unpackRequiredField<int>(data, '_flut_pid'),
          className: unpackRequiredField<String>(data, 'className'),
          native: flutNative,
          runtime: this,
        );
      case 'StatelessWidget':
        return FlutStatelessWidget(
          key: decodeKey(data),
          flutPid: unpackRequiredField<int>(data, '_flut_pid'),
          className: unpackRequiredField<String>(data, 'className'),
          native: flutNative,
          runtime: this,
        );
      case 'InheritedWidget':
        return FlutInheritedScopeWidget(
          key: decodeKey(data),
          flutPid: unpackRequiredField<int>(data, '_flut_pid'),
          scopeName: unpackRequiredField<String>(data, 'scopeName'),
          className: unpackRequiredField<String>(data, 'className'),
          native: flutNative,
          runtime: this,
        );
      case 'AppBar':
        return FlutAppBar.flutDecode(this, data);
      case 'Text':
        return FlutText.flutDecode(this, data);
      case 'SelectableText':
        return FlutSelectableText.flutDecode(this, data);
      case 'SelectionArea':
        return FlutSelectionArea.flutDecode(this, data);
      case 'RichText':
        return FlutRichText.flutDecode(this, data);
      case 'SelectionContainer':
        return FlutSelectionContainer.flutDecode(this, data);
      case 'SelectionRegistrarScope':
        return FlutSelectionRegistrarScope.flutDecode(this, data);
      case 'DefaultSelectionStyle':
        return FlutDefaultSelectionStyle.flutDecode(this, data);
      case 'TextSelectionTheme':
        return FlutTextSelectionTheme.flutDecode(this, data);
      case 'TextSelectionThemeData':
        return FlutTextSelectionThemeData.flutDecode(this, data);
      case 'SelectableRegion':
        return FlutSelectableRegion.flutDecode(this, data);
      case 'SelectableRegionSelectionStatus':
        return const FlutSelectableRegionSelectionStatus().flutDecode(data);
      case 'TextSelectionToolbar':
        return FlutTextSelectionToolbar.flutDecode(this, data);
      case 'AdaptiveTextSelectionToolbar':
        return FlutAdaptiveTextSelectionToolbar.flutDecode(this, data);
      case 'Center':
        return FlutCenter.flutDecode(this, data);
      case 'Padding':
        return FlutPadding.flutDecode(this, data);
      case 'IgnorePointer':
        return FlutIgnorePointer.flutDecode(this, data);
      case 'Align':
        return FlutAlign.flutDecode(this, data);
      case 'Opacity':
        return FlutOpacity.flutDecode(this, data);
      case 'ClipRRect':
        return FlutClipRRect.flutDecode(this, data);
      case 'SizedBox':
        return FlutSizedBox.flutDecode(this, data);
      case 'Expanded':
        return FlutExpanded.flutDecode(this, data);
      case 'Flexible':
        return FlutFlexible.flutDecode(this, data);
      case 'Spacer':
        return FlutSpacer.flutDecode(this, data);
      case 'Column':
        return FlutColumn.flutDecode(this, data);
      case 'Row':
        return FlutRow.flutDecode(this, data);
      case 'Stack':
        return FlutStack.flutDecode(this, data);
      case 'Positioned':
        return FlutPositioned.flutDecode(this, data);
      case 'Container':
        return FlutContainer.flutDecode(this, data);
      case 'Icon':
        return FlutIcon.flutDecode(this, data);
      case 'Builder':
        return FlutBuilder.flutDecode(this, data);
      case 'FocusTraversalGroup':
        return FlutFocusTraversalGroup.flutDecode(this, data);
      case 'FocusTraversalOrder':
        return FlutFocusTraversalOrder.flutDecode(this, data);
      case 'FocusTraversalPolicy':
        return FlutFocusTraversalPolicy.flutDecode(this, data);
      case 'ReadingOrderTraversalPolicy':
        return FlutReadingOrderTraversalPolicy.flutDecode(this, data);
      case 'OrderedTraversalPolicy':
        return FlutOrderedTraversalPolicy.flutDecode(this, data);
      case 'WidgetOrderTraversalPolicy':
        return FlutWidgetOrderTraversalPolicy.flutDecode(this, data);
      case 'NumericFocusOrder':
        return FlutNumericFocusOrder.flutDecode(this, data);
      case 'TraversalDirection':
        return const FlutTraversalDirection().flutDecode(data);
      case 'Visibility':
        return FlutVisibility.flutDecode(this, data);
      case 'ListView':
        return FlutListView.flutDecode(this, data);
      case 'CustomScrollView':
        return FlutCustomScrollView.flutDecode(this, data);
      case 'SliverToBoxAdapter':
        return FlutSliverToBoxAdapter.flutDecode(this, data);
      case 'SliverPadding':
        return FlutSliverPadding.flutDecode(this, data);
      case 'SingleChildScrollView':
        return FlutSingleChildScrollView.flutDecode(this, data);
      case 'InteractiveViewer':
        return FlutInteractiveViewer.flutDecode(this, data);
      case 'AnimatedContainer':
        return FlutAnimatedContainer.flutDecode(this, data);
      case 'AnimatedOpacity':
        return FlutAnimatedOpacity.flutDecode(this, data);
      case 'MouseRegion':
        return FlutMouseRegion.flutDecode(this, data);
      case 'GestureDetector':
        return FlutGestureDetector.flutDecode(this, data);
      case 'RawGestureDetector':
        return FlutRawGestureDetector.flutDecode(this, data);
      case 'Draggable':
        return FlutDraggable.flutDecode(this, data);
      case 'DragTarget':
        return FlutDragTarget.flutDecode(this, data);
      case 'DraggableDetails':
        return FlutDraggableDetails.flutDecode(this, data);
      case 'DragTargetDetails':
        return FlutDragTargetDetails.flutDecode(this, data);
      case 'MaterialApp':
        return FlutMaterialApp.flutDecode(this, data);
      case 'Scaffold':
        return FlutScaffold.flutDecode(this, data);
      case 'Scrollbar':
        return FlutScrollbar.flutDecode(this, data);
      case 'Card':
        return FlutCard.flutDecode(this, data);
      case 'Divider':
        return FlutDivider.flutDecode(this, data);
      case 'CircularProgressIndicator':
        return FlutCircularProgressIndicator.flutDecode(this, data);
      case 'FloatingActionButton':
        return FlutFloatingActionButton.flutDecode(this, data);
      case 'ElevatedButton':
        return FlutElevatedButton.flutDecode(this, data);
      case 'IconButton':
        return FlutIconButton.flutDecode(this, data);
      case 'InkWell':
        return FlutInkWell.flutDecode(this, data);
      case 'TextField':
        return FlutTextField.flutDecode(this, data);
      case 'CustomPaint':
        return FlutCustomPaint.flutDecode(this, data);
      case 'Wrap':
        return FlutWrap.flutDecode(this, data);
      case 'WrapAlignment':
        return const FlutWrapAlignment().flutDecode(data);
      case 'WrapCrossAlignment':
        return const FlutWrapCrossAlignment().flutDecode(data);
      case 'Transform':
        return FlutTransform.flutDecode(this, data);
      case 'TextButton':
        return FlutTextButton.flutDecode(this, data);
      case 'OutlinedButton':
        return FlutOutlinedButton.flutDecode(this, data);
      case 'ListTile':
        return FlutListTile.flutDecode(this, data);
      case 'Switch':
        return FlutSwitch.flutDecode(this, data);
      case 'Checkbox':
        return FlutCheckbox.flutDecode(this, data);
      case 'LinearProgressIndicator':
        return FlutLinearProgressIndicator.flutDecode(this, data);
      case 'Tooltip':
        return FlutTooltip.flutDecode(this, data);
      case 'CircleAvatar':
        return FlutCircleAvatar.flutDecode(this, data);
      case 'DropdownMenu':
        return FlutDropdownMenu.flutDecode(this, data);
      case 'DropdownMenuEntry':
        return FlutDropdownMenuEntry.flutDecode(this, data);
      case 'DropdownButton':
        return FlutDropdownButton.flutDecode(this, data);
      case 'DropdownMenuItem':
        return FlutDropdownMenuItem.flutDecode(this, data);
      case 'RouteSettings':
        return FlutRouteSettings.flutDecode(this, data);
      case 'ClipboardData':
        return FlutClipboardData.flutDecode(this, data);
      case 'ValueKey':
        return FlutValueKey.flutDecode(this, data);
      case 'BoxFit':
        return const FlutBoxFit().flutDecode(data);
      case 'ImageRepeat':
        return const FlutImageRepeat().flutDecode(data);
      case 'File':
        return FlutFile.flutDecode(this, data);
      case 'Uint8List':
        return FlutUint8List.flutDecode(this, data);
      case 'Image':
        return FlutImage.flutDecode(this, data);
      case 'BoxConstraints':
        return FlutBoxConstraints.flutDecode(this, data);
      case 'Slider':
        return FlutSlider.flutDecode(this, data);
      case 'AlertDialog':
        return FlutAlertDialog.flutDecode(this, data);
      case 'Dialog':
        return FlutDialog.flutDecode(this, data);
      case 'SimpleDialog':
        return FlutSimpleDialog.flutDecode(this, data);
      case 'SimpleDialogOption':
        return FlutSimpleDialogOption.flutDecode(this, data);
      case 'Drawer':
        return FlutDrawer.flutDecode(this, data);
      case 'NavigationBar':
        return FlutNavigationBar.flutDecode(this, data);
      case 'NavigationDestination':
        return FlutNavigationDestination.flutDecode(this, data);
      case 'Radio':
        return FlutRadio.flutDecode(this, data);
      case 'RadioGroup':
        return FlutRadioGroup.flutDecode(this, data);
      case 'Chip':
        return FlutChip.flutDecode(this, data);
      case 'AspectRatio':
        return FlutAspectRatio.flutDecode(this, data);
      case 'IntrinsicWidth':
        return FlutIntrinsicWidth.flutDecode(this, data);
      case 'FittedBox':
        return FlutFittedBox.flutDecode(this, data);
      case 'ConstrainedBox':
        return FlutConstrainedBox.flutDecode(this, data);
      case 'PopupMenuItem':
        return FlutPopupMenuItem.flutDecode(this, data);
      case 'PopupMenuButton':
        return FlutPopupMenuButton.flutDecode(this, data);
      case 'PopupMenuDivider':
        return FlutPopupMenuDivider.flutDecode(this, data);
      case 'MenuBar':
        return FlutMenuBar.flutDecode(this, data);
      case 'Material':
        return FlutMaterial.flutDecode(this, data);
      case 'MaterialType':
        return const FlutMaterialType().flutDecode(data);
      case 'MenuAnchor':
        return FlutMenuAnchor.flutDecode(this, data);
      case 'MenuItemButton':
        return FlutMenuItemButton.flutDecode(this, data);
      case 'SubmenuButton':
        return FlutSubmenuButton.flutDecode(this, data);
      case 'MenuAcceleratorLabel':
        return FlutMenuAcceleratorLabel.flutDecode(this, data);
      case 'PlatformMenuBar':
        return FlutPlatformMenuBar.flutDecode(this, data);
      case 'PlatformMenu':
        return FlutPlatformMenu.flutDecode(this, data);
      case 'PlatformMenuItem':
        return FlutPlatformMenuItem.flutDecode(this, data);
      case 'PlatformMenuItemGroup':
        return FlutPlatformMenuItemGroup.flutDecode(this, data);
      case 'PlatformProvidedMenuItem':
        return FlutPlatformProvidedMenuItem.flutDecode(this, data);
      case 'ExpansionTile':
        return FlutExpansionTile.flutDecode(this, data);
      case 'DefaultTabController':
        return FlutDefaultTabController.flutDecode(this, data);
      case 'TabBar':
        return FlutTabBar.flutDecode(this, data);
      case 'TabBarView':
        return FlutTabBarView.flutDecode(this, data);
      case 'Tab':
        return FlutTab.flutDecode(this, data);
      case 'Form':
        return FlutForm.flutDecode(this, data);
      case 'TextFormField':
        return FlutTextFormField.flutDecode(this, data);
      case 'AutovalidateMode':
        return const FlutAutovalidateMode().flutDecode(data);
      case 'AxisDirection':
        return const FlutAxisDirection().flutDecode(data);
      case 'NotificationListener':
        return FlutNotificationListener.flutDecode(this, data);
      case 'LayoutBuilder':
        return FlutLayoutBuilder.flutDecode(this, data);
      case 'ListenableBuilder':
        return FlutListenableBuilder.flutDecode(this, data);
      case 'AnimatedBuilder':
        return FlutAnimatedBuilder.flutDecode(this, data);
      case 'ValueListenableBuilder':
        return FlutValueListenableBuilder.flutDecode(this, data);
      case 'BoxShadow':
        return FlutBoxShadow.flutDecode(this, data);
      case 'GradientRotation':
        return FlutGradientRotation.flutDecode(this, data);
      case 'LinearGradient':
        return FlutLinearGradient.flutDecode(this, data);
      case 'RadialGradient':
        return FlutRadialGradient.flutDecode(this, data);
      case 'SweepGradient':
        return FlutSweepGradient.flutDecode(this, data);
      case 'AnimationStatus':
        return const FlutAnimationStatus().flutDecode(data);
      case 'NavigationDestinationLabelBehavior':
        return const FlutNavigationDestinationLabelBehavior().flutDecode(data);
      case 'PopupMenuPosition':
        return const FlutPopupMenuPosition().flutDecode(data);
      case 'ListTileControlAffinity':
        return const FlutListTileControlAffinity().flutDecode(data);
      case 'IconAlignment':
        return const FlutIconAlignment().flutDecode(data);
      case 'SliderInteraction':
        return const FlutSliderInteraction().flutDecode(data);
      case 'ShowValueIndicator':
        return const FlutShowValueIndicator().flutDecode(data);
      case 'OverflowBarAlignment':
        return const FlutOverflowBarAlignment().flutDecode(data);
      case 'SliverPaintOrder':
        return const FlutSliverPaintOrder().flutDecode(data);
      case 'DropdownMenuCloseBehavior':
        return const FlutDropdownMenuCloseBehavior().flutDecode(data);
      case 'SingleActivator':
        return FlutSingleActivator.flutDecode(this, data);
      case 'CharacterActivator':
        return FlutCharacterActivator.flutDecode(this, data);
      case 'Actions':
        return FlutActions.flutDecode(this, data);
      case 'Shortcuts':
        return FlutShortcuts.flutDecode(this, data);
      case 'CallbackShortcuts':
        return FlutCallbackShortcuts.flutDecode(this, data);
      case 'Velocity':
        return FlutVelocity.flutDecode(this, data);
      case 'DragStartDetails':
        return FlutDragStartDetails.flutDecode(this, data);
      case 'DragUpdateDetails':
        return FlutDragUpdateDetails.flutDecode(this, data);
      case 'DragEndDetails':
        return FlutDragEndDetails.flutDecode(this, data);
      case 'KeyEvent':
        return FlutKeyEvent.flutDecode(this, data);
      case 'KeyDownEvent':
        return FlutKeyDownEvent.flutDecode(this, data);
      case 'KeyUpEvent':
        return FlutKeyUpEvent.flutDecode(this, data);
      case 'KeyRepeatEvent':
        return FlutKeyRepeatEvent.flutDecode(this, data);
      case 'Callable':
        return FlutCallableRef.flutDecode(this, data);
      case 'Double':
        return FlutDouble.decode(data);
      case 'MediaQueryData':
        return FlutMediaQueryData.flutDecode(this, data);
      case 'ThemeMode':
        return const FlutThemeMode().flutDecode(data);
      case 'HitTestBehavior':
        return const FlutHitTestBehavior().flutDecode(data);
      case 'TraversalEdgeBehavior':
        return const FlutTraversalEdgeBehavior().flutDecode(data);
      case 'AnimationBehavior':
        return const FlutAnimationBehavior().flutDecode(data);
      case 'LockState':
        return const FlutLockState().flutDecode(data);
      case 'PanAxis':
        return const FlutPanAxis().flutDecode(data);
      case 'ScrollViewKeyboardDismissBehavior':
        return const FlutScrollViewKeyboardDismissBehavior().flutDecode(data);
      case 'VerticalDirection':
        return const FlutVerticalDirection().flutDecode(data);
      case 'TextInputAction':
        return const FlutTextInputAction().flutDecode(data);
      case 'RoundedRectangleBorder':
        return FlutRoundedRectangleBorder.flutDecode(this, data);
      case 'CircleBorder':
        return FlutCircleBorder.flutDecode(this, data);
      case 'StadiumBorder':
        return FlutStadiumBorder.flutDecode(this, data);
      case 'BeveledRectangleBorder':
        return FlutBeveledRectangleBorder.flutDecode(this, data);
      case 'ContinuousRectangleBorder':
        return FlutContinuousRectangleBorder.flutDecode(this, data);
      case 'ScrollPhysics':
        return FlutScrollPhysics.flutDecode(this, data);
      case 'BouncingScrollPhysics':
        return FlutBouncingScrollPhysics.flutDecode(this, data);
      case 'ClampingScrollPhysics':
        return FlutClampingScrollPhysics.flutDecode(this, data);
      case 'NeverScrollableScrollPhysics':
        return FlutNeverScrollableScrollPhysics.flutDecode(this, data);
      case 'AlwaysScrollableScrollPhysics':
        return FlutAlwaysScrollableScrollPhysics.flutDecode(this, data);
      case 'ScrollDecelerationRate':
        return const FlutScrollDecelerationRate().flutDecode(data);
      case 'VisualDensity':
        return FlutVisualDensity.flutDecode(this, data);
      case 'TextInputType':
        return FlutTextInputType.flutDecode(this, data);
      case 'ScrollBehavior':
        return FlutScrollBehavior.flutDecode(this, data);
      case 'IconThemeData':
        return FlutIconThemeData.flutDecode(this, data);
      case 'ChipAnimationStyle':
        return FlutChipAnimationStyle.flutDecode(this, data);
      case 'MenuStyle':
        return FlutMenuStyle.flutDecode(this, data);
      case 'PlatformProvidedMenuItemType':
        return const FlutPlatformProvidedMenuItemType().flutDecode(data);
      case 'TextEditingController':
      case 'ScrollController':
      case 'FocusNode':
      case 'FocusScopeNode':
      case 'ColorScheme':
      case 'ThemeData':
      case 'WidgetStateColor':
      case 'WidgetStateProperty':
      case 'WidgetStatePropertyAll':
      case 'PageRoute':
      case 'MaterialPageRoute':
      case 'ModalRoute':
      case 'HardwareKeyboard':
      case 'SchedulerBinding':
      case 'ScrollPosition':
      case 'BuildContext':
      case 'Canvas':
      case 'ExpansibleController':
      case 'GlobalKey':
      case 'RenderBox':
      case 'FormState':
      case 'NavigatorState':
      case 'OverlayState':
      case 'OverlayEntry':
      case 'ValueNotifier':
      case 'MagnifierController':
      case 'AnimationController':
      case 'TabController':
      case 'MenuController':
      case 'RenderObject':
      case 'FormFieldState':
      case 'TransformationController':
      case 'WidgetStatesController':
      case 'ButtonStyle':
      case 'InteractiveInkFeatureFactory':
      case 'TapGestureRecognizer':
      case 'LongPressGestureRecognizer':
        throw FlutRuntimeException(
          '$type is a realtime object. '
          'It must be created via createObject and resolved by OID.',
        );
      default:
        throw FlutUnknownTypeException(type);
    }
  }

  dynamic encodeValue(dynamic value) {
    if (value == null) return null;
    if (value is double) return FlutDouble.encode(value);
    if (value is num || value is String || value is bool) return value;
    if (value is Function) {
      final cid = _callableRegistry[value];
      if (cid != null) {
        return {'_flut_type': 'Callable', '_flut_cid': cid};
      }
      return null;
    }
    if (value is Uint8List) return FlutUint8List(value).flutEncode();
    if (value is List) return value.map(encodeValue).toList();
    if (value is Map) {
      return value.map((k, v) => MapEntry(k, encodeValue(v)));
    }
    if (value is Future) return FlutFuture.wrap(this, value).flutEncode();
    if (value is FlutValueObject) return value.flutEncode();
    if (value is FlutRealtimeObject) return value.flutEncode();

    final hash = identityHashCode(value);
    final existingOid = _hashToOid[hash];
    if (existingOid != null) {
      final existing = objectRegistry[existingOid];
      if (existing != null) return existing.flutEncode();
    }

    if (value is WidgetStateColor) {
      final wrapper = wrapObject<FlutWidgetStateColor>(
        value,
        (oid) => FlutWidgetStateColor.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is InteractiveInkFeatureFactory) {
      final wrapper = wrapObject<FlutInteractiveInkFeatureFactory>(
        value,
        (oid) => FlutInteractiveInkFeatureFactory.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is TapGestureRecognizer) {
      final wrapper = wrapObject<FlutTapGestureRecognizer>(
        value,
        (oid) => FlutTapGestureRecognizer.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is LongPressGestureRecognizer) {
      final wrapper = wrapObject<FlutLongPressGestureRecognizer>(
        value,
        (oid) => FlutLongPressGestureRecognizer.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is Matrix4) return FlutMatrix4(value).flutEncode();
    if (value is Color) return FlutColor(value).flutEncode();
    if (value is BoxShadow) return FlutBoxShadow(value).flutEncode();
    if (value is Shadow) return FlutShadow(value).flutEncode();
    if (value is Size) return FlutSize(value).flutEncode();
    if (value is Radius) return FlutRadius(value).flutEncode();
    if (value is Offset) return FlutOffset(value).flutEncode();
    if (value is Rect) return FlutRect(value).flutEncode();
    if (value is RRect) return FlutRRect(value).flutEncode();
    if (value is RelativeRect) return FlutRelativeRect(value).flutEncode();
    if (value is ViewPadding) return FlutViewPadding(value).flutEncode();
    if (value is EdgeInsets) return FlutEdgeInsets(value).flutEncode();
    if (value is EdgeInsetsDirectional) {
      return FlutEdgeInsetsDirectional(value).flutEncode();
    }
    if (value is EdgeInsetsGeometry) {
      return FlutEdgeInsetsGeometry(value).flutEncode();
    }
    if (value is ButtonStyle) {
      final wrapper = wrapObject<FlutButtonStyle>(
        value,
        (oid) => FlutButtonStyle.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is ColorScheme) {
      final wrapper = wrapObject<FlutColorScheme>(
        value,
        (oid) => FlutColorScheme.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is ThemeData) {
      final wrapper = wrapObject<FlutThemeData>(
        value,
        (oid) => FlutThemeData.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is TextTheme) return FlutTextTheme(value).flutEncode();
    if (value is TextStyle) return FlutTextStyle(value).flutEncode();
    if (value is TextSelection) return FlutTextSelection(value).flutEncode();
    if (value is SelectedContent) {
      return FlutSelectedContent(value).flutEncode();
    }
    if (value is SelectedContentRange) {
      return FlutSelectedContentRange(value).flutEncode();
    }
    if (value is SelectionPoint) return FlutSelectionPoint(value).flutEncode();
    if (value is SelectionGeometry) {
      return FlutSelectionGeometry(value).flutEncode();
    }
    if (value is SelectAllSelectionEvent) {
      return FlutSelectAllSelectionEvent(value).flutEncode();
    }
    if (value is ClearSelectionEvent) {
      return FlutClearSelectionEvent(value).flutEncode();
    }
    if (value is SelectWordSelectionEvent) {
      return FlutSelectWordSelectionEvent(value).flutEncode();
    }
    if (value is SelectParagraphSelectionEvent) {
      return FlutSelectParagraphSelectionEvent(value).flutEncode();
    }
    if (value is SelectionEdgeUpdateEvent) {
      return FlutSelectionEdgeUpdateEvent(value).flutEncode();
    }
    if (value is GranularlyExtendSelectionEvent) {
      return FlutGranularlyExtendSelectionEvent(value).flutEncode();
    }
    if (value is DirectionallyExtendSelectionEvent) {
      return FlutDirectionallyExtendSelectionEvent(value).flutEncode();
    }
    if (value is TextMagnifierConfiguration) {
      return FlutTextMagnifierConfiguration(value).flutEncode();
    }
    if (value is MagnifierInfo) return FlutMagnifierInfo(value).flutEncode();
    if (value is TextSelectionToolbarAnchors) {
      return FlutTextSelectionToolbarAnchors(value).flutEncode();
    }
    if (value is EmptyTextSelectionControls) {
      return FlutEmptyTextSelectionControls(value).flutEncode();
    }
    if (value is StaticSelectionContainerDelegate) {
      return FlutStaticSelectionContainerDelegate(value).flutEncode();
    }
    if (value is TextSelectionThemeData) {
      return FlutTextSelectionThemeData(value).flutEncode();
    }
    if (value is MediaQueryData) return FlutMediaQueryData(value).flutEncode();
    if (value is DeviceGestureSettings) {
      return FlutDeviceGestureSettings(value).flutEncode();
    }
    if (value is TextScaler) return FlutTextScaler(value).flutEncode();
    if (value is DragStartDetails) {
      return FlutDragStartDetails(value).flutEncode();
    }
    if (value is DragUpdateDetails) {
      return FlutDragUpdateDetails(value).flutEncode();
    }
    if (value is DragEndDetails) return FlutDragEndDetails(value).flutEncode();
    if (value is DragDownDetails) {
      return FlutDragDownDetails(value).flutEncode();
    }
    if (value is LongPressStartDetails) {
      return FlutLongPressStartDetails(value).flutEncode();
    }
    if (value is LongPressDownDetails) {
      return FlutLongPressDownDetails(value).flutEncode();
    }
    if (value is LongPressMoveUpdateDetails) {
      return FlutLongPressMoveUpdateDetails(value).flutEncode();
    }
    if (value is LongPressEndDetails) {
      return FlutLongPressEndDetails(value).flutEncode();
    }
    if (value is TapDownDetails) return FlutTapDownDetails(value).flutEncode();
    if (value is TapUpDetails) return FlutTapUpDetails(value).flutEncode();
    if (value is TapMoveDetails) return FlutTapMoveDetails(value).flutEncode();
    if (value is ScaleStartDetails) {
      return FlutScaleStartDetails(value).flutEncode();
    }
    if (value is ScaleUpdateDetails) {
      return FlutScaleUpdateDetails(value).flutEncode();
    }
    if (value is ScaleEndDetails) {
      return FlutScaleEndDetails(value).flutEncode();
    }
    if (value is DraggableDetails) {
      return FlutDraggableDetails(value).flutEncode();
    }
    if (value is DragTargetDetails) {
      return FlutDragTargetDetails(value, this).flutEncode();
    }
    if (value is DropdownMenuEntry) {
      return FlutDropdownMenuEntry(value).flutEncode();
    }
    if (value is Velocity) return FlutVelocity(value).flutEncode();
    if (value is ScrollUpdateNotification) {
      return FlutScrollUpdateNotification(value).flutEncode();
    }
    if (value is OverscrollNotification) {
      return FlutOverscrollNotification(value).flutEncode();
    }
    if (value is ScrollStartNotification) {
      return FlutScrollStartNotification(value).flutEncode();
    }
    if (value is ScrollEndNotification) {
      return FlutScrollEndNotification(value).flutEncode();
    }
    if (value is ScrollNotification) {
      return FlutScrollNotification(value).flutEncode();
    }
    if (value is PointerEnterEvent) {
      return FlutPointerEnterEvent(value).flutEncode();
    }
    if (value is PointerExitEvent) {
      return FlutPointerExitEvent(value).flutEncode();
    }
    if (value is PointerDownEvent) {
      return FlutPointerDownEvent(value).flutEncode();
    }
    if (value is PointerUpEvent) {
      return FlutPointerUpEvent(value).flutEncode();
    }
    if (value is PointerEvent) return FlutPointerEvent(value).flutEncode();
    if (value is KeyDownEvent) return FlutKeyDownEvent(value).flutEncode();
    if (value is KeyUpEvent) return FlutKeyUpEvent(value).flutEncode();
    if (value is KeyRepeatEvent) return FlutKeyRepeatEvent(value).flutEncode();
    if (value is KeyEvent) return FlutKeyEvent(value).flutEncode();
    if (value is Duration) return FlutDuration(value).flutEncode();
    if (value is FontWeight) return FlutFontWeight(value).flutEncode();
    if (value is TextDecoration) return FlutTextDecoration(value).flutEncode();
    if (value is LogicalKeyboardKey) {
      return FlutLogicalKeyboardKey(value).flutEncode();
    }
    if (value is PhysicalKeyboardKey) {
      return FlutPhysicalKeyboardKey(value).flutEncode();
    }
    if (value is AlignmentDirectional) {
      return FlutAlignmentDirectional(value).flutEncode();
    }
    if (value is Alignment) return FlutAlignment(value).flutEncode();
    if (value is AlignmentGeometry) {
      return FlutAlignmentGeometry(value).flutEncode();
    }
    if (value is IconData) return FlutIconData(value).flutEncode();
    if (value is BorderRadius) return FlutBorderRadius(value).flutEncode();
    if (value is BorderRadiusDirectional) {
      return FlutBorderRadiusDirectional(value).flutEncode();
    }
    if (value is BorderRadiusGeometry) {
      return FlutBorderRadiusGeometry(value).flutEncode();
    }
    if (value is BorderSide) return FlutBorderSide(value).flutEncode();
    if (value is Border) return FlutBorder(value).flutEncode();
    if (value is BoxDecoration) return FlutBoxDecoration(value).flutEncode();
    if (value is LinearGradient) {
      return FlutLinearGradient(value).flutEncode();
    }
    if (value is RadialGradient) {
      return FlutRadialGradient(value).flutEncode();
    }
    if (value is SweepGradient) {
      return FlutSweepGradient(value).flutEncode();
    }
    if (value is WidgetSpan) return FlutWidgetSpan(value).flutEncode();
    if (value is TextSpan) return FlutTextSpan(value).flutEncode();
    if (value is InputDecoration) {
      return FlutInputDecoration(value).flutEncode();
    }
    if (value is InputBorder) return FlutInputBorder(value).flutEncode();
    if (value is Curve) return FlutCurve(value).flutEncode();
    if (value is AnimationStyle) {
      return FlutAnimationStyle(value).flutEncode();
    }
    if (value is Paint) return FlutPaint(value).flutEncode();
    if (value is MaskFilter) return FlutMaskFilter(value).flutEncode();
    if (value is ColorFilter) return FlutColorFilter(value).flutEncode();
    if (value is ImageFilter) return FlutImageFilter(value).flutEncode();
    if (value is BoxConstraints) {
      return FlutBoxConstraints(value).flutEncode();
    }
    if (value is VisualDensity) {
      return FlutVisualDensity(value).flutEncode();
    }
    if (value is TextInputType) {
      return FlutTextInputType(value).flutEncode();
    }
    if (value is BouncingScrollPhysics) {
      return FlutBouncingScrollPhysics(value).flutEncode();
    }
    if (value is ClampingScrollPhysics) {
      return FlutClampingScrollPhysics(value).flutEncode();
    }
    if (value is NeverScrollableScrollPhysics) {
      return FlutNeverScrollableScrollPhysics(value).flutEncode();
    }
    if (value is AlwaysScrollableScrollPhysics) {
      return FlutAlwaysScrollableScrollPhysics(value).flutEncode();
    }
    if (value is ScrollPhysics) {
      return FlutScrollPhysics(value).flutEncode();
    }
    if (value is ScrollDecelerationRate) {
      return const FlutScrollDecelerationRate().flutEncode(value);
    }

    if (value is ScrollPosition) {
      final wrapper = wrapObject<FlutScrollPosition>(
        value,
        (oid) => FlutScrollPosition.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is BuildContext) {
      final wrapper = wrapObject<FlutBuildContext>(
        value,
        (oid) => FlutBuildContext.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is SelectableRegionState) {
      final wrapper = wrapObject<FlutSelectableRegionState>(
        value,
        (oid) => FlutSelectableRegionState.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is FormState) {
      final wrapper = wrapObject<FlutFormState>(
        value,
        (oid) => FlutFormState.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is NavigatorState) {
      final wrapper = wrapObject<FlutNavigatorState>(
        value,
        (oid) => FlutNavigatorState.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is OverlayState) {
      final wrapper = wrapObject<FlutOverlayState>(
        value,
        (oid) => FlutOverlayState.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is RenderBox) {
      final wrapper = wrapObject<FlutRenderBox>(
        value,
        (oid) => FlutRenderBox.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is RenderObject) {
      final wrapper = wrapObject<FlutRenderObject>(
        value,
        (oid) => FlutRenderObject.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is FocusScopeNode) {
      final wrapper = wrapObject<FlutFocusScopeNode>(
        value,
        (oid) => FlutFocusScopeNode.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is FocusNode) {
      final wrapper = wrapObject<FlutFocusNode>(
        value,
        (oid) => FlutFocusNode.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is TransformationController) {
      final wrapper = wrapObject<FlutTransformationController>(
        value,
        (oid) => FlutTransformationController.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is ValueNotifier) {
      final wrapper = wrapObject<FlutValueNotifier>(
        value,
        (oid) => FlutValueNotifier.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is MagnifierController) {
      final wrapper = wrapObject<FlutMagnifierController>(
        value,
        (oid) => FlutMagnifierController.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is TabController) {
      final wrapper = wrapObject<FlutTabController>(
        value,
        (oid) => FlutTabController.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is MenuController) {
      final wrapper = wrapObject<FlutMenuController>(
        value,
        (oid) => FlutMenuController.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is FormFieldState) {
      final wrapper = wrapObject<FlutFormFieldState>(
        value,
        (oid) => FlutFormFieldState.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    if (value is Set) {
      return {'_flut_type': 'Set', 'values': value.map(encodeValue).toList()};
    }
    if (value is WidgetState) {
      return const FlutWidgetState().flutEncode(value);
    }
    if (value is AnimationStatus) {
      return const FlutAnimationStatus().flutEncode(value);
    }
    if (value is BlurStyle) {
      return const FlutBlurStyle().flutEncode(value);
    }
    if (value is Brightness) {
      return const FlutBrightness().flutEncode(value);
    }
    if (value is NavigationMode) {
      return const FlutNavigationMode().flutEncode(value);
    }
    if (value is Orientation) {
      return const FlutOrientation().flutEncode(value);
    }
    if (value is ColorSpace) {
      return const FlutColorSpace().flutEncode(value);
    }
    if (value is TextAffinity) {
      return const FlutTextAffinity().flutEncode(value);
    }
    if (value is SelectionChangedCause) {
      return const FlutSelectionChangedCause().flutEncode(value);
    }
    if (value is SelectionStatus) {
      return const FlutSelectionStatus().flutEncode(value);
    }
    if (value is SelectableRegionSelectionStatus) {
      return const FlutSelectableRegionSelectionStatus().flutEncode(value);
    }

    if (value is RouteSettings) return FlutRouteSettings(value).flutEncode();
    if (value is ClipboardData) return FlutClipboardData(value).flutEncode();

    if (value is MaterialPageRoute) {
      final wrapper = wrapObject<FlutMaterialPageRoute>(
        value,
        (oid) => FlutMaterialPageRoute.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is PageRoute) {
      final wrapper = wrapObject<FlutPageRoute>(
        value,
        (oid) => FlutPageRoute.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }
    if (value is ModalRoute) {
      final wrapper = wrapObject<FlutModalRoute>(
        value,
        (oid) => FlutModalRoute.createFromObject(
          runtime: this,
          oid: oid,
          target: value,
        ),
      );
      return wrapper.flutEncode();
    }

    throw FlutEncodeException(value.runtimeType);
  }

  T wrapObject<T extends FlutRealtimeObject>(
    Object dartObj,
    T Function(int oid) factory, {
    int? requestedOid,
  }) {
    final hash = identityHashCode(dartObj);

    final existingOid = _hashToOid[hash];
    if (existingOid != null) {
      final existing = objectRegistry[existingOid];
      if (existing != null) {
        if (requestedOid != null && existingOid != requestedOid) {
          throw FlutOidConflictException(existingOid, requestedOid);
        }
        return existing as T;
      }
    }

    final oid = requestedOid ?? generateOid();

    if (objectRegistry.containsKey(oid)) {
      throw FlutOidInUseException(oid);
    }

    final wrapper = factory(oid);
    objectRegistry[oid] = wrapper;
    _hashToOid[hash] = oid;

    return wrapper;
  }

  void releaseObject(int oid) {
    final wrapper = objectRegistry.remove(oid);
    if (wrapper != null) {
      _hashToOid.removeWhere((_, v) => v == oid);
    }
  }

  void signalObjectDisposed(int oid) {
    releaseObject(oid);
    flutNative.invokeNativeAsync('realtime_dispose', {'oid': oid});
  }
}
