# -*- coding: utf-8 -*-

from deval.device.device import BaseDevice
from deval.component.android.androidcomponent import AndroidAppComponent, AndroidNetworkComponent, AndroidInputComponent
from deval.component.android.androidcomponent import AndroidKeyEventComponent, AndroidRuntimeComponent, AndroidScreenComponent, AndroidStatueComponent
from deval.core.android.androidfuncs import AndroidProxy, _check_platform_android


class AndroidDevice(BaseDevice):
    
    def __init__(self, uri):
        super(AndroidDevice, self).__init__()

        kw = _check_platform_android(uri)
        self.androidproxy = AndroidProxy(**kw)

        self.addComponent(AndroidAppComponent(uri, self))
        self.addComponent(AndroidNetworkComponent(uri, self))
        self.addComponent(AndroidInputComponent(uri, self))
        self.addComponent(AndroidKeyEventComponent(uri, self))
        self.addComponent(AndroidRuntimeComponent(uri, self))
        self.addComponent(AndroidScreenComponent(uri, self))
        self.addComponent(AndroidStatueComponent(uri, self))

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
