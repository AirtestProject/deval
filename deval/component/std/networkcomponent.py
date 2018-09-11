# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class NetworkComponent(Component):

    def get_ip_address(self):
        """
        Get the current device IP address
        """
        raise NotImplementedError
