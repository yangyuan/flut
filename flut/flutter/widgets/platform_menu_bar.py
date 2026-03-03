from typing import Optional, override

from flut._flut.engine import FlutEnumObject, _flut_pack_value
from flut.flutter.widgets.framework import Widget


class PlatformProvidedMenuItemType(FlutEnumObject):
    about: "PlatformProvidedMenuItemType"
    quit: "PlatformProvidedMenuItemType"
    servicesSubmenu: "PlatformProvidedMenuItemType"
    hide: "PlatformProvidedMenuItemType"
    hideOtherApplications: "PlatformProvidedMenuItemType"
    showAllApplications: "PlatformProvidedMenuItemType"
    startSpeaking: "PlatformProvidedMenuItemType"
    stopSpeaking: "PlatformProvidedMenuItemType"
    toggleFullScreen: "PlatformProvidedMenuItemType"
    minimizeWindow: "PlatformProvidedMenuItemType"
    zoomWindow: "PlatformProvidedMenuItemType"
    arrangeWindowsInFront: "PlatformProvidedMenuItemType"


class PlatformMenuItem(Widget):
    _flut_type = "PlatformMenuItem"

    def __init__(
        self,
        *,
        label: str,
        shortcut=None,
        onSelected=None,
        key=None,
    ):
        super().__init__(key=key)
        self.label = label
        self.shortcut = shortcut
        self.onSelected = onSelected

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["label"] = self.label
        if self.shortcut is not None:
            result["shortcut"] = _flut_pack_value(self.shortcut)
        if self.onSelected is not None:
            result["onSelected"] = self._register_action(
                self.onSelected, "VoidCallback"
            )._flut_pack()
        return result


class PlatformMenu(Widget):
    _flut_type = "PlatformMenu"

    def __init__(
        self,
        *,
        label: str,
        onOpen=None,
        onClose=None,
        menus: list,
        key=None,
    ):
        super().__init__(key=key)
        self.label = label
        self.onOpen = onOpen
        self.onClose = onClose
        self.menus = menus

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["label"] = self.label
        if self.onOpen is not None:
            result["onOpen"] = self._register_action(
                self.onOpen, "VoidCallback"
            )._flut_pack()
        if self.onClose is not None:
            result["onClose"] = self._register_action(
                self.onClose, "VoidCallback"
            )._flut_pack()
        result["menus"] = [_flut_pack_value(m) for m in self.menus]
        return result


class PlatformMenuItemGroup(Widget):
    _flut_type = "PlatformMenuItemGroup"

    def __init__(
        self,
        *,
        members: list,
        key=None,
    ):
        super().__init__(key=key)
        self.members = members

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["members"] = [_flut_pack_value(m) for m in self.members]
        return result


class PlatformProvidedMenuItem(Widget):
    _flut_type = "PlatformProvidedMenuItem"

    def __init__(
        self,
        *,
        type: PlatformProvidedMenuItemType,
        enabled: bool = True,
        key=None,
    ):
        super().__init__(key=key)
        self.type = type
        self.enabled = enabled

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["type"] = _flut_pack_value(self.type)
        result["enabled"] = self.enabled
        return result


class PlatformMenuBar(Widget):
    _flut_type = "PlatformMenuBar"

    def __init__(
        self,
        *,
        menus: list,
        child: Optional[Widget] = None,
        key=None,
    ):
        super().__init__(key=key)
        self.menus = menus
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["menus"] = [_flut_pack_value(m) for m in self.menus]
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
