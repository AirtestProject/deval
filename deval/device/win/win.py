# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.win.app import WinAppComponent
from deval.component.win.input import WinInputComponent
from deval.component.win.keyevent import WinKeyEventComponent
from deval.component.win.network import WinNetworkComponent
from deval.component.win.runtime import WinRuntimeComponent
from deval.component.win.screen import WinScreenComponent
from deval.utils.win.winfuncs import get_app, get_window, _check_platform_win


class WinDevice(BaseDevice):

    def __init__(self, uri):
        super(WinDevice, self).__init__(uri)
        self.app = get_app(_check_platform_win(uri))
        self.window = get_window(_check_platform_win(uri))
        self.handle = self.window.handle
        self.addComponent(WinNetworkComponent("network", self, uri))
        self.addComponent(WinInputComponent("input", self, uri))
        self.addComponent(WinKeyEventComponent("keyevent", self, uri))
        self.addComponent(WinRuntimeComponent("runtime", self, uri))
        self.addComponent(WinScreenComponent("screen", self, uri))
        self.addComponent(WinAppComponent("app", self, uri))

    @property
    def uuid(self):
        return self.handle
