# -*- coding: utf-8 -*-

import time
import re
from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.component import InputComponent, KeyEventComponent, NetworkComponent
from deval.component.component import AppComponent, ScreenComponent, Component
from deval.core.ios.iosfuncs import IOSProxy, _check_platform_ios, TOUCH_METHOD, IME_METHOD, CAP_METHOD
from deval.utils.parse import parse_uri
from wda import LANDSCAPE, PORTRAIT, LANDSCAPE_RIGHT, PORTRAIT_UPSIDEDOWN
from wda import WDAError


# retry when saved session failed
def retry_session(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except WDAError as err:
            # 6 : Session does not exist
            if err.status == 6:
                self.proxy._fetchNewSession()
                return func(self, *args, **kwargs)
            else:
                raise err
    return wrapper


class IOSInputComponent(InputComponent):   

    def __init__(self, uri, dev, name=None):
        super(IOSInputComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    @retry_session
    def click(self, pos, **kwargs):
        duration = kwargs.get("duration", 0.05)
        # trans pos of click
        pos = self.proxy._touch_point_by_orientation(pos)

        # scale touch postion
        x, y = pos[0] * self.proxy._touch_factor, pos[1] * self.proxy._touch_factor
        if duration >= 0.5:
            self.proxy.session.tap_hold(x, y, duration)
        else:
            self.proxy.session.tap(x, y)

    def swipe(self, p1, p2, **kwargs):
        duration = kwargs.get("duration", 0.5)
        steps = kwargs.get("steps", 5)
        fingers = kwargs.get("fingers", 1)

        fx, fy = self.proxy._touch_point_by_orientation(p1)
        tx, ty = self.proxy._touch_point_by_orientation(p2)

        self.proxy.session.swipe(fx * self.proxy._touch_factor, fy * self.proxy._touch_factor, tx * self.proxy._touch_factor, ty * self.proxy._touch_factor, duration)

    def double_tap(self, pos, **kwargs):
        # trans pos of click
        pos = self.proxy._touch_point_by_orientation(pos)

        x, y = pos[0] * self.proxy._touch_factor, pos[1] * self.proxy._touch_factor
        self.proxy.session.double_tap(x, y)


class IOSKeyEventComponent(KeyEventComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSKeyEventComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def keyevent(self, keys, **kwargs):
        """just use as home event"""
        if keys not in ['HOME', 'home', 'Home']:
            raise NotImplementedError
        self.home()

    @retry_session
    def text(self, text, enter=True, **kwargs):
        """bug in wda for now"""
        if enter:
            text += '\n'
        self.proxy.session.send_keys(text)
    
    def home(self, **kwargs):
        return self.proxy.driver.home()


class IOSAppComponent(AppComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSAppComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def start_app(self, package, activity=None, **kwargs):
        self.proxy.driver.session(package)

    def stop_app(self, package, **kwargs):
        self.proxy.driver.session().close()


class IOSScreenComponent(ScreenComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def snapshot(self, filename=None, strType=False, ensure_orientation=True, **kwargs):
        """
        take snapshot
        filename: save screenshot to filename
        """
        data = None

        if self.proxy.cap_method == CAP_METHOD.MINICAP:
            raise NotImplementedError
        elif self.proxy.cap_method == CAP_METHOD.MINICAP_STREAM:
            raise NotImplementedError
        elif self.proxy.cap_method == CAP_METHOD.WDACAP:
            data = self.proxy._neo_wda_screenshot()  # wda 截图不用考虑朝向

        if strType:
            if filename:
                with open(filename, 'wb') as f:
                    f.write(data)
            return data

        # output cv2 object
        try:
            screen = string_2_img(data)
        except:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        now_orientation = self.proxy.orientation

        # ensure the orientation is right
        if ensure_orientation and now_orientation in [LANDSCAPE, LANDSCAPE_RIGHT]:

            # minicap screenshots are different for various sdk_version
            if self.proxy.cap_method in (CAP_METHOD.MINICAP, CAP_METHOD.MINICAP_STREAM):
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(screen, self.proxy.display_info["orientation"] * 90, clockwise=False)

            # wda 截图是要根据orientation旋转
            elif self.proxy.cap_method == CAP_METHOD.WDACAP:
                # seems need to rotate in opencv opencv-contrib-python==3.2.0.7
                screen = rotate(screen, 90, clockwise=(now_orientation == LANDSCAPE_RIGHT))

        # readed screen size
        h, w = screen.shape[:2]

        # save last res for portrait
        if now_orientation in [LANDSCAPE, LANDSCAPE_RIGHT]:
            self.proxy._size['height'] = w
            self.proxy._size['width'] = h
        else:
            self.proxy._size['height'] = h
            self.proxy._size['width'] = w

        winw, winh = self.proxy.window_size()

        self.proxy._touch_factor = float(winh) / float(h)

        # save as file if needed
        if filename:
            imwrite(filename, screen)

        return screen


class IOSNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(IOSNetworkComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def get_ip_address(self, **kwargs):
        return self.proxy.driver.status()['ios']['ip']


class IOSStatueComponent(Component):
    
    def __init__(self, uri, dev, name="statue"):
        super(IOSStatueComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def device_status(self, **kwargs):
        return self.proxy.driver.status()
