import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutText {
  FlutText._();

  static Text? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'rich':
        return Text.rich(
          runtime.unpackRequiredField<InlineSpan>(data, 'textSpan'),
          key: runtime.decodeKey(data),
          style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
          strutStyle: runtime.unpackOptionalField<StrutStyle>(
            data,
            'strutStyle',
          ),
          textAlign: runtime.unpackOptionalField<TextAlign>(data, 'textAlign'),
          textDirection: runtime.unpackOptionalField<TextDirection>(
            data,
            'textDirection',
          ),
          softWrap: runtime.unpackOptionalField<bool>(data, 'softWrap'),
          overflow: runtime.unpackOptionalField<TextOverflow>(data, 'overflow'),
          textScaler: runtime.unpackOptionalField<TextScaler>(
            data,
            'textScaler',
          ),
          maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
          semanticsLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticsLabel',
          ),
          semanticsIdentifier: runtime.unpackOptionalField<String>(
            data,
            'semanticsIdentifier',
          ),
          textWidthBasis: runtime.unpackOptionalField<TextWidthBasis>(
            data,
            'textWidthBasis',
          ),
          selectionColor: runtime.unpackOptionalField<Color>(
            data,
            'selectionColor',
          ),
        );
      default:
        return Text(
          runtime.unpackRequiredField<String>(data, 'data'),
          key: runtime.decodeKey(data),
          style: runtime.unpackOptionalField<TextStyle>(data, 'style'),
          strutStyle: runtime.unpackOptionalField<StrutStyle>(
            data,
            'strutStyle',
          ),
          textAlign: runtime.unpackOptionalField<TextAlign>(data, 'textAlign'),
          textDirection: runtime.unpackOptionalField<TextDirection>(
            data,
            'textDirection',
          ),
          softWrap: runtime.unpackOptionalField<bool>(data, 'softWrap'),
          overflow: runtime.unpackOptionalField<TextOverflow>(data, 'overflow'),
          textScaler: runtime.unpackOptionalField<TextScaler>(
            data,
            'textScaler',
          ),
          maxLines: runtime.unpackOptionalField<int>(data, 'maxLines'),
          semanticsLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticsLabel',
          ),
          semanticsIdentifier: runtime.unpackOptionalField<String>(
            data,
            'semanticsIdentifier',
          ),
          textWidthBasis: runtime.unpackOptionalField<TextWidthBasis>(
            data,
            'textWidthBasis',
          ),
          selectionColor: runtime.unpackOptionalField<Color>(
            data,
            'selectionColor',
          ),
        );
    }
  }
}
