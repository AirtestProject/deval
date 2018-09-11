# -*- coding: utf-8 -*-

import re
from deval.component.std.runtime import RuntimeComponent
from deval.utils.android.androidfuncs import _check_platform_android
from deval.utils.parse import parse_uri


class AndroidRuntimeComponent(RuntimeComponent):

    def __init__(self, name, dev, uri):
        self.set_attribute(name, dev, uri)

        self.adb = self.dev.adb

    def shell(self, cmd):
        return self.adb.shell(cmd)

    def get_top_activity_name_and_pid(self):
        dat = self.adb.shell('dumpsys activity top')
        activityRE = re.compile(
            '\s*ACTIVITY ([A-Za-z0-9_.]+)/([A-Za-z0-9_.]+) \w+ pid=(\d+)')
        m = activityRE.search(dat)
        if m:
            return (m.group(1), m.group(2), m.group(3))
        else:
            return None

    def get_top_activity_name(self):
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
