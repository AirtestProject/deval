# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.ios.app import IOSAppComponent
from deval.component.ios.network import IOSNetworkComponent
from deval.component.ios.input import IOSInputComponent
from deval.component.ios.keyevent import IOSKeyEventComponent
from deval.component.ios.screen import IOSScreenComponent
from deval.component.ios.statue import IOSStatueComponent
from deval.component.ios.utils.iosfuncs import IOSProxy, check_platform_ios


class IOSDevice(DeviceBase):

    def __init__(self, uri):
        super(IOSDevice, self).__init__(uri)

        kw = check_platform_ios(uri)
        self.iosproxy = IOSProxy(**kw)

        self.add_component(IOSAppComponent("app", self, uri))
        self.add_component(IOSNetworkComponent("network", self, uri))
        self.add_component(IOSInputComponent("input", self, uri))
        self.add_component(IOSKeyEventComponent("keyevent", self, uri))
        self.add_component(IOSScreenComponent("screen", self, uri))
        self.add_component(IOSStatueComponent("statue", self, uri))

    @property
    def uuid(self):
        try:
            return self.iosproxy.addr
        except AttributeError:
            self.iosproxy = IOSProxy(
                **check_platform_ios(self.uri))
            return self.iosproxy.addr
