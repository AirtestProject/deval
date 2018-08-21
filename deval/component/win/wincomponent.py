# -*- coding: utf-8 -*-

import time
import subprocess
import socket
from mss import mss
from pywinauto import mouse, keyboard
from deval.component.component import InputComponent, KeyEventComponent, RuntimeComponent
from deval.component.component import AppComponent, ScreenComponent, NetworkComponent, Component
from deval.core.win.winfuncs import get_app, get_rect, get_window, set_foreground_window
from deval.core.win.winfuncs import Application, screenshot, get_action_pos
from deval.core.win.winfuncs import _check_platform_win
from deval.utils.cv import crop_image, imwrite


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
                mouse.scroll(coords=coords, wheel_dist=-1)
        else:
            for i in range(0, abs(steps)):
                time.sleep(interval)
                mouse.scroll(coords=coords, wheel_dist=1)
    

class WinKeyEventComponent(KeyEventComponent):
    def __init__(self, uri, dev, name=None):
        super(WinKeyEventComponent, self).__init__(uri, dev, name)
   
    def keyevent(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)

    def text(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)


class WinRuntimeComponent(RuntimeComponent):
    def __init__(self, uri, dev, name=None):
        super(WinRuntimeComponent, self).__init__(uri, dev, name)
        try:
            self.window = self.dev.window
        except AttributeError:
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.window = self.dev.window
   
    def shell(self, cmd, **kwargs):
        return subprocess.check_output(cmd, shell=True)

    def kill(self, pid, **kwargs):
        Application().connect(process=pid).kill()

    def get_title(self, **kwargs):
        if self.window:
            return self.window.texts()


class WinAppComponent(AppComponent):
    def __init__(self, uri, dev, name=None):
        super(WinAppComponent, self).__init__(uri, dev, name)
        try:
            self.app = self.dev.app
        except AttributeError:
            self.dev.app = get_app(_check_platform_win(self.uri))
            self.app = self.dev.app

    def start_app(self, path, **kwargs):
        return Application().start(path)
    
    def stop_app(self, **kwargs):
        if self.app:
            self.app.kill()


class WinScreenComponent(ScreenComponent):
    
    def __init__(self, uri, dev, name=None):
        super(WinScreenComponent, self).__init__(uri, dev, name)
        try:
            self.app = self.dev.app
            self.window = self.dev.window
        except AttributeError:
            self.dev.app = get_app(_check_platform_win(self.uri))
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.app = self.dev.app
            self.window = self.dev.window
        self.handle = None
        h = _check_platform_win(self.uri).get("handle")
        if h:
            self.handle = int(h)
    
    def snapshot(self, filename="tmp.png", **kwargs):
        if not filename:
            filename = "tmp.png"
        
        if self.handle:
            screen = screenshot(filename, self.handle)
        else:
            screen = screenshot(filename)
            if self.app:
                rect = get_rect(self.window)
                screen = crop_image(screen, [rect.left, rect.top, rect.right, rect.bottom])
        if not screen.any():
            if self.app:
                rect = get_rect(self.window)
                screen = crop_image(screenshot(filename), [rect.left, rect.top, rect.right, rect.bottom])
        if filename:
            imwrite(filename, screen)
        return screen

    def move(self, pos, **kwargs):
        if self.window:
            self.window.MoveWindow(x=pos[0], y=pos[1])


class WinNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(WinNetworkComponent, self).__init__(uri, dev, name)
        try:
            self.window = self.dev.window
        except AttributeError:
            self.dev.window = get_window(_check_platform_win(self.uri))
            self.window = self.dev.window

    def get_ip_address(self, **kwargs):
        return socket.gethostbyname(socket.gethostname())
