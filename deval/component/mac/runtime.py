# -*- coding: utf-8 -*-


import subprocess
from deval.component.std.runtimecomponent import RuntimeComponent


class MacRuntimeComponent(RuntimeComponent):
    
    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

    def shell(self, cmd):
        return subprocess.check_output(cmd, shell=True)
