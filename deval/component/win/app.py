# -*- coding: utf-8 -*-

from deval.component.std.appcomponent import AppComponent
from deval.utils.win.winfuncs import get_app
from deval.utils.win.winfuncs import Application, get_window
from deval.utils.win.winfuncs import _check_platform_win


class WinAppComponent(AppComponent):
    
    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)
        try:
            self.app = self.dev.app
            self.window = self.dev.window
        except AttributeError:
            self.dev.app = get_app(_check_platform_win(self.uri))
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.window = self.dev.window
            self.app = self.dev.app

    def start_app(self, path, **kwargs):
        return Application().start(path)

    def stop_app(self, app=None):
        if app is None and self.app:
            self.app.kill()
            return
        if app:
            app.kill()

    def get_title(self):
        if self.window:
            return self.window.texts()
