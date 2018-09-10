# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class KeyEventComponent(Component):
    def __init__(self, uri, dev=None, name="keyevent"):
        if name is None:
            super(KeyEventComponent, self).__init__(uri, dev, "keyevent")
        else:
            super(KeyEventComponent, self).__init__(uri, dev, name)

    def keyevent(self, keyname):
        """
        If the target device is a PC, perform keyboard operations.
        Otherwise, perform the action you specified, such as 'Home'.

        Parameters:
            keyname - a string refer to the keys.
        """
        raise NotImplementedError

    def text(self, text, enter=True):
        """
        If the target device is a PC, perform keyboard operations.
        Otherwise, type some text.

        Parameters:
            text - a string refer to the text.
            enter - Whether to enter the Enter key.
        """
        raise NotImplementedError
