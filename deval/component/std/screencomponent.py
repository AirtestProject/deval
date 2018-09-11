# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class ScreenComponent(Component):

    def snapshot(self, filename, ensure_orientation=True):
        """
        Perform a screenshot operation on the current screen.

        Parameters:
            filename - the path to save the image.
        """
        raise NotImplementedError

    def move(self, pos):
        """
        Move the window to a specific coordinate.

        Parameters:
            pos - the position
        """
        raise NotImplementedError
