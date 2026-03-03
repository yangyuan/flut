import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutSliderInteraction extends FlutEnumObject<SliderInteraction> {
  const FlutSliderInteraction()
    : super('SliderInteraction', const {
        'tapAndSlide': SliderInteraction.tapAndSlide,
        'tapOnly': SliderInteraction.tapOnly,
        'slideOnly': SliderInteraction.slideOnly,
        'slideThumb': SliderInteraction.slideThumb,
      });
}

class FlutSlider {
  FlutSlider._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Slider(
      key: runtime.decodeKey(data),
      value: runtime.unpackRequiredField<double>(data, 'value'),
      secondaryTrackValue: runtime.unpackOptionalField<double>(
        data,
        'secondaryTrackValue',
      ),
      onChanged: runtime.unpackNullableRequiredCallback(data, 'onChanged'),
      onChangeStart: runtime.unpackOptionalCallback(data, 'onChangeStart'),
      onChangeEnd: runtime.unpackOptionalCallback(data, 'onChangeEnd'),
      min: runtime.unpackRequiredField<double>(data, 'min'),
      max: runtime.unpackRequiredField<double>(data, 'max'),
      divisions: runtime.unpackOptionalField<int>(data, 'divisions'),
      label: runtime.unpackOptionalField<String>(data, 'label'),
      activeColor: runtime.unpackOptionalField<Color>(data, 'activeColor'),
      inactiveColor: runtime.unpackOptionalField<Color>(data, 'inactiveColor'),
      secondaryActiveColor: runtime.unpackOptionalField<Color>(
        data,
        'secondaryActiveColor',
      ),
      thumbColor: runtime.unpackOptionalField<Color>(data, 'thumbColor'),
      overlayColor: runtime
          .unpackGenericField<WidgetStateProperty<Color?>, Color?>(
            data,
            'overlayColor',
          ),
      mouseCursor: runtime.unpackOptionalField<MouseCursor>(
        data,
        'mouseCursor',
      ),
      semanticFormatterCallback: runtime.unpackOptionalCallback(
        data,
        'semanticFormatterCallback',
      ),
      focusNode: runtime.unpackOptionalField<FocusNode>(data, 'focusNode'),
      autofocus: runtime.unpackRequiredField<bool>(data, 'autofocus'),
      allowedInteraction: runtime.unpackOptionalField<SliderInteraction>(
        data,
        'allowedInteraction',
      ),
      padding: runtime.unpackOptionalField<EdgeInsets>(data, 'padding'),
      showValueIndicator: runtime.unpackOptionalField<ShowValueIndicator>(
        data,
        'showValueIndicator',
      ),
    );
  }
}
