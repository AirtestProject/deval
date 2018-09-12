# -*- coding: utf-8 -*-


import subprocess
from deval.component.std.runtime import RuntimeComponent
from deval.utils.linux.linuxfuncs import _check_platform_linux


class LinuxRuntimeComponent(RuntimeComponent):

    def __init__(self, name):
        self.name = name

    def shell(self, cmd):
        return subprocess.check_output(cmd, shell=True)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
