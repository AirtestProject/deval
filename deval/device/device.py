# -*- coding: utf-8 -*-


class BaseDevice(object):
    
    def __init__(self):
        self.ComponentList = dict()

    def addComponent(self, com):
        if com.com_name in self.ComponentList:
            raise RuntimeError("Duplicate component, please check component name")
        else:
            self.ComponentList[com.com_name] = com
            
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

    def click(self, *args, **kwargs):
        return self.inputComponent.click(*args, **kwargs)

    def tap(self, *args, **kwargs):
        return self.click(*args, **kwargs)

    def swipe(self, *args, **kwargs):
        return self.inputComponent.swipe(*args, **kwargs)

    def double_tap(self, *args, **kwargs):
        return self.inputComponent.double_tap(*args, **kwargs)

    def keyevent(self, *args, **kwargs):
        return self.keyeventComponent.keyevent(*args, **kwargs)
    
    def text(self, *args, **kwargs):
        return self.keyeventComponent.text(*args, **kwargs)

    def shell(self, *args, **kwargs):
        return self.runtimeComponent.shell(*args, **kwargs)

    def start_app(self, *args, **kwargs):
        return self.appComponent.start_app(*args, **kwargs)

    def stop_app(self, *args, **kwargs):
        return self.appComponent.stop_app(*args, **kwargs)

    def snapshot(self, *args, **kwargs):
        return self.screenComponent.snapshot(*args, **kwargs)

    def get_ip_address(self, *args, **kwargs):
        return self.networkComponent.get_ip_address(*args, **kwargs)

    
    

    


    
    
