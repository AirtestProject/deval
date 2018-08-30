# -*- coding: utf-8 -*-

from deval.utils.parse import parse_uri


def _check_platform_linux(uri, platform="linux"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    params.pop("platform")
    if "uuid" in params:
        pid = params["uuid"]
        if pid != '':
            params["pid"] = int(pid)
        params.pop("uuid")
    return params

