# -*- coding: utf-8 -*-

from deval.component.std.app import AppComponent
from deval.component.win.utils.winfuncs import get_app
from deval.component.win.utils.winfuncs import Application, get_window


class WinAppComponent(AppComponent):
    
    def __init__(self, name, dev, uri):
        self._name = name
        self.uri = uri
        self.device = dev
        try:
            self.application = self.device.application
            self.window = self.device.window
        except AttributeError:
            self.device.app = get_app(self.uri)
            self.device.window = get_window(self.uri)
            self.window = self.device.window
            self.application = self.device.application

    def start(self, path, **kwargs):
        return Application().start(path)

    def stop(self, app=None):
        if app is None and self.application:
            self.application.kill()
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
        