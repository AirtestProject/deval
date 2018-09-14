# -*- coding: utf-8 -*-

from deval.component.std.keyevent import KeyEventComponent
from deval.component.android.utils.recorder import Recorder
from deval.component.android.utils.ime import YosemiteIme


class AndroidYOSEMITEIMEKeyEventComponent(KeyEventComponent):

    def __init__(self, name, dev):
        self._name = name
        self.adb = dev.adb
        self.recorder = Recorder(self.adb)
        self.yosemite_ime = YosemiteIme(self.adb)

    def keyevent(self, keyname):
        return self.adb.keyevent(keyname)

    def text(self, text, enter=True):
        self.yosemite_ime.text(text)
        # 游戏输入时，输入有效内容后点击Enter确认，如不需要，enter置为False即可。
        if enter:
            self.adb.shell(["input", "keyevent", "ENTER"])

    def wake(self):
        self.adb.keyevent("HOME")
        self.recorder.install_or_upgrade()  # 暂时Yosemite只用了ime
        self.adb.shell(
            ['am', 'start', '-a', 'com.netease.nie.yosemite.ACTION_IDENTIFY'])
        self.adb.keyevent("HOME")

    def home(self):
        self.adb.keyevent("HOME")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


class AndroidADBIMEKeyEventComponent(KeyEventComponent):

    def __init__(self, name, dev):
        self._name = name
        self.adb = dev.adb
        self.recorder = Recorder(self.adb)

    def keyevent(self, keyname):
        return self.adb.keyevent(keyname)

    def text(self, text, enter=True):
        self.adb.shell(["input", "text", text])

        # 游戏输入时，输入有效内容后点击Enter确认，如不需要，enter置为False即可。
        if enter:
            self.adb.shell(["input", "keyevent", "ENTER"])

    def wake(self):
        self.adb.keyevent("HOME")
        self.recorder.install_or_upgrade()  # 暂时Yosemite只用了ime
        self.adb.shell(
            ['am', 'start', '-a', 'com.netease.nie.yosemite.ACTION_IDENTIFY'])
        self.adb.keyevent("HOME")

    def home(self):
        self.adb.keyevent("HOME")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
