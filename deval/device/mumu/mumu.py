# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.android.app import AndroidAppComponent
from deval.component.android.screen import AndroidADBScreenComponent
from deval.component.android.input import AndroidADBTouchInputComponent
from deval.component.win.input import WinInputComponent
from deval.component.win.screen import WinScreenComponent
from deval.utils.parse import parse_uri
from deval.component.android.utils.adb import ADB
from deval.component.win.utils.winfuncs import check_platform_win, get_app, get_window

# use parse_uri to parse your uri


def check_platform_mumu(uri, platform="mumu"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    if "uuid" in params:
        params["serialno"] = params["uuid"]
        params.pop("uuid")
    params.pop("platform")
    return params


class MumuDevice(DeviceBase):

    def __init__(self, uri):
        super(MumuDevice, self).__init__(uri)
        # First you have to connect to your Android emulator window in windows platform
        winuri = "windows:///657890"

        # Initialize the parameters required to operate Android Device
        self.kw = check_platform_mumu(uri)
        self.serialno = self.kw.get("serialno")
        self.adb = ADB(self.serialno, server_addr=self.kw.get("host"))

        # Initialize the parameters required to operate Windows Device
        self.app = get_app(check_platform_win(winuri))
        self.window = get_window(check_platform_win(winuri))
        self.handle = self.window.handle

        # Use android app component
        self.add_component(AndroidAppComponent("app", self))
        # Use android screen component as default
        self.add_component(AndroidADBScreenComponent("screen", self))
        # Use android input component as default
        self.add_component(AndroidADBTouchInputComponent("input", self))
        # add windows input component
        self.add_component(WinInputComponent("wininput", self, winuri))
        # add windows screen component
        self.add_component(WinScreenComponent("winscreen", self, winuri))
