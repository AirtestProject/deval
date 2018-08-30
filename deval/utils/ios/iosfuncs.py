#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import six
import time
import json
import base64
import wda
from deval.utils.cv import *
from deval.utils.ios.constant import CAP_METHOD, TOUCH_METHOD, IME_METHOD
from deval.utils.ios.rotation import XYTransformer, RotationWatcher
from deval.utils.ios.fake_minitouch import fakeMiniTouch
from deval.utils.ios.instruct_helper import InstructHelper
from deval.utils.logger import get_logger
from deval.utils.parse import parse_uri
from wda import LANDSCAPE, PORTRAIT, LANDSCAPE_RIGHT, PORTRAIT_UPSIDEDOWN
from wda import WDAError
if six.PY3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin


logger = get_logger(__name__)
DEFAULT_ADDR = "http://localhost:8100/"


# retry when saved session failed
def retry_session(func):
    def wrapper(self, *args, **kwargs):                                                                                                              
        try:
            return func(self, *args, **kwargs)
        except WDAError as err:
            # 6 : Session does not exist
            if err.status == 6:
                self._fetchNewSession()
                return func(self, *args, **kwargs)
            else:
                raise err
    return wrapper


def _check_platform_ios(uri, platform="ios"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    if "uuid" in params:
        params["addr"] = params["uuid"]
        params.pop("uuid")
    params.pop("platform")
    return params


class IOSProxy(object):
    """ios client
        # befor this you have to run WebDriverAgent
        # xcodebuild -project path/to/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$(idevice_id -l)" test
        # iproxy $port 8100 $udid
    """

    def __init__(self, addr=DEFAULT_ADDR):
        super(IOSProxy, self).__init__()

        # if none or empty, use default addr
        self.addr = addr or DEFAULT_ADDR

        # fit wda format, make url start with http://
        if not self.addr.startswith("http://"):
            self.addr = "http://" + addr

        """here now use these supported cap touch and ime method"""
        self.cap_method = CAP_METHOD.WDACAP
        self.touch_method = TOUCH_METHOD.WDATOUCH
        self.ime_method = IME_METHOD.WDAIME

        # wda driver, use to home, start app
        # init wda session, updata when start app
        # use to click/swipe/close app/get wda size
        wda.DEBUG = False
        self.driver = wda.Client(self.addr)

        # record device's width
        self._size = {'width': None, 'height': None}
        self._touch_factor = 0.5
        self._last_orientation = None
        self.defaultSession = None

        # start up RotationWatcher with default session
        self.rotation_watcher = RotationWatcher(self)

        # fake minitouch to simulate swipe
        self.minitouch = fakeMiniTouch(self)

        # helper of run process like iproxy
        self.instruct_helper = InstructHelper()

    @property
    def session(self):
        if not self.defaultSession:
            self.defaultSession = self.driver.session()
        return self.defaultSession

    def _fetchNewSession(self):
        self.defaultSession = self.driver.session()

    @retry_session
    def window_size(self):
        """
            return window size
            namedtuple:
                Size(wide , hight)
        """
        return self.session.window_size()

    @property
    @retry_session
    def orientation(self):
        """
            return device oritantation status
            in  LANDSACPE POR
        """
        return self.session.orientation

    @property
    def display_info(self):
        if not self._size['width'] or not self._size['height']:
            self.snapshot()
        return {'width': self._size['width'], 'height': self._size['height'], 'orientation': self.orientation, 'physical_width': self._size['width'], 'physical_height': self._size['height']}

    def snapshot(self, filename=None, strType=False, ensure_orientation=True):
        """
        take snapshot
        filename: save screenshot to filename
        """
        data = None

        if self.cap_method == CAP_METHOD.MINICAP:
            raise NotImplementedError
        elif self.cap_method == CAP_METHOD.MINICAP_STREAM:
            raise NotImplementedError
        elif self.cap_method == CAP_METHOD.WDACAP:
            data = self._neo_wda_screenshot()  # wda 截图不用考虑朝向

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

        now_orientation = self.orientation

        # ensure the orientation is right
        if ensure_orientation and now_orientation in [LANDSCAPE, LANDSCAPE_RIGHT]:

            # minicap screenshots are different for various sdk_version
            if self.cap_method in (CAP_METHOD.MINICAP, CAP_METHOD.MINICAP_STREAM):
                h, w = screen.shape[:2]  # cvshape是高度在前面!!!!
                if w < h:  # 当前是横屏，但是图片是竖的，则旋转，针对sdk<=16的机器
                    screen = rotate(screen, self.display_info["orientation"] * 90, clockwise=False)

            # wda 截图是要根据orientation旋转
            elif self.cap_method == CAP_METHOD.WDACAP:
                # seems need to rotate in opencv opencv-contrib-python==3.2.0.7
                screen = rotate(screen, 90, clockwise=(now_orientation == LANDSCAPE_RIGHT))

        # readed screen size
        h, w = screen.shape[:2]

        # save last res for portrait
        if now_orientation in [LANDSCAPE, LANDSCAPE_RIGHT]:
            self._size['height'] = w
            self._size['width'] = h
        else:
            self._size['height'] = h
            self._size['width'] = w

        winw, winh = self.window_size()

        self._touch_factor = float(winh) / float(h)

        # save as file if needed
        if filename:
            imwrite(filename, screen)

        return screen

    def _neo_wda_screenshot(self):
        """
            this is almost same as wda implementation, but without png header check,
            as response data is now jpg format in mid quality
        """
        value = self.driver.http.get('screenshot').value
        raw_value = base64.b64decode(value)
        return raw_value

    def _touch_point_by_orientation(self, tuple_xy):
        """
        Convert image coordinates to physical display coordinates, the arbitrary point (origin) is upper left corner
        of the device physical display

        Args:
            tuple_xy: image coordinates (x, y)

        Returns:

        """
        x, y = tuple_xy

        # use correct w and h due to now orientation
        # _size 只对应竖直时候长宽
        now_orientation = self.orientation

        if now_orientation in [PORTRAIT, PORTRAIT_UPSIDEDOWN]:
            width, height = self._size['width'], self._size["height"]
        else:
            height, width = self._size['width'], self._size["height"]

        # check if not get screensize when touching
        if not width or not height:
            # use snapshot to get current resuluton
            self.snapshot()

        x, y = XYTransformer.up_2_ori(
            (x, y),
            (width, height),
            now_orientation
        )
        return x, y
