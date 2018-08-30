# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class AppComponent(Component):
    def __init__(self, uri, dev=None, name="app"):
        if name is None:
            super(AppComponent, self).__init__(uri, dev, "app")
        else:
            super(AppComponent, self).__init__(uri, dev, name)
    
    def start_app(self, package, activity=None, **kwargs):
        raise NotImplementedError

    def stop_app(self, package, **kwargs):
        raise NotImplementedError

    def install(self, filepath, **kwargs):
        raise NotImplementedError

    def uninstall(self, package, **kwargs):
        raise NotImplementedError

    def start_app_timing(self, package, activity=None, **kwargs):
        raise NotImplementedError

    def clear_app(self, package, **kwargs):
        raise NotImplementedError

    def install_app(self, filepath, replace=False, **kwargs):
        raise NotImplementedError

    def install_multiple_app(self, filepath, replace=False, **kwargs):
        raise NotImplementedError

    def uninstall_app(self, package, **kwargs):
        raise NotImplementedError

    def list_app(self, third_only=False, **kwargs):
        raise NotImplementedError

    def get_install_path(self, package, **kwargs):
        raise NotImplementedError

    def exists(self, package, **kwargs):
        raise NotImplementedError

    def get_title(self, *args, **kwargs):
        raise NotImplementedError
