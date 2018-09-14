# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class KeyEventComponent(Component):

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

    def __call__(self, keyname):
        return self.keyevent(keyname)
