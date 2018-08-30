# -*- coding: utf-8 -*-

import subprocess
from deval.component.std.runtimecomponent import RuntimeComponent
from deval.utils.win.winfuncs import get_window, Application
from deval.utils.win.winfuncs import _check_platform_win


class WinRuntimeComponent(RuntimeComponent):
    def __init__(self, uri, dev, name=None):
        super(WinRuntimeComponent, self).__init__(uri, dev, name)
        try:
            self.window = self.dev.window
        except AttributeError:
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.window = self.dev.window
   
    def shell(self, cmd, **kwargs):
        return subprocess.check_output(cmd, shell=True)

    def kill(self, pid, **kwargs):
        Application().connect(process=pid).kill()
