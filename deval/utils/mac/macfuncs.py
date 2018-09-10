# -*- coding: utf-8 -*-

from deval.utils.parse import parse_uri


def _check_platform_mac(uri, platform="mac"):
    """
    Check the uri and return a dictionary containing the various parameters contained in the uri.

    Parameters:
        uri - an URI where to connect to device, e.g. `mac:///`

    Returns:
        A dictionary containing the various parameters contained in the uri.

    Raises:
        RuntimeError - raise when the platform does not match the uri.
    """
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    params.pop("platform")
    if "uuid" in params:
        params.pop("uuid")
    return params


# 由于pyatomac这个库不稳定，暂时不提供get_window和坐标转换函数
# 若要实现，参考poco mac SDK
