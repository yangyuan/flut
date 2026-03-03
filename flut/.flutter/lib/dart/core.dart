import 'package:flut/flut/runtime.dart';
import 'package:flut/flut/object.dart';

class FlutDuration extends FlutValueObject {
  final Duration duration;

  const FlutDuration(this.duration) : super('Duration');

  @override
  Map<String, dynamic> flutEncode() {
    final result = flutBaseProps();
    result['microseconds'] = duration.inMicroseconds;
    return result;
  }

  static Duration? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Duration(
      microseconds: runtime.unpackRequiredField<int>(data, 'microseconds'),
    );
  }
}
