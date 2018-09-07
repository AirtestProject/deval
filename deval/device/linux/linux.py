# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.linux.input import LinuxInputComponent
from deval.component.linux.network import LinuxNetworkComponent
from deval.component.linux.keyevent import LinuxKeyEventComponent
from deval.component.linux.runtime import LinuxRuntimeComponent
from deval.component.linux.screen import LinuxScreenComponent


class LinuxDevice(BaseDevice):

    def __init__(self, uri):
        super(LinuxDevice, self).__init__()
        self.addComponent(LinuxInputComponent(uri, self))
        self.addComponent(LinuxNetworkComponent(uri, self))
        self.addComponent(LinuxKeyEventComponent(uri, self))
        self.addComponent(LinuxRuntimeComponent(uri, self))
        self.addComponent(LinuxScreenComponent(uri, self))

        self.uri = uri

    @property
    def uuid(self):
        return self.uri
