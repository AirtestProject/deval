# -*- coding: utf-8 -*-

from six.moves.urllib.parse import parse_qsl, urlparse


def parse_uri(uri):
    """
    Initialize device with uri, and set as current device.

    :param uri: an URI where to connect to device, e.g. `android://adbhost:adbport/serialno?param=value&param2=value2`
    :return: device instance
    :Example:
        * ``android:///`` # local adb device using default params
        * ``android://adbhost:adbport/1234566?cap_method=javacap&touch_method=adb``  # remote device using custom params
        * ``windows:///`` # local Windows application
        * ``ios:///`` # iOS device
    """
    d = urlparse(uri)
    platform = d.scheme
    host = d.netloc
    uuid = d.path.lstrip("/")
    params = dict(parse_qsl(d.query))
    if host:
        params["host"] = host.split(":")
    params["platform"] = platform.lower()
    params["uuid"] = uuid
    return params

    
