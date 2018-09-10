# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.ios.app import IOSAppComponent
from deval.component.ios.network import IOSNetworkComponent
from deval.component.ios.input import IOSInputComponent
from deval.component.ios.keyevent import IOSKeyEventComponent
from deval.component.ios.screen import IOSScreenComponent
from deval.component.ios.statue import IOSStatueComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios


class IOSDevice(BaseDevice):

    def __init__(self, uri):
        super(IOSDevice, self).__init__(uri)

        kw = _check_platform_ios(uri)
        self.iosproxy = IOSProxy(**kw)

        self.addComponent(IOSAppComponent(uri, self))
        self.addComponent(IOSNetworkComponent(uri, self))
        self.addComponent(IOSInputComponent(uri, self))
        self.addComponent(IOSKeyEventComponent(uri, self))
        self.addComponent(IOSScreenComponent(uri, self))
        self.addComponent(IOSStatueComponent(uri, self))

    @property
    def uuid(self):
        return self.uri
