# -*- coding: utf-8 -*-

import os
from mss import mss
from deval.component.std.screen import ScreenComponent
from deval.utils.cv import imwrite, imread
from deval.utils.cv import pil_2_cv2


class MacScreenComponent(ScreenComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)
        self.screen = mss()
        self.monitor = self.screen.monitors[0]

    def snapshot(self, filename="tmp.png"):
        from PIL import Image
        sct_img = self.screen.grab(self.screen.monitors[0])
        image = Image.frombytes('RGB', sct_img.size,
                                sct_img.bgra, 'raw', 'BGRX')
        if len(self.screen.monitors) > 2 and self.screen.monitors[0].get("height") != self.screen.monitors[1].get(
                "height"):
            output = filename
            image.save(output)
            image = imread(output)
            os.remove(output)
        else:
            image = pil_2_cv2(image)
        imwrite(filename, image)
        return image

    def get_current_resolution(self):
        width = self.monitor["width"]
        height = self.monitor["height"]
        return width, height
