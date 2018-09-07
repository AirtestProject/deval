# -*- coding: utf-8 -*-


class BaseDevice(object):

    def __init__(self):
        self.ComponentList = dict()

    def addComponent(self, com):
        if com.name in self.ComponentList:
            raise RuntimeError(
                "Duplicate component, please check component name")
        else:
            self.ComponentList[com.name] = com

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

    # useful events

    def click(self, pos, duration=0.05, button='left'):
        """
        Win&Linux下可选参数：
            duration: 点击时长
            button: 点击的按钮（"left", "right", "middle"）
        """
        return self.inputComponent.click(pos, duration, button)

    def rclick(self, pos, duration=0.05, button='right'):
        return self.inputComponent.click(pos, duration, button)

    def long_click(self, pos, duration=2, button='left'):
        return self.inputComponent.click(pos, duration, button)

    def tap(self, pos, duration=0.05):
        return self.click(pos, duration, 'left')

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        """
        Win&Linux可选参数：
            duration: 完成swipe动作所需时长
            button: swipe使用的按钮（"left", "right", "middle"）
            steps: swipe中间的次数
        """
        return self.inputComponent.swipe(p1, p2, duration, steps, fingers, button)

    def double_tap(self, pos, button='left'):
        """
        Win&Linux下可选参数：
            button: 点击的按钮（"left", "right", "middle"）
        """
        return self.inputComponent.double_tap(pos, button)

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        return self.inputComponent.scroll(pos, direction, duration, steps)

    def keyevent(self, keyname):
        return self.keyeventComponent.keyevent(keyname)

    def text(self, text, enter=True):
        return self.keyeventComponent.text(text, enter)

    def shell(self, cmd):
        return self.runtimeComponent.shell(cmd)

    def start_app(self, package, activity=None):
        return self.appComponent.start_app(package, activity=None)

    def stop_app(self, package=None):
        return self.appComponent.stop_app(package)

    def snapshot(self, filename="tmp.jpg"):
        return self.screenComponent.snapshot(filename)

    def get_ip_address(self):
        return self.networkComponent.get_ip_address()
