# -*- coding: utf-8 -*-

from deval.component.std.app import AppComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios
from deval.utils.parse import parse_uri


class IOSAppComponent(AppComponent):

    def __init__(self, name, dev, uri):
        self.name = name
        self.device = dev
        try:
            self.driver = self.dev.iosproxy.driver
        except AttributeError:
            self.device.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.driver = self.device.iosproxy.driver

    def start(self, package, activity=None):
        self.driver.session(package)

    def stop(self, package):
        self.driver.session().close()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
