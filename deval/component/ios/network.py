# -*- coding: utf-8 -*-

from deval.component.std.network import NetworkComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def get_ip_address(self):
        return self.proxy.driver.status()['ios']['ip']
