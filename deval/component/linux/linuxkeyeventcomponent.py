# -*- coding: utf-8 -*-


from pywinauto import keyboard
from deval.component.std.keyeventcomponent import KeyEventComponent


class LinuxKeyEventComponent(KeyEventComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxKeyEventComponent, self).__init__(uri, dev, name)
   
    def keyevent(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)

    def text(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)
