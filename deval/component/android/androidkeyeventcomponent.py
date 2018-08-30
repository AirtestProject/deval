# -*- coding: utf-8 -*-

from deval.component.std.keyeventcomponent import KeyEventComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android
from deval.utils.parse import parse_uri


class AndroidYOSEMITEIMEKeyEventComponent(KeyEventComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidYOSEMITEIMEKeyEventComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def keyevent(self, keyname, **kwargs):
        return self.proxy.adb.keyevent(keyname)

    def text(self, text, enter=True, **kwargs):
    
        self.proxy.yosemite_ime.text(text)
        
        # 游戏输入时，输入有效内容后点击Enter确认，如不需要，enter置为False即可。
        if enter:
            self.proxy.adb.shell(["input", "keyevent", "ENTER"])

    def wake(self, **kwargs):
        self.proxy.adb.keyevent("HOME")
        self.proxy.recorder.install_or_upgrade()  # 暂时Yosemite只用了ime
        self.proxy.adb.shell(['am', 'start', '-a', 'com.netease.nie.yosemite.ACTION_IDENTIFY'])
        self.proxy.adb.keyevent("HOME")
    
    def home(self, **kwargs):
        self.proxy.adb.keyevent("HOME")


class AndroidADBIMEKeyEventComponent(KeyEventComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidADBIMEKeyEventComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def keyevent(self, keyname, **kwargs):
        return self.proxy.adb.keyevent(keyname)

    def text(self, text, enter=True, **kwargs):
        self.proxy.adb.shell(["input", "text", text])

        # 游戏输入时，输入有效内容后点击Enter确认，如不需要，enter置为False即可。
        if enter:
            self.proxy.adb.shell(["input", "keyevent", "ENTER"])

    def wake(self, **kwargs):
        self.proxy.adb.keyevent("HOME")
        self.proxy.recorder.install_or_upgrade()  # 暂时Yosemite只用了ime
        self.proxy.adb.shell(['am', 'start', '-a', 'com.netease.nie.yosemite.ACTION_IDENTIFY'])
        self.proxy.adb.keyevent("HOME")
    
    def home(self, **kwargs):
        self.proxy.adb.keyevent("HOME")
