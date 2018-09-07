# -*- coding: utf-8 -*-

import time
from pynput.keyboard import Controller
from deval.component.std.keyeventcomponent import KeyEventComponent


class MacKeyEventComponent(KeyEventComponent):
    def __init__(self, uri, dev, name=None):
        super(MacKeyEventComponent, self).__init__(uri, dev, name)
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
