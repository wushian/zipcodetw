#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

import zipcodetw.builder

class zipcodetw_install(install):

    def run(self):
        print 'Building ZIP code index ... '
        sys.stdout.flush()
        zipcodetw.builder.build_index_from_chp_csv('201311.csv')
        install.run(self)

import zipcodetw

setup(

    name = 'zipcodetw',
    version = zipcodetw.__version__,
    description = 'Find Taiwan ZIP code by address fuzzily.',
    long_description = open('README.rst').read(),

    author = 'Mosky',
    url = 'https://github.com/moskytw/zipcodetw',
    author_email = 'mosky.tw@gmail.com',
    license = 'MIT',
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages = find_packages(),
    package_data = {'zipcodetw': ['*.csv', '*.db']},

    cmdclass = {'install': zipcodetw_install},

)

