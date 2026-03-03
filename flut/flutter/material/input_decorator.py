from typing import Optional, override
from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class FloatingLabelBehavior(FlutEnumObject):
    never: "FloatingLabelBehavior"
    auto: "FloatingLabelBehavior"
    always: "FloatingLabelBehavior"


class InputDecoration(FlutValueObject):
    _flut_type = "InputDecoration"

    def __init__(
        self,
        *,
        icon=None,
        iconColor=None,
        label=None,
        labelText: Optional[str] = None,
        labelStyle=None,
        floatingLabelStyle=None,
        helper=None,
        helperText: Optional[str] = None,
        helperStyle=None,
        helperMaxLines: Optional[int] = None,
        hintText: Optional[str] = None,
        hint=None,
        hintStyle=None,
        hintTextDirection=None,
        hintMaxLines: Optional[int] = None,
        hintFadeDuration=None,
        maintainHintSize: bool = True,
        maintainLabelSize: bool = False,
        error=None,
        errorText: Optional[str] = None,
        errorStyle=None,
        errorMaxLines: Optional[int] = None,
        floatingLabelBehavior=None,
        floatingLabelAlignment=None,
        isCollapsed: Optional[bool] = None,
        isDense: Optional[bool] = None,
        contentPadding=None,
        prefixIcon=None,
        prefixIconConstraints=None,
        prefix=None,
        prefixText: Optional[str] = None,
        prefixStyle=None,
        prefixIconColor=None,
        suffixIcon=None,
        suffix=None,
        suffixText: Optional[str] = None,
        suffixStyle=None,
        suffixIconColor=None,
        suffixIconConstraints=None,
        counter=None,
        counterText: Optional[str] = None,
        counterStyle=None,
        filled: Optional[bool] = None,
        fillColor=None,
        focusColor=None,
        hoverColor=None,
        errorBorder=None,
        focusedBorder=None,
        focusedErrorBorder=None,
        disabledBorder=None,
        enabledBorder=None,
        border=None,
        enabled: bool = True,
        semanticCounterText: Optional[str] = None,
        alignLabelWithHint: Optional[bool] = None,
        constraints=None,
        visualDensity=None,
    ):
        super().__init__()
        self.icon = icon
        self.iconColor = iconColor
        self.label = label
        self.labelText = labelText
        self.labelStyle = labelStyle
        self.floatingLabelStyle = floatingLabelStyle
        self.helper = helper
        self.helperText = helperText
        self.helperStyle = helperStyle
        self.helperMaxLines = helperMaxLines
        self.hintText = hintText
        self.hint = hint
        self.hintStyle = hintStyle
        self.hintTextDirection = hintTextDirection
        self.hintMaxLines = hintMaxLines
        self.hintFadeDuration = hintFadeDuration
        self.maintainHintSize = maintainHintSize
        self.maintainLabelSize = maintainLabelSize
        self.error = error
        self.errorText = errorText
        self.errorStyle = errorStyle
        self.errorMaxLines = errorMaxLines
        self.floatingLabelBehavior = floatingLabelBehavior
        self.floatingLabelAlignment = floatingLabelAlignment
        self.isCollapsed = isCollapsed
        self.isDense = isDense
        self.contentPadding = contentPadding
        self.prefixIcon = prefixIcon
        self.prefixIconConstraints = prefixIconConstraints
        self.prefix = prefix
        self.prefixText = prefixText
        self.prefixStyle = prefixStyle
        self.prefixIconColor = prefixIconColor
        self.suffixIcon = suffixIcon
        self.suffix = suffix
        self.suffixText = suffixText
        self.suffixStyle = suffixStyle
        self.suffixIconColor = suffixIconColor
        self.suffixIconConstraints = suffixIconConstraints
        self.counter = counter
        self.counterText = counterText
        self.counterStyle = counterStyle
        self.filled = filled
        self.fillColor = fillColor
        self.focusColor = focusColor
        self.hoverColor = hoverColor
        self.errorBorder = errorBorder
        self.focusedBorder = focusedBorder
        self.focusedErrorBorder = focusedErrorBorder
        self.disabledBorder = disabledBorder
        self.enabledBorder = enabledBorder
        self.border = border
        self.enabled = enabled
        self.semanticCounterText = semanticCounterText
        self.alignLabelWithHint = alignLabelWithHint
        self.constraints = constraints
        self.visualDensity = visualDensity

    @staticmethod
    def _flut_unpack(data: dict) -> "InputDecoration":
        return InputDecoration(
            icon=_flut_unpack_optional_field(data, "icon"),
            iconColor=_flut_unpack_optional_field(data, "iconColor"),
            label=_flut_unpack_optional_field(data, "label"),
            labelText=_flut_unpack_optional_field(data, "labelText"),
            labelStyle=_flut_unpack_optional_field(data, "labelStyle"),
            floatingLabelStyle=_flut_unpack_optional_field(data, "floatingLabelStyle"),
            helper=_flut_unpack_optional_field(data, "helper"),
            helperText=_flut_unpack_optional_field(data, "helperText"),
            helperStyle=_flut_unpack_optional_field(data, "helperStyle"),
            helperMaxLines=_flut_unpack_optional_field(data, "helperMaxLines"),
            hintText=_flut_unpack_optional_field(data, "hintText"),
            hint=_flut_unpack_optional_field(data, "hint"),
            hintStyle=_flut_unpack_optional_field(data, "hintStyle"),
            hintTextDirection=_flut_unpack_optional_field(data, "hintTextDirection"),
            hintMaxLines=_flut_unpack_optional_field(data, "hintMaxLines"),
            hintFadeDuration=_flut_unpack_optional_field(data, "hintFadeDuration"),
            maintainHintSize=_flut_unpack_required_field(data, "maintainHintSize"),
            maintainLabelSize=_flut_unpack_required_field(data, "maintainLabelSize"),
            error=_flut_unpack_optional_field(data, "error"),
            errorText=_flut_unpack_optional_field(data, "errorText"),
            errorStyle=_flut_unpack_optional_field(data, "errorStyle"),
            errorMaxLines=_flut_unpack_optional_field(data, "errorMaxLines"),
            floatingLabelBehavior=_flut_unpack_optional_field(
                data, "floatingLabelBehavior"
            ),
            floatingLabelAlignment=_flut_unpack_optional_field(
                data, "floatingLabelAlignment"
            ),
            isCollapsed=_flut_unpack_optional_field(data, "isCollapsed"),
            isDense=_flut_unpack_optional_field(data, "isDense"),
            contentPadding=_flut_unpack_optional_field(data, "contentPadding"),
            prefixIcon=_flut_unpack_optional_field(data, "prefixIcon"),
            prefixIconConstraints=_flut_unpack_optional_field(
                data, "prefixIconConstraints"
            ),
            prefix=_flut_unpack_optional_field(data, "prefix"),
            prefixText=_flut_unpack_optional_field(data, "prefixText"),
            prefixStyle=_flut_unpack_optional_field(data, "prefixStyle"),
            prefixIconColor=_flut_unpack_optional_field(data, "prefixIconColor"),
            suffixIcon=_flut_unpack_optional_field(data, "suffixIcon"),
            suffix=_flut_unpack_optional_field(data, "suffix"),
            suffixText=_flut_unpack_optional_field(data, "suffixText"),
            suffixStyle=_flut_unpack_optional_field(data, "suffixStyle"),
            suffixIconColor=_flut_unpack_optional_field(data, "suffixIconColor"),
            suffixIconConstraints=_flut_unpack_optional_field(
                data, "suffixIconConstraints"
            ),
            counter=_flut_unpack_optional_field(data, "counter"),
            counterText=_flut_unpack_optional_field(data, "counterText"),
            counterStyle=_flut_unpack_optional_field(data, "counterStyle"),
            filled=_flut_unpack_optional_field(data, "filled"),
            fillColor=_flut_unpack_optional_field(data, "fillColor"),
            focusColor=_flut_unpack_optional_field(data, "focusColor"),
            hoverColor=_flut_unpack_optional_field(data, "hoverColor"),
            errorBorder=_flut_unpack_optional_field(data, "errorBorder"),
            focusedBorder=_flut_unpack_optional_field(data, "focusedBorder"),
            focusedErrorBorder=_flut_unpack_optional_field(data, "focusedErrorBorder"),
            disabledBorder=_flut_unpack_optional_field(data, "disabledBorder"),
            enabledBorder=_flut_unpack_optional_field(data, "enabledBorder"),
            border=_flut_unpack_optional_field(data, "border"),
            enabled=_flut_unpack_required_field(data, "enabled"),
            semanticCounterText=_flut_unpack_optional_field(
                data, "semanticCounterText"
            ),
            alignLabelWithHint=_flut_unpack_optional_field(data, "alignLabelWithHint"),
            constraints=_flut_unpack_optional_field(data, "constraints"),
            visualDensity=_flut_unpack_optional_field(data, "visualDensity"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.icon is not None:
            result["icon"] = _flut_pack_value(self.icon)
        if self.iconColor is not None:
            result["iconColor"] = _flut_pack_value(self.iconColor)
        if self.label is not None:
            result["label"] = _flut_pack_value(self.label)
        if self.labelText is not None:
            result["labelText"] = _flut_pack_value(self.labelText)
        if self.labelStyle is not None:
            result["labelStyle"] = _flut_pack_value(self.labelStyle)
        if self.floatingLabelStyle is not None:
            result["floatingLabelStyle"] = _flut_pack_value(self.floatingLabelStyle)
        if self.helper is not None:
            result["helper"] = _flut_pack_value(self.helper)
        if self.helperText is not None:
            result["helperText"] = _flut_pack_value(self.helperText)
        if self.helperStyle is not None:
            result["helperStyle"] = _flut_pack_value(self.helperStyle)
        if self.helperMaxLines is not None:
            result["helperMaxLines"] = _flut_pack_value(self.helperMaxLines)
        if self.hintText is not None:
            result["hintText"] = _flut_pack_value(self.hintText)
        if self.hint is not None:
            result["hint"] = _flut_pack_value(self.hint)
        if self.hintStyle is not None:
            result["hintStyle"] = _flut_pack_value(self.hintStyle)
        if self.hintTextDirection is not None:
            result["hintTextDirection"] = _flut_pack_value(self.hintTextDirection)
        if self.hintMaxLines is not None:
            result["hintMaxLines"] = _flut_pack_value(self.hintMaxLines)
        if self.hintFadeDuration is not None:
            result["hintFadeDuration"] = _flut_pack_value(self.hintFadeDuration)
        result["maintainHintSize"] = _flut_pack_value(self.maintainHintSize)
        result["maintainLabelSize"] = _flut_pack_value(self.maintainLabelSize)
        if self.error is not None:
            result["error"] = _flut_pack_value(self.error)
        if self.errorText is not None:
            result["errorText"] = _flut_pack_value(self.errorText)
        if self.errorStyle is not None:
            result["errorStyle"] = _flut_pack_value(self.errorStyle)
        if self.errorMaxLines is not None:
            result["errorMaxLines"] = _flut_pack_value(self.errorMaxLines)
        if self.floatingLabelBehavior is not None:
            result["floatingLabelBehavior"] = _flut_pack_value(
                self.floatingLabelBehavior
            )
        if self.floatingLabelAlignment is not None:
            result["floatingLabelAlignment"] = _flut_pack_value(
                self.floatingLabelAlignment
            )
        if self.isCollapsed is not None:
            result["isCollapsed"] = _flut_pack_value(self.isCollapsed)
        if self.isDense is not None:
            result["isDense"] = _flut_pack_value(self.isDense)
        if self.contentPadding is not None:
            result["contentPadding"] = _flut_pack_value(self.contentPadding)
        if self.prefixIcon is not None:
            result["prefixIcon"] = _flut_pack_value(self.prefixIcon)
        if self.prefixIconConstraints is not None:
            result["prefixIconConstraints"] = _flut_pack_value(
                self.prefixIconConstraints
            )
        if self.prefix is not None:
            result["prefix"] = _flut_pack_value(self.prefix)
        if self.prefixText is not None:
            result["prefixText"] = _flut_pack_value(self.prefixText)
        if self.prefixStyle is not None:
            result["prefixStyle"] = _flut_pack_value(self.prefixStyle)
        if self.prefixIconColor is not None:
            result["prefixIconColor"] = _flut_pack_value(self.prefixIconColor)
        if self.suffixIcon is not None:
            result["suffixIcon"] = _flut_pack_value(self.suffixIcon)
        if self.suffix is not None:
            result["suffix"] = _flut_pack_value(self.suffix)
        if self.suffixText is not None:
            result["suffixText"] = _flut_pack_value(self.suffixText)
        if self.suffixStyle is not None:
            result["suffixStyle"] = _flut_pack_value(self.suffixStyle)
        if self.suffixIconColor is not None:
            result["suffixIconColor"] = _flut_pack_value(self.suffixIconColor)
        if self.suffixIconConstraints is not None:
            result["suffixIconConstraints"] = _flut_pack_value(
                self.suffixIconConstraints
            )
        if self.counter is not None:
            result["counter"] = _flut_pack_value(self.counter)
        if self.counterText is not None:
            result["counterText"] = _flut_pack_value(self.counterText)
        if self.counterStyle is not None:
            result["counterStyle"] = _flut_pack_value(self.counterStyle)
        if self.filled is not None:
            result["filled"] = _flut_pack_value(self.filled)
        if self.fillColor is not None:
            result["fillColor"] = _flut_pack_value(self.fillColor)
        if self.focusColor is not None:
            result["focusColor"] = _flut_pack_value(self.focusColor)
        if self.hoverColor is not None:
            result["hoverColor"] = _flut_pack_value(self.hoverColor)
        if self.errorBorder is not None:
            result["errorBorder"] = _flut_pack_value(self.errorBorder)
        if self.focusedBorder is not None:
            result["focusedBorder"] = _flut_pack_value(self.focusedBorder)
        if self.focusedErrorBorder is not None:
            result["focusedErrorBorder"] = _flut_pack_value(self.focusedErrorBorder)
        if self.disabledBorder is not None:
            result["disabledBorder"] = _flut_pack_value(self.disabledBorder)
        if self.enabledBorder is not None:
            result["enabledBorder"] = _flut_pack_value(self.enabledBorder)
        if self.border is not None:
            result["border"] = _flut_pack_value(self.border)
        result["enabled"] = _flut_pack_value(self.enabled)
        if self.semanticCounterText is not None:
            result["semanticCounterText"] = _flut_pack_value(self.semanticCounterText)
        if self.alignLabelWithHint is not None:
            result["alignLabelWithHint"] = _flut_pack_value(self.alignLabelWithHint)
        if self.constraints is not None:
            result["constraints"] = _flut_pack_value(self.constraints)
        if self.visualDensity is not None:
            result["visualDensity"] = _flut_pack_value(self.visualDensity)
        return result
