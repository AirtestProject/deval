# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class KeyEventComponent(Component):
    def __init__(self, uri, dev=None, name="keyevent"):
        if name is None:
            super(KeyEventComponent, self).__init__(uri, dev, "keyevent")
        else:
            super(KeyEventComponent, self).__init__(uri, dev, name)
    
    def keyevent(self, keyname, **kwargs):
        raise NotImplementedError

    def text(self, text, **kwargs):
        raise NotImplementedError
