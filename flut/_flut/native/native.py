import os
import sys
import platform
from abc import ABC, abstractmethod


class FlutNative(ABC):
    @staticmethod
    def _create() -> "FlutNative":
        if os.name == "nt":
            from .windows import FlutWindowsNative

            return FlutWindowsNative()
        elif sys.platform == "darwin":
            from .macos import FlutMacOSNative

            return FlutMacOSNative()
        elif sys.platform.startswith("linux"):
            from .linux import FlutLinuxNative

            return FlutLinuxNative()
        else:
            raise NotImplementedError(f"Platform {sys.platform} not supported yet.")

    @staticmethod
    def _get_arch() -> str:
        machine = platform.machine().lower()
        if machine in ("amd64", "x86_64", "x64"):
            return "x64"
        elif machine in ("arm64", "aarch64"):
            return "arm64"
        return "x64"

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def run(self, method_call_handler, assets_path: str, width: int, height: int):
        pass

    @abstractmethod
    def setup_call_dart(self, callback_addr):
        pass

    @abstractmethod
    def setup_notify_dart(self, callback_addr):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    def trim_notify_keepalive(self, processed_count):
        trim_count = processed_count - self._notify_acked
        if trim_count > 0:
            if trim_count > len(self._notify_keepalive):
                trim_count = len(self._notify_keepalive)
            del self._notify_keepalive[:trim_count]
            self._notify_acked += trim_count

    @staticmethod
    def get_default_assets_path() -> str:
        raise NotImplementedError
