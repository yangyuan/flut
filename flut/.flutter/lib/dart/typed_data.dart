import 'dart:convert';
import 'dart:typed_data';

import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutUint8List extends FlutValueObject {
  final Uint8List bytes;

  const FlutUint8List(this.bytes) : super('Uint8List');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['data'] = base64Encode(bytes);
    return result;
  }

  static Uint8List? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return base64Decode(runtime.unpackRequiredField<String>(data, 'data'));
  }
}
