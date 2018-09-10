# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class RuntimeComponent(Component):
    def __init__(self, uri, dev=None, name="runtime"):
        if name is None:
            super(RuntimeComponent, self).__init__(uri, dev, "runtime")
        else:
            super(RuntimeComponent, self).__init__(uri, dev, name)

    def shell(self, cmd):
        """
        Enter console command

        Parameters:
            cmd - the command.
        """
        raise NotImplementedError

    def kill(self, pid):
        """
        Kill a program based on the process ID

        Parameters:
            pid - the pid.
        """
        raise NotImplementedError
