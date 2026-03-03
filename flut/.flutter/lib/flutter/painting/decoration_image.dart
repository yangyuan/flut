import 'package:flutter/painting.dart';
import 'package:flut/flut/object.dart';

class FlutImageRepeat extends FlutEnumObject<ImageRepeat> {
  const FlutImageRepeat()
    : super('ImageRepeat', const {
        'repeat': ImageRepeat.repeat,
        'repeatX': ImageRepeat.repeatX,
        'repeatY': ImageRepeat.repeatY,
        'noRepeat': ImageRepeat.noRepeat,
      });
}
