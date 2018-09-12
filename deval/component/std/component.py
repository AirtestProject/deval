# -*- coding: utf-8 -*-


class Component(object):
    @property
    def name(self):
        raise NotImplementedError
    
    @name.setter
    def name(self, value):
        raise NotImplementedError
