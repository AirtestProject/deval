# -*- coding: utf-8 -*-

import os
from deval.component.std.app import AppComponent


class MacAppComponent(AppComponent):
    
    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

    def start_app(self, path, **kwargs):
        """
        Use the console command to start a program

        Parameters:
            path - the command
        """
        os.system("open %s" % path)
