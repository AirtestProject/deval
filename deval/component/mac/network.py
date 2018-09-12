# -*- coding: utf-8 -*-

import socket
from deval.component.std.network import NetworkComponent


class MacNetworkComponent(NetworkComponent):

    def __init__(self, name):
        self.name = name

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
