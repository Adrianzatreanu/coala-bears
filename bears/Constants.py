import os

#from bears import VERSION

# Path to the bears directory
bears_root = os.path.dirname(__file__)


# Constants to be used for the uploadTool to improve automation

classifiers = """[
              'Development Status :: 4 - Beta',

              'Environment :: Console',
              'Environment :: MacOS X',
              'Environment :: Win32 (MS Windows)',
              'Environment :: X11 Applications :: Gnome',

              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',

              'License :: OSI Approved :: GNU Affero General Public License '
              'v3 or later (AGPLv3+)',

              'Operating System :: OS Independent',

              'Programming Language :: Python :: Implementation :: CPython',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3 :: Only',

              'Topic :: Scientific/Engineering :: Information Analysis',
              'Topic :: Software Development :: Quality Assurance',
              'Topic :: Text Processing :: Linguistic']"""
imports = """
import locale
import sys
from subprocess import call

import setuptools.command.build_py
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand"""

encoding = """try:
    locale.getlocale()
except (ValueError, UnicodeError):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')"""

requirements = """with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()"""
