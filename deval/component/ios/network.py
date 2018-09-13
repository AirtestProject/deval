# -*- coding: utf-8 -*-

from deval.component.std.network import NetworkComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self._name = name
        self.device = dev
        try:
            self.proxy = self.device.iosproxy
        except AttributeError:
            self.device.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.device.iosproxy

    def get_ip_address(self):
        return self.proxy.driver.status()['ios']['ip']
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
