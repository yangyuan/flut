import 'package:flutter/foundation.dart';
import 'package:flut/flut/object.dart';

class FlutTargetPlatform extends FlutEnumObject<TargetPlatform> {
  const FlutTargetPlatform()
    : super('TargetPlatform', const {
        'android': TargetPlatform.android,
        'fuchsia': TargetPlatform.fuchsia,
        'iOS': TargetPlatform.iOS,
        'linux': TargetPlatform.linux,
        'macOS': TargetPlatform.macOS,
        'windows': TargetPlatform.windows,
      });
}
