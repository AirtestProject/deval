# -*- coding: utf-8 -*-


import pyautogui as inputs
from deval.component.std.inputcomponent import InputComponent


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
