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
        self.addComponent(WinNetworkComponent(uri, self))
        self.addComponent(WinInputComponent(uri, self))
        self.addComponent(WinKeyEventComponent(uri, self))
        self.addComponent(WinRuntimeComponent(uri, self))
        self.addComponent(WinScreenComponent(uri, self))
        self.addComponent(WinAppComponent(uri, self))

    @property
    def uuid(self):
        return self.uri
