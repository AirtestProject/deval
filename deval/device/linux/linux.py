# -*- coding: utf-8 -*-

from functools import wraps
from deval.device.device import BaseDevice
from deval.component.linux.linuxcomponent import *


class LinuxDevice(BaseDevice):

    def __init__(self, uri):
        super(LinuxDevice, self).__init__()
        self.addComponent(LinuxInputComponent(uri, self))
        self.addComponent(LinuxGetterComponent(uri, self))
        self.addComponent(LinuxKeyEventComponent(uri, self))
        self.addComponent(LinuxRuntimeComponent(uri, self))
        self.addComponent(LinuxScreenComponent(uri, self))

        self.uri = uri
        
    @property
    def uuid(self):
        return self.uri

    
