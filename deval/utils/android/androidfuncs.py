#! /usr/bin/env python
# -*- coding: utf-8 -*-

from deval.utils.parse import parse_uri


def _check_platform_android(uri, platform="android"):
    params = parse_uri(uri)
    if params["platform"] != platform:
        raise RuntimeError("Platform error!")
    if "uuid" in params:
        params["serialno"] = params["uuid"]
        params.pop("uuid")
    params.pop("platform")
    return params

