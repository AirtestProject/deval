# -*- coding: utf-8 -*-

import socket
from deval.component.std.network import NetworkComponent
from deval.component.win.utils.winfuncs import get_window, check_platform_win


class WinNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self._name = name

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        