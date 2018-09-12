# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class AppComponent(Component):

    def start(self, package, activity=None):
        """
        Start a program based on the given path or package name

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def stop(self, package):
        """
        Stop a program based on the package name or just close the current app.

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def clear(self, package):
        """
        Clear a program data based on the given path or package name

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def install(self, filepath, replace=False):
        """
        Install an application based on the package name.

        Parameters:
            filepath - the path or the package name.
            replace - Whether to overwrite the previous application
        """
        raise NotImplementedError

    def uninstall(self, package):
        """
        Uninstall an application based on the package name.

        Parameters:
            filepath - the path or the package name.
            replace - Whether to overwrite the previous application
        """
        raise NotImplementedError

    def list(self, third_only=False):
        """
        list all installed application in the device.
        """
        raise NotImplementedError

    def get_install_path(self, package):
        """
        Get the installation path based on the application name

        Parameters:
            package - the application name or the package name.

        Returns:
            A string represent the path
        """
        raise NotImplementedError

    def exists(self, package):
        """
        Check whether the application exists

        Parameters:
            package - the application name or the package name.

        Returns:
            True or False
        """
        raise NotImplementedError

    def get_title(self):
        """
        Get the application title

        Returns:
            A string represent the title
        """
        raise NotImplementedError

