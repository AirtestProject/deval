# -*- coding: utf-8 -*-


class Component(object):
    def __init__(self, uri, dev, name):
        self.com_name = name
        self.uri = uri
        self.dev = dev


class InputComponent(Component):
    def __init__(self, uri, dev=None, name="input"):
        super(InputComponent, self).__init__(uri, dev, name)
    
    def click(self, *args, **kwargs):
        raise NotImplementedError

    def swipe(self, *args, **kwargs):
        raise NotImplementedError

    def pinch(self, *args, **kwargs):
        raise NotImplementedError

    def double_tap(self, *args, **kwargs):
        raise NotImplementedError


class KeyEventComponent(Component):
    def __init__(self, uri, dev=None, name="keyevent"):
        super(KeyEventComponent, self).__init__(uri, dev, name)
    
    def keyevent(self, *args, **kwargs):
        raise NotImplementedError

    def text(self, *args, **kwargs):
        raise NotImplementedError

    def wake(self, *args, **kwargs):
        raise NotImplementedError

    def home(self, *args, **kwargs):
        raise NotImplementedError


class RuntimeComponent(Component):
    def __init__(self, uri, dev=None, name="runtime"):
        super(RuntimeComponent, self).__init__(uri, dev, name)
    
    def shell(self, *args, **kwargs):
        raise NotImplementedError

    def kill(self, *args, **kwargs):
        raise NotImplementedError


class AppComponent(Component):
    def __init__(self, uri, dev=None, name="app"):
        super(AppComponent, self).__init__(uri, dev, name)
    
    def start_app(self, *args, **kwargs):
        raise NotImplementedError

    def stop_app(self, *args, **kwargs):
        raise NotImplementedError

    def install(self, *args, **kwargs):
        raise NotImplementedError

    def uninstall(self, *args, **kwargs):
        raise NotImplementedError

    def start_app_timing(self, *args, **kwargs):
        raise NotImplementedError

    def clear_app(self, *args, **kwargs):
        raise NotImplementedError

    def install_app(self, *args, **kwargs):
        raise NotImplementedError

    def install_multiple_app(self, *args, **kwargs):
        raise NotImplementedError

    def uninstall_app(self, *args, **kwargs):
        raise NotImplementedError

    def list_app(self, *args, **kwargs):
        raise NotImplementedError

    def path_app(self, *args, **kwargs):
        raise NotImplementedError

    def check_app(self, *args, **kwargs):
        raise NotImplementedError


class ScreenComponent(Component):
    def __init__(self, uri, dev=None, name="screen"):
        super(ScreenComponent, self).__init__(uri, dev, name)
    
    def snapshot(self, *args, **kwargs):
        raise NotImplementedError

    def move(self, *args, **kwargs):
        raise NotImplementedError


class GetterComponent(Component):
    def __init__(self, uri, dev=None, name="getter"):
        super(GetterComponent, self).__init__(uri, dev, name)
    
    def get_ip_address(self, *args, **kwargs):
        raise NotImplementedError

    def get_title(self, *args, **kwargs):
        raise NotImplementedError
