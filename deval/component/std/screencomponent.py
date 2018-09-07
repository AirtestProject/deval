# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class ScreenComponent(Component):
    def __init__(self, uri, dev=None, name="screen"):
        if name is None:
            super(ScreenComponent, self).__init__(uri, dev, "screen")
        else:
            super(ScreenComponent, self).__init__(uri, dev, name)

    def snapshot(self, filename, ensure_orientation=True):
        raise NotImplementedError

    def move(self, pos):
        raise NotImplementedError
