DEVAL
=====

Device abstraction layer for multi-platform devices. Android, Windows, iOS, mac OS X, Ubuntu, other virtual devices, etc.


Usage
-----


Windows
=======

.. code-block:: python

    from deval.device.win.win import WinDevice
    dev = WinDevice("windows:///?title_re=无标题")  # Connect to a specific window
    print(dev.uuid)
    dev.input_component.scroll((100, 100), steps=2, duration=5)
    dev.click((100, 100))
    dev.swipe((100, 100), (200, 200), duration=1)
    print(dev.shell("Python -V"))
    dev.snapshot("D:/c.jpg")
    dev.keyevent("xxx")
    dev.get_component("keyevent").text("111")
    dev.double_tap((10, 10))
    dev.start_app("notepad")
    print(dev.app_component.get_title())
    print(dev.get_ip_address())
    dev.stop_app()


Android
=======

.. code-block:: python

    from deval.device.android import AndroidDevice
    dev = AndroidDevice("android:///127.0.0.1:62001?cap_method=javacap&touch_method=minitouch")
    print(dev.uuid)
    dev.keyevent("d")
    dev.keyevent_component.home()
    dev.click((500, 500))
    dev.keyevent_component.home()
    dev.double_tap((500, 500))
    dev.keyevent_component.home()
    dev.swipe((100, 100), (500, 500), duration=1)
    dev.keyevent_component.wake()
    dev.start_app('com.netease.nie.yosemite')
    dev.stop_app('com.netease.nie.yosemite')
    dev.app_component.clear('com.netease.nie.yosemite')
    dev.get_component("screen").snapshot("D:/a.jpg")
    print(dev.get_component("screen").is_screenon())
    print(dev.get_component("screen").is_locked())
    print(dev.app_component.list())


Linux
=====

.. code-block:: python

    from deval.device.linux.linux import LinuxDevice
    dev = LinuxDevice("linux:///")  # Connect to the entire desktop
    dev.click((100, 100))
    dev.swipe((100, 100), (200, 200), duration=5)
    print(dev.shell("Python -V"))
    dev.snapshot()
    dev.keyevent("xxx")
    dev.text("111")
    dev.double_tap((100, 100))
    print(dev.get_ip_address())


Mac
===

.. code-block:: python

    from deval.device.mac.mac import MacDevice
    dev = MacDevice("mac:///")  # Connect to the entire desktop
    dev.click((100, 100))
    dev.swipe((100, 100), (200, 200), duration=5)
    dev.snapshot()
    dev.keyevent("xxx")
    dev.text("111")
    dev.double_tap((100, 100))
    print(dev.get_ip_address())


Customize your device
----------------------

You can easily customize your own device, here we use the Android simulator as an example

1. Inherit DeviceBase, write your own device
#. Add the components you need
#. Start testing your device


Here is an example to define your device

.. code-block:: python

    # -*- coding: utf-8 -*-

    from deval.device.std.device import DeviceBase
    from deval.component.android.app import AndroidAppComponent
    from deval.component.android.screen import AndroidADBScreenComponent
    from deval.component.android.input import AndroidADBTouchInputComponent
    from deval.component.win.input import WinInputComponent
    from deval.component.win.screen import WinScreenComponent
    from deval.utils.parse import parse_uri
    from deval.component.android.utils.adb import ADB
    from deval.component.win.utils.winfuncs import check_platform_win, get_app, get_window

    # use parse_uri to parse your uri
    def check_platform_mumu(uri, platform="mumu"):
        params = parse_uri(uri)
        if params["platform"] != platform:
            raise RuntimeError("Platform error!")
        if "uuid" in params:
            params["serialno"] = params["uuid"]
            params.pop("uuid")
        params.pop("platform")
        return params


    class MumuDevice(DeviceBase):

        def __init__(self, uri):
            super(MumuDevice, self).__init__(uri)
            # First you have to connect to your Android emulator window in windows platform
            winuri = "windows:///123456"

            # Initialize the parameters required to operate Android Device
            self.kw = check_platform_mumu(uri)
            self.serialno = self.kw.get("serialno")
            self.adb = ADB(self.serialno, server_addr=self.kw.get("host"))

            # Initialize the parameters required to operate Windows Device
            self.app = get_app(check_platform_win(winuri))
            self.window = get_window(check_platform_win(winuri))
            self.handle = self.window.handle

            # Use android app component
            self.add_component(AndroidAppComponent("app", self))
            # Use android screen component as default
            self.add_component(AndroidADBScreenComponent("screen", self))
            # Use android input component as default
            self.add_component(AndroidADBTouchInputComponent("input", self))
            # add windows input component
            self.add_component(WinInputComponent("wininput", self, winuri))
            # add windows screen component
            self.add_component(WinScreenComponent("winscreen", self, winuri))


Now, you can test your device

.. code-block:: python

    from deval.device.mumu.mumu import MumuDevice
    dev = MumuDevice("mumu:///127.0.0.1:62001")
    dev.click((500, 500))  # use default input component to click
    dev.get_component("winscreen").snapshot("D:/windows.jpg")  # use windows screen component to cut a photo of the simulator window
    dev.screen_component.snapshot("D:/android.jpg")  # use default screen component to cut a photo of the android system in simulator
