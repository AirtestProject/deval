# -*- coding: utf-8 -*-


from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.std.screencomponent import ScreenComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android, CAP_METHOD
from deval.utils.parse import parse_uri


class AndroidScreenComponent(ScreenComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidScreenComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

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

    def is_screenon(self, **kwargs):
        return self.proxy.adb.is_screenon()

    def is_locked(self, **kwargs):
        return self.proxy.adb.is_locked()

    def unlock(self, **kwargs):
        return self.proxy.adb.unlock()
