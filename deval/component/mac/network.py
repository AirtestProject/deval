# -*- coding: utf-8 -*-

import socket
from deval.component.std.networkcomponent import NetworkComponent


class MacNetworkComponent(NetworkComponent):

    def __init__(self, uri, dev, name=None):
        super(MacNetworkComponent, self).__init__(uri, dev, name)

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())
