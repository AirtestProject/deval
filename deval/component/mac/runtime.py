# -*- coding: utf-8 -*-


import subprocess
from deval.component.std.runtimecomponent import RuntimeComponent


class MacRuntimeComponent(RuntimeComponent):
    def __init__(self, uri, dev, name=None):
        super(MacRuntimeComponent, self).__init__(uri, dev, name)

    def shell(self, cmd):
        return subprocess.check_output(cmd, shell=True)
