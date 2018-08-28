# -*- coding: utf-8 -*-

import time
import re
from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.component import InputComponent, KeyEventComponent, RuntimeComponent
from deval.component.component import AppComponent, ScreenComponent, NetworkComponent, Component
from deval.core.android.androidfuncs import AndroidProxy, _check_platform_android, TOUCH_METHOD, IME_METHOD, CAP_METHOD
from deval.utils.parse import parse_uri


class AndroidInputComponent(InputComponent):   

    def __init__(self, uri, dev, name=None):
        super(AndroidInputComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def click(self, pos, **kwargs):
        duration = kwargs.get("duration", 0.05)
        if self.proxy.touch_method == TOUCH_METHOD.MINITOUCH:
            pos = self.proxy._touch_point_by_orientation(pos)
            self.proxy.minitouch.touch(pos, duration=duration)
        else:
            self.proxy.adb.touch(pos)

    def swipe(self, p1, p2, **kwargs):
        duration = kwargs.get("duration", 0.5)
        steps = kwargs.get("steps", 5)
        fingers = kwargs.get("fingers", 1)

        if self.proxy.touch_method == TOUCH_METHOD.MINITOUCH:
            p1 = self.proxy._touch_point_by_orientation(p1)
            p2 = self.proxy._touch_point_by_orientation(p2)
            if fingers == 1:
                self.proxy.minitouch.swipe(p1, p2, duration=duration, steps=steps)
            elif fingers == 2:
                self.proxy.minitouch.two_finger_swipe(p1, p2, duration=duration, steps=steps)
            else:
                raise Exception("param fingers should be 1 or 2")
        else:
            duration *= 1000  # adb的swipe操作时间是以毫秒为单位的。
            self.proxy.adb.swipe(p1, p2, duration=duration)

    def pinch(self, *args, **kwargs):
        return self.proxy.minitouch.pinch(*args, **kwargs)

    def double_tap(self, pos, **kwargs):
        duration = kwargs.get("duration", 0.05)
        if self.proxy.touch_method == TOUCH_METHOD.MINITOUCH:
            pos = self.proxy._touch_point_by_orientation(pos)
            self.proxy.minitouch.touch(pos, duration=duration)
        else:
            self.proxy.adb.touch(pos)

        time.sleep(0.05)

        if self.proxy.touch_method == TOUCH_METHOD.MINITOUCH:
            pos = self.proxy._touch_point_by_orientation(pos)
            self.proxy.minitouch.touch(pos, duration=duration)
        else:
            self.proxy.adb.touch(pos)


class AndroidKeyEventComponent(KeyEventComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidKeyEventComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def keyevent(self, keyname, **kwargs):
        return self.proxy.adb.keyevent(keyname)

    def text(self, text, enter=True, **kwargs):
        if self.proxy.ime_method == IME_METHOD.YOSEMITEIME:
            self.proxy.yosemite_ime.text(text)
        else:
            self.proxy.adb.shell(["input", "text", text])

        # 游戏输入时，输入有效内容后点击Enter确认，如不需要，enter置为False即可。
        if enter:
            self.proxy.adb.shell(["input", "keyevent", "ENTER"])

    def wake(self, **kwargs):
        self.proxy.adb.keyevent("HOME")
        self.proxy.recorder.install_or_upgrade()  # 暂时Yosemite只用了ime
        self.proxy.adb.shell(['am', 'start', '-a', 'com.netease.nie.yosemite.ACTION_IDENTIFY'])
        self.proxy.adb.keyevent("HOME")
    
    def home(self, **kwargs):
        self.proxy.adb.keyevent("HOME")


class AndroidRuntimeComponent(RuntimeComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidRuntimeComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def shell(self, *args, **kwargs):
        return self.proxy.adb.shell(*args, **kwargs)

    def get_top_activity_name_and_pid(self, **kwargs):
        dat = self.proxy.adb.shell('dumpsys activity top')
        activityRE = re.compile('\s*ACTIVITY ([A-Za-z0-9_.]+)/([A-Za-z0-9_.]+) \w+ pid=(\d+)')
        m = activityRE.search(dat)
        if m:
            return (m.group(1), m.group(2), m.group(3))
        else:
            return None

    def get_top_activity_name(self, **kwargs):
        """
        Get the top activity name

        Returns:
            package, activity and pid

        """
        tanp = self.get_top_activity_name_and_pid()
        if tanp:
            return tanp[0] + '/' + tanp[1]
        else:
            return None


class AndroidAppComponent(AppComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidAppComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def start_app(self, package, activity=None, **kwargs):
        return self.proxy.adb.start_app(package, activity)

    def start_app_timing(self, package, activity=None, **kwargs):
        return self.proxy.adb.start_app_timing(package, activity)

    def stop_app(self, package, **kwargs):
        return self.proxy.adb.stop_app(package)

    def clear_app(self, package, **kwargs):
        return self.proxy.adb.clear_app(package)

    def install_app(self, filepath, replace=False, **kwargs):
        return self.proxy.adb.install_app(filepath, replace=replace)

    def install_multiple_app(self, filepath, replace=False, **kwargs):
        return self.proxy.adb.install_multiple_app(filepath, replace=replace)

    def uninstall_app(self, package, **kwargs):
        return self.proxy.adb.uninstall_app(package)

    def list_app(self, third_only=False, **kwargs):
        return self.proxy.adb.list_app(third_only)

    def path_app(self, package, **kwargs):
        return self.proxy.adb.path_app(package)

    def check_app(self, package, **kwargs):
        return self.proxy.adb.check_app(package)


class AndroidScreenComponent(ScreenComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def snapshot(self, filename=None, ensure_orientation=True, **kwargs):
        if self.proxy.cap_method == CAP_METHOD.MINICAP_STREAM:
            self.proxy.rotation_watcher.get_ready()
            screen = self.proxy.minicap.get_frame_from_stream()
        elif self.proxy.cap_method == CAP_METHOD.MINICAP:
            screen = self.proxy.minicap.get_frame()
        elif self.proxy.cap_method == CAP_METHOD.JAVACAP:
            screen = self.proxy.javacap.get_frame_from_stream()
        else:
            screen = self.proxy.adb.snapshot()
        # output cv2 object
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        # ensure the orientation is right
        if ensure_orientation and self.proxy.display_info["orientation"]:
            # minicap screenshots are different for various sdk_version
            if self.proxy.cap_method in (CAP_METHOD.MINICAP, CAP_METHOD.MINICAP_STREAM) and self.proxy.sdk_version <= 16:
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(screen, self.proxy.display_info["orientation"] * 90, clockwise=False)
            # adb 截图总是要根据orientation旋转
            elif self.proxy.cap_method == CAP_METHOD.ADBCAP:
                screen = rotate(screen, self.proxy.display_info["orientation"] * 90, clockwise=False)
        if filename:
            imwrite(filename, screen)
        return screen


class AndroidNetworkComponent(NetworkComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidNetworkComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def get_ip_address(self, **kwargs):
        return self.proxy.adb.get_ip_address()


class AndroidStatueComponent(Component):
    
    def __init__(self, uri, dev, name="statue"):
        super(AndroidStatueComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self..dev.androidproxy
        except AttributeError:
            self..dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self..dev.androidproxy

    def is_keyboard_shown(self, **kwargs):
        return self.proxy.adb.is_keyboard_shown()

    def is_screenon(self, **kwargs):
        return self.proxy.adb.is_screenon()

    def is_locked(self, **kwargs):
        return self.proxy.adb.is_locked()

    def unlock(self, **kwargs):
        return self.proxy.adb.unlock()
