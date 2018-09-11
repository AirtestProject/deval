# -*- coding: utf-8 -*-


class Component(object):

    @property
    def name(self):
        try:
            return self._name
        except AttributeError:
            raise AttributeError("Component's attribute 'name' not found! Call 'set_attribute' to set the name of the component")

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def uri(self):
        try:
            return self._uri
        except AttributeError:
            raise AttributeError("Component's attribute 'uri' not found! Call 'set_attribute' to set the uri of the component")

    @uri.setter
    def uri(self, value):
        self._uri = value

    @property
    def dev(self):
        try:
            return self._dev
        except AttributeError:
            raise AttributeError("Component's attribute 'dev' not found! Call 'set_attribute' to set the device of the component")
        return self._dev

    @dev.setter
    def dev(self, value):
        self._dev = value

    def set_attribute(self, name, dev=None, uri=None):
        self._name = name
        self._uri = uri
        self._dev = dev
