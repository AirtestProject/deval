# -*- coding: utf-8 -*-

import socket
from deval.component.std.networkcomponent import NetworkComponent


class LinuxNetworkComponent(NetworkComponent):

    def __init__(self, uri, dev, name=None):
        super(LinuxNetworkComponent, self).__init__(uri, dev, name)

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())
