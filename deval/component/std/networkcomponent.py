# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class NetworkComponent(Component):
    def __init__(self, uri, dev=None, name="network"):
        if name is None:
            super(NetworkComponent, self).__init__(uri, dev, "network")
        else:
            super(NetworkComponent, self).__init__(uri, dev, name)
    
    def get_ip_address(self, *args, **kwargs):
        raise NotImplementedError
