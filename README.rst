DEVAL
+++++

Device abstraction layer for multi-platform devices. Android, Windows, iOS, mac OS X, Ubuntu, other virtual devices, etc.


Usage
-----


Windows
=======

.. code-block:: python

    dev = WinDevice("/?title_re=无标题")  # Connect to a specific window
    print(dev.uuid)
    dev.input.scroll((100, 100), steps=2, duration=5)
    dev.click((100, 100))
    dev.swipe((100, 100), (200, 200), duration=1)
    print(dev.shell("Python -V"))
    dev.snapshot("D:/c.jpg")
    dev.keyevent("xxx")
    dev.get_component("keyevent").text("111")
    # dev.screenComponent.move((10, 10))
    dev.double_tap((10, 10))
    dev.start_app("notepad")
    print(dev.app.get_title())
    print(dev.get_ip_address())
    dev.stop_app()


Android
=======

.. code-block:: python

    from deval.device.android import AndroidDevice
    dev = AndroidDevice("/127.0.0.1:62001?cap_method=javacap&touch_method=minitouch")
    print(dev.uuid)
    dev.keyevent("d")
    dev.keyevent.home()
    dev.click((500, 500))
    dev.keyevent.home()
    dev.double_tap((500, 500))
    dev.keyevent.home()
    dev.swipe((100, 100), (500, 500), duration=1)
    dev.keyevent.wake()
    dev.start_app('com.netease.nie.yosemite')
    dev.stop_app('com.netease.nie.yosemite')
    dev.app.clear('com.netease.nie.yosemite')
    dev.get_component("screen").snapshot("D:/a.jpg")
    print(dev.get_component("screen").is_screenon())
    print(dev.get_component("screen").is_locked())
    print(dev.app.list())


Linux
=====

.. code-block:: python

    from deval.device.linux.linux import LinuxDevice
    dev = LinuxDevice()  # Connect to the entire desktop
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
    dev = MacDevice()  # Connect to the entire desktop
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

    from deval.device.std.device import DeviceBase
    from deval.component.android.app import AndroidAppComponent
    from deval.component.android.screen import AndroidADBScreenComponent
    from deval.component.android.input import AndroidADBTouchInputComponent
    from deval.component.win.input import WinInputComponent
    from deval.component.win.screen import WinScreenComponent
    from deval.utils.parse import parse_uri
    from deval.component.android.utils.adb import ADB
    from deval.component.win.utils.winfuncs import get_app, get_window


    class MumuDevice(DeviceBase):

        def __init__(self, uri):
            super(MumuDevice, self).__init__(uri)

            # Initialize the parameters required to operate Android Device
            self.kw = parse_uri(uri)
            self.serialno = self.kw.get("serialno")
            self.adb = ADB(self.serialno, server_addr=self.kw.get("host"))

            # Initialize the parameters required to operate Windows Device
            self.application = get_app(uri)
            self.window = get_window(uri)
            self.handle = self.window.handle

            # Use android app component
            self.add_component(AndroidAppComponent("app", self))
            # Use android screen component as default
            self.add_component(AndroidADBScreenComponent("screen", self))
            # Use android input component as default
            self.add_component(AndroidADBTouchInputComponent("input", self))
            # add windows input component
            self.add_component(WinInputComponent("wininput", self, uri))
            # add windows screen component
            self.add_component(WinScreenComponent("winscreen", self, uri))


Now, you can test your device

.. code-block:: python

    from deval.device.mumu.mumu import MumuDevice
    dev = MumuDevice("/?serialno=127.0.0.1:62001&handle=123456")
    dev.click((500, 500))  # use default input component to click
    dev.get_component("winscreen").snapshot("D:/windows.jpg")  # use windows screen component to cut a photo of the simulator window
    dev.screen.snapshot("D:/android.jpg")  # use default screen component to cut a photo of the android system in simulator
