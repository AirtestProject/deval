# -*- coding: utf-8 -*-

from deval.utils.parse import parse_uri


def _check_platform_linux(uri, platform="linux"):
    """
    Check the uri and return a dictionary containing the various parameters contained in the uri.

    Parameters:
        uri - an URI where to connect to device, e.g. `linux:///`

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
        pid = params["uuid"]
        if pid != '':
            params["pid"] = int(pid)
        params.pop("uuid")
    return params

