# -*- coding: utf-8 -*-

from deval.component.std.screen import ScreenComponent
from deval.component.win.utils.winfuncs import get_app, get_rect, get_window
from deval.component.win.utils.winfuncs import Application, screenshot
from deval.utils.cv import crop_image, imwrite


class WinScreenComponent(ScreenComponent):

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
            self.application = self.device.application
            self.window = self.device.window
        self.handle = self.device.window.handle

    def snapshot(self, filename="tmp.png"):
        if not filename:
            filename = "tmp.png"

        if self.handle:
            screen = screenshot(filename, self.handle)
        else:
            screen = screenshot(filename)
            if self.application:
                rect = get_rect(self.window)
                screen = crop_image(
                    screen, [rect.left, rect.top, rect.right, rect.bottom])
        if not screen.any():
            if self.application:
                rect = get_rect(self.window)
                screen = crop_image(screenshot(filename), [
                                    rect.left, rect.top, rect.right, rect.bottom])
        if filename:
            imwrite(filename, screen)
        return screen

    def move(self, pos):
        # not stable, use carefully
        if self.window:
            self.window.MoveWindow(x=pos[0], y=pos[1])

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        