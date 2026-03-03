import 'package:flutter/material.dart';
import 'package:flut/flut/runtime.dart';

class FlutExpansionTile {
  FlutExpansionTile._();

  static Widget? flutDecode(FlutRuntime runtime, Map<String, dynamic> data) {
    return ExpansionTile(
      key: runtime.decodeKey(data),
      leading: runtime.unpackOptionalField<Widget>(data, 'leading'),
      title: runtime.unpackRequiredField<Widget>(data, 'title'),
      subtitle: runtime.unpackOptionalField<Widget>(data, 'subtitle'),
      onExpansionChanged: runtime.unpackOptionalCallback(
        data,
        'onExpansionChanged',
      ),
      trailing: runtime.unpackOptionalField<Widget>(data, 'trailing'),
      showTrailingIcon: runtime.unpackRequiredField<bool>(
        data,
        'showTrailingIcon',
      ),
      initiallyExpanded: runtime.unpackRequiredField<bool>(
        data,
        'initiallyExpanded',
      ),
      maintainState: runtime.unpackRequiredField<bool>(data, 'maintainState'),
      tilePadding: runtime.unpackOptionalField<EdgeInsets>(data, 'tilePadding'),
      expandedCrossAxisAlignment: runtime
          .unpackOptionalField<CrossAxisAlignment>(
            data,
            'expandedCrossAxisAlignment',
          ),
      expandedAlignment: runtime.unpackOptionalField<Alignment>(
        data,
        'expandedAlignment',
      ),
      childrenPadding: runtime.unpackOptionalField<EdgeInsets>(
        data,
        'childrenPadding',
      ),
      backgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'backgroundColor',
      ),
      collapsedBackgroundColor: runtime.unpackOptionalField<Color>(
        data,
        'collapsedBackgroundColor',
      ),
      textColor: runtime.unpackOptionalField<Color>(data, 'textColor'),
      collapsedTextColor: runtime.unpackOptionalField<Color>(
        data,
        'collapsedTextColor',
      ),
      iconColor: runtime.unpackOptionalField<Color>(data, 'iconColor'),
      collapsedIconColor: runtime.unpackOptionalField<Color>(
        data,
        'collapsedIconColor',
      ),
      shape: runtime.unpackOptionalField<ShapeBorder>(data, 'shape'),
      collapsedShape: runtime.unpackOptionalField<ShapeBorder>(
        data,
        'collapsedShape',
      ),
      clipBehavior: runtime.unpackOptionalField<Clip>(data, 'clipBehavior'),
      controlAffinity: runtime.unpackOptionalField<ListTileControlAffinity>(
        data,
        'controlAffinity',
      ),
      controller: runtime.unpackOptionalField<ExpansibleController>(
        data,
        'controller',
      ),
      dense: runtime.unpackOptionalField<bool>(data, 'dense'),
      splashColor: runtime.unpackOptionalField<Color>(data, 'splashColor'),
      visualDensity: runtime.unpackOptionalField<VisualDensity>(
        data,
        'visualDensity',
      ),
      minTileHeight: runtime.unpackOptionalField<double>(data, 'minTileHeight'),
      enableFeedback: runtime.unpackOptionalField<bool>(data, 'enableFeedback'),
      enabled: runtime.unpackRequiredField<bool>(data, 'enabled'),
      expansionAnimationStyle: runtime.unpackOptionalField<AnimationStyle>(
        data,
        'expansionAnimationStyle',
      ),
      internalAddSemanticForOnTap: runtime.unpackRequiredField<bool>(
        data,
        'internalAddSemanticForOnTap',
      ),
      children: runtime.unpackRequiredField<List<Widget>>(data, 'children'),
    );
  }
}
