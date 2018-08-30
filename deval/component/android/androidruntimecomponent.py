# -*- coding: utf-8 -*-

import re
from deval.component.std.runtimecomponent import RuntimeComponent
from deval.utils.android.androidfuncs import AndroidProxy, _check_platform_android
from deval.utils.parse import parse_uri


class AndroidRuntimeComponent(RuntimeComponent):
    
    def __init__(self, uri, dev, name=None):
        super(AndroidRuntimeComponent, self).__init__(uri, dev, name)

        try:
            self.proxy = self.dev.androidproxy
        except AttributeError:
            self.dev.androidproxy = AndroidProxy(**_check_platform_android(uri))
            self.proxy = self.dev.androidproxy

    def shell(self, *args, **kwargs):
        return self.proxy.adb.shell(*args, **kwargs)

    def get_top_activity_name_and_pid(self, **kwargs):
        dat = self.proxy.adb.shell('dumpsys activity top')
        activityRE = re.compile('\s*ACTIVITY ([A-Za-z0-9_.]+)/([A-Za-z0-9_.]+) \w+ pid=(\d+)')
        m = activityRE.search(dat)
        if m:
            return (m.group(1), m.group(2), m.group(3))
        else:
            return None

    def get_top_activity_name(self, **kwargs):
        """
        Get the top activity name

        Returns:
            package, activity and pid

        """
        tanp = self.get_top_activity_name_and_pid()
        if tanp:
            return tanp[0] + '/' + tanp[1]
        else:
            return None
