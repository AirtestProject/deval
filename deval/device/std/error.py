# -*- coding: utf-8 -*-

"""
error classes
"""


class BaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class DevalError(BaseError):
    """
        This is Deval BaseError
    """
    pass


class TargetNotFoundError(DevalError):
    """
        This is TargetNotFoundError BaseError
        When something is not found
    """
    pass


class ScriptParamError(DevalError):
    """
        This is ScriptParamError BaseError
        When something goes wrong
    """
    pass


class DeviceConnectionError(BaseError):
    """
        device connection error
    """
    DEVICE_CONNECTION_ERROR = r"error:\s*((device \'\w+\' not found)|(cannot connect to daemon at [\w\:\s\.]+ Connection timed out))"
    pass


class PerformanceError(BaseError):
    pass
