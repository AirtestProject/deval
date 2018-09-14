# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.linux.input import LinuxInputComponent
from deval.component.linux.network import LinuxNetworkComponent
from deval.component.linux.keyevent import LinuxKeyEventComponent
from deval.component.linux.runtime import LinuxRuntimeComponent
from deval.component.linux.screen import LinuxScreenComponent
from deval.utils.parse import parse_uri


class LinuxDevice(DeviceBase):

    def __init__(self):
        super(LinuxDevice, self).__init__(None)
        self.add_component(LinuxInputComponent("input"))
        self.add_component(LinuxNetworkComponent("network"))
        self.add_component(LinuxKeyEventComponent("keyevent"))
        self.add_component(LinuxRuntimeComponent("runtime"))
        self.add_component(LinuxScreenComponent("screen"))
