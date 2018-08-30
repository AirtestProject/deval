# -*- coding: utf-8 -*-

from deval.component.std.keyeventcomponent import KeyEventComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios, retry_session
from deval.utils.parse import parse_uri


class IOSKeyEventComponent(KeyEventComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSKeyEventComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def keyevent(self, keys, **kwargs):
        """just use as home event"""
        if keys not in ['HOME', 'home', 'Home']:
            raise NotImplementedError
        self.home()

    @retry_session
    def text(self, text, enter=True, **kwargs):
        """bug in wda for now"""
        if enter:
            text += '\n'
        self.proxy.session.send_keys(text)
    
    def home(self, **kwargs):
        return self.proxy.driver.home()
