#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'aiohttp'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    version='0.0.1',
    author="Nat Burns",
    author_email='nbaccount@burnskids.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Python wrapper for Polar Web API.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='polar_web',
    name='polar_web',
    packages=find_packages(exclude=['tests']),
    setup_requires=setup_requirements,
    url='https://github.com/burnnat/polar_web',
    zip_safe=False,
)
