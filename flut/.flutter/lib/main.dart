import 'package:flutter/material.dart';
import 'package:flut/flut/native.dart';
import 'package:flut/flut/runtime.dart';

late final FlutNative flutNative;
late final FlutRuntime flutRuntime;

void main(List<String> args) {
  int? nativeCallbackAddr;
  for (final arg in args) {
    if (arg.startsWith('--native-callback=')) {
      nativeCallbackAddr = int.tryParse(
        arg.substring('--native-callback='.length),
      );
    }
  }

  flutNative = FlutFfiNative(nativeCallbackAddr ?? 0);
  flutRuntime = FlutRuntime(flutNative);
  (flutNative as FlutFfiNative).bootstrap();

  (flutNative as FlutFfiNative).userInitDone.then((_) {
    Map<String, dynamic>? rootData;
    String? error;

    try {
      rootData = flutNative.invokeNativeSync("get_root", {});
      if (rootData == null) {
        error = 'get_root returned null';
      } else if (rootData['_flut_error'] != null) {
        error = rootData['_flut_error'].toString();
      }
    } catch (e) {
      error = e.toString();
    }

    if (error != null) {
      print(error);
      runApp(ErrorWidget.withDetails(message: error));
      return;
    }

    runApp(
      Builder(
        builder: (context) {
          final result = flutRuntime.buildWidgetFromJson(rootData!);
          return result;
        },
      ),
    );
  });
}
