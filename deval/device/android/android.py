# -*- coding: utf-8 -*-

from deval.device.std.device import BaseDevice
from deval.component.android.androidappcomponent import AndroidAppComponent
from deval.component.android.androidnetworkcomponent import AndroidNetworkComponent
from deval.component.android.androidinputcomponent import AndroidMiniTouchInputComponent, AndroidADBTouchInputComponent
from deval.component.android.androidkeyeventcomponent import AndroidYOSEMITEIMEKeyEventComponent, AndroidADBIMEKeyEventComponent
from deval.component.android.androidruntimecomponent import AndroidRuntimeComponent
from deval.component.android.androidscreencomponent import AndroidScreenComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android, TOUCH_METHOD, IME_METHOD


class AndroidDevice(BaseDevice):
    
    def __init__(self, uri):
        super(AndroidDevice, self).__init__()

        kw = _check_platform_android(uri)
        self.androidproxy = AndroidProxy(**kw)

        self.addComponent(AndroidAppComponent(uri, self))
        self.addComponent(AndroidNetworkComponent(uri, self))
        if kw.get("touch_method") == TOUCH_METHOD.ADBTOUCH:
            self.addComponent(AndroidADBTouchInputComponent(uri, self))
        else:
            self.addComponent(AndroidMiniTouchInputComponent(uri, self))
        if kw.get("ime_method") == IME_METHOD.ADBIME:
            self.addComponent(AndroidADBIMEKeyEventComponent(uri, self))
        else:
            self.addComponent(AndroidYOSEMITEIMEKeyEventComponent(uri, self))
        self.addComponent(AndroidRuntimeComponent(uri, self))
        self.addComponent(AndroidScreenComponent(uri, self))

        self.uri = uri

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
