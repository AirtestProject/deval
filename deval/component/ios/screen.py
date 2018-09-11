# -*- coding: utf-8 -*-

from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.std.screen import ScreenComponent
from deval.utils.ios.iosfuncs import IOSProxy, _check_platform_ios, CAP_METHOD, LANDSCAPE, LANDSCAPE_RIGHT
from deval.utils.parse import parse_uri


class IOSScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        try:
            self.proxy = self.dev.iosproxy
        except AttributeError:
            self.dev.iosproxy = IOSProxy(**_check_platform_ios(uri))
            self.proxy = self.dev.iosproxy

    def snapshot(self, filename=None, ensure_orientation=True):
        """
        take snapshot
        filename: save screenshot to filename
        """
        strType = False
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
                    screen = rotate(
                        screen, self.proxy.display_info["orientation"] * 90, clockwise=False)

            # wda 截图是要根据orientation旋转
            elif self.proxy.cap_method == CAP_METHOD.WDACAP:
                # seems need to rotate in opencv opencv-contrib-python==3.2.0.7
                screen = rotate(screen, 90, clockwise=(
                    now_orientation == LANDSCAPE_RIGHT))

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
