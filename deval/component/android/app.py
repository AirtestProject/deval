# -*- coding: utf-8 -*-

from deval.component.std.app import AppComponent
from deval.utils.parse import parse_uri
from deval.utils.android.androidfuncs import _check_platform_android


class AndroidAppComponent(AppComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb  # 获取设备的数据

    def start_app(self, package, activity=None):
        return self.adb.start_app(package, activity)

    def start_app_timing(self, package, activity=None):
        return self.adb.start_app_timing(package, activity)

    def stop_app(self, package):
        return self.adb.stop_app(package)

    def clear_app(self, package):
        return self.adb.clear_app(package)

    def install_app(self, filepath, replace=False):
        return self.adb.install_app(filepath, replace=replace)

    def install_multiple_app(self, filepath, replace=False):
        return self.adb.install_multiple_app(filepath, replace=replace)

    def uninstall_app(self, package):
        return self.adb.uninstall_app(package)

    def list_app(self, third_only=False):
        return self.adb.list_app(third_only)

    def path_app(self, package):
        return self.adb.path_app(package)

    def check_app(self, package):
        return self.adb.check_app(package)
