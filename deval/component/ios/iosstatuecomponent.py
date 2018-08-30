# -*- coding: utf-8 -*-

from deval.component.std.component import Component
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios, TOUCH_METHOD, IME_METHOD, CAP_METHOD
from deval.utils.parse import parse_uri


class IOSStatueComponent(Component):
    
    def __init__(self, uri, dev, name="statue"):
        super(IOSStatueComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def device_status(self, **kwargs):
        return self.proxy.driver.status()
