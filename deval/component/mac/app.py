# -*- coding: utf-8 -*-

import os
from deval.component.std.app import AppComponent


class MacAppComponent(AppComponent):
    
    def __init__(self, name):
        self.name = name

    def start(self, path, **kwargs):
        """
        Use the console command to start a program

        Parameters:
            path - the command
        """
        os.system("open %s" % path)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
