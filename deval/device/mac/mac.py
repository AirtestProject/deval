# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.mac.input import MacInputComponent
from deval.component.mac.network import MacNetworkComponent
from deval.component.mac.keyevent import MacKeyEventComponent
from deval.component.mac.runtime import MacRuntimeComponent
from deval.component.mac.screen import MacScreenComponent
from deval.component.mac.app import MacAppComponent


class MacDevice(DeviceBase):

    def __init__(self, uri):
        super(MacDevice, self).__init__(uri)
        self.add_component(MacInputComponent("input"))
        self.add_component(MacNetworkComponent("network"))
        self.add_component(MacKeyEventComponent("keyevent"))
        self.add_component(MacRuntimeComponent("runtime"))
        self.add_component(MacScreenComponent("screen"))
        self.add_component(MacAppComponent("app"))

    @property
    def uuid(self):
        return self.uri
