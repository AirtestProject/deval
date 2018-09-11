# -*- coding: utf-8 -*-

from Xlib import display, X
from PIL import Image
from deval.component.std.screencomponent import ScreenComponent
from deval.utils.cv import imwrite
from deval.utils.cv import pil_2_cv2


class LinuxScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

    def snapshot(self, filename="tmp.png"):
        w, h = self.get_current_resolution()
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(0, 0, w, h, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
        image = pil_2_cv2(image)
        if filename:
            imwrite(filename, image)
        return image

    def get_current_resolution(self):
        d = display.Display()
        screen = d.screen()
        w, h = (screen["width_in_pixels"], screen["height_in_pixels"])
        return w, h
