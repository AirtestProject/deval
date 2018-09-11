# -*- coding: utf-8 -*-

from deval.utils.android.adb import ADB
from deval.device.std.device import BaseDevice
from deval.component.android.app import AndroidAppComponent
from deval.component.android.network import AndroidNetworkComponent
from deval.component.android.runtime import AndroidRuntimeComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.android.constant import CAP_METHOD, TOUCH_METHOD, IME_METHOD, ORI_METHOD


class AndroidDevice(BaseDevice):

    def __init__(self, uri):
        super(AndroidDevice, self).__init__(uri)
   
        self.kw = _check_platform_android(uri)
        self.ime_method = self.kw.get("ime_method") or IME_METHOD.YOSEMITEIME
        self.touch_method = self.kw.get("touch_method") or TOUCH_METHOD.MINITOUCH
        self.cap_method = self.kw.get("cap_method") or CAP_METHOD.MINICAP_STREAM
        self.serialno = self.kw.get("serialno") or self.get_default_device()
        self.adb = ADB(self.uuid, server_addr=self.kw.get("host"))
        
        self.addComponent(AndroidAppComponent("app", self, uri))
        self.addComponent(AndroidNetworkComponent("network", self, uri))
        self.addComponent(AndroidRuntimeComponent("runtime", self, uri))

        if self.cap_method.upper() == CAP_METHOD.MINICAP_STREAM:
            from deval.component.android.screen import AndroidMiniCapStreamScreenComponent
            self.addComponent(AndroidMiniCapStreamScreenComponent("screen", self, uri))
        elif self.cap_method.upper() == CAP_METHOD.MINICAP:
            from deval.component.android.screen import AndroidMiniCapScreenComponent
            self.addComponent(AndroidMiniCapScreenComponent("screen", self, uri))
        elif self.cap_method.upper() == CAP_METHOD.JAVACAP:
            from deval.component.android.screen import AndroidJAVACapScreenComponent
            self.addComponent(AndroidJAVACapScreenComponent("screen", self, uri))
        else:
            from deval.component.android.screen import AndroidADBScreenComponent
            self.addComponent(AndroidADBScreenComponent("screen", self, uri))

        if self.touch_method.upper() == TOUCH_METHOD.ADBTOUCH:
            from deval.component.android.input import AndroidADBTouchInputComponent
            self.addComponent(AndroidADBTouchInputComponent("input", self, uri))
        else:
            from deval.component.android.input import AndroidMiniTouchInputComponent
            self.addComponent(AndroidMiniTouchInputComponent("input", self, uri))

        if self.ime_method.upper() == IME_METHOD.ADBIME:
            from deval.component.android.keyevent import AndroidADBIMEKeyEventComponent
            self.addComponent(AndroidADBIMEKeyEventComponent("keyevent", self, uri))
        else:
            from deval.component.android.keyevent import AndroidYOSEMITEIMEKeyEventComponent
            self.addComponent(AndroidYOSEMITEIMEKeyEventComponent("keyevent", self, uri))

    @property
    def uuid(self):
        return self.serialno

    def get_default_device(self):
        """
        Get local default device when no serailno

        Returns:
            local device serialno

        """
        if not ADB().devices(state="device"):
            raise IndexError("ADB devices not found")
        return ADB().devices(state="device")[0][0]
