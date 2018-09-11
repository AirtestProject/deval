# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.mac.input import MacInputComponent
from deval.component.mac.network import MacNetworkComponent
from deval.component.mac.keyevent import MacKeyEventComponent
from deval.component.mac.runtime import MacRuntimeComponent
from deval.component.mac.screen import MacScreenComponent
from deval.component.mac.app import MacAppComponent


class MacDevice(BaseDevice):

    def __init__(self, uri):
        super(MacDevice, self).__init__(uri)
        self.addComponent(MacInputComponent("input", self, uri))
        self.addComponent(MacNetworkComponent("network", self, uri))
        self.addComponent(MacKeyEventComponent("keyevent", self, uri))
        self.addComponent(MacRuntimeComponent("runtime", self, uri))
        self.addComponent(MacScreenComponent("screen", self, uri))
        self.addComponent(MacAppComponent("app", self, uri))

    @property
    def uuid(self):
        return self.uri
