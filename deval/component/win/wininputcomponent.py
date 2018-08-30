# -*- coding: utf-8 -*-

import time
from mss import mss
from pywinauto import mouse
from deval.component.std.inputcomponent import InputComponent
from deval.utils.win.winfuncs import get_app, get_rect, get_window, set_foreground_window
from deval.utils.win.winfuncs import Application, get_action_pos
from deval.utils.win.winfuncs import _check_platform_win


class WinInputComponent(InputComponent):
    def __init__(self, uri, dev, name=None):
        super(WinInputComponent, self).__init__(uri, dev, name)

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
        self.singlemonitor = self.screen.monitors[1]  # 双屏的时候，self.singlemonitor
        # self.secondmonitor = self.screen.monitors[2]  # 双屏的时候，self.secondmonitor
        
    def click(self, pos, **kwargs):
        set_foreground_window(self.window)
        duration = kwargs.get("duration", 0.01)
        right_click = kwargs.get("right_click", False)
        button = "right" if right_click else "left"
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        pos = tuple(pos)
        coords = get_action_pos(self.window, pos)
        mouse.press(button=button, coords=coords)
        time.sleep(duration)
        mouse.release(button=button, coords=coords)

    def swipe(self, p1, p2, **kwargs):
        set_foreground_window(self.window)

        duration = kwargs.get("duration", 0.8)
        steps = kwargs.get("steps", 5)

        x1, y1 = p1
        x2, y2 = p2
        # 设置坐标时相对于整个屏幕的坐标:
        x1 = x1 + self.monitor["left"]
        x2 = x2 + self.monitor["left"]
        y1 = y1 + self.monitor["top"]
        y2 = y2 + self.monitor["top"]
        # 双屏时，涉及到了移动的比例换算:
        if len(self.screen.monitors) > 2:
            ratio_x = (self.monitor["width"] + self.monitor["left"]) / self.singlemonitor["width"]
            ratio_y = (self.monitor["height"] + self.monitor["top"]) / self.singlemonitor["height"]
            x2 = int(x1 + (x2 - x1) * ratio_x)
            y2 = int(y1 + (y2 - y1) * ratio_y)
            p1 = (x1, y1)
            p2 = (x2, y2)

        from_x, from_y = get_action_pos(self.window, p1)
        to_x, to_y = get_action_pos(self.window, p2)
        interval = float(duration) / (steps + 1)
        mouse.press(coords=(from_x, from_y))
        time.sleep(interval)
        for i in range(1, steps):
            mouse.move(coords=(
                int(from_x + (to_x - from_x) * i / steps),
                int(from_y + (to_y - from_y) * i / steps),
            ))
            time.sleep(interval)
        for i in range(10):
            mouse.move(coords=(to_x, to_y))
        time.sleep(interval)
        mouse.release(coords=(to_x, to_y))

    def double_tap(self, pos, **kwargs):
        set_foreground_window(self.window)
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        pos = tuple(pos)
        coords = get_action_pos(self.window, pos)
        mouse.double_click(coords=coords)

    def scroll(self, pos, **kwargs):
        set_foreground_window(self.window)

        duration = kwargs.get("duration", 2)
        steps = kwargs.get("steps", -1)

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
