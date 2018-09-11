# -*- coding: utf-8 -*-

import time
from mss import mss
from pywinauto import mouse
from pynput.mouse import Controller, Button
from deval.component.std.input import InputComponent
from deval.utils.win.winfuncs import get_app, get_rect, get_window, set_foreground_window
from deval.utils.win.winfuncs import Application, get_action_pos
from deval.utils.win.winfuncs import _check_platform_win


class WinInputComponent(InputComponent):
    
    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        try:
            self.app = self.dev.app
            self.window = self.dev.window
        except AttributeError:
            self.dev.app = get_app(_check_platform_win(self.uri))
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.app = self.dev.app
            self.window = self.dev.window
        self.screen = mss()
        self.monitor = self.screen.monitors[0]  # 双屏的时候，self.monitor为整个双屏
        # 双屏的时候，self.singlemonitor
        self.singlemonitor = self.screen.monitors[1]
        # self.secondmonitor = self.screen.monitors[2]  # 双屏的时候，self.secondmonitor

    def click(self, pos, duration=0.05, button='left'):
        set_foreground_window(self.window)
        if button not in ("left", "right", "middle"):
            raise ValueError("Unknow button: " + button)

        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        pos = tuple(pos)
        coords = get_action_pos(self.window, pos)
        mouse.press(button=button, coords=coords)
        time.sleep(duration)
        mouse.release(button=button, coords=coords)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        set_foreground_window(self.window)

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
        # 设置坐标时相对于整个屏幕的坐标:
        x1 = x1 + self.monitor["left"]
        x2 = x2 + self.monitor["left"]
        y1 = y1 + self.monitor["top"]
        y2 = y2 + self.monitor["top"]
        # 双屏时，涉及到了移动的比例换算:
        if len(self.screen.monitors) > 2:
            ratio_x = (
                self.monitor["width"] + self.monitor["left"]) / self.singlemonitor["width"]
            ratio_y = (
                self.monitor["height"] + self.monitor["top"]) / self.singlemonitor["height"]
            x2 = int(x1 + (x2 - x1) * ratio_x)
            y2 = int(y1 + (y2 - y1) * ratio_y)
            p1 = (x1, y1)
            p2 = (x2, y2)

        from_x, from_y = get_action_pos(self.window, p1)
        to_x, to_y = get_action_pos(self.window, p2)

        m = Controller()
        interval = float(duration) / (steps + 1)
        m.position = (from_x, from_y)
        m.press(button)
        time.sleep(interval)
        for i in range(1, steps + 1):
            m.move(
                int((to_x - from_x) / steps),
                int((to_y - from_y) / steps)
            )
            time.sleep(interval)
        m.position = (x2, y2)
        time.sleep(interval)
        m.release(button)

    def double_tap(self, pos, button='left'):
        set_foreground_window(self.window)
        if button not in ("left", "right", "middle"):
            raise ValueError("Unknow button: " + button)

        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        pos = tuple(pos)
        coords = get_action_pos(self.window, pos)
        mouse.double_click(button=button, coords=coords)

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        if direction is "horizontal":
            raise ValueError(
                "Windows does not support horizontal scrolling currently")
        if direction is not 'vertical':
            raise ValueError(
                'Argument `direction` should be "vertical". Got {}'.format(repr(direction)))
        set_foreground_window(self.window)

        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        pos = tuple(pos)
        coords = get_action_pos(self.window, pos)
        interval = float(duration) / (abs(steps) + 1)
        if steps < 0:
            for i in range(0, abs(steps)):
                time.sleep(interval)
                mouse.scroll(coords=coords, wheel_dist=1)
        else:
            for i in range(0, abs(steps)):
                time.sleep(interval)
                mouse.scroll(coords=coords, wheel_dist=-1)
