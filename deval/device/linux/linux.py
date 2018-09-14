# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.linux.input import LinuxInputComponent
from deval.component.linux.network import LinuxNetworkComponent
from deval.component.linux.keyevent import LinuxKeyEventComponent
from deval.component.linux.runtime import LinuxRuntimeComponent
from deval.component.linux.screen import LinuxScreenComponent
from deval.utils.parse import parse_uri


def check_platform_linux(uri, platform="linux"):
    """
    Check the uri and return a dictionary containing the various parameters contained in the uri.

    Parameters:
        uri - an URI where to connect to device, e.g. `linux:///`

    Returns:
        A dictionary containing the various parameters contained in the uri.

    Raises:
        RuntimeError - raise when the platform does not match the uri.
    """
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    params.pop("platform")
    if "uuid" in params:
        pid = params["uuid"]
        if pid != '':
            params["pid"] = int(pid)
        params.pop("uuid")
    return params


class LinuxDevice(DeviceBase):

    def __init__(self, uri):
        super(LinuxDevice, self).__init__(uri)
        self.uri = uri
        self.add_component(LinuxInputComponent("input"))
        self.add_component(LinuxNetworkComponent("network"))
        self.add_component(LinuxKeyEventComponent("keyevent"))
        self.add_component(LinuxRuntimeComponent("runtime"))
        self.add_component(LinuxScreenComponent("screen"))
        
    @property
    def uuid(self):
        return self.uri
