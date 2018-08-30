# -*- coding: utf-8 -*-


class BaseDevice(object):
    
    def __init__(self):
        self.ComponentList = dict()

    def addComponent(self, com):
        if com.Name in self.ComponentList:
            raise RuntimeError("Duplicate component, please check component name")
        else:
            self.ComponentList[com.Name] = com
            
    def getComponent(self, name):
        if name in self.ComponentList:
            return self.ComponentList.get(name)
        else:
            raise RuntimeError("No such component!")

    def removeComponent(self, comName):
        if comName in self.ComponentList:
            self.ComponentList.pop(comName)
            return True
        return False

    @property
    def inputComponent(self):
        return self.getComponent("input")

    @property
    def keyeventComponent(self):
        return self.getComponent("keyevent")

    @property
    def runtimeComponent(self):
        return self.getComponent("runtime")

    @property
    def appComponent(self):
        return self.getComponent("app")
    
    @property
    def screenComponent(self):
        return self.getComponent("screen")

    @property
    def networkComponent(self):
        return self.getComponent("network")

    # useful functions

    def click(self, pos, **kwargs):
        return self.inputComponent.click(pos, **kwargs)

    def tap(self, pos, **kwargs):
        return self.click(pos, **kwargs)

    def swipe(self, p1, p2, **kwargs):
        return self.inputComponent.swipe(p1, p2, **kwargs)

    def double_tap(self, pos, **kwargs):
        return self.inputComponent.double_tap(pos, **kwargs)

    def keyevent(self, keyname, **kwargs):
        return self.keyeventComponent.keyevent(keyname, **kwargs)
    
    def text(self, text, **kwargs):
        return self.keyeventComponent.text(text, **kwargs)

    def shell(self, *args, **kwargs):
        return self.runtimeComponent.shell(*args, **kwargs)

    def start_app(self, package, activity=None, **kwargs):
        return self.appComponent.start_app(package, activity=None, **kwargs)

    def stop_app(self, package=None, **kwargs):
        return self.appComponent.stop_app(package, **kwargs)

    def snapshot(self, filename="tmp.jpg", **kwargs):
        return self.screenComponent.snapshot(filename, **kwargs)

    def get_ip_address(self, *args, **kwargs):
        return self.networkComponent.get_ip_address(*args, **kwargs)
