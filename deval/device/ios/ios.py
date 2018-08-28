# -*- coding: utf-8 -*-

from deval.device.device import BaseDevice
from deval.component.ios.ioscomponent import IOSAppComponent, IOSNetworkComponent, IOSInputComponent
from deval.component.ios.ioscomponent import IOSKeyEventComponent, IOSScreenComponent, IOSStatueComponent
from deval.core.ios.iosfuncs import IOSProxy, _check_platform_ios


class IOSDevice(BaseDevice):
    
    def __init__(self, uri):
        super(IOSDevice, self).__init__()

        kw = _check_platform_ios(uri)
        self.iosproxy = IOSProxy(**kw)

        self.addComponent(IOSAppComponent(uri, self))
        self.addComponent(IOSNetworkComponent(uri, self))
        self.addComponent(IOSInputComponent(uri, self))
        self.addComponent(IOSKeyEventComponent(uri, self))
        self.addComponent(IOSScreenComponent(uri, self))
        self.addComponent(IOSStatueComponent(uri, self))

        self.uri = uri

    @property
    def uuid(self):
        return self.uri

