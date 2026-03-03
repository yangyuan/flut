from typing import Callable, Optional, override

from flut._flut.engine import FlutValueObject, FlutRealtimeObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class Intent(FlutValueObject):
    _flut_type = "Intent"

    def __init__(self):
        super().__init__()

    @staticmethod
    def _flut_unpack(data: dict) -> "Intent":
        return Intent()

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["intentName"] = type(self).__name__
        data = {}
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                data[k] = _flut_pack_value(v)
        if data:
            result["data"] = data
        return result


def _reconstruct_intent(intent_class, intent_data):
    intent = intent_class.__new__(intent_class)
    Intent.__init__(intent)
    if intent_data and isinstance(intent_data, dict):
        for k, v in intent_data.items():
            setattr(intent, k, v)
    return intent


class CallbackAction:
    def __init__(self, *, onInvoke: Callable):
        self.onInvoke = onInvoke


class ActionDispatcher(FlutRealtimeObject):
    _flut_type = "ActionDispatcher"

    def __init__(self):
        super().__init__()
        self._flut_create()

    def invokeAction(self, action, intent, context=None):
        return action.onInvoke(intent)


class Actions(Widget):
    _flut_type = "Actions"

    def __init__(
        self,
        *,
        key=None,
        dispatcher: "ActionDispatcher | None" = None,
        actions: dict,
        child: Widget,
    ):
        super().__init__(key=key)
        self.dispatcher = dispatcher
        self.actions = actions
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        actions_map = {}
        for intent_class, action in self.actions.items():
            intent_name = intent_class.__name__
            user_fn = action.onInvoke
            cls = intent_class

            def _make_wrapper(c, f, action_obj, disp):
                def _wrapper(intent_data=None):
                    intent = _reconstruct_intent(c, intent_data)
                    if disp is not None:
                        return disp.invokeAction(action_obj, intent)
                    return f(intent)

                return _wrapper

            wrapper = _make_wrapper(cls, user_fn, action, self.dispatcher)
            action_cb = self._register_action(wrapper, "VoidCallback")
            actions_map[intent_name] = action_cb._flut_pack()
        result["actions"] = actions_map
        if self.dispatcher is not None:
            result["dispatcher"] = _flut_pack_value(self.dispatcher)
        result["child"] = _flut_pack_value(self.child)
        return result

    @staticmethod
    def invoke(context, intent):
        from flut._flut.engine import call_dart_static

        return call_dart_static(
            "Actions", "invoke", context._flut_pack(), intent._flut_pack()
        )

    @staticmethod
    def maybeInvoke(context, intent):
        from flut._flut.engine import call_dart_static

        return call_dart_static(
            "Actions", "maybeInvoke", context._flut_pack(), intent._flut_pack()
        )
