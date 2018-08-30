# -*- coding: utf-8 -*-


import subprocess
from deval.component.std.runtimecomponent import RuntimeComponent
from deval.utils.linux.linuxfuncs import _check_platform_linux


class LinuxRuntimeComponent(RuntimeComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxRuntimeComponent, self).__init__(uri, dev, name)
   
    def shell(self, cmd, **kwargs):
        return subprocess.check_output(cmd, shell=True)
