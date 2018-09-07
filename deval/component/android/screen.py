# -*- coding: utf-8 -*-


from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.std.screencomponent import ScreenComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android, CAP_METHOD
from deval.utils.parse import parse_uri


class AndroidMiniCapStreamScreenComponent(ScreenComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidMiniCapStreamScreenComponent,
              self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def snapshot(self, filename=None, ensure_orientation=True):

        self.proxy.rotation_watcher.get_ready()
        screen = self.proxy.minicap.get_frame_from_stream()

        # output cv2 object
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        if ensure_orientation and self.proxy.display_info["orientation"]:
            if self.proxy.sdk_version <= 16:
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(
                        screen, self.proxy.display_info["orientation"] * 90, clockwise=False)

        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.proxy.adb.is_screenon()

    def is_locked(self):
        return self.proxy.adb.is_locked()

    def unlock(self):
        return self.proxy.adb.unlock()


class AndroidJAVACapScreenComponent(ScreenComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidJAVACapScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def snapshot(self, filename=None, ensure_orientation=True):
        screen = self.proxy.javacap.get_frame_from_stream()
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.proxy.adb.is_screenon()

    def is_locked(self):
        return self.proxy.adb.is_locked()

    def unlock(self):
        return self.proxy.adb.unlock()


class AndroidMiniCapScreenComponent(ScreenComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidMiniCapScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def snapshot(self, filename=None, ensure_orientation=True):

        screen = self.proxy.minicap.get_frame()
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
            if self.proxy.sdk_version <= 16:
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(
                        screen, self.proxy.display_info["orientation"] * 90, clockwise=False)

        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.proxy.adb.is_screenon()

    def is_locked(self):
        return self.proxy.adb.is_locked()

    def unlock(self):
        return self.proxy.adb.unlock()


class AndroidADBScreenComponent(ScreenComponent):

    def __init__(self, uri, dev, name=None):
        super(AndroidADBScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(
                **_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def snapshot(self, filename=None, ensure_orientation=True):
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
            screen = rotate(
                screen, self.proxy.display_info["orientation"] * 90, clockwise=False)
        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.proxy.adb.is_screenon()

    def is_locked(self):
        return self.proxy.adb.is_locked()

    def unlock(self):
        return self.proxy.adb.unlock()
