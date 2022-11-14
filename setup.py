# Copyright (c) 2017-2022 Slang Labs Private Limited. All rights reserved.

import datetime
import os

from setuptools import find_packages, setup


def timestamp():
    return datetime.datetime.today().strftime('%Y%m%d%H%M%S')


def git_version():
    from subprocess import PIPE, Popen
    gitproc = Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE)
    (stdout, _) = gitproc.communicate()
    return stdout.strip().decode('utf-8')[0:7]


__version_num__ = "0.0.1"
__version__ = __version_num__ + "+build." + timestamp() + "." + git_version()

__license__ = """(c) 2017 Copyright, Slang Labs Private Limited.
                 All rights reserved."""


with open("README.md", 'r') as f:
    __description__ = f.readline().strip()
    __long_description__ = __description__ + os.linesep + f.read().strip()


setup(
    name='Slang Labs NLU',
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=__long_description__,
    packages=find_packages(),
    url='http://slanglabs.in',
    author='Slang Labs',
    author_email='support@slanglabs.in',
    zip_safe=False
)
