# -*- coding: utf-8 -*-


import subprocess
from deval.component.std.runtime import RuntimeComponent
from deval.utils.linux.linuxfuncs import _check_platform_linux


class LinuxRuntimeComponent(RuntimeComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

    def shell(self, cmd):
        return subprocess.check_output(cmd, shell=True)
