# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.ios.iosappcomponent import IOSAppComponent
from deval.component.ios.iosnetworkcomponent import IOSNetworkComponent
from deval.component.ios.iosinputcomponent import IOSInputComponent
from deval.component.ios.ioskeyeventcomponent import IOSKeyEventComponent
from deval.component.ios.iosscreencomponent import IOSScreenComponent
from deval.component.ios.iosstatuecomponent import IOSStatueComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios


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
