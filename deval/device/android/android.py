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
    
    # StatusComponent
    def is_keyboard_shown(self, *args, **kwargs):
        if "status" in self.ComponentList:
            return self.ComponentList["status"].is_keyboard_shown(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform is_keyboard_shown function")

    def is_screenon(self, *args, **kwargs):
        if "status" in self.ComponentList:
            return self.ComponentList["status"].is_screenon(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform is_screenon function")

    def is_locked(self, *args, **kwargs):
        if "status" in self.ComponentList:
            return self.ComponentList["status"].is_locked(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform is_locked function")

    def unlock(self, *args, **kwargs):
        if "status" in self.ComponentList:
            return self.ComponentList["status"].unlock(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform unlock function")
    # StatusComponent

