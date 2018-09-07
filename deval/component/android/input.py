# -*- coding: utf-8 -*-

import time
from deval.component.std.inputcomponent import InputComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android
from deval.utils.parse import parse_uri


class AndroidMiniTouchInputComponent(InputComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidMiniTouchInputComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def click(self, pos, duration=0.05, button='left'):
        pos = self.proxy._touch_point_by_orientation(pos)
        self.proxy.minitouch.touch(pos, duration=duration)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):

        p1 = self.proxy._touch_point_by_orientation(p1)
        p2 = self.proxy._touch_point_by_orientation(p2)
        if fingers == 1:
            self.proxy.minitouch.swipe(p1, p2, duration=duration, steps=steps)
        elif fingers == 2:
            self.proxy.minitouch.two_finger_swipe(
                p1, p2, duration=duration, steps=steps)
        else:
            raise Exception("param fingers should be 1 or 2")

    def pinch(self, *args, **kwargs):
        return self.proxy.minitouch.pinch(*args, **kwargs)

    def double_tap(self, pos, button='left'):
        duration = 0.05
        pos = self.proxy._touch_point_by_orientation(pos)
        self.proxy.minitouch.touch(pos, duration=duration)

        time.sleep(0.05)

        pos = self.proxy._touch_point_by_orientation(pos)
        self.proxy.minitouch.touch(pos, duration=duration)

    def is_keyboard_shown(self):
        return self.proxy.adb.is_keyboard_shown()


class AndroidADBTouchInputComponent(InputComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidADBTouchInputComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def click(self, pos, duration=0.05, button='left'):
        self.proxy.adb.touch(pos)

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        duration *= 1000  # adb的swipe操作时间是以毫秒为单位的。
        self.proxy.adb.swipe(p1, p2, duration=duration)

    def pinch(self, *args, **kwargs):
        return self.proxy.minitouch.pinch(*args, **kwargs)

    def double_tap(self, pos, button='left'):
        self.proxy.adb.touch(pos)
        time.sleep(0.05)
        self.proxy.adb.touch(pos)

    def is_keyboard_shown(self):
        return self.proxy.adb.is_keyboard_shown()
