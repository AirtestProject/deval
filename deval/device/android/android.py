# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.android.app import AndroidAppComponent
from deval.component.android.network import AndroidNetworkComponent
from deval.component.android.runtime import AndroidRuntimeComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android, TOUCH_METHOD, IME_METHOD, CAP_METHOD


class AndroidDevice(BaseDevice):

    def __init__(self, uri):
        super(AndroidDevice, self).__init__()

        kw = _check_platform_android(uri)
        self.proxy = AndroidProxy(**kw)
        self.uri = uri
        self.addComponent(AndroidAppComponent(uri, self))
        self.addComponent(AndroidNetworkComponent(uri, self))
        self.addComponent(AndroidRuntimeComponent(uri, self))

        if kw.get("touch_method") == TOUCH_METHOD.ADBTOUCH:
            from deval.component.android.input import AndroidADBTouchInputComponent
            self.addComponent(AndroidADBTouchInputComponent(uri, self))
        else:
            from deval.component.android.input import AndroidMiniTouchInputComponent
            self.addComponent(AndroidMiniTouchInputComponent(uri, self))

        if kw.get("ime_method") == IME_METHOD.ADBIME:
            from deval.component.android.keyevent import AndroidADBIMEKeyEventComponent
            self.addComponent(AndroidADBIMEKeyEventComponent(uri, self))
        else:
            from deval.component.android.keyevent import AndroidYOSEMITEIMEKeyEventComponent
            self.addComponent(AndroidYOSEMITEIMEKeyEventComponent(uri, self))

        if kw.get("cap_method") == CAP_METHOD.MINICAP_STREAM:
            from deval.component.android.screen import AndroidMiniCapStreamScreenComponent
            self.addComponent(AndroidMiniCapStreamScreenComponent(uri, self))
        elif kw.get("cap_method") == CAP_METHOD.MINICAP:
            from deval.component.android.screen import AndroidMiniCapScreenComponent
            self.addComponent(AndroidMiniCapScreenComponent(uri, self))
        elif kw.get("cap_method") == CAP_METHOD.JAVACAP:
            from deval.component.android.screen import AndroidJAVACapScreenComponent
            self.addComponent(AndroidJAVACapScreenComponent(uri, self))
        else:
            from deval.component.android.screen import AndroidADBScreenComponent
            self.addComponent(AndroidADBScreenComponent(uri, self))

    @property
    def uuid(self):
        return self.uri

    @property
    def adb(self):
        try:
            return self.proxy.adb
        except AttributeError:
            kw = _check_platform_android(self.uri)
            self.proxy = AndroidProxy(**kw)
            return self.proxy.adb
