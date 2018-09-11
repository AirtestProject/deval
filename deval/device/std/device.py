# -*- coding: utf-8 -*-


class BaseDevice(object):

    def __init__(self, uri):
        """
        Initialize the device via Uri

        Parameters:
            uri - the uri to uniquely identify a device
        """
        self.uri = uri
        self.ComponentList = dict()

    def addComponent(self, com):
        """
        Add the component into the device

        Parameters:
            com - the component

        Raises:
            RuntimeError - raise when the component is Duplicated
        """
        if com.name in self.ComponentList:
            raise RuntimeError(
                "Duplicate component, please check component name")
        else:
            self.ComponentList[com.name] = com

    def getComponent(self, name):
        """
        Get the component according to the given name

        Parameters:
            name - the name

        Returns:
            The component, return None if not found.
        """
        if name in self.ComponentList:
            return self.ComponentList.get(name)
        else:
            raise RuntimeError("No such component!")

    def removeComponent(self, comName):
        """
        Remove the component according to the given name

        Parameters:
            name - the name

        Returns:
            Returns True if successful, otherwise returns False
        """
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

    # some useful apis

    def click(self, pos, duration=0.05, button='left'):
        """
        This is a click functhion. It has different implementations on different devices.
        For specific implementation, please refer to the input component of each devices.

        Parameters:
            pos - a list refer to the click position. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.click(pos, duration, button)

    def rclick(self, pos, duration=0.05, button='right'):
        """
        This is a right-click functhion. Only the PC platform supports right-click operation.

        Parameters:
            pos - a list refer to the right click position. Supported devices: Windows, Linux, Mac
            duration - the duration of the operation. Supported devices: Windows, Linux, Mac
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.click(pos, duration, button)

    def long_click(self, pos, duration=2, button='left'):
        """
        This is a long-click functhion. Only the PC platform supports long-click operation.

        Parameters:
            pos - a list refer to the right click position. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.click(pos, duration, button)

    def tap(self, pos, duration=0.05):
        """
        Click alias
        """
        return self.click(pos, duration, 'left')

    def touch(self, pos, duration=0.05):
        """
        Click alias
        """
        return self.click(pos, duration, 'left')

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        """
        Perform swipe action on target device from point to point given by start point and end point.

        Parameters:
            p1 - a list refer to the start point. Supported devices: All
            p2 - a list refer to the end point. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            steps - the steps of the operation. Supported devices: Android, Linux, Mac, Windows
            fingers - the number of fingers to perform the operation. Supported devices: Android
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.swipe(p1, p2, duration, steps, fingers, button)

    def double_tap(self, pos, button='left'):
        """
        This is a double-tap functhion. Similar to click.

        Parameters:
            pos - a list refer to the double click position. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.double_tap(pos, button)

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        """
        Perform the scroll wheel operation of the middle mouse button.

        Parameters:
            pos - a list refer to the mouse position. Supported devices: Windows, Linux, Mac
            direction - the direction of the operation. Supported devices: Windows, Linux, Mac
            duration - the duration of the operation. Supported devices: Windows, Linux, Mac
            steps - the number of times of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.inputComponent.scroll(pos, direction, duration, steps)

    def keyevent(self, keyname):
        """
        If the target device is a PC, perform keyboard operations.
        Otherwise, perform the action you specified, such as 'Home'.

        Parameters:
            keyname - a string refer to the keys. Supported devices: All
        """
        return self.keyeventComponent.keyevent(keyname)

    def text(self, text, enter=True):
        """
        If the target device is a PC, perform keyboard operations.
        Otherwise, type some text.

        Parameters:
            text - a string refer to the text. Supported devices: All
            enter - Whether to enter the Enter key. Supported devices: Android, IOS
        """
        return self.keyeventComponent.text(text, enter)

    def shell(self, cmd):
        """
        Enter console command

        Parameters:
            cmd - the command. Supported devices: Android, Windows, Linux, Mac
        """
        return self.runtimeComponent.shell(cmd)

    def start_app(self, package, activity=None):
        return self.appComponent.start_app(package, activity=None)

    def stop_app(self, package=None):
        """
        Stop a program based on the package name or just close the current app.

        Parameters:
            package - the path or the package name. Supported devices: Android, Windows, IOS
        """
        return self.appComponent.stop_app(package)

    def snapshot(self, filename="tmp.jpg"):
        """
        Perform a screenshot operation on the current screen.

        Parameters:
            filename - the path to save the image. Supported devices: All
        """
        return self.screenComponent.snapshot(filename)

    def get_ip_address(self):
        """
        Get the current device IP address
        """
        return self.networkComponent.get_ip_address()
