# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.linux.input import LinuxInputComponent
from deval.component.linux.network import LinuxNetworkComponent
from deval.component.linux.keyevent import LinuxKeyEventComponent
from deval.component.linux.runtime import LinuxRuntimeComponent
from deval.component.linux.screen import LinuxScreenComponent


class LinuxDevice(DeviceBase):

    def __init__(self, uri):
        super(LinuxDevice, self).__init__(uri)
        self.add_component(LinuxInputComponent("input"))
        self.add_component(LinuxNetworkComponent("network"))
        self.add_component(LinuxKeyEventComponent("keyevent"))
        self.add_component(LinuxRuntimeComponent("runtime"))
        self.add_component(LinuxScreenComponent("screen"))
        
    @property
    def uuid(self):
        return self.uri
