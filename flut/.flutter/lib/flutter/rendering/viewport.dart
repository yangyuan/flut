import 'package:flutter/rendering.dart';
import 'package:flut/flut/object.dart';

class FlutSliverPaintOrder extends FlutEnumObject<SliverPaintOrder> {
  const FlutSliverPaintOrder()
    : super('SliverPaintOrder', const {
        'firstIsTop': SliverPaintOrder.firstIsTop,
        'lastIsTop': SliverPaintOrder.lastIsTop,
      });
}
