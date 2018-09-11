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

        self.addComponent(IOSAppComponent("app", self, uri))
        self.addComponent(IOSNetworkComponent("network", self, uri))
        self.addComponent(IOSInputComponent("input", self, uri))
        self.addComponent(IOSKeyEventComponent("keyevent", self, uri))
        self.addComponent(IOSScreenComponent("screen", self, uri))
        self.addComponent(IOSStatueComponent("statue", self, uri))

    @property
    def uuid(self):
        try:
            return self.iosproxy.addr
        except AttributeError:
            self.iosproxy = IOSProxy(
                **_check_platform_ios(self.uri))
            return self.iosproxy.addr
