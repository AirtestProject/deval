# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.mac.input import MacInputComponent
from deval.component.mac.network import MacNetworkComponent
from deval.component.mac.keyevent import MacKeyEventComponent
from deval.component.mac.runtime import MacRuntimeComponent
from deval.component.mac.screen import MacScreenComponent
from deval.component.mac.app import MacAppComponent
from deval.utils.parse import parse_uri


class MacDevice(DeviceBase):

    def __init__(self):
        super(MacDevice, self).__init__(None)
        self.add_component(MacInputComponent("input"))
        self.add_component(MacNetworkComponent("network"))
        self.add_component(MacKeyEventComponent("keyevent"))
        self.add_component(MacRuntimeComponent("runtime"))
        self.add_component(MacScreenComponent("screen"))
        self.add_component(MacAppComponent("app"))
