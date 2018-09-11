# -*- coding: utf-8 -*-

from deval.component.std.networkcomponent import NetworkComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri


class AndroidNetworkComponent(NetworkComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb

    def get_ip_address(self):
        return self.adb.get_ip_address()
