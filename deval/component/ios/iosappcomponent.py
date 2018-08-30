# -*- coding: utf-8 -*-

from deval.component.std.appcomponent import AppComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSAppComponent(AppComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSAppComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def start_app(self, package, activity=None, **kwargs):
        self.proxy.driver.session(package)

    def stop_app(self, package, **kwargs):
        self.proxy.driver.session().close()
