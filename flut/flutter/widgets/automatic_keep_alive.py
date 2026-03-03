class AutomaticKeepAliveClientMixin:
    _flut_want_keep_alive = True

    @property
    def wantKeepAlive(self) -> bool:
        return True

    @wantKeepAlive.setter
    def wantKeepAlive(self, value: bool):
        self._flut_want_keep_alive = value
        self._flut_call("updateKeepAlive", value)
