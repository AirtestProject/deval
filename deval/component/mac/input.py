# -*- coding: utf-8 -*-

import Quartz
import time
from mss import mss
from deval.component.std.inputcomponent import InputComponent


class MacInputComponent(InputComponent):
    def __init__(self, uri, dev, name=None):
        super(MacInputComponent, self).__init__(uri, dev, name)
        self.screen = mss()  # 双屏需要
        self.monitor = self.screen.monitors[0]
        self.singlemonitor = self.screen.monitors[1]

    def click(self, pos, duration=0.05, button='left'):
        pressID = [None, Quartz.kCGEventLeftMouseDown,
                   Quartz.kCGEventRightMouseDown, Quartz.kCGEventOtherMouseDown]
        releaseID = [None, Quartz.kCGEventLeftMouseUp,
                     Quartz.kCGEventRightMouseUp, Quartz.kCGEventOtherMouseUp]

        if button not in ("left", "right"):
            raise ValueError("Unknow button: " + button)
        if button == 'left':
            button = 1
        elif button == 'right':
            button = 2
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        theEvent = Quartz.CGEventCreateMouseEvent(
            None, pressID[button], (pos[0], pos[1]), button - 1)  # 按下消息
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)  # 发送消息
        Quartz.CGEventSetType(theEvent, releaseID[button])  # 抬起消息
        time.sleep(duration)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)  # 发送消息

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        pressID = [None, Quartz.kCGEventLeftMouseDown,
                   Quartz.kCGEventRightMouseDown, Quartz.kCGEventOtherMouseDown]
        releaseID = [None, Quartz.kCGEventLeftMouseUp,
                     Quartz.kCGEventRightMouseUp, Quartz.kCGEventOtherMouseUp]
        if button is "middle":
            button = 3
        elif button is "right":
            button = 2
        elif button is "left":
            button = 1
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

        sx = abs(x1 - x2)
        sy = abs(y1 - y2)
        stepx = sx / (duration * 10.0)  # 将滑动距离分割，实现平滑的拖动
        stepy = sy / (duration * 10.0)
        moveevent = Quartz.CGEventCreateMouseEvent(
            None, Quartz.kCGEventMouseMoved, (x1, y1), 0)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, moveevent)
        pressevent = Quartz.CGEventCreateMouseEvent(
            None, pressID[button], (x1, y1), button - 1)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, pressevent)
        duration = int(duration * 10.0)
        for i in range(duration + 1):
            drag = Quartz.CGEventCreateMouseEvent(
                None, Quartz.kCGEventLeftMouseDragged, (x1 + stepx * i, y1 + stepy * i), 0)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, drag)
            time.sleep(0.1)
        event = Quartz.CGEventCreateMouseEvent(
            None, releaseID[button], (x2, y2), button - 1)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

    def double_tap(self, pos, button='left'):
        pressID = [None, Quartz.kCGEventLeftMouseDown,
                   Quartz.kCGEventRightMouseDown, Quartz.kCGEventOtherMouseDown]
        releaseID = [None, Quartz.kCGEventLeftMouseUp,
                     Quartz.kCGEventRightMouseUp, Quartz.kCGEventOtherMouseUp]
        if button not in ("left", "right"):
            raise ValueError("Unknow button: " + button)
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]
        if button == 'left':
            button = 1
        else:
            button = 2
        theEvent = Quartz.CGEventCreateMouseEvent(
            None, pressID[button], (pos[0], pos[1]), button - 1)
        Quartz.CGEventSetIntegerValueField(
            theEvent, Quartz.kCGMouseEventClickState, 2)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)
        Quartz.CGEventSetType(theEvent, releaseID[button])
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)
        Quartz.CGEventSetType(theEvent, pressID[button])
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)
        Quartz.CGEventSetType(theEvent, releaseID[button])
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, theEvent)

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        if direction not in ('vertical', 'horizontal'):
            raise ValueError(
                'Argument `direction` should be one of "vertical" or "horizontal". Got {}'.format(repr(direction)))
        pos = list(pos)
        pos[0] = pos[0] + self.monitor["left"]
        pos[1] = pos[1] + self.monitor["top"]

        moveevent = Quartz.CGEventCreateMouseEvent(
            None, Quartz.kCGEventMouseMoved, (pos[0], pos[1]), 0)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, moveevent)
        if direction == 'horizontal':
            interval = float(duration) / (abs(steps) + 1)
            if steps < 0:
                for i in range(0, abs(steps)):
                    time.sleep(interval)
                    self._scroll(None, 1)
            else:
                for i in range(0, abs(steps)):
                    time.sleep(interval)
                    self._scroll(None, -1)
        else:
            interval = float(duration) / (abs(steps) + 1)
            if steps < 0:
                for i in range(0, abs(steps)):
                    time.sleep(interval)
                    self._scroll(1)
            else:
                for i in range(0, abs(steps)):
                    time.sleep(interval)
                    self._scroll(-1)

    def _scroll(self, vertical=None, horizontal=None, depth=None):
        # Local submethod for generating Mac scroll events in one axis at a time
        def scroll_event(y_move=0, x_move=0, z_move=0, n=1):
            for _ in range(abs(n)):
                scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
                    None,  # No source
                    Quartz.kCGScrollEventUnitLine,  # Unit of measurement is lines
                    3,  # Number of wheels(dimensions)
                    y_move,
                    x_move,
                    z_move)
                Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

        # Execute vertical then horizontal then depth scrolling events
        if vertical is not None:
            vertical = int(vertical)
            if vertical == 0:   # Do nothing with 0 distance
                pass
            elif vertical > 0:  # Scroll up if positive
                scroll_event(y_move=1, n=vertical)
            else:  # Scroll down if negative
                scroll_event(y_move=-1, n=abs(vertical))
        if horizontal is not None:
            horizontal = int(horizontal)
            if horizontal == 0:  # Do nothing with 0 distance
                pass
            elif horizontal > 0:  # Scroll right if positive
                scroll_event(x_move=1, n=horizontal)
            else:  # Scroll left if negative
                scroll_event(x_move=-1, n=abs(horizontal))
        if depth is not None:
            depth = int(depth)
            if depth == 0:  # Do nothing with 0 distance
                pass
            elif vertical > 0:  # Scroll "out" if positive
                scroll_event(z_move=1, n=depth)
            else:  # Scroll "in" if negative
                scroll_event(z_move=-1, n=abs(depth))
