import 'dart:io';
import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutFile extends FlutValueObject {
  final File file;

  const FlutFile(this.file) : super('File');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['path'] = file.path;
    return result;
  }

  static File? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return File(runtime.unpackRequiredField<String>(data, 'path'));
  }
}
