import logging
from flut._flut.engine import FlutRealtimeObject, FlutSingletonInstance

logger = logging.getLogger(__name__)


class SchedulerBinding(FlutRealtimeObject):
    _flut_type = "SchedulerBinding"

    instance: "SchedulerBinding" = FlutSingletonInstance()

    def addPostFrameCallback(self, callback, debugLabel="callback"):
        action_id = self._register_oneshot_action(lambda *args: callback(None))
        self._flut_call(
            "addPostFrameCallback", callbackId=action_id, debugLabel=debugLabel
        )
