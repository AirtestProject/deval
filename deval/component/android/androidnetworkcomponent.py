# -*- coding: utf-8 -*-

from deval.component.std.networkcomponent import NetworkComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android
from deval.utils.parse import parse_uri


class AndroidNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidNetworkComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def get_ip_address(self, **kwargs):
        return self.proxy.adb.get_ip_address()
