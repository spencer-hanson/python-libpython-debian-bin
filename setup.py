#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='python-libpython-debian-bin',
      description='Libraries for Python on debian',
      author='Spencer Hanson',
      url="http://github.com/spencer-hanson/python-libpython-debian-bin",
      version='0.0.2',
      package_data={
          'libpython': ['*.so*']
      },
      zip_safe=False,
      packages=['libpython'],
      long_description="""Libraries for Python on debian""",
      keywords="libpython"
      )
