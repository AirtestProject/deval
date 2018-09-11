# -*- coding: utf-8 -*-

import socket
from deval.component.std.networkcomponent import NetworkComponent
from deval.utils.win.winfuncs import get_window, _check_platform_win


class WinNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)
        try:
            self.window = self.dev.window
        except AttributeError:
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.window = self.dev.window

    def get_ip_address(self):
        return socket.gethostbyname(socket.gethostname())
