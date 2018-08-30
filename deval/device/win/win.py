# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.win.winappcomponent import WinAppComponent
from deval.component.win.wininputcomponent import WinInputComponent
from deval.component.win.winkeyeventcomponent import WinKeyEventComponent
from deval.component.win.winnetworkcomponent import WinNetworkComponent
from deval.component.win.winruntimecomponent import WinRuntimeComponent
from deval.component.win.winscreencomponent import WinScreenComponent
from deval.utils.win.winfuncs import get_app, get_window, _check_platform_win


class WinDevice(BaseDevice):

    def __init__(self, uri):
        super(WinDevice, self).__init__()
        self.app = get_app(_check_platform_win(uri))
        self.window = get_window(_check_platform_win(uri))
        self.addComponent(WinNetworkComponent(uri, self))
        self.addComponent(WinInputComponent(uri, self))
        self.addComponent(WinKeyEventComponent(uri, self))
        self.addComponent(WinRuntimeComponent(uri, self))
        self.addComponent(WinScreenComponent(uri, self))
        self.addComponent(WinAppComponent(uri, self))

        self.uri = uri
        
    @property
    def uuid(self):
        return self.uri
