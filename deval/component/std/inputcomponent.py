# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class InputComponent(Component):
    def __init__(self, uri, dev=None, name="input"):
        if name is None:
            super(InputComponent, self).__init__(uri, dev, "input")
        else:
            super(InputComponent, self).__init__(uri, dev, name)

    def click(self, pos, duration=0.05, button='left'):
        raise NotImplementedError

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        raise NotImplementedError

    def pinch(self, *args, **kwargs):
        raise NotImplementedError

    def double_tap(self, pos, button='left'):
        raise NotImplementedError

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        raise NotImplementedError
