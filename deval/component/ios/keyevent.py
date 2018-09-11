# -*- coding: utf-8 -*-

from deval.component.std.keyevent import KeyEventComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios, retry_session
from deval.utils.parse import parse_uri


class IOSKeyEventComponent(KeyEventComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def keyevent(self, keys):
        """just use as home event"""
        if keys not in ['HOME', 'home', 'Home']:
            raise NotImplementedError
        self.home()

    @retry_session
    def text(self, text, enter=True):
        """bug in wda for now"""
        if enter:
            text += '\n'
        self.proxy.session.send_keys(text)

    def home(self):
        return self.proxy.driver.home()
