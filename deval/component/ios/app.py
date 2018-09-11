# -*- coding: utf-8 -*-

from deval.component.std.appcomponent import AppComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSAppComponent(AppComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        try:
            self.driver = self.dev.iosproxy.driver
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.driver = self.dev.iosproxy.driver

    def start_app(self, package, activity=None):
        self.driver.session(package)

    def stop_app(self, package):
        self.driver.session().close()
