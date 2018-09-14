# -*- coding: utf-8 -*-

from deval.component.std.network import NetworkComponent


class AndroidNetworkComponent(NetworkComponent):

    def __init__(self, name, dev):
        self._name = name
        self.adb = dev.adb

    def get_ip_address(self):
        return self.adb.get_ip_address()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        