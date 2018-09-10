# -*- coding: utf-8 -*-

from deval.component.std.component import Component


class AppComponent(Component):
    def __init__(self, uri, dev=None, name="app"):
        if name is None:
            super(AppComponent, self).__init__(uri, dev, "app")
        else:
            super(AppComponent, self).__init__(uri, dev, name)

    def start_app(self, package, activity=None):
        """
        Start a program based on the given path or package name

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def stop_app(self, package):
        """
        Stop a program based on the package name or just close the current app.

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def install(self, filepath):
        """
        Install a program based on the package name.

        Parameters:
            filepath - the path or the package name.
        """
        raise NotImplementedError

    def uninstall(self, package):
        """
        Uninstall a program based on the package name.

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def start_app_timing(self, package, activity=None):
        """
        Start a program based on the given path or package name, and calculate startup time

        Parameters:
            package - the path or the package name.

        Returns:
            The time in second
        """
        raise NotImplementedError

    def clear_app(self, package):
        """
        Clear a program data based on the given path or package name

        Parameters:
            package - the path or the package name.
        """
        raise NotImplementedError

    def install_app(self, filepath, replace=False):
        """
        Install an application based on the package name.

        Parameters:
            filepath - the path or the package name.
            replace - Whether to overwrite the previous application
        """
        raise NotImplementedError

    def install_multiple_app(self, filepath, replace=False):
        raise NotImplementedError

    def uninstall_app(self, package):
        """
        Uninstall an application based on the package name.

        Parameters:
            filepath - the path or the package name.
            replace - Whether to overwrite the previous application
        """
        raise NotImplementedError

    def list_app(self, third_only=False):
        """
        Uninstall an application based on the package name.

        Parameters:
            filepath - the path or the package name.
            replace - Whether to overwrite the previous application
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
        Get the installation path based on the application name

        Parameters:
            package - the application name or the package name.

        Returns:
            A string represent the path
        """
        raise NotImplementedError

    def get_title(self):
        """
        Get the application name

        Returns:
            A string represent the name
        """
        raise NotImplementedError
