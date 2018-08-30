# -*- coding: utf-8 -*-

from deval.component.std.networkcomponent import NetworkComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSNetworkComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def get_ip_address(self, **kwargs):
        return self.proxy.driver.status()['ios']['ip']
