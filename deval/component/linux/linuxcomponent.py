# -*- coding: utf-8 -*-

import time
import subprocess
import socket
import pyautogui as inputs
from pywinauto import keyboard
from Xlib import display, X
from PIL import Image
from deval.component.component import InputComponent, KeyEventComponent, RuntimeComponent
from deval.component.component import AppComponent, ScreenComponent, NetworkComponent, Component
from deval.core.linux.linuxfuncs import _check_platform_linux
from deval.utils.cv import imwrite
from deval.utils.cv import pil_2_cv2


class LinuxInputComponent(InputComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxInputComponent, self).__init__(uri, dev, name)
        
    def click(self, pos, **kwargs):
        right_click = kwargs.get("right_click", False)
        button = "right" if right_click else "left"
        inputs.click(pos[0], pos[1], button=button)

    def swipe(self, p1, p2, **kwargs):
        duration = kwargs.get("duration", 0.8)
        from_x, from_y = p1
        to_x, to_y = p2
        inputs.moveTo(from_x, from_y)
        inputs.dragTo(to_x, to_y, duration=duration)

    def double_tap(self, pos, **kwargs):
        inputs.click(pos[0], pos[1], clicks=2, interval=0.05)


class LinuxKeyEventComponent(KeyEventComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxKeyEventComponent, self).__init__(uri, dev, name)
   
    def keyevent(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)

    def text(self, keyname, **kwargs):
        keyboard.SendKeys(keyname)


class LinuxRuntimeComponent(RuntimeComponent):
    def __init__(self, uri, dev, name=None):
        super(LinuxRuntimeComponent, self).__init__(uri, dev, name)
   
    def shell(self, cmd, **kwargs):
        return subprocess.check_output(cmd, shell=True)


class LinuxScreenComponent(ScreenComponent):
    
    def __init__(self, uri, dev, name=None):
        super(LinuxScreenComponent, self).__init__(uri, dev, name)
    
    def snapshot(self, filename="tmp.png", **kwargs):
        w, h = self.get_current_resolution()
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(0, 0, w, h, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
        image = pil_2_cv2(image)
        if filename:
            imwrite(filename, image)
        return image

    def get_current_resolution(self, **kwargs):
        d = display.Display()
        screen = d.screen()
        w, h = (screen["width_in_pixels"], screen["height_in_pixels"])
        return w, h


class LinuxNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(LinuxNetworkComponent, self).__init__(uri, dev, name)

    def get_ip_address(self, **kwargs):
        return socket.gethostbyname(socket.gethostname())
