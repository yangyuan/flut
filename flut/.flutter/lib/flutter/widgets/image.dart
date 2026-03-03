import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutImage {
  FlutImage._();

  static Image? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'memory':
        return Image.memory(
          runtime.unpackRequiredField<Uint8List>(data, 'bytes'),
          key: runtime.decodeKey(data),
          scale: runtime.unpackRequiredField<double>(data, 'scale'),
          semanticLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticLabel',
          ),
          excludeFromSemantics: runtime.unpackRequiredField<bool>(
            data,
            'excludeFromSemantics',
          ),
          width: runtime.unpackOptionalField<double>(data, 'width'),
          height: runtime.unpackOptionalField<double>(data, 'height'),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          colorBlendMode: runtime.unpackOptionalField<BlendMode>(
            data,
            'colorBlendMode',
          ),
          fit: runtime.unpackOptionalField<BoxFit>(data, 'fit'),
          alignment: runtime.unpackRequiredField<Alignment>(data, 'alignment'),
          repeat: runtime.unpackRequiredField<ImageRepeat>(data, 'repeat'),
          matchTextDirection: runtime.unpackRequiredField<bool>(
            data,
            'matchTextDirection',
          ),
          gaplessPlayback: runtime.unpackRequiredField<bool>(
            data,
            'gaplessPlayback',
          ),
          filterQuality: runtime.unpackRequiredField<FilterQuality>(
            data,
            'filterQuality',
          ),
          isAntiAlias: runtime.unpackRequiredField<bool>(data, 'isAntiAlias'),
          cacheWidth: runtime.unpackOptionalField<int>(data, 'cacheWidth'),
          cacheHeight: runtime.unpackOptionalField<int>(data, 'cacheHeight'),
        );
      case 'file':
        return Image.file(
          File(
            runtime.unpackRequiredField<String>(
              runtime.unpackRequiredField<Map<String, dynamic>>(data, 'file'),
              'path',
            ),
          ),
          key: runtime.decodeKey(data),
          scale: runtime.unpackRequiredField<double>(data, 'scale'),
          semanticLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticLabel',
          ),
          excludeFromSemantics: runtime.unpackRequiredField<bool>(
            data,
            'excludeFromSemantics',
          ),
          width: runtime.unpackOptionalField<double>(data, 'width'),
          height: runtime.unpackOptionalField<double>(data, 'height'),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          colorBlendMode: runtime.unpackOptionalField<BlendMode>(
            data,
            'colorBlendMode',
          ),
          fit: runtime.unpackOptionalField<BoxFit>(data, 'fit'),
          alignment: runtime.unpackRequiredField<Alignment>(data, 'alignment'),
          repeat: runtime.unpackRequiredField<ImageRepeat>(data, 'repeat'),
          matchTextDirection: runtime.unpackRequiredField<bool>(
            data,
            'matchTextDirection',
          ),
          gaplessPlayback: runtime.unpackRequiredField<bool>(
            data,
            'gaplessPlayback',
          ),
          filterQuality: runtime.unpackRequiredField<FilterQuality>(
            data,
            'filterQuality',
          ),
          isAntiAlias: runtime.unpackRequiredField<bool>(data, 'isAntiAlias'),
          cacheWidth: runtime.unpackOptionalField<int>(data, 'cacheWidth'),
          cacheHeight: runtime.unpackOptionalField<int>(data, 'cacheHeight'),
        );
      case 'network':
      default:
        return Image.network(
          runtime.unpackRequiredField<String>(data, 'src'),
          key: runtime.decodeKey(data),
          scale: runtime.unpackRequiredField<double>(data, 'scale'),
          semanticLabel: runtime.unpackOptionalField<String>(
            data,
            'semanticLabel',
          ),
          excludeFromSemantics: runtime.unpackRequiredField<bool>(
            data,
            'excludeFromSemantics',
          ),
          width: runtime.unpackOptionalField<double>(data, 'width'),
          height: runtime.unpackOptionalField<double>(data, 'height'),
          color: runtime.unpackOptionalField<Color>(data, 'color'),
          colorBlendMode: runtime.unpackOptionalField<BlendMode>(
            data,
            'colorBlendMode',
          ),
          fit: runtime.unpackOptionalField<BoxFit>(data, 'fit'),
          alignment: runtime.unpackRequiredField<Alignment>(data, 'alignment'),
          repeat: runtime.unpackRequiredField<ImageRepeat>(data, 'repeat'),
          matchTextDirection: runtime.unpackRequiredField<bool>(
            data,
            'matchTextDirection',
          ),
          gaplessPlayback: runtime.unpackRequiredField<bool>(
            data,
            'gaplessPlayback',
          ),
          filterQuality: runtime.unpackRequiredField<FilterQuality>(
            data,
            'filterQuality',
          ),
          isAntiAlias: runtime.unpackRequiredField<bool>(data, 'isAntiAlias'),
          headers: runtime.unpackOptionalField<Map<String, String>>(
            data,
            'headers',
          ),
          cacheWidth: runtime.unpackOptionalField<int>(data, 'cacheWidth'),
          cacheHeight: runtime.unpackOptionalField<int>(data, 'cacheHeight'),
        );
    }
  }
}
