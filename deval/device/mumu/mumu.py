# -*- coding: utf-8 -*-

from deval.device.std.device import DeviceBase
from deval.component.android.app import AndroidAppComponent
from deval.component.android.screen import AndroidADBScreenComponent
from deval.component.android.input import AndroidADBTouchInputComponent
from deval.component.win.input import WinInputComponent
from deval.component.win.screen import WinScreenComponent
from deval.utils.parse import parse_uri
from deval.component.android.utils.adb import ADB
from deval.component.win.utils.winfuncs import get_app, get_window


class MumuDevice(DeviceBase):

    def __init__(self, uri):
        super(MumuDevice, self).__init__(uri)

        # Initialize the parameters required to operate Android Device
        self.kw = parse_uri(uri)
        self.serialno = self.kw.get("serialno")
        self.adb = ADB(self.serialno, server_addr=self.kw.get("host"))

        # Initialize the parameters required to operate Windows Device
        self.application = get_app(uri)
        self.window = get_window(uri)
        self.handle = self.window.handle

        # Use android app component
        self.add_component(AndroidAppComponent("app", self))
        # Use android screen component as default
        self.add_component(AndroidADBScreenComponent("screen", self))
        # Use android input component as default
        self.add_component(AndroidADBTouchInputComponent("input", self))
        # add windows input component
        self.add_component(WinInputComponent("wininput", self, uri))
        # add windows screen component
        self.add_component(WinScreenComponent("winscreen", self, uri))
