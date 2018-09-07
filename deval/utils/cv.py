# -*- coding: utf-8 -*-

import os
import sys
import cv2
import numpy as np
from six import PY3
from PIL import Image


def string_2_img(pngstr):
    nparr = np.fromstring(pngstr, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def pil_2_cv2(pil_image):
    open_cv_image = np.array(pil_image)
    # Convert RGB to BGR (method-1):
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    # Convert RGB to BGR (method-2):
    # b, g, r = cv2.split(open_cv_image)
    # open_cv_image = cv2.merge([r, g, b])
    return open_cv_image


def cv2_2_pil(cv2_image):
    cv2_im = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im)
    return pil_im


def imread(filename):
    """根据图片路径，将图片读取为cv2的图片处理格式."""
    if not os.path.isfile(filename):
        raise RuntimeError("File not exist: %s" % filename)
    if PY3:
        stream = open(filename, "rb")
        bytes = bytearray(stream.read())
        numpyarray = np.asarray(bytes, dtype=np.uint8)
        img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    else:
        filename = filename.encode(sys.getfilesystemencoding())
        img = cv2.imread(filename, 1)
    return img


def imwrite(filename, img):
    """写出图片到本地路径"""
    if PY3:
        cv2.imencode('.jpg', img)[1].tofile(filename)
    else:
        filename = filename.encode(sys.getfilesystemencoding())
        cv2.imwrite(filename, img)


def rotate(img, angle=90, clockwise=True):
    """
        函数使图片可顺时针或逆时针旋转90、180、270度.
        默认clockwise=True：顺时针旋转
    """

    def count_clock_rotate(img):
        # 逆时针旋转90°
        rows, cols = img.shape[:2]
        rotate_img = np.zeros((cols, rows))
        rotate_img = cv2.transpose(img)
        rotate_img = cv2.flip(rotate_img, 0)
        return rotate_img

    # 将角度旋转转化为逆时针旋转90°的次数:
    counter_rotate_time = (
        4 - angle / 90) % 4 if clockwise else (angle / 90) % 4
    for i in range(int(counter_rotate_time)):
        img = count_clock_rotate(img)

    return img


def crop_image(img, rect):
    """
        区域截图，同时返回截取结果 和 截取偏移;
        Crop image , rect = [x_min, y_min, x_max ,y_max].
    """

    if isinstance(rect, (list, tuple)):
        height, width = img.shape[:2]
        # 获取在图像中的实际有效区域：
        x_min, y_min, x_max, y_max = [int(i) for i in rect]
        x_min, y_min = max(0, x_min), max(0, y_min)
        x_min, y_min = min(width - 1, x_min), min(height - 1, y_min)
        x_max, y_max = max(0, x_max), max(0, y_max)
        x_max, y_max = min(width - 1, x_max), min(height - 1, y_max)

        # 返回剪切的有效图像+左上角的偏移坐标：
        img_crop = img[y_min:y_max, x_min:x_max]
        return img_crop
    else:
        raise Exception(
            "to crop a image, rect should be a list like: [x_min, y_min, x_max, y_max].")
