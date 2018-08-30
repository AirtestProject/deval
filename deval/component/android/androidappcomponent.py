# -*- coding: utf-8 -*-

from deval.component.std.appcomponent import AppComponent
from deval.utils.parse import parse_uri
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android


class AndroidAppComponent(AppComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidAppComponent, self).__init__(uri, dev, name)
        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def start_app(self, package, activity=None, **kwargs):
        return self.proxy.adb.start_app(package, activity)

    def start_app_timing(self, package, activity=None, **kwargs):
        return self.proxy.adb.start_app_timing(package, activity)

    def stop_app(self, package, **kwargs):
        return self.proxy.adb.stop_app(package)

    def clear_app(self, package, **kwargs):
        return self.proxy.adb.clear_app(package)

    def install_app(self, filepath, replace=False, **kwargs):
        return self.proxy.adb.install_app(filepath, replace=replace)

    def install_multiple_app(self, filepath, replace=False, **kwargs):
        return self.proxy.adb.install_multiple_app(filepath, replace=replace)

    def uninstall_app(self, package, **kwargs):
        return self.proxy.adb.uninstall_app(package)

    def list_app(self, third_only=False, **kwargs):
        return self.proxy.adb.list_app(third_only)

    def path_app(self, package, **kwargs):
        return self.proxy.adb.path_app(package)

    def check_app(self, package, **kwargs):
        return self.proxy.adb.check_app(package)
