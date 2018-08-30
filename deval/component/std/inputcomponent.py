# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class InputComponent(Component):
    def __init__(self, uri, dev=None, name="input"):
        if name is None:
            super(InputComponent, self).__init__(uri, dev, "input")
        else:
            super(InputComponent, self).__init__(uri, dev, name)
    
    def click(self, pos, **kwargs):
        raise NotImplementedError

    def swipe(self, p1, p2, **kwargs):
        raise NotImplementedError

    def pinch(self, *args, **kwargs):
        raise NotImplementedError

    def double_tap(self, pos, **kwargs):
        raise NotImplementedError
