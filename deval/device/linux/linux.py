# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.linux.input import LinuxInputComponent
from deval.component.linux.network import LinuxNetworkComponent
from deval.component.linux.keyevent import LinuxKeyEventComponent
from deval.component.linux.runtime import LinuxRuntimeComponent
from deval.component.linux.screen import LinuxScreenComponent


class LinuxDevice(BaseDevice):

    def __init__(self, uri):
        super(LinuxDevice, self).__init__(uri)
        self.addComponent(LinuxInputComponent("input", self, uri))
        self.addComponent(LinuxNetworkComponent("network", self, uri))
        self.addComponent(LinuxKeyEventComponent("keyevent", self, uri))
        self.addComponent(LinuxRuntimeComponent("runtime", self, uri))
        self.addComponent(LinuxScreenComponent("screen", self, uri))
        
    @property
    def uuid(self):
        return self.uri
