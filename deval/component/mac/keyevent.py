# -*- coding: utf-8 -*-

import time
from pynput.keyboard import Controller
from deval.component.std.keyeventcomponent import KeyEventComponent


class MacKeyEventComponent(KeyEventComponent):
    
    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)
        self.keyboard = Controller()

    def keyevent(self, keyname):
        """
        Use pynput to simulate keyboard input

        Parameters:
            keyname - the keys
        """
        waittime = 0.05
        for c in keyname:
            self.keyboard.press(key=c)
            self.keyboard.release(key=c)
            time.sleep(waittime)

    def text(self, text, enter=False):
        """
        Use pynput to simulate keyboard input

        Parameters:
            keyname - the keys
        """
        waittime = 0.05
        for c in text:
            self.keyboard.press(key=c)
            self.keyboard.release(key=c)
            time.sleep(waittime)
