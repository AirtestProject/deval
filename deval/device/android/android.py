# -*- coding: utf-8 -*-

from deval.component.android.utils.adb import ADB
from deval.device.std.device import DeviceBase
from deval.component.android.app import AndroidAppComponent
from deval.component.android.network import AndroidNetworkComponent
from deval.component.android.runtime import AndroidRuntimeComponent
from deval.component.android.utils.constant import CAP_METHOD, TOUCH_METHOD, IME_METHOD, ORI_METHOD
from deval.utils.parse import parse_uri


def check_platform_android(uri, platform="android"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    if "uuid" in params:
        params["serialno"] = params["uuid"]
        params.pop("uuid")
    params.pop("platform")
    return params


def get_android_default_device():
    """
    Get local default device when no serailno

    Returns:
        local device serialno

    """
    if not ADB().devices(state="device"):
        raise IndexError("ADB devices not found")
    return ADB().devices(state="device")[0][0]


class AndroidDevice(DeviceBase):

    def __init__(self, uri):
        super(AndroidDevice, self).__init__(uri)
   
        self.kw = check_platform_android(uri)
        self.ime_method = self.kw.get("ime_method") or IME_METHOD.YOSEMITEIME
        self.touch_method = self.kw.get("touch_method") or TOUCH_METHOD.MINITOUCH
        self.cap_method = self.kw.get("cap_method") or CAP_METHOD.MINICAP_STREAM
        self.serialno = self.kw.get("serialno") or get_android_default_device()
        self.adb = ADB(self.uuid, server_addr=self.kw.get("host"))
        
        self.add_component(AndroidAppComponent("app", self))
        self.add_component(AndroidNetworkComponent("network", self))
        self.add_component(AndroidRuntimeComponent("runtime", self))

        if self.cap_method.upper() == CAP_METHOD.MINICAP_STREAM:
            from deval.component.android.screen import AndroidMiniCapStreamScreenComponent
            self.add_component(AndroidMiniCapStreamScreenComponent("screen", self))
        elif self.cap_method.upper() == CAP_METHOD.MINICAP:
            from deval.component.android.screen import AndroidMiniCapScreenComponent
            self.add_component(AndroidMiniCapScreenComponent("screen", self))
        elif self.cap_method.upper() == CAP_METHOD.JAVACAP:
            from deval.component.android.screen import AndroidJAVACapScreenComponent
            self.add_component(AndroidJAVACapScreenComponent("screen", self))
        else:
            from deval.component.android.screen import AndroidADBScreenComponent
            self.add_component(AndroidADBScreenComponent("screen", self))

        if self.touch_method.upper() == TOUCH_METHOD.ADBTOUCH:
            from deval.component.android.input import AndroidADBTouchInputComponent
            self.add_component(AndroidADBTouchInputComponent("input", self))
        else:
            from deval.component.android.input import AndroidMiniTouchInputComponent
            self.add_component(AndroidMiniTouchInputComponent("input", self))

        if self.ime_method.upper() == IME_METHOD.ADBIME:
            from deval.component.android.keyevent import AndroidADBIMEKeyEventComponent
            self.add_component(AndroidADBIMEKeyEventComponent("keyevent", self))
        else:
            from deval.component.android.keyevent import AndroidYOSEMITEIMEKeyEventComponent
            self.add_component(AndroidYOSEMITEIMEKeyEventComponent("keyevent", self))

    @property
    def uuid(self):
        return self.serialno
