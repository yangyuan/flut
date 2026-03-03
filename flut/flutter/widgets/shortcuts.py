from typing import Callable, Optional, override

from flut._flut.engine import FlutEnumObject, FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field
from flut.flutter.services.keyboard_key import LogicalKeyboardKey
from flut.flutter.widgets.framework import Widget


class LockState(FlutEnumObject):
    ignored: "LockState"
    locked: "LockState"
    unlocked: "LockState"


class ShortcutActivator:
    def __init__(self):
        pass


class SingleActivator(FlutValueObject):
    _flut_type = "SingleActivator"

    def __init__(
        self,
        trigger: LogicalKeyboardKey,
        *,
        control: bool = False,
        shift: bool = False,
        alt: bool = False,
        meta: bool = False,
        numLock: LockState = LockState.ignored,
        includeRepeats: bool = True,
    ):
        super().__init__()
        self.trigger = trigger
        self.control = control
        self.shift = shift
        self.alt = alt
        self.meta = meta
        self.numLock = numLock
        self.includeRepeats = includeRepeats

    @staticmethod
    def _flut_unpack(data: dict) -> "SingleActivator":
        return SingleActivator(
            trigger=_flut_unpack_required_field(data, "trigger"),
            control=_flut_unpack_required_field(data, "control"),
            shift=_flut_unpack_required_field(data, "shift"),
            alt=_flut_unpack_required_field(data, "alt"),
            meta=_flut_unpack_required_field(data, "meta"),
            numLock=_flut_unpack_required_field(data, "numLock"),
            includeRepeats=_flut_unpack_required_field(data, "includeRepeats"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["trigger"] = _flut_pack_value(self.trigger)
        result["control"] = _flut_pack_value(self.control)
        result["shift"] = _flut_pack_value(self.shift)
        result["alt"] = _flut_pack_value(self.alt)
        result["meta"] = _flut_pack_value(self.meta)
        result["numLock"] = _flut_pack_value(self.numLock)
        result["includeRepeats"] = _flut_pack_value(self.includeRepeats)
        return result


class CharacterActivator(FlutValueObject):
    _flut_type = "CharacterActivator"

    def __init__(
        self,
        character: str,
        *,
        control: bool = False,
        meta: bool = False,
        alt: bool = False,
        includeRepeats: bool = True,
    ):
        super().__init__()
        self.character = character
        self.control = control
        self.meta = meta
        self.alt = alt
        self.includeRepeats = includeRepeats

    @staticmethod
    def _flut_unpack(data: dict) -> "CharacterActivator":
        return CharacterActivator(
            character=_flut_unpack_required_field(data, "character"),
            control=_flut_unpack_required_field(data, "control"),
            meta=_flut_unpack_required_field(data, "meta"),
            alt=_flut_unpack_required_field(data, "alt"),
            includeRepeats=_flut_unpack_required_field(data, "includeRepeats"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["character"] = _flut_pack_value(self.character)
        result["control"] = _flut_pack_value(self.control)
        result["meta"] = _flut_pack_value(self.meta)
        result["alt"] = _flut_pack_value(self.alt)
        result["includeRepeats"] = _flut_pack_value(self.includeRepeats)
        return result


class Shortcuts(Widget):
    _flut_type = "Shortcuts"

    def __init__(
        self,
        *,
        key=None,
        shortcuts: dict,
        debugLabel: Optional[str] = None,
        includeSemantics: bool = True,
        child: Widget,
    ):
        super().__init__(key=key)
        self.shortcuts = shortcuts
        self.debugLabel = debugLabel
        self.includeSemantics = includeSemantics
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        shortcuts_list = []
        for activator, intent in self.shortcuts.items():
            entry = {
                "activator": _flut_pack_value(activator),
                "intentName": type(intent).__name__,
            }
            data = {}
            for k, v in intent.__dict__.items():
                if not k.startswith("_"):
                    data[k] = _flut_pack_value(v)
            if data:
                entry["intentData"] = data
            shortcuts_list.append(entry)
        result["shortcuts"] = shortcuts_list
        if self.debugLabel is not None:
            result["debugLabel"] = _flut_pack_value(self.debugLabel)
        result["includeSemantics"] = _flut_pack_value(self.includeSemantics)
        result["child"] = _flut_pack_value(self.child)
        return result


class CallbackShortcuts(Widget):
    _flut_type = "CallbackShortcuts"

    def __init__(self, *, key=None, bindings: dict, child: Widget):
        super().__init__(key=key)
        self.bindings = bindings
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        bindings_list = []
        for activator, callback in self.bindings.items():
            cb = self._register_action(callback, "VoidCallback")
            bindings_list.append(
                {
                    "activator": _flut_pack_value(activator),
                    "callback": cb._flut_pack(),
                }
            )
        result["bindings"] = bindings_list
        result["child"] = _flut_pack_value(self.child)
        return result
