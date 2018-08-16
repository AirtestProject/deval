#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import warnings
from copy import copy
from deval.core.android.ime import YosemiteIme
from deval.core.android.constant import CAP_METHOD, TOUCH_METHOD, IME_METHOD, ORI_METHOD
from deval.core.android.adb import ADB
from deval.core.android.minicap import Minicap
from deval.core.android.minitouch import Minitouch
from deval.core.android.javacap import Javacap
from deval.core.android.rotation import RotationWatcher, XYTransformer
from deval.core.android.recorder import Recorder
from deval.utils.parse import parse_uri


def _check_platform_android(uri, platform="android"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    if "uuid" in params:
        params["serialno"] = params["uuid"]
        params.pop("uuid")
    params.pop("platform")
    return params


class AndroidProxy(object):
    """AndroidProxy Class"""

    def __init__(self, serialno=None, host=None,
                 cap_method=CAP_METHOD.MINICAP_STREAM,
                 touch_method=TOUCH_METHOD.MINITOUCH,
                 ime_method=IME_METHOD.YOSEMITEIME,
                 ori_method=ORI_METHOD.MINICAP,
                 ):
        self.serialno = serialno or self.get_default_device()
        self.cap_method = cap_method.upper()
        self.touch_method = touch_method.upper()
        self.ime_method = ime_method.upper()
        self.ori_method = ori_method.upper()
        # init adb
        self.adb = ADB(self.serialno, server_addr=host)
        self.adb.wait_for_device()
        self.sdk_version = self.adb.sdk_version
        self._display_info = {}
        self._current_orientation = None
        # init components
        self.rotation_watcher = RotationWatcher(self.adb)
        self.minicap = Minicap(self.adb, ori_function=self.get_display_info)
        self.javacap = Javacap(self.adb)
        self.minitouch = Minitouch(self.adb, ori_function=self.get_display_info)
        self.yosemite_ime = YosemiteIme(self.adb)
        self.recorder = Recorder(self.adb)
        self._register_rotation_watcher()

    def get_default_device(self):
        """
        Get local default device when no serailno

        Returns:
            local device serialno

        """
        if not ADB().devices(state="device"):
            raise IndexError("ADB devices not found")
        return ADB().devices(state="device")[0][0]

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
        if self.ori_method == ORI_METHOD.MINICAP:
            display_info = self.minicap.get_display_info()
        else:
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

    def _touch_point_by_orientation(self, tuple_xy):
        """
        Convert image coordinates to physical display coordinates, the arbitrary point (origin) is upper left corner
        of the device physical display

        Args:
            tuple_xy: image coordinates (x, y)

        Returns:

        """
        x, y = tuple_xy
        x, y = XYTransformer.up_2_ori(
            (x, y),
            (self.display_info["width"], self.display_info["height"]),
            self.display_info["orientation"]
        )
        return x, y
