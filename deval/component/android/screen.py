# -*- coding: utf-8 -*-

from copy import copy
from deval.utils.cv import string_2_img, rotate, imwrite
from deval.component.std.screencomponent import ScreenComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri
from deval.utils.android.rotation import RotationWatcher
from deval.utils.android.minicap import Minicap
from deval.utils.android.javacap import Javacap


class AndroidMiniCapStreamScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
        self.rotation_watcher = RotationWatcher(self.adb)
        self.minicap = Minicap(self.adb)
        self._display_info = {}
        self._current_orientation = None
        self._register_rotation_watcher()

    def snapshot(self, filename=None, ensure_orientation=True):

        self.rotation_watcher.get_ready()
        screen = self.minicap.get_frame_from_stream()

        # output cv2 object
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        if ensure_orientation and self.display_info["orientation"]:
            if self.adb.sdk_version <= 16:
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(
                        screen, self.display_info["orientation"] * 90, clockwise=False)

        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.adb.is_screenon()

    def is_locked(self):
        return self.adb.is_locked()

    def unlock(self):
        return self.adb.unlock()

    @property
    def display_info(self):
        """
        Return the display info (width, height, orientation and max_x, max_y)

        Returns:
            display information

        """
        if not self._display_info:
            self._display_info = self.get_display_info()
        display_info = copy(self._display_info)
        # update ow orientation, which is more accurate
        if self._current_orientation is not None:
            display_info.update({
                "rotation": self._current_orientation * 90,
                "orientation": self._current_orientation,
            })
        return display_info

    def get_display_info(self):
        """
        Return the display info (width, height, orientation and max_x, max_y)

        Returns:
            display information

        """
        display_info = self.adb.get_display_info()
        return display_info

    def _register_rotation_watcher(self):
        """
        Register callbacks for Android and minicap when rotation of screen has changed

        callback is called in another thread, so be careful about thread-safety

        Returns:
            None

        """
        self.rotation_watcher.reg_callback(lambda x: setattr(self, "_current_orientation", x))
        self.rotation_watcher.reg_callback(lambda x: self.minicap.update_rotation(x * 90))


class AndroidJAVACapScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
        self.javacap = Javacap(self.adb)
        self._display_info = {}
        self._current_orientation = None
        self.rotation_watcher = RotationWatcher(self.adb)
        self._register_rotation_watcher()
        
    def snapshot(self, filename=None, ensure_orientation=True):
        screen = self.javacap.get_frame_from_stream()
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
        return self.adb.is_screenon()

    def is_locked(self):
        return self.adb.is_locked()

    def unlock(self):
        return self.adb.unlock()

    @property
    def display_info(self):
        if not self._display_info:
            self._display_info = self.get_display_info()
        display_info = copy(self._display_info)
        # update ow orientation, which is more accurate
        if self._current_orientation is not None:
            display_info.update({
                "rotation": self._current_orientation * 90,
                "orientation": self._current_orientation,
            })
        return display_info

    def get_display_info(self):
        display_info = self.adb.get_display_info()
        return display_info

    def _register_rotation_watcher(self):
        self.rotation_watcher.reg_callback(lambda x: setattr(self, "_current_orientation", x))


class AndroidMiniCapScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
        self.rotation_watcher = RotationWatcher(self.adb)
        self.minicap = Minicap(self.adb)
        self._display_info = {}
        self._current_orientation = None
        self._register_rotation_watcher()

    def snapshot(self, filename=None, ensure_orientation=True):

        screen = self.minicap.get_frame()
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        # ensure the orientation is right
        if ensure_orientation and self.display_info["orientation"]:
            # minicap screenshots are different for various sdk_version
            if self.adb.sdk_version <= 16:
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(
                        screen, self.display_info["orientation"] * 90, clockwise=False)

        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.adb.is_screenon()

    def is_locked(self):
        return self.adb.is_locked()

    def unlock(self):
        return self.adb.unlock()

    @property
    def display_info(self):
        if not self._display_info:
            self._display_info = self.get_display_info()
        display_info = copy(self._display_info)
        # update ow orientation, which is more accurate
        if self._current_orientation is not None:
            display_info.update({
                "rotation": self._current_orientation * 90,
                "orientation": self._current_orientation,
            })
        return display_info

    def get_display_info(self):
        display_info = self.minicap.get_display_info()
        return display_info

    def _register_rotation_watcher(self):
        self.rotation_watcher.reg_callback(lambda x: setattr(self, "_current_orientation", x))
        self.rotation_watcher.reg_callback(lambda x: self.minicap.update_rotation(x * 90))


class AndroidADBScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb
        self.rotation_watcher = RotationWatcher(self.adb)
        self._display_info = {}
        self._current_orientation = None
        self._register_rotation_watcher()

    def snapshot(self, filename=None, ensure_orientation=True):
        screen = self.adb.snapshot()
        # output cv2 object
        try:
            screen = string_2_img(screen)
        except Exception:
            # may be black/locked screen or other reason, print exc for debugging
            import traceback
            traceback.print_exc()
            return None

        # ensure the orientation is right
        if ensure_orientation and self.display_info["orientation"]:
            screen = rotate(
                screen, self.display_info["orientation"] * 90, clockwise=False)
        if filename:
            imwrite(filename, screen)
        return screen

    def is_screenon(self):
        return self.adb.is_screenon()

    def is_locked(self):
        return self.adb.is_locked()

    def unlock(self):
        return self.adb.unlock()

    @property
    def display_info(self):
        if not self._display_info:
            self._display_info = self.get_display_info()
        display_info = copy(self._display_info)
        # update ow orientation, which is more accurate
        if self._current_orientation is not None:
            display_info.update({
                "rotation": self._current_orientation * 90,
                "orientation": self._current_orientation,
            })
        return display_info

    def get_display_info(self):
        display_info = self.adb.get_display_info()
        return display_info

    def _register_rotation_watcher(self):
        self.rotation_watcher.reg_callback(lambda x: setattr(self, "_current_orientation", x))
