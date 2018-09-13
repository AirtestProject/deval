# -*- coding: utf-8 -*-

from deval.component.std.app import AppComponent
from deval.utils.parse import parse_uri
from deval.utils.android.androidfuncs import _check_platform_android


class AndroidAppComponent(AppComponent):

    def __init__(self, name, dev):
        self._name = name
        self.adb = dev.adb  # 获取设备的数据

    def start(self, package, activity=None):
        return self.adb.start_app(package, activity)

    def stop(self, package):
        return self.adb.stop_app(package)

    def clear(self, package):
        return self.adb.clear_app(package)

    def install(self, filepath, replace=False):
        return self.adb.install_app(filepath, replace=replace)

    def uninstall(self, package):
        return self.adb.uninstall_app(package)

    def list(self, third_only=False):
        return self.adb.list_app(third_only)

    def get_install_path(self, package):
        return self.adb.path_app(package)

    def exists(self, package):
        return self.adb.check_app(package)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
