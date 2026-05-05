import 'package:flutter/rendering.dart';
import 'package:flutter/widgets.dart';
import 'package:flut/flut/object.dart';
import 'package:flut/flut/runtime.dart';

class FlutSelectionRegistrar extends FlutValueObject {
  const FlutSelectionRegistrar() : super('SelectionRegistrar');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'SelectionRegistrar has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static SelectionRegistrar? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'SelectionRegistrar has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutSelectionContainerDelegate extends FlutValueObject {
  const FlutSelectionContainerDelegate() : super('SelectionContainerDelegate');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'SelectionContainerDelegate has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static SelectionContainerDelegate? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'SelectionContainerDelegate has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutMultiSelectableSelectionContainerDelegate extends FlutValueObject {
  const FlutMultiSelectableSelectionContainerDelegate()
    : super('MultiSelectableSelectionContainerDelegate');

  @override
  Map<String, dynamic> flutEncode() {
    throw UnimplementedError(
      'MultiSelectableSelectionContainerDelegate has no concrete wire form. Pass a concrete subtype.',
    );
  }

  static MultiSelectableSelectionContainerDelegate? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    throw UnimplementedError(
      'MultiSelectableSelectionContainerDelegate has no concrete wire form. Pass a concrete subtype.',
    );
  }
}

class FlutStaticSelectionContainerDelegate extends FlutValueObject {
  final StaticSelectionContainerDelegate delegate;

  const FlutStaticSelectionContainerDelegate(this.delegate)
    : super('StaticSelectionContainerDelegate');

  @override
  Map<String, dynamic> flutEncode() => flutBaseProps();

  static StaticSelectionContainerDelegate? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return StaticSelectionContainerDelegate();
  }
}

class FlutSelectionContainer {
  FlutSelectionContainer._();

  static SelectionContainer? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    final constructor = runtime.unpackConstructor(data);
    switch (constructor) {
      case 'disabled':
        return SelectionContainer.disabled(
          key: runtime.decodeKey(data),
          child: runtime.unpackRequiredField<Widget>(data, 'child'),
        );
      default:
        return SelectionContainer(
          key: runtime.decodeKey(data),
          registrar: runtime.unpackOptionalField<SelectionRegistrar>(
            data,
            'registrar',
          ),
          delegate: runtime.unpackRequiredField<SelectionContainerDelegate>(
            data,
            'delegate',
          ),
          child: runtime.unpackRequiredField<Widget>(data, 'child'),
        );
    }
  }

  static void registerStatics(FlutRuntime runtime) {
    runtime.registerStatic('SelectionContainer.maybeOf', maybeOf);
  }

  static SelectionRegistrar? maybeOf(
    FlutRuntime runtime,
    BuildContext context,
  ) {
    return SelectionContainer.maybeOf(context);
  }
}

class FlutSelectionRegistrarScope {
  FlutSelectionRegistrarScope._();

  static SelectionRegistrarScope? flutDecode(
    FlutRuntime runtime,
    Map<String, dynamic> data,
  ) {
    return SelectionRegistrarScope(
      key: runtime.decodeKey(data),
      registrar: runtime.unpackRequiredField<SelectionRegistrar>(
        data,
        'registrar',
      ),
      child: runtime.unpackRequiredField<Widget>(data, 'child'),
    );
  }
}
