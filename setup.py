#!/usr/bin/env python

from distutils.core import setup

setup(name='psn',
      version='1.0',
      description='Simple library to access status of friends on PSN',
      author='Thomas Achtemichuk',
      author_email='tom@tomchuk.com',
      url='http://github.com/tomchuk/psn',
      packages=['psn'],
      package_dir={'psn': 'src/psn'},
      package_data={'psn': ['templates/*']},
     )
