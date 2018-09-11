# -*- coding: utf-8 -*-

import socket
from deval.component.std.networkcomponent import NetworkComponent


class LinuxNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())
