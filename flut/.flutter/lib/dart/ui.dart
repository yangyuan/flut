import 'dart:typed_data';
import 'dart:ui';

import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/error.dart';

class FlutColor extends FlutValueObject {
  final Color color;

  const FlutColor(this.color) : super('Color');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['value'] = color.toARGB32();
    return result;
  }

  static Color? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Color(runtime.unpackRequiredField<int>(data, 'value'));
  }
}

class FlutColorSpace extends FlutEnumObject<ColorSpace> {
  const FlutColorSpace()
    : super('ColorSpace', const {
        'sRGB': ColorSpace.sRGB,
        'extendedSRGB': ColorSpace.extendedSRGB,
        'displayP3': ColorSpace.displayP3,
      });
}

class FlutPaintingStyle extends FlutEnumObject<PaintingStyle> {
  const FlutPaintingStyle()
    : super('PaintingStyle', const {
        'fill': PaintingStyle.fill,
        'stroke': PaintingStyle.stroke,
      });
}

class FlutStrokeCap extends FlutEnumObject<StrokeCap> {
  const FlutStrokeCap()
    : super('StrokeCap', const {
        'butt': StrokeCap.butt,
        'round': StrokeCap.round,
        'square': StrokeCap.square,
      });
}

class FlutStrokeJoin extends FlutEnumObject<StrokeJoin> {
  const FlutStrokeJoin()
    : super('StrokeJoin', const {
        'miter': StrokeJoin.miter,
        'round': StrokeJoin.round,
        'bevel': StrokeJoin.bevel,
      });
}

class FlutBlurStyle extends FlutEnumObject<BlurStyle> {
  const FlutBlurStyle()
    : super('BlurStyle', const {
        'normal': BlurStyle.normal,
        'solid': BlurStyle.solid,
        'outer': BlurStyle.outer,
        'inner': BlurStyle.inner,
      });
}

class FlutTileMode extends FlutEnumObject<TileMode> {
  const FlutTileMode()
    : super('TileMode', const {
        'clamp': TileMode.clamp,
        'repeated': TileMode.repeated,
        'mirror': TileMode.mirror,
        'decal': TileMode.decal,
      });
}

class FlutMaskFilter extends FlutValueObject {
  final MaskFilter maskFilter;

  const FlutMaskFilter(this.maskFilter) : super('MaskFilter');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    // MaskFilter doesn't expose its fields, so we can only encode from Python→Dart
    return result;
  }

  static MaskFilter? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'blur':
        return MaskFilter.blur(
          runtime.unpackRequiredField<BlurStyle>(data, 'style'),
          runtime.unpackRequiredField<double>(data, 'sigma'),
        );
      default:
        return null;
    }
  }
}

class FlutColorFilter extends FlutValueObject {
  final ColorFilter colorFilter;

  const FlutColorFilter(this.colorFilter) : super('ColorFilter');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static ColorFilter? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'mode':
        return ColorFilter.mode(
          runtime.unpackRequiredField<Color>(data, 'color'),
          runtime.unpackRequiredField<BlendMode>(data, 'blendMode'),
        );
      case 'matrix':
        final matrixData = data['matrix'] as List;
        return ColorFilter.matrix(
          matrixData.map((e) => (e as num).toDouble()).toList(),
        );
      case 'linearToSrgbGamma':
        return const ColorFilter.linearToSrgbGamma();
      case 'srgbToLinearGamma':
        return const ColorFilter.srgbToLinearGamma();
      case 'saturation':
        return ColorFilter.saturation(
          runtime.unpackRequiredField<double>(data, 'saturation'),
        );
      default:
        return null;
    }
  }
}

class FlutImageFilter extends FlutValueObject {
  final ImageFilter imageFilter;

  const FlutImageFilter(this.imageFilter) : super('ImageFilter');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static ImageFilter? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'blur':
        return ImageFilter.blur(
          sigmaX: runtime.unpackRequiredField<double>(data, 'sigmaX'),
          sigmaY: runtime.unpackRequiredField<double>(data, 'sigmaY'),
          tileMode: runtime.unpackOptionalField<TileMode>(data, 'tileMode'),
        );
      case 'dilate':
        return ImageFilter.dilate(
          radiusX: runtime.unpackRequiredField<double>(data, 'radiusX'),
          radiusY: runtime.unpackRequiredField<double>(data, 'radiusY'),
        );
      case 'erode':
        return ImageFilter.erode(
          radiusX: runtime.unpackRequiredField<double>(data, 'radiusX'),
          radiusY: runtime.unpackRequiredField<double>(data, 'radiusY'),
        );
      case 'matrix':
        final matrixData = data['matrix4'] as List;
        final matrix4 = Float64List.fromList(
          matrixData.map((e) => (e as num).toDouble()).toList(),
        );
        return ImageFilter.matrix(
          matrix4,
          filterQuality: runtime.unpackRequiredField<FilterQuality>(
            data,
            'filterQuality',
          ),
        );
      case 'compose':
        return ImageFilter.compose(
          outer: runtime.unpackRequiredField<ImageFilter>(data, 'outer'),
          inner: runtime.unpackRequiredField<ImageFilter>(data, 'inner'),
        );
      default:
        return null;
    }
  }
}

class FlutGradient extends FlutValueObject {
  final Gradient gradient;

  const FlutGradient(this.gradient) : super('Gradient');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    return result;
  }

  static Shader? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'linear':
        final colors = (data['colors'] as List)
            .map((c) => runtime.decodeObject<Color>(c)!)
            .toList();
        final colorStopsRaw = data['colorStops'] as List?;
        final colorStops = colorStopsRaw
            ?.map((e) => (e as num).toDouble())
            .toList();
        final linearMatrix4Raw = data['matrix4'] as List?;
        final linearMatrix4 = linearMatrix4Raw != null
            ? Float64List.fromList(
                linearMatrix4Raw.map((e) => (e as num).toDouble()).toList(),
              )
            : null;
        return Gradient.linear(
          runtime.unpackRequiredField<Offset>(data, 'from'),
          runtime.unpackRequiredField<Offset>(data, 'to'),
          colors,
          colorStops,
          runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
          linearMatrix4,
        );
      case 'radial':
        final colors = (data['colors'] as List)
            .map((c) => runtime.decodeObject<Color>(c)!)
            .toList();
        final colorStopsRaw = data['colorStops'] as List?;
        final colorStops = colorStopsRaw
            ?.map((e) => (e as num).toDouble())
            .toList();
        final radialMatrix4Raw = data['matrix4'] as List?;
        final radialMatrix4 = radialMatrix4Raw != null
            ? Float64List.fromList(
                radialMatrix4Raw.map((e) => (e as num).toDouble()).toList(),
              )
            : null;
        return Gradient.radial(
          runtime.unpackRequiredField<Offset>(data, 'center'),
          runtime.unpackRequiredField<double>(data, 'radius'),
          colors,
          colorStops,
          runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
          radialMatrix4,
          runtime.unpackOptionalField<Offset>(data, 'focal'),
          runtime.unpackRequiredField<double>(data, 'focalRadius'),
        );
      case 'sweep':
        final colors = (data['colors'] as List)
            .map((c) => runtime.decodeObject<Color>(c)!)
            .toList();
        final colorStopsRaw = data['colorStops'] as List?;
        final colorStops = colorStopsRaw
            ?.map((e) => (e as num).toDouble())
            .toList();
        final sweepMatrix4Raw = data['matrix4'] as List?;
        final sweepMatrix4 = sweepMatrix4Raw != null
            ? Float64List.fromList(
                sweepMatrix4Raw.map((e) => (e as num).toDouble()).toList(),
              )
            : null;
        return Gradient.sweep(
          runtime.unpackRequiredField<Offset>(data, 'center'),
          colors,
          colorStops,
          runtime.unpackRequiredField<TileMode>(data, 'tileMode'),
          runtime.unpackRequiredField<double>(data, 'startAngle'),
          runtime.unpackRequiredField<double>(data, 'endAngle'),
          sweepMatrix4,
        );
      default:
        return null;
    }
  }
}

class FlutPlaceholderAlignment extends FlutEnumObject<PlaceholderAlignment> {
  const FlutPlaceholderAlignment()
    : super('PlaceholderAlignment', const {
        'baseline': PlaceholderAlignment.baseline,
        'aboveBaseline': PlaceholderAlignment.aboveBaseline,
        'belowBaseline': PlaceholderAlignment.belowBaseline,
        'top': PlaceholderAlignment.top,
        'bottom': PlaceholderAlignment.bottom,
        'middle': PlaceholderAlignment.middle,
      });
}

class FlutTextBaseline extends FlutEnumObject<TextBaseline> {
  const FlutTextBaseline()
    : super('TextBaseline', const {
        'alphabetic': TextBaseline.alphabetic,
        'ideographic': TextBaseline.ideographic,
      });
}

class FlutTextAlign extends FlutEnumObject<TextAlign> {
  const FlutTextAlign()
    : super('TextAlign', const {
        'left': TextAlign.left,
        'right': TextAlign.right,
        'center': TextAlign.center,
        'justify': TextAlign.justify,
        'start': TextAlign.start,
        'end': TextAlign.end,
      });
}

class FlutBrightness extends FlutEnumObject<Brightness> {
  const FlutBrightness()
    : super('Brightness', const {
        'dark': Brightness.dark,
        'light': Brightness.light,
      });
}

class FlutTextDirection extends FlutEnumObject<TextDirection> {
  const FlutTextDirection()
    : super('TextDirection', const {
        'rtl': TextDirection.rtl,
        'ltr': TextDirection.ltr,
      });
}

class FlutTextAffinity extends FlutEnumObject<TextAffinity> {
  const FlutTextAffinity()
    : super('TextAffinity', const {
        'upstream': TextAffinity.upstream,
        'downstream': TextAffinity.downstream,
      });
}

class FlutFontStyle extends FlutEnumObject<FontStyle> {
  const FlutFontStyle()
    : super('FontStyle', const {
        'normal': FontStyle.normal,
        'italic': FontStyle.italic,
      });
}

class FlutTextDecorationStyle extends FlutEnumObject<TextDecorationStyle> {
  const FlutTextDecorationStyle()
    : super('TextDecorationStyle', const {
        'solid': TextDecorationStyle.solid,
        'double': TextDecorationStyle.double,
        'dotted': TextDecorationStyle.dotted,
        'dashed': TextDecorationStyle.dashed,
        'wavy': TextDecorationStyle.wavy,
      });
}

class FlutTextLeadingDistribution
    extends FlutEnumObject<TextLeadingDistribution> {
  const FlutTextLeadingDistribution()
    : super('TextLeadingDistribution', const {
        'proportional': TextLeadingDistribution.proportional,
        'even': TextLeadingDistribution.even,
      });
}

class FlutFontWeight extends FlutValueObject {
  final FontWeight fontWeight;

  const FlutFontWeight(this.fontWeight) : super('FontWeight');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['index'] = FontWeight.values.indexOf(fontWeight);
    return result;
  }

  static FontWeight? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return FontWeight.values[runtime.unpackRequiredField<int>(data, 'index')];
  }
}

class FlutTextDecoration extends FlutValueObject {
  final TextDecoration decoration;

  const FlutTextDecoration(this.decoration) : super('TextDecoration');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    int mask = 0;
    if (decoration.contains(TextDecoration.underline)) mask |= 0x1;
    if (decoration.contains(TextDecoration.overline)) mask |= 0x2;
    if (decoration.contains(TextDecoration.lineThrough)) mask |= 0x4;
    result['mask'] = mask;
    return result;
  }

  static TextDecoration? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final mask = runtime.unpackRequiredField<int>(data, 'mask');
    final parts = <TextDecoration>[];
    if (mask & 0x1 != 0) parts.add(TextDecoration.underline);
    if (mask & 0x2 != 0) parts.add(TextDecoration.overline);
    if (mask & 0x4 != 0) parts.add(TextDecoration.lineThrough);
    return parts.isEmpty ? TextDecoration.none : TextDecoration.combine(parts);
  }
}

class FlutBlendMode extends FlutEnumObject<BlendMode> {
  const FlutBlendMode()
    : super('BlendMode', const {
        'clear': BlendMode.clear,
        'src': BlendMode.src,
        'dst': BlendMode.dst,
        'srcOver': BlendMode.srcOver,
        'dstOver': BlendMode.dstOver,
        'srcIn': BlendMode.srcIn,
        'dstIn': BlendMode.dstIn,
        'srcOut': BlendMode.srcOut,
        'dstOut': BlendMode.dstOut,
        'srcATop': BlendMode.srcATop,
        'dstATop': BlendMode.dstATop,
        'xor': BlendMode.xor,
        'plus': BlendMode.plus,
        'modulate': BlendMode.modulate,
        'screen': BlendMode.screen,
        'overlay': BlendMode.overlay,
        'darken': BlendMode.darken,
        'lighten': BlendMode.lighten,
        'colorDodge': BlendMode.colorDodge,
        'colorBurn': BlendMode.colorBurn,
        'hardLight': BlendMode.hardLight,
        'softLight': BlendMode.softLight,
        'difference': BlendMode.difference,
        'exclusion': BlendMode.exclusion,
        'multiply': BlendMode.multiply,
        'hue': BlendMode.hue,
        'saturation': BlendMode.saturation,
        'color': BlendMode.color,
        'luminosity': BlendMode.luminosity,
      });
}

class FlutFilterQuality extends FlutEnumObject<FilterQuality> {
  const FlutFilterQuality()
    : super('FilterQuality', const {
        'none': FilterQuality.none,
        'low': FilterQuality.low,
        'medium': FilterQuality.medium,
        'high': FilterQuality.high,
      });
}

class FlutClip extends FlutEnumObject<Clip> {
  const FlutClip()
    : super('Clip', const {
        'none': Clip.none,
        'hardEdge': Clip.hardEdge,
        'antiAlias': Clip.antiAlias,
        'antiAliasWithSaveLayer': Clip.antiAliasWithSaveLayer,
      });
}

class FlutPointerDeviceKind extends FlutEnumObject<PointerDeviceKind> {
  const FlutPointerDeviceKind()
    : super('PointerDeviceKind', const {
        'touch': PointerDeviceKind.touch,
        'mouse': PointerDeviceKind.mouse,
        'stylus': PointerDeviceKind.stylus,
        'invertedStylus': PointerDeviceKind.invertedStylus,
        'trackpad': PointerDeviceKind.trackpad,
        'unknown': PointerDeviceKind.unknown,
      });
}

class FlutSize extends FlutValueObject {
  final Size size;

  const FlutSize(this.size) : super('Size');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['width'] = size.width;
    result['height'] = size.height;
    return result;
  }

  static Size? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Size(
      runtime.unpackRequiredField<double>(data, 'width'),
      runtime.unpackRequiredField<double>(data, 'height'),
    );
  }
}

class FlutRadius extends FlutValueObject {
  final Radius radius;

  const FlutRadius(this.radius) : super('Radius');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['x'] = radius.x;
    result['y'] = radius.y;
    return result;
  }

  static Radius? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Radius.elliptical(
      runtime.unpackRequiredField<double>(data, 'x'),
      runtime.unpackRequiredField<double>(data, 'y'),
    );
  }
}

class FlutOffset extends FlutValueObject {
  final Offset offset;

  const FlutOffset(this.offset) : super('Offset');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['dx'] = offset.dx;
    result['dy'] = offset.dy;
    return result;
  }

  static Offset? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Offset(
      runtime.unpackRequiredField<double>(data, 'dx'),
      runtime.unpackRequiredField<double>(data, 'dy'),
    );
  }
}

class FlutRect extends FlutValueObject {
  final Rect rect;

  const FlutRect(this.rect) : super('Rect');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = rect.left;
    result['top'] = rect.top;
    result['right'] = rect.right;
    result['bottom'] = rect.bottom;
    return result;
  }

  static Rect? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Rect.fromLTRB(
      runtime.unpackRequiredField<double>(data, 'left'),
      runtime.unpackRequiredField<double>(data, 'top'),
      runtime.unpackRequiredField<double>(data, 'right'),
      runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}

class FlutRRect extends FlutValueObject {
  final RRect rrect;

  const FlutRRect(this.rrect) : super('RRect');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = rrect.left;
    result['top'] = rrect.top;
    result['right'] = rrect.right;
    result['bottom'] = rrect.bottom;
    result['tlRadiusX'] = rrect.tlRadiusX;
    result['tlRadiusY'] = rrect.tlRadiusY;
    result['trRadiusX'] = rrect.trRadiusX;
    result['trRadiusY'] = rrect.trRadiusY;
    result['brRadiusX'] = rrect.brRadiusX;
    result['brRadiusY'] = rrect.brRadiusY;
    result['blRadiusX'] = rrect.blRadiusX;
    result['blRadiusY'] = rrect.blRadiusY;
    return result;
  }

  static RRect? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return RRect.fromLTRBAndCorners(
      runtime.unpackRequiredField<double>(data, 'left'),
      runtime.unpackRequiredField<double>(data, 'top'),
      runtime.unpackRequiredField<double>(data, 'right'),
      runtime.unpackRequiredField<double>(data, 'bottom'),
      topLeft: Radius.elliptical(
        runtime.unpackRequiredField<double>(data, 'tlRadiusX'),
        runtime.unpackRequiredField<double>(data, 'tlRadiusY'),
      ),
      topRight: Radius.elliptical(
        runtime.unpackRequiredField<double>(data, 'trRadiusX'),
        runtime.unpackRequiredField<double>(data, 'trRadiusY'),
      ),
      bottomRight: Radius.elliptical(
        runtime.unpackRequiredField<double>(data, 'brRadiusX'),
        runtime.unpackRequiredField<double>(data, 'brRadiusY'),
      ),
      bottomLeft: Radius.elliptical(
        runtime.unpackRequiredField<double>(data, 'blRadiusX'),
        runtime.unpackRequiredField<double>(data, 'blRadiusY'),
      ),
    );
  }
}

class _FlutViewPadding implements ViewPadding {
  const _FlutViewPadding({
    required this.left,
    required this.top,
    required this.right,
    required this.bottom,
  });

  @override
  final double left;

  @override
  final double top;

  @override
  final double right;

  @override
  final double bottom;
}

class FlutViewPadding extends FlutValueObject {
  final ViewPadding viewPadding;

  const FlutViewPadding(this.viewPadding) : super('ViewPadding');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['left'] = viewPadding.left;
    result['top'] = viewPadding.top;
    result['right'] = viewPadding.right;
    result['bottom'] = viewPadding.bottom;
    return result;
  }

  static ViewPadding? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return _FlutViewPadding(
      left: runtime.unpackRequiredField<double>(data, 'left'),
      top: runtime.unpackRequiredField<double>(data, 'top'),
      right: runtime.unpackRequiredField<double>(data, 'right'),
      bottom: runtime.unpackRequiredField<double>(data, 'bottom'),
    );
  }
}

class FlutPaint extends FlutValueObject {
  final Paint paint;

  const FlutPaint(this.paint) : super('Paint');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (paint.blendMode != BlendMode.srcOver) {
      result['blendMode'] = const FlutBlendMode().flutEncode(paint.blendMode);
    }
    if (paint.color != const Color(0xFF000000)) {
      result['color'] = FlutColor(paint.color).flutEncode();
    }
    if (paint.colorFilter != null) {
      result['colorFilter'] = FlutColorFilter(paint.colorFilter!).flutEncode();
    }
    if (paint.filterQuality != FilterQuality.none) {
      result['filterQuality'] = const FlutFilterQuality().flutEncode(
        paint.filterQuality,
      );
    }
    if (paint.imageFilter != null) {
      result['imageFilter'] = FlutImageFilter(paint.imageFilter!).flutEncode();
    }
    if (paint.invertColors != false) {
      result['invertColors'] = paint.invertColors;
    }
    if (paint.isAntiAlias != true) {
      result['isAntiAlias'] = paint.isAntiAlias;
    }
    if (paint.maskFilter != null) {
      result['maskFilter'] = FlutMaskFilter(paint.maskFilter!).flutEncode();
    }
    if (paint.shader != null) {
      if (paint.shader is Gradient) {
        result['shader'] = FlutGradient(paint.shader! as Gradient).flutEncode();
      }
    }
    if (paint.strokeCap != StrokeCap.butt) {
      result['strokeCap'] = const FlutStrokeCap().flutEncode(paint.strokeCap);
    }
    if (paint.strokeJoin != StrokeJoin.miter) {
      result['strokeJoin'] = const FlutStrokeJoin().flutEncode(
        paint.strokeJoin,
      );
    }
    if (paint.strokeMiterLimit != 4.0) {
      result['strokeMiterLimit'] = paint.strokeMiterLimit;
    }
    if (paint.strokeWidth != 0.0) {
      result['strokeWidth'] = paint.strokeWidth;
    }
    if (paint.style != PaintingStyle.fill) {
      result['style'] = const FlutPaintingStyle().flutEncode(paint.style);
    }
    return result;
  }

  static Paint? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final paint = Paint();
    final blendMode = runtime.unpackOptionalField<BlendMode>(data, 'blendMode');
    if (blendMode != null) paint.blendMode = blendMode;
    final color = runtime.unpackOptionalField<Color>(data, 'color');
    if (color != null) paint.color = color;
    final colorFilter = runtime.unpackOptionalField<ColorFilter>(
      data,
      'colorFilter',
    );
    if (colorFilter != null) paint.colorFilter = colorFilter;
    final filterQuality = runtime.unpackOptionalField<FilterQuality>(
      data,
      'filterQuality',
    );
    if (filterQuality != null) paint.filterQuality = filterQuality;
    final imageFilter = runtime.unpackOptionalField<ImageFilter>(
      data,
      'imageFilter',
    );
    if (imageFilter != null) paint.imageFilter = imageFilter;
    final invertColors = runtime.unpackOptionalField<bool>(
      data,
      'invertColors',
    );
    if (invertColors != null) paint.invertColors = invertColors;
    final isAntiAlias = runtime.unpackOptionalField<bool>(data, 'isAntiAlias');
    if (isAntiAlias != null) paint.isAntiAlias = isAntiAlias;
    final maskFilter = runtime.unpackOptionalField<MaskFilter>(
      data,
      'maskFilter',
    );
    if (maskFilter != null) paint.maskFilter = maskFilter;
    final shader = runtime.unpackOptionalField<Shader>(data, 'shader');
    if (shader != null) paint.shader = shader;
    final strokeCap = runtime.unpackOptionalField<StrokeCap>(data, 'strokeCap');
    if (strokeCap != null) paint.strokeCap = strokeCap;
    final strokeJoin = runtime.unpackOptionalField<StrokeJoin>(
      data,
      'strokeJoin',
    );
    if (strokeJoin != null) paint.strokeJoin = strokeJoin;
    final strokeMiterLimit = runtime.unpackOptionalField<double>(
      data,
      'strokeMiterLimit',
    );
    if (strokeMiterLimit != null) paint.strokeMiterLimit = strokeMiterLimit;
    final strokeWidth = runtime.unpackOptionalField<double>(
      data,
      'strokeWidth',
    );
    if (strokeWidth != null) paint.strokeWidth = strokeWidth;
    final style = runtime.unpackOptionalField<PaintingStyle>(data, 'style');
    if (style != null) paint.style = style;
    return paint;
  }
}

class FlutShadow extends FlutValueObject {
  final Shadow shadow;

  const FlutShadow(this.shadow) : super('Shadow');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    if (shadow.color != const Color(0xFF000000)) {
      result['color'] = FlutColor(shadow.color).flutEncode();
    }
    if (shadow.offset != Offset.zero) {
      result['offset'] = FlutOffset(shadow.offset).flutEncode();
    }
    if (shadow.blurRadius != 0.0) {
      result['blurRadius'] = shadow.blurRadius;
    }
    return result;
  }

  static Shadow? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Shadow(
      color: runtime.unpackRequiredField<Color>(data, 'color'),
      offset: runtime.unpackRequiredField<Offset>(data, 'offset'),
      blurRadius: runtime.unpackRequiredField<double>(data, 'blurRadius'),
    );
  }
}

class FlutCanvas with FlutRealtimeObject<Canvas> {
  FlutCanvas.createFromObject({
    required FlutRuntime runtime,
    required int oid,
    required Canvas target,
  }) {
    initRealtimeFromObject(
      runtime: runtime,
      oid: oid,
      type: 'Canvas',
      target: target,
    );
  }

  @override
  dynamic getRawProperty(String property) {
    throw FlutUnknownPropertyException('Canvas', property);
  }

  @override
  bool setProperty(String property, dynamic value) {
    throw FlutUnknownPropertyException('Canvas', property);
  }

  @override
  dynamic callMethod(
    String method,
    List<dynamic> args,
    Map<String, dynamic> kwargs,
  ) {
    switch (method) {
      case 'drawLine':
        flutTarget.drawLine(args[0], args[1], args[2]);
        return null;
      case 'drawRect':
        flutTarget.drawRect(args[0], args[1]);
        return null;
      case 'drawCircle':
        flutTarget.drawCircle(args[0], (args[1] as num).toDouble(), args[2]);
        return null;
      case 'drawOval':
        flutTarget.drawOval(args[0], args[1]);
        return null;
      case 'drawArc':
        flutTarget.drawArc(
          args[0],
          (args[1] as num).toDouble(),
          (args[2] as num).toDouble(),
          args[3],
          args[4],
        );
        return null;
      case 'clipRect':
        flutTarget.clipRect(args[0]);
        return null;
      case 'save':
        flutTarget.save();
        return null;
      case 'restore':
        flutTarget.restore();
        return null;
      case 'translate':
        flutTarget.translate(
          (args[0] as num).toDouble(),
          (args[1] as num).toDouble(),
        );
        return null;
      case 'scale':
        flutTarget.scale(
          (args[0] as num).toDouble(),
          args.length > 1 ? (args[1] as num).toDouble() : null,
        );
        return null;
      case 'rotate':
        flutTarget.rotate((args[0] as num).toDouble());
        return null;
    }
    throw FlutUnknownMethodException(method);
  }
}
