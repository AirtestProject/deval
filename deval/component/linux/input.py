# -*- coding: utf-8 -*-

import time
from pywinauto import mouse
from deval.component.std.inputcomponent import InputComponent
from mss import mss
from pynput.mouse import Controller, Button


class LinuxInputComponent(InputComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxInputComponent, self).__init__(uri, dev, name)
        self.screen = mss()
        self.monitor = self.screen.monitors[0]
        self.singlemonitor = self.screen.monitors[1]

    def click(self, pos, duration=0.05, button='left'):
        if button not in ("left", "right", "middle"):
            raise ValueError("Unknow button: " + button)

        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        mouse.press(button=button, coords=pos)
        time.sleep(duration)
        mouse.release(button=button, coords=pos)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        if button is "middle":
            button = Button.middle
        elif button is "right":
            button = Button.right
        elif button is "left":
            button = Button.left
        else:
            raise ValueError("Unknow button: " + button)
        x1, y1 = p1
        x2, y2 = p2
        x1 = x1 + self.monitor["left"]
        x2 = x2 + self.monitor["left"]
        y1 = y1 + self.monitor["top"]
        y2 = y2 + self.monitor["top"]
        ratio_x = self.monitor["width"] / self.singlemonitor["width"]
        ratio_y = self.monitor["height"] / self.singlemonitor["height"]
        x2 = x1 + (x2 - x1) / ratio_x
        y2 = y1 + (y2 - y1) / ratio_y
        m = Controller()
        interval = float(duration) / (steps + 1)
        m.position = (x1, y1)
        m.press(button)
        time.sleep(interval)
        for i in range(1, steps + 1):
            m.move(
                int((x2 - x1) / steps),
                int((y2 - y1) / steps)
            )
            time.sleep(interval)
        m.position = (x2, y2)
        time.sleep(interval)
        m.release(button)

    def double_tap(self, pos, button='left'):
        if button not in ("left", "right", "middle"):
            raise ValueError("Unknow button: " + button)
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        mouse.double_click(button=button, coords=pos)
