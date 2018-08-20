# -*- coding: utf-8 -*-

import re
import warnings
from functools import wraps
from copy import copy
from deval.device.device import BaseDevice
from deval.component.android.androidcomponent import *
from deval.core.android.androidfuncs import _check_platform_android


class AndroidDevice(BaseDevice):
    
    def __init__(self, uri):
        super(AndroidDevice, self).__init__()

        kw = _check_platform_android(uri)
        self.proxy = AndroidProxy(**kw)

        self.addMethodInComponent("is_keyboard_shown", "status")
        self.addMethodInComponent("is_screenon", "status")
        self.addMethodInComponent("is_locked", "status")
        self.addMethodInComponent("unlock", "status")
        self.addMethodInComponent("get_top_activity_name", "getter")
        self.addMethodInComponent("get_top_activity_name_and_pid", "getter")

        self.addComponent(AndroidAppComponent(uri, self))
        self.addComponent(AndroidGetterComponent(uri, self))
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
