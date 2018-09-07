# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class RuntimeComponent(Component):
    def __init__(self, uri, dev=None, name="runtime"):
        if name is None:
            super(RuntimeComponent, self).__init__(uri, dev, "runtime")
        else:
            super(RuntimeComponent, self).__init__(uri, dev, name)

    def shell(self, cmd):
        raise NotImplementedError

    def kill(self, pid):
        raise NotImplementedError
