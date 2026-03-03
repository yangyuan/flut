import 'package:flutter/material.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flutter/widgets/scroll_metrics.dart';
import 'package:flut/flutter/gestures/drag_details.dart';

class FlutScrollNotification extends FlutValueObject {
  final ScrollNotification notification;
  FlutScrollNotification(this.notification) : super('ScrollNotification');
  FlutScrollNotification._(this.notification, String type) : super(type);

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['metrics'] = FlutScrollMetrics(notification.metrics).flutEncode();
    result['depth'] = notification.depth;
    return result;
  }
}

class FlutScrollStartNotification extends FlutScrollNotification {
  FlutScrollStartNotification(ScrollStartNotification notification)
    : super._(notification, 'ScrollStartNotification');

  @override
  Map<String, dynamic> flutEncode() {
    final result = super.flutEncode();
    final n = notification as ScrollStartNotification;
    if (n.dragDetails != null) {
      result['dragDetails'] = FlutDragStartDetails(n.dragDetails!).flutEncode();
    }
    return result;
  }

  static ScrollStartNotification? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return null;
  }
}

class FlutScrollUpdateNotification extends FlutScrollNotification {
  FlutScrollUpdateNotification(ScrollUpdateNotification notification)
    : super._(notification, 'ScrollUpdateNotification');

  @override
  Map<String, dynamic> flutEncode() {
    final result = super.flutEncode();
    final n = notification as ScrollUpdateNotification;
    if (n.scrollDelta != null) {
      result['scrollDelta'] = n.scrollDelta;
    }
    if (n.dragDetails != null) {
      result['dragDetails'] = FlutDragUpdateDetails(
        n.dragDetails!,
      ).flutEncode();
    }
    return result;
  }
}

class FlutScrollEndNotification extends FlutScrollNotification {
  FlutScrollEndNotification(ScrollEndNotification notification)
    : super._(notification, 'ScrollEndNotification');

  @override
  Map<String, dynamic> flutEncode() {
    final result = super.flutEncode();
    final n = notification as ScrollEndNotification;
    if (n.dragDetails != null) {
      result['dragDetails'] = FlutDragEndDetails(n.dragDetails!).flutEncode();
    }
    return result;
  }
}

class FlutOverscrollNotification extends FlutScrollNotification {
  FlutOverscrollNotification(OverscrollNotification notification)
    : super._(notification, 'OverscrollNotification');

  @override
  Map<String, dynamic> flutEncode() {
    final result = super.flutEncode();
    final n = notification as OverscrollNotification;
    result['overscroll'] = n.overscroll;
    result['velocity'] = n.velocity;
    if (n.dragDetails != null) {
      result['dragDetails'] = FlutDragUpdateDetails(
        n.dragDetails!,
      ).flutEncode();
    }
    return result;
  }
}
