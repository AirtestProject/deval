# -*- coding: utf-8 -*-

import types

_method_str = u'''
def %s(self, *args, **kwargs):
    if "%s" in self.ComponentList:
        return self.ComponentList["%s"].%s(*args, **kwargs)
    else:
        raise RuntimeError("No such component to perform %s function")
self.__dict__[funcname] = types.MethodType(%s, self)
'''


class BaseDevice(object):
    
    def __init__(self):
        self.ComponentList = dict()

        self.addMethodInComponent("click", "input")
        self.tap = self.click
        self.addMethodInComponent("swipe", "input")
        self.addMethodInComponent("pinch", "input")
        self.addMethodInComponent("double_tap", "input")
        self.addMethodInComponent("scroll", "input")
        self.addMethodInComponent("keyevent", "keyevent")
        self.addMethodInComponent("text", "keyevent")
        self.addMethodInComponent("wake", "keyevent")
        self.addMethodInComponent("home", "keyevent")
        self.addMethodInComponent("shell", "runtime")
        self.addMethodInComponent("kill", "runtime")
        self.addMethodInComponent("start_app", "app")
        self.addMethodInComponent("stop_app", "app")
        self.addMethodInComponent("install", "app")
        self.addMethodInComponent("uninstall", "app")
        self.addMethodInComponent("start_app_timing", "app")
        self.addMethodInComponent("clear_app", "app")
        self.addMethodInComponent("install_app", "app")
        self.addMethodInComponent("install_multiple_app", "app")
        self.addMethodInComponent("uninstall_app", "app")
        self.addMethodInComponent("list_app", "app")
        self.addMethodInComponent("path_app", "app")
        self.addMethodInComponent("check_app", "app")
        self.addMethodInComponent("snapshot", "screen")
        self.addMethodInComponent("move", "screen")
        self.addMethodInComponent("get_current_resolution", "screen")
        self.addMethodInComponent("get_ip_address", "getter")
        self.addMethodInComponent("get_title", "getter")
           
    def addComponent(self, com):
        self.ComponentList[com.com_name] = com

    def getComponent(self, name):
        return self.ComponentList.get(name)

    def addMethodInComponent(self, funcname, comname):
        exec(_method_str % (funcname, comname, comname, funcname, funcname, funcname))
