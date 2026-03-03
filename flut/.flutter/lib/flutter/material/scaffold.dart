import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flut/flut/runtime.dart';

class FlutScaffold {
  FlutScaffold._();

  static Scaffold? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return Scaffold(
      key: runtime.decodeKey(data),
      appBar: runtime.unpackOptionalField<PreferredSizeWidget>(data, 'appBar'),
      body: runtime.unpackOptionalField<Widget>(data, 'body'),
      floatingActionButton: runtime.unpackOptionalField<Widget>(
        data,
        'floatingActionButton',
      ),
      persistentFooterButtons: runtime.unpackOptionalField<List<Widget>>(
        data,
        'persistentFooterButtons',
      ),
      persistentFooterDecoration: runtime.unpackOptionalField<BoxDecoration>(
        data,
        'persistentFooterDecoration',
      ),
      persistentFooterAlignment: runtime
          .unpackRequiredField<AlignmentDirectional>(
            data,
            'persistentFooterAlignment',
          ),
      drawer: runtime.unpackOptionalField<Widget>(data, 'drawer'),
      onDrawerChanged: runtime.unpackOptionalCallback(data, 'onDrawerChanged'),
      endDrawer: runtime.unpackOptionalField<Widget>(data, 'endDrawer'),
      onEndDrawerChanged: runtime.unpackOptionalCallback(
        data,
        'onEndDrawerChanged',
      ),
      bottomNavigationBar: runtime.unpackOptionalField<Widget>(
        data,
        'bottomNavigationBar',
      ),
      bottomSheet: runtime.unpackOptionalField<Widget>(data, 'bottomSheet'),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      resizeToAvoidBottomInset: runtime.unpackOptionalField<bool>(
        data,
        'resizeToAvoidBottomInset',
      ),
      primary: runtime.unpackRequiredField<bool>(data, 'primary'),
      extendBody: runtime.unpackRequiredField<bool>(data, 'extendBody'),
      drawerBarrierDismissible: runtime.unpackRequiredField<bool>(
        data,
        'drawerBarrierDismissible',
      ),
      extendBodyBehindAppBar: runtime.unpackRequiredField<bool>(
        data,
        'extendBodyBehindAppBar',
      ),
      drawerScrimColor: runtime.unpackOptionalField<Color>(
        data,
        'drawerScrimColor',
      ),
      drawerDragStartBehavior: runtime.unpackRequiredField<DragStartBehavior>(
        data,
        'drawerDragStartBehavior',
      ),
      drawerEdgeDragWidth: runtime.unpackOptionalField<double>(
        data,
        'drawerEdgeDragWidth',
      ),
      drawerEnableOpenDragGesture: runtime.unpackRequiredField<bool>(
        data,
        'drawerEnableOpenDragGesture',
      ),
      endDrawerEnableOpenDragGesture: runtime.unpackRequiredField<bool>(
        data,
        'endDrawerEnableOpenDragGesture',
      ),
      restorationId: runtime.unpackOptionalField<String>(data, 'restorationId'),
    );
  }
}
