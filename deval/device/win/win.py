# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.win.app import WinAppComponent
from deval.component.win.input import WinInputComponent
from deval.component.win.keyevent import WinKeyEventComponent
from deval.component.win.network import WinNetworkComponent
from deval.component.win.runtime import WinRuntimeComponent
from deval.component.win.screen import WinScreenComponent
from deval.component.win.utils.winfuncs import get_app, get_window


class WinDevice(DeviceBase):

    def __init__(self, uri):
        super(WinDevice, self).__init__(uri)
        self.application = get_app(uri)
        self.window = get_window(uri)
        self.handle = self.window.handle
        self.add_component(WinNetworkComponent("network", self, uri))
        self.add_component(WinInputComponent("input", self, uri))
        self.add_component(WinKeyEventComponent("keyevent", self, uri))
        self.add_component(WinRuntimeComponent("runtime", self, uri))
        self.add_component(WinScreenComponent("screen", self, uri))
        self.add_component(WinAppComponent("app", self, uri))

    @property
    def uuid(self):
        return self.handle
