# -*- coding: utf-8 -*-

import subprocess
from deval.component.std.runtime import RuntimeComponent
from deval.utils.win.winfuncs import get_window, Application
from deval.utils.win.winfuncs import _check_platform_win


class WinRuntimeComponent(RuntimeComponent):
    
    def __init__(self, name, dev, uri):
        self.name = name

    def shell(self, cmd):
        return subprocess.check_output(cmd, shell=True)

    def kill(self, pid):
        Application().connect(process=pid).kill()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value