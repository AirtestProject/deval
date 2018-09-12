# -*- coding: utf-8 -*-

from deval.component.std.component import Component
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios, TOUCH_METHOD, IME_METHOD, CAP_METHOD
from deval.utils.parse import parse_uri


class IOSStatueComponent(Component):

    def __init__(self, name, dev, uri):
        self.name = name
        self.device = dev
        try:
            self.proxy = self.device.iosproxy
        except AttributeError:
            self.device.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.device.iosproxy

    def device_status(self):
        return self.proxy.driver.status()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
