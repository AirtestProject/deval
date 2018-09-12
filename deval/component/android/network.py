# -*- coding: utf-8 -*-

from deval.component.std.network import NetworkComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri


class AndroidNetworkComponent(NetworkComponent):

    def __init__(self, name, dev):
        self.name = name
        self.adb = dev.adb

    def get_ip_address(self):
        return self.adb.get_ip_address()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        