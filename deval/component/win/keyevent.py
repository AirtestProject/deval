# -*- coding: utf-8 -*-

import time
from pywinauto import keyboard
from deval.component.std.keyevent import KeyEventComponent
from pynput.keyboard import Controller


class WinKeyEventComponent(KeyEventComponent):
    
    def __init__(self, name, dev, uri):
        self.name = name
        self.keyboard = Controller()

    def keyevent(self, keyname):
        waittime = 0.05
        for c in keyname:
            self.keyboard.press(key=c)
            self.keyboard.release(key=c)
            time.sleep(waittime)

    def text(self, text, enter=True):
        waittime = 0.05
        for c in text:
            self.keyboard.press(key=c)
            self.keyboard.release(key=c)
            time.sleep(waittime)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
