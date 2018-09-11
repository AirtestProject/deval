# -*- coding: utf-8 -*-

from deval.component.std.keyevent import KeyEventComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri
from deval.utils.android.recorder import Recorder
from deval.utils.android.ime import YosemiteIme


class AndroidYOSEMITEIMEKeyEventComponent(KeyEventComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
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


class AndroidADBIMEKeyEventComponent(KeyEventComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
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
