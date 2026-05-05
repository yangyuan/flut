import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flutter/rendering.dart';

class FlutCenter {
  FlutCenter._();

  static Center? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Center(
      key: runtime.decodeKey(data),
      widthFactor: data['widthFactor'] as double?,
      heightFactor: data['heightFactor'] as double?,
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutPadding {
  FlutPadding._();

  static Padding? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Padding(
      key: runtime.decodeKey(data),
      padding: runtime.unpackRequiredField<EdgeInsets>(data, 'padding'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutIgnorePointer {
  FlutIgnorePointer._();

  static IgnorePointer? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return IgnorePointer(
      key: runtime.decodeKey(data),
      ignoring: runtime.unpackRequiredField<bool>(data, 'ignoring'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutRichText {
  FlutRichText._();

  static RichText? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return RichText(
      key: runtime.decodeKey(data),
      text: runtime.unpackRequiredField<InlineSpan>(data, 'text'),
      textAlign: runtime.unpackRequiredField<TextAlign>(data, 'textAlign'),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      softWrap: runtime.unpackRequiredField<bool>(data, 'softWrap'),
      overflow: runtime.unpackRequiredField<TextOverflow>(data, 'overflow'),
      textScaler: runtime.unpackRequiredField<TextScaler>(data, 'textScaler'),
      maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
      locale: runtime.unpackOptionalField<Locale>(data, 'locale'),
      strutStyle: runtime.unpackOptionalField<StrutStyle>(data, 'strutStyle'),
      textWidthBasis: runtime.unpackRequiredField<TextWidthBasis>(
        data,
        'textWidthBasis',
      ),
      textHeightBehavior: runtime.unpackOptionalField<TextHeightBehavior>(
        data,
        'textHeightBehavior',
      ),
      selectionRegistrar: runtime.unpackOptionalField<SelectionRegistrar>(
        data,
        'selectionRegistrar',
      ),
      selectionColor: runtime.unpackOptionalField<Color>(
        data,
        'selectionColor',
      ),
    );
  }
}

class FlutAlign {
  FlutAlign._();

  static Align? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Align(
      key: runtime.decodeKey(data),
      alignment: runtime.unpackRequiredField<Alignment>(data, 'alignment'),
      widthFactor: data['widthFactor'] as double?,
      heightFactor: data['heightFactor'] as double?,
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutOpacity {
  FlutOpacity._();

  static Opacity? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Opacity(
      key: runtime.decodeKey(data),
      opacity: runtime.unpackRequiredField<double>(data, 'opacity'),
      alwaysIncludeSemantics: runtime.unpackRequiredField<bool>(
        data,
        'alwaysIncludeSemantics',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutClipRRect {
  FlutClipRRect._();

  static ClipRRect? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ClipRRect(
      key: runtime.decodeKey(data),
      borderRadius: runtime.unpackRequiredField<BorderRadiusGeometry>(
        data,
        'borderRadius',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutSizedBox {
  FlutSizedBox._();

  static SizedBox? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'expand':
        return SizedBox.expand(
          key: runtime.decodeKey(data),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'shrink':
        return SizedBox.shrink(
          key: runtime.decodeKey(data),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'fromSize':
        return SizedBox.fromSize(
          key: runtime.decodeKey(data),
          size: runtime.unpackOptionalField<Size>(data, 'size'),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'square':
        return SizedBox.square(
          key: runtime.decodeKey(data),
          dimension: runtime.unpackOptionalField<double>(data, 'dimension'),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      default:
        return SizedBox(
          key: runtime.decodeKey(data),
          width: runtime.unpackOptionalField<double>(data, 'width'),
          height: runtime.unpackOptionalField<double>(data, 'height'),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
    }
  }
}

class FlutExpanded {
  FlutExpanded._();

  static Expanded? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Expanded(
      key: runtime.decodeKey(data),
      flex: runtime.unpackRequiredField<int>(data, 'flex'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutFlexible {
  FlutFlexible._();

  static Flexible? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Flexible(
      key: runtime.decodeKey(data),
      flex: runtime.unpackRequiredField<int>(data, 'flex'),
      fit: runtime.unpackRequiredField<FlexFit>(data, 'fit'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutColumn {
  FlutColumn._();

  static Column? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Column(
      key: runtime.decodeKey(data),
      mainAxisAlignment: runtime.unpackRequiredField<MainAxisAlignment>(
        data,
        'mainAxisAlignment',
      ),
      mainAxisSize: runtime.unpackRequiredField<MainAxisSize>(
        data,
        'mainAxisSize',
      ),
      crossAxisAlignment: runtime.unpackRequiredField<CrossAxisAlignment>(
        data,
        'crossAxisAlignment',
      ),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      verticalDirection: runtime.unpackRequiredField<VerticalDirection>(
        data,
        'verticalDirection',
      ),
      textBaseline: runtime.unpackOptionalField<TextBaseline>(
        data,
        'textBaseline',
      ),
      spacing: runtime.unpackRequiredField<double>(data, 'spacing'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutRow {
  FlutRow._();

  static Row? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Row(
      key: runtime.decodeKey(data),
      mainAxisAlignment: runtime.unpackRequiredField<MainAxisAlignment>(
        data,
        'mainAxisAlignment',
      ),
      mainAxisSize: runtime.unpackRequiredField<MainAxisSize>(
        data,
        'mainAxisSize',
      ),
      crossAxisAlignment: runtime.unpackRequiredField<CrossAxisAlignment>(
        data,
        'crossAxisAlignment',
      ),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      verticalDirection: runtime.unpackRequiredField<VerticalDirection>(
        data,
        'verticalDirection',
      ),
      textBaseline: runtime.unpackOptionalField<TextBaseline>(
        data,
        'textBaseline',
      ),
      spacing: runtime.unpackRequiredField<double>(data, 'spacing'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutStack {
  FlutStack._();

  static Stack? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Stack(
      key: runtime.decodeKey(data),
      alignment: runtime.unpackRequiredField<AlignmentGeometry>(
        data,
        'alignment',
      ),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      fit: runtime.unpackRequiredField<StackFit>(data, 'fit'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutPositioned {
  FlutPositioned._();

  static Positioned? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return Positioned(
      key: runtime.decodeKey(data),
      left: runtime.unpackOptionalField<double>(data, 'left'),
      top: runtime.unpackOptionalField<double>(data, 'top'),
      right: runtime.unpackOptionalField<double>(data, 'right'),
      bottom: runtime.unpackOptionalField<double>(data, 'bottom'),
      width: runtime.unpackOptionalField<double>(data, 'width'),
      height: runtime.unpackOptionalField<double>(data, 'height'),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}

class FlutMouseRegion {
  FlutMouseRegion._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return MouseRegion(
      key: runtime.decodeKey(data),
      cursor: runtime.unpackRequiredField<MouseCursor>(data, 'cursor'),
      onEnter: runtime.unpackOptionalCallback(data, 'onEnter'),
      onExit: runtime.unpackOptionalCallback(data, 'onExit'),
      onHover: runtime.unpackOptionalCallback(data, 'onHover'),
      opaque: runtime.unpackRequiredField<bool>(data, 'opaque'),
      hitTestBehavior: runtime.unpackOptionalField<HitTestBehavior>(
        data,
        'hitTestBehavior',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutWrap {
  FlutWrap._();

  static Wrap? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Wrap(
      key: runtime.decodeKey(data),
      direction: runtime.unpackRequiredField<Axis>(data, 'direction'),
      alignment: runtime.unpackRequiredField<WrapAlignment>(data, 'alignment'),
      spacing: runtime.unpackRequiredField<double>(data, 'spacing'),
      runAlignment: runtime.unpackRequiredField<WrapAlignment>(
        data,
        'runAlignment',
      ),
      runSpacing: runtime.unpackRequiredField<double>(data, 'runSpacing'),
      crossAxisAlignment: runtime.unpackRequiredField<WrapCrossAlignment>(
        data,
        'crossAxisAlignment',
      ),
      textDirection: runtime.unpackOptionalField<TextDirection>(
        data,
        'textDirection',
      ),
      verticalDirection: runtime.unpackRequiredField<VerticalDirection>(
        data,
        'verticalDirection',
      ),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}

class FlutTransform {
  FlutTransform._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'rotate':
        return Transform.rotate(
          key: runtime.decodeKey(data),
          angle: runtime.unpackRequiredField<double>(data, 'angle'),
          origin: runtime.unpackOptionalField<Offset>(data, 'origin'),
          alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
          transformHitTests: runtime.unpackRequiredField<bool>(
            data,
            'transformHitTests',
          ),
          filterQuality: runtime.unpackOptionalField<FilterQuality>(
            data,
            'filterQuality',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'scale':
        return Transform.scale(
          key: runtime.decodeKey(data),
          scale: runtime.unpackOptionalField<double>(data, 'scale'),
          scaleX: runtime.unpackOptionalField<double>(data, 'scaleX'),
          scaleY: runtime.unpackOptionalField<double>(data, 'scaleY'),
          origin: runtime.unpackOptionalField<Offset>(data, 'origin'),
          alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
          transformHitTests: runtime.unpackRequiredField<bool>(
            data,
            'transformHitTests',
          ),
          filterQuality: runtime.unpackOptionalField<FilterQuality>(
            data,
            'filterQuality',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'translate':
        return Transform.translate(
          key: runtime.decodeKey(data),
          offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
          transformHitTests: runtime.unpackRequiredField<bool>(
            data,
            'transformHitTests',
          ),
          filterQuality: runtime.unpackOptionalField<FilterQuality>(
            data,
            'filterQuality',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      case 'flip':
        return Transform.flip(
          key: runtime.decodeKey(data),
          flipX: runtime.unpackRequiredField<bool>(data, 'flipX'),
          flipY: runtime.unpackRequiredField<bool>(data, 'flipY'),
          origin: runtime.unpackOptionalField<Offset>(data, 'origin'),
          transformHitTests: runtime.unpackRequiredField<bool>(
            data,
            'transformHitTests',
          ),
          filterQuality: runtime.unpackOptionalField<FilterQuality>(
            data,
            'filterQuality',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
      default:
        return Transform(
          key: runtime.decodeKey(data),
          transform: runtime.unpackRequiredField<Matrix4>(data, 'transform'),
          origin: runtime.unpackOptionalField<Offset>(data, 'origin'),
          alignment: runtime.unpackOptionalField<Alignment>(data, 'alignment'),
          transformHitTests: runtime.unpackRequiredField<bool>(
            data,
            'transformHitTests',
          ),
          filterQuality: runtime.unpackOptionalField<FilterQuality>(
            data,
            'filterQuality',
          ),
          child: runtime.unpackOptionalField<Widget>(data, 'child'),
        );
    }
  }
}

class FlutBuilder {
  FlutBuilder._();

  static Builder? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Builder(
      key: runtime.decodeKey(data),
      builder: runtime.unpackRequiredCallback(data, 'builder') as WidgetBuilder,
    );
  }
}

class FlutAspectRatio {
  FlutAspectRatio._();

  static AspectRatio? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return AspectRatio(
      key: runtime.decodeKey(data),
      aspectRatio: runtime.unpackRequiredField<double>(data, 'aspectRatio'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutIntrinsicWidth {
  FlutIntrinsicWidth._();

  static IntrinsicWidth? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return IntrinsicWidth(
      key: runtime.decodeKey(data),
      stepWidth: runtime.unpackOptionalField<double>(data, 'stepWidth'),
      stepHeight: runtime.unpackOptionalField<double>(data, 'stepHeight'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutFittedBox {
  FlutFittedBox._();

  static FittedBox? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return FittedBox(
      key: runtime.decodeKey(data),
      fit: runtime.unpackRequiredField<BoxFit>(data, 'fit'),
      alignment: runtime.unpackRequiredField<Alignment>(data, 'alignment'),
      clipBehavior: runtime.unpackRequiredField<Clip>(data, 'clipBehavior'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutConstrainedBox {
  FlutConstrainedBox._();

  static ConstrainedBox? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return ConstrainedBox(
      key: runtime.decodeKey(data),
      constraints: runtime.unpackRequiredField<BoxConstraints>(
        data,
        'constraints',
      ),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutSliverPadding {
  FlutSliverPadding._();

  static SliverPadding? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SliverPadding(
      key: runtime.decodeKey(data),
      padding: runtime.unpackRequiredField<EdgeInsets>(data, 'padding'),
      sliver: runtime.unpackOptionalField<Widget>(data, 'sliver'),
    );
  }
}

class FlutSliverToBoxAdapter {
  FlutSliverToBoxAdapter._();
  static SliverToBoxAdapter? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SliverToBoxAdapter(
      key: runtime.decodeKey(data),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}

class FlutCustomPaint {
  FlutCustomPaint._();

  static CustomPaint? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return CustomPaint(
      key: runtime.decodeKey(data),
      painter: runtime.unpackOptionalField<CustomPainter>(data, 'painter'),
      foregroundPainter: runtime.unpackOptionalField<CustomPainter>(
        data,
        'foregroundPainter',
      ),
      size: runtime.unpackRequiredField<Size>(data, 'size'),
      isComplex: runtime.unpackRequiredField<bool>(data, 'isComplex'),
      willChange: runtime.unpackRequiredField<bool>(data, 'willChange'),
      child: runtime.unpackOptionalField<Widget>(data, 'child'),
    );
  }
}
