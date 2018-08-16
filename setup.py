import sys
from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


reqs = parse_requirements('requirements.txt')
if sys.platform == "win32":
    reqs.append('pywin32')


setup(
    name='deval',
    version='1.0.0',
    author='Netease Games',
    author_email='lxn3032@corp.netease.com',
    description='Device abstraction layer for multi-platform devices. Android, Windows, iOS, mac OS X, Ubuntu, other virtual devices, etc.',
    long_description='Device abstraction layer for multi-platform devices. Android, Windows, iOS, mac OS X, Ubuntu, other virtual devices, present by NetEase Games',
    url='https://github.com/AirtestProject/deval',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
