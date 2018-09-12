# -*- coding: utf-8 -*-

import time
from deval.component.std.input import InputComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri
from deval.utils.android.rotation import XYTransformer
from deval.utils.android.minitouch import Minitouch


class AndroidMiniTouchInputComponent(InputComponent):

    def __init__(self, name, dev):
        self.name = name
        self.device = dev
        self.adb = self.device.adb
        self.minitouch = Minitouch(self.device)

    def click(self, pos, duration=0.05, button='left'):
        pos = self._touch_point_by_orientation(pos)
        self.minitouch.touch(pos, duration=duration)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):

        p1 = self._touch_point_by_orientation(p1)
        p2 = self._touch_point_by_orientation(p2)
        if fingers == 1:
            self.minitouch.swipe(p1, p2, duration=duration, steps=steps)
        elif fingers == 2:
            self.minitouch.two_finger_swipe(
                p1, p2, duration=duration, steps=steps)
        else:
            raise Exception("param fingers should be 1 or 2")

    def pinch(self, *args, **kwargs):
        return self.minitouch.pinch(*args, **kwargs)

    def double_tap(self, pos, button='left'):
        duration = 0.05
        pos = self._touch_point_by_orientation(pos)
        self.minitouch.touch(pos, duration=duration)

        time.sleep(0.05)

        pos = self._touch_point_by_orientation(pos)
        self.minitouch.touch(pos, duration=duration)

    def is_keyboard_shown(self):
        return self.adb.is_keyboard_shown()

    def _touch_point_by_orientation(self, tuple_xy):
        x, y = tuple_xy
        x, y = XYTransformer.up_2_ori(
            (x, y),
            (self.device.screen_component.display_info["width"],
             self.device.screen_component.display_info["height"]),
            self.device.screen_component.display_info["orientation"]
        )
        return x, y

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


class AndroidADBTouchInputComponent(InputComponent):

    def __init__(self, name, dev):
        self.name = name
        self.adb = dev.adb

    def click(self, pos, duration=0.05, button='left'):
        self.adb.touch(pos)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        duration *= 1000  # adb的swipe操作时间是以毫秒为单位的。
        self.adb.swipe(p1, p2, duration=duration)

    def double_tap(self, pos, button='left'):
        self.adb.touch(pos)
        time.sleep(0.05)
        self.adb.touch(pos)

    def is_keyboard_shown(self):
        return self.adb.is_keyboard_shown()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
