# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.mac.input import MacInputComponent
from deval.component.mac.network import MacNetworkComponent
from deval.component.mac.keyevent import MacKeyEventComponent
from deval.component.mac.runtime import MacRuntimeComponent
from deval.component.mac.screen import MacScreenComponent
from deval.component.mac.app import MacAppComponent
from deval.utils.parse import parse_uri


def check_platform_mac(uri, platform="mac"):
    """
    Check the uri and return a dictionary containing the various parameters contained in the uri.

    Parameters:
        uri - an URI where to connect to device, e.g. `mac:///`

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
        params.pop("uuid")
    return params


class MacDevice(DeviceBase):

    def __init__(self, uri):
        super(MacDevice, self).__init__(uri)
        self.uri = uri
        self.add_component(MacInputComponent("input"))
        self.add_component(MacNetworkComponent("network"))
        self.add_component(MacKeyEventComponent("keyevent"))
        self.add_component(MacRuntimeComponent("runtime"))
        self.add_component(MacScreenComponent("screen"))
        self.add_component(MacAppComponent("app"))

    @property
    def uuid(self):
        return self.uri
