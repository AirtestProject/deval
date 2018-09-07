# -*- coding: utf-8 -*-

from deval.utils.parse import parse_uri


def _check_platform_mac(uri, platform="mac"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    params.pop("platform")
    if "uuid" in params:
        params.pop("uuid")
    return params


# 由于pyatomac这个库不稳定，暂时不提供get_window和坐标转换函数
# 若要实现，参考poco mac SDK
