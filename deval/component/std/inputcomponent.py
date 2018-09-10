# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class InputComponent(Component):
    def __init__(self, uri, dev=None, name="input"):
        if name is None:
            super(InputComponent, self).__init__(uri, dev, "input")
        else:
            super(InputComponent, self).__init__(uri, dev, name)

    def click(self, pos, duration=0.05, button='left'):
        """
        This is a click functhion.

        Parameters:
            pos - a list refer to the click position.
            duration - the duration of the operation.
            button - the button of the operation.
        """
        raise NotImplementedError

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        """
        Perform swipe action on target device from point to point given by start point and end point.

        Parameters:
            p1 - a list refer to the start point.
            p2 - a list refer to the end point.
            duration - the duration of the operation.
            steps - the steps of the operation.
            fingers - the number of fingers to perform the operation.
            button - the button of the operation.
        """
        raise NotImplementedError

    def pinch(self, *args, **kwargs):
        raise NotImplementedError

    def double_tap(self, pos, button='left'):
        """
        This is a double-tap functhion. Similar to click.

        Parameters:
            pos - a list refer to the double click position.
            button - the button of the operation.
        """
        raise NotImplementedError

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        """
        Perform the scroll wheel operation of the middle mouse button.

        Parameters:
            pos - a list refer to the mouse position.
            direction - the direction of the operation.
            duration - the duration of the operation.
            steps - the number of times of the operation.
        """
        raise NotImplementedError
