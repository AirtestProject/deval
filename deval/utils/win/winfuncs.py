# -*- coding: utf-8 -*-

import win32gui
import win32api
import win32ui
import win32con
from pywinauto.application import Application
from pywinauto.win32functions import GetSystemMetrics, SetForegroundWindow
from pywinauto.win32structures import RECT
from deval.utils.cv import Image, pil_2_cv2
from deval.utils.parse import parse_uri

DPIFACTOR = 1
SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79


def _check_platform_win(uri, platform="windows"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    params.pop("platform")
    if "host" in params:
        params.pop("host")
    if "uuid" in params:
        handle = params["uuid"]
        if handle != '':
            params["handle"] = int(handle)
        params.pop("uuid")
    return params


def set_foreground_window(window):
    if window:
        SetForegroundWindow(window)


def get_rect(window):
    if window:
        return window.rectangle()
    else:
        return RECT(right=GetSystemMetrics(0), bottom=GetSystemMetrics(1))


def get_app(kwargs):
    if len(kwargs) == 0:
        return None
    if "handle" in kwargs:
        kwargs["handle"] = int(kwargs["handle"])
    return Application().connect(**kwargs)


def get_window(kwargs):
    handle = kwargs.get("handle")
    if handle:
        handle = int(handle)
        return get_app(kwargs).window(handle=handle).wrapper_object()
    else:
        app = get_app(kwargs)
        if app:
            return app.top_window().wrapper_object()


def get_action_pos(window, pos):
    if window:
        rect = get_rect(window)
        pos = (int((pos[0] + rect.left) * DPIFACTOR), int((pos[1] + rect.top) * DPIFACTOR))
    pos = (int(pos[0]), int(pos[1]))
    return pos


def screenshot(filename, hwnd=None):
    """
    Take the screenshot of Windows app

    Args:
        filename: file name where to store the screenshot
        hwnd:

    Returns:
        bitmap screenshot file

    """
    # import ctypes
    # user32 = ctypes.windll.user32
    # user32.SetProcessDPIAware()

    if hwnd is None:
        """all screens"""
        hwnd = win32gui.GetDesktopWindow()
        # get complete virtual screen including all monitors
        w = win32api.GetSystemMetrics(SM_CXVIRTUALSCREEN)
        h = win32api.GetSystemMetrics(SM_CYVIRTUALSCREEN)
        x = win32api.GetSystemMetrics(SM_XVIRTUALSCREEN)
        y = win32api.GetSystemMetrics(SM_YVIRTUALSCREEN)
    else:
        """window"""
        rect = win32gui.GetWindowRect(hwnd)
        w = abs(rect[2] - rect[0])
        h = abs(rect[3] - rect[1])
        x, y = 0, 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x, y), win32con.SRCCOPY)
    # saveBitMap.SaveBitmapFile(saveDC, filename)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    pil_image = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    cv2_image = pil_2_cv2(pil_image)
    return cv2_image
