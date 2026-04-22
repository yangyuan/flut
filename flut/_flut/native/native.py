import os
import sys
import platform
from abc import ABC, abstractmethod
from contextlib import contextmanager
from importlib.resources import as_file, files
from typing import Iterator


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
    def run(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        app_id: str | None = None,
        on_initialized=None,
        on_close=None,
    ):
        pass

    @abstractmethod
    async def run_async(
        self,
        method_call_handler,
        flutter_asset_path: str,
        width: int,
        height: int,
        title: str,
        icon_path: str | None = None,
        app_id: str | None = None,
        on_initialized=None,
        on_close=None,
        loop=None,
    ):
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
    def get_default_icon() -> bytes | None:
        icon_resource = files("flut").joinpath("assets/icon.png")
        if not icon_resource.is_file():
            return None
        return icon_resource.read_bytes()

    @staticmethod
    @contextmanager
    def _use_default_icon_path() -> Iterator[str | None]:
        icon_resource = files("flut").joinpath("assets/icon.png")
        if not icon_resource.is_file():
            yield None
            return
        with as_file(icon_resource) as icon_path:
            yield os.fspath(icon_path)

    @staticmethod
    def get_default_assets_path() -> str:
        raise NotImplementedError
