# -*- coding: utf-8 -*-

from deval.component.std.app import AppComponent
from deval.component.win.utils.winfuncs import get_app
from deval.component.win.utils.winfuncs import Application, get_window
from deval.component.win.utils.winfuncs import check_platform_win


class WinAppComponent(AppComponent):
    
    def __init__(self, name, dev, uri):
        self._name = name
        self.uri = uri
        self.device = dev
        try:
            self.app = self.dev.app
            self.window = self.dev.window
        except AttributeError:
            self.device.app = get_app(check_platform_win(self.uri))
            self.device.window = get_window(check_platform_win(self.uri))
            self.window = self.device.window
            self.app = self.device.app

    def start(self, path, **kwargs):
        return Application().start(path)

    def stop(self, app=None):
        if app is None and self.app:
            self.app.kill()
            return
        if app:
            app.kill()

    def get_title(self):
        if self.window:
            return self.window.texts()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        