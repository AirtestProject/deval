# -*- coding: utf-8 -*-


class Component(object):
    def __init__(self, uri, dev, name):
        self.name = name  # com的名字，预定义的com可不填名字，自定义的com需自己定义名字
        self.uri = uri  # com对应的device的uri，唯一标识一个设备
        self.dev = dev  # com对应的设备
    
    @property
    def Name(self):
        return self.name
